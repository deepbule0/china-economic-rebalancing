#!/usr/bin/env python3
"""Build standalone bilingual PDFs with embedded CJK subsets when provided."""
import html,os,pathlib,re
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT,TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,PageBreak,KeepTogether
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
BUILD=ROOT/'.build-fonts';BUILD.mkdir(exist_ok=True)
FONTROOT=pathlib.Path('/usr/share/fonts/truetype/dejavu')
for n,f in [('Serif','DejaVuSerif.ttf'),('SerifB','DejaVuSerif-Bold.ttf'),('Sans','DejaVuSans.ttf'),('SansB','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:
 pdfmetrics.registerFont(TTFont(n,str(FONTROOT/f)))
pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='SerifB',italic='Serif',boldItalic='SerifB')
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansB',italic='Sans',boldItalic='SansB')
fontpath=os.environ.get('CJK_FONT')
if fontpath:
 from fontTools.ttLib import TTFont as FontToolsFont
 from fontTools.varLib.instancer import instantiateVariableFont
 from fontTools import subset
 texts=''.join(p.read_text() for p in ROOT.glob('*.md'))
 for name,weight in [('CJK',400),('CJKB',650)]:
  f=FontToolsFont(fontpath)
  if 'fvar' in f:f=instantiateVariableFont(f,{'wght':weight},inplace=True)
  opts=subset.Options();opts.layout_features=['*'];opts.name_IDs=['*'];opts.name_legacy=True
  ss=subset.Subsetter(options=opts);ss.populate(text=texts+'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');ss.subset(f)
  target=BUILD/(name+'.ttf');f.save(target);pdfmetrics.registerFont(TTFont(name,str(target)))
else:
 from reportlab.pdfbase.cidfonts import UnicodeCIDFont
 pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'));pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
 CJK='STSong-Light';CJKB='HeiseiKakuGo-W5'
 # Alias below uses selected family names.
if fontpath:CJK='CJK';CJKB='CJKB'
pdfmetrics.registerFontFamily(CJK,normal=CJK,bold=CJKB,italic=CJK,boldItalic=CJKB)
BASEURL='https://github.com/deepbule0/china-economic-rebalancing/blob/main/papers/high-saving-consumption-transition/'
CJKRE=re.compile(r'([\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef]+)')
def plain(s):
 s=html.escape(s)
 return CJKRE.sub(lambda m:f'<font name="{CJK}">{m.group(1)}</font>',s)
def inline(s):
 # Parse only the deliberately small Markdown vocabulary used in the paper.
 pat=re.compile(r'\[([^\]]+)\]\(([^\)]+)\)|\*\*(.+?)\*\*|`([^`]+)`')
 out=[];pos=0
 for m in pat.finditer(s):
  out.append(plain(s[pos:m.start()]))
  if m.group(1) is not None:
   url=m.group(2)
   if not url.startswith(('http:','https:','#')):url=BASEURL+url
   out.append(f'<a href="{html.escape(url,quote=True)}" color="#24577b">{inline(m.group(1))}</a>')
  elif m.group(3) is not None:out.append('<b>'+inline(m.group(3))+'</b>')
  else:out.append('<font name="Mono" size="8.7">'+plain(m.group(4))+'</font>')
  pos=m.end()
 out.append(plain(s[pos:]))
 return ''.join(out)
W,H=A4;LEFT=54;RIGHT=54;AW=W-LEFT-RIGHT
class PaperDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and getattr(f,'_outline_level',None) is not None:
   level=f._outline_level
   key=f'bookmark-{self.page}-{getattr(self,"_bm",0)}';self._bm=getattr(self,'_bm',0)+1
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.getPlainText(),key,level=level,closed=False)
def styles(lang):
 cn=lang=='zh-CN';bodyfont=CJK if cn else 'Serif';boldfont=CJKB if cn else 'SerifB'
 d={
 'body':ParagraphStyle('body',fontName=bodyfont,fontSize=10.1 if cn else 10.45,leading=16.4 if cn else 15.1,spaceAfter=7.8,textColor=colors.HexColor('#1f2933'),wordWrap='CJK' if cn else None,splitLongWords=True),
 'h1':ParagraphStyle('title',fontName=boldfont,fontSize=23 if cn else 22,leading=31 if cn else 27.5,spaceAfter=11,textColor=colors.HexColor('#193e5a'),keepWithNext=True),
 'h2':ParagraphStyle('subtitle',fontName=boldfont,fontSize=14.5,leading=21,spaceAfter=12,textColor=colors.HexColor('#193e5a'),keepWithNext=True),
 'h3':ParagraphStyle('section',fontName=boldfont,fontSize=12.2,leading=18,spaceBefore=13,spaceAfter=7,textColor=colors.HexColor('#193e5a'),keepWithNext=True),
 'h4':ParagraphStyle('subsection',fontName=boldfont,fontSize=10.6,leading=16.5,spaceBefore=9,spaceAfter=5,keepWithNext=True),
 'caption':ParagraphStyle('caption',fontName=CJK if cn else 'Sans',fontSize=8.0,leading=12.3,spaceAfter=10,textColor=colors.HexColor('#52616c'),wordWrap='CJK'),
 'cell':ParagraphStyle('cell',fontName=CJK,fontSize=8.0,leading=12.1,wordWrap='CJK',splitLongWords=True),
 'headcell':ParagraphStyle('headcell',fontName=CJKB,fontSize=8.0,leading=12.1,textColor=colors.white,wordWrap='CJK',splitLongWords=True),
 'ref':ParagraphStyle('reference',fontName=CJK if cn else 'Serif',fontSize=8.7,leading=13.2,spaceAfter=5.6,wordWrap='CJK',splitLongWords=True),
 }
 return d

