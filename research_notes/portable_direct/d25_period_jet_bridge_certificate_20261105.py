#!/usr/bin/env python3
"""D25 exact-rational complex period / weighted jet checker. No floats."""
from fractions import Fraction as F
from math import comb
import json

def main(n=500, d=145):
    u=v=F(1)
    A=B=P=Q=F(0)
    for k in range(n):
        A+=u; B+=v; P+=(6*k+1)*u; Q+=(8*k+1)*v
        u*=F((2*k+1)*(3*k+1)*(3*k+2),36*(k+1)**3)
        v*=F((2*k+1)*(4*k+1)*(4*k+3),288*(k+1)**3)
    # Exact upper tails; all terms positive and raw ratios < 1/2 or 1/9.
    ta=2*u
    tb=F(9,8)*v
    ra=F(6*n+7,2*(6*n+1))
    rb=F(8*n+9,9*(8*n+1))
    assert ra<1 and rb<1
    tp=(6*n+1)*u/(1-ra)
    tq=(8*n+1)*v/(1-rb)
    d0=8*A*A-9*B*B
    d1=2*P-3*Q
    err0=abs(d0)+8*(2*A*ta+ta*ta)+9*(2*B*tb+tb*tb)
    err1=abs(d1)+2*tp+3*tq
    assert err0 < F(1,10**d)
    assert err1 < F(1,10**d)
    p=13; mod=p**3
    W=V=0
    for k in range(p):
        W=(W+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod))%mod
        V=(V+(8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,mod))%mod
    assert W==V==13
    assert (2*W-3*V)%(p*p)==156
    print(json.dumps({
      "N":n,"precision_decimal":d,
      "inequalities":["abs(8*A_inf**2-9*B_inf**2)<1e-145",
                      "abs(2*P_inf-3*Q_inf)<1e-145"],
      "integer_rational_assertions":"PASSED",
      "p13_original_mod_p3":{"W":W,"V":V,"2W_minus_3V_mod_p2":156},
      "note":"Unproved exact analytic equalities; native H0/B0 not executed"
    },indent=2))

if __name__=="__main__":
    main()
