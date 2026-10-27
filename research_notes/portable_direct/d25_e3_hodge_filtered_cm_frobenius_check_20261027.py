#!/usr/bin/env python3
"""Exact finite-ring diagnostic for conditional original E3 Hodge-filtered Frobenius.
Algebraic constructed matrices only; NOT a native H0/B0 benchmark.
"""
def check(p,u,choices=((1,0),(2,1))):
    q=p*p
    def add(a,b): return ((a[0]+b[0])%q,(a[1]+b[1])%q)
    def neg(a): return ((-a[0])%q,(-a[1])%q)
    def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
    def scal(k,a): return ((k*a[0])%q,(k*a[1])%q)
    def sig(a): return (a[0],(-a[1])%q)
    def inv(a):
        N=(a[0]*a[0]-2*a[1]*a[1])%q
        return scal(pow(N,-1,q),sig(a))
    def mm(a,b):
        return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
    def ms(a): return [[sig(x) for x in row] for row in a]
    zero=(0,0);one=(1,0)
    lam=scal(pow(72,-1,q),(4,-1)); lb=sig(lam)
    n=scal(pow(2592,-1,q),(7,0))
    assert mul(lam,lb)==n and (u*u+3)%q==0
    uu=(u%q,0);T=(0,1)
    Theta=[[mul(uu,T),scal(pow(18,-1,q),mul(uu,add(one,scal(-2,T))))],[zero,neg(mul(uu,T))]]
    expected=[[(p%q,0),zero],[zero,(p%q,0)]]
    A0=[[lam,add((p,0),neg(n))],[one,neg(lb)]]
    assert mm(Theta,A0)==mm(A0,ms(Theta))
    assert mm(A0,ms(A0))==expected
    assert A0[1][0][0]%p != 0 # previous valid CM/square model violates Hodge
    for r in choices:
        r=(r[0]%q,r[1]%q)
        z=scal(p,r)
        y=add(inv(sig(r)),neg(scal(p,mul(n,r))))
        A=[[mul(lam,z),y],[z,neg(mul(lb,z))]]
        assert mm(Theta,A)==mm(A,ms(Theta))
        assert mm(A,ms(A))==expected
        assert all(A[i][0][j]%p==0 for i in (0,1) for j in (0,1))
        assert (A[0][1][0]%p,A[0][1][1]%p)!=(0,0)
        print("p",p,"q",q,"r",r,"matrix",A)
    print("PASS_HODGE_FILTERED_CM",p)
for p,root in [(13,0),(19,0),(373,89697)]:
    if root==0:
        root=next(u for u in range(p*p) if (u*u+3)%(p*p)==0)
    check(p,root)
