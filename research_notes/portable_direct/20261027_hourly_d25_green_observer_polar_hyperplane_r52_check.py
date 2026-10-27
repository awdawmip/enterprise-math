#!/usr/bin/env python3
"""Author exact checks: R52 rank-one Green polar residue and safe observer hyperplanes."""
from fractions import Fraction
from pathlib import Path
from runpy import run_path

r51 = run_path(str(Path(__file__).with_name("20261027_hourly_d25_green_endpoint_resonance_r51_check.py")))
w, s, a, b, vp, norm_mod = (r51[name] for name in ("w", "s", "a", "b", "vp", "norm_mod"))


def exact_boundary(p, c0, c1):
    n = (3*p - 1)//4 + 1
    W, S, W1, S1 = w(n), s(n), w(n+1), s(n+1)
    Lw = Fraction(c0) + Fraction(c1) * Fraction(7,18)
    Ls = Fraction(c0) + Fraction(c1) * Fraction(3,32)
    D = W*S1 - S*W1
    C = (-Lw*S1+Ls*W1)/D
    C1 = (Lw*S-Ls*W)/D
    assert C*W+C1*W1 == -Lw
    assert C*S+C1*S1 == -Ls
    return (n,W,S,C,C1,Lw,Ls,D)


def main():
    expected = {
        139: (105, 66, 105, 115, 37, 107, 136),
        199: (150, 138, 68, 46, 111, 191, 37),
        277: (208, 251, 224, 217, 254, 43, 53),
    }
    for p, (n0,U0,V0,t0,delta0,safe_c0,T1) in expected.items():
        n,W,S,C,C1,Lw,Ls,D = exact_boundary(p,0,1)
        assert n == n0
        U,V = norm_mod(W,p,3),norm_mod(S,p,3)
        t = norm_mod(a(n),p,0)
        delta = norm_mod(D,p,7)
        assert (U,V,t,delta)==(U0,V0,t0,delta0)
        T = (norm_mod(Lw,p,0)*V - norm_mod(Ls,p,0)*U)%p
        assert T == T1
        assert (vp(C,p),vp(C1,p)) == (-4,-4)
        assert norm_mod(p**4*C,p,0) == (-t*T*pow(delta,-1,p))%p
        assert norm_mod(p**4*C1,p,0) == (T*pow(delta,-1,p))%p
        _,_,_,CC,CC1,LLw,LLs,_=exact_boundary(p,safe_c0,1)
        assert (norm_mod(LLw,p,0)*V - norm_mod(LLs,p,0)*U)%p == 0
        assert (vp(CC,p),vp(CC1,p)) == (-3,-3)
        # The distinct c0 and c1 observer rows have determinant b0-a0=-85/288, a p-unit.
        assert norm_mod(Fraction(-85,288),p,0) != 0
        print('R52',p,'N',n,'U/V',U,V,'t/delta',t,delta,
              'unsafe polar',(norm_mod(p**4*C,p,0),norm_mod(p**4*C1,p,0)),
              'safe c0',safe_c0,'safe valuation',(vp(CC,p),vp(CC1,p)))
    print('R52 PASS: exact rank-one polar residue, codimension-one witness, 3 primes')


if __name__ == '__main__':
    main()
