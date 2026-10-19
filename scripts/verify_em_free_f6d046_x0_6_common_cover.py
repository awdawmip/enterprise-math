#!/usr/bin/env python3
"""Exact and high-precision verifier for the EM-FREE-F6D046 X0(6) common-cover result.

The exact layer uses only fractions and a tiny rational-function implementation.
The numerical layer uses Decimal. No third-party dependency is required.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
import json
from typing import Iterable, Sequence

Q = Fraction


def _trim(c: Iterable[Fraction]) -> tuple[Fraction, ...]:
    a = list(c)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a or [Q(0)])


@dataclass(frozen=True)
class Poly:
    c: tuple[Fraction, ...]

    def __init__(self, c: Iterable[Fraction | int]):
        object.__setattr__(self, "c", _trim(Q(x) for x in c))

    @staticmethod
    def const(x: Fraction | int) -> "Poly":
        return Poly([Q(x)])

    @property
    def degree(self) -> int:
        return len(self.c) - 1

    def __add__(self, other: "Poly | Fraction | int") -> "Poly":
        o = other if isinstance(other, Poly) else Poly.const(other)
        n = max(len(self.c), len(o.c))
        return Poly([
            (self.c[i] if i < len(self.c) else 0)
            + (o.c[i] if i < len(o.c) else 0)
            for i in range(n)
        ])

    __radd__ = __add__

    def __neg__(self) -> "Poly":
        return Poly([-x for x in self.c])

    def __sub__(self, other: "Poly | Fraction | int") -> "Poly":
        return self + (-other if isinstance(other, Poly) else -Q(other))

    def __rsub__(self, other: "Poly | Fraction | int") -> "Poly":
        return (other if isinstance(other, Poly) else Poly.const(other)) - self

    def __mul__(self, other: "Poly | Fraction | int") -> "Poly":
        o = other if isinstance(other, Poly) else Poly.const(other)
        out = [Q(0)] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                out[i + j] += a * b
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n: int) -> "Poly":
        if n < 0:
            raise ValueError("negative polynomial power")
        out = Poly.const(1)
        b = self
        k = n
        while k:
            if k & 1:
                out = out * b
            b = b * b
            k >>= 1
        return out

    def derivative(self) -> "Poly":
        if self.degree == 0:
            return Poly.const(0)
        return Poly([Q(i) * self.c[i] for i in range(1, len(self.c))])

    def eval_fraction(self, x: Fraction) -> Fraction:
        out = Q(0)
        for a in reversed(self.c):
            out = out * x + a
        return out


@dataclass(frozen=True)
class RF:
    n: Poly
    d: Poly

    def __init__(self, n: "RF | Poly | Fraction | int", d: Poly | Fraction | int = 1):
        if isinstance(n, RF):
            object.__setattr__(self, "n", n.n)
            object.__setattr__(self, "d", n.d)
            return
        nn = n if isinstance(n, Poly) else Poly.const(n)
        dd = d if isinstance(d, Poly) else Poly.const(d)
        if dd == Poly.const(0):
            raise ZeroDivisionError
        object.__setattr__(self, "n", nn)
        object.__setattr__(self, "d", dd)

    @staticmethod
    def coerce(x: "RF | Poly | Fraction | int") -> "RF":
        return x if isinstance(x, RF) else RF(x)

    def __add__(self, other: "RF | Poly | Fraction | int") -> "RF":
        o = RF.coerce(other)
        return RF(self.n * o.d + o.n * self.d, self.d * o.d)

    __radd__ = __add__

    def __neg__(self) -> "RF":
        return RF(-self.n, self.d)

    def __sub__(self, other: "RF | Poly | Fraction | int") -> "RF":
        return self + (-RF.coerce(other))

    def __rsub__(self, other: "RF | Poly | Fraction | int") -> "RF":
        return RF.coerce(other) - self

    def __mul__(self, other: "RF | Poly | Fraction | int") -> "RF":
        o = RF.coerce(other)
        return RF(self.n * o.n, self.d * o.d)

    __rmul__ = __mul__

    def __truediv__(self, other: "RF | Poly | Fraction | int") -> "RF":
        o = RF.coerce(other)
        if o.n == Poly.const(0):
            raise ZeroDivisionError
        return RF(self.n * o.d, self.d * o.n)

    def __rtruediv__(self, other: "RF | Poly | Fraction | int") -> "RF":
        return RF.coerce(other) / self

    def __pow__(self, n: int) -> "RF":
        if n >= 0:
            return RF(self.n ** n, self.d ** n)
        return RF(self.d ** (-n), self.n ** (-n))

    def derivative(self) -> "RF":
        return RF(self.n.derivative() * self.d - self.n * self.d.derivative(), self.d ** 2)

    def equals(self, other: "RF | Poly | Fraction | int") -> bool:
        o = RF.coerce(other)
        return self.n * o.d == o.n * self.d

    @property
    def degree(self) -> int:
        return max(self.n.degree, self.d.degree)


T = Poly([0, 1])


def pullback_gauss(alpha: RF, a: Fraction) -> tuple[RF, RF]:
    """Pull back y'' + P(x)y' + Q(x)y=0 through x=alpha(t)."""
    ap = alpha.derivative()
    app = ap.derivative()
    p_x = (1 - 2 * alpha) / (alpha * (1 - alpha))
    q_x = -a * (1 - a) / (alpha * (1 - alpha))
    return p_x * ap - app / ap, q_x * ap**2


