#!/usr/bin/env python3
"""Exact E3 Picard-Fuchs certificate; no finite-prime or target-product calculation."""
import json
from pathlib import Path
import sympy as S

x,t,lam=S.symbols('x t lam')
P=4*x**3+(x+t/27)**2
R=x*(-2*t**2+108*t*x+9*t+11664*x**3+3888*x**2+243*x)/6561
# Derivatives of P^(-1/2), all written over P^(5/2).
N=t*(1-t)*(-P+3*(x+t/27)**2)/729-(1-2*t)*(x+t/27)*P/27-S.Rational(2,9)*P**2
residual=S.Poly(S.expand(S.diff(R,x)*P-S.Rational(3,2)*R*S.diff(P,x)-N),x,t)
assert residual.is_zero
# lambda=4t(1-t), L_t applied to f(lambda) is 4 L_lambda(f).
z=4*t*(1-t)
c2=t*(1-t)*S.diff(z,t)**2
c1=t*(1-t)*S.diff(z,t,2)+(1-2*t)*S.diff(z,t)
assert S.expand(c2-4*z*(1-z))==0
assert S.expand(c1-4*(1-S.Rational(3,2)*z))==0
assert -S.Rational(2,9)==4*(-S.Rational(1,18))
# Recurrence fixes the entire analytic branch; these checks audit indexing only.
q=[S.rf(S.Rational(1,3),n)*S.rf(S.Rational(2,3),n)/S.factorial(n)**2 for n in range(8)]
assert all(S.simplify((n+1)**2*q[n+1]-(n+S.Rational(1,3))*(n+S.Rational(2,3))*q[n])==0 for n in range(7))
out={'kind':'EXACT_POLYNOMIAL_CERTIFICATE','sympy_version':S.__version__,
     'P':str(P),'R':str(R),'PF_numerator_residual':str(residual.as_expr()),
     'quadratic_change_residuals':[0,0,0],'analytic_recurrence_index_checks':7,
     'failures':0,'prime_tests':0,
     'not_computed':['CM action','Katz actual comparison','kappa','D25 product digit'],
     'proof_boundary':'The residue/cycle argument and use of source CM/Ramanujan uniqueness are hand proofs; this program only verifies the exact polynomial and change-of-variable identities.'}
Path(__file__).with_name('e3_period_gauge_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
