"""Lift a support clique cut to an entire implicit intersecting family."""
from pathlib import Path
from fractions import Fraction
import json
HERE=Path(__file__).resolve().parent
data=json.loads((HERE.parent/'lower/fractional_covers.json').read_text())
def points(mask):
 while mask:
  bit=mask&-mask;yield bit.bit_length()-1;mask-=bit
cuts=[]
for frame in data['frames']:
 rows=frame['weights'];masks=[int(r['mask'])for r in rows];weights=[Fraction(r['numerator'],r['denominator'])for r in rows];free=int(frame['free']);best=None
 for i,(m,w)in enumerate(zip(masks,weights)):
  compatible=[Fraction(0)]*125
  for n,v in zip(masks,weights):
   if n&m:continue
   for p in points(n):compatible[p]+=v
  for p in points(free^m):
   margin=w-compatible[p]
   if best is None or margin>best[0]:best=(margin,i,p,compatible[p])
 margin,i,p,c=best
 item={'frame':frame['frame'],'free':frame['free'],'anchor_mask':str(masks[i]),'point':p,'anchor_weight':str(weights[i]),'compatible_point_weight':str(c),'violation':str(margin),'rhs':1,'strictly_separates':margin>0}
 cuts.append(item);print(item,flush=True)
(HERE/'lifted_star_cuts.json').write_text(json.dumps({'source_tag':data['tag'],'cut_rule':'x_anchor + sum(x_C for C containing point and intersecting anchor) <= 1','cuts':cuts},indent=2)+'\n')
