#!/usr/bin/env python3
"""PREFIX-642: exact rational certificate for improved Poisson-cap BRC strip.

Inputs: 189-layer stopping extinction and independent unit Poisson clocks
(PREFIX-621/622), PREFIX-631 endpoint signs, PREFIX-639 central bounds.
"""
from fractions import Fraction as F
import json
from pathlib import Path

N=189
h=F(7,2**28)
A=sum(n for n in range(N))
B=2*sum(n*(n-1) for n in range(N))
C=sum(n*(n+1) for n in range(N))
D=2*sum(n*(n-1)*(n+1) for n in range(N))
E=N*N
J=2*sum(n*(n-1)*(n+1)*(n+2) for n in range(N))
K=2*(J+2*A*C+E*B+(N+10)*D)+F(D,12)
checks={
 'gamma_cap_from_cauchy':F(N,2)<100,
 'mean_cap_strict':N+10==199,
 'K_refined_exact':K==920566268685,
 'K_less_than_PREFIX641':K<1146545169525,
 'radius_times7':h/F(1,2**28)==7,
 'z_domain':F(37,256)<F(19,128)-h<F(19,128)+h<F(39,256),
 'mu_p_lower':F(274)-C*h>273,
 'mu_p_upper':F(321)+C*h<322,
 'curvature_margin':K*h<24100,
 'curvature_lower':F(27100)-K*h>3000,
 'curvature_upper':F(48100)+K*h<72200,
 'valley_gap_lower':F(273,72200)/24==F(91,577600),
 'valley_gap_upper':F(322,3000)/24==F(161,36000),
 'valley_gap_consistent':0<F(91,577600)<F(161,36000)<F(1,6)-F(3,20),
 'curvature_strong_lower':F(273*273,72200)>1,
 'curvature_strong_upper':F(322*322,3000)<35
}
assert all(checks.values()),checks
result={
 'schema':'PREFIX642_R6_POISSON_CAP_SEVENFOLD_VALLEY_CERTIFICATE_V1',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'N':N,'mu_global_upper':'199 (strict)',
 'A':A,'B':B,'C':C,'D':D,'E':E,'J':J,'K':str(K),
 'radius':'7/268435456','K_times_radius':str(K*h),
 'domain':{'p1':'[3/20,1/6]','p2':'[19/128-7/2^28,19/128+7/2^28]','q':'real [12,24]'},
 'conclusions':['273<mu_p<322','3000<F_q,pp<72200',
 '91/577600<c(12,z)-c(24,z)<161/36000',
 '273^2/72200 < -Phi_tt < 322^2/3000'],
 'checks':list(checks),'check_count':len(checks),'status':'ALL_CHECKS_PASS',
 'proof_basis':'Gamma(N,1) independent arrival cap, degreewise Bernstein and exact rational implication from PREFIX-631/639',
 'scope':'fixed signed statistical observer; prior native-graph and 189-state results reused',
 'review':'AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    Path(__file__).with_name('PREFIX642_R6_RESULTS.json').write_text(
      json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS',len(checks),'K',K,'radius',h,'K*h',K*h)
