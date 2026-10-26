#!/usr/bin/env python3
"""Exact author checks: global Ward adjoint, exceptional integral gluing, full Hasse jets."""
from fractions import Fraction as F
from math import factorial

CHANNELS=((0,2),(1,2),(0,3),(2,2),(1,3),(0,4))
HIGH=((2,2),(1,3),(0,4))

def prime(n):
    return n>1 and all(n%d for d in range(2,int(n**.5)+1))

def exact_small(p):
    m=(p-1)//6; L=1-2*m; N=2*m-1
    w=lambda n:F(2)**n
    lam={0:F(0)}
    for n in range(0,L,-1):
        lam[n-1]=((p-2*n)*lam[n]-w(n))/(p-2*n+1)
    delta=w(L)-(p-2*L)*lam[L]
    kappa=F(p+1,p-2*L)
    for n in range(L+1,0):kappa*=F(p-2*n+1,p-2*n)
    a={L-1:F(0)}
    for n in range(L,N+1):a[n]=(w(n)+(p-2*n+1)*a[n-1])/(p-2*n)
    assert a[0]==kappa*delta/p
    mu={0:F(0)}
    for n in range(1,N+1):mu[n]=(w(n)+(p-2*n+1)*mu[n-1])/(p-2*n)
    h=F(1)
    for n in range(1,N+1):
        h*=F(p-2*n+1,p-2*n)
        assert a[n]==mu[n]+a[0]*h
    assert a[-1]-lam[-1]==a[0]*p/(p+1)
    y={n:F((n-L+1)**2+2,n-L+2) for n in range(L,N+1)}
    y[N+1]=F(0)
    s={n:(p-2*n)*y[n]-(p-2*n-1)*y[n+1] for n in range(L,N+1)}
    lhs=sum(w(n)*y[n] for n in range(L,N+1))
    assert lhs==sum(a[n]*s[n] for n in range(L,N+1))
    split=(sum(lam[n]*s[n] for n in range(L,0)) +delta*y[L]
           +sum(mu[n]*s[n] for n in range(1,N+1)))
    assert lhs==split
    return delta,a[0]

def boundary(p,precision):
    m=(p-1)//6;L=1-2*m
    big=p**(precision+1); mod=p**precision
    lam=0
    for n in range(0,L,-1):
        lam=((p-2*n)*lam-pow(2,n,big))*pow(p-2*n+1,-1,big)%big
    delta=(pow(2,L,big)-(p-2*L)*lam)%big
    kap=(p+1)*pow(p-2*L,-1,mod)%mod
    for n in range(L+1,0):kap=kap*(p-2*n+1)*pow(p-2*n,-1,mod)%mod
    return delta,kap

