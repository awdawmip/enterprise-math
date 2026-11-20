from fractions import Fraction as Q
import sympy as s
x,y,z=s.symbols('x y z',real=True)
w=(1,3,3,1); m=(61,21,9,9)
B=lambda k,t:t**k*(1-t)**(3-k)
r=lambda k,a,b:(4*B(k,a)+B(k,b))/5-Q(m[k],160)
l=Q(233,1000); h=Q(119,500); v=Q(561,1000); cap=Q(577,1000); top=Q(3,5)
assert s.simplify(sum(w[k]*r(k,x,y) for k in range(4)))==0
assert r(0,l,v)<0 and r(2,l,v)>0 and r(3,h,top)<0
assert r(1,l,v)>0 and r(1,h,cap)<0
b0=s.Rational(15,16)*r(2,x,y)
b1=s.Rational(15,16)*(r(1,x,y)+r(2,x,y))
A=s.Rational(3,4)*(1-2*x); By=s.Rational(3,16)*(1-2*y)
C=s.Rational(3,4)*x*(2-3*x); D=s.Rational(3,16)*y*(2-3*y)
for actual,expected in [(s.diff(b0,x),C),(s.diff(b0,y),D),(s.diff(b1,x),A),(s.diff(b1,y),By)]:
    assert s.simplify(actual-expected)==0
patterns_x=[(-1,1,1,1),(-1,-1,1,1)]
patterns_y=[(1,1,-1,-1),(-1,-1,1,1),(-1,-1,-1,1)]
def dp(sign):
    return -sum(w[k]*sign[k]*s.diff(B(k,z),z) for k in range(4))/2
cx=(63*dp(patterns_x[0])+dp(patterns_x[1]))/256
cy0=(9*dp(patterns_y[0])+7*dp(patterns_y[1]))/256
cy1=(9*dp(patterns_y[0])+7*dp(patterns_y[2]))/256
p=(1-z)*(189-183*z)/256
q0=3*z*(1-z)/64
q1=3*z*(18-25*z)/256
assert s.simplify(cx+p)==s.simplify(cy0-q0)==s.simplify(cy1-q1)==0
for a,xx in [(Q(1,4),l),(Q(1,4),h),(Q(3,4),l),(Q(3,4),h)]:
    pattern=patterns_x[0] if a==Q(1,4) else patterns_x[1]
    assert tuple(1 if B(k,a)>B(k,xx) else -1 for k in range(4))==pattern
for yy in [v,cap,top]:
    assert tuple(1 if B(k,Q(1,4))>B(k,yy) else -1 for k in range(4))==patterns_y[0]
yd=(1+s.sqrt(13))/8
assert s.simplify(B(2,s.Rational(3,4))-B(2,yd))==0
assert Q(13)>Q(18,5)**2 and Q(13)<Q(451,125)**2
assert r(1,l,Q(23,40))<0 and r(1,h,Q(72,125))>0
pmin=(1-h)*(189-183*h)/256
qmax=3*Q(23,40)*(18-25*Q(23,40))/256
assert pmin==Q(27707463,64000000)>Q(43,100)
assert qmax==Q(2001,81920)<Q(49,2000)
M=Q(43,100)/(Q(3,4)*(1-2*l))
N=Q(49,2000)/(Q(3,16)*(2*v-1))
assert M==Q(860,801) and N==Q(196,183) and M-N==Q(128,48861)>0
budget=Q(15,16)*r(2,h,cap)
assert budget==Q(96689637,16000000000)<Q(61,10000)
print('R0_MAX',r(0,l,v),'R2_MIN',r(2,l,v),'R3_MAX',r(3,h,top))
print('R1_ENDPOINTS',r(1,l,v),r(1,h,cap))
print('C_GRADIENT',s.factor(cx),s.factor(cy0),s.factor(cy1))
print('P_MIN',pmin,'Q_UPPER_WITNESS',qmax)
print('P_OVER_A_LOWER',M,'Q_OVER_MINUS_B_UPPER',N,'MARGIN',M-N)
print('PUBLIC_BUDGET_UPPER',budget)
print('STAGE335B_RECTANGULAR_R1_UNIQUE_CONSTRAINED_PARETO_EXACT_PASS')