def table(rows,ss):
 n=len(rows[0]);widths=[AW/n]*n
 if n==7:widths=[74]+[(AW-74)/6]*6
 if n==4:widths=[AW*.14,AW*.28,AW*.28,AW*.30]
 if n==3:widths=[AW*.23,AW*.38,AW*.39]
 data=[]
 for ri,row in enumerate(rows):
  cells=[]
  for ci,c in enumerate(row):
   st=ss['headcell'] if ri==0 else ss['cell']
   if ri>0 and re.fullmatch(r'[+\-\d.,% ]+',c):st=ParagraphStyle('num',parent=st,alignment=TA_RIGHT)
   cells.append(Paragraph(inline(c),st))
  data.append(cells)
 t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#234e6c')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f0f4f6'),colors.white]),('LINEBELOW',(0,-1),(-1,-1),.6,colors.HexColor('#b6c6cf'))]))
 return t

def parse(md,lang,refs=False):
 ss=styles(lang);lines=md.splitlines();story=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',c) for c in row):rows.append(row)
    i+=1
   assert all(len(r)==len(rows[0]) for r in rows)
   story.extend([table(rows,ss),Spacer(1,9)]);continue
  m=re.match(r'!\[.*?\]\((.*?)\)',line)
  if m:
   p=ROOT/m.group(1);im=Image(str(p));scale=min(AW/im.imageWidth,270/im.imageHeight);im.drawWidth=im.imageWidth*scale;im.drawHeight=im.imageHeight*scale
   caption=None
   if i+2<len(lines) and lines[i+2].strip().startswith('*') and not lines[i+2].strip().startswith('**'):
    caption=Paragraph(inline(lines[i+2].strip().strip('*')),ss['caption']);i+=2
   story.append(KeepTogether([im,Spacer(1,5)]+([caption] if caption else [])));i+=1;continue
  m=re.match(r'^(#{1,4})\s+(.*)',line)
  if m:
   level=len(m.group(1));key='h'+str(level)
   if refs:key='h3' if level==1 else 'h4'
   p=Paragraph(inline(m.group(2)),ss[key])
   if not refs and level in (1,3):p._outline_level=0 if level==1 else 1
   story.append(p);i+=1;continue
  if line.startswith('- '):
   story.append(Paragraph(inline(line[2:]),ss['ref'] if refs else ss['body'],bulletText='•'));i+=1;continue
  parts=[line];i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|','![','- ')):
   parts.append(lines[i].strip());i+=1
  text=' '.join(parts)
  if text.startswith('*') and text.endswith('*') and not text.startswith('**'):story.append(Paragraph(inline(text.strip('*')),ss['caption']))
  else:story.append(Paragraph(inline(text),ss['ref'] if refs else ss['body']))
 return story

def page(canvas,doc):
 canvas.saveState();canvas.setFillColor(colors.HexColor('#52616c'));canvas.setFont('Sans',7.7)
 canvas.drawString(LEFT,H-32,'CAPITAL ACCUMULATION AND HOUSEHOLD WELFARE')
 canvas.drawRightString(W-RIGHT,H-32,'WORKING PAPER 1.0 | 22 OCT 2026')
 canvas.setStrokeColor(colors.HexColor('#c9d4da'));canvas.setLineWidth(.5);canvas.line(LEFT,H-39,W-RIGHT,H-39)
 canvas.line(LEFT,35,W-RIGHT,35);canvas.setFont('Sans',8);canvas.drawString(LEFT,22,'Bilingual comparative macroeconomic and fiscal research');canvas.drawRightString(W-RIGHT,22,str(doc.page));canvas.restoreState()
def main():
 for lang in ['zh-CN','en']:
  target=OUT/f'saving-consumption.{lang}.pdf'
  doc=PaperDoc(str(target),pagesize=A4,leftMargin=LEFT,rightMargin=RIGHT,topMargin=56,bottomMargin=52,title='从资本积累到居民福利' if lang=='zh-CN' else 'From Capital Accumulation to Household Welfare',author='deepbule0; prepared with ChatGPT assistance',subject='Research working paper; sectoral saving and fiscal institutions',pageCompression=1)
  story=parse((ROOT/f'paper.{lang}.md').read_text(),lang)
  story.append(Spacer(1,18));story+=parse((ROOT/'REFERENCES.md').read_text(),lang,refs=True)
  doc.build(story,onFirstPage=page,onLaterPages=page)
  print(target)
if __name__=='__main__':main()
