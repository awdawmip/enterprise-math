"""D25 source-fixed full LOW/HIGH cutoff pole: author exact-rational checks.

This is NOT the native benchmark and does not prove the LIFT target.
Only the auxiliary fixed-p contiguous cutoff m -> m+1 is inspected.
All calculations are exact fractions; no floating point or external library.
"""
from fractions import Fraction as Q
from math import comb, factorial


def invmod_q(x, p):
    assert x.denominator % p != 0, (p, x)
    return x.numerator * pow(x.denominator, -1, p) % p


def bernstein_port(r, order):
    return sum((Q((-1)**n * comb(r, n), 2**n * (3*n + order))
                for n in range(r+1)), Q(0))


def low_A(r):
    return sum((Q((-1)**n * comb(r, n), 2**n)
                * Q((1-3*n)*(6*n+3), (3*n+1)*(3*n+2))
                for n in range(r+1)), Q(0))


def low_J(r):
    e, result = Q(0), Q(0)
    for n in range(r+1):
        b = Q((-1)**n * comb(r, n), 2**n)
        k = Q((1-3*n)*(6*n+3), (3*n+1)*(3*n+2))
        d = (Q(2, 1-3*n) + Q(2, 6*n+3)
             - Q(1, 3*n+2) - Q(2, 3*n+1))
        result += b * k * (e+d)
        e += Q(3,6*n+1) - Q(1,3*n+2) - Q(2,3*n+1)
    return result


def B(r):
    return Q(factorial(2*r-1)*factorial(2*r), factorial(4*r))


def high_Z(r):
    A, C = Q(0), Q(0)
    for s in range(1,r):
        a = Q(2**(r-s)*factorial(2*r)*factorial(s-1),
              factorial(r+s)*factorial(r-1))
        kA = Q(4*(1-2*s)*(3*s+1),(2*s+1)*(6*s+1))
        A += a*kA
    for s in range(1,2*r):
        c = Q(factorial(2*r+1)*factorial(r+s-1),
              2**(s-1)*factorial(r)*factorial(2*r+s))
        kC = Q((2-3*s)*(6*s+1), 3*s*(3*s+1))
        C += c*kC
    return A-C/24


def harmonics(r):
    return sum((Q(1,j) for j in range(1,r+1)),Q(0))


def harmonic_seam(r):
    return Q(28,9)+harmonics(r)/3+Q(2,9)*harmonics(2*r)


def diagnostic_phi(p,r):
    """Auxiliary fixed-p expression, NOT a new original-task instance at r=m+1."""
    return ((low_A(r)+(1-2*r)*B(r))/p + low_J(r)
            + B(r)*(high_Z(r)+harmonic_seam(r)))


def exact_checks():
    # Integral beta-by-parts recurrence, tested independent of modular work.
    for r in range(1,10):
        for order in (1,2):
            assert ((3*r+order)*bernstein_port(r,order)
                    -3*r*bernstein_port(r-1,order) == Q(1,2**r))
        assert (low_A(r) == Q(-2,2**r)
                + 2*bernstein_port(r,1)+3*bernstein_port(r,2))


def check_prime(p):
    m=(p-1)//6
    assert m>=2 and p==6*m+1
    r=m+1
    # These are the three exact sources of the first principal cutoff pole.
    boundary=invmod_q(low_A(r)-(2*m+1)*B(r),p)
    b_last=Q((-1)**r,2**r)
    k_last=Q((1-3*r)*(6*r+3),(3*r+1)*(3*r+2))
    jet=invmod_q(3*b_last*k_last,p)
    high=invmod_q(-82*B(r),p)
    sources=(boundary,jet,high)
    res=sum(sources)%p
    # No p-pole from the harmonic seam; direct Q evaluation retains all terms.
    direct=invmod_q(p*diagnostic_phi(p,r),p)
    assert direct==res,(p,direct,res,sources)
    # New single-LOW-port formula.
    rhs=(Q(20,63)*bernstein_port(m,1)
         +Q(46+72*(-1)**m,63*2**m)+Q(976,189)*B(m))
    assert invmod_q(rhs,p)==res,(p,res,rhs)
    assert invmod_q(Q(-20,21),p)!=0
    orig=low_A(m)+(1-2*m)*B(m)
    assert orig.denominator % p and orig.numerator % p == 0
    return p,m,*sources,res


if __name__=='__main__':
    exact_checks()
    rows=[check_prime(p) for p in (13,19,31,37,43,61,211)]
    print('PASS exact Cauchy recurrence r=1..9 and direct rational cutoff pole cases:',len(rows))
    for row in rows:
        print('p,m,LOW_divided,LOW_jet,HIGH_fixed,combined=',row)
    assert rows[0] == (13,2,7,4,8,6)
    assert rows[1] == (19,3,12,8,6,7)
