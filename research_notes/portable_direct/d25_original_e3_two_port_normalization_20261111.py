#!/usr/bin/env python3
"""Original E3 fixed-z two-port common-unit obstruction and triangular repair.
Exact arithmetic in (Z/p^2)[T]/(T^2-2). AUTHOR_SIDE/UNREVIEWED/NOT_NATIVE_H0B0.
"""
from math import comb
PRIMES=(13,19,37,43,109,139,157,373)
def add(x,y,q):return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def mul(x,y,q):return ((x[0]*y[0]+2*x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)
def scale(x,a,q):return (x[0]*a%q,x[1]*a%q)
def inv(x,q):
    d=(x[0]*x[0]-2*x[1]*x[1])%q
    return scale((x[0],-x[1]),pow(d,-1,q),q)
def original_e3(p):
    # E3(t): y^2+xy+(t/27)y=x^3; z=-x/y, t=(2-T)/4.
    # Fixed-z coefficient H_[p-1] and its t derivative, exact binomial sum.
    q=p*p;n=p-1;a=scale((2,-1),pow(108,-1,q),q)
    power=prev=(1,0);H=Ht=(0,0)
    for j in range(n//3+1):
        c=comb(n-j,j)*comb(n-2*j,j)
        H=add(H,scale(power,c,q),q)
        if j:Ht=add(Ht,scale(prev,j*c*pow(27,-1,q),q),q)
        prev=power;power=mul(power,a,q)
    W=add(H,scale(mul(Ht,(0,1),q),6*pow(4,-1,q),q),q)
    return H,W
def frozen_scalar(p):
    q=p*p;B=1;g=h=0
    for k in range(p):
        g=(g+B)%q;h=(h+(12*k+1)*B)%q
        if k<p-1:B=B*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,q)%q
    return g,h
def test(p):
    q=p*p;H,W=original_e3(p);g,h=frozen_scalar(p)
    assert H[0]%p==g%p==H[1]%p==0
    assert W[0]%p==h%p and W[1]%p==0 and h%p!=0
    u=mul((h,0),inv(W,q),q)  # Unique common unit forced by second port
    assert u[0]%p==1 and u[1]%p==0 and mul(u,W,q)==(h,0)
    residual=add(mul(u,H,q),(-g,0),q)
    assert residual==add(H,(-g,0),q)
    assert residual[0]%p==residual[1]%p==0
    delta=(residual[0]//p,residual[1]//p)
    assert delta!=(0,0)  # Common scalar alone cannot align both ports
    c=mul(add((g,0),scale(mul(u,H,q),-1,q),q),inv(W,q),q)
    assert c[0]%p==c[1]%p==0
    assert add(mul(u,H,q),mul(c,W,q),q)==(g,0)
    assert mul(u,W,q)==(h,0)
    if p==373:
        assert (H,g,W,h,u,delta,c)==((130177,17904),8952,(97151,8952),62835,(11191,63410),(325,48),(12309,126820))
    return p,delta,(c[0]//p,c[1]//p)
if __name__=='__main__':
    for p in PRIMES:print('p, common-unit obstruction /p, repair shear /p:',*test(p))
    print('PASS: 8 exact E3 original-port common-unit no-go and triangular repair cases')
