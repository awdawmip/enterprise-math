"""Independent literal signed-step prefix tuple check for four slot samples."""
from frozen_model import W,STEPS,observe,candidates
from pathlib import Path
import json
D=json.loads(Path(__file__).with_name('EC49FCF_150_CERTIFICATE.json').read_text())
def prefixes(w):
 steps=tuple(z for op in w for z in STEPS[op])
 return frozenset(steps[:j] for j in range(1,len(steps)+1))
chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
pools={f'{h}:{sig}':ws for h in range(4,10) for sig,ws in candidates(h).items()}
base={k:prefixes(w) for k,w in chosen.items()}
assert len(frozenset().union(*base.values()))==158
SAMPLE=[('H7_H7_H8_TAIL30',0),('H7_H9_H9',16),('H8_H8_H8',22),('H8_H9_H9',16)]
results=[]
for family,index in SAMPLE:
 r=D['per_family'][family][index];slots=set(r['slots'])
 fixed=frozenset().union(*(v for k,v in base.items() if k not in slots))
 limit=158-len(fixed)
 arr=[]
 for k in r['slots']:
  masks={frozenset(prefixes(w)-fixed) for w in pools[k]}
  arr.append([v for v in masks if len(v)<limit])
 arr.sort(key=len)
 a,b,c,d=arr
 best=158;checks=0
 for x in a:
  for y in b:
   xy=x|y
   if len(xy)>=limit:continue
   for z in c:
    xyz=xy|z
    if len(xyz)>=limit:continue
    for w in d:
     checks+=1
     best=min(best,len(fixed|xyz|w))
 assert best==r['minimum']==158
 assert checks==r['fourth_checks'],(family,index,checks,r['fourth_checks'])
 results.append({'family':family,'index':index,'slots':r['slots'],
                 'minimum':best,'fourth_checks':checks})
 print('PASS_TUPLE',family,index,checks)
Path(__file__).with_name('EC49FCF_TUPLE_CROSSCHECK.json').write_text(json.dumps({'schema':'EC49FCF_TUPLE_XCHECK_V1','results':results},indent=2)+'\n')
