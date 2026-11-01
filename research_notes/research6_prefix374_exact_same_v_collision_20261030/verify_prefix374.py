#!/usr/bin/env python3
"""PREFIX-374: exact global counterexample to v-only coherent observers.

All decisions are exact SymPy rationals / polynomial remainders / Fraction intervals.
Requires Python 3 and SymPy (tested in this environment). No floats in proof.
"""
from fractions import Fraction as F
import json
import sympy as S

x,c,d=S.symbols('x c d',real=True)
i=S.I
A=S.Matrix([[4,4,0],[0,-4,4],[-5+3*i,0,-3+i],[-2-2*i,4+4*i,2+2*i],[-2,0,5+2*i]])
B=A[3:5,:]*A[:3,:].inv()
expected_B=S.Matrix([[S.Rational(5,2)+S.Rational(9,2)*i,S.Rational(3,2)+S.Rational(7,2)*i,4*i],
    [S.Rational(11,4)+S.Rational(15,8)*i,S.Rational(11,4)+S.Rational(15,8)*i,S.Rational(5,4)+S.Rational(9,4)*i]])
assert all(S.simplify(B[j,k]-expected_B[j,k])==0 for j in range(2) for k in range(3))
T=(200-2125*x)/(12759*x-3521)
Q=S.Matrix([34000+204144*T,3200+56336*T,58250+1286*T,46600+12936*T,31525+28011*T])
K=S.Rational(1101,424)-S.Rational(995,106)*x
q4=S.Rational(217,106)-S.Rational(381,53)*x
q5=S.Rational(1133,848)-S.Rational(921,212)*x
assert all(S.cancel(Q[j]/Q[0]-target)==0 for j,target in enumerate([1,x,K,q4,q5]))

v=c+i*d
rows=[list(B.row(0)),list(B.row(1))]
Ds=[];Rs=[]
for (aa,bb,cc),q in zip(rows,[q4,q5]):
    # With |u|^2=x, |v|^2=K, the original strength becomes Re(D*u)=R.
    Dj=S.expand(S.conjugate(aa+cc*v)*bb)
    n0=S.expand(S.conjugate(aa+cc*v)*(aa+cc*v))
    nlin=S.expand(n0-(S.re(cc)**2+S.im(cc)**2)*(c*c+d*d-K))
    Rj=S.factor((q-nlin-S.expand(bb*S.conjugate(bb))*x)/2)
    Ds.append(Dj);Rs.append(Rj)
D4,D5=Ds;R4,R5=Rs
assert S.simplify(R4-(-72*c+40*d+257*x-132)/4)==0
assert S.simplify(R5-(-51940*c+26076*d+158627*x-91398)/6784)==0

P=969505478041769500*x**3-252816887318686105*x**2+21782521288209164*x-619641499680032
cn=-(64604767873260*x**2-3646596531185*x-272689480603)
dn=-(152534330462820*x**2-32445854882263*x+1713609219709)
common=106*(66291907391*x-6553384154)
cf=cn/common;df=dn/common
subs={c:cf,d:df}

# The single cubic P is an exact common algebraic solution of the
# circle equation, collinearity determinant and BOTH compatibility rows.
N4=S.expand(S.re(D4)**2+S.im(D4)**2)
det=S.expand(S.re(D4)*(-S.im(D5))-S.re(D5)*(-S.im(D4)))
Ere=S.expand(S.re(D4)*R5-S.re(D5)*R4)
Eim=S.expand(S.im(D4)*R5-S.im(D5)*R4)
identities=[(c*c+d*d-K).subs(subs),det.subs(subs),Ere.subs(subs),Eim.subs(subs)]
for expr in identities:
    num,den=map(S.expand,S.together(expr).as_numer_denom())
    assert S.rem(S.Poly(num,x),S.Poly(P,x)).is_zero

class Interval:
    def __init__(self,lo,hi=None):
        if isinstance(lo,Interval): self.lo,self.hi=lo.lo,lo.hi
        else: self.lo,self.hi=F(lo),F(hi) if hi is not None else F(lo)
        assert self.lo<=self.hi
    def __add__(self,b):
        b=Interval(b);return Interval(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,b):return self+-Interval(b)
    def __rsub__(self,b):return Interval(b)-self
    def __mul__(self,b):
        b=Interval(b); z=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return Interval(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=Interval(b);assert b.lo>0 or b.hi<0
        return self*Interval(1/b.hi,1/b.lo)
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return Interval(1)
        if n==1:return self
        if n%2==0:
            arr=[self.lo**n,self.hi**n]
            return Interval(0 if self.lo<=0<=self.hi else min(arr),max(arr))
        return Interval(self.lo**n,self.hi**n)

def ef(v):return F(int(v.p),int(v.q)) if isinstance(v,S.Rational) else F(v)
lo=F(100169778291,10**12);hi=F(100169778292,10**12)
X=Interval(lo,hi)

def polyeval(poly,z):
    ans=Interval(0)
    for coeff in S.Poly(poly,x).all_coeffs():ans=ans*z+ef(coeff)
    return ans
assert polyeval(P,Interval(lo)).hi<0<polyeval(P,Interval(hi)).lo
# Derivative lower bound on the full isolating interval is strictly positive.
assert polyeval(S.diff(P,x),X).lo>0
assert F(8,85)<lo<hi<F(4321,21259)
assert (66291907391*X-6553384154).lo>0
C=-(64604767873260*X**2-3646596531185*X-272689480603)/(106*(66291907391*X-6553384154))
D=-(152534330462820*X**2-32445854882263*X+1713609219709)/(106*(66291907391*X-6553384154))
k=S.Rational(1101,424)-S.Rational(995,106)*x
Kbox=Interval(ef(S.Rational(1101,424)))-ef(S.Rational(995,106))*X
U4=14*C-6*D+F(39,2)
V4=-6*C-14*D+2
N=U4**2+V4**2
rhs4=(-72*C+40*D+257*X-132)/4
slack=X*N-rhs4**2
margin=16*(V4**2)*slack-N**2
assert N.lo>F(1,10)
assert slack.lo>F(8,1000)
assert margin.lo>F(5,10000)
# The last strict inequality certifies |C_u(+) - C_u(-)| > 1.
# u_{+,-}=(R4*(alpha-i beta) +/- sqrt(slack)*(beta+i alpha))/N.
# They have |u|^2=x and Re(D4*u)=R4, hence both other intensities.

out={'unit':'PREFIX-374',
     'claim':'two distinct physical sources share exactly the same v at one real algebraic x',
     'exact_cubic':str(S.expand(P)),
     'root_isolation_x':[str(lo),str(hi)],
     'c_formula':str(cn)+' / ('+str(common)+')',
     'd_formula':str(dn)+' / ('+str(common)+')',
     'four_polynomial_identities_verified_mod_cubic':True,
     'exact_rational_interval_checks':{
         'N4_gt':'1/10','slack_gt':'1/125','gap_square_margin_gt':'1/2000',
         'strict_Cu_gap_gt':'1', 'noise_tolerance_Cu_midpoint':'1/2'},
     'original_five_intensities':'identical',
     'all_coherent_observers_of_v':'identical',
     'counterexample_scope':'one algebraic parameter inside 0<=t<=1/4; no branch-exhaustion assumption',
     'formal_project_admission':False,'independent_review':False,
     'native_X6_typed_BRC_computation':False}
print(json.dumps(out,ensure_ascii=False,indent=2))
print('PASS_PREFIX374_EXACT_SAME_V_TWO_PHYSICAL_SOURCES')
