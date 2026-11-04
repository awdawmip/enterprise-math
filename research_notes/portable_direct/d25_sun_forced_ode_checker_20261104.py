#!/usr/bin/env python3
"""Independent Sun defect/Green-operator test. Exact modular integer arithmetic."""
from math import comb, isqrt
import json
def primes(n):
    v=[True]*(n+1);v[0]=v[1]=False
    for x in range(2,isqrt(n)+1):
        if v[x]:
            for j in range(x*x,n+1,x):v[j]=False
    return [i for i in range(5,n+1) if v[i]]
def multiply(a,b,m):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%m
    return z
def derivative(a,p):return [i*a[i]%p for i in range(1,len(a))]
def linear(*terms,p):
    z=[0]*max(map(len,terms))
    for a in terms:
        for i,x in enumerate(a):z[i]=(z[i]+x)%p
    while z and not z[-1]:z.pop()
    return z
def scale(a,k,p):return [k*x%p for x in a]
def test(p,d):
    C=(d-1)*pow(d*d,-1,p)%p
    mod=p**3
    c=[1]
    for k in range(p-1):
        c.append(c[-1]*(d*k+1)*(d*k+d-1)*pow(d*d*(k+1)**2,-1,mod)%mod)
    F2=multiply(c,c,mod)
    H=[0]*(2*p-1)
    for k in range(p):
        h=comb(2*k,k)*c[k]
        for j in range(k+1):
            H[k+j]=(H[k+j]+(-1 if j%2 else 1)*h*comb(k,j))%mod
    defect=[]
    for a,b in zip(F2,H):
        delta=(a-b)%mod
        assert delta%(p*p)==0,(p,d,'Sun divisibility')
        defect.append(delta//(p*p)%p)
    assert not any(defect[:p+1]),(p,d,'support')
    Q=[x*pow(C,-1,p)%p for x in defect[p:]]
    F=[x%p for x in c]
    J=max((i for i,x in enumerate(Q) if x),default=0)
    q=[0]
    for n in range(J):
        f=((2*(n+1)-6*C)*pow(n+1,-1,p)*F[n])%p
        old=q[n-1] if n else 0
        t=f+(2*n+1)*(n*(n+1)+2*C)*q[n]-n*(n*n-1+4*C)*old
        q.append(t*pow(n+1,-3,p)%p)
    assert q==Q[:J+1],(p,d,'recurrence')
    u=[0,1,p-1];v=[1,p-2]
    q1=derivative(Q,p);q2=derivative(q1,p);q3=derivative(q2,p)
    T=linear(multiply(multiply(u,u,p),q3,p),
        scale(multiply(multiply(u,v,p),q2,p),3,p),
        multiply(linear(multiply(v,v,p),scale(u,-2-4*C,p),p=p),q1,p),
        scale(multiply(v,Q,p),-2*C,p),p=p)
    rhs=linear(scale(F,2,p),
        scale(multiply([1,p-1],derivative(F,p),p),-6,p),p=p)
    assert T==rhs,(p,d,'ODE',T,rhs)
    return {'p':p,'d':d,'J':J,'forcing_degree':len(rhs)-1}
if __name__=='__main__':
    cases=[test(p,d) for p in sorted(set(primes(151)+[139,373])) for d in (3,4)]
    print(json.dumps({'checked':len(cases),'failed':0,
        'selected':[t for t in cases if t['p'] in (13,19,139,373)]}))
