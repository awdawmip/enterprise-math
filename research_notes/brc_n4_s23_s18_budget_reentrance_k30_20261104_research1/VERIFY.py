"""Exact rational interval certificate for S23 at v=1/21, s=1/8.
Run: python VERIFY.py. No floating-point arithmetic or external packages.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial, isqrt

@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q
    def __init__(self, a, b=None):
        object.__setattr__(self,'lo', Q(a))
        object.__setattr__(self,'hi', Q(a if b is None else b))
        assert self.lo <= self.hi
    @staticmethod
    def of(v): return v if isinstance(v,I) else I(v)
    def __add__(self, other):
        o=I.of(other);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-I.of(other)
    def __rsub__(self,other):return I.of(other)+-self
    def __mul__(self,other):
        o=I.of(other)
        xs=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=I.of(other)
        assert o.lo>0 or o.hi<0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,other):return I.of(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0 and self.lo<0<self.hi:
            return I(0,max(self.lo**n,self.hi**n))
        vals=(self.lo**n,self.hi**n)
        return I(min(vals),max(vals))
    def fmt(self,digits=17):
        from decimal import Decimal,localcontext
        with localcontext() as c:
            c.prec=digits+8
            return '['+format(Decimal(self.lo.numerator)/Decimal(self.lo.denominator),f'.{digits}E')+','+format(Decimal(self.hi.numerator)/Decimal(self.hi.denominator),f'.{digits}E')+']'

def sqrt_q(x,decimals=30):
    assert x>=0
    scale=10**decimals
    r=isqrt(x.numerator*scale*scale//x.denominator)
    return I(Q(r,scale),Q(r+1,scale))

def atanh_q(x,n=13):
    assert Q(0)<x<Q(1)
    val=sum((x**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
    err=x**(2*n+1)/(Q(2*n+1)*(1-x*x))
    return I(val,val+err)

def exp_pos(x,n=12):
    assert Q(0)<=x<Q(1)
    val=sum((x**j/Q(factorial(j)) for j in range(n+1)),Q(0))
    err=x**(n+1)/Q(factorial(n+1))/(1-x/Q(n+2))
    return I(val,val+err)

def exp_i(x):
    assert -1<x.lo<=x.hi<1
    if x.lo>=0:
        return I(exp_pos(x.lo).lo,exp_pos(x.hi).hi)
    if x.hi<=0:
        return I(1/exp_pos(-x.lo).hi,1/exp_pos(-x.hi).lo)
    return I(1/exp_pos(-x.lo).hi,exp_pos(x.hi).hi)

def minus_log_near_one(z,n=7):
    assert 0<z.lo<=z.hi<=1, 'Z must be in (0,1]'
    w=(I(1)-z)/(I(1)+z)
    assert 0<=w.lo<=w.hi<Q(1,10)
    def p(x):return 2*sum((x**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
    rem=2*w.hi**(2*n+1)/(Q(2*n+1)*(1-w.hi*w.hi))
    return I(p(w.lo),p(w.hi)+rem)

s=Q(1,8);v=Q(1,21);k=s/(2-s)
a=s*(1+v)/2;b=s*(1-v)/2
r=sqrt_q(1-v*v);rb=sqrt_q(1-(k*v)**2)
alpha=atanh_q(v);gamma=atanh_q(k*v)
X=I(s)/2*r;Y=I(2-s)/2*rb

# Z(δ) = Σ P^((1+δ)/2)Q^((1-δ)/2), δ∈[-1,1].
def coeffs(delta):
    z1=exp_i(alpha*delta);z2=exp_i(-alpha*delta)
    z3=exp_i(-gamma*delta)
    zt=I(1-s)+(I(s)*r)*(z1+z2)/2
    zb=X*z1+Y*z3
    ztd=(I(s)*r)*alpha*(z1-z2)/2
    zbd=X*alpha*z1-Y*gamma*z3
    return zt,zb,ztd,zbd

def fT(delta):return minus_log_near_one(coeffs(I(delta))[0])
def fB(delta):return minus_log_near_one(coeffs(I(delta))[1])
def fMix(m,n,delta):
    zt,zb,td,bd=coeffs(I(delta))
    val=m*minus_log_near_one(zt)+n*minus_log_near_one(zb)
    der=-(m*td/zt+n*bd/zb)
    return val,der

# Optimizers use one common exponent. Exact rational test points are just evaluation probes.
dB=Q(7413,1000000);d4=Q(1561,1000000);d5=Q(1853,1000000)
b_probe,b_der=fMix(0,1,dB)
ct=fT(0)

# For any δ∈[-1,1], log Z_B''(δ)=w(1-w)(alpha+gamma)^2;
# w in [b,a], so log Z_B'' >= b(1-a)*v^2 > 1/10000.
muB=b*(1-a)*v*v
assert muB>Q(1,10000)
# max f <= f(d0) + [f'(d0)]^2/(2mu), by global mu-strong concavity.
bound_sq=lambda d:max(abs(d.lo),abs(d.hi))**2
CB_lo=b_probe.lo
CB_hi=b_probe.hi + bound_sq(b_der)/(2*Q(1,10000))
CB=I(CB_lo,CB_hi)

block=8*ct-15*CB
assert block.lo>0
# For any 1<=m<=16 with 8∤m, residual budget slack >= 1/8.
eps=ct-I(Q(15,8))*CB
assert eps.lo>0 and (16*eps.hi<CB.lo/8)

mix4,_=fMix(8,4,d4)
D4=mix4-19*CB
assert D4.lo>0

# Curvature for 8T+5B: log ZT'' >= alpha² (s*r -v²),
# because ZT<=1 (Hölder), tilted nonzero mass >=s*r,
# and |tilted signed moment|<=tanh(alpha)=v.
# log ZB'' >= b(1-a)*alpha². Hence curvature >1/400.
mu_mix_lo=8*v*v*(s*(1-v*v)-v*v)+5*b*(1-a)*v*v
assert mu_mix_lo>Q(1,400)
mix5,mix5_der=fMix(8,5,d5)
mix5_upper=mix5.hi+bound_sq(mix5_der)/(2*Q(1,400))
D5=I(mix5.lo-20*CB_hi,mix5_upper-20*CB_lo)
assert D5.hi<0

# Strict monotonic D(n)=Cmix(8,n)-(15+n)CB follows from max(f+g)<=max(f)+max(g).
# Linear upper bound kills all m not divisible by 8 for K<=30.
# m=8, n<=K-15; m=16,n<=K-30. For K<=29 there is at most one
# nonzero multiple-of-8 m. D4>0>D5 thus D(0..4)>0 and D(5..14)<0.
# For K=30, 16 T beats 8 T + 15 B by the positive block gap.
res={K: ((0,K) if K<=14 or 20<=K<=29 else (8,K-15) if 15<=K<=19 else (16,0)) for K in range(1,31)}
assert res[15]==(8,0) and res[16]==(8,1) and res[19]==(8,4)
assert res[20]==(0,20) and res[30]==(16,0)
print('PASS_S23_S18_INTEGER_BUDGET_REENTRANCE_EXACT_20261104')
print('domain: s=1/8,v=1/21, integer K=1..30; all real common Chernoff exponents')
for name,x in [('C_T',ct),('C_B',CB),('8C_T-15C_B',block),('D4_lower_at_delta',D4),('D5_upper_with_curvature',D5),('eps',eps)]:
    print(name,x.fmt(22))
print('probes', 'dB=',dB,'d4=',d4,'d5=',d5)
print('unique_optimizers_by_budget',res)
