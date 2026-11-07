"""Exact p^3 lift for 216 weighted sum, p=6m+1; author-side portable test."""
from math import factorial, comb

def prime(p):
    return p>1 and all(p%d for d in range(2,__import__('math').isqrt(p)+1))

def check(p):
    assert prime(p) and p%6==1 and p>3
    m=(p-1)//6; q=p**3
    f=[factorial(i)%q for i in range(p)]
    inv=lambda a: pow(a%q,-1,q)
    H=[0]*p; J=[0]*p
    for i in range(1,p):
        H[i]=(H[i-1]+inv(i))%q
        J[i]=(J[i-1]+inv(i*i))%q
    D=lambda r,n,T: (T[r]-T[r-n])%q
    original=1; port=[0]*4
    for n in range(p):
        if n:
            original=original*(2*n-1)*(3*n-2)*(3*n-1)*inv(36*n**3)%q
        common=inv(2**n)*inv(f[n])**3%q
        if n<=2*m:
            lead=(-1)**n*f[2*m]*inv(f[2*m-n])*f[3*m]*inv(f[3*m-n])*f[4*m]*inv(f[4*m-n])*common%q
            e=-(D(2*m,n,H)*inv(3)+D(3*m,n,H)*inv(2)+2*D(4*m,n,H)*inv(3))%q
            v=(D(2*m,n,J)*inv(9)+D(3*m,n,J)*inv(4)+4*D(4*m,n,J)*inv(9))%q
            a=lead*(1+p*e+p*p*inv(2)*(e*e-v))%q; level=0
        elif n<=3*m:
            lead=f[2*m]*f[n-2*m-1]*f[3*m]*inv(f[3*m-n])*f[4*m]*inv(f[4*m-n])*common*inv(3)%q
            e=(inv(3)*(H[n-2*m-1]-H[2*m])-inv(2)*D(3*m,n,H)-2*inv(3)*D(4*m,n,H))%q
            a=p*lead*(1+p*e)%q; level=1
        elif n<=4*m:
            lead=(-1)**(3*m+n)*f[2*m]*f[n-2*m-1]*f[3*m]*f[n-3*m-1]*f[4*m]*inv(f[4*m-n])*common*inv(6)%q
            a=p*p*lead%q; level=2
        else: a=0; level=3
        assert a==original,(p,n,a,original)
        port[level]=(port[level]+(6*n+1)*a)%q
        if p in (13,19,43,67,373):
            raw=comb(2*n,n)**2*comb(3*n,n)*inv(216**n)%q
            assert a==raw,(p,n,a,raw)
    return port

if __name__=='__main__':
    ps=[p for p in range(7,1000) if p%6==1 and prime(p)]
    for p in ps:check(p)
    print('PASS:',len(ps),'primes;',sum(ps),'exact coefficients checked; p range',min(ps),max(ps))
    for p in (13,19,43,67,373):
        L,M,U,Z=check(p)
        print(p,'L=',L,'M/p=',M//p,'U/p2=',U//(p*p),'sum=',(L+M+U)%p**3)
