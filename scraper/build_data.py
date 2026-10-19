import json,sys
src=sys.argv[1]
d=json.load(open(src))
TIER=[('RF',1),('RF (Japan)',1),('Composite',2),('S-Video',3),('Component YPbPr',4),('Analog RGB',5),('Digital RGB',5),('SDI',6),('HDMI',6),('DVI',6)]
def best(inputs):
    t=0
    for name,v in TIER:
        if name in inputs: t=max(t,v)
    return t
FAMOUS={'XBR','Wega','Wega (HD)','D-Series',"I'Art",'Tau','Omnivision','Profeel','Qualia','Trinitron','GDM','DDM','Multisync','Diamond Pro','SuperScan'}
out=[];pool=[]
seen=set()
for x in d:
    if not x.get('size_in') or not x.get('inputs'): continue
    mask=x['mask'].replace('Monochrome Tube (no mask)','Monochrome')
    row=[x['name'],x['brand'].strip(),x['series'],x['application'] or '',round(x['size_in'],1),best(x['inputs']),mask,
         x['tube_brand'],x['country'],x['weight_lbs'] or 0,x['url'].split('/crts/')[1],
         ', '.join(x['resolutions']),', '.join(x['formats']),x['tube_model'],x.get('image','')]
    i=len(out); out.append(row)
    core=all([x['application'],mask,x['country'],x['tube_brand'],best(x['inputs'])])
    notable=(x['application']=='Professional' or 'Hall of Fame' in x['tags']
             or best(x['inputs'])>=4 or x['series'] in FAMOUS)
    if core and notable: pool.append(i)
print(len(out),'sets,',len(pool),'answer pool',file=sys.stderr)
js='const CRTS='+json.dumps(out,separators=(',',':'),ensure_ascii=False)+';\nconst POOL='+json.dumps(pool,separators=(',',':'))+';'
open('data.js','w',encoding='utf-8').write(js)
print(len(js)//1024,'KB',file=sys.stderr)
