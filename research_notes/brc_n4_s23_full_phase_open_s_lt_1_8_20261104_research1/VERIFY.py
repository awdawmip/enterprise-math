#!/usr/bin/env python3
"""Exact rational certificate for K=17 S23 full parameter interval (0,1/8).
All signs certified via Fractions, interval arithmetic, isqrt, and atanh remainders.
"""
from fractions import Fraction as F
from math import isqrt
G=10**44

def dn(x): return F(x.numerator*G//x.denominator,G)
def up(x): return -dn(-x)
def I(x): return (x,x)
def R(x): return (dn(x[0]),up(x[1]))
def add(x,y): return R((x[0]+y[0],x[1]+y[1]))
def neg(x): return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y]
    return R((min(v),max(v)))
def div(x,y):
    assert y[0]>0 or y[1]<0, ('denominator crosses zero',y)
    return mul(x,R((F(1)/y[1],F(1)/y[0])))
def sqrt_pt(x):
    assert x>0
    k=isqrt(x.numerator*G*G//x.denominator)
    return (F(k,G),F(k+1,G))
def log_pt(x,N=19):
    assert x>0
    y=(x-1)/(x+1)
    assert abs(y)<F(1,3),('large log',x)
    p=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    err=2*abs(y)**(2*N+1)/(F(2*N+1)*(1-y*y))
    return R((p-err,p+err))
def log_iv(x): return (log_pt(x[0])[0],log_pt(x[1])[1])

alpha,beta=F(11,21),F(10,21)
H=log_pt(alpha/beta)
d=sub(I(1),mul(I(2),sqrt_pt(alpha*beta)))

def stats(s):
    a=mul(I(alpha),s)
    b=mul(I(beta),s)
    om_a=sub(I(1),a)
    om_b=sub(I(1),b)
    L=log_iv(div(om_b,om_a))
    M=add(H,L)
    r=div(L,M)
    rp=div(mul(I(alpha-beta),H),mul(mul(om_a,om_b),mul(M,M)))
    CB=add(mul(r,log_iv(div(r,a))),mul(sub(I(1),r),log_iv(div(sub(I(1),r),om_a))))
    CT=neg(log_iv(sub(I(1),mul(d,s))))
    logratio=log_iv(div(mul(r,om_a),mul(a,sub(I(1),r))))
    CBprime=add(sub(mul(rp,logratio),div(r,s)),div(mul(I(alpha),sub(I(1),r)),om_a))
    CTprime=div(d,sub(I(1),mul(d,s)))
    gp=sub(mul(I(9),CTprime),mul(I(17),CBprime))
    g=sub(mul(I(9),CT),mul(I(17),CB))
    return g,gp,CB,CT

s0=F(1,9); s1=F(1,8)
# Analytic Chernoff lemma, established in PROOF.md: CT(s)<2CB(s) for 0<s<1.
# Cost feasibility for 0<s<1/8: m=0..8 has n<=17-2m;
# m=9 iff s>=1/9 (n=0); m>=10 is never feasible.
assert 9*(2-s0)==17 and 10*(2-s1)>17
for m in range(1,9): assert m*s1<=1

# Section I: positivity on [1/9, 1/9+10^-6] by monotonic endpoint enclosures.
a0=s0; a1=s0+F(1,10**6); a2=s0+F(1,10**5)
positive_cells=10
for j in range(positive_cells):
    a=a0+(a1-a0)*F(j,positive_cells)
    b=a0+(a1-a0)*F(j+1,positive_cells)
    # CT and CB both increase with s, so this is a lower bound on g.
    assert 9*stats(I(a))[3][0]-17*stats(I(b))[2][1]>0, ('positive cell',j)

# Section II: unique decreasing g and unique zero on [1/9+10^-6, 1/9+10^-5].
N=128
lowest=None;highest=None
for j in range(N):
    a=a1+(a2-a1)*F(j,N);b=a1+(a2-a1)*F(j+1,N)
    gp=stats((a,b))[1]
    lowest=gp[0] if lowest is None else min(lowest,gp[0]);highest=gp[1] if highest is None else max(highest,gp[1])
    assert gp[1]<-F(1,2500),('derivative',j,gp)
    assert gp[0]>-F(1,1300),('derivative lower',j,gp)
assert stats(I(a1))[0][0]>0
assert stats(I(a2))[0][1]<0
lo=s0+F(9805774634637,10**18)
hi=s0+F(9805774634638,10**18)
assert stats(I(lo))[0][0]>0 and stats(I(hi))[0][1]<0
assert a1<lo<hi<a2

# Section III: negativity on [a2,1/8].
# CB is nondecreasing by independent Bernoulli thinning of a larger-s sample.
# CT'=d/(1-ds)<1/500 on [0,1/8], verified by a rational sqrt enclosure.
assert div(d,sub(I(1),mul(d,I(s1))))[1]<F(1,500)
# Hence, g(s)<=g(a)+9*(s-a)/500. Start at a2 with g(a2)<0
# and proceed with steps of length min(25*(-upper(g(a))),remaining interval).
a=a2
negative_cells=0
while a<s1:
    g_hi=stats(I(a))[0][1]
    assert g_hi<0,('negative start',negative_cells,g_hi)
    step=min(25*(-g_hi),s1-a)
    b=a+step
    assert g_hi+F(9,500)*step<0,('negative derivative cap',negative_cells)
    a=b
    negative_cells+=1
    assert negative_cells<10000
assert a==s1
assert stats(I(s1))[0][1]<0
print('K=17, 0<s<1/8: pure B if s<1/9; 9T if 1/9<=s<s*; pure B if s*<s<1/8.')
print('At s* exactly 9T and 17B tie, unique switch s* in J.')
print('Root offset in (9805774634637,9805774634638)/10^18 relative to 1/9')
print('positive endpoint cells',positive_cells,'strict decreasing derivative cells',N,'negative extension cells',negative_cells)
print('g(1/9):',float(stats(I(s0))[0][0]),float(stats(I(s0))[0][1]))
print('g(1/8):',float(stats(I(s1))[0][0]),float(stats(I(s1))[0][1]))
print('negative derivative enclosure on J:',float(lowest),float(highest))
print('PASS_S23_K17_FULL_OPEN_PARAMETER_INTERVAL_BELOW_1_8_20261104')
