#!/usr/bin/env python3
"""PREFIX737-R6 exact Gamma left-band exclusion; run in research_notes/portable_direct.
Uses the frozen 189-row kernel and the original PREFIX713/716/718 JSON files.
Python 3 standard library only. Creates a result JSON when all assertions pass.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair

HERE=Path(__file__).resolve().parent
PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
FLOORS={"76":[17346039,22001762,26782554,31680134,36685090,41786898,46973964,52233679,57511868,62800064,68124919,73471219,78823227,84164818,89479630,94751221,99963231,105099542],"77":[18921165,23357463,27922528,32609341,37409778,42314624,47313596,52395384,57547712,62757412,67966070,73179859,78414633,83655183,88885942,94091128,99254892,104361467],"78":[20845249,25061085,29408190,33880742,38471858,43173590,47976936,52871870,57847383,62891546,67991581,73133952,78257514,83381077,88510705,93631369,98727843,103784835]}
def flip(points):
    s={tuple(v) for v in points}
    return s|{(j,i) for i,j in s}
@lru_cache(None)
def bound(a,b,c,d,wm,wv):
    lm,_=pair(a,b)
    _,hi2=pair(c,d)
    gap=wv-hi2+lm*lm
    return min(gap,gap-(wm-lm)/2)
def envelope(i,j,sub,wm,wv):
    return min(bound(F(sub*i+di,384*sub),F(sub*j+dj,384*sub),
                     F(sub*i+di+1,384*sub),F(sub*j+dj+1,384*sub),wm,wv)
               for di in range(sub) for dj in range(sub))
def read(name):
    return json.loads((HERE/name).read_text(encoding="utf-8"))

wm,wm2=pair(F(0),F(73,500)); wv=wm2-wm*wm
om,om2=pair(F(0),F(3,20)); ov=om2-om*om
records=[]
for j in range(76,79):
    for i in range(40,58):
        g1=envelope(i,j,1,wm,wv)
        assert g1<=F(17), (i,j,"unexpected coarse bound")
        g=envelope(i,j,2,wm,wv)
        floor=(1000000*g).numerator//(1000000*g).denominator
        assert floor==FLOORS[str(j)][i-40], (i,j,floor)
        assert g>17, (i,j,"missing certificate",str(g))
        # PREFIX712 uses the old witness on this exact 384 cell. If its
        # endpoint envelope is not positive here, neither it nor its
        # containing 192 parent can be certified by that criterion.
        old=envelope(i,j,1,om,ov)
        assert old<=0, (i,j,"unexpected PREFIX712 overlap")
        records.append((i,j,floor))
assert len(records)==54 and min(v for _,_,v in records)==17346039
new=flip([(i,j) for i,j,_ in records])
assert len(new)==108

a=read("PREFIX713_R6_RESULTS.json")
m=read("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
b=read("PREFIX716_R6_RESULTS.json")
c=read("PREFIX718_R6_RESULTS.json")
assert all(x["scientific_pin"]==PIN for x in (a,m,b,c))
parents=[(2*i+di,2*j+dj) for i,j in a["full_child_parents"]
         for di in (0,1) for dj in (0,1)]
x=a["extra_child"]
parents.append((2*x["parent"][0]+x["subcell"][0],
                2*x["parent"][1]+x["subcell"][1]))
historical={
    "PREFIX713_coupled":flip(parents),
    "PREFIX713_multi":flip([p[:2] for p in m["additional_exact_cells"]["all_q_ge_2"]]),
    "PREFIX716":flip(b["representatives"]),
    "PREFIX718":flip(c["new_half_square_representatives"]),
    "PREFIX733_A":{(i,j) for i in range(30,58) for j in range(30,58)},
    "PREFIX733_B":{(i,j) for i in range(50,70) for j in range(50,70)},
    "PREFIX735":flip((i,j) for i in range(58,70) for j in range(70,76)),
    "PREFIX736":flip((i,j) for i in range(58,70) for j in range(76,96)),
}
assert all(not(new&old) for old in historical.values())
assert 140484+len(new)==140592
assert F(140592,147456)==F(2929,3072)
assert 147456-140592==6864
output=read("PREFIX737_R6_GAMMA_LEFT_BAND_108_RESULTS.json")
if __name__=="__main__":
    (HERE/"PREFIX737_R6_GAMMA_LEFT_BAND_108_RESULTS.json").write_text(
        json.dumps(output,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX737-R6; 108 new cells; min floor",min(v for _,_,v in records))
