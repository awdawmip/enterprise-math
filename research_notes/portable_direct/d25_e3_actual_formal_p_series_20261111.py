#!/usr/bin/env python3
"""D25 E3 formal multiplication coefficient [z^p][p]_E3 modulo p^3.

Author-side executable finite certificate; NOT the native H0/B0 divided-power
[X]U benchmark or its Frobenius normalization.
"""
from math import comb
from fractions import Fraction as F

def add(x,y,M):
    return ((x[0]+y[0])%M,(x[1]+y[1])%M)
def mul(x,y,M):
    return ((x[0]*y[0]+2*x[1]*y[1])%M,(x[0]*y[1]+x[1]*y[0])%M)
def scale(x,a,M):
    return (x[0]*a%M,x[1]*a%M)

def h_binomial(p,M):
    a=scale((2,-1),pow(108,-1,M),M); pw=[(1,0)]
    for j in range(1,(p-1)//3+1):pw.append(mul(pw[-1],a,M))
    H=[]
    for n in range(p):
        v=(0,0)
        for j in range(n//3+1):
            v=add(v,scale(pw[j],comb(n-j,j)*comb(n-2*j,j),M),M)
        H.append(v)
    return H

def h_formal(p,M):
    # Original E3: (1-z)w - a*w^2 = z^3, omega=dz/(1-z-2*a*w).
    a=scale((2,-1),pow(108,-1,M),M)
    w=[(0,0)]*p;H=[(0,0)]*p;H[0]=(1,0)
    for n in range(1,p):
        s=(0,0)
        for i in range(3,n-2):s=add(s,mul(w[i],w[n-i],M),M)
        w[n]=add(add(w[n-1],(1,0) if n==3 else (0,0),M),mul(a,s,M),M)
        s=(0,0)
        for i in range(3,n+1):s=add(s,mul(w[i],H[n-i],M),M)
        H[n]=add(H[n-1],scale(mul(a,s,M),2,M),M)
    return H

def evaluate(p):
    assert p>3 and 108%p
    M=p**3
    H=h_binomial(p,M)
    assert H==h_formal(p,M),('formal recurrence disagree',p)
    assert H[:2]==[(1,0),(1,0)]
    S=(0,0)
    for i in range(1,p):
        v=mul(H[i-1],H[p-i-1],p)
        S=add(S,scale(v,pow(i*(p-i)%p,-1,p),p),p)
    C=add(H[-1],scale(S,-p*p*pow(2,-1,M),M),M)
    return {'p':p,'H':H[-1],'S':S,'C':C}

def independent_inverse_composition(p):
    # Exact Q(sqrt(2)) inverse power series of ell(z), only at p=5,7,13.
    N=p;Z=(F(0),F(0));ONE=(F(1),F(0));a=(F(1,54),F(-1,108))
    def qa(x,y):return (x[0]+y[0],x[1]+y[1])
    def qm(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def qs(x,s):return (x[0]*s,x[1]*s)
    pw=[ONE]
    for j in range(1,p//3+1):pw.append(qm(pw[-1],a))
    H=[]
    for n in range(p):
        v=Z
        for j in range(n//3+1):
            v=qa(v,qs(pw[j],comb(n-j,j)*comb(n-2*j,j)))
        H.append(v)
    log=[Z]+[qs(H[n-1],F(1,n)) for n in range(1,N+1)]
    pwlog=[[Z]*(N+1) for _ in range(N+1)];pwlog[0][0]=ONE
    for k in range(1,N+1):
        for n in range(k,N+1):
            v=Z
            for j in range(1,n+1):
                v=qa(v,qm(log[j],pwlog[k-1][n-j]))
            pwlog[k][n]=v
    inverse=[Z]*(N+1);inverse[1]=ONE
    for n in range(2,N+1):
        v=Z
        for k in range(1,n):v=qa(v,qm(inverse[k],pwlog[k][n]))
        inverse[n]=qs(v,-1)
    v=Z
    for k in range(1,N+1):
        v=qa(v,qs(qm(inverse[k],pwlog[k][N]),p**k))
    M=p**3
    def reduce(x):
        assert x.denominator%p!=0
        return x.numerator*pow(x.denominator,-1,M)%M
    got=(reduce(v[0]),reduce(v[1]))
    assert got==evaluate(p)['C'],('independent direct inverse failed',p,got)
    return got

if __name__=='__main__':
    for p in (5,7,13,19,37,43,109,139,157,373):
        x=evaluate(p)
        if p==13:
            assert x=={'p':13,'H':(2054,1469),'S':(10,8),'C':(1209,793)}
        if p==373:
            assert x=={'p':373,
              'H':(46042747,33130606),'S':(46,350),
              'C':(42842780,8783031)}
        print(x)
    for p in (5,7,13):
        print('exact-Q(sqrt2) inverse-composition',p,independent_inverse_composition(p))
    print('PASS: 10 independent E3 H-sequences; 3 direct characteristic-zero p-series compositions.')
