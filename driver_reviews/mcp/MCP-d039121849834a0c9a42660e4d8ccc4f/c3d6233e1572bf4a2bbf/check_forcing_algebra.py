"""Exact symbolic audit only. No prime scan, fitting, or numerical campaign."""

import json
from pathlib import Path
import sympy as S

z, x, X, n, p = S.symbols("z x X n p")
u0, u1, u2 = S.symbols("u0 u1 u2")
A = (3*z-1)/(z-1)**3
B = (3*z-1)**2/(z+1)**3
L = (z+1)/(2*(1-z))
K = -z*(z-3)*(3*z-1)/(3*(z+1)**2)
QB = -2/(z*(z+1)**2)
J = X*(X-3)*(3*X-1)/(X*X-1)**2
checks = []

def exact(name, expression):
    residual = S.factor(S.cancel(expression))
    assert residual == 0, (name, residual)
    checks.append({"name": name, "residual": str(residual)})

def transformed_operator(t, gauge):
    y = gauge*u0
    yp = S.diff(gauge,z)*u0 + gauge*S.diff(t,z)*u1
    ypp = (S.diff(gauge,z,2)*u0
           + (2*S.diff(gauge,z)*S.diff(t,z)
              + gauge*S.diff(t,z,2))*u1
           + gauge*S.diff(t,z)**2*u2)
    return K*ypp + S.diff(K,z)*yp + K*QB*y

def DH_at(t):
    return t*(1-t)*u2 + (1-2*t)*u1 - S.Rational(2,9)*u0

exact("A_prime", S.diff(A,z)+6*z/(z-1)**4)
exact("B_prime", S.diff(B,z)+3*(z-3)*(3*z-1)/(z+1)**4)
exact("K_definition", K-B*(1-B)/S.diff(B,z))
exact("K_A_relation", A*(1-A)/S.diff(A,z)-2*L**2*K)
exact("K_QB", K*QB-2*(z-3)*(3*z-1)/(3*(z+1)**4))
exact("O_F_B", transformed_operator(B,S.Integer(1))-S.diff(B,z)*DH_at(B))
exact("O_LF_A", transformed_operator(A,L)-S.diff(A,z)/(2*L)*DH_at(A))

f0,f1,f2,g0,g1,g2,k0,k1,q = S.symbols("f0 f1 f2 g0 g1 g2 k0 k1 q")
Rprime = k1*(f0*g1-g0*f1)+k0*(f0*g2-g0*f2)
Of = k0*f2+k1*f1+k0*q*f0
Og = k0*g2+k1*g1+k0*q*g0
exact("Wronskian_sign", Rprime-(f0*Og-g0*Of))

DH_monomial = n**2*x**(n-1)-(n+S.Rational(1,3))*(n+S.Rational(2,3))*x**n
exact("recurrence_diagonal", (n+S.Rational(1,3))*(n+S.Rational(2,3))-(n*n+n+S.Rational(2,9)))
exact("full_top_multiplier", (p-1+S.Rational(1,3))*(p-1+S.Rational(2,3))-(p-S.Rational(2,3))*(p-S.Rational(1,3)))
exact("top_multiplier_expansion", (p-S.Rational(2,3))*(p-S.Rational(1,3))-(p*p-p+S.Rational(2,9)))
exact("A_forcing_prefactor", S.diff(A,z)/(2*L)-6*z/((z-1)**3*(z+1)))
exact("B_forcing_prefactor", L*S.diff(B,z)-3*(z-3)*(3*z-1)/(2*(z-1)*(z+1)**3))

Jpartial = 4/(X+1)-4/(X+1)**2-1/(X-1)-1/(X-1)**2
exact("J_partial_fractions", J-Jpartial)
exact("J_derivative", S.diff(J,X)+(X**2-6*X+1)*(3*X**2-2*X+3)/((X-1)**3*(X+1)**3))
exact("J_prime_at_3", S.diff(J,X).subs(X,3)-S.Rational(3,8))
exact("J_prime_at_third", S.diff(J,X).subs(X,S.Rational(1,3))+S.Rational(27,8))

T1 = 6*z*(3*X-1)/((z+1)*(3*z-1)*(X-1)**3)
T2 = 3*(z-3)*(3*X-1)**2/(2*(z+1)*(3*z-1)*(X-1)*(X+1)**2)
bracket = (3*(3*X-1)*(4*z*(X+1)**2-(z-3)*(3*X-1)*(X-1)**2)
           /(2*(z+1)*(3*z-1)*(X-1)**3*(X+1)**2))
exact("combined_forcing_after_H_transport", T1-T2-bracket)

q3, c, v3, va, eta = S.symbols("q3 c v3 va eta")
N = eta*X**3 + (c+8*v3-S.Rational(8,9)*va-S.Rational(10,3)*eta)*X**2
N += (eta-S.Rational(10,3)*c+S.Rational(8,3)*(va-v3))*X+c
exact("kernel_interpolation_at_0", N.subs(X,0)-c)
exact("kernel_interpolation_at_3", N.subs(X,3)-64*v3)
exact("kernel_interpolation_at_third", N.subs(X,S.Rational(1,3))-S.Rational(64,81)*va)
exact("kernel_leading_coefficient", S.Poly(N,X).nth(3)-eta)

report = {
    "status": "PASS_EXACT_SYMBOLIC_ALGEBRA",
    "scope": "Exact rational identities only; proofs of valuation, pole bounds and finite-field kernel are in the adjacent note",
    "prime_scan": False,
    "check_count": len(checks),
    "checks": checks,
}
target = Path(__file__).with_name("SYMBOLIC_AUDIT.json")
target.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "check_count": len(checks), "report": str(target)}))
