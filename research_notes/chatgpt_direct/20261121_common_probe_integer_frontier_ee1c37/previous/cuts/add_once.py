"""One bounded LP pass adding the discovered clique cut, then exact rational recovery.
Only reconstructed rational covers, not floating-point solver statuses, establish
that these added inequalities still leave a nonempty relaxation.
"""
from pathlib import Path
from fractions import Fraction
import json,struct,sys,time
import numpy as np
import sympy as sp
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack
HERE=Path(__file__).resolve().parent
work=HERE.parent/'lower/work'
source=json.loads((HERE.parent/'lower/fractional_covers.json').read_text())
cuts=json.loads((HERE/'clique_cuts.json').read_text())
counts={tuple(map(int,t.split('-')[:2])):int(t.split('-')[2])for t in source['tag'].split('_')}
counts.pop((12,1104));types=sorted(counts)
def points(mask):
 while mask:
  bit=mask&-mask;yield bit.bit_length()-1;mask-=bit
bank=[]
for lo,hi,c,s in struct.iter_unpack('<QQII',(work/'bank').read_bytes()):
 t=(s%256,c)
 if t in counts:bank.append((lo+(hi<<64),types.index(t)))
results=[]
for frame in source['frames']:
 start=time.time();free=int(frame['free']);cut=next(c for c in cuts['cuts']if c['frame']==frame['frame']);cut_masks=set(map(int,cut['class_masks']))
 allowed=[(mask,t)for mask,t in bank if mask&free==mask];ri=[];ci=[]
 for j,(mask,t)in enumerate(allowed):
  support=list(points(mask))+[125+t];ri.extend(support);ci.extend([j]*len(support))
 matrix=coo_matrix((np.ones(len(ri),dtype=int),(ri,ci)),shape=(125+len(types),len(allowed))).tocsc()
 target=np.zeros(125+len(types),dtype=int);target[list(points(free))]=1
 for i,t in enumerate(types):target[125+i]=counts[t]
 coeff=np.array([int(mask in cut_masks)for mask,t in allowed],dtype=int)
 fit=linprog(np.zeros(len(allowed)),A_eq=matrix,b_eq=target,A_ub=coeff.reshape(1,-1),b_ub=[1],bounds=(0,None),method='highs',options={'time_limit':30})
 assert fit.status==0,fit.message
 support=np.flatnonzero(fit.x>1e-8);active=abs(coeff@fit.x-1)<1e-7
 exact=sp.Matrix(matrix[:,support].toarray());rhs=sp.Matrix(target)
 if active:exact=exact.col_join(sp.Matrix([coeff[support].tolist()]));rhs=rhs.col_join(sp.Matrix([1]))
 solution,params=exact.gauss_jordan_solve(rhs);assert not params.rows
 rat=[Fraction(int(x.p),int(x.q))for x in solution];assert all(x>0 for x in rat)
 sums=[Fraction(0)]*len(target);value=Fraction(0);rows=[]
 for j,v in zip(support,rat):
  mask,t=allowed[j]
  for p in points(mask):sums[p]+=v
  sums[125+t]+=v
  if mask in cut_masks:value+=v
  rows.append({'mask':str(mask),'type':types[t],'numerator':v.numerator,'denominator':v.denominator})
 assert sums==list(target)and value<=1
 result={'frame':frame['frame'],'free':str(free),'complete_candidate_count':len(allowed),'positive_classes':len(rows),'weights':rows,'cut_lhs_numerator':value.numerator,'cut_lhs_denominator':value.denominator,'seconds':time.time()-start}
 results.append(result);print(json.dumps({k:v for k,v in result.items()if k!='weights'}),flush=True)
 (HERE/'after_one_cut_covers.json').write_text(json.dumps({'tag':source['tag'],'types':types,'scope':'exact fractional covers satisfying one additional clique inequality per frame','frames':results},indent=2)+'\n')
