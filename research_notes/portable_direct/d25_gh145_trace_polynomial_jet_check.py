#!/usr/bin/env python3
"""GH145: full finite-field family trace interpolation vs directly evaluated marked first moment."""

def field(p):
    d=next(j for j in range(2,p) if pow(j,(p-1)//2,p)==p-1)
    K=[(a,b) for a in range(p) for b in range(p)]
    zero=(0,0); one=(1,0)
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def sub(x,y):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
    def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def sq(x):return mul(x,x)
    invnorm=[0]+[pow(n,p-2,p) for n in range(1,p)]
    def inv(x):
        n=(x[0]*x[0]-d*x[1]*x[1])%p
        if n==0: raise ZeroDivisionError(x)
        return (x[0]*invnorm[n]%p,(-x[1])*invnorm[n]%p)
    leg=[0]+[-1]*(p-1)
    for a in range(1,p):leg[a*a%p]=1
    def chi(x):return leg[(x[0]*x[0]-d*x[1]*x[1])%p]
    def scalar(x,v):return (v*x[0]%p,v*x[1]%p)
    return K,zero,one,add,sub,mul,sq,inv,chi,scalar

def check(p):
    K,z,one,add,sub,mul,sq,inv,chi,scalar=field(p)
    c=(pow(4,-1,p),0)
    # Build the entire trace-function table without its coefficient polynomial.
    T={}
    for B in K:
        T[B]=sum(chi(mul(x,add(add(sq(x),x),B))) for x in K)
    assert T[z]==-1 and T[c]==-1, (p,T[z],T[c])
    assert all(T[B]==T[sub(c,B)] for B in K)
    failures=[]
    for B in K:
        # Marked first moment by independent finite-field enumeration.
        direct=z
        for x in K:
            f=mul(x,add(add(sq(x),x),B))
            if f!=z:
                direct=add(direct,scalar(mul(x,inv(f)),chi(f)))
        # Full trace-family interpolation: polynomial of degree < q, no Hasse coefficient.
        deriv=z
        for v in K:
            if v!=B:
                deriv=add(deriv,scalar(inv(sub(B,v)),T[v]))
        inferred=scalar(deriv,-2)
        if direct!=inferred:failures.append((B,direct,inferred))
    assert not failures,(p,failures[:3])
    print('PASS_GH145_FIELD','p',p,'q',p*p,'parameter_cases',len(K),'singular_trace',T[z],T[c])

if __name__=='__main__':
    for p in (5,7,11,13,19):check(p)
    print('PASS_GH145_TRACE_POLYNOMIAL_JET_INTERPOLATION')
