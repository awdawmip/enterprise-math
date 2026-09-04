"""Five-step lexicographic Pareto certificate for post-#1161 AGM resources.

First, an analytic lower bound proves that four exact outer AGM steps cannot
produce a 256-bit completion bracket, regardless of inner return depth:

    exact bracket width D_n > s_n^2,
    s_0 > 1/6,
    s_{n+1} >= s_n^2/4,

so D_4 > 16/24^32 > 2^-156.

Thus at least five outer steps are required for either a 256-bit-width target or
a common 256-bit dyadic cell.  Conditional on this minimal outer count, the same
B=640 outward interval compiler is used to prove global inner-depth optima:

- width <2^-256:      (50,18,8,3,1), depth sum 80, state cost 1980;
- common 256-bit cell: (51,18,8,3,1), depth sum 81, state cost 2004.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, isqrt


BITS = 640
SCALE = 1 << BITS
STEPS = 5
TARGET = 256


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo < 0 or self.lo > self.hi:
            raise ValueError("bad interval")


def mul_i(x: I, y: I) -> I:
    return I(x.lo * y.lo // SCALE, ceil_div(x.hi * y.hi, SCALE))


def div_i(x: I, y: I) -> I:
    if y.lo <= 0:
        raise ValueError("positive denominator required")
    return I(x.lo * SCALE // y.hi, ceil_div(x.hi * SCALE, y.lo))


def half_i(x: I) -> I:
    return I(x.lo // 2, ceil_div(x.hi, 2))


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def f_interval(shape: I, depth: int) -> I:
    sl, su = shape.lo, shape.hi
    pow_lo = pow_hi = SCALE
    lo = hi = 0
    for k in range(1, depth + 1):
        pow_lo = pow_lo * sl // SCALE
        pow_lo = pow_lo * sl // SCALE
        pow_hi = ceil_div(pow_hi * su, SCALE)
        pow_hi = ceil_div(pow_hi * su, SCALE)
        num = catalan(k - 1)
        den = 1 << (2 * k - 1)
        lo += num * pow_lo // den
        hi += ceil_div(num * pow_hi, den)
    pow_hi = ceil_div(pow_hi * su, SCALE)
    pow_hi = ceil_div(pow_hi * su, SCALE)
    return I(lo, min(SCALE, hi + pow_hi))


def update(a: I, b: I, A: I, P: int, depth: int) -> tuple[I, I, I, int]:
    H = I(a.lo + b.lo, a.hi + b.hi)
    U = I(max(0, a.lo - b.hi), max(0, a.hi - b.lo))
    shape = div_i(U, H)
    F = f_interval(shape, depth)
    a2 = half_i(H)
    b2 = half_i(mul_i(H, I(SCALE - F.hi, SCALE - F.lo)))
    U2 = mul_i(U, U)
    A2 = I(A.lo - P * U2.hi, A.hi - P * U2.lo)
    if A2.lo <= 0:
        raise AssertionError("A lost positivity")
    return a2, b2, A2, 2 * P


def bracket(a: I, b: I, A: I, P: int) -> tuple[Fraction, Fraction]:
    lower = Fraction(4 * a.lo * b.lo, SCALE * A.hi)
    u_hi = max(0, a.hi - b.lo)
    den = A.lo * SCALE - 2 * P * u_hi * u_hi
    if den <= 0:
        raise AssertionError("bad upper denominator")
    upper = Fraction((a.hi + b.hi) ** 2, den)
    return lower, upper


def evaluate(schedule: list[int]) -> tuple[int, int]:
    if len(schedule) != STEPS or any(n < 1 for n in schedule):
        raise ValueError("five positive depths required")
    a = I(SCALE, SCALE)
    root_target = 1 << (2 * BITS - 1)
    k = isqrt(root_target)
    b = I(k, k + 1)
    A = I(SCALE, SCALE)
    P = 1
    for depth in schedule:
        a, b, A, P = update(a, b, A, P, depth)
    lo, hi = bracket(a, b, A, P)

    width = hi - lo
    width_exp = -1
    for p in range(700):
        if not width < Fraction(1, 1 << p):
            width_exp = p - 1
            break

    common = -1
    for p in range(700):
        lcell = lo.numerator * (1 << p) // lo.denominator
        ucell = hi.numerator * (1 << p) // hi.denominator
        if lcell != ucell:
            break
        common = p
    return common, width_exp


def minimal_coordinate(coordinate: int, cap: int, metric: int) -> int:
    lo, hi = 1, cap
    base = [cap] * STEPS
    while lo < hi:
        mid = (lo + hi) // 2
        trial = base.copy()
        trial[coordinate] = mid
        if evaluate(trial)[metric] >= TARGET:
            hi = mid
        else:
            lo = mid + 1
    return lo


def state_cost(schedule: list[int]) -> int:
    return sum(24 * n + 12 for n in schedule)


def run() -> dict[str, object]:
    # Analytic four-step impossibility: s4^2 > 16/24^32 > 2^-156,
    # while the exact completion-bracket width is > s4^2.
    four_step_lower = Fraction(16, 24**32)
    if not four_step_lower > Fraction(1, 1 << 156):
        raise AssertionError("four-step analytic lower bound weakened")
    if not Fraction(1, 1 << 156) > Fraction(1, 1 << TARGET):
        raise AssertionError("target comparison failed")

    # Width target: under hypothetical depth sum <=79, each coordinate <=79.
    # Maximizing the other four depths to 79 yields necessary coordinate minima.
    width_lower = [minimal_coordinate(i, 79, 1) for i in range(STEPS)]
    if width_lower != [50, 18, 7, 3, 1]:
        raise AssertionError("five-step width lower bounds changed")
    if sum(width_lower) != 79:
        raise AssertionError("width lower-bound sum changed")
    width_boundary = evaluate(width_lower)
    if width_boundary[1] >= TARGET:
        raise AssertionError("depth-sum 79 boundary unexpectedly feasible")

    width_opt = [50, 18, 8, 3, 1]
    width_result = evaluate(width_opt)
    if width_result[1] < TARGET:
        raise AssertionError("five-step width optimum lost target")

    # Common-cell target: under hypothetical sum <=80, each coordinate <=80.
    common_lower = [minimal_coordinate(i, 80, 0) for i in range(STEPS)]
    if common_lower != [51, 18, 8, 3, 1]:
        raise AssertionError("five-step common-cell lower bounds changed")
    if sum(common_lower) != 81:
        raise AssertionError("common lower-bound sum changed")
    common_result = evaluate(common_lower)
    if common_result[0] < TARGET:
        raise AssertionError("five-step common optimum lost target")

    return {
        "analytic_four_step_width_lower_bound": "16/24^32 > 2^-156",
        "minimum_outer_steps_for_256_bit_bracket": 5,
        "width_coordinate_lower_bounds_under_sum79": width_lower,
        "sum79_boundary_result_common_width": list(width_boundary),
        "width_opt_schedule": width_opt,
        "width_opt_depth_sum": sum(width_opt),
        "width_opt_s4_state_cost": state_cost(width_opt),
        "width_opt_result_common_width": list(width_result),
        "common_coordinate_lower_bounds_under_sum80": common_lower,
        "common_opt_schedule": common_lower,
        "common_opt_depth_sum": sum(common_lower),
        "common_opt_s4_state_cost": state_cost(common_lower),
        "common_opt_result_common_width": list(common_result),
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "analytic_four_step_width_lower_bound": "16/24^32 > 2^-156",
        "minimum_outer_steps_for_256_bit_bracket": 5,
        "width_coordinate_lower_bounds_under_sum79": [50, 18, 7, 3, 1],
        "sum79_boundary_result_common_width": [255, 255],
        "width_opt_schedule": [50, 18, 8, 3, 1],
        "width_opt_depth_sum": 80,
        "width_opt_s4_state_cost": 1980,
        "width_opt_result_common_width": [255, 257],
        "common_coordinate_lower_bounds_under_sum80": [51, 18, 8, 3, 1],
        "common_opt_schedule": [51, 18, 8, 3, 1],
        "common_opt_depth_sum": 81,
        "common_opt_s4_state_cost": 2004,
        "common_opt_result_common_width": [261, 262],
    }
    if result != expected:
        raise SystemExit(f"unexpected five-step Pareto output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
