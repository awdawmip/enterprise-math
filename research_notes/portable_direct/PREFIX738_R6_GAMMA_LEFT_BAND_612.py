#!/usr/bin/env python3
"""PREFIX738-R6: exact all-q Gamma exclusion for 612 new 384-grid cells.

Run from research_notes/portable_direct after the PREFIX731 center-variance
SHA256 literal repair. Uses only Python standard library and frozen PIN
f42f2906d77f24085c123f3ccfe9667d41caa96d. No task claim is inferred.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair

HERE = Path(__file__).resolve().parent
PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
FLOOR_BY_J = {
    79:23100177, 80:25666322, 81:28522867, 82:31648103,
    83:35019735, 84:38615165, 85:42411756, 86:46387080,
    87:50519140, 88:54786572, 89:59168811, 90:63646250,
    91:68200362, 92:72813804, 93:77470499, 94:82155704,
    95:86856046
}
wm, wm2 = pair(F(0), F(73,500))
wv = wm2 - wm*wm
om, om2 = pair(F(0), F(3,20))
ov = om2 - om*om

@lru_cache(maxsize=512)
def lower(a,b,c,d,w_mu,w_var):
    low_mu, _ = pair(a,b)
    _, high_m2 = pair(c,d)
    delta = w_var - high_m2 + low_mu*low_mu
    return min(delta, delta - (w_mu-low_mu)/2)

def envelope(i,j,sub,w_mu,w_var):
    return min(
        lower(F(sub*i+di,384*sub),F(sub*j+dj,384*sub),
              F(sub*i+di+1,384*sub),F(sub*j+dj+1,384*sub),
              w_mu,w_var)
        for di in range(sub) for dj in range(sub))

def flip(items):
    data = {tuple(v) for v in items}
    return data | {(j,i) for i,j in data}

def load(name):
    return json.loads((HERE/name).read_text(encoding="utf-8"))

rows=[]
for j in range(79,96):
    for i in range(40,58):
        g = envelope(i,j,2,wm,wv)
        assert g>20, (i,j,"Gamma lower gap is not >20")
        scaled = g*1000000
        floored = scaled.numerator//scaled.denominator
        old = envelope(i,j,1,om,ov)
        # PREFIX712: the frozen all-q old-witness certificate uses the
        # unrefined 384-child / containing 192-parent envelope. If this
        # exact child envelope is nonpositive, those cells are absent.
        assert old<=0, (i,j,"unexpected PREFIX712 intersection")
        rows.append([i,j,floored])
    jmin = min(r[2] for r in rows if r[1]==j)
    assert jmin==FLOOR_BY_J[j], (j,jmin)
    # Keep exact arithmetic bounded in memory across the 17 j-rows.
    pair.cache_clear()
    lower.cache_clear()

assert len(rows)==306
new = flip([(i,j) for i,j,_ in rows])
assert len(new)==612
a=load("PREFIX713_R6_RESULTS.json")
m=load("PREFIX713_R6_MULTICOMPETITOR_RESULTS.json")
b=load("PREFIX716_R6_RESULTS.json")
c=load("PREFIX718_R6_RESULTS.json")
assert all(x["scientific_pin"]==PIN for x in (a,m,b,c))
coupled=[(2*i+di,2*j+dj) for i,j in a["full_child_parents"]
         for di in (0,1) for dj in (0,1)]
x=a["extra_child"]
coupled.append((2*x["parent"][0]+x["subcell"][0],
                2*x["parent"][1]+x["subcell"][1]))
prior={
    "PREFIX713_coupled":flip(coupled),
    "PREFIX713_multi":flip([v[:2] for v in m["additional_exact_cells"]["all_q_ge_2"]]),
    "PREFIX716":flip(b["representatives"]),
    "PREFIX718":flip(c["new_half_square_representatives"]),
    "PREFIX733_A":{(i,j) for i in range(30,58) for j in range(30,58)},
    "PREFIX733_B":{(i,j) for i in range(50,70) for j in range(50,70)},
    "PREFIX735":flip((i,j) for i in range(58,70) for j in range(70,76)),
    "PREFIX736":flip((i,j) for i in range(58,70) for j in range(76,96)),
    "PREFIX737":flip((i,j) for i in range(40,58) for j in range(76,79))
}
assert all(not (new & cells) for cells in prior.values())
assert min(r[2] for r in rows)==23100177
assert 140592+len(new)==141204
assert F(141204,147456)==F(58835,61440)
assert 147456-141204==6252

result={
    "schema":"PREFIX738_R6_GAMMA_LEFT_BAND_612_V1",
    "frozen_scientific_pin":PIN,
    "model":"independent Gamma auxiliary maximum with 189 frozen BRC stop-count rows",
    "q_domain":"all real q>=2",
    "witness":["0","73/500"],
    "upper_region":{"i":[40,58],"j":[79,96],"denominator":384},
    "split_per_cell":2,
    "n_upper":306,"n_reflected":612,
    "min_floor_times_1000000":23100177,
    "per_j_min_floor_times_1000000":FLOOR_BY_J,
    "strict_gap":"V_q(witness)-V_q(p,z)>20*q^2",
    "old_witness_712_intersections":0,
    "other_historical_intersections":{k:len(new&v) for k,v in prior.items()},
    "previous_union":140592,"new_union":141204,
    "grid_total":147456,"unexcluded":6252,
    "new_upper_coordinates":[[i,j] for i,j,_ in rows],
    "all_306_upper_cell_floors":[r for r in rows],
    "validation":"ALL_CHECKS_PASS PREFIX738-R6",
    "grade":"AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
if __name__=="__main__":
    (HERE/"PREFIX738_R6_GAMMA_LEFT_BAND_612_RESULTS_REGENERATED.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("ALL_CHECKS_PASS PREFIX738-R6; 612 new cells; min floor",min(r[2] for r in rows))
