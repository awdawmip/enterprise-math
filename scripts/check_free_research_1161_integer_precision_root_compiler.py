"""Integer precision-root compiler checks for free research #1161.

This is a task-local checker, not a new global tool family.  It reuses the same
natural-number floor-root semantics as EnterpriseMath.IntegerRoot.root.

For x=p/q>0 and precision m, define

    rho_m(x) = floor(2**m * sqrt(x)).

Then

    rho_m(p/q) = isqrt(floor(p * 2**(2m) / q)),

and rho_{m+1}//2 = rho_m, with one binary precision detail bit.
The standard first Gauss--Legendre root-depth value b_1=2**(-1/4) has

    floor(2**m * b_1) = fourth_root(2**(4m-1)),  m>=1,

where fourth_root is two composed integer square roots.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def rational_sqrt_cell(x: Fraction, bits: int) -> int:
    """Return floor(2**bits * sqrt(x)) using integer arithmetic only."""
    if x < 0:
        raise ValueError("x must be nonnegative")
    if bits < 0:
        raise ValueError("bits must be nonnegative")
    scaled_floor = (x.numerator << (2 * bits)) // x.denominator
    return isqrt(scaled_floor)


def check_rational_cell(x: Fraction, bits: int) -> int:
    """Verify the exact rational square-root cell inequalities."""
    k = rational_sqrt_cell(x, bits)
    scale2 = 1 << (2 * bits)
    # k^2 <= 2^(2m) x < (k+1)^2, denominator-cleared.
    if k * k * x.denominator > scale2 * x.numerator:
        raise AssertionError("lower cell inequality failed")
    if scale2 * x.numerator >= (k + 1) * (k + 1) * x.denominator:
        raise AssertionError("upper cell inequality failed")
    return k


def fourth_root(n: int) -> int:
    """Natural-number floor fourth root via two integer square roots."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return isqrt(isqrt(n))


def b0_cell(bits: int) -> int:
    """floor(2^m / sqrt(2)) = root_2(2^(2m-1)), m>=1."""
    if bits < 1:
        raise ValueError("bits must be at least 1")
    return isqrt(1 << (2 * bits - 1))


def b1_cell(bits: int) -> int:
    """floor(2^m * 2^(-1/4)) = root_4(2^(4m-1)), m>=1."""
    if bits < 1:
        raise ValueError("bits must be at least 1")
    return fourth_root(1 << (4 * bits - 1))


def check_nested_cells(cells: list[int]) -> None:
    """Verify exact binary projection/detail law k_{m+1}=2 k_m + eps."""
    for coarse, fine in zip(cells, cells[1:]):
        if fine // 2 != coarse:
            raise AssertionError("root precision projection failed")
        detail = fine - 2 * coarse
        if detail not in (0, 1):
            raise AssertionError("root precision detail is not binary")


def run() -> dict[str, object]:
    # Exhaustive bounded rational regression for the theorem's integer formula.
    rational_cases = 0
    for p in range(1, 41):
        for q in range(1, 41):
            x = Fraction(p, q)
            cells = [check_rational_cell(x, m) for m in range(13)]
            check_nested_cells(cells)
            rational_cases += 1

    b0 = [b0_cell(m) for m in range(1, 65)]
    b1 = [b1_cell(m) for m in range(1, 65)]
    check_nested_cells(b0)
    check_nested_cells(b1)

    # Direct exact fourth-power certificate for b1 cells.
    for m, k in enumerate(b1, start=1):
        target = 1 << (4 * m - 1)
        if not (k**4 <= target < (k + 1) ** 4):
            raise AssertionError("b1 fourth-root cell certificate failed")

    # First 32 binary precision-detail bits are deterministic finite state data.
    b1_details = "".join(str(f - 2 * c) for c, f in zip(b1, b1[1:33]))

    return {
        "rational_cases": rational_cases,
        "rational_bits_checked": 13,
        "b0_bits_checked": 64,
        "b1_bits_checked": 64,
        "b1_first_32_detail_bits": b1_details,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "rational_cases": 1600,
        "rational_bits_checked": 13,
        "b0_bits_checked": 64,
        "b1_bits_checked": 64,
        "b1_first_32_detail_bits": "10101110100010011111100110010100",
    }
    if result != expected:
        raise SystemExit(f"unexpected precision-root compiler output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
