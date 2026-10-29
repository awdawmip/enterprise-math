#!/usr/bin/env python3
"""PREFIX-343: exact arithmetic verification, no sampled phases.

This checks the rational/Gaussian arithmetic premises. The infinite-arc
Hausdorff and minimum-enclosing-radius inequalities are proved analytically
in README_PREFIX343.zh-CN.md. The five-contact h=3/2 lower input is the
source-pinned PREFIX-342 author-side certificate (re-executed separately).
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

A=[[(4,0),(4,0),(0,0)],[(0,0),(-4,0),(4,0)],
   [(-5,3),(0,0),(-3,1)],[(-2,-2),(4,4),(2,2)],[(-2,0),(0,0),(5,2)]]
a0=[(4,0),(5,-2),(7,-4)]
b=[1360,128,2330,1864,1261]
lam=F(10,61)
q=[F(2125,3721),F(200,3721),F(29125,29768),F(5825,7442),F(31525,59536)]
q3=q[2]; L=F(1062562,458329)
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def ordered_mass(j):
    v=[mul(A[j][k],a0[k]) for k in range(3)]
    terms=[mul(v[k],conj(v[l])) for k,l in product(range(3),repeat=2)]
    return tuple(map(sum,zip(*terms))),len(terms)

rows=[]
for j in range(5):
    m,count=ordered_mass(j)
    assert count==9 and m==(b[j],0)
    assert q[j]==lam*lam*F(b[j],64) and 0<q[j]<1
    rows.append({'port':j+1,'ordered_pairs':count,
                 'exact_gaussian_sum':[m[0],m[1]],'intensity':str(q[j])})
assert sum(t['ordered_pairs'] for t in rows)==45

gram=[]
for k in range(3):
    row=[]
    for l in range(3):
        acc=(0,0)
        for j in range(5): acc=add(acc,mul(conj(A[j][k]),A[j][l]))
        row.append(acc)
    gram.append(row)
assert gram==[[(62,0),(0,0),(0,0)],
             [(0,0),(64,0),(0,0)],
             [(0,0),(0,0),(63,0)]]
assert sum(b)==6943
N=lam*lam*F(sum(b),62)
assert N==F(347150,115351)

h0=F(3,2); hmax=F(71,46); tmax=hmax-1; K=F(21,10)
assert hmax>h0>1 and tmax*tmax<q3
assert N<K*K*(q3-tmax*tmax)
old_r2_lower=F(16322694483,6250000000)
old_r_lower=F(202,125)
assert old_r_lower**2<old_r2_lower
dh=hmax-h0
assert dh==F(1,23)
r_lower=old_r_lower-K*dh
assert r_lower==F(8767,5750)
rsq_lower=r_lower*r_lower
assert rsq_lower==F(76860289,33062500) and rsq_lower>L

report={
 'schema':'PREFIX343_FULL_FIBRE_REPORT_HAUSDORFF_STABILITY_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL_WITH_PREFIX342_CERTIFIED_LOWER_INPUT',
 'model':'STATIC_AUXILIARY_S7_3_FIVE_PORT_BRC_KEEP_GLOBAL_PHASE',
 'exact_intensity_q':[str(v) for v in q],
 'source_scope':'ALL_COMPLEX_SOURCES_WITH_EXACT_MASSES_NOT_ONLY_SIX_ROOTS',
 'A_dagger_A':[[[z[0],z[1]] for z in row] for row in gram],
 'BRC_ordered_pairs':45,'BRC_port_evidence':rows,
 'full_source_norm_squared_bound':str(N),
 'param_h_open_closed_interval':'1 < h <= 71/46',
 'q3':str(q3),'target_port':3,'report_Im_target':'h',
 'other_nine_components_target':0,'absolute_component_error':1,
 'phase_endpoint_imag_floor_max':str(tmax),
 'hausdorff_radius_lipschitz_constant':str(K),
 'frame_speed_certificate':f'{N} < ({K})^2*({q3}-({tmax})^2)',
 'reference_h':str(h0),
 'prefix342_five_contact_r2_lower':str(old_r2_lower),
 'radius_lower_at_reference':str(old_r_lower),
 'max_h_perturbation_from_reference':str(dh),
 'all_h_strict_radius_lower':str(r_lower),
 'all_h_strict_radius_squared_lower':str(rsq_lower),
 'legacy_L':str(L),'certified_superL_margin':str(rsq_lower-L),
 'all_h_nonempty_compact':True,'no_antipodes_for_h_gt_one':True,
 'analytic_proof_dependencies':[
  'All q_j<1 makes nine non-target report components automatic.',
  'Global unit phase preserves all ordered BRC pairs and exact intensities.',
  'Arc boundary speed ||a||/sqrt(q3-t^2) bounded by 21/10.',
  'Nested upper arcs give d_H(S(h1),S(h2))<=21/10*(h2-h1).',
  'MEB radius is 1-Lipschitz under Euclidean Hausdorff distance.',
  'PREFIX342 five-contact lower proves R(S(3/2))>202/125.'
 ],
 'not_required':'SIX_SOURCE_EXHAUSTIVENESS_FOR_ANY_FULL_FIBRE_LOWER_BOUND',
 'scope_limitations':['author-side','static auxiliary C3','global phase retained',
                      'X6/Detector/time preservation pending','native review pending']
}
Path(__file__).with_name('RESULTS_PREFIX343.json').write_text(
 json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(report['status'])
print('A*A:',gram)
print('full-source ||a||^2 <=',N,'and K^2*(q3-tmax^2) =',K*K*(q3-tmax*tmax))
print('forall 1<h<=71/46: R >',r_lower,'R^2 >',rsq_lower,'> L=',L)
print('no antipodes; no six-source exhaustiveness assumed')
