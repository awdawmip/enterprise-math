"""Author-side exact p-adic witness for D25 high-seam unified Beta/Cauchy kernel.

No native benchmark, Source Result, or independent review is claimed.
"""
from fractions import Fraction
from math import factorial, comb


def primes_upto(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit**.5) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((limit-d*d)//d + 1)
    return [p for p in range(7, limit+1) if sieve[p] and p%6 == 1]


def inv(x, p):
    return pow(x % p, -1, p)


def modular_original_high(p):
    m = (p-1)//6
    v, unit = 0, 1
    total = 0
    for n in range(4*m+1):
        if m < n < 4*m and n != 2*m:
            assert v == 1, (p,n,v)
            knum = (2*p+1-3*n)*(6*n+2*p+3)
            kden = (3*n+p+2)*(3*n+2*p+1)
            total = (total + (unit*knum)*inv(kden,p)) % p
        if n == 4*m:
            break
        num = (4*m+1+2*n)*(3*n+1)*(3*n+2)
        den = 36*(n+1)*(2*m+n+1)*(4*m+n+1)
        while num%p == 0:
            num//=p
            v+=1
        while den%p == 0:
            den//=p
            v-=1
        unit = unit*num*inv(den,p)%p
    return total


def rational_a(m, r):
    return Fraction(2**(m-r) if m>=r else 1, 1 if m>=r else 2**(r-m)) * Fraction(
        factorial(2*m)*factorial(r-1),factorial(m+r)*factorial(m-1))


def rational_c(m, s):
    return Fraction(factorial(2*m+1)*factorial(m+s-1),
                    2**(s-1)*factorial(m)*factorial(2*m+s))


def modular_unified_high(p):
    m=(p-1)//6
    B = factorial(2*m-1)*factorial(2*m)*inv(factorial(4*m),p)%p
    a = pow(2,m-1,p)*factorial(2*m)*inv(factorial(m+1)*factorial(m-1),p)%p
    out = 0
    one_third=inv(3,p)
    for r in range(1,3*m):
        if r != m:
            weight = 1 if r < m else one_third
            k = 4*(1-2*r)*(3*r+1)*inv((2*r+1)*(6*r+1),p)%p
            out = (out + weight*a*k)%p
        if r<3*m-1:
            a = a*r*inv(2*(m+r+1),p)%p
    return B*out%p, out


def verify_cauchy_bridge():
    for m in range(1,15):
        for r in range(1,3*m):
            cauchy = Fraction(m*comb(2*m,m)*2**m,2**r) * sum(
                (Fraction((-1)**n*comb(m,n),r+n) for n in range(m+1)), Fraction(0))
            assert cauchy == rational_a(m,r), (m,r)



def rising(x, count):
    value = Fraction(1)
    for j in range(count):
        value *= x+j
    return value


def verify_mirror_split():
    # Exact rank-two divided-difference identity on the same seam carrier.
    k = lambda x: Fraction(-2) + Fraction(4,6*x+1) + Fraction(2,2*x+1)
    for m in range(1,14):
        pairs = [(r,Fraction(1) if r<m else Fraction(1,3))
                 for r in range(1,3*m) if r!=m]
        F = lambda n: sum((w*Fraction(1,2**r*(r+n)) for r,w in pairs),Fraction(0))
        F6 = sum((w*Fraction(1,2**r*(6*r+1)) for r,w in pairs),Fraction(0))
        F2 = sum((w*Fraction(1,2**r*(2*r+1)) for r,w in pairs),Fraction(0))
        raw = sum((w*rational_a(m,r)*k(r) for r,w in pairs),Fraction(0))
        refl = sum(((-1)**n*comb(m,n)*k(-n)*F(n) for n in range(m+1)),Fraction(0))
        moments = 4*factorial(m)*F6/rising(Fraction(-1,6),m+1) + 2*factorial(m)*F2/rising(Fraction(-1,2),m+1)
        out = m*comb(2*m,m)*2**m*(refl+moments)
        assert raw==out,(m,raw,out)


def main():
    verify_cauchy_bridge()
    verify_mirror_split()
    for m in range(1,13):
        lam = -Fraction(2*m+1,12*m)
        assert lam-Fraction(1,3)==-Fraction(6*m+1,12*m)
        for s in range(1,2*m):
            assert -rational_c(m,s)/24 == lam*rational_a(m,m+s)
    pts=[]
    for p in primes_upto(1000):
        org=modular_original_high(p)
        uni, scalar=modular_unified_high(p)
        assert org==uni,(p,org,uni)
        pts.append((p,org,scalar))
    print('Cauchy exact m=1..14: PASS; mirror exact m=1..13: PASS; seam exact m=1..12: PASS')
    print('original high versus unified: ',len(pts),'primes <=1000 PASS',
          'target classes:',sum(p%24 in (13,19) for p,_,_ in pts))
    print('examples:',[x for x in pts if x[0] in (13,19,31,37,61)])


if __name__=='__main__':
    main()