def gauge_rational(Pt: RF, Qt: RF, r: RF) -> tuple[RF, RF]:
    """Equation after u=r h."""
    lr = r.derivative() / r
    return Pt + 2 * lr, Qt + Pt * lr + r.derivative().derivative() / r


def gauge_log_derivatives(Pt: RF, Qt: RF, log_r_prime: RF, rpp_over_r: RF) -> tuple[RF, RF]:
    return Pt + 2 * log_r_prime, Qt + Pt * log_r_prime + rpp_over_r


def matrix_rank(A: Sequence[Sequence[Fraction]]) -> int:
    M = [[Q(x) for x in row] for row in A]
    if not M:
        return 0
    rows, cols = len(M), len(M[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if M[r][col] != 0), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        p = M[rank][col]
        M[rank] = [v / p for v in M[rank]]
        for r in range(rows):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][c] - f * M[rank][c] for c in range(cols)]
        rank += 1
    return rank


def left_fixed_nullity(mats: Sequence[Sequence[Sequence[int]]]) -> int:
    n = len(mats[0])
    equations: list[list[Fraction]] = []
    for M in mats:
        for j in range(n):
            equations.append([Q(M[i][j] - (1 if i == j else 0)) for i in range(n)])
    return n - matrix_rank(equations)


def sym2(M: Sequence[Sequence[int]]) -> list[list[int]]:
    a, b = M[0]
    c, d = M[1]
    return [
        [a*a, 2*a*b, b*b],
        [a*c, a*d+b*c, b*d],
        [c*c, 2*c*d, d*d],
    ]


# ---------- Exact algebra ----------
D = RF(T**2 + 12*T + 24)
alpha4 = RF(T * (T+8)**3, (T**2 + 12*T + 24)**2)
alpha3 = RF(T * (T+9)**2, (T+6)**3)

one_minus_a4_expected = RF(64*(T+9), (T**2+12*T+24)**2)
one_minus_a3_expected = RF(27*(T+8), (T+6)**3)

j4 = 64*(1+3*alpha4)**3 / (alpha4*(1-alpha4)**2)
j3 = 27*(1+8*alpha3)**3 / (alpha3*(1-alpha3)**3)
j_t = RF((T+6)**3*(T**3+18*T**2+84*T+24)**3, T*(T+8)**3*(T+9)**2)

mixed = (
    64*(1+3*alpha4)**3 * alpha3*(1-alpha3)**3
    - 27*(1+8*alpha3)**3 * alpha4*(1-alpha4)**2
)

