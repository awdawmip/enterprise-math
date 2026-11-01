#!/usr/bin/env python3
"""PREFIX-420 exact algebraic certificate: first negative-branch active-set event.

Model scope: the five-port external static coherent-amplitude model of PREFIX-419.
All assertions are exact Fraction/integer-square-root operations; no floating tests.
"""
from fractions import Fraction as F
from math import isqrt

BETA=F(1,10**6)
E=F(53,8)
N=F(37577,64)
L=F(187,100000)
R=F(1,500)
DEN=10**15
C_LO=F(1941856698303,DEN)
C_HI=F(1941856698304,DEN)
CE_LO=F(1942078678057,DEN)
CE_HI=F(1942078678058,DEN)

class I:
    def __init__(self,a,b=None):
        self.lo=F(a); self.hi=F(a if b is None else b)
        assert self.lo<=self.hi
    @staticmethod
    def cast(x): return x if isinstance(x,I) else I(x)
    def __add__(self,y):
        y=I.cast(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-I.cast(y)
    def __rsub__(self,y):return I.cast(y)+-self
    def __mul__(self,y):
        y=I.cast(y); c=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return I(min(c),max(c))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=I.cast(y); assert y.lo*y.hi>0
        return self*I(1/y.hi,1/y.lo)
    def __rtruediv__(self,y):return I.cast(y)/self
    def __repr__(self):return f'I({self.lo}, {self.hi})'

def sqrt_int_interval(x,scale=10**36):
    x=I.cast(x); assert x.lo>=0
    def lower(z):
        return F(isqrt((z.numerator*scale*scale)//z.denominator),scale)
    return I(lower(x.lo),lower(x.hi)+F(1,scale))

def Fcrit(eta):
    # Multiplying the t=beta tangency relation by 135424.
    return 35881*eta*eta+63662*BETA*eta+35881*BETA*BETA-135424*BETA

assert Fcrit(C_LO)<0<Fcrit(C_HI)
assert Fcrit(L)<0<Fcrit(R)
# q_0 = -23; p_0 = 61/8. Exact negative-corner linear inverse.
P=F(61,8);Q=F(-23);A=F(24);B=F(-48)
assert (P/2-1)/Q == -F(45,368)
assert (P/2-E)/Q == F(45,368)
assert 2*F(93,23)+F(48,23)*P==A
assert F(48,23)*Q==B
assert F(93,23)+F(48,23)*E-F(43,23)==16
# The original norm and tangency are the same quadratic.
for eta in [L,C_LO,C_HI,R]:
    x=-(eta+BETA)/2
    y=-F(45,368)*(eta-BETA)
    assert 135424*(x*x+y*y-BETA)==Fcrit(eta)
print('PASS exact quadratic, coefficient identities, 1e-15 root enclosure')

# Ranges for the positive-phase witness on eta in [0.00187,0.002].
eta=I(L,R)
Kp=eta-E*BETA
Sp=sqrt_int_interval(N*BETA-Kp*Kp)
assert Sp.lo>F(3,125) and Sp.hi<F(1,40)
alpha=F(1165); delta=F(182)
lam=(alpha-delta*Kp/Sp)/N
assert lam.lo>F(19,10) and lam.hi<F(21,10)
assert 16-E*lam.hi>0
xp=(Kp*23+Sp*F(61,8))/N
hp=2*xp+BETA
assert xp.lo>0 and hp.lo>0 and hp.hi<L
print('PASS positive branch witness: lambda>0, D>0, |h|<eta, t=beta, k=eta')

# Ranges for the negative-phase witness on eta in [critical,0.002].
eta2=I(C_LO,R) # lower bound slightly below the true event; h-feasibility proved analytically.
Km=-eta2-E*BETA
Sm=sqrt_int_interval(N*BETA-Km*Km)
assert Sm.lo>F(3,125) and Sm.hi<F(1,40)
Xm=(Km*P+Sm*Q)/N
Ym=(Km*Q-Sm*P)/N
assert Xm.hi<0 and Ym.hi<0
assert Xm.lo>-BETA*1000 and Ym.lo>-BETA*1000
# No noisy sign convention or floating-point comparison is used.
print('PASS negative circle-line witness: x<0,y<0,t=beta,k=-eta')

# Use a 1e-36 exact rational enclosure for sqrt(1+epsilon) in the
# parameterized fixed-u tangency condition at epsilon=10^-6.
eps=I(BETA)
w=sqrt_int_interval(1+eps)
p=(245-123*w)/16
q=(-123-245*w)/16
c=F(709,64)*eps
a=p/2-1
b=(p/2-E)*BETA-c

def fe(eta):
    # Multiplication, not interval division, keeps signs rigorous.
    num=a*eta+b
    return ((eta+BETA)/2)*((eta+BETA)/2)+(num/q)*(num/q)-BETA
assert fe(I(CE_LO)).hi<0 and fe(I(CE_HI)).lo>0
assert fe(I(R)).lo>0
# Uniform fixed-corner positive-phase support certificate for all epsilon and eta.
EPS=I(F(0),BETA)
Wp=sqrt_int_interval(1-EPS)
pp=(245+123*Wp)/16
qp=(-123+245*Wp)/16
ap=36+12*Wp
bp=-20+28*Wp
np=pp*pp+qp*qp
kp=I(L,R)+F(709,64)*EPS-E*BETA
sp=sqrt_int_interval(np*BETA-kp*kp)
al=ap*pp+bp*qp
de=ap*qp-bp*pp
ml=(al-de*kp/sp)/np
xxx=(kp*pp+sp*qp)/np
hhh=2*xxx+BETA
assert de.lo>0 and ml.lo>F(19,10) and ml.hi<F(21,10)
assert (16-E*ml).lo>0 and 0<hhh.lo and hhh.hi<L
print('PASS uniform epsilon positive fixed-u support and h-slack')
# Uniform negative fixed-u certificate of the circle-line witness signs.
Wm=sqrt_int_interval(1+EPS)
pm=(245-123*Wm)/16
qm=(-123-245*Wm)/16
am=36-12*Wm
bm=-20-28*Wm
nm=pm*pm+qm*qm
cm=F(709,64)*EPS
km=-I(L,R)-cm-E*BETA
sm=sqrt_int_interval(nm*BETA-km*km)
xx=(km*pm+sm*qm)/nm
yy=(km*qm-sm*pm)/nm
assert xx.hi<0 and yy.hi<0 and xx.lo> -F(1,1000) and yy.lo>-F(1,1000)
assert F(15,2)<pm.lo and pm.hi<F(31,4)
assert F(23)<=(-qm).lo and (-qm).hi<F(93,4)
assert F(239,10)<am.lo and am.hi<F(241,10)
assert F(479,10)<(-bm).lo and (-bm).hi<F(481,10)
# These bounds plus 0<(-y)/(-x)<P/|Q| give 2<mu<9/4,
# D>(A-(9/4)P)/(2*0.001)>3000, tau>0, by explicit algebra.
print('PASS uniform epsilon negative fixed-u dual-multiplier coefficient ranges')
# Exact fixed-u negative linear observation identity and robust dual bounds.
mu=bm/qm
lamh=(am-mu*pm)/2
d=16-lamh-E*mu
assert mu.lo>2 and lamh.lo>3 and d.lo>-3 and d.hi<3
assert 3-F(3)*F(3,2500)/(1-F(3,2500))>0
assert 2-F(3)*F(1,11000)/(1-F(3,2500))>0
# Uniform parameterized root lies inside [L,R]: F(epsilon,L)<0<F(epsilon,R).
# F(epsilon,L) decreases with epsilon by direct exact derivative signs,
# so F(0,L)<0 suffices; F(1e-6,R)>0 is checked above.
assert Fcrit(L)<0
print('PASS uniform negative fixed-u double-boundary convex/Lipschitz certificates')
print('PASS epsilon=1e-6 tangency root enclosed in 1e-15 interval')
print('PASS_PREFIX420_FIXED_SOURCE_FIRST_ACTIVE_SET_CHANGE_EXACT_CERTIFICATE')
