#!/usr/bin/env python3
"""PREFIX-733-R6. Exact all-q Gamma tile extension and union deduplication.

Science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run from research_notes/portable_direct with Python3 stdlib; no floats decide proof.
Depends on PREFIX731_R6_MONOTONE_MOMENT_TILE.py and four earlier all-q data
sets, plus PREFIX732_R6_RESULTS.json.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair, result as r731

PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert r731['frozen_science_pin']==PIN
assert r731['whole_grid_cells_independently_certified']==144
ROOT=Path(__file__).resolve().parent
def read(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
prev=read('PREFIX732_R6_RESULTS.json')
a713=read('PREFIX713_R6_RESULTS.json')
m713=read('PREFIX713_R6_MULTICOMPETITOR_RESULTS.json')
a716=read('PREFIX716_R6_RESULTS.json')
a718=read('PREFIX718_R6_RESULTS.json')
assert prev['scientific_pin']==PIN and prev['new_certified_all_q_total']==139140
assert all(x['scientific_pin']==PIN for x in (a713,m713,a716,a718))
e_mu,e_m2=pair(F(0),F(73,500));e_W=e_m2-e_mu**2
@lru_cache(None)
def gaps(xlo,ylo,xhi,yhi):
    mu,_=pair(xlo,ylo);_,m2=pair(xhi,yhi)
    U=m2-mu*mu
    a=e_W-U
    b=a-(e_mu-mu)/2
    return a,b
base_fail=[]
positive_leaf=0
split_count=0
max_depth=0
min_floor=10**6
def certify(xlo,ylo,xhi,yhi,depth=0):
    global positive_leaf,split_count,max_depth,min_floor
    a,b=gaps(xlo,ylo,xhi,yhi)
    if a>0 and b>0:
        positive_leaf+=1
        max_depth=max(max_depth,depth)
        min_floor=min(min_floor,a.numerator//a.denominator,b.numerator//b.denominator)
        return
    assert depth<4, ('unresolved tile',xlo,ylo,xhi,yhi)
    split_count+=1
    mx=(xlo+xhi)/2;my=(ylo+yhi)/2
    for u,v,w,t in ((xlo,ylo,mx,my),(mx,ylo,xhi,my),
                    (xlo,my,mx,yhi),(mx,my,xhi,yhi)):
        certify(u,v,w,t,depth+1)
lo,hi=30,58
edges=[F(lo,384)+F(i,576) for i in range(43)]
assert edges[-1]==F(hi,384)
for i in range(42):
    for j in range(i,42):
        u,v=edges[i],edges[j]
        w,t=edges[i+1],edges[j+1]
        a,b=gaps(u,v,w,t)
        if a<=0 or b<=0:base_fail.append([i,j])
        certify(u,v,w,t)
assert split_count==len(base_fail) and max_depth<=1
assert len(base_fail)==87 and positive_leaf==903+3*87
def reflect(points):
    v=set(map(tuple,points))
    return v | {(j,i) for i,j in v}
coupled=[(2*i+di,2*j+dj) for i,j in a713['full_child_parents']
         for di in (0,1) for dj in (0,1)]
extra=a713['extra_child']
coupled.append((2*extra['parent'][0]+extra['subcell'][0],
                2*extra['parent'][1]+extra['subcell'][1]))
later={
    'PREFIX713_coupled':reflect(coupled),
    'PREFIX713_multi':reflect([row[:2] for row in m713['additional_exact_cells']['all_q_ge_2']]),
    'PREFIX716':reflect(a716['representatives']),
    'PREFIX718':reflect(a718['new_half_square_representatives']),
}
assert [len(v) for v in later.values()]==[90,20,1590,150]
square={(i,j) for i in range(lo,hi) for j in range(lo,hi)}
inner={(i,j) for i in range(38,50) for j in range(38,50)}
outer=square-inner
assert len(square)==784 and len(inner)==144 and len(outer)==640
old_mu,old_m2=pair(F(0),F(3,20));old_w=old_m2-old_mu**2
old_outer=set()
for i in range(lo,hi):
    for j in range(i,hi):
        if (i,j) not in outer:continue
        u,_=pair(F(i,384),F(j,384))
        _,m2=pair(F(i+1,384),F(j+1,384))
        cap=m2-u*u
        if old_w-cap>0 and old_w-old_mu/2-(cap-u/2)>0:
            old_outer.add((i,j));old_outer.add((j,i))
assert len(old_outer)==136
later_overlap={key:len(square & val) for key,val in later.items()}
assert all(v==0 for v in later_overlap.values()),later_overlap
new_outer=sorted(outer-old_outer)
assert len(new_outer)==504
assert 139140+len(new_outer)==139644
assert F(139644,384**2)==F(3879,4096)
result={
  'schema':'PREFIX733_R6_ADAPTIVE_GAMMA_28X28_V1',
  'frozen_science_pin':PIN,
  'observer':'189-row BRC stopped-count; independent unit-rate Gamma maximum',
  'witness':['0','73/500'],
  'domain':'all real q>=2, p,z in [30/384,58/384]',
  'symmetry_reduced_base_tiles':903,
  'base_failed_tiles_repaired':len(base_fail),
  'base_failed_tile_representatives':base_fail,
  'split_nodes':split_count,
  'max_refinement_depth':max_depth,
  'positive_leaf_tests':positive_leaf,
  'min_positive_leaf_endpoint_floor':min_floor,
  'whole_grid_cells_independently_certified':len(square),
  'previous_certified_total':139140,
  'prior_small_square_cells':len(inner),
  'prior_prefix712_overlap_in_outer':len(old_outer),
  'prior_prefix712_overlap_indices':sorted(map(list,old_outer)),
  'later_certificate_overlaps':later_overlap,
  'new_deduplicated_cells':len(new_outer),
  'new_deduplicated_indices':[list(x) for x in new_outer],
  'updated_certified_total':139644,
  'updated_grid_fraction':'3879/4096',
  'updated_percentage':'94.7021484375',
  'uncertified_grid_cells':7812,
  'verification':'ALL_CHECKS_PASS PREFIX733-R6',
  'grade':'AUTHOR_EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    (ROOT/'PREFIX733_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(result['verification'], 'new=',len(new_outer),'total=',139644)
