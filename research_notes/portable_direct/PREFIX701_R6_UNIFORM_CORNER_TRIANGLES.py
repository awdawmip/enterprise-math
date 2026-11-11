#!/usr/bin/env python3
"""PREFIX-701 exact rational consequence of frozen PREFIX-700 witness and PREFIX-630 derivative envelopes.
Frozen science input f42f2906d77f24085c123f3ccfe9667d41caa96d.
No native heartbeat dynamics or new survivor rows are executed.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

N=189
A=sum(range(N))
S2=sum(n*(n+1) for n in range(N))
mu_max=2*N
assert (A,S2,mu_max)==(17766,2250360,378)
# For each parameter, |mu_i|<=A, |H_i|<=S2, |W_i|<=2*S2+2*mu_max*A.
# q>=2 implies |partial_i (V_q/q**2)| <= |W_i| + |mu_i|/2.
M=2*S2+2*mu_max*A+Q(A,2)
assert M==17940699
rho=Q(1,65536)
# These are proven 1e-6 rational floor bins for delta_mu and delta_W,
# recomputed from PREFIX-700's frozen 189-level integer path recurrence.
ticks={
    'zero_zero': ((48811611,48811612),(557257209,557257210)),
    'zero_half': ((-111509701,-111509700),(386820427,386820428)),
    'half_half': ((-119288768,-119288767),(439711044,439711045)),
}
out=[]
for corner,((ml,mu),(wl,wu)) in ticks.items():
    lower_dw=Q(wl,10**6)
    upper_dm=Q(mu,10**6)
    # For all q>=2, -delta_mu/q>=-max(delta_mu,0)/2.
    lower_gap=lower_dw-max(upper_dm,Q(0))/2
    assert lower_gap>386
    lower_net=lower_gap-M*rho
    assert lower_net>Q(7356197,65536)>112
    out.append({'corner':corner,'delta_mu_1e6_ticks':[ml,mu],
                'delta_W_1e6_ticks':[wl,wu],
                'uniform_over_q_ge_2_gap_lower_bound':str(lower_gap),
                'net_margin_lower_bound':str(lower_net),
                'inequality_verified':True})
margin=Q(386)-M*rho
assert margin==Q(7356197,65536)>112
result={'schema':'PREFIX701_R6_ALL_SLOT_CORNER_TRIANGLE_EXCLUSION_V1',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model':'two labelled independent Poissonized signed BRC first-stop clocks; D=[0,1/2]^2; q real >=2',
    'theorem':'For every real q>=2 and every point at L1 distance <=1/65536 from any square corner, V_q(0,1/8)-V_q(point)>7356197*q^2/65536.',
    'derivative_bound_normalized':str(M),
    'radius':str(rho),'margin_lower_bound':str(margin),
    'corner_checks':out,'dependencies':['PREFIX625 exact formula and strict mean derivative','PREFIX630 global moment derivative envelopes','PREFIX700 exact rational corner sign ticks'],
    'check':'ALL_CHECKS_PASS PREFIX701-R6',
    'verification_scope':'Exact Fraction check of predecessor numerical bounds and new Lipschitz consequence; no independent 189-row replay in this script; requires ancestor certificates',
    'admission':'AUTHOR_DERIVED/EXACT_FRACTION_IMPLICATION_CHECKED/UNREVIEWED/NOT_ADMITTED'}
Path(__file__).with_name('PREFIX701_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('ALL_CHECKS_PASS PREFIX701-R6',margin,'=',float(margin))
for x in out:print(x['corner'],x['uniform_over_q_ge_2_gap_lower_bound'],x['net_margin_lower_bound'])
