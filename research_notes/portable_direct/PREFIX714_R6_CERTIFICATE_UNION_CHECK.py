#!/usr/bin/env python3
"""PREFIX-714 union of two independent exact continuous-domain Gamma exclusions.
Inputs: PREFIX-712 verified 384^2 count, PREFIX-713 coupled moment envelope's
45 explicit half-grid cells and reflections, and the 26 exact multi-competitor
witnesses (20 all-q, six q12..24) in the adjacent companion checker.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy,json

base=Path(__file__).parent
# Exact 189-row model / Gamma survival / extra cell inequalities are re-executed.
m=runpy.run_path(str(base/'PREFIX713_R6_MULTICOMPETITOR_CERTIFICATE.py'))
groups=[(16,72),(24,64),(32,72),(0,80),(4,80),(8,72),(8,80),
        (16,80),(24,72),(24,80),(32,64)]
coupled45={(2*i+di,2*j+dj) for i,j in groups for di in (0,1) for dj in (0,1)}|{(9,145)}
assert len(coupled45)==45 and all(i<j for i,j in coupled45)
coupled90=coupled45 | {(j,i) for i,j in coupled45}
assert len(coupled90)==90
own_all={(i,j) for i,j,_ in m['extra_all']}
own_range={(i,j) for i,j,_ in m['extra_range']}
assert len(own_all)==20 and len(own_range)==6
assert not coupled90.intersection(own_all)
assert not coupled90.intersection(own_range)
# Coupled PREFIX-713 is certified for all t in [0,1/2]. To add its 90 cells
# to the more inclusive PREFIX-712 q12..24 reference, prove independently
# that none belongs to the OLD q12..24 certified set.
for i,j in sorted(coupled90):
    assert min(m['gap_for_cell'](i,j,'old_3_20',F(1,24)),
               m['gap_for_cell'](i,j,'old_3_20',F(1,12)))<=0, (i,j)
# All-q new 20 are already included in PREFIX-712's more inclusive q12..24 set;
# their count should not be added a second time to the range certificate.
for i,j in own_all:
    assert min(m['gap_for_cell'](i,j,'old_3_20',F(1,24)),
               m['gap_for_cell'](i,j,'old_3_20',F(1,12)))>0, (i,j)
q_all=137168+90+20
q_range=137398+90+6
assert q_all==137278 and q_range==137494
result={
 'schema':'PREFIX714_R6_INDEPENDENT_WITNESS_UNION_V1',
 'date':'2026-11-12',
 'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':'Y=max of two independent Gamma(N,1) completion clocks',
 'base_prefix712_384_grid':{'all_q_ge_2':137168,'q12_to_24':137398},
 'prefix713_coupled_envelope_new_cells':90,
 'prefix713_multicompetitor_new_cells':{'all_q_ge_2':20,'q12_to_24':6},
 'coupled_cells_fail_old_q12_to24':True,
 'twenty_extra_all_q_already_in_q12_to24_base':True,
 'two_new_witness_sets_disjoint':True,
 'certified_minimum':{'all_q_ge_2':q_all,'q12_to_24':q_range},
 'denominator_total':147456,
 'relative_area_lower_bound':{'all_q_ge_2':str(F(q_all,147456)),
                              'q12_to_24':str(F(q_range,147456))},
 'remaining_fraction_upper_bound':{'all_q_ge_2':str(F(147456-q_all,147456)),
                                    'q12_to_24':str(F(147456-q_range,147456))},
 'verification':'ALL_CHECKS_PASS PREFIX714-R6',
 'mathematical_basis':'Inherited exact PREFIX-712 and PREFIX-713 coupled certificate; re-executed exact new 20+6 comparator certificates and exact nonoverlap/cell-range membership checks',
 'grade':'AUTHOR_DERIVED / EXACT_INTEGER_GAMMA_KERNEL / UNREVIEWED / NOT_ADMITTED'
}
(base/'PREFIX714_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS PREFIX714-R6',result['relative_area_lower_bound'],flush=True)
