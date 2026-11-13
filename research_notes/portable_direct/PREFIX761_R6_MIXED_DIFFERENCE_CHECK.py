#!/usr/bin/env python3
"""PREFIX-761: exact finite arithmetic certificates; no 189-row re-execution.
Source assumptions are PREFIX-757 stochastic order and PREFIX-760 exact point signs.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json

N = 189
A = sum(range(N))
B = 2 * sum(i * (i + 1) for i in range(N))
L = B + 6 * N * A
assert (A, B, L) == (17766, 4500720, 24647364)

left_radius = Q(1, 100000)
right_radius = Q(1, 200000)
left_var_lower = Q(367) - L * left_radius
left_all_q_margin = 2 * left_var_lower - Q(112)
right_var_upper = -Q(159) + L * right_radius
assert left_all_q_margin == Q(1613159, 12500) > 0
assert right_var_upper == -Q(1788159, 50000) < 0

D = Q(1) - Q(1, 4) ** 25 - Q(3, 4) ** 25
assert D == Q(281263154558295, 281474976710656) > 0

def mixed_gap_constant(r):
    return Q(r * factorial(r + 49), factorial(25)**2 * 2**(r + 50))

c1 = mixed_gap_constant(1)
c2 = mixed_gap_constant(2)
assert c1 == Q(comb(50,25), 2**51)
assert c2 == 51 * c1
assert D**2 * c1 > Q(56,1000)
assert D**2 * c2 > Q(2858,1000)

summary = {
    'schema': 'PREFIX761_R6_ANALYTIC_ARITHMETIC_CHECK_V1',
    'scientific_pin': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'scope': 'external 189-layer independent Gamma-clock auxiliary',
    'validation': 'STDLIB_EXACT_FRACTION_ARITHMETIC_AND_ANALYTIC_PROOF_ASSUMPTIONS',
    'A': A, 'B': B, 'global_delta_variance_lipschitz_L': L,
    'left_z_interval': ['0', '1/100000'],
    'left_variance_lower': str(left_var_lower),
    'left_positive_margin_for_q_ge_2': str(left_all_q_margin),
    'right_z_interval': ['49999/200000', '50001/200000'],
    'right_variance_upper': str(right_var_upper),
    'D_at_0_to_quarter': str(D),
    'mixed_raw_moment_gap_lower': {
        'r1': str(D**2 * c1),
        'r2': str(D**2 * c2)
    },
    'limit': 'Checks arithmetic and sufficient inequalities, not original 189-row recurrence or independent theorem review',
    'status': 'ALL_CHECKS_PASS'
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
