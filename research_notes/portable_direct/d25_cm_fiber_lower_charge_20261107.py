"""D25 Fricke-common-CM-coordinate lower-source residual; exact prime checks."""
from math import comb,isqrt

def primes(N):return [p for p in range(5,N+1) if all(p%d for d in range(2,isqrt(p)+1))]

def observed_operator(p,mode,x):
    a,b=((1,6),(1,3)) if mode=='A' else (((1,8),(3,8)) if p%8==3 else ((5,8),(7,8)))
    h=2*((p-1)//6)+1 if mode=='A' else 3*((p-3)//8 if p%8==3 else (p-5)//8)+2
    P=p**3;c=1;rr=[0]*p
    for n in range(p):
        if n>=h:assert c%(p*p)==0;rr[n]=c//(p*p)%p
        if n<p-1:c=c*(a[1]*n+a[0])*(b[1]*n+b[0])*pow(a[1]*b[1]*(n+1)**2,-1,P)%P
    za=pow(a[1],-1,p)*a[0]%p;zb=pow(b[1],-1,p)*b[0]%p
    ans=0
    for n in range(h,p):
        ans+=(n*n*rr[n]*pow(x,n,p)-((n+za)*(n+zb))*rr[n]*pow(x,n+1,p))
    return ans%p

def fiber(p):
    assert p%24 in (13,19)
    m=(p-1)//6;k=(p-3)//8 if p%8==3 else (p-5)//8
    la=observed_operator(p,'A',pow(2,-1,p))
    lb=observed_operator(p,'B',pow(9,-1,p))
    direct=(36*la-192*lb)%p
    rhs=(((-1)**m)*pow(pow(4,m,p)*comb(2*m,m),-1,p)+pow(pow(9,3*k+1,p)*comb(3*k+1,k),-1,p))%p
    assert direct==rhs,(p,direct,rhs)
    return p,direct

if __name__=='__main__':
    ps=[p for p in primes(5000) if p%24 in (13,19)]
    records=[fiber(p) for p in ps]
    print('PASS',len(records),'CM fiber residuals')
    print('samples',[x for x in records if x[0] in (13,19,37,43,67,109,373)])
    print('zero_count',sum(x[1]==0 for x in records))
