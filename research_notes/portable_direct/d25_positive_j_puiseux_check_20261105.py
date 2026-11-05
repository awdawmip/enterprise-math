"""Exact D25 high-CM Puiseux and half-integer cancellation checker."""
import sympy as s
z,t,x=s.symbols("z t x")
u=(1+s.sqrt(1-z))/2
v=(1+s.sqrt(1-t))/2
J3=27*(1+8*u)**3/(u*(1-u)**3)
J4=64*(1+3*v)**3/(v*(1-v)**2)
G=s.simplify(z**3*J3)
H=s.simplify(t**2*J4)
assert s.series(G,z,0,4).removeO()==1259712-1469664*z+317844*z**2-702*z**3
assert s.series(H,t,0,3).removeO()==65536-53248*t+2816*t**2
alpha=32*s.sqrt(3)/243
U=alpha*(1+s.Rational(7,12)*x**2-13*s.sqrt(3)/243*x**3+s.Rational(83,216)*x**4)
tx=x**3*U
curve=s.series(s.series(G,z,0,3).removeO().subs(z,x**2)*U**2-s.series(H,t,0,2).removeO().subs(t,tx),x,0,5).removeO()
assert s.simplify(curve)==0
M2=s.series(3*U/(3*U+x*s.diff(U,x))*s.sqrt(1-tx)/s.sqrt(1-x**2),x,0,5).removeO()
assert s.simplify(M2-(1+x**2/9-s.sqrt(3)*x**3/81+5*x**4/108))==0
M=s.series(s.sqrt(M2),x,0,5).removeO()
assert s.simplify(M-(1+x**2/18-s.sqrt(3)*x**3/162+7*x**4/324))==0
Fb=s.series(1+s.Rational(3,64)*tx,x,0,5).removeO()
assert s.simplify(Fb-(1+s.sqrt(3)*x**3/162))==0
assert s.simplify(s.series(M*Fb,x,0,5).removeO()-(1+x**2/18+7*x**4/324))==0
print("EXACT_PUISEUX_AND_HALF_INTEGER_CANCELLATION_PASS")
