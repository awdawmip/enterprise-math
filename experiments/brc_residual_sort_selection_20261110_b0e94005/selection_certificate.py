from itertools import product
from functools import cmp_to_key

def order(ws,ss,C):
 ids=[i for i,w in enumerate(ws) if w<=C]
 def cmp(i,j):
  d=ss[i]*ws[j]-ss[j]*ws[i]
  if d:return -1 if d>0 else 1
  if ss[i]!=ss[j]:return -1 if ss[i]>ss[j] else 1
  if ws[i]!=ws[j]:return -1 if ws[i]<ws[j] else 1
  return i-j
 return sorted(ids,key=cmp_to_key(cmp))

checked=ambiguous=certified_opt=certified_no_mass=0
first=None
for ws in product(range(1,6),repeat=3):
 for ss in product(range(1,6),repeat=3):
  S=sum(ss)
  for C in range(1,11):
   ids=order(ws,ss,C);used=mass=0
   for i in ids:
    if used+ws[i]<=C:used+=ws[i];mass+=ss[i]
   used=full=0;upper=None
   for i in ids:
    if used+ws[i]<=C:used+=ws[i];full+=ss[i]
    else:
     upper=full+(C-used)*ss[i]//ws[i]
     break
   if upper is None:upper=full
   exact=max(sum(ss[i] for i in range(3) if mask>>i&1) for mask in range(8) if sum(ws[i] for i in range(3) if mask>>i&1)<=C)
   assert mass<=exact<=upper
   threshold=(S+1)//2
   if mass==upper:
    certified_opt+=1;assert mass==exact
   if upper<threshold:
    certified_no_mass+=1;assert exact<threshold
   if mass<threshold<=exact:
    ambiguous+=1
    if first is None:first=(ws,ss,C,mass,exact,upper)
   checked+=1
print({'cases':checked,'certified_sample_optimal':certified_opt,'certified_half_mass_infeasible':certified_no_mass,'greedy_half_fail_with_feasible_exact':ambiguous,'first_failure':first,'result':'PASS'})
