#!/usr/bin/env python3
"""Exact original-E3 conjugate 2-isogeny certificate (all u at p=13,19,373)."""
from fractions import Fraction as F
import json

def P(a=0,b=0): return F(a),F(b)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def sub(x,y): return add(x,neg(y))
def mul(x,y): return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def sc(x,c): return x[0]*c,x[1]*c
def inv(x):
    n=x[0]**2-2*x[1]**2
    if n==0: raise ZeroDivisionError
    return x[0]/n,-x[1]/n
def div(x,y): return mul(x,inv(y))
def sq(x): return mul(x,x)
def sig(x): return x[0],-x[1]

T=P(0,1); one=P(1)
c=sc(sub(P(2),T),F(1,108))
e=sc(sub(sc(T,2),P(3)),F(1,36))
a=add(sc(e,3),P(F(1,4)))
b=add(add(sc(sq(e),3),sc(e,F(1,2))),sc(c,F(1,2)))
assert a==sc(T,F(1,6)) and b==sc(sub(P(3),sc(T,2)),F(1,432))
aq=sc(a,-2); bq=sub(sq(a),sc(b,4))
assert sc(aq,F(1,2))==sig(a) and sc(bq,F(1,4))==sig(b)
assert mul(T,sig(T))==P(-2)
for i in range(1,41):
    u=P(i); Q=add(add(sq(u),mul(a,u)),b)
    U=div(Q,u); us=sc(U,F(1,2))
    u2=sc(add(add(us,sig(a)),div(sig(b),us)),F(1,2))
    double=div(sq(sub(sq(u),b)),sc(mul(u,Q),4))
    assert u2==double
    z2=mul(u,Q); Z2=mul(z2,sq(sub(one,div(b,sq(u)))))
    assert Z2==add(add(mul(sq(U),U),mul(aq,sq(U))),mul(bq,U))
    us2=sc(Z2,F(1,8))
    assert us2==add(add(mul(sq(us),us),mul(sig(a),sq(us))),mul(sig(b),us))
def check(p):
    assert p%24 in (13,19) and pow(2,(p-1)//2,p)==p-1
    def cv(x):return tuple(int(z.numerator*pow(z.denominator,-1,p))%p for z in x)
    def fm(x,y):return (x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p
    def fa(x,y):return (x[0]+y[0])%p,(x[1]+y[1])%p
    def fs(x,y):return (x[0]-y[0])%p,(x[1]-y[1])%p
    def scale(x,k):return x[0]*k%p,x[1]*k%p
    def fi(x):
        n=(x[0]*x[0]-2*x[1]*x[1])%p
        if n==0:raise ZeroDivisionError
        d=pow(n,-1,p);return x[0]*d%p,-x[1]*d%p
    af,bf,aqf,bqf,asf,bsf=map(cv,(a,b,aq,bq,sig(a),sig(b)))
    assert scale(aqf,pow(2,-1,p))==asf
    assert scale(bqf,pow(4,-1,p))==bsf
    valid=0
    for u0 in range(p):
      for u1 in range(p):
        u=(u0,u1);u2=fm(u,u); Q=fa(fa(u2,fm(af,u)),bf)
        left=fm(fs(u2,bf),fs(u2,bf))
        right=fa(fa(fm(Q,Q),fm(fm(aqf,u),Q)),fm(bqf,u2))
        assert left==right,(p,u,left,right)
        if valid<128 and u!=(0,0) and Q!=(0,0):
            U=fm(Q,fi(u));us=scale(U,pow(2,-1,p))
            back=scale(fa(fa(us,asf),fm(bsf,fi(us))),pow(2,-1,p))
            twice=fm(left,fi(scale(fm(u,Q),4)))
            assert back==twice,(p,u,back,twice)
            valid+=1
    assert valid==128
    return {"p":p,"all_field_u_verified":p*p,"nonpole_compositions_verified":valid,
            "coefficient_frobenius":"T->-T"}
if __name__=="__main__":
    print(json.dumps({"curve":"E3:y²+xy+((2-T)/108)y=x³",
        "isogeny_pullback":"Phi*omega_sigma=T omega",
        "isogeny_composition":"Phi_sigma o Phi=[-2]",
        "rational_chart_checks":40,
        "fields":[check(p) for p in (13,19,373)],
        "p373_from_prior_geometric_Frob":"+373 -> A_373²=[-746]"},
        indent=2,ensure_ascii=False))
