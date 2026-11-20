from collections import Counter
import itertools
def fixed(P,rots,bad,pair,class_cost):
 records=[]
 for t,g in enumerate(rots):
  cycles=[];ix={}
  for i in range(125):
   if i in ix:continue
   q=[];j=i
   while j not in q:q.append(j);ix[j]=len(cycles);j=g[j]
   cycles.append(q)
  E={};counts=Counter()
  def rec(start,q,points):
   for idx in range(start,len(cycles)):
    v=points+cycles[idx];s=len(v)
    if s>13 or any(bad[a][b]>>c&1 for a,b,c in itertools.combinations(v,3)):continue
    m=q|(1<<idx);cost=class_cost(v,pair);E[m]=(cost,s);counts[s]+=1
    rec(idx+1,m,v)
  rec(0,0,[])
  (P/f'fix{t}').write_text(''.join(f'{q} {cost} {size}\n'for q,(cost,size) in sorted(E.items())))
  records.append(len(E))
 return records
