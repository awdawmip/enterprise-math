#!/usr/bin/env python3
"""PREFIX-732: deduplicate PREFIX-731's 144 whole Gamma-grid cells.
Frozen mathematical input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses the exact integer BRC+Gamma kernel from PREFIX731 and the immutable predecessor
results PREFIX713/716/718/730. All decisions use Fraction or integer comparisons.
Run in research_notes/portable_direct with Python 3 standard library.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair, result as r731

ROOT=Path(__file__).resolve().parent
PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert r731["frozen_science_pin"]==PIN
assert r731["whole_grid_cells_independently_certified"]==144
assert r731["minimum_floor"]==46
def read(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))
a713=read("PREFIX713_R6_RESULTS.json")
m713=read("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
a716=read("PREFIX716_R6_RESULTS.json")
a718=read("PREFIX718_R6_RESULTS.json")
a730=read("PREFIX730_R6_RESULTS.json")
assert all(d["scientific_pin"]==PIN for d in (a713,m713,a716,a718))
assert a730["frozen_science_pin"]==PIN and a730["new_all_q_cells"]==139076

def reflected(points):
    v=set(map(tuple,points))
    return v | {(j,i) for i,j in v}

coupled=[(2*i+di,2*j+dj)
         for i,j in a713["full_child_parents"]
         for di in (0,1) for dj in (0,1)]
last=a713["extra_child"]
coupled.append((2*last["parent"][0]+last["subcell"][0],
                2*last["parent"][1]+last["subcell"][1]))
later={
 "PREFIX713_coupled":reflected(coupled),
 "PREFIX713_multi":reflected([x[:2] for x in m713["additional_exact_cells"]["all_q_ge_2"]]),
 "PREFIX716":reflected(a716["representatives"]),
 "PREFIX718":reflected(a718["new_half_square_representatives"]),
}
assert [len(v) for v in later.values()]==[90,20,1590,150]

# PREFIX-712's all-q certificate uses e0=(0,3/20) and the monotone
# low-mean/high-second-moment rectangle envelope. Its t-endpoints are 0,1/2.
e_mu,e_m2=pair(F(0),F(3,20))
e_w=e_m2-e_mu*e_mu
@lru_cache(None)
def old_all_q(a,b,c,d):
    lo_mu,_=pair(F(a,384),F(b,384))
    _,hi_m2=pair(F(c,384),F(d,384))
    U=hi_m2-lo_mu*lo_mu
    return e_w-U>0 and e_w-e_mu/2-(U-lo_mu/2)>0

old=set()
coarse=[]
for a in range(38,50,2):
    for b in range(38,50,2):
        if old_all_q(a,b,a+2,b+2):
            coarse.append((a,b))
            old.update((a+di,b+dj) for di in (0,1) for dj in (0,1))
        else:
            for di in (0,1):
                for dj in (0,1):
                    i,j=a+di,b+dj
                    if old_all_q(i,j,i+1,j+1):
                        old.add((i,j))

square={(i,j) for i in range(38,50) for j in range(38,50)}
inner={(i,j) for i in range(40,48) for j in range(40,48)}
old64=old & inner
assert len(square)==144 and len(inner)==64
assert len(old)==22 and len(old64)==6 and not coarse
assert old64=={(40,40),(40,41),(41,40),(41,41),(40,42),(42,40)}
assert a730["old_base_overlap_count"]==len(old64)
later_overlaps={k:sorted(square & s) for k,s in later.items()}
assert not any(later_overlaps.values())
assert len(old-inner)==16
newcells=sorted(square-(old|inner))
assert len(newcells)==64
updated=a730["new_all_q_cells"]+len(newcells)
assert updated==139140
assert F(updated,384*384)==F(3865,4096)
out={
 "schema":"PREFIX732_R6_DEDUPLICATED_GAMMA_144_GRID_V1",
 "scientific_pin":PIN,
 "source_certificate":"PREFIX731-R6",
 "source_certificate_gap":"V_q(0,73/500)-V_q(p,z)>40*q^2 for all real q>=2 on [38/384,50/384]^2",
 "grid_denominator":384,
 "total_grid_cells":147456,
 "old_prefix730_certified":a730["new_all_q_cells"],
 "prefix731_independent_block":144,
 "inherited_prefix729_block":64,
 "prefix712_all_q_old_overlap_144":len(old),
 "prefix712_all_q_old_overlap_inner64":len(old64),
 "prefix712_old_outer_overlap":16,
 "prefix712_coarse_2x2_parents":list(map(list,coarse)),
 "prefix712_old_overlap_indices":[list(x) for x in sorted(old)],
 "later_certificate_overlaps":{k:len(v) for k,v in later_overlaps.items()},
 "new_deduplicated_cells":len(newcells),
 "new_deduplicated_indices":[list(x) for x in newcells],
 "new_certified_all_q_total":updated,
 "new_exact_fraction":"3865/4096",
 "new_percentage":94.3603515625,
 "verification":"ALL_CHECKS_PASS PREFIX732-R6",
 "grade":"AUTHOR_EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if False:
    (ROOT/"PREFIX732_R6_RESULTS.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX732-R6; +64; 139140/147456 = 3865/4096")

# PREFIX733-R6: extend exact 144-cell predecessor union with 400 new cells.
# Parent PREFIX732 calculations above remain active; its standalone output
# block is suppressed in this combined reproducer.
e_mu733,e_m2_733=pair(F(0),F(73,500))
e_w733=e_m2_733-e_mu733**2

@lru_cache(None)
def half_tile_gap733(i,j):
    gaps=[]
    for a in (2*i,2*i+1):
        for b in (2*j,2*j+1):
            low_mu,_=pair(F(a,768),F(b,768))
            _,high_m2=pair(F(a+1,768),F(b+1,768))
            upper_var=high_m2-low_mu**2
            g0=e_w733-upper_var
            ghalf=g0-(e_mu733-low_mu)/2
            gaps.append(min(g0,ghalf))
    return min(gaps)

minimum733=None
worst733=None
for i in range(50,70):
    for j in range(i,70):
        g=half_tile_gap733(i,j)
        assert g>0,(i,j,g)
        if minimum733 is None or g<minimum733:
            minimum733,worst733=g,[i,j]
        assert not old_all_q(i,j,i+1,j+1),("PREFIX712 overlap",i,j)
assert 76<minimum733<77 and worst733==[50,69]
new_square733={(i,j) for i in range(50,70) for j in range(50,70)}
assert len(new_square733)==400
assert new_square733.isdisjoint(square) and new_square733.isdisjoint(inner)
assert not any(new_square733 & s for s in later.values())
new_total733=updated+400
assert new_total733==139540 and F(new_total733,384**2)==F(34885,36864)
result733={
    "schema":"PREFIX733_R6_HALF_TILE_400_ALL_Q_CERTIFICATE_V1",
    "frozen_science_pin":PIN,
    "observer":"189-row BRC stopped-count, independent unit-rate Gamma maximum",
    "parameter_region":"[50/384,70/384]^2",
    "q_domain":"all real q >= 2",
    "witness":["0","73/500"],
    "fine_grid_denominator":384,
    "subtile_denominator":768,
    "ordered_whole_grid_cells":400,
    "symmetry_reduced_cells":210,
    "exact_rational_endpoint_comparisons":1680,
    "minimum_gap_integer_floor":minimum733.numerator//minimum733.denominator,
    "worst_cell_representative":worst733,
    "uniform_strict_gap":"V_q(witness)-V_q(p,z)>76*q^2",
    "old_PREFIX712_overlap":0,
    "later_certificate_overlap":{k:len(new_square733&s) for k,s in later.items()},
    "prior_732_certified":updated,
    "deduplicated_new_cells":400,
    "all_q_certified":new_total733,
    "total_cells":384**2,
    "exact_fraction":"34885/36864",
    "percentage":float(F(new_total733,384**2)*100),
    "unexcluded_cells":384**2-new_total733,
    "verification":"ALL_CHECKS_PASS PREFIX733-R6",
    "grade":"AUTHOR_EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if __name__=="__main__":
    (ROOT/"PREFIX733_R6_RESULTS.json").write_text(
        json.dumps(result733,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX733-R6; +400; 139540/147456 = 34885/36864")