Z4 = 4*alpha4*(1-alpha4)
Z3 = 4*alpha3*(1-alpha3)
Z4_expected = RF(256*T*(T+8)**3*(T+9), (T**2+12*T+24)**4)
Z3_expected = RF(108*T*(T+8)*(T+9)**2, (T+6)**6)

k4 = Z4 / (RF(T) * Z4.derivative())
k3 = Z3 / (RF(T) * Z3.derivative())
k4_expected = RF(-(T+8)*(T+9)*(T**2+12*T+24), 3*(T**2+8*T-8)*(T**2+16*T+72))
k3_expected = RF(-(T+6)*(T+8)*(T+9), 2*(T+12)*(T**2+6*T-18))

P4, Q4 = pullback_gauss(alpha4, Q(1,4))
P3, Q3 = pullback_gauss(alpha3, Q(1,3))
P4_expected = RF(T**4+24*T**3+204*T**2+816*T+1728, T*(T+8)*(T+9)*(T**2+12*T+24))
Q4_expected = RF(-108*(T+8), T*(T+9)*(T**2+12*T+24)**2)
P3_expected = RF(T**3+18*T**2+132*T+432, T*(T+6)*(T+8)*(T+9))
Q3_expected = RF(-24, T*(T+6)**2*(T+8))

L6_P = RF(1, T) + RF(1, T+8) + RF(1, T+9)
L6_Q = RF(T+6, T*(T+8)*(T+9))

r3 = RF(T+6, 6)
P3h, Q3h = gauge_rational(P3, Q3, r3)

Dprime = D.derivative()
log_r4_prime = Dprime/(2*D)
r4pp_over_r = Dprime.derivative()/(2*D) - Dprime**2/(4*D**2)
P4h, Q4h = gauge_log_derivatives(P4, Q4, log_r4_prime, r4pp_over_r)

q4 = D/24
q3 = RF((T+6)**2, 36)
R = 3*D/(2*(T+6)**2)

U = Poly([0,1])
t_u = RF(-2*(U**2+2*U-5), (U-1)*(U+1))
s_u = RF(-2*(U**2-4*U+1), (U-1)*(U+1))
D_u = t_u**2 + 12*t_u + 24
a4_u = RF(-(U**2+2*U-5)*(3*U**2-2*U+1)**3, (U**2-4*U+1)**4)
a3_u = RF(-(U**2+2*U-5)*(7*U**2-4*U+1)**2, 32*(U**2-U+1)**3)

alpha4_tu = t_u*(t_u+8)**3/(t_u**2+12*t_u+24)**2
alpha3_tu = t_u*(t_u+9)**2/(t_u+6)**3
R_u = 3*(t_u**2+12*t_u+24)/(2*(t_u+6)**2)
R_u_expected = RF(3*(U**2-4*U+1)**2, 8*(U**2-U+1)**2)

Tpar = [[1,1],[0,1]]
Upar = [[1,0],[-6,1]]

