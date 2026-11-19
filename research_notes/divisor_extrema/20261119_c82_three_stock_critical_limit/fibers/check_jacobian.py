"""Symbolic checks of the physical Jacobian and its smooth boundary factor."""
from fractions import Fraction
import sympy as sp

A, d = sp.symbols('A d', positive=True)
e = A-1
m = sp.Rational(7,16)*A**4*d
u = m/(1+m)
v = A*m/(1+A*m)
T = 4*u*(1-u)+5*v*(1-v)
S = 16*u*(1-u)+25*v*(1-v)
N = A/e**2+S
h = 1/e+5-4*u-5*v
D = (1+m)*(1+A*m)
log_A = sp.Rational(19,5)/A+1/e-4*u/A-5*v/A
log_d = sp.Rational(14,3)/d+1/(d-1)-(u+v)/d
assert sp.cancel(A*log_A-h+sp.Rational(1,5))==0
assert sp.cancel(sp.diff(h,A)+N/A)==0
assert sp.cancel(sp.diff(h,d)+T/d)==0
bracket=N*(sp.Rational(14,3)-u-v+d/(d-1))-(h-sp.Rational(1,5))*T
assert sp.cancel(A*d*(log_A*sp.diff(h,d)-log_d*sp.diff(h,A))-bracket)==0
R=sp.Rational(3,14)*(d-1)/D**2*((1+e**2*S/A)*((sp.Rational(14,3)-u-v)*(d-1)+d)-(e+(sp.Rational(24,5)-4*u-5*v)*e**2)*(d-1)*T/A)
assert sp.cancel(R-sp.Rational(3,14)*e**2*(d-1)**2*bracket/(A*D**2))==0
assert sp.cancel(R.subs(d,0)-1)==0
# Remove denominators before boundary substitutions.
R=sp.cancel(R)
assert sp.cancel(R.subs(A,0)-(d-1)*(17*d-14)/14)==0
numerator,denominator=sp.fraction(R)
assert denominator.subs(A,1)!=0
assert sp.cancel(sp.diff(R,d).subs(d,1)-sp.Rational(3,14)*(1+e**2*S/A).subs(d,1)/D.subs(d,1)**2)==0
# Conversion of all powers from (A,d) to the original (x,y) coordinates.
assert Fraction(44,45)+Fraction(121,15)+Fraction(80,9)==Fraction(269,15)
assert Fraction(2025,64)*Fraction(14,3)==Fraction(4725,32)
assert Fraction(4725,32)*4==Fraction(4725,8)
assert Fraction(49,256)*4**9==50176
assert Fraction(1,20)<Fraction(1,16)<Fraction(8,121)
print('Jacobian, smooth factor, boundary identities and original constants verified.')
print('Factor denominator:',sp.factor(denominator))
