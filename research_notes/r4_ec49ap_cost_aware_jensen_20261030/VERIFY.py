"""EC49AP exact rational certificate: all-real causal upper bound at fixed cost.

Reuses the source-defined EC49AO positive auxiliary BRC fibers and 168-vertex
construction. Python 3 stdlib only. No native signed-BRC inference is made.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
import json

ZERO=F(0); ONE=F(1)
ETA=F(1,25); C1=F(43,16); C2=F(13,16)
COST=(1,1,2,2,0)
L=F(25,32); U=F(43,48); CMIN=F(43,96)
LAMBDA=F(553,946)*ETA-F(152,473)
B=F(22625,60544)-F(13825,30272)*ETA
K=-LAMBDA

def first_cost_vertices():
    out=set()
    for m in range(3):
        others=[w for w in range(3) if w != m]
        for i,j in product(range(5),repeat=2):
            needed=C1-COST[i]-COST[j]
            for a,b in combinations(range(5),2):
                if not min(COST[a],COST[b]) < needed < max(COST[a],COST[b]):
                    continue
                p=(needed-COST[b])/F(COST[a]-COST[b])
                x=[[ZERO]*5 for _ in range(3)]
                x[others[0]][i]=x[others[1]][j]=ONE
                x[m][a]=p; x[m][b]=ONE-p
                out.add(tuple(tuple(row) for row in x))
    return sorted(out)

def fibers(x):
    for c,u in product(range(4),range(2)):
        q=[x[w][c]*(F(1,2)+(2*u-1)*(1-w)*ETA)/3 for w in range(3)]
        T=sum(q); V=sum(max(ZERO,43*qz-16*T) for qz in q)
        yield T,V

def paid_cost(x):
    return sum((t for t,_ in fibers(x)),ZERO)

def full_value(x):
    return sum((v/F(172) for _,v in fibers(x)),ZERO)

def dual_value(x):
    return full_value(x)-LAMBDA*paid_cost(x)

def midpoint(x,y):
    return tuple(tuple((a+b)/2 for a,b in zip(rx,ry)) for rx,ry in zip(x,y))

verts=first_cost_vertices()
assert len(verts)==168
for x in verts:
    assert all(sum(row)==ONE and all(z>=ZERO for z in row) for row in x)
    assert sum(COST[c]*x[w][c] for w,c in product(range(3),range(5)))==C1

gaps={x:B-dual_value(x) for x in verts}
assert all(t>=0 for t in gaps.values())
low_tight=[x for x in verts if paid_cost(x)==L and gaps[x]==0]
high=[x for x in verts if paid_cost(x)==U]
low_strict=[x for x in verts if x not in low_tight and paid_cost(x)<U]
assert (len(low_tight),len(high),len(low_strict))==(12,24,132)
assert set(verts)==set(low_tight)|set(high)|set(low_strict)
assert min(paid_cost(x) for x in verts)==CMIN
assert all(paid_cost(x)<=L for x in low_strict)
A=min(gaps[x] for x in low_strict)
assert A==F(7173,137600)

# Jensen defect (D(x)+D(y))/2 - D((x+y)/2) on all 12*24
# tight-low/high-cost cross pairs. All fractions exact.
defect=[(dual_value(x)+dual_value(y))/2 -dual_value(midpoint(x,y))
        for x in low_tight for y in high]
assert len(defect)==288
assert all(v>=0 for v in defect)
J=min(defect)
assert J==F(1,600)
assert sum(v==J for v in defect)>0
assert sum(gaps[x]==0 for x in high)==4

# Resource-bound coefficient proof. For nonnegative l,h,n summing to 1:
# paid cost >= C2 implies h>=3/11 and 11*l+43*n+96*s>=8,
# where s=paid_cost-C2>=0. The following exact coefficients imply
# B+lambda*C2-H >= (11*l+43*n+96*s)/12100 >= 2/3025.
TAU=F(1,12100)
HMIN=F(3,11)
assert (C2-L)/(U-L)==HMIN
assert U-C2==F(8,96)
assert U-L==F(11,96)
assert U-CMIN==F(43,96)
assert A>=43*TAU
assert 2*J*HMIN==11*TAU
assert K>=96*TAU
DELTA=8*TAU
assert DELTA==F(2,3025)

OLD_SUPPORT=B+LAMBDA*C2
assert OLD_SUPPORT==F(171531,1513600)
NEW_UPPER=OLD_SUPPORT-DELTA
assert NEW_UPPER==F(1875833,16649600)
PREVIOUS_UPPER=F(1715013,15136000)
WITNESS_VALUE=F(77,688)
assert PREVIOUS_UPPER>NEW_UPPER>WITNESS_VALUE
assert PREVIOUS_UPPER-NEW_UPPER==F(106813,166496000)
assert NEW_UPPER-WITNESS_VALUE==F(12433,16649600)

# Exact legal all-purchase witness from EC49AO (not a new optimum claim).
witness=((ZERO,F(3,16),F(1,4),ZERO,F(9,16)),
         (ONE,ZERO,ZERO,ZERO,ZERO),
         (ZERO,ONE,ZERO,ZERO,ZERO))
assert all(sum(row)==ONE for row in witness)
assert sum(COST[c]*witness[w][c] for w,c in product(range(3),range(5)))==C1
assert paid_cost(witness)==C2
assert full_value(witness)==WITNESS_VALUE

P=Q=ZERO
for w,u,z in product(range(3),range(2),range(3)):
    t=F(1,2)+(2*u-1)*(1-w)*ETA
    p=t*(F(1,6) if z==w else F(1,12))
    q=t/9
    assert p>0 and q>0
    P+=p;Q+=q
assert P==Q==ONE

# Counts per paid-cost group make the exhaustive domain auditable.
cost_counts=Counter(str(paid_cost(v)) for v in verts)
report={
 'schema':'EC49AP_COST_AWARE_CROSS_FIBER_CERT_V1',
 'status':'PASS_EXACT_FRACTION_AUTHOR_UNREVIEWED',
 'model':'18+18 positive auxiliary BRC; causal purchase coins; w erased',
 'eta':str(ETA),'C1':str(C1),'C2':str(C2),
 'vertices':len(verts),'low_tight_count':len(low_tight),
 'high_cost_count':len(high),'other_lower_cost_count':len(low_strict),
 'first_cost_vertex_paid_cost_distribution':dict(sorted(cost_counts.items())),
 'low_strict_min_vertex_slack':str(A),
 'low_tight_high_cross_defects_checked':len(defect),
 'low_tight_high_min_jensen_defect':str(J),
 'cross_pairs_attaining_min_jensen_defect':sum(t==J for t in defect),
 'high_cost_tight_count':sum(gaps[x]==0 for x in high),
 'dual_B':str(B),'dual_lambda':str(LAMBDA),
 'low_resource_purchases_bound':str(HMIN),
 'uniform_resource_charge_tau':str(TAU),
 'new_certified_support_gap':str(DELTA),
 'original_support':str(OLD_SUPPORT),
 'new_all_real_causal_upper_bound':str(NEW_UPPER),
 'previous_author_upper_bound':str(PREVIOUS_UPPER),
 'certified_upper_improvement':str(PREVIOUS_UPPER-NEW_UPPER),
 'unchanged_legal_lower_witness':str(WITNESS_VALUE),
 'remaining_global_interval_width':str(NEW_UPPER-WITNESS_VALUE),
 'scope':'full real causal protocol; author-side finite exact certificate + analytic convexity reduction; not native signed BRC/X6 or independently reviewed'
}
print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
