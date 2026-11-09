"""D25: exact mod-p Pfaff-to-CM-24 certificate; author-side, not a native run.

Run: python d25_pfaff_cm24_short_root_20261109.py
No external dependencies; no floating point; verifies all eligible primes <=10000 and
polynomial equality by enough field evaluations for all eligible p<=400.
"""
from math import isqrt


def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, isqrt(limit) + 1):
        if sieve[q]:
            sieve[q*q:limit+1:q] = b'\x00' * ((limit-q*q)//q + 1)
    return [i for i in range(2, limit+1) if sieve[i]]


def short_Q0(p):
    m = (p + 3) // 8
    a, n = 5*m-2, m-1
    term = result = 1
    inv8 = pow(8, -1, p)
    for k in range(n):
        term = term * (-(a-k)) * (n-k) * inv8 * pow((k+1)*(k+1), -1, p) % p
        result = (result + term) % p
    return result


def P_root_and_derivative(p):
    """Original P(z)=sum binom(a,k)binom(b,k) z^k, z=1/9."""
    m=(p+3)//8
    a,b=5*m-2,7*m-3
    z=pow(9,-1,p)
    term=1
    value=1
    weighted=0
    for k in range(a):
        term=term*(a-k)*(b-k)*z*pow((k+1)**2,-1,p)%p
        value=(value+term)%p
        weighted=(weighted+(k+1)*term)%p
    return value,9*weighted%p


def h_coefficients(p):
    """[t^((p-1)/2)] (t^2+2*t+x)^((p-1)/2)."""
    q = (p-1)//2
    c = pow(2, q, p)
    yield c
    inv4 = pow(4, -1, p)
    for k in range(q//2):
        c = c*(q-2*k)*(q-2*k-1)*inv4*pow((k+1)**2, -1, p) % p
        yield c


def hasse_at(p, x):
    power = 1
    value = 0
    for c in h_coefficients(p):
        value = (value + c*power) % p
        power = power*x % p
    return value


def hasse_mod_s_quadratic(p):
    """Coefficient pair A+B*s modulo (36*s^2-36*s+1)."""
    inv36 = pow(36, -1, p)
    zero, one = 0, 0
    a, b = 1, 0
    for c in h_coefficients(p):
        zero = (zero+c*a) % p
        one = (one+c*b) % p
        a, b = -b*inv36 % p, (a+b) % p
    return zero, one


def R_at(p, x):
    """R(4x(1-x)) at x in F_p via recurrence, including z=1."""
    m = (p+3)//8
    a, n = 5*m-2, m-1
    z = (4*x*(1-x)) % p
    total = 0
    ca = cn = 1
    power = 1
    for k in range(n+1):
        total = (total + (-1 if k%2 else 1)*ca*cn*power*pow(1-z,n-k,p)) % p
        if k<n:
            ca = ca*(a-k)*pow(k+1,-1,p)%p
            cn = cn*(n-k)*pow(k+1,-1,p)%p
            power = power*z%p
    return total


def main():
    ps=[p for p in primes_upto(10000) if p % 24 == 13]
    assert len(ps) == 157, len(ps)
    for p in ps:
        assert (p+3)%8 == 0
        assert short_Q0(p) == 0, ('Q0',p)
        pval,pder=P_root_and_derivative(p)
        assert pval == 0 and pder != 0, ('simple root',p,pval,pder)
        assert hasse_mod_s_quadratic(p)==(0,0), ('CM Hasse',p)
    poly_checked = 0
    for p in ps:
        if p > 400:
            continue
        m=(p+3)//8
        degree=2*m-1
        unit=pow(2,(p-1)//2,p)
        assert unit == p-1
        for x in range(degree+1):
            left=hasse_at(p,x)
            right=unit*(1-2*x)*R_at(p,x)%p
            assert left==right, ('pullback',p,x,left,right)
        poly_checked += 1
    jA, jB = 2417472, 1707264
    assert 2*jA==4834944
    assert jA*jA-2*jB*jB==14670139392
    for p in (13,37,61,109,373,9973):
        if p % 24 == 13:
            print('p',p,'m',(p+3)//8,'Q0',short_Q0(p), 'P_derivative',P_root_and_derivative(p)[1],
                  'Hasse remainder',hasse_mod_s_quadratic(p))
    print('PASS: Q0=P=0, P_derivative !=0, Hasse remainder=(0,0) for',len(ps),
          'primes p<=10000, p=13 mod24')
    print('PASS: full polynomial identity by field-evaluation certificates for',
          poly_checked,'primes p<=400')
    print('PASS: CM -24 class polynomial arithmetic')


if __name__=='__main__':
    main()
