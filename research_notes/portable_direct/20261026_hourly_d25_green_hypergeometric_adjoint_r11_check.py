"""Author finite-ring check for a portable D25 Clausen rank-kernel theorem.
Only finite coefficient/port equivalence modulo p is checked, not CM/LIFT.
"""
from math import factorial


def primes(n):
    ps=[]
    for p in range(7,n+1):
        if p%6!=1:
            continue
        if all(p%d for d in range(2,int(p**0.5)+1)):
            ps.append(p)
    return ps


def check(p):
    m=(p-1)//6
    f=[factorial(j)%p for j in range(4*m+1)]
    def inv(n):
        return pow(n%p,-1,p)
    def frac(num,den):
        return num*inv(den)%p
    h=[0]*(2*m+1)
    a=[0]*(2*m+1)
    h[1]=frac(2,(m+1)*(2*m+1))
    for j in range(1,2*m):
        h[j+1]=frac(h[j]*j*j,(j+m+1)*(j+2*m+1))
    for j in range(1,2*m+1):
        hfac=frac(2*f[m]*f[2*m]*f[j-1]**2,f[j+m]*f[j+2*m])
        assert h[j]==hfac,(p,j,'h_factorial')
    for j in range(m+1,2*m+1):
        a[j]=frac((-1)**(m+j+1)*f[m]*f[j-m-1]*f[2*m],f[2*m-j]*f[j]**2)
    g=[0]+[(pow(2,j,p)*h[j])%p for j in range(1,2*m+1)]
    k_direct=[0]*(2*m+1)
    k_green=[0]*(2*m+1)
    k_green[1]=g[1]
    for j in range(1,2*m+1):
        k_direct[j]=sum((6*(j-l)+1)*g[l] for l in range(1,j+1))%p
        if j>=2:
            k_green[j]=(2*k_green[j-1]-k_green[j-2]+g[j]+5*g[j-1])%p
        assert k_direct[j]==k_green[j],(p,j,'green')
        if j>=2:
            lhs=(j-1)*(j+m)*(j+2*m)*g[j]-2*(j-1)**3*g[j-1]
            assert lhs%p==0,(p,j,'3F2_operator')
    L,U=m+1,2*m
    v=[0]*(U+3)
    for j in range(L,U+1):
        v[j]=a[j]*inv(pow(2,j,p))%p
    q=[0]*(U+3)
    for ell in range(U,0,-1):
        q[ell]=(2*q[ell+1]-q[ell+2]+v[ell]+5*v[ell+1])%p
        direct_q=sum((6*(j-ell)+1)*v[j] for j in range(max(L,ell),U+1))%p
        assert q[ell]==direct_q,(p,ell,'adjoint-green')
    b=[0]*(U+2)
    for j in range(L,U+1):
        b[j]=j*j*v[j]%p
        if j<U:
            ratio=frac((j-m)*(j-2*m),2*(j+1)**2)
            assert v[j+1]==v[j]*ratio%p,(p,j,'outer-ratio')
    wsum=sum((j*j+3*m*j-2*m*m)*v[j] for j in range(L,U+1))%p
    assert wsum==(2*b[L])%p,(p,'outer-telescope')
    mixed=sum((j*j+3*m*j-2*m*m)*v[j]*k_green[j] for j in range(L,U+1))%p
    boundary=2*b[L]*k_green[L]%p
    residual=2*sum(b[j]*(k_green[j]-k_green[j-1]) for j in range(L+1,U+1))%p
    assert mixed==(boundary+residual)%p,(p,'weighted-abel')
    s_direct=0
    s_green=0
    for j in range(m+1,2*m+1):
        v=a[j]*inv(pow(2,j,p))%p
        inner=sum((6*(j-l)+1)*g[l] for l in range(1,j+1))%p
        s_direct+=v*inner
        s_green+=v*k_green[j]
    s_direct=(-s_direct*inv(216))%p
    s_green=(-s_green*inv(216))%p
    assert s_direct==s_green,(p,'outer')
    assert s_green==(-inv(216)*sum(g[j]*q[j] for j in range(1,U+1)))%p,(p,'adjoint-sum')
    return s_green, residual

if __name__=='__main__':
    ps=primes(997)
    out={p:check(p) for p in ps}
    assert [out[p][0] for p in (7,13,19,31)]==[4,2,2,9],out
    print('PASS',len(ps),'primes', 'max_p=',max(ps))
    print({p:out[p] for p in (7,13,19,31,37,43,61,73,373,997) if p in out})
