"""D25 first-digit Gauss/216 certified finite exact checks, external arithmetic only."""
from math import isqrt


def primes(n):
    s = bytearray(b'\1') * (n + 1)
    s[:2] = b'\0\0'
    for k in range(2, isqrt(n) + 1):
        if s[k]:
            s[k*k:n+1:k] = b'\0' * ((n-k*k)//k+1)
    return [p for p in range(7, n+1) if s[p] and p % 6 == 1]


def obs(p, two_digits=False):
    m = (p-1)//6
    d = D = U = a = 1
    Dz = 0
    for k in range(1, m+1):
        d = d*(m-k+1)*(2*m-k+1)*pow(2*k*k,-1,p)%p
        D = (D+d)%p
        Dz = (Dz+2*k*d)%p
    for k in range(1,2*m+1):
        a = a*(k-1-3*m)*(k-1-2*m)*(k-1-4*m)*pow(2*k**3,-1,p)%p
        U = (U+(6*k+1)*a)%p
    flux = (D+6*Dz)%p
    assert U == D*flux%p, (p,'Clausen flux')
    if not two_digits:
        return D,Dz,flux,U,None
    M=p*p
    a=U0=1
    for k in range(1,2*m+1):
        a=a*(k-1-3*m)*(k-1-2*m)*(k-1-4*m)*pow(2*k**3,-1,M)%M
        U0=(U0+(6*k+1)*a)%M
    a=W=1
    for k in range(1,p):
        a=a*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,M)%M
        W=(W+(6*k+1)*a)%M
    assert U0%p == 0 and W%p == 0, (p,'first-digit')
    alpha=U0//p
    beta=((W-U0)//p)%p
    assert (alpha+beta)%p == 1, (p,'two-digit balance')
    return D,Dz,flux,U,(alpha,beta,W,U0)


def main():
    ps=primes(10000)
    counts={r:{'D_zero':0,'flux_zero':0} for r in (1,3,5,7)}
    sample={}
    for p in ps:
        D,Dz,flux,U,_=obs(p)
        assert (D==0) != (flux==0), (p,'nonexclusive')
        assert (D==0) == (p%8 in (3,5)), (p,'character pattern')
        counts[p%8]['D_zero' if D==0 else 'flux_zero']+=1
        if p in (7,13,19,31,37,43,67,73,373,5113):
            sample[p]=(D,Dz,flux)
    two=[p for p in ps if p<=1999]
    for p in two:
        D,Dz,flux,U,ports=obs(p,True)
        if p in sample:
            sample[p]=(D,Dz,flux,ports)
    print('primes<=10000:',len(ps),'target classes:',sum(p%24 in (13,19) for p in ps))
    print('D/flux classes:',counts)
    print('two-digit exact p^2:',len(two),'target:',sum(p%24 in(13,19) for p in two))
    print('all assertions PASS; selected:',sample)


if __name__=='__main__':
    main()
