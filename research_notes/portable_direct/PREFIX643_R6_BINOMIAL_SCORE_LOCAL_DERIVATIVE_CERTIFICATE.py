#!/usr/bin/env python3
"""PREFIX-643: exact rational implication certificate for the localized BRC score strip."""
from fractions import Fraction as Q
from math import comb
import json
from pathlib import Path

N=189
M=N-1
p0,p1=Q(3,20),Q(1,6)
zlo,zhi=Q(37,256),Q(39,256)
z0=Q(19,128)
h=Q(1,2**18)
alpha=Q(37*219,256**2)
P=20
R=1500
A=N*P
B=N*R
C=N*P*P
D=N*R*P
E=N*P
J=N*(N+1)//2*R*P
gamma_tail=Q(N*comb(2*N,N),4**N)
gamma_max=Q(N)+gamma_tail
K=2*(J+2*A*C+E*B+197*D)+Q(D,12)
Fpp_lower=Q(27100)-K*h
Fpp_upper=Q(48100)+K*h
Mp_lower=Q(274)-C*h
Mp_upper=Q(321)+C*h
checks={
    'normalization_bounds':0<p0<p1<Q(1,2) and 0<zlo<z0<zhi<Q(1,2),
    'alpha_z':alpha==zlo*(1-zlo),
    'alpha_smaller_than_p_product':alpha<p0*(1-p0),
    'binomial_score_strict_20':Q(M)<4*P*P*alpha,
    'binomial_second_strict_1500':Q(M)<R*p0*(1-p0),
    'gamma_exact_cap':gamma_tail<Q(8),
    'gamma_max_less_197':gamma_max<Q(197),
    'gamma_tail_positive':gamma_tail>0,
    'A':A==3780,
    'B':B==283500,
    'C':C==75600,
    'D':D==5670000,
    'E':E==3780,
    'J':J==538650000,
    'mixed_K':K==Q(6598084500),
    'mixed_improves_PREFIX642':K<Q(920566268685),
    'h_in_target_band':zlo<z0-h<z0+h<zhi,
    'h_improves_PREFIX642':h/Q(7,2**28)==Q(1024,7),
    'mixed_times_h':K*h==Q(1649521125,65536),
    'mixed_times_h_less_25170':K*h<25170,
    'mu_derivative_lower':Mp_lower>273,
    'mu_derivative_upper':Mp_upper<322,
    'curvature_lower':Fpp_lower>1930,
    'curvature_upper':Fpp_upper<73270,
    'valley_gap_lower_positive':Q(273,24*73270)>0,
    'valley_gap_upper_within_interval':Q(322,24*1930)<p1-p0,
    'curvature_lower_strict':Q(273**2,73270)>1,
    'curvature_upper_finite':Q(322**2,1930)<54,
}
assert all(checks.values()),[k for k,v in checks.items() if not v]
result={
    'schema':'PREFIX643_R6_BINOMIAL_SCORE_STRIP_CERTIFICATE_V1',
    'date':'2026-11-09',
    'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'model':'PREFIX-621/622 signed two-information-direction BRC statistical first-stop observer',
    'inherited_source':['PREFIX-621/622 survivor and moments','PREFIX-631 endpoint gradient signs','PREFIX-639 central Bernstein bounds'],
    'N':N,
    'score':{'alpha':str(alpha),'sprime_lt':P,'ssecond_lt':R},
    'gamma_max':{'fraction':str(gamma_max),'cap_lt':197},
    'mixed':{'A':A,'B':B,'C':C,'D':D,'E':E,'J':J,'K':str(K)},
    'strip':{'p':'[3/20,1/6]','z':'[19/128-2^-18,19/128+2^-18]','q':'[12,24]','ratio_to_PREFIX642':'1024/7'},
    'bounds':['273<mu_p<322','1930<F_q_pp<73270',
        '273/(24*73270)<c(12,z)-c(24,z)<322/(24*1930)',
        '273^2/73270<-Phi_tt<322^2/1930'],
    'check_count':len(checks),'checks':list(checks),
    'status':'ALL_CHECKS_PASS',
    'review':'AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
    'next':'Adaptive bivariate Bernstein certification over full z band.'
}
Path(__file__).with_name('PREFIX643_R6_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',len(checks))
print('K',K,'K*h',K*h)
