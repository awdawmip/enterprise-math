#!/usr/bin/env python3
"""Original weighted 216 and 2304 integers falsify a precisely named scalar-only candidate."""
import json
from math import comb

def check(p):
    m=p**3; inv216=pow(216,-1,m); inv2304=pow(2304,-1,m)
    a=b=1; W=S=0
    for k in range(p):
        c=comb(2*k,k)
        W=(W+(6*k+1)*c*c*comb(3*k,k)*a)%m
        S=(S+(8*k+1)*comb(4*k,2*k)*c*c*b)%m
        a=a*inv216%m; b=b*inv2304%m
    gauge=pow(18,(p*p-1)//4,m); invGauge=pow(gauge,-1,p*p)
    epsilon=1 if pow(-18,(p-1)//2,p)==1 else -1
    q=(pow(18,p-1,p*p)-1)//p
    residual=(W-invGauge*S)%m
    conditional=(p*(1-epsilon)+epsilon*p*p*(q*pow(4,-1,p)%p))%m
    assert W==S==p # Exact witnesses for the declared finite sample only.
    assert residual==conditional
    assert residual!=0
    if p%24==13: assert residual%(p*p)==2*p
    if p==19: assert residual==5*p*p
    return dict(p=p,W216_mod_p3=W,S2304_mod_p3=S,epsilon=epsilon,
                q18_mod_p=q,inv_power_gauge_mod_p2=invGauge,
                scalar_model_defect=residual)

if __name__=="__main__":
    samples=[13,19,37,43,109,373]
    print(json.dumps(dict(status="PASS_EXACT_ORIGINAL_WEIGHTED_COUNTEREXAMPLES",
                          samples=[check(p) for p in samples]),indent=2))