checks: dict[str, bool] = {}
checks["alpha4_complement"] = (1-alpha4).equals(one_minus_a4_expected)
checks["alpha3_complement"] = (1-alpha3).equals(one_minus_a3_expected)
checks["cover_degree_4"] = alpha4.degree == 4
checks["cover_degree_3"] = alpha3.degree == 3
checks["same_j_from_signature4"] = j4.equals(j_t)
checks["same_j_from_signature3"] = j3.equals(j_t)
checks["mixed_modular_relation"] = mixed.equals(0)
checks["Z4_factorization"] = Z4.equals(Z4_expected)
checks["Z3_factorization"] = Z3.equals(Z3_expected)
checks["kappa4"] = k4.equals(k4_expected)
checks["kappa3"] = k3.equals(k3_expected)
checks["pullback_P4"] = P4.equals(P4_expected)
checks["pullback_Q4"] = Q4.equals(Q4_expected)
checks["pullback_P3"] = P3.equals(P3_expected)
checks["pullback_Q3"] = Q3.equals(Q3_expected)
checks["signature3_to_L6_P"] = P3h.equals(L6_P)
checks["signature3_to_L6_Q"] = Q3h.equals(L6_Q)
checks["signature4_to_L6_P"] = P4h.equals(L6_P)
checks["signature4_to_L6_Q"] = Q4h.equals(L6_Q)
checks["squared_period_gauge"] = (q4/q3).equals(R)
checks["strict_cover_conic"] = (s_u**2).equals(D_u)
checks["strict_cover_alpha4"] = alpha4_tu.equals(a4_u)
checks["strict_cover_alpha3"] = alpha3_tu.equals(a3_u)
checks["strict_cover_degree_8"] = a4_u.degree == 8
checks["strict_cover_degree_6"] = a3_u.degree == 6
checks["strict_cover_squared_gauge"] = R_u.equals(R_u_expected)
checks["orbifold_euler_degree_balance"] = Q(4)*Q(-1,2) == Q(3)*Q(-2,3) == Q(-2)
checks["orbifold_minimal_coprime_pair"] = __import__("math").gcd(4,3) == 1
checks["rank2_no_global_fixed_covector"] = left_fixed_nullity([Tpar,Upar]) == 0
checks["sym2_no_global_fixed_covector"] = left_fixed_nullity([sym2(Tpar),sym2(Upar)]) == 0
checks["quadratic_twist_two_simple_branch_points"] = (
    (T**2+12*T+24).derivative().degree == 1
    and Q(12)**2 - 4*Q(24) == Q(48)
)

# ---------- High-precision numerical checks ----------
getcontext().prec = 110
DD = Decimal


def dsqrt(x: Decimal) -> Decimal:
    return x.sqrt()


def gauss_legendre_pi(iterations: int = 9) -> Decimal:
    a = DD(1)
    b = DD(1)/dsqrt(DD(2))
    tt = DD(1)/DD(4)
    p = DD(1)
    for _ in range(iterations):
        an = (a+b)/2
        b = dsqrt(a*b)
        tt = tt-p*(a-an)*(a-an)
        a = an
        p *= 2
    return (a+b)*(a+b)/(4*tt)


def hyp2f1(a: Decimal, b: Decimal, c: Decimal, x: Decimal, max_terms: int = 500) -> Decimal:
    term = DD(1)
    total = term
    for n in range(1, max_terms+1):
        k = DD(n-1)
        term *= (a+k)*(b+k)*x/((c+k)*DD(n))
        total += term
        if abs(term) < DD("1e-104"):
            break
    return total


def a4_dec(x: Decimal) -> Decimal:
    d = x*x+12*x+24
    return x*(x+8)**3/(d*d)


def a4p_dec(x: Decimal) -> Decimal:
    d = x*x+12*x+24
    n = x*(x+8)**3
    np = 4*(x+8)**2*(x+2)
    dp = 2*d*(2*x+12)
    return (np*d*d-n*dp)/(d**4)


def a3_dec(x: Decimal) -> Decimal:
    return x*(x+9)**2/(x+6)**3


def a3p_dec(x: Decimal) -> Decimal:
    n = x*(x+9)**2
    d = (x+6)**3
    np = 3*(x+9)*(x+3)
    dp = 3*(x+6)**2
    return (np*d-n*dp)/(d*d)


def newton(func, deriv, target: Decimal, x0: Decimal, steps: int = 20) -> Decimal:
    x = x0
    for _ in range(steps):
        x -= (func(x)-target)/deriv(x)
    return x


def h6_and_prime(x: Decimal) -> tuple[Decimal, Decimal]:
    aa = a3_dec(x)
    u3 = hyp2f1(DD(1)/3, DD(2)/3, DD(1), aa)
    u3a = (DD(2)/9)*hyp2f1(DD(4)/3, DD(5)/3, DD(2), aa)
    u3p = u3a*a3p_dec(x)
    h = 6*u3/(x+6)
    hp = 6*(u3p*(x+6)-u3)/(x+6)**2
    return h, hp


def k4_dec(x: Decimal) -> Decimal:
    d = x*x+12*x+24
    return -(x+8)*(x+9)*d/(3*(x*x+8*x-8)*(x*x+16*x+72))


