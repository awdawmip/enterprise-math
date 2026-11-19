"""Exact identities for the intermediate-stock position theorem."""
from pathlib import Path
import json
import sympy as S

t=S.symbols('t', real=True)
s=1-t
A=1-s/3-t**2/(6*s)+t**3/(30*s**2)
mid=S.factor(A.subs(t,S.Rational(1,2)))
quarter=S.factor(A.subs(t,S.Rational(1,4)))
assert mid==S.Rational(23,30)
assert quarter==S.Rational(199,270)
assert S.factor(S.Rational(21,4)*(mid-quarter))==S.Rational(7,45)
assert S.factor(quarter/mid)==S.Rational(199,207)
derivative=S.factor(S.diff(A,t))
# The displayed numerator is positive for 0<t<1/2.
assert derivative==(2*t-1)*(4*t**2-10*t+5)/(15*(t-1)**3)
low_ratio=S.sqrt(S.Rational(1,4)*S.Rational(3,4)/(S.Rational(1,2)**2))
assert low_ratio==S.sqrt(3)/2
x,z,h=S.symbols('x z h', positive=True)
g=S.integrate((h*x+z)*(1-x),(x,0,1))
g+=S.integrate(-(h*x+z)*(1+x),(x,-1,-z/h))
g+=S.integrate((h*x+z)*(1+x),(x,-z/h,0))
assert S.simplify(g-(h/3+z*z/h-z**3/(3*h*h)))==0
m,n,r=S.symbols('m n r', nonzero=True)
k=(r*(n-m),-r*n,r*m)
assert S.expand(sum(k))==0
assert S.expand(m*k[1]+n*k[2])==0
assert S.simplify(k[1]*(m/n)**2+k[2]-r*m*(n-m)/n)==0
out={'scope':'Exact identities and coefficients; analytic limit proof is in READING_POSITION.md',
     'A_half':str(mid),'A_quarter':str(quarter),
     'A_derivative':str(derivative),'quarter_to_mid_low_success_ratio':str(low_ratio),
     'quarter_to_mid_high_local_ambiguity_ratio':'199/207',
     'high_local_unique_gap_coefficient_over_pi2_a':'7/45',
     'fixed_integer_times_second_fourier_coefficient':str(r*m*(n-m)/n),
     'all_assertions_passed':True}
Path(__file__).with_name('position_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
