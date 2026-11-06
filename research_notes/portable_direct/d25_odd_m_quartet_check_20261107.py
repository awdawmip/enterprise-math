"""D25 p=19 mod24 odd-m Klein orbit signed-reduction exact integer check.
Standalone Python 3 stdlib. Scientific run is not the pending native p373 benchmark.
"""


def primes_upto(n):
    a=bytearray(b'\x01')*(n+1)
    a[:2]=b'\x00\x00'
    for d in range(2,int(n**0.5)+1):
        if a[d]:
            a[d*d:n+1:d]=b'\x00'*(((n-d*d)//d)+1)
    return [i for i in range(2,n+1) if a[i]]


def legendre(z,p):
    x=pow(z%p,(p-1)//2,p)
    return 0 if x==0 else (1 if x==1 else -1)


def check(p):
    assert p%24==19
    m=(p-1)//6
    assert m%2==1
    inv2=pow(2,-1,p)
    X=set(range(p))-{0,p-1,(-inv2)%p}
    def s(x):return (-1-x)%p
    def q(x):return (-x*pow(2*x+1,-1,p))%p
    def r(x):return (-(x+1)*pow(2*x+1,-1,p))%p
    def v(x):return pow((pow(x,5,p)*pow(x+1,2,p)*(2*x+1))%p,m,p)
    def a(x):return legendre(x*(x+1),p)
    def b(x):return legendre(2*x+1,p)
    assert sum(a(x) for x in X)==0
    assert sum(b(x) for x in X)==0
    t=sum(legendre(x*(x+1)*(2*x+1),p) for x in range(p))
    assert t==0
    remaining=set(X)
    c=0
    total=0
    chosen=0
    while remaining:
        x=next(iter(remaining))
        orbit={x,s(x),q(x),r(x)}
        assert len(orbit)==4 and orbit<=X
        remaining-=orbit
        assert {(a(z),b(z)) for z in orbit}=={(-1,-1),(-1,1),(1,-1),(1,1)}
        assert v(s(x))==(a(x)*v(x))%p
        assert v(q(x))==(-b(x)*v(x))%p
        assert v(r(x))==(a(x)*b(x)*v(x))%p
        assert sum(v(z) for z in orbit)%p == (v(x)*(1+a(x)-b(x)+a(x)*b(x)))%p
        w=next(z for z in orbit if a(z)==b(z)==1)
        assert sum(v(z) for z in orbit)%p == (2*v(w))%p
        total=(total+sum(v(z) for z in orbit))%p
        chosen=(chosen+2*v(w))%p
        c+=1
    assert c==(p-3)//4 and total==chosen
    S=1
    term=1
    for k in range(1,m+1):
        term=term*(m-k+1)*(2*m+k)*pow(k*k,-1,p)%p
        S=(S+term)%p
    assert S==(-2*sum(v(z) for z in X if a(z)==b(z)==1))%p
    assert S==(-total)%p
    return p,c,S,t


if __name__=='__main__':
    tests=[check(p) for p in primes_upto(10000) if p%24==19]
    print('cases',len(tests),'failures 0')
    for p in [19,43,67,139,163,211,331,379]:
        print(next((t for t in tests if t[0]==p),None))
