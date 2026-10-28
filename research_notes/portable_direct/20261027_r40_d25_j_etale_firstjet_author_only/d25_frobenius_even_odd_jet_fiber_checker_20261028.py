#!/usr/bin/env python3
"""Author-only exact fiber witness in R2=(Z/p^2)[T]/(T^2-2).
Not the native fixed H0/B0 object; no Source permission or review is inferred.
"""
import json
from math import isqrt


def prime(p):
    return p > 1 and all(p % q for q in range(2, isqrt(p)+1))


def mul(x,y,m):
    return ((x[0]*y[0]+2*x[1]*y[1])%m,
            (x[0]*y[1]+x[1]*y[0])%m)


def sigma(x,m):
    return (x[0],(-x[1])%m)


def specimen(p,a,b):
    m=p*p
    eta=((1+p*a)%m,(p*b)%m)
    norm=mul(eta,sigma(eta,m),m)
    # Matrix in the pinned ordered basis (1,T): F(x)=eta*sigma(x)
    F=((eta[0],(-2*eta[1])%m),(eta[1],(-eta[0])%m))
    # Odd jet is the second coefficient divided by p, not a gauge-free scalar.
    assert eta[1] % p == 0
    chi=(eta[1]//p)%p
    assert norm==((1+2*p*a)%m,0), (p,a,b,norm)
    assert (eta[0]%p,eta[1]%p)==(1,0)
    assert (F[0][0]%p,F[0][1]%p,F[1][0]%p,F[1][1]%p)==(1,0,0,p-1)
    assert chi==b%p
    for x in [(1,0),(0,1),(p-1,p+1),(3,5)]:
        fx=mul(eta,sigma(x,m),m)
        ffx=mul(eta,sigma(fx,m),m)
        assert ffx==mul(norm,x,m)
    # Units u_c=1+p*c*T act by u_c F u_c^-1, sending b -> b+2c.
    c=(a+b+1)%p
    u=(1,(p*c)%m)
    eta_gauged=mul(mul(u,eta,m),u,m) # sigma(u)^(-1)==u (mod p^2)
    assert eta_gauged==((1+p*a)%m,(p*(b+2*c))%m)
    return norm[0],chi


def run():
    cases=[]
    for p in (13,19,37,43,109,211,373):
        assert prime(p) and p%24 in (13,19)
        assert pow(2,(p-1)//2,p)==p-1 # inert quadratic extension
        a_values=range(p) if p<=43 else (0,1,(p-1)//2,p-1)
        pairs=0
        for a in a_values:
            norm_to_chi={}
            for b in range(p):
                norm,chi=specimen(p,a,b)
                norm_to_chi.setdefault(norm,set()).add(chi)
                pairs+=1
            assert len(norm_to_chi)==1
            assert len(next(iter(norm_to_chi.values())))==p
        plus=specimen(p,0,1)
        minus=specimen(p,0,p-1)
        assert plus==(1,1) and minus==(1,p-1)
        cases.append({"p":p,"p2":p*p,"tested_a":len(a_values),"tested_eta":pairs,
                      "norm_at_a0_b1":plus[0],"odd_jet_plus":plus[1],
                      "odd_jet_minus":minus[1],"fiber_size_per_tested_even_value":p})
    out={"status":"PASS","classification":"AUTHOR_DERIVED_AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
         "scope":"auxiliary pinned-basis unramified quadratic semilinear models; not H0/B0",
         "theorem":"For p=13,19 mod24, eta(a,b)=1+p(a+bT); Norm mod p^2=1+2pa; F mod p is sigma; odd coefficient jet=b mod p. Every fixed norm fiber has p different odd jets.",
         "cases":cases,"gauge_checks":sum(x['tested_eta'] for x in cases),"checked_pairs":sum(x['tested_eta'] for x in cases),
         "source_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
         "actual_native_experiment":"NOT_RUN","native_result_or_claim":"NOT_ASSERTED"}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':run()