def k3_dec(x: Decimal) -> Decimal:
    return -(x+6)*(x+8)*(x+9)/(2*(x+12)*(x*x+6*x-18))


def common_row(x: Decimal, which: int) -> tuple[Decimal, Decimal]:
    if which == 4:
        A = DD(2206)/DD(9801)
        B = DD(52780)/DD(9801)
        q = (x*x+12*x+24)/24
        theta_q = x*(x+6)/12
        k = k4_dec(x)
        scale = dsqrt(DD(2))
    elif which == 3:
        A = DD(827)/DD(3000)
        B = DD(14151)/DD(3000)
        q = (x+6)**2/36
        theta_q = x*(x+6)/18
        k = k3_dec(x)
        scale = DD(2)/dsqrt(DD(3))
    else:
        raise ValueError(which)
    return scale*(A*q+B*k*theta_q), scale*(B*k*q)


a4_star = DD(1)/2 - DD(910)*dsqrt(DD(29))/DD(9801)
a3_star = DD(1)/2 - DD(53)*dsqrt(DD(89))/DD(1000)
t4_star = newton(a4_dec, a4p_dec, a4_star, DD("2.93e-9"))
t3_star = newton(a3_dec, a3p_dec, a3_star, DD("-2.67e-6"))

pi = gauss_legendre_pi()
invpi = DD(1)/pi
values: dict[str, str] = {
    "t4_star": str(t4_star),
    "t3_star": str(t3_star),
    "a4_star": str(a4_star),
    "a3_star": str(a3_star),
}

for label, root, sig in (("signature4", t4_star, 4), ("signature3", t3_star, 3)):
    h, hp = h6_and_prime(root)
    S = h*h
    thetaS = 2*root*h*hp
    C0, C1 = common_row(root, sig)
    val = C0*S+C1*thetaS
    values[f"{label}_common_row_C0"] = str(C0)
    values[f"{label}_common_row_C1"] = str(C1)
    values[f"{label}_S"] = str(S)
    values[f"{label}_thetaS"] = str(thetaS)
    values[f"{label}_inverse_pi"] = str(val)
    checks[f"{label}_lifted_inverse_pi"] = abs(val-invpi) < DD("1e-90")

checks["signature4_root"] = abs(a4_dec(t4_star)-a4_star) < DD("1e-100")
checks["signature3_root"] = abs(a3_dec(t3_star)-a3_star) < DD("1e-100")

sample = DD("0.01")
u4 = hyp2f1(DD(1)/4, DD(3)/4, DD(1), a4_dec(sample))
u3 = hyp2f1(DD(1)/3, DD(2)/3, DD(1), a3_dec(sample))
G = dsqrt(DD(3)*(sample*sample+12*sample+24)/(DD(2)*(sample+6)**2))
checks["period_ratio_sample"] = abs(u4/u3-G) < DD("1e-98")
values["period_ratio_sample_residual"] = str(u4/u3-G)


def j4_dec(a: Decimal) -> Decimal:
    return 64*(1+3*a)**3/(a*(1-a)**2)


def j3_dec(a: Decimal) -> Decimal:
    return 27*(1+8*a)**3/(a*(1-a)**3)


j4s = j4_dec(a4_star)
j3s = j3_dec(a3_star)
checks["specific_basepoints_distinct_j"] = j4s > 0 and j3s < 0 and j4s != j3s
values["j_signature4_basepoint"] = str(j4s)
values["j_signature3_basepoint"] = str(j3s)
values["inverse_pi_reference"] = str(invpi)

result = {
    "schema": "EM_FREE_F6D046_X0_6_COMMON_COVER_VERIFICATION_V1",
    "researcher_id": "EM-FREE-F6D046",
    "research_unit": "EM-FREE-F6D046-R3-X0-6-COMMON-COVER-HOLONOMY",
    "all_passed": all(checks.values()),
    "check_count": len(checks),
    "checks": checks,
    "values": values,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)
