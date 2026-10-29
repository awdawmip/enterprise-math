"""D25 author-side: independently check A216 tier-two universal kernel.
No native H0/B0 execution, formal Source admission, or claim implied.
"""
from math import comb, factorial


def primes_below(limit):
    prime = [True] * limit
    prime[0:2] = [False, False]
    for d in range(2, int(limit**0.5) + 1):
        if prime[d]:
            for n in range(d*d, limit, d):
                prime[n] = False
    return [n for n, yes in enumerate(prime) if yes]


def q_original(p):
    m = (p-1)//6
    modulus = p**3
    a = 1
    total = 0
    for n in range(p):
        if 3*m+1 <= n <= 4*m:
            term = (6*n+1)*a % modulus
            assert term % (p*p) == 0, (p,n,term)
            total = (total+term) % modulus
        if n < p-1:
            numerator = (2*n+1)*(3*n+1)*(3*n+2)
            denominator = 36*(n+1)**3
            a = (a*numerator*pow(denominator,-1,modulus)) % modulus
    assert total % (p*p) == 0
    return total//(p*p)


def q_reflected(p):
    m=(p-1)//6
    out=0
    for r in range(2*m,3*m):
        term=(6*r+5)*pow(216,r,p)*pow(factorial(r),5,p)
        term*=pow(factorial(2*r+1)*factorial(3*r+2-p),-1,p)
        out=(out+term)%p
    return out


def q_universal(p):
    m=(p-1)//6
    c=(3*pow(216,2*m,p)*pow(factorial(2*m),5,p)*pow(factorial(4*m+1),-1,p))%p
    t=1
    h=0
    for s in range(m):
        h=(h+t)%p
        if s < m-1:
            numerator=4*(2*s+3)*(3*s+2)**3
            denominator=3*(2*s+1)*(6*s+7)*(3*s+4)*(s+1)
            assert denominator % p != 0, (p,s)
            t=(t*numerator*pow(denominator,-1,p))%p
    return c,h,c*h%p


def q_raw_independent(p):
    m=(p-1)//6
    modulus=p**3
    total=0
    for n in range(3*m+1,4*m+1):
        numerator=(6*n+1)*comb(2*n,n)**2*comb(3*n,n)
        term=numerator*pow(216,-n,modulus)%modulus
        assert term%(p*p)==0
        total=(total+term)%modulus
    return total//(p*p)


if __name__ == '__main__':
    checked=0
    targets=0
    for p in primes_below(1500):
        if p < 7 or p%6!=1:
            continue
        q=q_original(p)
        r=q_reflected(p)
        c,h,u=q_universal(p)
        assert q==r==u,(p,q,r,c,h,u)
        checked+=1
        targets+=(p%24 in (13,19))
        if p in (7,13,19,31,373):
            raw=q_raw_independent(p)
            assert raw==q,(p,raw,q)
            print('CERT',p,'Q',q,'C',c,'H',h,'raw',raw)
    print('PASS_ALL_A216_UNIVERSAL_MID_KERNEL',checked,'TARGET_13_19_MOD24',targets)
