#!/usr/bin/env python3
"""PREFIX-735-R6: exact transverse Gamma certificate for all real q>=2.

Run in research_notes/portable_direct with original PREFIX731 module and
PREFIX713/716/718 JSON evidence. Uses frozen scientific pin, never floating
point for proof decisions. Output: PREFIX735_R6_TRANSVERSE_STRIP_130_RESULTS.json.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from functools import lru_cache
from PREFIX731_R6_MONOTONE_MOMENT_TILE import pair

ROOT=Path(__file__).resolve().parent
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
def load(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
def reflect(points):
    v={tuple(x) for x in points}
    return v|{(j,i) for i,j in v}
mu_e,m2_e=pair(F(0),F(73,500)); W_e=m2_e-mu_e*mu_e
mu_o,m2_o=pair(F(0),F(3,20)); W_o=m2_o-mu_o*mu_o

@lru_cache(None)
def bound(lo_p,lo_z,hi_p,hi_z,w_mu,w_var):
    low_mu,_=pair(lo_p,lo_z)
    _,high_m2=pair(hi_p,hi_z)
    upper=high_m2-low_mu*low_mu
    a=w_var-upper
    b=a-(w_mu-low_mu)/2
    return min(a,b)

passed=[];old_overlap=[];subdivided=0;worst=None;worst_cell=None
for i in range(58,70):
    for j in range(70,76):
        lo_p,lo_z=F(i,384),F(j,384)
        hi_p,hi_z=F(i+1,384),F(j+1,384)
        g=bound(lo_p,lo_z,hi_p,hi_z,mu_e,W_e)
        if g<=0:
            subdivided+=1
            g=min(bound(F(2*i+di,768),F(2*j+dj,768),
                        F(2*i+di+1,768),F(2*j+dj+1,768),mu_e,W_e)
                  for di in range(2) for dj in range(2))
        assert g>F(1,20),(i,j,'strict margin failed',g)
        if worst is None or g<worst: worst,worst_cell=g,(i,j)
        passed.append((i,j))
        if bound(lo_p,lo_z,hi_p,hi_z,mu_o,W_o)>0:
            old_overlap.append((i,j))
assert len(passed)==72
assert old_overlap==[(68,74),(68,75),(69,71),(69,72),(69,73),(69,74),(69,75)]
assert subdivided==65
new_upper=sorted(set(passed)-set(old_overlap))
assert len(new_upper)==65
new_cells=reflect(new_upper)
assert len(new_cells)==130

a=load('PREFIX713_R6_RESULTS.json')
m=load('PREFIX713_R6_MULTICOMPETITOR_RESULTS.json')
b=load('PREFIX716_R6_RESULTS.json')
c=load('PREFIX718_R6_RESULTS.json')
assert all(x['scientific_pin']==PIN for x in (a,m,b,c))
coupled=[(2*i+di,2*j+dj) for i,j in a['full_child_parents']
         for di in (0,1) for dj in (0,1)]
x=a['extra_child'];coupled.append((2*x['parent'][0]+x['subcell'][0],
                                   2*x['parent'][1]+x['subcell'][1]))
later={'PREFIX713_coupled':reflect(coupled),
       'PREFIX713_multi':reflect([x[:2] for x in m['additional_exact_cells']['all_q_ge_2']]),
       'PREFIX716':reflect(b['representatives']),
       'PREFIX718':reflect(c['new_half_square_representatives'])}
assert [len(x) for x in later.values()]==[90,20,1590,150]
assert all(len(new_cells&s)==0 for s in later.values())
A={(i,j) for i in range(30,58) for j in range(30,58)}
B={(i,j) for i in range(50,70) for j in range(50,70)}
assert not(new_cells&A) and not(new_cells&B)
prior=139980;total=prior+len(new_cells);frac=F(total,384*384)
assert total==140110 and frac==F(70055,73728)
assert 384*384-total==7346

out={'schema':'PREFIX735_R6_TRANSVERSE_STRIP_130_ALL_Q_V1',
     'frozen_science_pin':PIN,'q_domain':'all real q>=2',
     'comparator':['0','73/500'],
     'strip_upper_cells':'58<=i<70,70<=j<76; 384-grid',
     'upper_half_tested':len(passed),'subdivided_to_half_grid':subdivided,
     'strict_margin':'V_q(e)-V_q(p,z) > q^2/20 on all 72 upper strip cells',
     'old_PREFIX712_overlap_upper':[list(x) for x in old_overlap],
     'other_certificates_overlap':{k:len(new_cells&s) for k,s in later.items()},
     'distinct_upper_new':len(new_upper),'reflected_new_cells':len(new_cells),
     'new_grid_coordinates':[list(x) for x in sorted(new_cells)],
     'minimum_margin_numerator_sha256':sha256(str(worst.numerator).encode()).hexdigest(),
     'minimum_margin_denominator_sha256':sha256(str(worst.denominator).encode()).hexdigest(),
     'minimum_margin_floor_times_1000000':(worst*1000000).numerator//(worst*1000000).denominator,
     'worst_upper_cell':list(worst_cell),'prior_certified':prior,'new_certified':total,
     'total_grid':147456,'new_fraction':'70055/73728',
     'new_percentage_display_only':float(frac*100),
     'not_yet_certified':7346,
     'proof_semantics':'exact monotone moments and affine t=1/q endpoint inequalities on all 72 closed cells; historical union inherited author certificates',
     'status':'AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED',
     'verification':'ALL_CHECKS_PASS PREFIX735-R6-TSTRIP'}
if __name__=='__main__':
    (ROOT/'PREFIX735_R6_TRANSVERSE_STRIP_130_RESULTS.json').write_text(
       json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(out['verification'],'+130','140110/147456',
          'minimum floor x1e6=',out['minimum_margin_floor_times_1000000'])
