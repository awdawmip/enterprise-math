"""Stage328-B exact-rational certificate for cusp-slope obstruction.

Pure auxiliary Bernoulli BRC probability model, not native X6 dynamics.
Runs using Python 3 stdlib Fraction and sympy for symbolic polynomial identities.
All inequalities in proof are certified by rational interval arithmetic.
"""
from fractions import Fraction as Q
from math import isqrt
import sympy as sp

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(hi if hi is not None else lo)
        assert self.lo<=self.hi
    def __repr__(self): return f"[{self.lo}, {self.hi}]"
    def __add__(self,o):
        o=C(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-C(o)
    def __rsub__(self,o):return C(o)+-self
    def __mul__(self,o):
        o=C(o); a=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]; return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=C(o); assert o.lo>0 or o.hi<0, 'division across zero'; return self*I(1/o.hi,1/o.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n==1:return self
        if n%2: return self*(self**(n-1))
        t=self**(n//2);return t*t

def C(x): return x if isinstance(x,I) else I(x)
def abs_I(x):
    if x.lo>=0:return x
    if x.hi<=0:return -x
    return I(0,max(-x.lo,x.hi))

def B(k,z):return z**k*(1-z)**(3-k)
P=[Q(v,160) for v in (61,21,9,9)]
w=(1,3,3,1)
def r(k,x,y):return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-P[k]
def public_b(x,y):return Q(5,32)*sum(w[k]*abs_I(r(k,x,y)) for k in range(4))
def g(z):return z*(2-3*z)
def h(z):return (1-z)*(1-3*z)
def yp(x,y):return -4*h(x)/h(y)
def bp(x,y):return Q(15,16)*(Q(4,5)*g(x)+Q(1,5)*g(y)*yp(x,y))
def cx(x):return -(1-x)*(189-183*x)/256
def cy_left(y):return 3*y*(1-y)/64
def cy_right(y):return cy_left(y)+Q(21,256)*g(y)
def sl(x,y,post=False):
    return (cx(x)+(cy_right(y) if post else cy_left(y))*yp(x,y))/bp(x,y)

def bracket_dagger_y(decimals=35):
    D=10**decimals
    lower_root=isqrt(13*D*D)
    n=(D+lower_root)//8
    lo=Q(n,D);hi=Q(n+1,D)
    f=lambda z:16*z*z-4*z-3
    assert f(lo)<0<f(hi)
    return I(lo,hi)

def isolate_x_for_y(Y,iterations=115):
    # r1 rises with x in [0.237,0.238], falls with y in [0.575,0.576]
    lo=Q(237,1000);hi=Q(238,1000)
    assert r(1,I(lo),I(Y.lo)).hi<0
    assert r(1,I(hi),I(Y.hi)).lo>0
    for _ in range(iterations):
        mid=(lo+hi)/2
        R=r(1,I(mid),Y)
        if R.hi<0:lo=mid
        elif R.lo>0:hi=mid
        else:break
    assert r(1,I(lo),I(Y.lo)).hi<0
    assert r(1,I(hi),I(Y.hi)).lo>0
    return I(lo,hi)

Xstar=I(Q(231083940855521,10**15),Q(231083940855522,10**15))
Ystar=I(Q(555508857277,10**12),Q(555508857278,10**12))
Ydag=bracket_dagger_y()
Xdag=isolate_x_for_y(Ydag)
assert Q(237806902,10**9)<Xdag.lo<Xdag.hi<Q(237806904,10**9)
assert r(2,Xstar,Ystar).lo>0 and r(3,Xstar,Ystar).hi<0
assert r(0,Xdag,Ydag).hi<0 and r(2,Xdag,Ydag).lo>0 and r(3,Xdag,Ydag).hi<0
assert bp(Xstar,Ystar).lo>0 and bp(Xdag,Ydag).lo>0

# Exact comparison-pattern verification and independent symbolic differentiation.
A0=Q(1,4); A1=Q(3,4)
def sign_at(a,z,k):
    diff=B(k,I(a))-B(k,z)
    if diff.lo>0:return 1
    if diff.hi<0:return -1
    raise ValueError('nonfixed comparison')
def patterns(xval,yval):
    return tuple(tuple(sign_at(a,z,k) for k in range(4)) for a,z in ((A0,xval),(A1,xval),(A0,yval),(A1,yval)))
ps=patterns(Xstar,Ystar)
# For cusp itself only (3/4,y,k=2) crosses; take exact rational sample away from cusp.
left_y=I(Ydag.lo-Q(1,10**8));right_y=I(Ydag.hi+Q(1,10**8))
pl=patterns(Xdag,left_y)
pr=patterns(Xdag,right_y)
assert ps==pl
assert all(pl[i][k]==pr[i][k] for i in range(4) for k in range(4) if (i,k)!=(3,2))
assert pl[3][2]==1 and pr[3][2]==-1

t,u=sp.symbols('t u')
def f_sym(k,z): return z**k*(1-z)**(3-k)
def make_c(pattern):
    result=sp.Rational(0)
    for i,(a,z,c) in enumerate(((sp.Rational(1,4),t,63),(sp.Rational(3,4),t,1),(sp.Rational(1,4),u,9),(sp.Rational(3,4),u,7))):
        d_i=sum(sp.Rational(w[k],2)*pattern[i][k]*(f_sym(k,a)-f_sym(k,z)) for k in range(4))
        result+=c*d_i/256
    return sp.expand(result)
c_l=make_c(pl);c_r=make_c(pr)
assert sp.simplify(sp.diff(c_l,t)-(-(1-t)*(189-183*t)/256))==0
assert sp.simplify(sp.diff(c_l,u)-(3*u*(1-u)/64))==0
assert sp.simplify(sp.diff(c_r,t)-sp.diff(c_l,t))==0
assert sp.simplify(sp.diff(c_r,u)-sp.diff(c_l,u)-sp.Rational(21,256)*u*(2-3*u))==0

Sl=sl(Xstar,Ystar)
Sdleft=sl(Xdag,Ydag)
Sdright=sl(Xdag,Ydag,True)
margin=Sdright-Sl
# Explicit rational interval certificates (not floating-point comparisons)
assert Q(-1197919,10**6)<Sl.lo<=Sl.hi<Q(-1197917,10**6)
assert Q(-1280654,10**6)<Sdleft.lo<=Sdleft.hi<Q(-1280649,10**6)
assert Q(-1163998,10**6)<Sdright.lo<=Sdright.hi<Q(-1163995,10**6)
assert margin.lo>Q(1,30)
# Budget location: along r1=0 at both points b=(15/16)r2.
bs=Q(15,16)*r(2,Xstar,Ystar)
bd=Q(15,16)*r(2,Xdag,Ydag)
eps=bd-bs
assert Q(21814072,10**10)<eps.lo<=eps.hi<Q(21814073,10**10)

# Show r1_x>0 and r1_y<0 at star/dagger; monotone implicit curve.
for x,y in ((Xstar,Ystar),(Xdag,Ydag)):
    assert (Q(4,5)*h(x)).lo>0
    assert (Q(1,5)*h(y)).hi<0

print('STAGE328B_LOCAL_CUSP_MARGINAL_EXCHANGE_EXACT_PASS')
print('dagger y bracket',Ydag)
print('dagger x bracket',Xdag)
print('epsilon_dagger bracket',eps)
print('slope_initial',Sl)
print('slope_dagger_left',Sdleft)
print('slope_dagger_right',Sdright)
print('slope_gap',margin)
print('symbolic_16_word_sign_pattern_left',pl)
print('symbolic_16_word_sign_pattern_right',pr)
print('cusp cost jump symbolic verified: (21/256)*y*(2-3*y)')


# Explicit all-rational two-group witness only about 0.000001 above the cusp.
# Candidate right r1=0 branch Xw,Yw, while the two competing groups are fully rational.
Xw=I(Q(23781,100000))
def isolate_y_for_x(x,n=112):
    lo=Q(575,1000);hi=Q(576,1000)
    assert r(1,I(x),I(lo)).lo>0 and r(1,I(x),I(hi)).hi<0
    for _ in range(n):
        m=(lo+hi)/2
        if r(1,I(x),I(m)).lo>0:lo=m
        else:hi=m
    assert r(1,I(x),I(lo)).lo>0 and r(1,I(x),I(hi)).hi<0
    return I(lo,hi)
Yw=isolate_y_for_x(Q(23781,100000))
assert r(0,Xw,Yw).hi<0 and r(2,Xw,Yw).lo>0 and r(3,Xw,Yw).hi<0

def D_I(a,z):
    return Q(1,2)*sum(w[k]*abs_I(B(k,C(a))-B(k,z)) for k in range(4))
def c_I(x,y):
    return (63*D_I(Q(1,4),x)+D_I(Q(3,4),x)+9*D_I(Q(1,4),y)+7*D_I(Q(3,4),y))/256

# Preserve all 128 labeled and 32 public atoms via exact cubic/Bernoulli-TV formula.
comp1x=I(Q(2378087,10**7))
comp1y=I(Q(575698999217604420,10**18))
comp2x=I(Q(23108514,10**8))
comp2y=I(Q(555512675903066452,10**18))
P_1=Q(15,16)*r(2,Xstar,Ystar)
P_w=Q(15,16)*r(2,Xw,Yw)
slack=P_1+P_w-public_b(comp1x,comp1y)-public_b(comp2x,comp2y)
gain=c_I(Xstar,Ystar)+c_I(Xw,Yw)-c_I(comp1x,comp1y)-c_I(comp2x,comp2y)
eps_w=P_w-P_1
assert slack.lo>Q(2,10**9)
assert gain.lo>Q(1,10**8)
assert Q(2182,10**6)<eps_w.lo<=eps_w.hi<Q(218238,10**8)

def decimal_cert(interval,scale=10**12):
    lo=(interval.lo*scale).__floor__()
    hi=(interval.hi*scale).__ceil__()
    return f'({lo}/{scale}, {hi}/{scale})'

print('EXPLICIT_RATIONAL_TWO_GROUP_WITNESS_PASS')
print('epsilon_dagger_decimal_certificate',decimal_cert(eps,10**13))
print('epsilon_w_decimal_certificate',decimal_cert(eps_w,10**12))
print('public_slack_decimal_certificate',decimal_cert(slack,10**12))
print('tagged_gain_decimal_certificate',decimal_cert(gain,10**12))
print('candidate_X',Xw,'candidate_Y_exact_root_bracket',Yw)
print('competitor_pairs', (comp1x,comp1y),(comp2x,comp2y))
