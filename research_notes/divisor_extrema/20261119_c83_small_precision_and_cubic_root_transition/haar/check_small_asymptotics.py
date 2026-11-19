"""Exact algebra supporting the C83 small-covolume asymptotics.

This verifies identities, not the analytic geometry or Haar limit theorem.
"""
from fractions import Fraction as Q
import sympy as s

# Endpoint slicing: dtheta_0 dtheta_1 dtheta_2 = 1/2 dx dz dt.
x,z,t=s.symbols('x z t', real=True)
mapping=s.Matrix([x,(x+z-t)/2,z])
assert abs(mapping.jacobian([x,z,t]).det())==s.Rational(1,2)
# Integrating all slice areas and the Jacobian recovers the unit cube.
slice_total=2*(s.integrate(1-t**2/2,(t,0,1))
               +s.integrate((2-t)**2/2,(t,1,2)))
assert slice_total/2==1

# kappa_3 lower bound: 2sqrt(2) int_0^sqrt(2)(r^2/2-r^4/4) dr.
r=s.symbols('r', positive=True)
lower=2*s.sqrt(2)*s.integrate(r**2/2-r**4/4,(r,0,s.sqrt(2)))
assert lower==s.Rational(8,15)

# First-quadrant angular integral z/(1+z)^4: z=u/(1-u).
u=s.symbols('u', real=True)
quarter=s.integrate(u*(1-u),(u,0,1))
assert quarter==s.Rational(1,6)
angular=4*quarter
assert angular==s.Rational(2,3)
# coefficient a^3/(4 zeta(2))*angular, zeta(2)=pi^2/6
assert s.simplify(angular*6/4)==1

# Two independent pieces of the quartic integral establish the upper bound.
den=u**4-u**2+1
log_ratio=s.log((u*u+s.sqrt(3)*u+1)/(u*u-s.sqrt(3)*u+1))
assert s.simplify(s.diff(log_ratio,u)-2*s.sqrt(3)*(1-u*u)/den)==0
# The sum integral is arctan(u/(1-u^2)), with endpoint limit pi/2.
assert s.simplify(s.diff(s.atan(u/(1-u*u)),u)-(1+u*u)/den)==0
kappa_upper=s.Rational(4,3)+s.pi+2/s.sqrt(3)*s.log(2+s.sqrt(3))
assert float(kappa_upper)>float(lower)>0

# Primitive Siegel short-vector moment: int_disk |x|^2 = pi R^4/2.
R=s.symbols('R', positive=True)
disk_moment=2*s.pi*s.integrate(r**3,(r,0,R))
assert disk_moment==s.pi*R**4/2

print('All exact small-covolume algebra checks passed.')
print('F2(a) = a^3/pi^2 + O(a^4)')
print('F3(a) = kappa_3*a^(3/2) + O(a^3)')
print('kappa_3 lower bound =',lower)
print('kappa_3 upper bound =',kappa_upper)
print('upper bound decimal =',s.N(kappa_upper,18))
