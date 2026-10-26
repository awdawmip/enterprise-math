"""Author check of the genuine diagonal Hasse/Ward cancellation and finite-face jet flux."""
from math import isqrt

CH = (((0,2),), ((1,2),(0,3)), ((2,2),(1,3),(0,4)))

def mul(a,b,q,d):
    c=[0]*d
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<d: c[i+j]=(c[i+j]+x*y)%q
    return c

def jets(m,p,q):
    f=[[0]*5 for _ in range(p)]; f[0][0]=1
    half=p*pow(2,-1,q)%q
    for r in range(1,p):
        a,b=r-1-m,r-1-2*m
        c=mul(f[r-1],[a*b,-2*a-b,2],q,5)
        u,v=r*(r-half),-3*r; inv=pow(u,-1,q)
        for k in range(5): f[r][k]=(c[k]-(v*f[r][k-1] if k else 0))*inv%q
    assert f[2*m][0]==0
    assert all(f[r][0]==f[r][1]==0 for r in range(4*m+1,p))
    return f

def face(n,m,p,q,f):
    if n>=0:
        x=mul([2*m*m,4*m,2],f[p-n-1][2:],q,3)
        y=mul([6*m*m,-8*m,2],f[2*m-n][:3],q,3)
        y=mul(y,f[4*m][2:],q,3)
        return [(x[i]-y[i])%q for i in range(3)]
    x=mul([20*m*m,-14*m,2],f[-n][:3],q,3)
    x=mul(x,f[p-1][2:],q,3)
    y=mul([0,2*m,-2],f[2*m][:3],q,3)
    y=mul(y,f[p-(2*m+n+1)][2:],q,3)
    return [(x[i]+y[i])%q for i in range(3)]

def check(p):
    m=(p-1)//6; L=1-2*m; N=2*m-1; q=p**3
    f=jets(m,p,q)
    M={}
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j
            for group in CH:
                for a,b in group:
                    v=f[j][a]*f[p-ell][b]%q
                    for h in (0,1):
                        key=n,a,b,h
                        M[key]=(M.get(key,0)+v*(j if h else 1))%q
    get=lambda n,a,b,h:M.get((n,a,b,h),0)
    inv2=pow(2,-1,q); Y={}; E={}
    for n in range(L,N+2):
        E[n]=face(n,m,p,q,f) if n<=N else [0,0,0]
        for k,g in enumerate(CH):
            Y[n,k]=(sum(get(n,a,b,1) for a,b in g)
                   -(p-n)*inv2*sum(get(n,a,b,0) for a,b in g))%q
    tested=0
    for n in range(L,N+1):
        for k,g in enumerate(CH):
            js=0
            for a,b in g:
                v=(3*get(n,a-1,b,1)-3*get(n+1,a-1,b,1)
                   +4*m*get(n+1,a-1,b,0)+2*get(n+1,a-2,b,0)
                   -3*((p-n)*get(n,a,b-1,0)-get(n,a,b-1,1))
                   +(14*m-3*n)*get(n+1,a,b-1,0)
                   -3*get(n+1,a,b-1,1)-2*get(n+1,a,b-2,0))
                js=(js+v)%q
            prev=(6*(Y[n,k-1]-Y[n+1,k-1]))%q if k else 0
            assert js==prev,(p,n,k,'coupling')
            assert ((p-2*n)*Y[n,k]-(p-2*n-1)*Y[n+1,k]-prev-E[n][k])%q==0,(p,n,k,'Ward')
            tested+=2
    # Independently form true finite-face flux, not from the predicted left boundary.
    tail=[1,0,0]; flux=[0,0,0]
    for n in range(N,L-1,-1):
        inv=pow(p-2*n-1,-1,p)
        dinv=[inv,6*inv*inv%p,36*inv**3%p]
        D=mul(tail,dinv,p,3)
        ef=mul(D,E[n],p,3)
        flux=[(flux[k]+ef[k])%p for k in range(3)]
        tail=mul(D,[p-2*n,-6],p,3)
    U=pow(p-1,-1,p)
    for n in range(L,N+1):
        if n: U=U*(p-2*n)*pow(p-2*n-1,-1,p)%p
    a1=(-2*m*f[2*m][1]*f[p-1][2])%p
    assert Y[L,0]==0 and Y[L,1]%p==a1
    assert a1 and U and tail[:2]==[0,(-6*U)%p]
    assert flux==[0,0,(-6*U*a1)%p] and flux[2]!=0,(p,flux)
    return tested,U,a1,flux[2]

if __name__=='__main__':
    primes=[p for p in range(7,212) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]+[733]
    total=0
    for p in primes:
        tested,U,a1,fl=check(p);total+=tested
        if p in (13,733): print(f'p={p}: U0={U}, Y_left_linear={a1}, finite_face_flux_2={fl} (mod p)')
    assert len(primes)==23
    print(f'PASS {len(primes)} primes; {total} exact J-cancellation + Ward checks; 23 finite-face flux certificates')
