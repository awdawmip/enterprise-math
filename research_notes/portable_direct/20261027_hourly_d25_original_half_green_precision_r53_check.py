#!/usr/bin/env python3
"""Exact R53 author checks for the genuine R23 low-half W/S observer.

The only potentially stronger Green poles are three explicit primes; these
are exhausted by integer/rational arithmetic, not by extrapolating a sample.
"""
from fractions import Fraction
from pathlib import Path
from runpy import run_path

r51 = run_path(str(Path(__file__).with_name("20261027_hourly_d25_green_endpoint_resonance_r51_check.py")))
w, s, vp, norm_mod, is_prime = (r51[x] for x in ("w", "s", "vp", "norm_mod", "is_prime"))


def check(p):
    L = (p-1)//2
    N = (3*p-1)//4+1
    Lw = sum((w(k) for k in range(L+1)),Fraction(0))
    Ls = sum((s(k) for k in range(L+1)),Fraction(0))
    W,S,W1,S1 = w(N),s(N),w(N+1),s(N+1)
    D=W*S1-S*W1
    C=(-Lw*S1+Ls*W1)/D
    C1=(Lw*S-Ls*W)/D
    assert C*W+C1*W1 == -Lw
    assert C*S+C1*S1 == -Ls
    assert C*(W-S)+C1*(W1-S1) == -(Lw-Ls)
    assert vp(C,p)>=-3 and vp(C1,p)>=-3
    return Lw,Ls,C,C1


def main():
    exceptions={
      139: (138,110,66,105),
      199: (81,141,138,68),
      277: (227,230,251,224),
    }
    checked=0
    for p in range(13,501):
        if p%6!=1 or not is_prime(p):
            continue
        Lw,Ls,C,C1=check(p)
        checked+=1
        if p in exceptions:
            cn,cn1,U,V=exceptions[p]
            assert vp(Lw,p)==vp(Ls,p)==1
            assert norm_mod(Lw,p,1)==norm_mod(Ls,p,1)==1
            assert norm_mod(w((3*p-1)//4+1),p,3)==U
            assert norm_mod(s((3*p-1)//4+1),p,3)==V
            assert (V-U)%p!=0
            assert (vp(C,p),vp(C1,p))==(-3,-3)
            assert (norm_mod(p**3*C,p,0),norm_mod(p**3*C1,p,0))==(cn,cn1)
            print('R53 exception',p,'Lw,Ls/p modp',1,1,'p3 endpoint coefficients',cn,cn1)
    assert checked==44
    print('R53 PASS: 44 target primes, complete 3-prime pole-resonance exhaustion')


if __name__=='__main__':
    main()
