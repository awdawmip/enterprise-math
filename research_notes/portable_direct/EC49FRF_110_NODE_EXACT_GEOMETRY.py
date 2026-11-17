#!/usr/bin/env python3
"""EC49FRF exact standalone 98→110 BRC certified-price geometry.
Scientific native Bellman evidence, full profile input and independent DP are in the
self-contained EC49FRF evidence archive; this checker verifies geometry only.
Python stdlib, no network, deterministic integer/fractional arithmetic.
"""
from fractions import Fraction as Q
from math import isqrt
from decimal import Decimal, localcontext
from functools import cmp_to_key
import json

OLD = """1,49/48,25/24,17/16,13/12,53/48,9/8,55/48,7/6,19/16,29/24,59/48,5/4,61/48,31/24,21/16,4/3,65/48,11/8,67/48,17/12,23/16,35/24,71/48,3/2,49/32,25/16,51/32,13/8,53/32,27/16,55/32,7/4,57/32,29/16,59/32,15/8,61/32,31/16,63/32,2,65/32,131/64,33/16,133/64,67/32,135/64,17/8,137/64,69/32,139/64,35/16,141/64,71/32,143/64,9/4,145/64,73/32,147/64,37/16,149/64,75/32,151/64,19/8,153/64,77/32,155/64,39/16,157/64,79/32,159/64,5/2,121/48,61/24,41/16,31/12,125/48,21/8,127/48,8/3,43/16,65/24,131/48,11/4,133/48,67/24,45/16,17/6,137/48,23/8,185/64,93/32,187/64,47/16,189/64,95/32,191/64,3"""
NEW = "107/64,109/64,111/64,113/64,115/64,117/64,119/64,121/64,123/64,125/64,127/64,129/64"
old = list(map(Q, OLD.split(",")))
add = list(map(Q, NEW.split(",")))
new = sorted(set(old + add))
assert old == sorted(set(old)) and len(old) == 98
assert len(add) == 12 and len(new) == 110
assert (old[0],old[-1]) == (Q(1),Q(3))

K=lambda x:Q(7557)-169*x
G=lambda x:310*(3-x)/K(x)
D=Q(2185500)
def area(nodes):
    return sum(((b-a)*(G(a)-G(b)) for a,b in zip(nodes,nodes[1:])),Q(0))
def area_from_k(nodes):
    return D/Q(169**2)*sum((K(a)/K(b)+K(b)/K(a)-2 for a,b in zip(nodes,nodes[1:])),Q(0))
s98,s110=area(old),area(new)
assert s98==area_from_k(old) and s110==area_from_k(new)
assert s98==Q(296902200973874060795,160864097511408031554912)
assert s110==Q(259924479610030238135,162277343928838082317536)
assert s98-s110==Q(13113000,53754785413)>0

# Compare log gaps without logarithms: log K(a)/K(b) is increasing in the rational K ratio.
edges=list(zip(old,old[1:]))
ratios=[K(a)/K(b) for a,b in edges]
ranking=sorted(range(len(edges)),key=lambda i:ratios[i],reverse=True)
picked=ranking[:12]
assert {Q((edges[i][0]+edges[i][1])/2) for i in picked} == set(add)
assert ratios[ranking[11]]>ratios[ranking[12]]
# log(ratio_selected)/2 < log(ratio_13th) is equivalent to ratio_selected < ratio_13th**2
assert all(ratios[i]<ratios[ranking[12]]**2 for i in picked)

# Exact radical enclosure; no decimal comparison decides interval rank.
SCALE=10**40
def root_bracket(z):
    q=isqrt(z.numerator*SCALE*SCALE//z.denominator)
    low,high=Q(q,SCALE),Q(q+1,SCALE)
    assert low*low<=z<high*high
    return low,high
def regret_bounds(a,b):
    al,au=root_bracket(K(a));bl,bu=root_bracket(K(b))
    return Q(50)*(b-a)/(au+bu)**2, Q(50)*(b-a)/(al+bl)**2
rows=[(a,b,*regret_bounds(a,b)) for a,b in zip(new,new[1:])]
old_rows=[(a,b,*regret_bounds(a,b)) for a,b in zip(old,old[1:])]
best=max(rows,key=lambda row:row[2]); previous=max(old_rows,key=lambda row:row[2])
assert all(best[2]>row[3] for row in rows if row is not best)
assert all(previous[2]>row[3] for row in old_rows if row is not previous)
assert best[3]<previous[2]
assert (best[0],best[1])==(Q(13,8),Q(53,32))
assert (previous[0],previous[1])==(Q(2),Q(65,32))

with localcontext() as ctx:
    ctx.prec=65
    dec=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
    regret=lambda a,b:Decimal(50)*dec(b-a)/(dec(K(a)).sqrt()+dec(K(b)).sqrt())**2
    result={
      "schema":"EC49FRF_110_NODE_GEOMETRY_EXACT",
      "old_node_count":len(old),"new_node_count":len(new),
      "S98":str(s98),"S110":str(s110),"strict_gain":str(s98-s110),
      "certified_fraction_lower_bound":str(Q(1)-s110/2),
      "certified_percent_lower_bound":str(100*(Q(1)-s110/2)),
      "new_price_nodes":list(map(str,add)),
      "new_worst_interval":[str(best[0]),str(best[1])],
      "previous_worst_interval":[str(previous[0]),str(previous[1])],
      "old_max_regret_over_t":str(regret(previous[0],previous[1])),
      "new_max_regret_over_t":str(regret(best[0],best[1])),
      "top_twelve_allocation_exact_rational_comparisons":True,
      "all_109_regret_intervals_outward_bracket_checked":True,
      "native_scientific_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
      "scope":"GEOMETRIC_INTERPOLATION_ONLY; NATIVE_BELLMAN_CERTIFICATES_IN_ARCHIVE"
    }
    print(json.dumps(result,indent=2))
    print("EC49FRF_EXACT_GEOMETRY_VERIFIED")
