#!/usr/bin/env python3
"""Fetch and freeze World Bank WDI data; standard library only."""
import concurrent.futures, csv, datetime, json, pathlib, time, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
COUNTRIES = 'CHN;JPN;KOR;SGP;USA'
INDICATORS = {
 'NE.CON.PRVT.ZS':'household_consumption_pct_gdp',
 'NE.CON.GOVT.ZS':'government_consumption_pct_gdp',
 'NE.CON.TOTL.ZS':'total_consumption_pct_gdp',
 'NE.GDI.TOTL.ZS':'gross_capital_formation_pct_gdp',
 'NY.GNS.ICTR.ZS':'gross_national_saving_pct_gdp',
 'NY.GDS.TOTL.ZS':'gross_domestic_saving_pct_gdp',
 'BN.CAB.XOKA.GD.ZS':'current_account_pct_gdp'
}
def fetch(item):
 code, label = item
 url = f'https://api.worldbank.org/v2/country/{COUNTRIES}/indicator/{code}?date=2000:2024&format=json&per_page=20000'
 for attempt in range(3):
  try:
   with urllib.request.urlopen(url, timeout=40) as r: payload=json.load(r)
   if not isinstance(payload,list) or len(payload)!=2: raise ValueError(payload)
   assert payload[0]['pages']==1
   (ROOT/'data/raw'/f'{code}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
   return code,label,url,payload
  except Exception:
   if attempt==2: raise
   time.sleep(1)

def main():
 (ROOT/'data/raw').mkdir(parents=True,exist_ok=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
  results=list(pool.map(fetch,INDICATORS.items()))
 rows=[];manifest=[]
 for code,label,url,payload in results:
  manifest.append({'indicator':code,'label':label,'api_url':url,'api_lastupdated':payload[0].get('lastupdated'),'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'period':'2000:2024'})
  for o in payload[1]:
   rows.append({'iso3':o['countryiso3code'],'country':o['country']['value'],'year':int(o['date']),'indicator':code,'label':label,'value':o['value'],'unit':'percent of GDP','api_lastupdated':payload[0].get('lastupdated')})
 rows.sort(key=lambda r:(r['iso3'],r['year'],r['indicator']))
 with (ROOT/'data/wdi_long.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (ROOT/'data/wdi_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 base=[]
 for c in COUNTRIES.split(';'):
  subset=[r for r in rows if r['iso3']==c and r['year']==2024]
  d={'iso3':c,'country':subset[0]['country'],'year':2024}
  d.update({r['label']:r['value'] for r in subset});base.append(d)
 with (ROOT/'data/baseline_2024.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(base[0]));w.writeheader();w.writerows(base)
 print(json.dumps(base,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
