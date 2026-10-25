"""Author-side exact finite-ring checker for the D25 observer-fiber lemma.

This is not an original CM/divided-power experiment or an independent review.
"""
from collections import Counter


def check_case(p: int, r: int, a: int, b: int, u: int, v: int):
    mod = p**r
    n = p ** (r - 2)
    F = u * a + v * b
    L = 4 * u * b + 2 * v * a
    assert (a*a - 2*b*b) % p != 0
    assert F % p != 0 and L % p == 0
    ell = L // p
    norm = (a*a - 2*b*b) % mod

    observed = Counter()
    for x in range(p ** (r - 1)):
        t = p*x
        den = (1-2*t*t) % mod
        inv = pow(den, -1, mod)
        a1 = (a*(1+2*t*t)+4*b*t)*inv % mod
        b1 = (b*(1+2*t*t)+2*a*t)*inv % mod
        assert (a1*a1 - 2*b1*b1) % mod == norm
        f1 = (u*a1+v*b1) % mod
        dy = (f1-F) % mod
        assert dy % (p*p) == 0
        y = dy // (p*p)
        observed[y] += 1
        direct = (ell*x + 4*F*x*x)*pow(1-2*p*p*x*x, -1, mod) % mod
        assert y == direct % n

    square_roots = Counter(z*z % n for z in range(n))
    for y in range(n):
        delta = (ell*ell+16*F*y+8*p*p*y*y) % n
        assert observed[y] == p*square_roots[delta], (p,r,y,observed[y],p*square_roots[delta])
    assert sum(observed.values()) == p ** (r - 1)
    return {
        'p':p,'r':r,'source_parameters':(a,b,u,v),
        'x_checked':p**(r-1),'y_checked':n,
        'max_fiber':max(observed.values()),
        'number_of_observed_outputs':len(observed),
        'norm':norm,'F':F % mod,
        'ell_mod_p':ell % p,
    }


def main():
    cases = [
        (13,2,2,3,2,13-6),
        (13,3,2,3,2,13-6),
        (13,4,2,3,2,13-6),
        (19,3,2,3,2,19-6),
        (19,4,2,3,2,19-6),
        (373,3,92060,21788,302,-308),
    ]
    for case in cases:
        print('PASS',check_case(*case))

    p,r,a,b,u,v=373,3,92060,21788,302,-308
    M=p**r; F=u*a+v*b; L=4*u*b+2*v*a; ell=L//p
    z=(-ell*pow(4*F,-1,p))%p
    xc=(-ell*pow(8*F,-1,p))%p
    yc=(ell*xc+4*F*xc*xc)%p
    assert (z,xc,yc)==(295,334,97)
    print('p373_mod_p3_branch_certificate',{'x_pair':(0,z),'critical_x':xc,'critical_y':yc,'ordinary_F_mod_p3':F%M,'norm_mod_p3':(a*a-2*b*b)%M,'fiber_size_at_y0':2*p,'fiber_size_at_ycrit':p})

if __name__ == '__main__':
    main()
