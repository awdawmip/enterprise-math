#!/usr/bin/env python3
"""Exact finite-field Gauss parameter 2-jet, Frobenius charge and CM first lifts.

All arithmetic is integer modular. This is an author-side portable regression,
not a native Enterprise Math experiment or formal acceptance.
"""
from math import comb, factorial


def primes_to(N):
    sieve = bytearray(b'\x01') * (N + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, int(N**0.5) + 1):
        if sieve[k]:
            sieve[k*k:N+1:k] = b'\x00' * ((N-k*k)//k+1)
    return [p for p in range(5, N+1) if sieve[p] and p%24 in (13,19)]


def run_model(p, label):
    if label == 'A':
        m=(p-1)//6
        u,v=m,2*m
        c1=pow(6,-1,p); c2=pow(3,-1,p)
        n1,d1=1,6; n2,d2=1,3
        xden,weight=2,12
    else:
        k=(p-3)//8 if p%8==3 else (p-5)//8
        u,v=k,3*k+1
        c1=pow(8,-1,p);c2=3*pow(8,-1,p)%p
        n1,d1=1,8;n2,d2=3,8
        xden=9; weight=16 if p%8==3 else 128*pow(9,-1,p)%p
    assert 0<u<v<p-1
    q=[0]*p; f=[0]*p; s=[0]*p
    q[0]=1
    c12=c1*c2%p
    for n in range(1,p):
        r=n-1
        A=(r-u)*(r-v)%p
        K=(c1*(r-v)+c2*(r-u))%p
        inv=pow(n*n,-1,p)
        q[n]=A*q[n-1]*inv%p
        f[n]=(A*f[n-1]+K*q[n-1])*inv%p
        s[n]=(A*s[n-1]+K*f[n-1]+c12*q[n-1])*inv%p
    assert all(q[n]==comb(u,n)*comb(v,n)%p for n in range(u+1))
    assert all(t==0 for t in q[u+1:])
    assert all(t==0 for t in f[v+1:])
    invbin=pow(comb(v,u),-1,p)
    lower=(-1)**(u+v)*c12*invbin%p
    fac=[1]*p
    for n in range(1,p):fac[n]=fac[n-1]*n%p
    invfac=[1]*p
    invfac[-1]=pow(fac[-1],-1,p)
    for n in range(p-1,0,-1):invfac[n-1]=invfac[n]*n%p
    for n in range(v+1,p):
        fact = (c12 * (-1)**(u+v) * fac[u]*fac[v]*fac[n-u-1]*fac[n-v-1]
                *invfac[n]*invfac[n])%p
        assert s[n]==fact,(p,label,n,'factorial high tail')
    R=[0]*(v+1)+s[v+1:]
    for n in range(0,p+1):
        # coeff of z^n in L0 y, zK y and c1*c2*zQ, including z^p.
        def L0(y):
            return (n*n*(y[n] if n<p else 0)
                    - ((n-1-u)*(n-1-v)*y[n-1] if n>0 else 0))%p
        zKf=((c1*(n-1-v)+c2*(n-1-u))*f[n-1] if 0<n<=p else 0)%p
        zKq=((c1*(n-1-v)+c2*(n-1-u))*q[n-1] if 0<n<=p else 0)%p
        zq=(q[n-1] if 0<n<=p else 0)
        assert L0(q)==0,(p,label,n,'Q')
        assert L0(f)==zKq,(p,label,n,'first-jet ODE')
        assert L0(s)==(zKf+c12*zq-(c12 if n==p else 0))%p,(p,label,n,'second-jet ODE')
        assert L0(R)==(lower if n==v+1 else (-c12 if n==p else 0))%p,(p,label,n,'two boundary law')
    # Clear the rational denominator in the exact Wronskian/Green identity.
    if p <= 67:
        def poly_mul(a,b):
            r=[0]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                if x:
                    for j,y in enumerate(b):
                        r[i+j]=(r[i+j]+x*y)%p
            return r
        def deriv(a):return [(i*a[i])%p for i in range(1,len(a))]
        def pad(a,n):return a+[0]*(n-len(a))
        Q=q[:u+1];P=f[:v+1]
        U=poly_mul(Q,deriv(P));V=poly_mul(deriv(Q),P)
        N=max(len(U),len(V))
        W=[(a-b)%p for a,b in zip(pad(U,N),pad(V,N))]
        lhs=[0]*(len(W)+1)
        for i,wi in enumerate(W):
            lhs[i]=(lhs[i]+(i+1)*wi)%p
            lhs[i+1]=(lhs[i+1]+(u+v-i-1)*wi)%p
        KQ=[(-(c1*v+c2*u)*Q[0])%p]+[
            ((c1+c2)*i-(c1*v+c2*u))*Q[i]%p for i in range(1,len(Q))]
        rhs=poly_mul(Q,KQ)
        M=max(len(lhs),len(rhs))
        assert pad(lhs,M)==pad(rhs,M),(p,label,'Wronskian flux')
    # Independent p^2 recurrence on exact Gauss parameters at h=p.
    modulus=p*p
    a=(-u+n1*p*pow(d1,-1,modulus))%modulus
    b=(-v+n2*p*pow(d2,-1,modulus))%modulus
    g=1; xp=1; z=pow(xden,-1,modulus)
    G=1
    for n in range(1,p):
        g=g*(a+n-1)*(b+n-1)*pow(n*n,-1,modulus)%modulus
        xp=xp*z%modulus
        G=(G+g*xp)%modulus
        qn=comb(u,n)*comb(v,n) if n<=u else 0
        assert (g-qn)%modulus==(p*f[n])%modulus,(p,label,n,'Gauss lift')
    Q=sum(comb(u,n)*comb(v,n)*pow(z,n,modulus) for n in range(u+1))%modulus
    assert Q%p==0,(p,label,'CM zero')
    x=pow(xden,-1,p)
    fp=0; J=0;xp=1
    for n in range(p):
        fp=(fp+f[n]*xp)%p
        J=(J+n*q[n]*xp)%p
        xp=xp*x%p
    gjet=(Q//p+fp)%p
    assert G//p%p==gjet,(p,label,'p-adic Gauss zero-jet')
    unit=weight*J*gjet%p
    assert unit==1,(p,label,'first-digit unit evidence')
    return (Q//p%p,fp,J,gjet,lower,(-c12)%p)


def main():
    P=primes_to(2500)
    assert len(P)==94
    samples={}
    for p in P:
        a=run_model(p,'A')
        b=run_model(p,'B')
        if p in (13,19,43,67,373,997): samples[p]={'A':a,'B':b}
    print('PASS:',len(P),'target primes x 2 source models, p<2500; all coefficient and differential boundary checks')
    print('Tuple = (Q(x)/p, parameter P(x), DQ(x), Gauss G(x)/p, lower boundary, top charge) mod p')
    for p,t in samples.items():print(p,t)

if __name__=='__main__': main()
