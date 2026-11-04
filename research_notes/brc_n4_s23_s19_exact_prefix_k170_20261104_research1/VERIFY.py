#!/usr/bin/env python3
"""Exact rational interval certificate for s=1/9 S23 finite-prefix and K>=170.
Python standard library only. All interval endpoints are fractions.
"""
from fractions import Fraction as F
from math import isqrt, factorial

ROUND=10**35
class I:
    def __init__(self, lo, hi=None):
        lo=F(lo); hi=F(lo if hi is None else hi)
        self.lo=F((lo*ROUND).numerator//(lo*ROUND).denominator,ROUND)
        neg=-(hi*ROUND)
        self.hi=F(- (neg.numerator//neg.denominator),ROUND)
        assert self.lo<=self.hi
    def __add__(self,b):
        b=iv(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-iv(b)
    def __rsub__(self,b):return iv(b)+-self
    def __mul__(self,b):
        b=iv(b);a=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return I(min(a),max(a))
    __rmul__=__mul__
    def inverse(self):
        assert self.lo*self.hi>0
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,b):return self*iv(b).inverse()
    def __rtruediv__(self,b):return iv(b)*self.inverse()
    def square(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))
    def midpoint(self):return (self.lo+self.hi)/2
    def __repr__(self):return f'[{float(self.lo):.18g}, {float(self.hi):.18g}]'
def iv(x):return x if isinstance(x,I) else I(x)
SCALE=10**45
LOG_N=24
EXP_N=25

def sqrt_f(x):
    x=F(x);assert x>=0
    v=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    return I(F(v,SCALE),F(v+1,SCALE))

def log_gt1(x):
    x=F(x);assert x>=1
    y=(x-1)/(x+1)
    sm=sum((2*y**(2*j+1)/F(2*j+1)) for j in range(LOG_N))
    rem=2*y**(2*LOG_N+1)/((2*LOG_N+1)*(1-y*y))
    return I(sm,sm+rem)

def log_f(x):
    x=F(x);assert x>0
    if x>=1:return log_gt1(x)
    return -log_gt1(1/x)

def log_i(x):
    x=iv(x);assert x.lo>0
    return I(log_f(x.lo).lo,log_f(x.hi).hi)

def exp_pos(x):
    x=F(x);assert 0<=x<=1
    sm=sum((x**j/F(factorial(j))) for j in range(EXP_N+1))
    rem=3*x**(EXP_N+1)/F(factorial(EXP_N+1))
    return I(sm,sm+rem)

def exp_f(x):
    x=F(x)
    return exp_pos(x) if x>=0 else exp_pos(-x).inverse()

def exp_i(x):
    x=iv(x)
    return I(exp_f(x.lo).lo,exp_f(x.hi).hi)

def round_frac(x,q=10**12):
    n=x.numerator*q//x.denominator
    # nearest integer, ties irrelevant to validity
    if 2*(x.numerator*q % x.denominator)>=x.denominator:n+=1
    return F(n,q)

def max_square(x):
    x=iv(x)
    return max(x.lo*x.lo,x.hi*x.hi)

s=F(1,9);v=F(1,21);a=s*(1+v)/2;b=s*(1-v)/2
assert a==F(11,189) and b==F(10,189)
U=sqrt_f(a*b);V=sqrt_f((1-a)*(1-b));L1=log_f(a/b);L2=log_f((1-a)/(1-b));DELTA=L1-L2

# Exact -log of Chernoff coefficients and derivatives at t=1/2+delta
CT=-log_i(I(1-s)+2*U)

def bf(delta):
    z1=U*exp_i(iv(delta)*L1)
    z2=V*exp_i(iv(delta)*L2)
    z=z1+z2
    return -log_i(z),-(z1*L1+z2*L2)/z

def tf(delta):
    z1=U*exp_i(iv(delta)*L1)
    z2=U*exp_i(-iv(delta)*L1)
    z=I(1-s)+z1+z2
    return -log_i(z),-(z1-z2)*L1/z

B0,D=bf(F(0))
assert D.lo>0
# Valid global strong concavity bounds, over t in [0,1]:
# w_B in [b,a], hence -f_B''=w(1-w)(L1-L2)^2 >= b(1-a)*DELTA^2
mB=(iv(b*(1-a))*DELTA.square()).lo
# For T, x+y>=2sqrt(ab), z=1-s+x+y<=1.
# -f_T''=L1^2 [u-v0^2]>=L1^2 u(1-u) >= L1^2*2sqrt(ab)*(1-s)
mT=(2*U*iv(1-s)*L1.square()).lo
assert mB>0 and mT>0
# choose rational delta from exact mid-point of quadratic model, then
# certify true maximum with global strong concavity: f(t*)<=f(t0)+f'(t0)^2/(2m).
kB=(U*V/(U+V).square())*DELTA.square()
kT=(2*U/(iv(1-s)+2*U))*L1.square()

def cb_interval():
    delta=round_frac(D.midpoint()/kB.midpoint())
    f,g=bf(delta)
    assert 0<delta<F(1,2)
    return I(f.lo,f.hi+max_square(g)/(2*mB)),delta

CB,deltaB=cb_interval()
E=CT-iv(F(17,9))*CB
d=CB-B0
assert E.lo>0 and (CB/9-8*E-16*d).lo>0
assert (99*E-16*d).lo>0
print('CERT_BASE: exact rational bounds on C_T,C_B,E,d; old eventual K>=187 verified')
print('delta_B',deltaB)
print('E',E)
print('d',d)

# Whole-prefix complete by two theorems:
# 1) For m not divisible by 9, C(K)-C(m,n) >= C_B/9-8E-16d > 0.
# 2) For m=9j, fixed K=17L+r, j in [0,L]:
# max_t[9j f_T(t)+(K-17j)f_B(t)] convex in j, so only
# j=0 (pure B) and j=L (9L T, r B) can be optimal.
# For fixed L>=1 the difference D(L,r)=C(9L,r)-(17L+r)C_B
# is STRICTLY decreasing in integer r: C(9L,r+1)<C(9L,r)+C_B,
# because maximizers for T and B are distinct.

def mix_interval(L,r):
    assert L>=1 and 0<=r<17
    delta=round_frac(F(r)*D.midpoint()/(9*L*kT.midpoint()+r*kB.midpoint()))
    assert 0<=delta<F(1,2)
    f1,g1=tf(delta)
    f2,g2=bf(delta)
    f=9*L*f1+r*f2
    der=9*L*g1+r*g2
    # 9L * mT is the globally-valid -f_mix'' lower bound.
    return I(f.lo, f.hi+max_square(der)/F(2*9*L*mT)),delta

def cert(L,r,want):
    K=17*L+r
    cm,trial=mix_interval(L,r)
    score=cm-K*CB
    if want=='T': assert score.lo>0, (L,r,score)
    else:assert score.hi<0,(L,r,score)
    print(f'K={K:3d} L={L:2d} r={r:2d} {want}: [{float(score.lo):+.15e}, {float(score.hi):+.15e}], trial={trial}')
    return score

# Only 19 decisive boundary certificates: monotonicity in r extends them
# to every 1<=K<187. For L=0 the two endpoints coincide (pure B).
lastT=[1,3,5,6,8,10,12,13,15]
verified=[]
for L,last in enumerate(lastT,1):
    verified.append(cert(L,last,'T'))
    verified.append(cert(L,last+1,'B'))
verified.append(cert(10,16,'T'))

# K=169 (L9, r16) pure B and K=170 (L10,r0) pure T;
# K=170..186 follow monotonicity, K>=187 follow old general lemma,
# proving smallest integer K0 such that all K>=K0 follow period-17 formula.
assert all(z.lo>0 if i%2==0 else z.hi<0 for i,z in enumerate(verified[:18]))
assert verified[18].lo>0
print('RESULT: for 1<=K<=16 pure B; 17<=K<=169 L=floor(K/17), r=K%17, period endpoint wins iff r<=lastT[L-1].')
print('RESULT: for every integer K>=170, unique optimum=(9 floor(K/17), K mod 17).')
print('RESULT: minimal eventual threshold K0=170 (K=169 is pure B).')
print('PASS_BRC_S23_S19_EXACT_PREFIX_MINIMAL_PERIOD17_THRESHOLD_20261104')
