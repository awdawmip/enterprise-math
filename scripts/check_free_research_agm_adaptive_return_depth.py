"""Task-local resource checker for post-#1161 finite return-depth AGM RG.

For depth N>=1 let

    F_N(s)=sum_{k=1}^N f_k s^(2k),
    f_k=Catalan(k-1)/2^(2k-1),
    T_N(s)=F_N(s)/(2-F_N(s)).

On 0<s<=1/4 every finite depth already lies in the AGM quadratic universality
class: s^2/4 <= T_N(s) < (256/961)s^2 and T_N(s)/s^2 -> 1/4.
The exact shape update T satisfies

    0 <= T(s)-T_N(s) < (512/961) s^(2N+2).

The standard exact AGM orbit has the previously proved dyadic bound

    s_n < 2^(2-3*2^n).

Hence one-step inner truncation error is below

    2^(-(3*2^n-2)*(2N+2)).

For target p bits it therefore suffices to choose

    N_n(p)=max(1, ceil(p/[2(3*2^n-2)])-1).

The S4 scalar predictive state cost for return depth N is 12(2N+1)=24N+12.
"""

from __future__ import annotations

from fractions import Fraction
from math import ceil, comb


def catalan(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return comb(2 * n, n) // (n + 1)


def return_mass(n: int) -> Fraction:
    if n < 1:
        raise ValueError("n must be positive")
    return Fraction(catalan(n - 1), 2 ** (2 * n - 1))


def f_trunc(s: Fraction, depth: int) -> Fraction:
    if not Fraction(0) <= s <= Fraction(1, 4):
        raise ValueError("checker scope is 0<=s<=1/4")
    if depth < 1:
        raise ValueError("depth must be at least one")
    return sum(
        (return_mass(k) * s ** (2 * k) for k in range(1, depth + 1)),
        Fraction(0),
    )


def shape_trunc(s: Fraction, depth: int) -> Fraction:
    f = f_trunc(s, depth)
    return f / (2 - f)


def g_of_t(t: Fraction) -> Fraction:
    """s^2 as a rational function of exact AGM next-shape t."""
    return 4 * t / (1 + t) ** 2


def required_depth(target_bits: int, outer_step: int) -> int:
    if target_bits < 1 or outer_step < 0:
        raise ValueError("positive target bits and nonnegative outer step required")
    exponent_per_two_units = 3 * (1 << outer_step) - 2
    return max(1, ceil(target_bits / (2 * exponent_per_two_units)) - 1)


def state_cost(depth: int) -> int:
    if depth < 1:
        raise ValueError("depth must be positive")
    # horizon h=2N-1 gives |D_12 x Q_h|=12(h+2)=12(2N+1)
    return 24 * depth + 12


def certified_error_exponent(outer_step: int, depth: int) -> int:
    if outer_step < 0 or depth < 1:
        raise ValueError("invalid outer step/depth")
    return (3 * (1 << outer_step) - 2) * (2 * depth + 2)


def run() -> dict[str, object]:
    # Exact rational universality/error regression.
    rational_cases = 0
    inequalities_checked = 0
    for q in range(4, 65):
        for p in range(1, q // 4 + 1):
            s = Fraction(p, q)
            for depth in range(1, 9):
                t_n = shape_trunc(s, depth)

                # Every nonzero finite return depth already has the quadratic
                # coefficient bracket; the lower bound also shows depth zero
                # would be the degenerate collapse and cannot capture the class.
                if t_n < s * s / 4:
                    raise AssertionError("finite shape map fell below s^2/4")
                if not t_n < Fraction(256, 961) * s * s:
                    raise AssertionError("finite shape map lost quadratic upper bound")

                # The exact shape t is the unique small t in [0,1) with
                # g(t)=s^2, and g is increasing there.  The candidate rational
                # upper bracket therefore certifies T-T_N <= c*s^(2N+2)
                # without evaluating a square root.
                upper = t_n + Fraction(512, 961) * s ** (2 * depth + 2)
                if g_of_t(upper) < s * s:
                    raise AssertionError("shape truncation error bracket failed")
                inequalities_checked += 3
            rational_cases += 1

    # Minimal nontrivial shell is explicit.
    for q in range(4, 65):
        for p in range(1, q // 4 + 1):
            s = Fraction(p, q)
            if shape_trunc(s, 1) != s * s / (4 - s * s):
                raise AssertionError("one-shell rational RG formula failed")

    # Adaptive schedules at representative bit targets.
    targets = (64, 128, 256, 512, 1024)
    schedules: dict[int, list[tuple[int, int, int, int]]] = {}
    for bits in targets:
        rows = []
        for outer in range(9):
            depth = required_depth(bits, outer)
            exponent = certified_error_exponent(outer, depth)
            if exponent < bits:
                raise AssertionError("adaptive depth did not meet target exponent")
            if depth > 1:
                previous = certified_error_exponent(outer, depth - 1)
                if previous >= bits:
                    raise AssertionError("adaptive depth was not minimal under the dyadic bound")
            rows.append((outer, depth, state_cost(depth), exponent))
        schedules[bits] = rows

    expected_256 = [
        (0, 127, 3060, 256),
        (1, 31, 756, 256),
        (2, 12, 300, 260),
        (3, 5, 132, 264),
        (4, 2, 60, 276),
        (5, 1, 36, 376),
        (6, 1, 36, 760),
        (7, 1, 36, 1528),
        (8, 1, 36, 3064),
    ]
    if schedules[256] != expected_256:
        raise AssertionError("256-bit adaptive schedule changed")

    return {
        "rational_shape_cases": rational_cases,
        "finite_depths_per_case": 8,
        "exact_inequalities_checked": inequalities_checked,
        "minimal_nontrivial_depth": 1,
        "minimal_s4_state_cost": state_cost(1),
        "bit_targets_checked": list(targets),
        "schedule_256": schedules[256],
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "rational_shape_cases": 496,
        "finite_depths_per_case": 8,
        "exact_inequalities_checked": 11904,
        "minimal_nontrivial_depth": 1,
        "minimal_s4_state_cost": 36,
        "bit_targets_checked": [64, 128, 256, 512, 1024],
        "schedule_256": [
            (0, 127, 3060, 256),
            (1, 31, 756, 256),
            (2, 12, 300, 260),
            (3, 5, 132, 264),
            (4, 2, 60, 276),
            (5, 1, 36, 376),
            (6, 1, 36, 760),
            (7, 1, 36, 1528),
            (8, 1, 36, 3064),
        ],
    }
    if result != expected:
        raise SystemExit(f"unexpected adaptive-return output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
