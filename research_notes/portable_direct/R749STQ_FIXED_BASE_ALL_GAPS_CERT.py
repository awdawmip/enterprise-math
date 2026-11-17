#!/usr/bin/env python3
"""R749STQ exact Fraction/SymPy certificate for a five-source scalar observer."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp

W = (1, 1, 2, 3, 6)
k = sp.Symbol("k", integer=True, nonnegative=True)
LIMIT = 73 + 6 * 10
part = [0] * (LIMIT + 1)
part[0] = 1
for weight in W:
    for index in range(weight, LIMIT + 1):
        part[index] += part[index - weight]
C = [0] * (LIMIT + 1)
T = [0] * (LIMIT + 1)
for n in range(1, LIMIT + 1):
    C[n] = C[n - 1] + part[n - 1]
    T[n] = T[n - 1] + C[n - 1]

Pc = sp.factor(sp.interpolate([(i, C[73 + 6*i]) for i in range(6)], k))
Pt = sp.factor(sp.interpolate([(i, T[73 + 6*i]) for i in range(7)], k))
assert all(sp.expand(Pc.subs(k, i)) == C[73 + 6*i] for i in range(6, 11))
assert all(sp.expand(Pt.subs(k, i)) == T[73 + 6*i] for i in range(7, 11))
assert Pc == (k+13)*(k+14)*(54*k**3 + 2097*k**2 + 27103*k + 116595)/30
assert Pt == (k+12)*(k+13)*(k+14)*(216*k**3 + 8532*k**2 + 112161*k + 490715)/120

def S(n):
    return 18*n**4 + 54*n**3 - 345*n**2 + 2070*n - 16315

def Y(index, e, d):
    n = 73 + 6*index
    return n**3 * (Pt.subs(k, index)+e)/(Pc.subs(k, index)+d) - S(n)*sp.Rational(1,108)

def D(index, e, d):
    return sp.cancel(Y(index,e,d) - Y(index+1,e,d))

def positive_poly(name, expr):
    numer, denom = sp.fraction(sp.cancel(expr))
    nc = [int(x) for x in sp.Poly(numer,k).all_coeffs()]
    dc = [int(x) for x in sp.Poly(denom,k).all_coeffs()]
    assert all(x > 0 for x in nc), (name, "numerator", nc)
    assert all(x > 0 for x in dc), (name, "denominator", dc)
    return {"numerator_degree":len(nc)-1, "denominator_degree":len(dc)-1,
            "numerator_coefficients_high_to_low":nc,
            "denominator_coefficients_high_to_low":dc}

n = 73 + 6*k
c0, c1 = Pc, Pc.subs(k,k+1)
t0, t1 = Pt, Pt.subs(k,k+1)
# These conservative bounds apply simultaneously on the entire [-2,2]^2.
a = sp.cancel(n**3/(c0+2) - (n+6)**3/(c1-2))
b = sp.cancel(n**3*(t0-2)/(c0+2)**2 - (n+6)**3*(t1+2)/(c1-2)**2)
cert_a = positive_poly("positive_partial_e_D", a)
cert_b = positive_poly("positive_negative_partial_d_D", b)
cert_tail = positive_poly("Dmax_strictly_decreases",
                          sp.cancel(D(k,2,-2)-D(k+1,2,-2)))

def exact(z):
    z = sp.cancel(z)
    assert z.is_Rational
    return Q(int(z.p),int(z.q))

d73min = exact(D(0,-2,2))
def delta(h):
    return d73min - exact(D(h,2,-2))
d20, d21 = delta(20), delta(21)
assert d20 == Q(-191487918321907500088582,11634459400665158622199815)
assert d21 == Q(80015723664272810907563,15593573618164568131752840)
assert d20 < 0 < d21
assert all(delta(h) < 0 for h in range(1,21))
assert all(delta(h) > 0 for h in range(21,75))
# The second extremum of H is positive for every positive gap.
assert exact(D(0,2,-2)) > exact(D(1,2,-2))

out = {
  "unit":"R749STQ",
  "evidence":"AUTHOR_EXACT_NOT_REVIEWED",
  "frozen_science_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "weights":list(W),
  "q":73, "p":"73+6h, integer h>=1",
  "statistic":"H_h=D_73(e,d)-D_(73+6h)(E,D)",
  "nuisance":"(e,d,E,D) real in [-2,2]^4, each pair fixed across both initial reads",
  "C_73_plus_6k":str(Pc), "T_73_plus_6k":str(Pt),
  "positive_polynomial_certificates":{
       "e_monotonicity":cert_a,"d_monotonicity":cert_b,
       "six_step_tail_monotonicity":cert_tail},
  "delta20":str(d20),"delta21":str(d21),
  "critical_h":21,"critical_p":199,
  "uniform_h_ge_21":"H_h>=delta21>0",
  "noise_per_original_read":"eta < delta21/4 = "+str(d21/4),
  "h_le_20":"H_h crosses zero; does not prove two-vector collision",
  "coverage":"all integers h>=1; all real nuisance quadruples in [-2,2]^4",
  "next":"Full two-vector separation for h<=20; minimum noise margins; provenance-preserving BRC/Port/Cell lifts"
}
path = Path(__file__).with_name("R749STQ_FIXED_BASE_ALL_GAPS_RESULTS.json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n", encoding="utf-8")
print("PASS: R749STQ exact polynomials, 40 positive numerator coefficients, exact threshold h=21")
print("delta20 =",d20,"delta21 =",d21)
