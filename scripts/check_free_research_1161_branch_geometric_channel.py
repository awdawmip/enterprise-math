"""Finite branch-return certificate for the first #1161 geometric channel.

The target b_1 is NOT computed with sqrt(a*b) or a fourth-root call.
The only square-root input is the already-native seed line length sqrt(2),
enclosed by integer isqrt.  The lower channel is then reconstructed from
finite balanced-return polynomials and rational bisection.

At branch depth N=10 the resulting rigorous interval for the true b_1 lies in
one common 54-bit binary cell.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, isqrt


def sqrt_bounds(q: Fraction, bits: int) -> tuple[Fraction, Fraction]:
    if q < 0:
        raise ValueError("q must be nonnegative")
    scale = 1 << bits
    scaled_num = q.numerator * scale * scale
    den = q.denominator
    k = isqrt(scaled_num // den)
    lo = Fraction(k, scale)
    hi = lo if k * k * den == scaled_num else Fraction(k + 1, scale)
    if not (lo * lo <= q <= hi * hi):
        raise AssertionError("sqrt enclosure failed")
    return lo, hi


def coeff(k: int) -> Fraction:
    return Fraction(comb(2 * k, k) ** 2, 16**k)


def green_poly(t: Fraction, depth: int) -> Fraction:
    t2 = t * t
    power = Fraction(1)
    total = Fraction(0)
    for k in range(depth + 1):
        total += coeff(k) * power
        power *= t2
    return total


def contrast_root_bounds(s: Fraction, depth: int, iterations: int) -> tuple[Fraction, Fraction]:
    """Bracket the unique t with (1+t)G_N(t)=G_N(s)."""
    target = green_poly(s, depth)
    lo = Fraction(0)
    hi = s
    for _ in range(iterations):
        mid = (lo + hi) / 2
        value = (1 + mid) * green_poly(mid, depth)
        if value < target:
            lo = mid
        else:
            hi = mid
    return lo, hi


def binary_common_cell(lo: Fraction, hi: Fraction, max_bits: int = 256) -> tuple[int, int]:
    best_bits = 0
    best_cell = 0
    for bits in range(1, max_bits + 1):
        scale = 1 << bits
        left = (lo.numerator * scale) // lo.denominator
        right = (hi.numerator * scale) // hi.denominator
        if left != right:
            break
        best_bits = bits
        best_cell = left
    return best_bits, best_cell


def run(seed_bits: int = 256, depth: int = 10, bisection_steps: int = 220) -> dict[str, object]:
    # Native seed line-length enclosure only: sqrt(2).
    root2_lo, root2_hi = sqrt_bounds(Fraction(2), seed_bits)

    # s0=3-2sqrt(2), H0=1+1/sqrt(2), with outward rational bounds.
    s_lo = 3 - 2 * root2_hi
    s_hi = 3 - 2 * root2_lo
    h_lo = 1 + Fraction(1, 1) / root2_hi
    h_hi = 1 + Fraction(1, 1) / root2_lo

    if not (Fraction(0) < s_lo <= s_hi < Fraction(1, 4)):
        raise AssertionError("seed contrast bounds escaped the proved branch-RG domain")

    # t_N(s) is increasing in s.  Bracket it using rational bisection only.
    t_lo, _ = contrast_root_bounds(s_lo, depth, bisection_steps)
    _, t_hi = contrast_root_bounds(s_hi, depth, bisection_steps)

    # B_N=(H/2)*(1-t)/(1+t).  Outward interval, allowing independent H/t bounds.
    ratio_lo = (1 - t_hi) / (1 + t_hi)
    ratio_hi = (1 - t_lo) / (1 + t_lo)
    bN_lo = h_lo * ratio_lo / 2
    bN_hi = h_hi * ratio_hi / 2

    # Proven theorem: 0 < B_N - b_exact <= H*s^(2N+2)/(1-s^2).
    tail_hi = h_hi * s_hi ** (2 * depth + 2) / (1 - s_hi * s_hi)
    exact_lo = bN_lo - tail_hi
    exact_hi = bN_hi

    if exact_lo <= 0 or exact_lo >= exact_hi:
        raise AssertionError("invalid exact lower-channel bracket")

    common_bits, common_cell = binary_common_cell(exact_lo, exact_hi)
    width = exact_hi - exact_lo

    return {
        "branch_depth": depth,
        "seed_sqrt_only": True,
        "direct_geometric_sqrt_used": False,
        "common_binary_bits": common_bits,
        "common_binary_cell": common_cell,
        "interval_width_lt_2^-54": width < Fraction(1, 1 << 54),
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "branch_depth": 10,
        "seed_sqrt_only": True,
        "direct_geometric_sqrt_used": False,
        "common_binary_bits": 54,
        "common_binary_cell": 15148384199492731,
        "interval_width_lt_2^-54": True,
    }
    if result != expected:
        raise SystemExit(f"unexpected finite branch-channel output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
