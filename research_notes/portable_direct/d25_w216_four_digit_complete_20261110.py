"""Exact W216 fourth-digit four-grade certificate, author-side only."""
from math import comb,factorial

def primes_upto(n):
    z=[True]*(n+1);z[:2]=[False,False]
    for k in range(2,int(n**.5)+1):
        if z[k]:
            for j in range(k*k,n+1,k):z[j]=False
    return [p for p in range(5,n+1) if z[p] and p%6==1]

def check(p):
    m=(p-1)//6;M=p**4;M2=p**2
    inv2=pow(2,-1,M);inv3=pow(3,-1,M);inv6=pow(6,-1,M)
    H=[[0]*(4*m+1) for _ in range(3)]
    for n in range(1,4*m+1):
        v=pow(n,-1,M)
        for r in range(3):H[r][n]=(H[r][n-1]+pow(v,r+1,M))%M
    def D(r,n,k):return (H[r-1][n]-H[r-1][n-k])%M
    F=[factorial(i) for i in range(p)]
    A=[comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,M)%M for k in range(p)]
    orig=sum((6*k+1)*A[k] for k in range(p))%M
    low0=low1=0
    for k in range(2*m+1):
        B=(-1)**k*pow(inv2,k,M)*comb(2*m,k)*comb(3*m,k)*comb(4*m,k)%M
        a=(inv3*D(1,2*m,k)+inv2*D(1,3*m,k)+2*inv3*D(1,4*m,k))%M
        b=(inv3**2*D(2,2*m,k)+inv2**2*D(2,3*m,k)+4*inv3**2*D(2,4*m,k))%M
        c=(inv3**3*D(3,2*m,k)+inv2**3*D(3,3*m,k)+8*inv3**3*D(3,4*m,k))%M
        t=(1-p*a+p*p*inv2*(a*a-b)+p**3*inv6*(-a**3+3*a*b-2*c))%M
        pred=B*t%M
        assert pred==A[k],(p,k,'J0-3')
        low0=(low0+(6*k+1)*pred)%M
    for k in range(2*m+1,3*m+1):
        T=F[2*m]*F[k-2*m-1]*F[3*m]*F[4*m]%M
        T=T*pow(F[3*m-k]*F[4*m-k]*F[k]**3*pow(2,k,M),-1,M)%M
        g=(inv3*(H[0][k-2*m-1]-H[0][2*m])-inv2*D(1,3*m,k)-2*inv3*D(1,4*m,k))%M
        d=(inv3**2*(H[1][k-2*m-1]+H[1][2*m])+inv2**2*D(2,3*m,k)+4*inv3**2*D(2,4*m,k))%M
        pred=p*inv3*T*(1+p*g+p*p*inv2*(g*g-d))%M
        assert pred==A[k],(p,k,'J1-2')
        low1=(low1+(6*k+1)*pred)%M
    k0=2*m+1; C=(A[k0]//p)*(A[p-k0]//p**2)%M2
    e=0;w2=0
    for j in range(m):
        k=k0+j;L=A[k]//p%M2
        H2=C*pow(k0*pow(k,-1,M2),3,M2)*(1+p*e)*pow(L,-1,M2)%M2
        assert H2==A[p-k]//p**2%M2,(p,k,'J2-1')
        w2=(w2+(6*(p-k)+1)*p*p*H2)%M
        if j<m-1:
            e=(e-3*pow(k,-1,p)+2*pow(2*k+1,-1,p)+3*pow(3*k+1,-1,p)+3*pow(3*k+2,-1,p))%p
    g3=sum((6*h-1)*pow(18*h**3*A[h],-1,p) for h in range(1,2*m+1))%p
    assert (low0+low1+w2+p**3*g3)%M==orig,(p,'full-fourth-digit')
    return orig,g3

if __name__=='__main__':
    ps=primes_upto(1000)
    for p in ps:
        a,b=check(p)
        if p in (7,13,19,37,73,109,181,373,997):print(p,a,b)
    print('PASS',len(ps),'primes')
