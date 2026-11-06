"""D25 portable two-port Hensel checker. Python 3 standard library, exact mod p^2."""
from math import comb

def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**.5)+1))

def vals(m):
    terms = [comb(m,k)*comb(2*m+k,k) for k in range(m+1)]
    return sum(terms), sum(k*t for k,t in enumerate(terms))

def jets(m,z,q):
    a=b=c=0
    for k in range(m,-1,-1):
        c=(z*c+2*b)%q
        b=(z*b+a)%q
        a=(z*a+comb(m,k)*comb(2*m,k))%q
    return a,b,c

def verify(p):
    m=(p-1)//6; q=p*p
    S,T=vals(m)
    B=(1-12*m)*S+24*T
    V=-2*m*S+4*T
    U=(-36*m-11)*V+48*m*m*S
    z0=pow(2,-1,q); sc=pow(2,m,q)
    d,dp,ddp=jets(m,z0,q)
    assert (sc*d-S)%q == (sc*dp-V)%q == 0
    assert (sc*(d+6*dp)-B)%q == (sc*(dp+6*ddp)-U)%q == 0
    zeroD=S%p==0; zeroE=B%p==0
    assert zeroD != zeroE, (p,"classification")
    if zeroD:
        assert V%p == 4*T%p and T%p
        branch="D"; numerator=S//p; derivative=V%p
    else:
        assert p!=13 and U%p == (13*pow(6,-1,p)*S)%p
        branch="E"; numerator=B//p; derivative=U%p
    u=(-numerator*pow(derivative,-1,p))%p
    z=(z0+p*u)%q; nd,ndp,_=jets(m,z,q)
    assert (nd if zeroD else nd+6*ndp)%q==0
    wrong=(z0+p*((u+1)%p))%q
    wd,wdp,_=jets(m,wrong,q)
    assert (wd if zeroD else wd+6*wdp)%q!=0
    return p,branch,u,z,derivative,S%q,T%q

if __name__ == "__main__":
    results=[verify(p) for p in range(7,2000) if p%6==1 and prime(p)]
    assert len(results)==148
    assert sum(r[1]=="D" for r in results)==77
    assert sum(r[1]=="E" for r in results)==71
    extra=verify(5113)
    print("PASS",len(results),"primes <=1999 plus",extra[0],"branches D/E=77/71")
    for r in results+[extra]:
        if r[0] in (7,13,19,31,37,67,373,5113): print(r)
