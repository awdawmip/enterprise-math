#!/usr/bin/env python3
"""Exact-rational interval certificate for BRC S23 K=17 transition uniqueness.
All asserted signs are rational; no floating-point decisions.
"""
from fractions import Fraction as F
from math import isqrt

G=10**44

def down(x):return F(x.numerator*G//x.denominator,G)
def up(x):return -down(-x)
def I(x):return (x,x)
def R(x):return (down(x[0]),up(x[1]))
def add(x,y):return R((x[0]+y[0],x[1]+y[1]))
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y];return R((min(v),max(v)))
def div(x,y):
    assert y[0]>0 or y[1]<0, ('denominator straddles zero',y)
    return mul(x,R((1/y[1],1/y[0])))
def sqrt_pt(x):
    assert x>0
    k=isqrt(x.numerator*G*G//x.denominator)
    return (F(k,G),F(k+1,G))
def sqrt_iv(x):return(sqrt_pt(x[0])[0],sqrt_pt(x[1])[1])
def log_pt(x,N=19):
    assert x>0
    y=(x-1)/(x+1)
    assert abs(y)<F(1,3),('large atanh argument',x)
    p=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    err=2*abs(y)**(2*N+1)/(F(2*N+1)*(1-y*y))
    return R((p-err,p+err))
def log_iv(x):return (log_pt(x[0])[0],log_pt(x[1])[1])

alpha,beta=F(11,21),F(10,21)
H=log_pt(alpha/beta)
d=sub(I(1),mul(I(2),sqrt_pt(alpha*beta)))

def stats(s):
    a=mul(I(alpha),s)
    b=mul(I(beta),s)
    one_minus_a=sub(I(1),a)
    one_minus_b=sub(I(1),b)
    L=log_iv(div(one_minus_b,one_minus_a))
    M=add(H,L)
    r=div(L,M)
    # r'= (alpha-beta) H / [(1-alpha*s)(1-beta*s) M^2].
    rp=div(mul(I(alpha-beta),H),mul(mul(one_minus_a,one_minus_b),mul(M,M)))
    # Chernoff tilted Bernoulli probability r, hence C_B = D(r || a)
    ca=log_iv(div(r,a))
    cb=log_iv(div(sub(I(1),r),one_minus_a))
    CB=add(mul(r,ca),mul(sub(I(1),r),cb))
    CT=neg(log_iv(sub(I(1),mul(d,s))))
    # exact envelope derivative C_B' via r and its derivative
    logratio=log_iv(div(mul(r,one_minus_a),mul(a,sub(I(1),r))))
    CBprime=add(sub(mul(rp,logratio),div(r,s)),div(mul(I(alpha),sub(I(1),r)),one_minus_a))
    CTprime=div(d,sub(I(1),mul(d,s)))
    gd=sub(mul(I(9),CTprime),mul(I(17),CBprime))
    g=sub(mul(I(9),CT),mul(I(17),CB))
    return g,gd,CB,CT,r

left=F(1,9)+F(9805774,10**12)
right=F(1,9)+F(9805775,10**12)
start=F(1,9)+F(1,10**6)
end=F(1,9)+F(1,10**5)

# Endpoint signs, fully independent from previous external root script.
gl=stats(I(left))[0];gr=stats(I(right))[0]
assert gl[0]>0, gl
assert gr[1]<0, gr

# A single global interval may be over-wide: split into 128 exact rational slices.
N=128
max_hi=None
min_lo=None
for j in range(N):
    lo=start+(end-start)*F(j,N)
    hi=start+(end-start)*F(j+1,N)
    derivative=stats((lo,hi))[1]
    max_hi=derivative[1] if max_hi is None else max(max_hi,derivative[1])
    min_lo=derivative[0] if min_lo is None else min(min_lo,derivative[0])
    assert derivative[1]<0, ('nonnegative interval',j,derivative)

assert min_lo > -F(1,1300), min_lo
assert max_hi < -F(1,2500), max_hi
assert gl[0] > F(3,10**16),gl
assert gr[1] < -F(2,10**16),gr

# The earlier uniform B comparison excludes m=1,...,8 across the entire interval,
# not just at the root bracket. Cost 9T is feasible and 10T infeasible throughout.
assert 9*(2-end)<17 and 9*(2-start)<17
assert 10*(2-end)>17
for m in range(1,9):
    # 17-(2-s)m = 17- (17/9)m + m(s-1/9), fractional part
    # is m/9 + m(s-1/9) (for positive perturbation)
    assert F(m,9)+m*(start-F(1,9))>F(1,10)
    assert F(m,9)+m*(end-F(1,9))<1

_,_,CBstart,_,_=stats(I(start))
_,_,_,CTend,_=stats(I(end))
# C_B monotone by thinning; C_T increasing in s.
Eupper=CTend[1]-(2-end)*CBstart[0]
assert CBstart[0]>F(1,100000)
# NOTE: Eupper across full 1e-6..1e-5 may be too broad; if so we will split.
if 8*Eupper<CBstart[0]/10:
    cert='GLOBAL_COST_EXCLUSION'
else:
    # On each interval, optimize uniform cost exclusion using monotonic bounds.
    for j in range(N):
        lo=start+(end-start)*F(j,N)
        hi=start+(end-start)*F(j+1,N)
        _,_,CBlo,_,_=stats(I(lo))
        _,_,_,CThi,_=stats(I(hi))
        Eu=CThi[1]-(2-hi)*CBlo[0]
        assert 8*Eu<CBlo[0]/10, ('mixed-cost exclusion failed',j,Eu)
    cert='SLICED_COST_EXCLUSION'

# Refine the unique root to a unit bracket on the 10^-18 rational grid.
D=10**18
low=int((left-F(1,9))*D)
high=int((right-F(1,9))*D)
assert low*1==9805774*10**6 and high==9805775*10**6
while high-low>1:
    middle=(low+high)//2
    gm=stats(I(F(1,9)+F(middle,D)))[0]
    if gm[0]>0:low=middle
    elif gm[1]<0:high=middle
    else:raise ArithmeticError(('unresolved midpoint',middle,gm))
assert stats(I(F(1,9)+F(low,D)))[0][0]>0
assert stats(I(F(1,9)+F(high,D)))[0][1]<0
print('unique root in s=1/9 + epsilon; epsilon in (',low,'/10^18,',high,'/10^18)')
print('g(left) rational interval:',gl)
print('g(right) rational interval:',gr)
print('rigorous global derivative bound: -1/1300 < gprime < -1/2500')
print('gprime observed interval outer bounds (display only):',float(min_lo),float(max_hi))
print('mixed exclusion:',cert,'slices:',N)
print('PASS_S23_K17_UNIQUE_TRANSITION_FULL_INTERVAL_EXACT_20261104')
