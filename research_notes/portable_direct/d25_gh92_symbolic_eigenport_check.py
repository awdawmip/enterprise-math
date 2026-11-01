"""GH-92 symbolic check of Lagrange derivative and target-root eigenport."""
import sympy as s
z,s0,u,u1,u2,u3,j,t,c,q=s.symbols('z s0 u u1 u2 u3 j t c q')
H=8*u1+5*u
P=u3+s.Rational(9,4)*u2+s.Rational(27,16)*u1+s.Rational(27,64)*u
Bdot=c*q*u/8
Vdot=c*q*u1/8+z*s0*P
assert s.expand(64*Vdot+40*Bdot-(c*q*H+64*z*s0*P))==0
U1=-s.Rational(5,8)*u
U2=(j-5*U1)/8
U3=-((3-9*9)*U2/4+(2-27*9)*U1/16-27*9*u/64)/(1-9)
assert s.factor(P.subs({u1:U1,u2:U2,u3:U3},simultaneous=True)+(6*j+u)/256)==0
W=8*j*t+3*(8*j+u)*s0
Wd=-s.Rational(9,4)*s0*(6*j+u)
assert s.expand((8*j+u)*Wd+s.Rational(3,4)*(6*j+u)*W-6*j*(6*j+u)*t)==0
print('PASS_GH92_SYMBOLIC_SOURCE_DERIVATIVE_AND_EIGENPORT')
