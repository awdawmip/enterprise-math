import json
from fractions import Fraction as F
from pathlib import Path
ns={}
exec(Path('prefix1128_verify.py').read_text().split('L0=10**90')[0],ns)
lines,_,volume=ns['scan'](10**100,3*10**60,ns['V2'])
r=[json.loads(l) for l in open('tail_observers.jsonl')];ex=json.load(open('extra_rows.json'))[0]
assert volume==620 and len(lines)==len(r)==115
assert lines==[tuple(map(int,x['line'])) for x in r]
n=tuple(r[0]['tests'][0]['normal']);dot=lambda a,b:sum(x*y for x,y in zip(a,b))
a=[]
for row in r:
 m=row['m']+[ex['m']];C=[c+[ex['cols'][i]] for i,c in enumerate(row['cols'])];e=row['error']+[ex['error']]
 v=dot(n,m);s=sum(abs(dot(n,c)) for c in C)+dot(list(map(abs,n)),e)
 assert abs(v)>14000*s>0;a.append((v,s))
mn=min(abs(v) for v,s in a);mx=max(s for v,s in a);assert mn>14000*mx
Q=3*10**60;L3=L2=10**8
while 4*ns['E']*L3<=ns['d'][0]*Q*Q:L3*=2
while L2<=Q*Q:L2*=2
assert L3>10**100 and L2>10**100
out=dict(normal=n,grid=125,minimum_abs_center=str(mn),maximum_support=str(mx),first_triple=str(L3),first_sqrt_pair=str(L2),positive=sum(v>0 for v,s in a),count=len(a))
Path('fixed_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('all assertions passed')
