from verify_threshold import model
from itertools import combinations_with_replacement
from collections import Counter, defaultdict
import json
p=5
X,ports,ks,Y,B=model(p)
n=len(X)
ptports=[[i for i,_,row in []] for _ in range(n)]
ptports=[[j for j,(_,_,L) in enumerate(ports) if x in L] for x in range(n)]
assert all(len(q)==p for q in ptports)
movable={}
for d in range(p+1):
 for x in range(n):
  family=[]
  for a,(_,_,L) in enumerate(ports):
   if ports[a][0]!=d:continue
   s=tuple(sorted(tuple(L)+(x,)))
   family.append(s)
  assert len(set(family))==p-1
  for tup in family:
   assert tup not in movable
   movable[tup]=(d,x)

def residue(tup):
   counts=[0]*n
   for x in tup:
    for j in ptports[x]: counts[j]+=1
   return bytes([v%p for v in counts])
mov_res=defaultdict(set)
for tup,k in movable.items(): mov_res[residue(tup)].add(k)
print('movable states',len(movable),'movable components',len(set(movable.values())),'distinct movable residues',len(mov_res))
conflicted={key:val for key,val in mov_res.items() if len(val)>1}
print('distinct movable components sharing residue',len(conflicted),'example',[(list(v)[:3]) for v in list(conflicted.values())[:3]])
res_m=set(mov_res)
total=0; in_target=0; isolated_target=0; atomic_target=0;some_example=None
for tup in combinations_with_replacement(range(n),p+1):
 total+=1
 sig=residue(tup)
 if sig in res_m:
  in_target+=1
  if tup not in movable:
   isolated_target+=1
   if some_example is None:
    some_example=tup, list(mov_res[sig])
 if len(set(tup))==1 and sig in res_m:
  atomic_target+=1
print('total',total,'in movable residue target',in_target,'isolated target',isolated_target,'atomic target',atomic_target, 'example', some_example)
print('predicted all movable',len(movable))
assert total==475020
result={'p':p,'N':p+1,'states':total,'movable_states':len(movable),'movable_components':len(set(movable.values())),
'movable_residue_fibers':len(mov_res),'movable_cross_component_residual_collisions':len(conflicted),'isolated_states_same_residue_as_a_movable':isolated_target,'first_isolated_target':some_example}
with open('/mnt/data/EM_BRC_NonnegativeFiberSharpThreshold_20261015/p5_mass6_certificate.json','w') as f:json.dump(result,f,indent=2)
