#!/usr/bin/env python3
"""PREFIX751: exact /384-to-/768 Gamma support audit. Python 3 standard library.
Run from research_notes/portable_direct with historical JSON files present.
Integer-set geometry ONLY; does not recompute the Gamma inequalities.
"""
import json
from pathlib import Path

D = Path(__file__).resolve().parent
def load(name):
    return json.loads((D / name).read_text(encoding="utf-8"))
def xy(rows):
    return {(int(row[0]), int(row[1])) for row in rows}
def mirror(s):
    return s | {(j,i) for i,j in s}
def box(i0,i1,j0,j1):
    return {(i,j) for i in range(i0,i1) for j in range(j0,j1)}
def fine(s):
    return {(2*i+a,2*j+b) for i,j in s for a in (0,1) for b in (0,1)}
def upper(name,field):
    return xy(load(name)[field])

G = {}
G["A733"] = box(30,58,30,58)
G["B733"] = box(50,70,50,70)
G["P735"] = box(58,70,70,76)
G["P736"] = box(58,70,76,96)
G["P737"] = box(40,58,76,79)
G["P738"] = box(40,58,79,96)
G["P739"] = {(i,j) for j,hi in
              ((96,58),(97,58),(98,58),(99,58),(100,58),
               (101,58),(102,58),(103,55),(104,52),(105,46))
              for i in range(40,hi)}
G["P740"] = box(58,70,96,104)
G["P741"] = upper("PREFIX741_R6_INNER_STRIP_194_RESULTS.json","per_upper_cell_microfloors")
for tag,filename in (
    ("P742","PREFIX742_R6_GAMMA_LEFT_EXTENSION_36_RESULTS.json"),
    ("P743","PREFIX743_R6_GAMMA_LEFT_EXTENSION_30_RESULTS.json"),
    ("P744","PREFIX744_R6_ADAPTIVE_4X4_16_RESULTS.json"),
    ("P745","PREFIX745_R6_GAMMA_140_RESULTS.json")):
    G[tag] = upper(filename,"checked_upper_cells")
G["P746_749"] = upper("PREFIX_R6_GAMMA_SIBLING_UNION_746_749_RESULTS.json",
                      "all_unique_upper_pairs")
expected = dict(A733=784,B733=400,P735=72,P736=240,P737=54,
                P738=306,P739=159,P740=96,P741=97,P742=18,
                P743=15,P744=8,P745=70,P746_749=197)
assert {name:len(v) for name,v in G.items()} == expected
MACRO = set()
net = {}
for name,s in G.items():
    m=mirror(s)
    net[name]=(len(m),len(m&MACRO))
    MACRO |= m
assert len(box(30,58,30,58) & box(50,70,50,70)) == 64
assert net["B733"] == (400,64),net
assert net["P746_749"] == (394,2),net
assert all(k=="B733" or k=="P746_749" or overlap==0
           for k,(_,overlap) in net.items()),net
assert mirror(G["A733"]) & mirror(G["P746_749"]) == {(30,52),(52,30)}
assert len(MACRO)==3782,len(MACRO)
FINE=fine(MACRO)
assert len(FINE)==15128,len(FINE)
b=load("PREFIX713_R6_RESULTS.json")
coupled=fine(xy(b["full_child_parents"]))
p=b["extra_child"]
coupled.add((2*p["parent"][0]+p["subcell"][0],2*p["parent"][1]+p["subcell"][1]))
c=load("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
OLD={
  "PREFIX713_coupled":mirror(coupled),
  "PREFIX713_multicomp":xy(c["additional_exact_cells"]["all_q_ge_2"]),
  "PREFIX716":mirror(upper("PREFIX716_R6_RESULTS.json","representatives")),
  "PREFIX718":mirror(upper("PREFIX718_R6_RESULTS.json","new_half_square_representatives"))
}
assert {k:len(v) for k,v in OLD.items()} == {
   "PREFIX713_coupled":90,"PREFIX713_multicomp":20,
   "PREFIX716":1590,"PREFIX718":150}
assert len(set().union(*OLD.values()))==1850
assert {k:len(FINE&v) for k,v in OLD.items()}=={
   "PREFIX713_coupled":0,"PREFIX713_multicomp":14,
   "PREFIX716":244,"PREFIX718":84}
old712=load("PREFIX750B_R6_712_FINE_CHILD_OVERLAP_RESULTS.json")
known712=mirror(xy(old712["result"]["explicit_positive_fine_upper_children_microfloor"]))
assert len(known712)==54 and len(FINE&known712)==54
assert len(fine(mirror(G["A733"]))&known712)==8
assert len(fine(mirror(G["P746_749"]))&known712)==54
assert 15128-(14+244+84)==14786
assert 14786-(147456-139018)==6348
print("PASS 3782 macro; 15128 original fine; explicit historical 342; "
      "necessary PREFIX712 overlap >=6348")
print("KNOWN old PREFIX712 subset in sibling",len(known712))
print("FULL HISTORICAL UNION NOT DETERMINED: missing original PREFIX712 mask")
