#!/usr/bin/env python3
"""Exact rational implication certificate for PREFIX-640-R6.

Inputs: PREFIX-631 (endpoint signs on full z bracket), PREFIX-636
(global mixed-derivative bounds), PREFIX-639 (central full-I coefficients).
This tests their exact rational consequences. It does not reconstruct the
189-layer signed observer or certify the original 96-port native graph.
"""
import json
from fractions import Fraction as F
from pathlib import Path

N, M = 189, 188
K0 = N*M*M
K2 = 25*N*N*M*M*M
h = F(1, 2**28)
z0 = F(19,128)
a,b = F(3,20),F(1,6)
checks = []

def ck(label, relation):
    assert relation, label
    checks.append(label)

ck('source_K0', K0 == 6680016)
ck('source_K2', K2 == 5933858212800)
ck('exact_K0h', K0*h == F(417501, 16777216))
ck('exact_K2h', K2*h == F(92716534575,4194304))
ck('centered_band_within_PREFIX631',
   F(37,256) <= z0-h < z0+h <= F(39,256))
ck('mu_derivative_lower', F(274)-K0*h > 273)
ck('mu_derivative_upper', F(321)+K0*h < 322)
ck('curvature_lower', F(27100)-K2*h > 4000)
ck('curvature_upper', F(48100)+K2*h < 71000)
ck('q_interval', 12<=24)
ck('q_inverse_integral', F(1,12)-F(1,24) == F(1,24))
ck('minimizer_gap_lower', F(273,71000)/24 == F(91,568000))
ck('minimizer_gap_upper', F(322,4000)/24 == F(161,48000))
ck('minimizer_gap_interval', 0 < F(91,568000)<F(161,48000)<b-a)
ck('strong_concavity_lower', F(273**2,71000)>1)
ck('strong_concavity_upper', F(322**2,4000)<26)
ck('new_radius_vs_PREFIX636', h/F(1,2**33)==32)

report={
  'schema':'PREFIX640_R6_EXACT_RATIONAL_IMPLICATION_V1',
  'scientific_input_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'parent_claims':['PREFIX-631 endpoint signs for all z in [37/256,39/256], q>=12',
                   'PREFIX-636 |mu_pz| <= K0 and |F_ppz| < K2 for q>=12',
                   'PREFIX-639 center z=19/128: 274<mu_p<321 and 27100<F_pp<48100 on I, 12<=q<=24'],
  'domain':{'p1':'[3/20,1/6]','p2':'[19/128-2^-28,19/128+2^-28]', 'q':'[12,24] real'},
  'constants':{'K0':str(K0),'K2':str(K2),'h':str(h), 'K0h':str(K0*h), 'K2h':str(K2*h)},
  'certified_implied_bounds':{'mu_p':'273<mu_p<322','F_pp':'4000<F_pp<71000',
    'c12_minus_c24':'91/568000 < c(12,z)-c(24,z) < 161/48000',
    'minus_Phi_tt':'273^2/71000 < -Phi_tt < 322^2/4000'},
  'checks':checks,'status':'ALL_CHECKS_PASS',
  'scope':'Exact algebraic implications of the named predecessor results; no rerun of native BRC graph or 189-layer model',
  'math_review':'UNREVIEWED_NOT_ADMITTED'
}
if __name__ == '__main__':
    p = Path(__file__).with_name('PREFIX640_R6_RESULTS.json')
    p.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS',len(checks))
    print('K0*h',K0*h,'K2*h',K2*h)
    print('Valley gap:',F(91,568000),'< c12-c24 <',F(161,48000))
