"""Pure-integer two-index interval certificate for post-#1161 AGM research.

The outer index is the AGM step n.  The inner index is finite first-return depth
N.  All propagated intervals use one fixed dyadic denominator 2**B and outward
integer rounding.  No floating point, pi, elliptic integral, or runtime real
square root is used.

The only initial irrational b0=1/sqrt(2) is enclosed by integer isqrt on
2**(2B-1), reusing the project's finite precision-root semantics.

At each outer step, if s lies in [sL,sU], the completed first-return mass obeys

    F_N(sL) <= F(s) <= F_N(sU) + sU**(2N+2).

This gives outward intervals for the exact next a,b,A state.  Finally the
already-proved endogenous completion bracket is evaluated without a new root:

    4 a b / A <= Pi_* <= H^2 / (A - 2 P U^2).

The checker uses B=640, six outer steps, and a 256-bit adaptive return-depth
schedule with 96 guard bits.  The resulting Pi_* interval has width <2^-546,
shares one 544-bit dyadic cell, and shares one 162-decimal-place cell.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, comb, isqrt


BITS = 640
SCALE = 1 << BITS
TARGET_BITS = 256
GUARD_BITS = 96
OUTER_STEPS = 6


def ceil_div(a: int, b: int) -> int:
    if a < 0 or b <= 0:
        raise ValueError("ceil_div checker path expects a>=0,b>0")
    return (a + b - 1) // b


@dataclass(frozen=True)
class DyadicInterval:
    """Closed [lo/SCALE, hi/SCALE] interval with nonnegative integer endpoints."""

    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo < 0 or self.lo > self.hi:
            raise ValueError("invalid nonnegative dyadic interval")


def mul_interval(x: DyadicInterval, y: DyadicInterval) -> DyadicInterval:
    return DyadicInterval(
        x.lo * y.lo // SCALE,
        ceil_div(x.hi * y.hi, SCALE),
    )


def div_interval(x: DyadicInterval, y: DyadicInterval) -> DyadicInterval:
    if y.lo <= 0:
        raise ValueError("positive denominator interval required")
    return DyadicInterval(
        x.lo * SCALE // y.hi,
        ceil_div(x.hi * SCALE, y.lo),
    )


def half_interval(x: DyadicInterval) -> DyadicInterval:
    return DyadicInterval(x.lo // 2, ceil_div(x.hi, 2))


def catalan(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return comb(2 * n, n) // (n + 1)


def first_return_mass_interval(
    shape: DyadicInterval,
    depth: int,
) -> DyadicInterval:
    """Outward interval for completed F using F_N plus the exact tail bound."""
    if depth < 1:
        raise ValueError("depth must be positive")

    sl = shape.lo
    su = shape.hi
    pow_lo = SCALE
    pow_hi = SCALE
    f_lo = 0
    f_hi = 0

    for k in range(1, depth + 1):
        # Outward s^(2k) interval, built monotonically because s>=0.
        pow_lo = pow_lo * sl // SCALE
        pow_lo = pow_lo * sl // SCALE
        pow_hi = ceil_div(pow_hi * su, SCALE)
        pow_hi = ceil_div(pow_hi * su, SCALE)

        numerator = catalan(k - 1)
        denominator = 1 << (2 * k - 1)
        f_lo += numerator * pow_lo // denominator
        f_hi += ceil_div(numerator * pow_hi, denominator)

    # Exact theorem: 0 <= F-F_N <= s^(2N+2).  Add an outward upper power.
    pow_hi = ceil_div(pow_hi * su, SCALE)
    pow_hi = ceil_div(pow_hi * su, SCALE)
    f_hi += pow_hi

    return DyadicInterval(f_lo, min(SCALE, f_hi))


def initial_b0() -> DyadicInterval:
    """Outward cell for 1/sqrt(2) using integer floor square root only."""
    target = 1 << (2 * BITS - 1)
    k = isqrt(target)
    if not (k * k <= target < (k + 1) * (k + 1)):
        raise AssertionError("initial integer-root cell failed")
    return DyadicInterval(k, k + 1)


def required_depth(target_bits: int, outer_step: int) -> int:
    exponent_unit = 3 * (1 << outer_step) - 2
    return max(1, ceil(target_bits / (2 * exponent_unit)) - 1)


def state_cost(depth: int) -> int:
    return 24 * depth + 12


def update(
    a: DyadicInterval,
    b: DyadicInterval,
    A: DyadicInterval,
    P: int,
    depth: int,
) -> tuple[
    DyadicInterval,
    DyadicInterval,
    DyadicInterval,
    int,
    DyadicInterval,
    DyadicInterval,
]:
    """One outward exact-AGM state update via finite return mass plus tail."""
    H = DyadicInterval(a.lo + b.lo, a.hi + b.hi)
    U = DyadicInterval(max(0, a.lo - b.hi), max(0, a.hi - b.lo))
    shape = div_interval(U, H)
    F = first_return_mass_interval(shape, depth)

    one_minus_F = DyadicInterval(SCALE - F.hi, SCALE - F.lo)
    a_next = half_interval(H)
    b_next = half_interval(mul_interval(H, one_minus_F))

    U2 = mul_interval(U, U)
    A_next = DyadicInterval(A.lo - P * U2.hi, A.hi - P * U2.lo)
    if A_next.lo <= 0:
        raise AssertionError("A interval lost positive denominator")

    return a_next, b_next, A_next, 2 * P, shape, F


def pi_star_bracket(
    a: DyadicInterval,
    b: DyadicInterval,
    A: DyadicInterval,
    P: int,
) -> tuple[Fraction, Fraction]:
    """Outward bracket from 4ab/A <= Pi_* <= H^2/(A-2P U^2)."""
    lower = Fraction(4 * a.lo * b.lo, SCALE * A.hi)

    H_hi = a.hi + b.hi
    U_hi = max(0, a.hi - b.lo)
    denominator = A.lo * SCALE - 2 * P * U_hi * U_hi
    if denominator <= 0:
        raise AssertionError("completion upper denominator is nonpositive")
    upper = Fraction(H_hi * H_hi, denominator)

    if lower > upper:
        raise AssertionError("completion bracket inverted")
    return lower, upper


def common_cell(
    lower: Fraction,
    upper: Fraction,
    base: int,
    max_digits: int,
) -> tuple[int, int]:
    """Largest d such that both endpoints lie in one base^-d half-open cell."""
    best = (-1, 0)
    scale = 1
    for digits in range(max_digits + 1):
        if digits:
            scale *= base
        left = lower.numerator * scale // lower.denominator
        right = upper.numerator * scale // upper.denominator
        if left != right:
            break
        best = (digits, left)
    return best


def width_exponent(lower: Fraction, upper: Fraction, limit: int = 2000) -> int:
    """Largest p with bracket width < 2^-p."""
    width = upper - lower
    for p in range(limit + 1):
        if not width < Fraction(1, 1 << p):
            return p - 1
    return limit


def run() -> dict[str, object]:
    a = DyadicInterval(SCALE, SCALE)
    b = initial_b0()
    A = DyadicInterval(SCALE, SCALE)
    P = 1

    local_target = TARGET_BITS + GUARD_BITS
    schedule = [required_depth(local_target, n) for n in range(OUTER_STEPS)]
    expected_schedule = [175, 43, 17, 7, 3, 1]
    if schedule != expected_schedule:
        raise AssertionError("adaptive guarded schedule changed")

    bracket_width_bits = []
    state_costs = []
    for outer, depth in enumerate(schedule):
        bracket = pi_star_bracket(a, b, A, P)
        bracket_width_bits.append(width_exponent(*bracket))
        state_costs.append(state_cost(depth))

        a, b, A, P, shape, F = update(a, b, A, P, depth)
        if shape.hi > SCALE // 2:
            raise AssertionError("shape interval escaped safe AGM range")
        if F.hi > SCALE:
            raise AssertionError("return mass escaped [0,1]")

    final_bracket = pi_star_bracket(a, b, A, P)
    final_width_bits = width_exponent(*final_bracket)
    bracket_width_bits.append(final_width_bits)

    binary_digits, binary_cell = common_cell(*final_bracket, base=2, max_digits=800)
    decimal_digits, decimal_cell = common_cell(*final_bracket, base=10, max_digits=250)

    decimal_text = str(decimal_cell)
    if len(decimal_text) <= decimal_digits:
        decimal_text = "0" * (decimal_digits + 1 - len(decimal_text)) + decimal_text
    decimal_prefix = decimal_text[:-decimal_digits] + "." + decimal_text[-decimal_digits:]

    if final_width_bits < TARGET_BITS:
        raise AssertionError("whole-trajectory bracket failed target precision")
    if binary_digits < TARGET_BITS:
        raise AssertionError("whole-trajectory bracket failed common binary cell target")

    return {
        "fixed_dyadic_bits": BITS,
        "outer_steps": OUTER_STEPS,
        "return_depth_schedule": schedule,
        "s4_state_cost_schedule": state_costs,
        "pi_bracket_width_bits_after_steps_0_to_6": bracket_width_bits,
        "final_width_exponent": final_width_bits,
        "common_binary_cell_bits": binary_digits,
        "common_decimal_cell_digits": decimal_digits,
        "decimal_prefix_first_80_chars": decimal_prefix[:80],
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "fixed_dyadic_bits": 640,
        "outer_steps": 6,
        "return_depth_schedule": [175, 43, 17, 7, 3, 1],
        "s4_state_cost_schedule": [4212, 1044, 420, 180, 84, 36],
        "pi_bracket_width_bits_after_steps_0_to_6": [0, 8, 25, 61, 132, 276, 546],
        "final_width_exponent": 546,
        "common_binary_cell_bits": 544,
        "common_decimal_cell_digits": 162,
        "decimal_prefix_first_80_chars": "3.141592653589793238462643383279502884197169399375105820974944592307816406286208",
    }
    if result != expected:
        raise SystemExit(f"unexpected two-index interval output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
