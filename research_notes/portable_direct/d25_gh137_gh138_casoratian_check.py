#!/usr/bin/env python3
"""Exact, standalone F_p checks of two-moment row determinants.

Theorems are supported by separate symbolic derivations; these are finite checks.
No remote service / native Enterprise Math experiment is invoked.
"""
from math import comb


def poly_coefficient(p, exponent, degree):
    """[X^degree](X^2+X+B)^exponent as a polynomial in B over F_p."""
    out = [0] * (exponent + 1)
    for a in range(exponent + 1):
        b = degree - 2 * a
        c = exponent - a - b
        if b >= 0 and c >= 0:
            out[c] = (out[c] + comb(exponent, a) * comb(exponent - a, b)) % p
    return out


def val(coeffs, b, p):
    ans = 0
    for c in reversed(coeffs):
        ans = (ans * b + c) % p
    return ans


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


def check(p, exhaustive=False):
    N = (p - 1) // 2
    h = (p - 1) // 4
    s0 = (p + 1) // 4
    # Row map (U,V) -> -m_s, shared with GH-129; no use of trace data.
    A = [None] + [poly_coefficient(p, p - s, N) for s in range(1, N + 1)]
    E = [None] + [poly_coefficient(p, p - s, 3 * N + 1) for s in range(1, N + 1)]
    assert E[s0][0] % p == (3 * h + 1 if p % 4 == 1 else 1) % p
    assert all(c % p == 0 for c in E[s0][1:])
    assert all(c % p == 0 for c in E[s0 + 1])
    factor = (-1)**h * comb(N, h) % p
    for b in range(p) if exhaustive else sorted(set([0, 1, 2, 3, 4, p // 2, p - 1])):
        d = b * (1 - 4*b) % p
        if d == 0:
            continue
        a = [None] + [val(A[s], b, p) for s in range(1, N+1)]
        e = [None] + [val(E[s], b, p) for s in range(1, N+1)]
        assert a[s0+1] == factor * pow(d, h, p) % p
        product = 1
        for s in range(1, N):
            det = (a[s] * e[s+1] - a[s+1] * e[s]) % p
            pred = (-N * pow(d, N-s, p) * product) % p
            assert det == pred, (p,b,s,det,pred)
            assert (det != 0) == (s <= s0), (p,b,s,det,s0)
            product = product * (1 - 16*s*s) * pow(4*s*(s+1), -1, p) % p
        assert (-a[s0+1]*e[s0]) % p == (-e[s0]*factor*pow(d,h,p)) % p
        for s in range(s0+1, N+1):
            assert e[s] == 0
    return N-1, s0



def mul2(x, y, p):
    # F_p[rho]/(rho^2-2), p=3 (mod 8): rho^2=2 is nonsquare.
    return ((x[0]*y[0] + 2*x[1]*y[1]) % p,
            (x[0]*y[1] + x[1]*y[0]) % p)


def eval2(coeffs, b, p):
    t = (0, 0)
    for c in reversed(coeffs):
        u = mul2(t, b, p)
        t = ((u[0]+c)%p,u[1])
    return t


def target_mark_check(p):
    assert p%8==3
    N=(p-1)//2
    s0=(p+1)//4
    b=(pow(8,-1,p),pow(12,-1,p))
    d=mul2(b, (1-4*b[0],-4*b[1]),p)
    assert d==(pow(144,-1,p),0)
    a=[None]+[eval2(poly_coefficient(p,p-s,N),b,p) for s in range(1,N+1)]
    e=[None]+[eval2(poly_coefficient(p,p-s,3*N+1),b,p) for s in range(1,N+1)]
    prod=1
    for s in range(1,N):
        t1=mul2(a[s],e[s+1],p);t2=mul2(a[s+1],e[s],p)
        det=((t1[0]-t2[0])%p,(t1[1]-t2[1])%p)
        theory=(-N*pow(d[0],N-s,p)*prod)%p
        assert det==(theory,0),(p,s,det,theory)
        assert (det!=(0,0))==(s<=s0)
        prod=prod*(1-16*s*s)*pow(4*s*(s+1),-1,p)%p
    return N-1


def check_3347():
    p = 3347
    h = (p-3)//4
    N = (p-1)//2
    s0 = (p+1)//4
    d = pow(144,-1,p)
    c = comb(N,h) * pow(d,h,p) % p
    assert (N,h,s0,c) == (1673,836,837,954)
    # E_{s0}=1, E_{s0+1}=0.  Consecutive determinant at center:
    center_det = (-c) % p
    assert center_det == 2393
    product = 1
    for s in range(1,s0):
        product = product*(1-16*s*s)*pow(4*s*(s+1),-1,p)%p
    closed = (-N*pow(d,N-s0,p)*product)%p
    assert closed == center_det
    assert (1-16*s0*s0) % p == 0
    print('P3347_EXACT', {'p':p, 'central_index':s0, 'A_successor':c,
         'last_nonzero_adjacent_det':center_det, 'first_zero_adjacent_det':0,
         'preboundary_product_check':closed})


def main():
    primes = [p for p in range(5,200) if is_prime(p)]
    pairs = 0
    for p in primes:
        n,s0=check(p,exhaustive=p<=43)
        pairs+=n
    marked = [(p,target_mark_check(p)) for p in primes if p%8==3]
    check_3347()
    print('PASS_GH137_GH138_ROW_CASORATIAN', 'prime_count', len(primes),
          'total_adjacent_indices_per_sample', pairs,
          'both_p_mod_4_classes', True,
          'marked_extension_instances', marked)

if __name__=='__main__':
    main()
