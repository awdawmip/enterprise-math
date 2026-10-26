#!/usr/bin/env python3
"""Author portable finite-ring certificate; NOT native CM/Driver or accepted theorem.
Original ordered Clausen Q_p is independent of stored corrected-Hasse ports.
"""
from math import gcd

PORTS = {
    13: {
        (0,2): dict(U=138,T=130,K=99,B=104,C=0),
        (1,2): dict(U=80,T=41,K=154,B=30,C=72),
        (0,3): dict(U=69,T=113,K=13,B=96,C=0),
    },
    733: {
        (0,2): dict(U=194980,T=14284,K=492593,B=506918,C=0),
        (1,2): dict(U=225095,T=108012,K=109186,B=377020,C=300530),
        (0,3): dict(U=400749,T=526050,K=300290,B=229559,C=0),
    },
}

def original_quotient(p):
    mod = p**4
    r = [1]
    for n in range(p-1):
        den = 36*(n+1)**2
        assert gcd(den, mod) == 1
        r.append(r[-1]*(6*n+1)*(3*n+1)*pow(den,-1,mod) % mod)
    Q = 0
    for a in range(p):
        for b in range(p-a,p):
            Q += (6*(a+b)+1)*r[a]*r[b]
    Q %= mod
    assert Q % (p*p) == 0
    return Q//(p*p), Q

def check(p):
    q = p*p
    d = PORTS[p]
    inv6 = pow(6,-1,q)
    scale = pow(2,-p,q)*pow(18,-1,q) % q
    val = lambda ch,k: d[ch][k]
    for ch in d:
        U,T,K,B,C = [val(ch,k) for k in ("U","T","K","B","C")]
        assert T == ((1-6*p)*U + 12*K - 12*(B+C))%q, (p,ch,"ward")
    bracket = (val((0,2),"T") + p*(6*val((0,2),"U")
              -inv6*(val((1,2),"T")+val((0,3),"T"))))%q
    U02,K02,B02,C02 = [val((0,2),k) for k in ("U","K","B","C")]
    U12,U03 = val((1,2),"U"),val((0,3),"U")
    K12,K03 = val((1,2),"K"),val((0,3),"K")
    B12,B03 = val((1,2),"B"),val((0,3),"B")
    C12,C03 = val((1,2),"C"),val((0,3),"C")
    source = (U02+12*K02-12*B02-12*C02
              -p*inv6*(U12+U03)-2*p*(K12+K03)
              +2*p*(B12+B03+C12+C03))%q
    assert bracket == source, (p,bracket,source)
    Q_over_p2,Q = original_quotient(p)
    assert Q_over_p2 == scale*bracket%q, (p,Q_over_p2,bracket)
    sensitivity = scale*2*p*C12%q
    assert (C12%p==0) == (sensitivity==0)
    return dict(p=p,Q_mod_p4=Q,Q_over_p2_mod_p2=Q_over_p2,
                bracket=bracket,scale=scale,C12=C12,
                scalar_loss_when_C12_dropped=sensitivity,
                projected_quotient=(Q_over_p2-sensitivity)%q)

if __name__ == "__main__":
    for p in (13,733):
        print("PASS",check(p))
