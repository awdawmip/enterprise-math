"""Exact rational identities only; no prime scan or numeric campaign."""

import json
from pathlib import Path

import sympy as S

s, z, p = S.symbols("s z p")
A = (3*s-1)/(s-1)**3
B = (3*s-1)**2/(s+1)**3
L = (s+1)/(2*(1-s))
K = -s*(s-3)*(3*s-1)/(3*(s+1)**2)

def pullback(t):
    tp = S.diff(t, s)
    return (
        (1-2*t)*tp/(t*(1-t))-S.diff(t, s, 2)/tp,
        -S.Rational(2, 9)*tp**2/(t*(1-t)),
    )

PA, QA = pullback(A)
PB, QB = pullback(B)
PB_display = (3*s**3+9*s**2-23*s+3)/(s*(s-3)*(s+1)*(3*s-1))
QB_display = -2/(s*(s+1)**2)
checks = []

def exact(name, expression):
    residual = S.factor(S.cancel(expression))
    assert residual == 0, (name, residual)
    checks.append({"name": name, "residual": str(residual)})

def cm(name, expression):
    numerator = S.together(expression).as_numer_denom()[0]
    residual = S.factor(S.rem(numerator, s*s-6*s+1, s))
    assert residual == 0, (name, residual)
    checks.append({"name": name, "residual": str(residual)})

exact("A_prime", S.diff(A, s)+6*s/(s-1)**4)
exact("B_prime", S.diff(B, s)+3*(s-3)*(3*s-1)/(s+1)**4)
exact("K_integrating_factor", K-B*(1-B)/S.diff(B, s))
exact("P_B_display", PB-PB_display)
exact("Q_B_display", QB-QB_display)
exact("gauge_P", PA-2*S.diff(L, s)/L-PB)
exact("gauge_Q", QA-PA*S.diff(L, s)/L+2*(S.diff(L, s)/L)**2-S.diff(L, s, 2)/L-QB)
exact("K_log_derivative", S.diff(K, s)/K-PB)
cm("CM_A_plus_B", A+B-1)
cm("CM_quadratic_image", 4*A*(1-A)-S.Rational(1, 2))
cm("CM_equal_derivatives", S.diff(A, s)-S.diff(B, s))
cm("CM_K_times_r", K*S.diff(B, s)-S.Rational(1, 8))
cm("CM_Frobenius_shape", s*(1-3*s)*(3-s)/(1-s*s)**2-S.Rational(1, 4))

w = 4*z*(1-z)
exact("quadratic_second_coefficient", z*(1-z)*S.diff(w, z)**2-4*w*(1-w))
exact("quadratic_first_coefficient", z*(1-z)*S.diff(w, z, 2)+(1-2*z)*S.diff(w, z)-4*(1-S.Rational(3, 2)*w))
exact("top_recurrence_multiplier", (S.Rational(2, 3)*(p-1)+S.Rational(1, 3))*(S.Rational(2, 3)*(p-1)+S.Rational(2, 3))-2*p*(2*p-1)/9)

shape = s*(s-3)*(3*s-1)/(s*s-1)**2
exact("shape_leading_pole_at_1", S.limit(shape*(s-1)**2, s, 1)+1)

report = {
    "status": "PASS_EXACT_SYMBOLIC_IDENTITIES",
    "scope": "Rational identities and CM algebra only; no prime checks",
    "check_count": len(checks),
    "checks": checks,
}
target = Path(__file__).with_name("SYMBOLIC_CHECK.json")
target.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "check_count": len(checks), "report": str(target)}))
