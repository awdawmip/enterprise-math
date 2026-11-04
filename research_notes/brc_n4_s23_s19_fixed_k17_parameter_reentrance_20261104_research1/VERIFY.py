#!/usr/bin/env python3
"""Rigorous finite-parameter Chernoff allocation certificates; Fraction/isqrt only."""
from fractions import Fraction as F
from math import isqrt, factorial

ONE=F(1)
S=10**32
def rin(x):
    return F(x.numerator*S//x.denominator,S)
def rout(x):
    return -rin(-x)
def rnd(x): return (rin(x[0]),rout(x[1]))

def sqrt_iv(x, digits=32):
    assert x >= 0
    M=10**digits
    k=isqrt(x.numerator*M*M//x.denominator)
    return (F(k,M), F(k+1,M))

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    z=[a*b for a in x for b in y]
    return rnd((min(z),max(z)))
def div(x,y):
    assert y[0]>0 or y[1]<0
    return mul(x,rnd((1/y[1],1/y[0])))
def iv(x): return (x,x)

def log_point(x, N=13):
    assert x>0
    y=(x-1)/(x+1)
    s=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    r=2*abs(y)**(2*N+1)/F((2*N+1)) /(1-y*y)
    return rnd((s-r,s+r))

def log_iv(x):
    return (log_point(x[0])[0],log_point(x[1])[1])

def exp_point(x, N=10):
    assert abs(x)<F(1,100)
    p=sum((x**j/F(factorial(j)) for j in range(N)),F(0))
    e=3*abs(x)**N/F(factorial(N))
    return rnd((p-e,p+e))

def exp_iv(x): return (exp_point(x[0])[0],exp_point(x[1])[1])

def model(s):
    h=F(1,42)
    a=s*(F(1,2)+h); b=s*(F(1,2)-h)
    U=sqrt_iv(a*b); V=sqrt_iv((1-a)*(1-b))
    l1=log_point(a/b); l2=log_point((1-a)/(1-b))
    # C_T = -log(1-s+2 sqrt(a*b)) is exact because T is symmetric.
    CT=neg(log_iv(add(iv(1-s),mul(iv(2),U))))
    delta=F(37375,10**7)
    x=mul(U,exp_iv(mul(iv(delta),l1)))
    y=mul(V,exp_iv(mul(iv(delta),l2)))
    Z=add(x,y)
    fB=neg(log_iv(Z))
    deriv=neg(div(add(mul(x,l1),mul(y,l2)),Z))
    q=sub(l1,l2)
    mB=b*(1-a)*q[0]**2 # q positive
    assert mB>0
    maxder=max(abs(deriv[0]),abs(deriv[1]))
    CB=(fB[0], fB[1]+maxder**2/(2*mB))
    E=sub(CT,mul(iv(2-s),CB))
    return CT,CB,E,deriv

points={
 'left':F(1,9)-F(1,10**6),
 'near_right':F(1,9)+F(1,10**6),
 'far_right':F(1,9)+F(1,10**5),
}
for key,s in points.items():
    CT,CB,E,d=model(s)
    assert CB[0]>F(1,10**5) and E[1]<F(1,10**8)
    # m<=8 candidates have at least 1/10 unspent budget, so are dominated by B^17.
    # 8E<(1/10)CB using the certified inequalities above.
    assert 8*E[1]<CB[0]/10
    difference=sub(mul(iv(9),CT),mul(iv(17),CB))
    if key=='left':
        assert 9*(2-s)>17  # 9 T not feasible.
    else:
        assert 9*(2-s)<17 and 10*(2-s)>17
        assert (difference[0]>0) if key=='near_right' else (difference[1]<0)
    print(key,'s=',s,'CB~=',float((CB[0]+CB[1])/2),
          'E~=',float((E[0]+E[1])/2),
          '9CT-17CB in [',float(difference[0]),',',float(difference[1]),']',
          'derivative bound=',float(max(map(abs,d))))
print('PASS_S23_S19_FIXED_K17_PARAMETER_REENTRANCE_EXACT_20261104')
