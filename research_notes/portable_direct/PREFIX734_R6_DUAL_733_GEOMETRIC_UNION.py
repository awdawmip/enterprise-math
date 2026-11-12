#!/usr/bin/env python3
"""PREFIX-734: exact grid-set union of the two distinct PREFIX-733 certificates.
Run from research_notes/portable_direct. Python standard library only.
This checks source claims and count geometry, not Gamma moment inequalities.
"""
import json
from pathlib import Path
from fractions import Fraction
root=Path(__file__).resolve().parent
def load(name): return json.loads((root/name).read_text(encoding="utf-8"))
c=load("PREFIX732_R6_RESULTS.json")
a=load("PREFIX733_R6_SUMMARY.json") # adaptive 28x28
b=load("PREFIX733_R6_RESULTS.json") # half-tile 20x20, same PREFIX733 label
pin="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert c["scientific_pin"]==a["frozen_science_pin"]==b["frozen_science_pin"]==pin
assert a["schema"]=="PREFIX733_R6_ADAPTIVE_GAMMA_SUMMARY_V1"
assert b["schema"]=="PREFIX733_R6_HALF_TILE_400_ALL_Q_CERTIFICATE_V1"
assert c["new_certified_all_q_total"]==a["prior_certified"]==b["prior_732_certified"]==139140
assert a["whole_cells_certified_by_new_region"]==784
assert a["prior_inner_square_overlap"]==144
assert a["prefix712_old_outer_overlap"]==136
assert a["outer_cells"]==640 and a["new_cells"]==504
assert a["total_certified"]==139644
assert all(x==0 for x in a["later_explicit_overlaps"].values())
assert b["ordered_whole_grid_cells"]==b["deduplicated_new_cells"]==400
assert b["old_PREFIX712_overlap"]==0
assert all(x==0 for x in b["later_certificate_overlap"].values())
assert b["all_q_certified"]==139540
assert a["comparator"]==b["witness"]==["0","73/500"]
A={(i,j) for i in range(30,58) for j in range(30,58)}
B={(i,j) for i in range(50,70) for j in range(50,70)}
inner={(i,j) for i in range(38,50) for j in range(38,50)}
intersection=A&B
assert len(A)==784 and len(B)==400 and len(inner)==144
assert len(intersection)==64 and intersection=={
 (i,j) for i in range(50,58) for j in range(50,58)}
assert not (B&inner)
# A overlaps old certified union in 144 inner + 136 PREFIX712 outer cells.
# B's predecessor certificate asserts zero prior-union overlap.
assert len(A)-len(inner)-a["prefix712_old_outer_overlap"]==504
new=a["new_cells"]+b["deduplicated_new_cells"]-len(intersection)
total=c["new_certified_all_q_total"]+new
frac=Fraction(total,384*384)
assert (new,total,frac,384*384-total)==(840,139980,Fraction(11665,12288),7476)
out={
 "schema":"PREFIX734_R6_DUAL_733_GEOMETRIC_UNION_V1",
 "scientific_pin":pin,"q_domain":"real q >= 2",
 "predecessors":["PREFIX732_R6_RESULTS.json","PREFIX733_R6_SUMMARY.json","PREFIX733_R6_RESULTS.json"],
 "A_28x28":784,"B_20x20":400,"intersection":64,
 "A_old_overlap":280,"B_old_overlap":0,
 "A_new":504,"B_new":400,"unique_new":new,
 "prior_certified":139140,"new_certified":total,"grid_total":147456,
 "exact_fraction":"11665/12288","percent":float(100*frac),
 "not_yet_certified":7476,
 "grade":"AUTHOR_EXACT_SET_ARITHMETIC_WITH_INHERITED_AUTHOR_GAMMA_CERTIFICATES; UNREVIEWED",
 "verification":"ALL_CHECKS_PASS PREFIX734-R6-UNION"}
if __name__=="__main__":
 (root/"PREFIX734_R6_UNION_RESULTS.json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(out["verification"],"new=",new,"total=",total,"fraction=",frac)
