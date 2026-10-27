from fractions import Fraction as F
from itertools import product
from json import dumps
from hashlib import sha256

P = [F(3, 8), F(1, 8)]
Q = [F(1, 8), F(3, 8)]
R = [[F(1, 3), F(2, 3)], [F(1, 2), F(1, 2)]]
Pr = [p * r for p, rr in zip(P, R) for r in rr]
Qr = [q * r for q, rr in zip(Q, R) for r in rr]
assert sum(P) == sum(Q) == sum(Pr) == sum(Qr) == F(1, 2)
assert all(v > 0 for v in P + Q + Pr + Qr)

def area(p, q):
    return sum(abs(p[i] * q[j] - p[j] * q[i])
               for i in range(len(p)) for j in range(i + 1, len(p)))

def support(p, q, a, b):
    return sum(max(F(0), a * x + b * y) for x, y in zip(p, q))

def quotient_defect(p, q, blocks, tau):
    return sum(sum(max(F(0), p[i] - tau * q[i]) for i in block)
               - max(F(0), sum(p[i] - tau * q[i] for i in block))
               for block in blocks)

for a, b in product(range(-10, 11), repeat=2):
    assert support(P, Q, a, b) == support(Pr, Qr, a, b)
assert area(P, Q) == area(Pr, Qr) == F(1, 8)
for k in range(41):
    tau = F(k, 10)
    assert quotient_defect(Pr, Qr, [[0, 1], [2, 3]], tau) == 0
assert quotient_defect(P, Q, [[0, 1]], F(1)) == F(1, 4)
xr = [F(1), F(0), F(0), F(1)]
x = [sum(r * v for r, v in zip(rr, xr[sum(map(len, R[:i])):sum(map(len, R[:i+1]))]))
     for i, rr in enumerate(R)]
assert x == [F(1, 3), F(1, 2)]
ap = sum(p * v for p, v in zip(Pr, xr))
bp = sum(q * v for q, v in zip(Qr, xr))
assert (ap, bp) == (F(3, 16), F(11, 48))
assert (ap, bp) == (sum(p * v for p, v in zip(P, x)),
                   sum(q * v for q, v in zip(Q, x)))
gain = (sum(abs(p - q) for p, q in zip(P, Q)) - abs(sum(P) - sum(Q))) / 2
assert gain == F(1, 4)
c = F(1, 8)
assert gain - c * (sum(P) + sum(Q)) == F(1, 8)
report = {
    "schema": "EM_EC48T_EXACT_V1",
    "status": "EXACT_FINITE_CHECK_OF_SPECIFIED_EXAMPLE_NOT_UNIVERSAL_PROOF",
    "source_masses_P": [str(v) for v in P],
    "source_masses_Q": [str(v) for v in Q],
    "refined_masses_P": [str(v) for v in Pr],
    "refined_masses_Q": [str(v) for v in Qr],
    "zonotope_area": str(area(P, Q)),
    "strict_illegal_merge_defect_tau_1": str(quotient_defect(P, Q, [[0, 1]], F(1))),
    "safe_merge_thresholds_checked": 41,
    "support_directions_checked": 21 * 21,
    "exact_acceptance_pair": [str(ap), str(bp)],
    "variation_gain": str(gain),
    "gain_minus_one_step_cost_c_1_8": str(gain - c * (sum(P) + sum(Q))),
    "all_assertions": "PASS"
}
print(dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
