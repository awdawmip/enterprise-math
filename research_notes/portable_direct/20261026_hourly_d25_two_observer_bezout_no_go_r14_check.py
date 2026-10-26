"""D25 Ward two-observer Bezout proof: exact author arithmetic checks only."""
from fractions import Fraction
from math import comb


def coeff(p, k=1, seam=False):
    m, mod = (p - 1) // 6, p**k
    M = 2*m - 1
    c = [1]
    a = 0
    for t in range(1, M + 1):
        if seam:
            a = pow(p+2, -1, mod) if t == 1 else a*(p+2*t-1)*pow(p+2*t, -1, mod)%mod
            c.append((p+1)*a%mod)
        else:
            c.append(c[-1]*(2*t-1)*pow(2*t, -1, mod)%mod)
    return M, mod, c


def obs(z, c, mod):
    inv, x, A, D = pow(z, -1, mod), 1, 0, 0
    for t, v in enumerate(c):
        term = v*x%mod
        A = (A+term)%mod
        D = (D-t*term)%mod
        x = x*inv%mod
    return A, D, (A-6*D)%mod


def lift(z, p, k, derivative, seam=False):
    _, mod, c = coeff(p, k+1, seam)
    v = obs(z, c, mod)[0]
    assert v % p**k == 0
    return z + (-(v//p**k)*pow(derivative, -1, p)%p)*p**k


def run():
    rational = 0
    for M in range(13):
        c = [Fraction(comb(2*t, t), 4**t) for t in range(M+1)]
        for t in range(M+1):
            lhs = ((t+1)*c[t+1] if t<M else 0) - (Fraction(t)+Fraction(1, 2))*c[t]
            rhs = -(Fraction(M)+Fraction(1, 2))*c[M] if t==M else 0
            assert lhs == rhs
            rational += 1
        assert sum(c) == (2*M+1)*c[M]
        rational += 1
    primes = [p for p in range(7, 998) if p%6 == 1 and all(p%d for d in range(2, int(p**.5)+1))]
    samples, checks, roots, lifts = {}, 0, 0, 0
    for p in primes:
        M, _, c = coeff(p)
        cm = c[-1]
        m = (p-1)//6
        left = (4*(-1 if m%2 else 1)*pow(comb(2*m, m)*(2*m+1)*(m+1), -1, p))%p
        assert cm != 0 and left != 0 and (2*M+1)%p != 0
        for z in range(1, p):
            A, D, B = obs(z, c, p)
            unit = 3*(2*M+1)*cm*pow(z, -M, p)%p
            assert ((z+2)*A-(z-1)*B-unit)%p == 0
            assert A != 0 or B != 0
            fA, fB = A*pow(cm, -1, p)*left%p, B*pow(cm, -1, p)*left%p
            assert ((z+2)*fA-(z-1)*fB-3*(2*M+1)*pow(z, -M, p)*left)%p == 0
            checks += 3
            if A == 0:
                roots += 1
                assert z != 1 and B != 0
                assert D == (2*M+1)*pow(2,-1,p)*cm*pow(z,-M,p)*pow(z-1,-1,p)%p
                if p <= 211:
                    h = lift(z, p, 1, D*pow(z,-1,p)%p)
                    assert h%p == z and obs(h, coeff(p,2)[2], p*p)[0] == 0
                    lifts += 1
            if z == 2 and p in (13, 733):
                samples[p] = (A,D,B,fA,fB,unit)
    assert samples == {13:(9,3,4,7,6,6), 733:(0,211,200,0,236,533)}
    p = 733
    derivative = 472
    free2 = lift(2,p,1,derivative)
    free3 = lift(free2,p,2,derivative)
    fixed2 = lift(2,p,1,derivative,True)
    fixed3 = lift(fixed2,p,2,derivative,True)
    assert (free2,free3,fixed2,fixed3) == (385560,185750265,534359,155810880)
    assert obs(free3, coeff(p,3)[2],p**3)[0] == 0
    assert obs(fixed3, coeff(p,3,True)[2],p**3)[0] == 0
    assert obs(2, coeff(p,3,True)[2],p**3)[0] == 137318021
    print(dict(status='PASS', primes=len(primes), exact_rational_checks=rational,
               finite_ring_assertions=checks, geometric_roots=roots,
               first_lifts=lifts, p13=samples[13], p733=samples[733],
               free_733=(free2,free3), fixed_center_733=(fixed2,fixed3)))


if __name__ == '__main__':
    run()
