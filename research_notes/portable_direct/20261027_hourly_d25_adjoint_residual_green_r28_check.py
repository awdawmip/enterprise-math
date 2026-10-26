"""R28 exact finite Green inverse and weighted adjoint transfer author check."""
from fractions import Fraction
from math import factorial, isqrt

def invq(q, p):
    q = Fraction(q)
    return q.numerator % p * pow(q.denominator % p, -1, p) % p

def primes_upto(n):
    for p in range(7, n):
        if p % 6 == 1 and all(p % t for t in range(2, isqrt(p) + 1)):
            yield p

def check(p):
    m = (p - 1) // 6
    e3, e6, e12 = (invq(Fraction(1, d), p) for d in (3, 6, 12))
    aa, hh = [1], [1]
    for r in range(1, m):
        ar = r*(r+e6)*(r+e3) % p
        hr = (r-e12)*(r+5*e12) % p
        assert ar and hr
        aa.append(aa[-1] * pow((r-e3)%p,3,p)*pow(ar,-1,p)%p)
        hh.append(hh[-1] * r*(r+e3)*pow(hr,-1,p)%p)
    C = 3*pow(216,2*m,p)*pow(factorial(2*m),5,p)*pow(factorial(4*m+1),-1,p)%p
    D = 2*pow(2304,2*m,p)*pow(factorial(2*m),4,p)*pow(factorial(2*m+2),-1,p)%p
    assert C and D
    vw = [C*(2*r+1)*pow(2,r,p)%p for r in range(m)]
    vs = [D*(8*r+13*e3)*pow(9,r,p)*hh[r]%p for r in range(m)]
    v = [(vw[r]-vs[r])%p for r in range(m)]
    U = sum(vw[r]*aa[r] for r in range(m))%p
    M = sum(vs[r]*aa[r] for r in range(m))%p
    c = aa[-1]*pow(8,-1,p)%p
    assert c

    def L(f):
        return [0]+[(r*(r+e6)*(r+e3)*(f[r] if r<m else 0)
                     -pow((r-e3)%p,3,p)*f[r-1])%p for r in range(1,m+1)]

    for f in (aa, [r*r+7 for r in range(m)], [13*r+5 for r in range(m)]):
        f=[x%p for x in f]
        gg=L(f)
        zz=[0]*m
        zz[-1]=gg[m]*pow(c,-1,p)%p
        for r in range(m-2,-1,-1):
            t=r+1
            A=t*(t+e6)*(t+e3)%p
            zz[r]=(zz[r+1]-gg[t]*pow(A*aa[t]%p,-1,p))%p
        assert all(aa[r]*zz[r]%p==f[r] for r in range(m))
        prefix=0
        adj=gg[m]*(U-M)*pow(c,-1,p)%p
        for t in range(1,m):
            prefix=(prefix+v[t-1]*aa[t-1])%p
            A=t*(t+e6)*(t+e3)%p
            adj=(adj-gg[t]*prefix*pow(A*aa[t]%p,-1,p))%p
        direct=sum(v[r]*f[r] for r in range(m))%p
        assert direct==adj, (p,direct,adj)
    return (p,m,U,M,(U-M)%p,(U-M)*pow(c,-1,p)%p)

if __name__=='__main__':
    rows=[check(p) for p in primes_upto(2000)]
    assert len(rows)==148
    print('PASS',len(rows),'primes, full Green inverse + exact adjoint for 3 polynomial inputs each')
    print('p m U M U-M endpoint_dual')
    for row in rows:
        if row[0] in (7,13,19,37,61,181,373,733,997): print(*row)
