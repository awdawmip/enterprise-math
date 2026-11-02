"""D25 signed 216/2304 cutoff mismatch; exact bounded prime replay."""
from math import comb, factorial, isqrt

def primes(n):
    return [p for p in range(13, n+1) if p%24 in (13,19)
            and all(p%d for d in range(2,isqrt(p)+1))]

def run(p):
    modulus = p**3
    a, b = [], []
    # Two independently defined original binomial source series.
    for k in range(p):
        a.append((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,modulus)%modulus)
        b.append((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,modulus)%modulus)
    l, h = 2*p//3, 3*p//4
    assert all(x==0 for x in a[l+1:]) and all(x==0 for x in b[h+1:])
    strip = sum(b[l+1:h+1]) % modulus
    assert strip%p**2==0
    u = []
    for k in range(l+1,h+1):
        v = 2*(8*k+1)*factorial(4*k-2*p)*pow(factorial(k),-4,p)*pow(2304,-k,p)%p
        assert v == (b[k]//p**2)%p
        u.append(v)
    for k in range(l+1,h):
        numerator = (8*k+9)
        for j in range(1,5): numerator *= 4*k+j
        denominator = 2304*(8*k+1)*(k+1)**4
        assert denominator%p != 0
        assert (u[k-l]*denominator-u[k-l-1]*numerator)%p == 0
    defect = (sum(a[:l+1])-sum(b[:l+1])) % modulus
    assert (sum(a)-sum(b)-defect+strip)%modulus == 0
    assert defect%p**2 == 0
    assert sum(b)%modulus == p and sum(a)%modulus == p # Last is finite evidence only.
    assert defect//p**2 == sum(u)%p == strip//p**2
    k0 = (p+3)//4
    assert k0*3 < p
    assert a[k0]%p != 0 and b[k0]%p == 0
    return (p, strip//p**2, l+1, h, len(u))

if __name__=='__main__':
    results=[run(p) for p in primes(2000)]
    assert len(results)==77
    print('cases',len(results),'zero_strip',[p for p,d,*_ in results if d==0])
    for x in results:
        if x[0] in (13,19,37,43,109,181,373,1171): print(*x)
