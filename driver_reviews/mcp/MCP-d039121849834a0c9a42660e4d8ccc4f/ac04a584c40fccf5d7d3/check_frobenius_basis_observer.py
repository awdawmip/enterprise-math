"""Exact characteristic-zero coefficient identities for a finite-field paper lemma.

No primes are instantiated and no congruence campaign is run. Characteristic-p
integral existence and pole bounds are established separately in the paper.
"""
import json
from pathlib import Path
import sympy as s

X, z = s.symbols("X z")
den = (X**2 - 1)**3
aa = 4*(X+1)**2 - (3*X-1)*(X-1)**2
bb = 3*(3*X-1)*(X-1)**2
A = -(3*X-1)*aa/(9*den)
B = -(3*X-1)*(aa+3*bb)/(9*den)
C = -(aa+3*bb)/(9*den)
J = X*(X-3)*(3*X-1)/(X**2-1)**2
checks = []

def check(name, lhs, rhs):
    residual = s.cancel(lhs-rhs)
    ok = residual == 0
    checks.append({"name": name, "pass": ok, "residual": str(residual)})
    if not ok:
        raise AssertionError((name, residual))

check("derivative_numerator", s.diff(J,X)*den, X*aa+bb)
check("top_basis_cancellation", A+C+s.diff(J,X)/3, 0)
W, T, E = s.symbols("W T E")
# W=(3z-1)T+1; 1/(3z-1) is replaced by E/(3X-1).
check("polynomial_division_observer",
      -(3*X-1)/(3*den)*(aa*W/3+(aa/3+bb)*(T+E/(3*X-1))),
      A*W+B*T+C*E)
delta = s.sqrt(2)
zz, XX = 3-2*delta, 3+2*delta
check("cm_inverse", zz*XX, 1)
check("cm_A", A.subs(X,XX), -s.Rational(1,6)+delta/8)
check("cm_B", B.subs(X,XX), -s.Rational(1,6))
check("cm_C", C.subs(X,XX), s.Rational(1,6)-delta/8)
check("cm_poly_a", aa.subs(X,XX), 12*(1-3*XX))
check("cm_poly_b", bb.subs(X,XX), -12*XX*(1-3*XX))
for node, expected in [
    (1, (-s.Rational(32,9),-s.Rational(32,9),-s.Rational(16,9))),
    (-1,(s.Rational(64,9),-s.Rational(512,9),s.Rational(128,9)))
]:
    for label, value, target in zip("ABC",(A*den,B*den,C*den),expected):
        check(f"pole_numerator_{label}_{node}",s.cancel(value).subs(X,node),target)
check("node_third_A", A.subs(X,s.Rational(1,3)), 0)
check("node_third_B", B.subs(X,s.Rational(1,3)), 0)
check("node_third_C", C.subs(X,s.Rational(1,3)), s.Rational(9,8))
l0=(X-3)*(X-s.Rational(1,3))/(X*X-1)**2
l3=8*X*(X-s.Rational(1,3))/(X*X-1)**2
la=-s.Rational(8,9)*X*(X-3)/(X*X-1)**2
check("cm_interpolation_zero",12*l0.subs(X,XX),zz)
check("cm_interpolation_three",12*l3.subs(X,XX),3-zz)
check("cm_interpolation_third",12*la.subs(X,XX),zz-s.Rational(1,3))
check("cm_endpoint_ferm_quotient",(3-zz+zz-s.Rational(1,3))*s.Rational(3,8),1)
check("cm_reference_value",J.subs(X,XX),s.Rational(1,4))
report={"status":"PASS", "prime_campaign":False, "checks":checks,
        "count":len(checks), "limitations":["No all-prime LIFT identity is tested or proved.",
        "The paper uses the directed forcing/boundary theorem as an explicit input."]}
out=Path(__file__).with_name("EXACT_FROBENIUS_BASIS_OBSERVER_CHECK.json")
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"status":"PASS","count":len(checks),"prime_campaign":False}))
