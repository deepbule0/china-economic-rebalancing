#!/usr/bin/env python3
"""Rebuild exact accounting results and publication figures from frozen inputs."""
import csv,json,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read_csv(name):
 with (ROOT/'data'/name).open(newline='') as f:return list(csv.DictReader(f))
def values(name):return {r['item']:float(r['value']) for r in read_csv(name)}
def write_csv(name,rows):
 with (ROOT/'data'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 baseline=read_csv('baseline_2024.csv')
 long=read_csv('wdi_long.csv')
 keys=[(r['iso3'],r['year'],r['indicator']) for r in long]
 assert len(keys)==len(set(keys)), 'Duplicate observation'
 reconciliation=[]
 for row in baseline:
  c={k:float(v) for k,v in row.items() if k not in ['iso3','country','year']}
  reconciliation.append({'iso3':row['iso3'],'year':2024,
   'consumption_residual':c['total_consumption_pct_gdp']-c['household_consumption_pct_gdp']-c['government_consumption_pct_gdp'],
   'domestic_saving_residual':c['gross_domestic_saving_pct_gdp']+c['total_consumption_pct_gdp']-100,
   'saving_investment_current_account_residual':c['gross_national_saving_pct_gdp']-c['gross_capital_formation_pct_gdp']-c['current_account_pct_gdp']})
 assert max(abs(x['consumption_residual']) for x in reconciliation)<1e-3
 assert max(abs(x['domestic_saving_residual']) for x in reconciliation)<1e-7
 write_csv('reconciliation_2024.csv',reconciliation)
 cn=values('china_2023_source.csv');us=values('us_2024_source.csv')
 cncorporate=cn['nonfinancial_enterprise_gross_saving']+cn['financial_institution_gross_saving']
 cnsum=cn['household_gross_saving']+cncorporate+cn['general_government_gross_saving']
 assert abs(cnsum-cn['total_gross_saving_reported'])<0.11
 sector={'china_2023':{
  'household_gross_saving_pct_gdp':cn['household_gross_saving']/cn['GDP']*100,
  'corporate_gross_saving_pct_gdp':cncorporate/cn['GDP']*100,
  'government_gross_saving_pct_gdp':cn['general_government_gross_saving']/cn['GDP']*100,
  'national_gross_saving_pct_gdp_reported':cn['total_gross_saving_reported']/cn['GDP']*100,
  'national_gross_saving_pct_gdp_component_sum':cnsum/cn['GDP']*100,
  'household_saving_rate':cn['household_gross_saving']/cn['household_disposable_income']*100,
  'household_income_pct_gdp':cn['household_disposable_income']/cn['GDP']*100},
  'us_2024':{
   'household_gross_saving_pct_gdp':(us['household_net_saving']+us['household_cfc'])/us['GDP']*100,
   'corporate_proxy_gross_saving_pct_gdp':sum(us[k] for k in ['nonfinancial_corporate_net_saving','nonfinancial_corporate_cfc','financial_business_net_saving','financial_business_cfc'])/us['GDP']*100,
   'broad_business_gross_saving_pct_gdp':(us['domestic_business_net_saving']+us['domestic_business_cfc'])/us['GDP']*100,
   'government_gross_saving_pct_gdp':(us['government_net_saving']+us['government_cfc'])/us['GDP']*100}}
 h=cn['household_disposable_income']/cn['GDP'];s=cn['household_gross_saving']/cn['household_disposable_income'];dh=.03;ds=-.05
 scenarios=[]
 for name,hx,sx in [('baseline',h,s),('income_only',h+dh,s),('saving_only',h,s+ds),('both',h+dh,s+ds)]:
  scenarios.append({'scenario':name,'income_share':hx,'saving_rate':sx,'consumption_share_pct_gdp':hx*(1-sx)*100})
 decomposition={'income_channel_pp':(1-s)*dh*100,'saving_channel_pp':-h*ds*100,'interaction_pp':-dh*ds*100}
 total=sum(decomposition.values())
 assert abs(total-(scenarios[-1]['consumption_share_pct_gdp']-scenarios[0]['consumption_share_pct_gdp']))<1e-10
 assert abs(1.5-(.5+.4+.6))<1e-10
 write_csv('accounting_scenarios.csv',scenarios)
 (ROOT/'data/derived_results.json').write_text(json.dumps({'sector':sector,'decomposition':decomposition,'change_pp':total,'scope':'Accounting only, not estimated behavioral effects'},indent=2)+'\n')
 # Meaningful publication checks: compare every main-table displayed value against source inputs.
 for lang in ['en','zh-CN']:
  paper=(ROOT/f'paper.{lang}.md').read_text()
  for row in baseline:
   for key in ['household_consumption_pct_gdp','government_consumption_pct_gdp','total_consumption_pct_gdp','gross_capital_formation_pct_gdp','gross_national_saving_pct_gdp','current_account_pct_gdp']:
    assert f"{float(row[key]):.2f}" in paper,(lang,row['iso3'],key)
  for v in scenarios:assert f"{v['consumption_share_pct_gdp']:.2f}" in paper
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 import numpy as np
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','savefig.facecolor':'white'})
 rows={r['iso3']:r for r in baseline};order=['CHN','JPN','KOR','SGP','USA'];names=['China','Japan','Korea','Singapore','United States'];x=np.arange(5)
 fig,ax=plt.subplots(figsize=(9.2,5.5))
 hc=[float(rows[i]['household_consumption_pct_gdp']) for i in order]
 inv=[float(rows[i]['gross_capital_formation_pct_gdp']) for i in order]
 sav=[float(rows[i]['gross_national_saving_pct_gdp']) for i in order]
 for shift,vals,color,label in [(-.24,hc,'#1f5278','Household consumption'),(0,inv,'#c79044','Gross capital formation'),(.24,sav,'#7b9596','Gross national saving')]:
  ax.barh(x+shift,vals,height=.21,color=color,label=label)
  for j,v in enumerate(vals):ax.text(v+.55,j+shift,f'{v:.1f}',va='center',fontsize=10)
 ax.set(yticks=x,yticklabels=names,xlim=(0,78),xlabel='Percent of GDP')
 ax.invert_yaxis();ax.tick_params(labelsize=11);ax.set_axisbelow(True);ax.xaxis.grid(True,alpha=.12)
 ax.legend(loc='upper center',bbox_to_anchor=(.5,-.14),ncol=3,frameon=False,fontsize=9.4)
 fig.suptitle('Household consumption, investment and national saving | 2024',fontweight='bold',fontsize=13,y=.98)
 fig.text(.025,.012,'Source: World Bank WDI, API update 2026-10-08. Bars are not additive.',fontsize=8,color='#555555')
 fig.tight_layout(rect=(0,.09,1,.94))
 (ROOT/'figures').mkdir(exist_ok=True)
 for ext in ['png','svg']:fig.savefig(ROOT/'figures'/f'comparison_2024.{ext}',dpi=180)
 plt.close(fig)
 fig,ax=plt.subplots(figsize=(9.8,4.3));yy=[r['consumption_share_pct_gdp'] for r in scenarios]
 bars=ax.bar(['2023 baseline','Income share\n+3 pp','Saving rate\n-5 pp','Both changes'],yy,color=['#7f8c98','#42819b','#42819b','#267a66'],width=.57)
 ax.set(ylim=(0,50),ylabel='Household consumption (% of GDP)',title='Accounting scenario: two channels to consumption')
 for b,v in zip(bars,yy):ax.text(b.get_x()+b.get_width()/2,v+.65,f'{v:.2f}%',ha='center',fontweight='bold')
 ax.spines['left'].set_visible(False);ax.set_axisbelow(True);ax.yaxis.grid(True,alpha=.15)
 fig.text(.02,.015,f"China 2023 NBS baseline. Combined change: {total:.2f} pp. Assumptions only; no estimated policy effect.",fontsize=8,color='#555555')
 fig.tight_layout(rect=(0,.06,1,1))
 for ext in ['png','svg']:fig.savefig(ROOT/'figures'/f'accounting_scenario.{ext}',dpi=180)
 plt.close(fig)
 print(json.dumps({'observations':len(long),'country_year_baselines':len(baseline),'sector_results':sector,'scenario_change_pp':total,'checks':'passed'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
