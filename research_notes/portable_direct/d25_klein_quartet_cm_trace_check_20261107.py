"""Exact finite-field checks for D25 Pfaff Klein-quartet reduction.
All arithmetic is integer / modular; no floating point and no native benchmark claims.
"""
from collections import Counter


def primes_upto(n):
    a = bytearray(b'\x01')*(n+1)
    a[:2] = b'\x00\x00'
    for d in range(2, int(n**.5)+1):
        if a[d]:
            a[d*d:n+1:d] = b'\x00'*(((n-d*d)//d)+1)
    return [i for i in range(2,n+1) if a[i]]


def legendre(z, p):
    r = pow(z%p, (p-1)//2,p)
    return 0 if r == 0 else (1 if r==1 else -1)


def check(p):
    assert p%24==13
    m = (p-1)//6
    assert m%2==0
    inverse2 = pow(2,-1,p)
    branch = {0,p-1,(-inverse2)%p}

    def sigma(x): return (-1-x)%p
    def psi(x): return (-x*pow(2*x+1,-1,p))%p
    def rho(x): return (-(x+1)*pow(2*x+1,-1,p))%p
    def v(x):return pow((pow(x,5,p)*pow(x+1,2,p)*(2*x+1))%p,m,p)

    allpoints = set(range(p))-branch
    remaining = set(allpoints)
    surviving = 0
    exceptional = 0
    total_v=0
    zero4=0
    while remaining:
        x=next(iter(remaining))
        orb={x,sigma(x),psi(x),rho(x)}
        assert orb<=allpoints
        assert len(orb) in (2,4)
        remaining-=orb
        alpha=legendre(x*(x+1),p)
        beta=legendre(2*x+1,p)
        w=v(x)
        assert alpha in (-1,1) and beta in (-1,1)
        assert v(sigma(x))==(alpha*w)%p
        assert v(psi(x))==(beta*w)%p
        assert v(rho(x))==(alpha*beta*w)%p
        orbit_sum=sum(v(z) for z in orb)%p
        total_v=(total_v+orbit_sum)%p
        if len(orb)==2:
            exceptional+=1
            assert alpha==beta==-1 and orbit_sum==0
        else:
            assert orbit_sum==(w*(1+alpha)*(1+beta))%p
            if alpha==beta==1:
                assert orbit_sum==(4*w)%p
                surviving+=1
            else:
                assert orbit_sum==0
                zero4+=1

    t=sum(legendre(x*(x+1)*(2*x+1),p) for x in range(p))
    assert (p-7+t)%16==0
    assert exceptional==1 and 4*(surviving+zero4)+2==p-3
    assert surviving==(p-7+t)//16
    S=1
    term=1
    for k in range(1,m+1):
        term = term*(m-k+1)*(2*m+k)*pow(k*k,-1,p)%p
        S=(S+term)%p
    assert S==(-total_v)%p
    return p,t,surviving,zero4,S

if __name__=='__main__':
    tests=[check(p) for p in primes_upto(10000) if p%24==13]
    print('cases',len(tests),'failures 0')
    for p in [13,37,61,109,373,397,421]:
        print(next((t for t in tests if t[0]==p),None))
