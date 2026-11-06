"""Exact Clausen-square third-digit boundary. Python 3 standard library."""
from math import isqrt
def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))
def run(p):
    assert p>3 and p%6==1 and prime(p)
    m=(p-1)//6; q=p**3; z=pow(2,-1,q)
    u=[1]*p; t=[1]*p
    for k in range(1,p):
        n=k-1
        u[k]=u[n]*(6*n+1)*(3*n+1)*pow(18*k*k,-1,q)%q
        t[k]=t[n]*z%q
    F=sum(u[k]*t[k] for k in range(p))%q
    theta=sum(k*u[k]*t[k] for k in range(p))%q
    gauss=(F*F+12*F*theta)%q
    direct_tail=0
    if p<=373:
        for i in range(p):
            for j in range(max(0,p-i),p):
                direct_tail=(direct_tail+(6*(i+j)+1)*u[i]*u[j]*t[i]*t[j])%q
    band=0
    for i in range(1,m+1):
        for j in range(p-i,p):
            band=(band+2*(6*(i+j)+1)*u[i]*u[j]*t[i]*t[j])%q
    h=pow(10,-1,p)
    K=0; iz=pow(2,-1,p)
    for ell in range(1,m+1):
        assert u[p-ell]//p**2%p==h,(p,ell)
        for i in range(ell,m+1):
            K=(K+(6*(i-ell)+1)*u[i]*h*pow(iz,i-ell,p))%p
        if ell<m:
            h=h*18*ell*ell*pow((6*ell+5)*(3*ell+2),-1,p)%p
    assert band==K*p*p,(p,K,band)
    if p<=373: assert direct_tail==band,(p,direct_tail,band)
    a=1; W=0
    for n in range(p):
        W=(W+(6*n+1)*a)%q
        if n<p-1:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,q)%q
    assert W==(gauss-band)%q,(p,W,gauss,band)
    return p,K,gauss,W,F%p
if __name__=="__main__":
    results=[run(p) for p in range(7,2000) if p%6==1 and prime(p)]
    assert len(results)==148
    assert sum(p%24 in (13,19) for p,*_ in results)==77
    extra=run(5113)
    print("PASS",len(results),"primes p<=1999 plus",extra[0])
    for r in results+[extra]:
        if r[0] in (13,19,67,373,5113): print(r)
