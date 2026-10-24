"""Exact author check: Hesse reflection two-port jet transport, no native CM claim.

Source: fixed source polynomial A_p and inherited reflection/Green identities.
Arithmetic: F_p and the quadratic ring (Z/p^2)[T]/(T^2-2), integer-only.
"""
from math import comb, isqrt


def prime(p):
    return p >= 2 and all(p % j for j in range(2, isqrt(p)+1))


def mul(a, b, q):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % q,
            (a[0] * b[1] + a[1] * b[0]) % q)


def original_value_and_derivative(p):
    q = p * p
    n = (p - 1) // 3
    u = (2 * pow(4, -1, q) % q, -pow(4, -1, q) % q)
    power = (1, 0)
    value = (1, 0)
    deriv = (0, 0)
    ck = 1
    for k in range(1, n + 1):
        # coefficient of derivative at X^k uses u^(k-1)
        ck = ck * (3*k-2) * (3*k-1) * (3*k) * pow(27*k**3, -1, q) % q
        term = mul((k * ck % q, 0), power, q)
        deriv = ((deriv[0] + term[0]) % q, (deriv[1] + term[1]) % q)
        power = mul(power, u, q)
        term = mul((ck, 0), power, q)
        value = ((value[0] + term[0]) % q, (value[1] + term[1]) % q)
    return value, deriv


def green_coefficients(p):
    assert p >= 13 and p % 6 == 1 and prime(p)
    m = (p - 1) // 6
    n = 2 * m
    fact = 1
    for k in range(1, n + 1):
        fact = fact * k % p
    C = -pow(9 * pow(27, n, p) * pow(fact, 3, p), -1, p) % p
    inv9 = pow(9, -1, p)
    f = [(-1 if j & 1 else 1) * comb(2*m-1-j, j) % p
         for j in range(m)]
    beta = [0] * (m+1)
    for j in range(m-1, -1, -1):
        lam = ((6*j+4)*(6*j+5)*inv9) % p
        beta[j] = ((j+1)**2 * beta[j+1] - f[j]) * pow(lam, -1, p) % p
    coeffs = [C * bj % p for bj in beta[:-1]]
    return C, f, coeffs


def shifted(poly, p, z0):
    """Coefficient vector of poly(z0+Z) in ascending powers of Z."""
    return [sum(poly[j]*comb(j,k)*pow(z0,j-k,p)
                for j in range(k,len(poly))) % p
            for k in range(len(poly))]


def forward_reconstruct(p,C,f,v,E):
    """Regular CM evaluation jet from both source-provenance ports."""
    m=len(f)
    z0=pow(8,-1,p)
    g=shifted(f,p,z0)
    a=[0]*m
    a[0]=4*v%p
    a[1]=(4*E+16*v)%p
    for r in range(m-2):
        lam=(6*r+4)*(6*r+5)*pow(9,-1,p)%p
        rhs=(C*g[r]+(r+1)*pow(4,-1,p)*a[r+1]+lam*a[r])%p
        a[r+2]=16*rhs*pow((r+1)*(r+2),-1,p)%p
    return a,g


def check(p):
    C,f,phi=green_coefficients(p)
    (av,ab),(dv,db)=original_value_and_derivative(p)
    assert ab%p==0 and dv%p==0
    v=(ab//p)%p
    E=(dv//p)%p
    ans,g=forward_reconstruct(p,C,f,v,E)
    actual=shifted(phi,p,pow(8,-1,p))
    assert ans==actual, (p,ans,actual)
    assert (v*4)%p==actual[0]
    assert (4*E+16*v)%p==actual[1]
    assert (E-(-actual[0]+actual[1]*pow(4,-1,p)))%p==0
    # Exact Picard--Fuchs, shifted Y=1/8+z; compare all coefficients.
    for r in range(len(actual)):
        lhs = ( ((r+2)*(r+1)*actual[r+2]*pow(16,-1,p)) if r+2<len(actual) else 0 )
        lhs -= ((r+1)*actual[r+1]*pow(4,-1,p)) if r+1<len(actual) else 0
        lhs -= (6*r+4)*(6*r+5)*pow(9,-1,p)*actual[r]
        assert (lhs-C*g[r])%p==0, (p,r)
    return (p,C,v,E,actual[0],actual[1],actual[2] if len(actual)>2 else None,(av,ab),(dv,db), db%p)


if __name__=='__main__':
    for p in (13,19,37,43,61,67,211,373):
        print(check(p))
    q=check(373)
    assert q==(373,40,154,0,243,226,350,(112646,57442),(0,130607),57)
    print('verified eight source-prime instances; exceptional target p=373 two-port jet recovered')
