#!/usr/bin/env python3
"""PREFIX-736-R6: exact Gamma all-real-q>=2 transverse strip extension.

Run in research_notes/portable_direct with PREFIX731 exact frozen kernel and
the original PREFIX713/716/718 source JSON. Python 3 standard library only.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from collections import Counter
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair

ROOT = Path(__file__).resolve().parent
PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
wm,wm2 = pair(F(0),F(73,500)); wv=wm2-wm*wm
om,om2 = pair(F(0),F(3,20)); ov=om2-om*om

def reflect(points):
    p={tuple(x) for x in points}
    return p | {(j,i) for i,j in p}

@lru_cache(None)
def bound(a,b,c,d,w_mu,w_var):
    lm,_=pair(a,b)
    _,hm2=pair(c,d)
    delta=w_var-hm2+lm*lm
    return min(delta, delta-(w_mu-lm)/2)

def envelope(i,j,k,w_mu,w_var):
    return min(bound(F(k*i+di,384*k),F(k*j+dj,384*k),
                     F(k*i+di+1,384*k),F(k*j+dj+1,384*k),w_mu,w_var)
               for di in range(k) for dj in range(k))

records=[]; overlap712=[]; new_upper=[]
for j in range(76,96):
    for i in range(58,70):
        g=envelope(i,j,1,wm,wv); k=1
        if g<=F(1,10):
            g=envelope(i,j,2,wm,wv); k=2
        assert g>F(1,10),(i,j,g)
        old=envelope(i,j,1,om,ov)>0
        records.append([i,j,k,(g*1000000).numerator//(g*1000000).denominator])
        if old: overlap712.append((i,j))
        else: new_upper.append((i,j))
assert len(records)==240
assert Counter(x[2] for x in records)=={1:52,2:188}
assert min(x[3] for x in records)==110609
assert len(overlap712)==53 and len(new_upper)==187
assert all(i<j for i,j in new_upper)
new_cells=reflect(new_upper)
assert len(new_cells)==374

def load(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))
a=load('PREFIX713_R6_RESULTS.json')
m=load('PREFIX713_R6_MULTICOMPETITOR_RESULTS.json')
b=load('PREFIX716_R6_RESULTS.json')
c=load('PREFIX718_R6_RESULTS.json')
assert all(x['scientific_pin']==PIN for x in (a,m,b,c))
coupled=[(2*i+di,2*j+dj) for i,j in a['full_child_parents']
         for di in (0,1) for dj in (0,1)]
x=a['extra_child']
coupled.append((2*x['parent'][0]+x['subcell'][0],
                2*x['parent'][1]+x['subcell'][1]))
prior_sets={
 'PREFIX713_coupled':reflect(coupled),
 'PREFIX713_multi':reflect([x[:2] for x in m['additional_exact_cells']['all_q_ge_2']]),
 'PREFIX716':reflect(b['representatives']),
 'PREFIX718':reflect(c['new_half_square_representatives']),
 'PREFIX733_A':{(i,j) for i in range(30,58) for j in range(30,58)},
 'PREFIX733_B':{(i,j) for i in range(50,70) for j in range(50,70)},
 'PREFIX735':reflect([(i,j) for i in range(58,70) for j in range(70,76)])
}
assert all(not(new_cells&s) for s in prior_sets.values())
assert 140110+len(new_cells)==140484
assert 147456-140484==6972
assert F(140484,147456)==F(11707,12288)
out={
 'schema':'PREFIX736_R6_OUTER_TRANSVERSE_374_ALL_Q_V1',
 'date':'2026-11-13 Asia/Shanghai',
 'scientific_pin':PIN,
 'source_kernel':'PREFIX731_R6_MONOTONE_MOMENT_TILE.py',
 'gamma_observer':'189 stopped-count rows, independent Gamma maximum',
 'region_upper':'58<=i<70,76<=j<96 in 384x384 cell indices; plus transposes',
 'comparison_witness':['0','73/500'],
 'q_domain':'all real q>=2',
 'strict_uniform_gap':'V_q(e)-V_q(p,z)>q^2/10',
 'exact_author_checked_cells':240,
 'coarse_384_cells':52,
 'halfgrid_768_subdivided_cells':188,
 'minimum_gap_floor_times_one_million':110609,
 'minimum_margin_cell':[67,88],
 'old_PREFIX712_overlap_upper':[list(t) for t in overlap712],
 'old_PREFIX712_overlap_upper_count':len(overlap712),
 'other_historical_overlap_counts':{k:len(new_cells&s) for k,s in prior_sets.items()},
 'new_upper_cell_count':len(new_upper),
 'new_total_with_transposes':len(new_cells),
 'new_upper_cell_coordinates':[list(t) for t in new_upper],
 'per_cell_minimum_floor_records':records,
 'previous_author_union':140110,
 'new_author_union':140484,
 'grid_total':147456,
 'certified_fraction':'11707/12288',
 'not_yet_certified':6972,
 'verification':'ALL_CHECKS_PASS PREFIX736-R6',
 'status':'AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    (ROOT/'PREFIX736_R6_OUTER_TRANSVERSE_374_RESULTS.json').write_text(
        json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(out['verification'],len(new_cells),'min floor',min(x[3] for x in records))