def resonant_adjoint(p,precision=3):
    m=(p-1)//6;L=1-2*m;N=2*m-1;mod=p**precision
    d,k=boundary(p,precision)
    assert d%p==0
    zero=(k*(d//p))%mod
    a={L-1:0}
    for n in range(L,0):
        a[n]=(pow(2,n,mod)+(p-2*n+1)*a[n-1])*pow(p-2*n,-1,mod)%mod
    assert (p*zero-1-(p+1)*a[-1])%mod==0
    a[0]=zero
    for n in range(1,N+1):
        a[n]=(pow(2,n,mod)+(p-2*n+1)*a[n-1])*pow(p-2*n,-1,mod)%mod
    return a,d,k

def p733_hasse():
    p=733;m=(p-1)//6;L=1-2*m;N=2*m-1;mod=p**3
    adj,delta,kap=resonant_adjoint(p,3)
    assert delta%(p*p)==p*241 and kap%p==20 and adj[0]%p==422
    jets=[[0]*p for _ in range(5)];jets[0][0]=1
    i2=pow(2,-1,mod)
    for n in range(1,p):
        v=pow(n*(n-p*i2),-1,mod)
        for a in range(5):
            t=(n-1-m)*(n-1-2*m)*jets[a][n-1]
            if a>=1:t+=3*n*jets[a-1][n]-(3*(n-1)-4*m)*jets[a-1][n-1]
            if a>=2:t+=2*jets[a-2][n-1]
            jets[a][n]=t*v%mod
    width=N-L+1
    mom0={ch:[0]*width for ch in CHANNELS};mom1={ch:[0]*width for ch in CHANNELS}
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j;idx=n-L
            for a,b in CHANNELS:
                ch=(a,b);z=jets[a][j]*jets[b][p-ell]%mod
                mom0[ch][idx]=(mom0[ch][idx]+z)%mod
                mom1[ch][idx]=(mom1[ch][idx]+j*z)%mod
    A={};D={};X={};W={}
    for ch in CHANNELS:
        y={n:(mom1[ch][n-L]-(p-n)*i2*mom0[ch][n-L])%mod for n in range(L,N+1)}
        y[N+1]=0
        s={n:((p-2*n)*y[n]-(p-2*n-1)*y[n+1])%mod for n in range(L,N+1)}
        if ch==(1,2):
            assert y[L]%p==610
            face_unit=(2*(delta//p)*y[L])%p
            bridged=(2*adj[0]*pow(kap,-1,p)*y[L])%p
            assert face_unit==bridged==87
        W[ch]=sum(pow(2,n,mod)*y[n] for n in range(L,N+1))%mod
        source=sum(adj[n]*s[n] for n in range(L,N+1))%mod
        assert W[ch]==source,(ch,'full source')
        A[ch]=sum(pow(2,n,mod)*mom0[ch][n-L] for n in range(L,N+1))%mod
        D[ch]=sum(pow(2,n,mod)*mom1[ch][n-L] for n in range(L,N+1))%mod
        X[ch]=sum(pow(2,n,mod)*(1-6*n)*mom0[ch][n-L] for n in range(L,N+1))%mod
        assert X[ch]==((1-6*p)*A[ch]+12*(D[ch]-source))%mod,(ch,'global Ward scalar')
    i6=pow(6,-1,mod);i36=pow(36,-1,mod);i3=pow(3,-1,mod)
    E=(X[(0,2)]+p*(6*A[(0,2)]-(X[(1,2)]+X[(0,3)])*i6)
       +p*p*(sum(X[ch] for ch in HIGH)*i36-A[(1,2)]-A[(0,3)]))%mod
    src=(A[(0,2)]+12*(D[(0,2)]-W[(0,2)])
        -p*i6*(A[(1,2)]+A[(0,3)])
        -2*p*(D[(1,2)]-W[(1,2)]+D[(0,3)]-W[(0,3)])
        +p*p*i36*sum(A[ch] for ch in HIGH)
        +p*p*i3*sum(D[ch]-W[ch] for ch in HIGH))%mod
    assert E==src
    gamma=pow(2,-p,mod)*pow(18,-1,mod)%mod
    assert gamma*E%mod==233027780,(gamma*E%mod, E)
    return {'delta_mod_p2':delta%(p*p),'gluing_unit_mod_p':kap%p,
            'rank_zero_adjoint_mod_p':adj[0]%p,'channel_sources_checked':len(CHANNELS),
            'E3_mod_p3':E,'normalized_endpoint':gamma*E%mod}

def main():
    small={p:exact_small(p) for p in (7,13,19,31)}
    assert small[13][0]==F(4337,2016)
    assert small[13][1]==F(8674,62985)
    primes=[p for p in range(7,998) if p%6==1 and prime(p)]
    resonance=[]
    for p in primes:
        d,k=boundary(p,2)
        if d%p==0:resonance.append((p,d%(p*p),k%p))
    assert len(primes)==80 and resonance==[(733,176653,20)]
    actual=p733_hasse()
    print('PASS: exact Q-adjoints for p=7,13,19,31; 80-prime resonance scan; 733 six-channel Hasse mod p^3.')
    print('p=13 delta=',small[13][0],'; alpha0=',small[13][1])
    print('resonance<=997:',resonance)
    print('p=733',actual)

if __name__=='__main__':main()
