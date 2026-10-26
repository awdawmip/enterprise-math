#!/usr/bin/env python3
"""Author-only exact check of lower-oriented corrected-Clausen Ward adjoint.

Arithmetic: Fraction throughout; modular reductions only for p-local denominators.
No native CM or formal project authority is asserted.
"""
from fractions import Fraction as Q

CHANNELS = ((0,2),(1,2),(0,3))

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

def jets(m, max_order=3):
    p=6*m+1
    u=[[Q(0) for _ in range(p)] for _ in range(max_order+1)]
    u[0][0]=Q(1)
    for a in range(max_order+1):
        for r in range(1,p):
            take=lambda b,s: u[b][s] if b>=0 and s>=0 else Q(0)
            u[a][r]=((r-1-m)*(r-1-2*m)*take(a,r-1)
                +3*r*take(a-1,r)
                -(3*(r-1)-4*m)*take(a-1,r-1)
                +2*take(a-2,r-1))/(r*(Q(r)-Q(p,2)))
    return u

def scalar(u,a,r):
    return u[a][r] if a>=0 and 0<=r<len(u[0]) else Q(0)

def moments(m,u,a,b,n,s=0):
    p=6*m+1
    acc=Q(0)
    for j in range(1,2*m+1):
        ell=j+n
        if 1<=ell<=2*m:
            acc+= j**s * scalar(u,a,j)*scalar(u,b,p-ell)
    return acc

def source(m,u,a,b,n):
    p=6*m+1
    M=lambda aa,bb,nn,ss=0: moments(m,u,aa,bb,nn,ss)
    J=(3*M(a-1,b,n,1)-3*M(a-1,b,n+1,1)
       +4*m*M(a-1,b,n+1)+2*M(a-2,b,n+1)
       -3*((p-n)*M(a,b-1,n)-M(a,b-1,n,1))
       +(14*m-3*n)*M(a,b-1,n+1)
       -3*M(a,b-1,n+1,1)-2*M(a,b-2,n+1))
    if n>=0:
        E=((2*m*m*(a==0)+4*m*(a==1)+2*(a==2))*scalar(u,b,p-n-1)
         +scalar(u,a,2*m-n)*(-6*m*m*scalar(u,b,4*m)
         +8*m*scalar(u,b-1,4*m)-2*scalar(u,b-2,4*m)))
    else:
        E=(scalar(u,a,-n)*(20*m*m*scalar(u,b,p-1)
         -14*m*scalar(u,b-1,p-1)+2*scalar(u,b-2,p-1))
         +scalar(u,b,p-(2*m+n+1))*(2*m*scalar(u,a-1,2*m)-2*scalar(u,a-2,2*m)))
    return J+E

def p_mod(x,p,exp=2):
    q=p**exp
    return (x.numerator % q)*pow(x.denominator%q,-1,q)%q

def test(m):
    p=6*m+1
    if not is_prime(p):
        return None
    L=1-2*m
    u=jets(m)
    w=lambda n: Q(2)**n
    lam={0:Q(0)}
    for k in range(0,L,-1):
        lam[k-1]=((p-2*k)*lam[k]-w(k))/Q(p-2*k+1)
    delta=w(L)-(p-2*L)*lam[L]
    records=[]
    checks=0
    for a,b in CHANNELS:
        Y=lambda n: moments(m,u,a,b,n,1)-Q(p-n,2)*moments(m,u,a,b,n)
        for n in range(L,2*m):
            assert (p-2*n)*Y(n)-(p-2*n-1)*Y(n+1)==source(m,u,a,b,n), (m,a,b,n,'WARD')
            checks+=1
        U=sum((w(n)*moments(m,u,a,b,n) for n in range(L,1)),Q(0))
        T=sum((w(n)*(1-6*n)*moments(m,u,a,b,n) for n in range(L,1)),Q(0))
        K=sum((w(n)*moments(m,u,a,b,n,1) for n in range(L,1)),Q(0))
        R=sum((w(n)*Y(n) for n in range(L,1)),Q(0))
        dual=sum((lam[n]*source(m,u,a,b,n) for n in range(L,0)),Q(0))+delta*Y(L)
        assert R==dual,(m,a,b,'ADJOINT',R,dual)
        assert T==(1-6*p)*U+12*K-12*dual, (m,a,b,'T decomposition')
        checks+=2
        records.append({'channel':(a,b),'U':p_mod(U,p),'T':p_mod(T,p),'K':p_mod(K,p),
             'R':p_mod(R,p),'source_adj':p_mod(dual-delta*Y(L),p),'edge_adj':p_mod(delta*Y(L),p),
             'delta':p_mod(delta,p)})
    return p, checks, records

def main():
    total=0
    for m in range(1,13):
        r=test(m)
        if r is None: continue
        p,k,records=r
        total+=k
        print('p=',p,'m=',m,'PASS=',k,'values=',records if p==13 else '<checked>')
    print('ALL EXACT ASSERTIONS PASS=',total)

if __name__=='__main__':
    main()
