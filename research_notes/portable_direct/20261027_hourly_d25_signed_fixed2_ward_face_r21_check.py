#!/usr/bin/env python3
"""Source-labelled six-Hasse finite face at fixed rank weight 2; author finite-ring check."""
ORDER = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]

def uprod(a,b,p,K):
    out=[0]*(K+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=K: out[i+j]=(out[i+j]+x*y)%p
    return out

def series(p):
    m=(p-1)//6
    f=[[1,0,0,0,0]]
    for r in range(p-1):
        v=pow(r+1,-1,p)
        a=[(r-m)*(r-2*m),4*m-3*r,2]
        d=[v*v*pow(3*v,k,p)%p for k in range(5)]
        f.append(uprod(uprod(f[-1],a,p,4),d,p,4))
    return f

def outer(a,b,p):
    return [(a[i]*b[j])%p if i<len(a) and j<len(b) else 0 for i,j in ORDER]

def add(a,b,p):return [(x+y)%p for x,y in zip(a,b)]
def sub(a,b,p):return [(x-y)%p for x,y in zip(a,b)]
def scale(k,a,p):return [(k*x)%p for x in a]

def bmul(a,b,p):
    out=[0]*6
    for k,(i,j) in enumerate(ORDER):
        for l,(s,t) in enumerate(ORDER):
            if i+j+s+t<=2:
                h=ORDER.index((i+s,j+t))
                out[h]=(out[h]+a[k]*b[l])%p
    return out

def edge_faces(p,f):
    m=(p-1)//6;L=1-2*m;N=2*m-1
    def q(r):
        assert r>2*m and f[r][0]==f[r][1]==0
        return f[r][2:5]
    edges={}
    for n in range(L,N+1):
        if n>=0:
            a=outer([2*m*m,4*m,2],q(p-n-1),p)
            bs=uprod([6*m*m,-8*m,2],q(4*m),p,2)
            b=scale(-1,outer(f[2*m-n][:3],bs,p),p)
            edges[n]=add(a,b,p)
        else:
            bs=uprod([20*m*m,-14*m,2],q(p-1),p,2)
            a=outer(f[-n][:3],bs,p)
            at=uprod([0,2*m,-2],f[2*m][:3],p,2)
            b=outer(at,q(p-(2*m+n+1)),p)
            edges[n]=add(a,b,p)
    return edges

def check(p):
    m=(p-1)//6;L=1-2*m;N=2*m-1
    f=series(p);E=edge_faces(p,f)
    U={n:[0]*6 for n in range(L,N+2)}
    V={n:[0]*6 for n in range(L,N+2)}
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j
            pair=outer(f[j][:3],f[p-ell][2:5],p)
            V[n]=add(V[n],pair,p)
            U[n]=add(U[n],scale(j,pair,p),p)
    total=[0]*6;neg=[0]*6;pos=[0]*6;moment=[0]*6
    half=pow(2,-1,p)
    for n in range(L,N+1):
        alpha=[p-2*n,-3,-3,0,0,0]
        beta=[-(p-n)*(p*half-n),0,3*(p-n),0,0,0]
        gamma=[6*m-2*n,-3,-3,0,0,0]
        delta=[-18*m*m+9*m*n-n*n,4*m,14*m-3*n,2,0,-2]
        here=add(bmul(alpha,U[n],p),bmul(beta,V[n],p),p)
        next_=add(bmul(gamma,U[n+1],p),bmul(delta,V[n+1],p),p)
        assert sub(here,next_,p)==E[n],('rank',p,n)
        weighted=scale(pow(2,n,p),E[n],p)
        total=add(total,weighted,p)
        if n<=0:neg=add(neg,weighted,p)
        else:pos=add(pos,weighted,p)
        k=n-1
        g_prev=[6*m-2*k,-3,-3,0,0,0]
        d_prev=[-18*m*m+9*m*k-k*k,4*m,14*m-3*k,2,0,-2]
        a=sub(alpha,scale(half,g_prev,p),p)
        b=sub(beta,scale(half,d_prev,p),p)
        moment=add(moment,scale(pow(2,n,p),add(bmul(a,U[n],p),bmul(b,V[n],p),p),p),p)
        if n==L:
            endpoint=add(bmul(g_prev,U[L],p),bmul(d_prev,V[L],p),p)
            moment=add(moment,scale(pow(2,L-1,p),endpoint,p),p)
    assert moment==total,('telescope',p,moment,total)
    if p==13:
        assert E[-3]==[0,7,0,8,0,0] and E[0]==[8,0,8,10,2,0] and E[1]==[9,7,8,11,0,1]
    a,b,c,d,e,f=total
    signed=(a,(b+c)%p,(d+e+f)%p,(b-c)%p,2*(d-f)%p,2*(d-e+f)%p)
    return neg,pos,total,signed

if __name__=='__main__':
    for p in [7,13,19,31,37,43,733]:
        a,b,c,d=check(p)
        print(p,'lower',a,'upper',b,'full',c,'signed',d)
    print('PASS: authentic six-channel E faces, all rank master identities, exact fixed-2 telescope; 7 primes including 733, mod p')
