#!/usr/bin/env python3
"""R241 exact rational certificate (Python standard library)."""
from fractions import Fraction as F
import json

S_LO, S_HI = F(39,100), F(41,100)
C=F(5,18)
THETA=F(9847338,10000000)
R_HI_FLOOR=F(990783,1000000)
Z3,KAP,A0=F(50,1089),F(1680,1681),F(65,192)
GAMMA1,GAP,W5=655776,233424,86400

def family(s):
    t=(1691*s-2615)/(2615*s-3539)
    alpha=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
    b=(F(13,60),)+tuple(C*abs(F(1,2)-x) for x in alpha[1:])
    pi=tuple(bi/(1-ai) for ai,bi in zip(alpha,b))
    assert sum(pi)==1 and min(pi)>0
    return alpha,b

def secular(s,omitted,x):
    alpha,b=family(s)
    assert x>max(a for i,a in enumerate(alpha) if i!=omitted)
    return sum(b[i]/(x-alpha[i]) for i in range(7) if i!=omitted)-1

f_beta=secular(S_HI,4,THETA)
f_r=secular(S_HI,3,R_HI_FLOOR)
assert f_beta<0 and f_r>0
t_deriv_left=F(853776)/(2615*S_LO-3539)**2
assert t_deriv_left>F(13,100)
assert F(13,240)>F(5,297)
Z_LO=F(122345,46116)
assert Z_LO>F(53,20)
eta=F(W5)*KAP*(Z_LO-Z3)/(F(GAMMA1)*Z_LO+F(GAP)*A0)
q=THETA/R_HI_FLOOR
assert eta==F(1042768025600,8424836672439)
assert q==F(1641223,1651305)
assert q<F(14771007,14858075)
assert eta>F(304910592000,2463633795601)

def certified(n,d):
    k=n-1
    return d*(eta.denominator-eta.numerator)*q.numerator**k < eta.numerator*q.denominator**k

def first_horizon(d):
    lo,hi=2,2
    while not certified(hi,d): hi*=2
    while lo<hi:
        mid=(lo+hi)//2
        if certified(mid,d): hi=mid
        else: lo=mid+1
    assert certified(lo,d) and not certified(lo-1,d)
    return lo

n100,n1000=first_horizon(100),first_horizon(1000)
assert (n100,n1000)==(1073,1449)

result={
    "schema":"EM_R241_ENDPOINT_COUPLED_RATIO_EXACT_V1",
    "result":"PASS",
    "arithmetic":"Python Fraction and exact integer comparisons",
    "model":"R234 stationary sticky-reset seven-source scalar observer, 39/100 < s < 41/100",
    "f_beta_at_s_upper_theta":str(f_beta),
    "f_r_at_s_upper_lower_root":str(f_r),
    "t_derivative_left":str(t_deriv_left),
    "Z_left":str(Z_LO),
    "eta_lower":str(eta),
    "q_upper":str(q),
    "certificate_first_relative_error_lt_1_percent_n":n100,
    "certificate_first_relative_error_lt_0_1_percent_n":n1000,
    "comparison_R240_horizons":[1118,1510],
    "continuous_proof":"symbolic implicit derivative in accompanying proof",
    "review":"NOT_REVIEWED",
    "native_BRC":"NOT_EXECUTED"
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
