"""Find short violated intersecting-family inequalities; verify with Fractions."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json,random
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'lower/fractional_covers.json'
doc=json.loads(SOURCE.read_text());result=[]
for frame in doc['frames']:
 rows=frame['weights'];m=[int(r['mask'])for r in rows];w=[Fraction(r['numerator'],r['denominator'])for r in rows]
 adj=[sum(1<<j for j in range(len(rows))if i!=j and m[i]&m[j])for i in range(len(rows))]
 best=None;attempts=0
 order=sorted(range(len(rows)),key=lambda i:w[i],reverse=True)
 # Cardinality-first complete searches have tiny upper sums on these points.
 def rec(chosen,cand,total,k):
  global attempts
  if len(chosen)==k:
   attempts+=1
   return chosen if total>1 else None
  need=k-len(chosen)
  if len(cand)<need or total+sum((w[i]for i in cand[:need]),Fraction(0))<=1:return None
  for z,i in enumerate(cand):
   if len(cand)-z<need:break
   more=[j for j in cand[z+1:]if adj[i]>>j&1]
   ans=rec(chosen+[i],more,total+w[i],k)
   if ans is not None:return ans
  return None
 for k in range(3,15):
  best=rec([],order,Fraction(0),k)
  if best is not None:break
 assert best is not None
 total=sum((w[i]for i in best),Fraction(0))
 assert total>1 and all(m[i]&m[j]for i,j in combinations(best,2))
 common=m[best[0]]
 for i in best:common&=m[i]
 assert common==0
 entry={'frame':frame['frame'],'free':frame['free'],'kind':'pairwise_intersecting_clique','rhs':1,'support_indices':sorted(best),'class_masks':[rows[i]['mask']for i in sorted(best)],'lhs_numerator':total.numerator,'lhs_denominator':total.denominator,'margin_numerator':total.numerator-total.denominator,'margin_denominator':total.denominator,'float_lhs_for_display':float(total),'cardinality':len(best)}
 result.append(entry);print(json.dumps({k:entry[k]for k in ['frame','cardinality','float_lhs_for_display','lhs_numerator','lhs_denominator']}),flush=True)
(HERE/'clique_cuts.json').write_text(json.dumps({'source_tag':doc['tag'],'scope':'valid integer-cover inequalities cutting only the five supplied fractional points; no whole-polyhedron infeasibility claim','cuts':result},indent=2)+'\n')
