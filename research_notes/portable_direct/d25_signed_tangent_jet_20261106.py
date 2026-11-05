"""D25 q-adic Lucas B-port as a four-parameter finite-field jet.
Exact modular check against independent signed harmonic/carry formula.
No native H0/B0 execution or mathematical admission is claimed.
"""
from math import comb, isqrt, prod

def primes(bound):
    return [p for p in range(5, bound + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]

def diagonal_data(p):
    N,r=divmod((p*p-1)//6,p)
    return [(i*r)%p for i in (2,3,4)]

def tangent_jet(p,s):
    a=-pow(2,-1,p)%p
    u=1
    dx=[0,0,0]
    da=0
    Z=L=Da=0
    D=[0,0,0]
    for j in range(p):
        w=(6*j+1)%p
        Z=(Z+u)%p
        L=(L+w*u)%p
        D=[(D[i]+w*dx[i])%p for i in range(3)]
        Da=(Da+w*da)%p
        if j==p-1:
            break
        t=[(x-j)%p for x in s]
        base=a*pow(j+1,-3,p)%p
        c=base*prod(t)%p
        ndx=[(c*dx[i]+base*u*prod(t[k] for k in range(3) if k!=i))%p
              for i in range(3)]
        nda=c*(da-u*pow(j+1,-1,p))%p
        u,dx,da=c*u%p,ndx,nda
    return Z,L,D,Da

def old_signed_carry(p,s):
    a=-pow(2,-1,p)%p
    J=min(s)
    u=[pow(a,j,p)*prod(comb(x,j) for x in s)%p for j in range(J+1)]
    Z=sum(u)%p
    L=sum((6*j+1)*u[j] for j in range(J+1))%p
    H=[0]*p
    fac=[1]*p
    for j in range(1,p):
        H[j]=(H[j-1]+pow(j,-1,p))%p
        fac[j]=fac[j-1]*j%p
    U=[];V=[];K=[]
    for i,x in enumerate(s):
        U.append(sum((6*j+1)*u[j]*(H[x]-H[x-j])
                     for j in range(J+1))%p)
        V.append(sum((6*j+1)*u[j]*(H[x-j]-H[j])
                     for j in range(J+1))%p)
        second=min(s[t] for t in range(3) if t!=i)
        K.append(sum((6*j+1)*pow(a,j,p) *
                     (-1 if (j-x)%2==0 else 1) *
                     fac[x]*fac[j-x-1]*pow(fac[j],-1,p) *
                     prod(comb(s[t],j) for t in range(3) if t!=i)
                     for j in range(x+1,second+1))%p)
    phi=(pow(2,p-1,p*p)-1)//p
    B=(6*Z-phi*L+sum(V[i]-K[i] for i in range(3)))%p
    return Z,L,B,U,K,H,phi

def original_W(p):
    m=p*p
    term=total=1
    for k in range(1,p):
        term=term*(2*k-1)*(3*k-2)*(3*k-1)*pow(36*k**3,-1,m)%m
        total=(total+(6*k+1)*term)%m
    return total

def test(bound=1200):
    ps=primes(bound)
    selected=(5,7,11,13,19,37,373)
    for p in ps:
        s=diagonal_data(p)
        Z,L,D,Da=tangent_jet(p,s)
        zr,lr,B,U,K,H,phi=old_signed_carry(p,s)
        assert (Z,L)==(zr,lr),('Z,L',p)
        assert all(D[i]==(U[i]+K[i])%p for i in range(3)),('channels',p)
        Bj=(6*Z+(sum(H[x] for x in s)-phi)*L-sum(D)+3*Da)%p
        assert Bj==B,('B jet',p,Bj,B)
        if L==0:
            W=original_W(p)
            assert W%p==0,('W first digit',p)
            Theta=(W//p-Z+(sum(D)-3*Da)*pow(6,-1,p))%p
            assert Theta==0,('finite observation Theta',p,Theta)
        if p in selected:
            print('q',p,'s',s,'Z',Z,'L',L,'B',Bj,
                  'Dx',D,'Dalpha',Da,'W/q',original_W(p)//p)
    print('PASS',len(ps),'prime-field cases, independent jets/carries and finite Theta check')

if __name__=='__main__':
    test()
