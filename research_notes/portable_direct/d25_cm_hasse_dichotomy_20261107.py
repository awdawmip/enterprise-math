"""Exact author-side regression for the D25 CM/Hasse residue-class bridge.

Finite tests support the accompanying universal algebra/CM argument; they do
not replace Deuring's theorem, the CM identification or formal admission.
Python standard library only. Arithmetic in F_p[s]/(s^2-2).
"""
from math import comb, isqrt


def primes_below(limit):
    out = []
    for p in range(5, limit):
        if all(p % q for q in range(2, isqrt(p) + 1)):
            out.append(p)
    return out


def add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def mul(x, y, p):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def scale(x, n, p):
    return (x[0] * n % p, x[1] * n % p)


def evaluate_binomial(k, top, z, p):
    term = (1, 0)
    total = term
    for j in range(k):
        factor = ((k-j)*(top-j)*pow(j+1, -2, p)) % p
        term = mul(term, scale(z, factor, p), p)
        total = add(total, term, p)
    return total


def hasse_independent(d, u, p):
    """Direct [x^(2d)] of ((x+1)^2-u)^(2d)."""
    n = 2*d
    term = (1, 0)
    total = (0, 0)
    negative_u = scale(u, -1, p)
    for j in range(d + 1):
        coeff = comb(n, j) * comb(2*(n-j), n) % p
        total = add(total, scale(term, coeff, p), p)
        term = mul(term, negative_u, p)
    return total


def poly_mul(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] = (c[i+j]+ai*bj)%p
    return c


def poly_add(a, b, p):
    n=max(len(a),len(b))
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(n)]


def poly_trim(a):
    while len(a)>1 and not a[-1]:
        a.pop()
    return a


def polynomial_quadratic_identity(p):
    k=(p-5)//8
    d=2*k+1
    r=5*k+3
    s=7*k+4
    z=[0,4%p,-4%p]  # 4u(1-u)
    coeff=[comb(r,j)*comb(s,j)%p for j in range(r+1)]
    ans=[coeff[-1]]
    for j in range(r-1,-1,-1):
        ans=poly_add(poly_mul(ans,z,p),[coeff[j]],p)
    L=[comb(d,j)*comb(3*d,j)%p for j in range(d+1)]
    rhs=[0]*(p+d+1)
    for j,c in enumerate(L):
        rhs[j]=(rhs[j]+c)%p
        rhs[j+p]=(rhs[j+p]-2*c)%p
    return poly_trim(ans)==poly_trim(rhs)


def derivative_binomial(k, top, z, p):
    """Differentiate sum_j binom(k,j)binom(top,j) z^j by Horner."""
    v = (0, 0)
    for j in range(k, 0, -1):
        v = add(mul(v, z, p), (j*comb(k,j)*comb(top,j)%p, 0), p)
    return v


def test(limit=1000):
    checked=[]
    for p in primes_below(limit):
        if p%8!=5:
            continue
        k=(p-5)//8
        d=(p-1)//4
        r=5*k+3
        s=7*k+4
        u=(pow(2,-1,p),pow(3,-1,p)) # (3+2sqrt(2))/6
        z=(pow(9,-1,p),0)
        G=evaluate_binomial(r,s,z,p)
        H=evaluate_binomial(k,3*k+1,z,p)
        L=evaluate_binomial(d,3*d,u,p)
        A=hasse_independent(d,u,p)
        assert L==A, (p,'hasse-vs-L',A,L)
        assert G==scale(H,pow(8*pow(9,-1,p)%p,(p+1)//2,p),p), (p,'G-vs-H')
        one_minus_2u=add((1,0),scale(u,-2,p),p)
        # Characteristic-p Frobenius: (1-2u)^p = (1,0)-2*u^p;
        # u^p=1-u when (2/p)=-1.
        factor=add((1,0),scale(add((1,0),scale(u,-1,p),p),-2,p),p)
        assert (G[0],0)==mul(factor,L,p), (p,'G-vs-L',G,L)
        expected_zero = p%24==13
        assert (H==(0,0)) == expected_zero, (p,'CM classification',H)
        if expected_zero:
            Lprime = derivative_binomial(d,3*d,u,p)
            Hprime = derivative_binomial(k,3*k+1,z,p)
            norm = pow(8*pow(9,-1,p)%p, (p+1)//2, p)
            jet_transfer = scale(Lprime, -pow(4*norm,-1,p), p)
            assert Lprime[1] == 0, (p,'CM derivative extension descent')
            assert Hprime == jet_transfer, (p,'first-jet CM transfer')
            assert Hprime != (0,0), (p,'first-jet nonzero')
        checked.append((p,k,H[0],L))
    checked_poly=[]
    for p in [5,13,29,37,53,61]:
        assert polynomial_quadratic_identity(p), ('polynomial quadratic transform',p)
        checked_poly.append(p)
    assert 2417472**2-2*1707264**2==14670139392
    print('PASS CM discriminant -24 j-minimal-polynomial certificate')
    print('PASS exact modular CM/Hasse sample',len(checked),'primes p<',limit,'p=5 mod8')
    print('PASS exact polynomial quadratic transform primes',checked_poly)
    print('EXAMPLES', [item for item in checked if item[0] in [5,13,29,37,53,61,109,181,373]])


if __name__=='__main__':
    test()
