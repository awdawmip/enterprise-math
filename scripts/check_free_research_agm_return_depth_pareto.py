"""Global finite Pareto certificate for six-step post-#1161 return-depth schedules.

Scope is deliberately fixed:
- dyadic arithmetic carrier B=640;
- six outer AGM steps;
- every inner return depth N_i>=1;
- scalar S4 state cost sum_i (24*N_i+12);
- exact outward interval compiler used by the two-index certificate.

Two target notions are optimized:
1. final Pi_* interval width < 2^-256;
2. both final endpoints lie in one common 256-bit dyadic cell.

Using monotonicity of the positive first-return enclosure in every depth, the
checker gives coordinatewise necessary lower bounds under any hypothesized
smaller total budget, then tests the unique boundary schedule where needed.
It certifies global depth-sum optima 81 and 82 respectively.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, isqrt


BITS = 640
SCALE = 1 << BITS
OUTER_STEPS = 6
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
    one_minus_f = I(SCALE - F.hi, SCALE - F.lo)
    a2 = half_i(H)
    b2 = half_i(mul_i(H, one_minus_f))
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
        raise AssertionError("upper denominator failed")
    upper = Fraction((a.hi + b.hi) ** 2, den)
    return lower, upper


def evaluate(schedule: list[int]) -> tuple[int, int]:
    if len(schedule) != OUTER_STEPS or any(n < 1 for n in schedule):
        raise ValueError("six positive return depths required")
    a = I(SCALE, SCALE)
    target = 1 << (2 * BITS - 1)
    k = isqrt(target)
    b = I(k, k + 1)
    A = I(SCALE, SCALE)
    P = 1
    for depth in schedule:
        a, b, A, P = update(a, b, A, P, depth)
    lo, hi = bracket(a, b, A, P)

    # width exponent
    width = hi - lo
    width_exp = -1
    for p in range(700):
        if not width < Fraction(1, 1 << p):
            width_exp = p - 1
            break

    # common binary cell depth
    common = -1
    for p in range(700):
        left = lo.numerator * (1 << p) // lo.denominator
        right = hi.numerator * (1 << p) // hi.denominator
        if left != right:
            break
        common = p
    return common, width_exp


def minimal_coordinate(
    coordinate: int,
    other_cap: int,
    metric_index: int,
) -> int:
    """Least depth at coordinate with all five other depths maximized to cap."""
    lo, hi = 1, other_cap
    schedule = [other_cap] * OUTER_STEPS
    while lo < hi:
        mid = (lo + hi) // 2
        trial = schedule.copy()
        trial[coordinate] = mid
        if evaluate(trial)[metric_index] >= TARGET:
            hi = mid
        else:
            lo = mid + 1
    return lo


def total_s4_cost(schedule: list[int]) -> int:
    return sum(24 * n + 12 for n in schedule)


def run() -> dict[str, object]:
    # Width target.  Under a hypothetical total depth <=80, every coordinate is
    # itself <=80.  Maximize the other coordinates to 80 to get the most
    # favorable possible test for each candidate coordinate.  Monotonicity then
    # makes the resulting minima necessary for every <=80 schedule.
    width_lower = [minimal_coordinate(i, 80, 1) for i in range(OUTER_STEPS)]
    if width_lower != [50, 18, 7, 3, 1, 1]:
        raise AssertionError("width coordinate lower bounds changed")
    if sum(width_lower) != 80:
        raise AssertionError("width lower-bound sum changed")

    width_boundary_result = evaluate(width_lower)
    if width_boundary_result[1] >= TARGET:
        raise AssertionError("depth-sum 80 boundary unexpectedly became feasible")

    width_opt = [50, 18, 8, 3, 1, 1]
    width_opt_result = evaluate(width_opt)
    if width_opt_result[1] < TARGET:
        raise AssertionError("depth-sum 81 witness lost 256-bit width")

    # Common-cell target.  Under a hypothetical total depth <=81, every
    # coordinate <=81.  Necessary coordinate minima already sum to 82, so no
    # <=81 schedule can be feasible.
    common_lower = [minimal_coordinate(i, 81, 0) for i in range(OUTER_STEPS)]
    if common_lower != [51, 18, 8, 3, 1, 1]:
        raise AssertionError("common-cell coordinate lower bounds changed")
    if sum(common_lower) != 82:
        raise AssertionError("common-cell lower-bound sum changed")

    common_opt = common_lower
    common_opt_result = evaluate(common_opt)
    if common_opt_result[0] < TARGET:
        raise AssertionError("depth-sum 82 witness lost common 256-bit cell")

    conservative = [175, 43, 17, 7, 3, 1]

    return {
        "width_coordinate_lower_bounds_under_sum80": width_lower,
        "sum80_boundary_result_common_width": list(width_boundary_result),
        "width_opt_schedule": width_opt,
        "width_opt_depth_sum": sum(width_opt),
        "width_opt_s4_state_cost": total_s4_cost(width_opt),
        "width_opt_result_common_width": list(width_opt_result),
        "common_coordinate_lower_bounds_under_sum81": common_lower,
        "common_opt_schedule": common_opt,
        "common_opt_depth_sum": sum(common_opt),
        "common_opt_s4_state_cost": total_s4_cost(common_opt),
        "common_opt_result_common_width": list(common_opt_result),
        "conservative_depth_sum": sum(conservative),
        "conservative_s4_state_cost": total_s4_cost(conservative),
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "width_coordinate_lower_bounds_under_sum80": [50, 18, 7, 3, 1, 1],
        "sum80_boundary_result_common_width": [255, 255],
        "width_opt_schedule": [50, 18, 8, 3, 1, 1],
        "width_opt_depth_sum": 81,
        "width_opt_s4_state_cost": 2016,
        "width_opt_result_common_width": [255, 257],
        "common_coordinate_lower_bounds_under_sum81": [51, 18, 8, 3, 1, 1],
        "common_opt_schedule": [51, 18, 8, 3, 1, 1],
        "common_opt_depth_sum": 82,
        "common_opt_s4_state_cost": 2040,
        "common_opt_result_common_width": [261, 262],
        "conservative_depth_sum": 246,
        "conservative_s4_state_cost": 5976,
    }
    if result != expected:
        raise SystemExit(f"unexpected return-depth Pareto output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
