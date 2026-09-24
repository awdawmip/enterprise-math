#!/usr/bin/env python3
"""Deterministic regression for d25_gauss_manin_representative_gauge_20260924.md. Regression only; not an all-prime proof."""
from math import comb

class Q2:
    __slots__=("a","b","m")
    def __init__(self,a=0,b=0,m=1): self.m=m; self.a=a%m; self.b=b%m
    def _co(self,x): return x if isinstance(x,Q2) else Q2(x,0,self.m)
    def __add__(self,x): x=self._co(x); return Q2(self.a+x.a,self.b+x.b,self.m)
    __radd__=__add__
    def __sub__(self,x): x=self._co(x); return Q2(self.a-x.a,self.b-x.b,self.m)
    def __rsub__(self,x): return Q2(x,0,self.m)-self
    def __neg__(self): return Q2(-self.a,-self.b,self.m)
    def __mul__(self,x):
        x=self._co(x); return Q2(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a,self.m)
    __rmul__=__mul__
    def div_scalar(self,d):
        u=pow(d,-1,self.m); return Q2(self.a*u,self.b*u,self.m)
    def inv(self):
        n=(self.a*self.a-2*self.b*self.b)%self.m; u=pow(n,-1,self.m)
        return Q2(self.a*u,-self.b*u,self.m)
    def __pow__(self,n):
        r=Q2(1,0,self.m); x=self
        while n:
            if n&1: r=r*x
            x=x*x; n//=2
        return r
    def tup(self): return self.a,self.b

def prime_list(n):
    a=[True]*(n+1); a[0]=a[1]=False
    for q in range(2,int(n**0.5)+1):
        if a[q]: a[q*q:n+1:q]=[False]*(((n-q*q)//q)+1)
    return [q for q,v in enumerate(a) if v]

def formal_H(p):
    M=p*p; s=Q2(0,1,M); t=(Q2(2,0,M)-s).div_scalar(4)
    H=Q2(0,0,M); Ht=Q2(0,0,M); n=(p-1)//3
    for j in range(n+1):
        c=comb(p-1-j,j)*comb(p-1-2*j,p-1-3*j)
        c=(c*pow(pow(27,j,M),-1,M))%M
        H=H+c*(t**j)
        if j: Ht=Ht+(j*c)*(t**(j-1))
    return H,Ht,t

def truncated_F(p,t):
    M=p*p; F=Q2(0,0,M); Ft=Q2(0,0,M); coeff=1
    for k in range(p):
        if k:
            j=k-1
            coeff=(coeff*(3*j+1)*(3*j+2))%M
            coeff=(coeff*pow(9*k*k,-1,M))%M
        F=F+coeff*(t**k)
        if k: Ft=Ft+(k*coeff)*(t**(k-1))
    return F,Ft

def divide_by_p(x,p):
    assert x.m==p*p and x.a%p==0 and x.b%p==0
    return Q2(x.a//p,x.b//p,p)

def run_one(p):
    H,Ht,t=formal_H(p); F,Ft=truncated_F(p,t)
    assert H.a%p==H.b%p==0 and F.a%p==F.b%p==0
    alpha=divide_by_p(H,p); beta=divide_by_p(F,p); sp=Q2(0,1,p)
    Jxi=(sp*Q2(Ht.a,Ht.b,p)).div_scalar(4)
    JF=(sp*Q2(Ft.a,Ft.b,p)).div_scalar(4)
    assert Jxi.tup()==JF.tup()
    assert (6*beta*JF).tup()==(1,0)
    C=beta-alpha
    assert (6*alpha*Jxi+6*C*JF).tup()==(1,0)
    witness=2*sp-1
    assert (6*alpha*Jxi).tup()==witness.tup()
    q=alpha*Jxi; c0=q.inv(); assert (c0*q).tup()==(1,0)
    eta=Q2((p+3)//4,7,p)
    predicted=c0*alpha*eta
    assert predicted.tup()==(c0*alpha*eta).tup()
    return witness.tup()

def main():
    targets=[p for p in prime_list(4999) if p%24 in (13,19)]
    assert len(targets)==166
    samples={}
    for p in targets:
        w=run_one(p)
        if len(samples)<8: samples[p]=w
    print("target_primes",len(targets))
    print("class13",sum(p%24==13 for p in targets),"class19",sum(p%24==19 for p in targets))
    print("failures",0)
    print("finite_witness: 6*alpha*Jxi == 2*s-1 for all checked targets")
    print("sample_witness_pairs",samples)
    print("REGRESSION_ONLY_NOT_ALL_PRIME_PROOF")

if __name__=="__main__": main()
