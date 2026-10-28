#!/usr/bin/env python3
"""Exact author-side certificate for D25 auxiliary X0(3) cusp/CM first-jet tradeoff.

Uses only stdlib rational arithmetic. Not a native H0/B0 or LIFT computation.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import isqrt
import json
from pathlib import Path

@dataclass(frozen=True)
class Qsqrt2:
    a: Fraction
    b: Fraction

    def __add__(self, other):
        other = into(other)
        return Qsqrt2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-into(other))

    def __rsub__(self, other):
        return into(other) - self

    def __mul__(self, other):
        other = into(other)
        return Qsqrt2(self.a * other.a + 2 * self.b * other.b,
                      self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a * self.a - 2 * self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("quadratic-field zero")
        return Qsqrt2(self.a / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * into(other).inverse()

    def __rtruediv__(self, other):
        return into(other) / self

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        out = into(1)
        base = self
        while n:
            if n & 1:
                out *= base
            base *= base
            n //= 2
        return out


def into(v):
    if isinstance(v, Qsqrt2):
        return v
    return Qsqrt2(Fraction(v), Fraction(0))


def values(h):
    # J=N/h; theta_t=(h(1+27h)/(1-27h)) d/dh.
    x = 1 + 27*h
    y = 1 + 243*h
    N = x * y**3
    Nprime = 27*y**3 + 729*x*y**2
    J = N / h
    thetaJ = (x / (1 - 27*h)) * (Nprime - J)
    return J, thetaJ


def assert_integer_s(v, expected):
    assert v == Qsqrt2(Fraction(0), Fraction(expected)), (v, expected)


def run():
    sqrt2 = Qsqrt2(Fraction(0), Fraction(1))
    hplus = (3 + 2*sqrt2) / 27
    hminus = (3 - 2*sqrt2) / 27
    Jplus, theta_plus = values(hplus)
    Jminus, theta_minus = values(hminus)
    assert Jplus + Jminus == into(2*2417472)
    assert_integer_s(Jplus-Jminus, 3414528)
    assert_integer_s(theta_plus-theta_minus, -13519872)

    dJ = 3414528
    dTheta = -13519872
    dReg = dJ + dTheta
    assert dReg == -10105344
    assert abs(dReg) == (2**9)*(3**3)*17*43
    assert_integer_s((Jplus + theta_plus)-(Jminus + theta_minus), dReg)
    assert_integer_s((Jplus + 6*theta_plus)-(Jminus + 6*theta_minus), -77704704)
    assert_integer_s((9*Jplus + 6*theta_plus)-(9*Jminus + 6*theta_minus), -50388480)
    # J=N/h, N(0)=1. thetaJ has Laurent leading term -1/h:
    # theta multiplier h+54h^2+..., so polar coefficient of A J+B thetaJ is A-B.
    assert (1 + 27*0)*(1+243*0)**3 == 1
    p = 43
    assert pow(2,(p-1)//2,p) == p-1  # s^2=2 irreducible in F_43
    assert dJ % p == 27 and dTheta % p == 16
    assert dReg % p == 0
    assert (-77704704)%p == 37

    # Universal target-prime classification is an integer-factor theorem.
    # This bounded regression cross-check is not its proof.
    target_primes = [q for q in range(5, 5000)
                     if q % 24 in (13, 19)
                     and all(q % d for d in range(2, isqrt(q) + 1))]
    assert len(target_primes) == 166
    assert [q for q in target_primes if dReg % q == 0] == [43]
    assert dReg % 13 == 11 and dReg % 19 == 15

    # Complete coefficient-pair census in F_43. This is a finite-field linear
    # identity check, not the proof of the characteristic-zero sheet formulas.
    count = 0
    for A,B in product(range(p),repeat=2):
        polar = (A-B)%p
        sheet_coeff = (A*dJ+B*dTheta)%p
        assert sheet_coeff == (27*polar)%p
        assert (sheet_coeff==0) == (polar==0)
        count += 1

    return {
      "schema":"EM_D25_AUTHOR_EXACT_AUX_FIRSTJET_CUSP_CM_NO_GO_V1",
      "scientific_source_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
      "author_status":"AUTHOR_DERIVED_AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
      "carrier":"Q[s]/(s^2-2) then F_43[s]/(s^2-2)",
      "observer":"A*J+B*theta_t(J); cusp h^-1 coefficient vs signed CM two-sheet difference",
      "J_sheet_difference_over_s":dJ,
      "thetaJ_sheet_difference_over_s":dTheta,
      "regular_sheet_difference_over_s":dReg,
      "factorization_abs_regular_sheet_difference":{"2":9,"3":3,"17":1,"43":1},
      "p":p,
      "p_mod_24":p%24,
      "j_diff_coeff_mod_p":dJ%p,
      "theta_diff_coeff_mod_p":dTheta%p,
      "s_non_square_mod_p":True,
      "mod43_exact_law":"CM_sheet_diff = 27*s*(cusp_h_minus_one_coeff) in F_43[s]/(s^2-2)",
      "coefficient_pairs_checked":count,
      "target_primes_below_5000_checked":len(target_primes),
      "cusp_regular_firstjet_exceptional_target_primes":[43],
      "cusp_regular_and_sheet_separating_simultaneously_mod43":False,
      "additional_outside_scope":"No assertion about nonlinear/higher-jet/meromorphic-normalizer bridges or native H0/B0, original W_p, JT2",
      "result":"PASS"
    }


if __name__=='__main__':
    result=run()
    out=Path(__file__).with_name("d25_cusp_regular_firstjet_source_tradeoff_p43_author_check_20261027.json")
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("result","p","coefficient_pairs_checked","mod43_exact_law")},ensure_ascii=False))
