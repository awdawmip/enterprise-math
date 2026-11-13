#!/usr/bin/env python3
"""PREFIX-750C-R6: original-PREFIX712 /768 fine-grid union of:
  inherited PREFIX712+713+716+718 source certificates,
  and 11 PREFIX746–749 sibling macro rectangle certificates.
Consumes exact source JSON and PREFIX750B's exact old fine-child scan.
Checks *coordinate* overlap and prior inherited count, not analytic Gamma inequalities.
"""
import json
from pathlib import Path
from fractions import Fraction
D=Path(__file__).resolve().parent
load=lambda p: json.loads((D/p).read_text(encoding="utf-8"))
s=load("PREFIX_R6_GAMMA_SIBLING_UNION_746_749_RESULTS.json")
a=load("PREFIX750B_R6_712_FINE_CHILD_OVERLAP_RESULTS.json")
b=load("PREFIX713_R6_RESULTS.json")
c=load("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
d=load("PREFIX716_R6_RESULTS.json")
e=load("PREFIX718_R6_RESULTS.json")
def mirror(items):
    return {(int(i),int(j)) for i,j,*_ in items}|{(int(j),int(i)) for i,j,*_ in items}
def children(items):
    return {(2*i+x,2*j+y) for i,j in items for x in (0,1) for y in (0,1)}
S=mirror(children(s["all_unique_upper_pairs"]))
old=mirror(a["result"]["explicit_positive_fine_upper_children_microfloor"])
coupled_upper=set(children(b["full_child_parents"]))
p=b["extra_child"]
coupled_upper.add((2*p["parent"][0]+p["subcell"][0],2*p["parent"][1]+p["subcell"][1]))
coupled=mirror(coupled_upper)
multi={(x[0],x[1]) for x in c["additional_exact_cells"]["all_q_ge_2"]}
source716=mirror(d["representatives"])
source718=mirror(e["new_half_square_representatives"])
groups=[("PREFIX712_OLD",old,54),("PREFIX713_COUPLED",coupled,0),
        ("PREFIX713_MULTICOMP",multi,2),("PREFIX716",source716,94),
        ("PREFIX718",source718,84)]
prior=set()
for name,group,expected_overlap in groups:
    assert not group&prior, (name,"historical source families collision")
    overlapping=S&group
    assert len(overlapping)==expected_overlap,(name,len(overlapping))
    prior|=group
    print("PASS",name,"prior",len(group),"overlap sibling",len(overlapping))
assert len(prior)==1904
assert len(S)==1576
assert len(S&prior)==234
assert 139018+len(S-prior)==140360
assert 147456-140360==7096
assert Fraction(140360,147456)==Fraction(17545,18432)
print("ALL_CHECKS_PASS PREFIX750C-R6 234 overlapping fine cells; 1342 novel vs PREFIX718; 140360 conditional partial union")
