"""Exact rational checks for R1/N14 depth-two LR-signature quotient.
Finite witnesses only; full all-policy generality is in PROOF.md.
"""
from fractions import Fraction as F
import json
def pp(x): return max(x,F(0))
def partitions(xs):
    if not xs:
        yield ()
        return
    h,*tail=xs
    for p in partitions(tail):
        yield ((h,),)+p
        for k in range(len(p)):
            q=list(p);q[k]=(h,)+q[k];yield tuple(q)
def test(pi,rows,ratios):
    assert sum(pi)==1 and all(x>0 for x in pi)
    assert all(sum(p)==1 and all(x>0 for x in p) for p in rows)
    q=[[p[j]*ratios[j] for j in range(len(ratios))] for p in rows]
    assert all(sum(p)==1 for p in q)
    R=sorted(set(ratios))
    signature=lambda row:tuple(str(sum((row[j] for j,r in enumerate(ratios) if r==a),F(0))) for a in R)
    mus=[signature(p) for p in rows]
    return {"P_rows":[[str(a) for a in p] for p in rows],
            "Q_rows":[[str(a) for a in p] for p in q],
            "signatures":mus,
            "minimum_profile":[1,len(set(mus)),len(R)],
            "ordered_prefixes":1+len(pi)+len(pi)*len(ratios)}
pi=[F(1,3)]*3
p=[[F(1,4),F(1,4),F(1,2)],
   [F(1,12),F(3,4),F(1,6)],
   [F(1,6),F(1,2),F(1,3)]]
r=[F(2),F(1),F(1,2)]
first=test(pi,p,r)
assert first["minimum_profile"]==[1,3,3]
scores=[sum((p[i][j]*pp(r[j]-1) for j in range(3)),F(0)) for i in range(3)]
assert scores==[F(1,4),F(1,12),F(1,6)]
witnesses=[];seen=set()
for blocks in partitions([0,1,2]):
    blocks=tuple(sorted(tuple(sorted(b)) for b in blocks))
    if blocks in seen: continue
    seen.add(blocks)
    if len(blocks)==3: continue
    chosen=next(b for b in blocks if len(b)>1)
    lo,hi=min(scores[i] for i in chosen),max(scores[i] for i in chosen)
    lam=(lo+hi)/2
    full=sum((pi[i]*pp(scores[i]-lam) for i in range(3)),F(0))
    coarse=F(0)
    for b in blocks:
        mass=sum((pi[i] for i in b),F(0))
        avg=sum((pi[i]*scores[i] for i in b),F(0))/mass
        coarse+=mass*pp(avg-lam)
    gap=full-coarse
    assert gap>0
    witnesses.append({"partition":[list(b) for b in blocks],
      "lambda":str(lam),"full_max":str(full),"compressed_upper":str(coarse),"gap":str(gap)})
assert len(seen)==5 and len(witnesses)==4
pi2=[F(1,2)]*2
p2=[[F(1,16),F(3,16),F(1,2),F(1,4)],
    [F(3,16),F(1,16),F(1,2),F(1,4)]]
r2=[F(2),F(2),F(1,2),F(1)]
second=test(pi2,p2,r2)
assert p2[0]!=p2[1] and second["minimum_profile"]==[1,1,3]
for rows,target in [(p2,F(1,8)),([[p2[i][j]*r2[j] for j in range(4)] for i in range(2)],F(1,4))]:
    full=pi2[0]*sum((rows[0][j] for j in range(4) if r2[j]==2),F(0))
    quotient=F(1,2)*sum((pi2[i]*sum((rows[i][j] for j in range(4) if r2[j]==2),F(0)) for i in range(2)),F(0))
    assert full==quotient==target
print(json.dumps({"status":"PASS_EXACT_FRACTION","first_instance":first,
  "all_four_partition_support_gaps":witnesses,"second_instance":second,
  "merged_witness_P_D1":"1/8","merged_witness_Q_D1":"1/4",
  "scope":"finite rational cases; general theorem from PROOF.md; review/P000 transfer pending"},indent=2))
