from fractions import Fraction
from math import comb
from statistics import median

# Frozen R14 paired total deltas in ms. Positive means FFT total > hybrid total.
TG32 = [
    28.129336999938914,
    18.762986000012916,
    14.390807000040695,
    37.78684600001725,
    24.782942999991064,
]
RANDOM32 = [
    8.84141799997451,
    6.3507149999963985,
    0.3281420000007529,
    -0.8326179999471606,
    0.09508099998356556,
]
ALL_FALLBACK_32 = [
    6.518245999984629,
    -1.262400999962665,
    -11.547092999990127,
    14.94078799998988,
    1.4752509999880203,
]


def sign_tail(n: int, k: int) -> Fraction:
    """Exact one-sided sign-test tail P[Bin(n,1/2) >= k]."""
    return Fraction(sum(comb(n, j) for j in range(k, n + 1)), 2**n)


def threshold(n: int, alpha: Fraction) -> int:
    for k in range(n // 2 + 1, n + 1):
        if sign_tail(n, k) <= alpha:
            return k
    raise AssertionError("no admissible threshold")


def power(n: int, k: int, p: float) -> float:
    return sum(comb(n, j) * p**j * (1 - p) ** (n - j) for j in range(k, n + 1))


# Descriptive pseudo-control only: distinct initial-condition cases, not causal pairs.
tg_minus_frozen_control = [a - b for a, b in zip(TG32, ALL_FALLBACK_32)]
r32_minus_frozen_control = [a - b for a, b in zip(RANDOM32, ALL_FALLBACK_32)]
assert all(x > 0 for x in tg_minus_frozen_control)
assert round(median(tg_minus_frozen_control), 12) == round(22.84605800002737, 12)
assert sum(x > 0 for x in r32_minus_frozen_control) == 3
assert round(median(r32_minus_frozen_control), 12) == round(2.3231719999898815, 12)
assert sign_tail(5, 5) == Fraction(1, 32)

# Complete six-order cycle for three arms A=dense, B=automatic hybrid, C=forced fallback.
PERMS = ["ABC", "BCA", "CAB", "ACB", "CBA", "BAC"]
assert len(set(PERMS)) == 6
for arm in "ABC":
    assert [sum(order[pos] == arm for order in PERMS) for pos in range(3)] == [2, 2, 2]

# Two pre-specified directional confirmatory gates use Bonferroni alpha=0.025 each:
# (1) end-to-end A-B, and (2) attribution C-B.
ALPHA = Fraction(1, 40)
EXPECTED = {
    6: (6, Fraction(1, 64)),
    12: (10, Fraction(79, 4096)),
    18: (14, Fraction(253, 16384)),
    24: (18, Fraction(190051, 16777216)),
    30: (21, Fraction(22964087, 1073741824)),
}
for n, (k, p_exact) in EXPECTED.items():
    assert threshold(n, ALPHA) == k
    assert sign_tail(n, k) == p_exact

# Preferred design: 24 three-arm blocks = four complete cycles of all six A/B/C orders.
# It has about 81% power when a directional contrast is positive with probability 0.8.
assert power(24, 18, 0.8) > 0.81
assert power(24, 18, 0.8) < 0.812

# Minimum compact design: 12 blocks = two complete six-order cycles.
assert threshold(12, ALPHA) == 10

print("R15_CHECK_PASS")
print("tg_minus_frozen_control_ms", [round(x, 6) for x in tg_minus_frozen_control])
print("tg_paired_median_minus_frozen_control_ms", round(median(tg_minus_frozen_control), 6))
print("order_cycle", PERMS)
for n in [6, 12, 18, 24, 30]:
    k = threshold(n, ALPHA)
    print("design", n, "threshold", k, "p", float(sign_tail(n, k)), "power_p0.8", round(power(n, k, 0.8), 6))
