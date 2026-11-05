"""Exact rational/projective and endpoint checks for the D25 high CM branch.
Proof of positive analytic solution uses bounded origin (paired Markdown).
"""
import sympy as s
u,v,J,x,z,t=s.symbols("u v J x z t")
r2=s.sqrt(2)
j3=27*(1+8*u)**3/(u*(1-u)**3)
j4=64*(1+3*v)**3/(v*(1-v)**2)
P=lambda w:(1-s.Rational(3,2)*w)/(w*(1-w))
I=lambda q:-q/(x*(1-x))-s.diff(P(x),x)/2-P(x)**2/4
Sc=lambda f,w:s.diff(f,w,3)/s.diff(f,w)-s.Rational(3,2)*(s.diff(f,w,2)/s.diff(f,w))**2
pull=lambda f,w,q:s.diff(f,w)**2*I(q).subs(x,f)+Sc(f,w)/2
ij=(J**2-1968*J+2654208)/(4*J**2*(J-1728)**2)
assert s.cancel(pull(1728/J,J,s.Rational(5,144))-ij)==0
zu=4*u*(1-u);tv=4*v*(1-v)
assert s.cancel(pull(zu,u,s.Rational(1,18))-s.diff(j3,u)**2*ij.subs(J,j3)-Sc(j3,u)/2)==0
assert s.cancel(pull(tv,v,s.Rational(3,64))-s.diff(j4,v)**2*ij.subs(J,j4)-Sc(j4,v)/2)==0
plus_u=(1+s.sqrt(1-z))/2
plus_v=(1+s.sqrt(1-t))/2
g=j3.subs(u,plus_u);h=j4.subs(v,plus_v)
reduce=lambda q:s.simplify(s.radsimp(s.simplify(q)))
z0=s.Rational(1,2);t0=s.Rational(1,9)
tp=reduce(s.diff(g,z).subs(z,z0)/s.diff(h,t).subs(t,t0))
tpp=reduce((s.diff(g,z,2).subs(z,z0)-s.diff(h,t,2).subs(t,t0)*tp**2)/s.diff(h,t).subs(t,t0))
assert reduce(g.subs(z,z0)-(2417472+1707264*r2))==0
assert reduce(g.subs(z,z0)-h.subs(t,t0))==0
assert reduce(tp-8*r2/27)==0
assert reduce(tpp-(104-16*r2)/81)==0
L=reduce((P(t0)*tp-tpp/tp-P(z0))/2)
M2=reduce(s.Rational(3,2)*t0*s.sqrt(1-t0)/(z0*s.sqrt(1-z0)*tp))
assert reduce(L-(r2-1)/6)==0
assert reduce(M2-3*r2/4)==0
assert reduce(M2*r2-s.Rational(3,2))==0
assert reduce(1+6*L-r2)==0
assert reduce(3*tp/r2-s.Rational(8,9))==0
print("EXACT_HIGH_CM_J_PROJECTIVE_AND_WEIGHTED_JET_PASS")
