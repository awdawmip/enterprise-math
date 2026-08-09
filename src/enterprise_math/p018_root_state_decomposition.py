"""Exact quotient-root state decomposition from the coalescence horizon.

For one fixed positive integer state ``n`` and root exponent ``r>=1``, define

    phi(d) = R_r(floor(n/d)),   1<=d<=n.

The all-power divisor-span law implies a state-specific collision horizon

    H_r(n) = R_{r+1}(r*n - 1).

Put

    D_r(n) = floor(n/(H_r(n)+1)^r).

Then the denominator axis splits exactly:

* ``1<=d<=D_r(n)`` gives ``phi(d)>H_r(n)``; these high roots are pairwise
  distinct, because a collision above H would violate ``t^(r+1)<r*n``.
* ``d>D_r(n)`` gives ``phi(d)<=H_r(n)``.

Hence all positive quotient-root states can be enumerated without scanning all
``d<=n``.  The high part is the strictly decreasing sequence obtained from the
first ``D_r(n)`` denominator labels; the low part is the set of nonempty exact
fibers among ``t=1,...,H_r(n)``.

Writing ``N_r(n)`` for the number of distinct positive quotient-root states,

    N_r(n)
      = D_r(n)
        + #{1<=t<=H_r(n) : floor(n/t^r)>floor(n/(t+1)^r)}

and therefore

    D_r(n) <= N_r(n) <= D_r(n) + H_r(n).

The continuous balance of ``H + n/H^r`` occurs at ``H~(r*n)^(1/(r+1))``;
its coefficient is ``(r+1) r^{-r/(r+1)}``.  For r=1 this recovers the familiar
``2*sqrt(n)`` hyperbola scale; for r=2 it gives the cubic-root state scale.
The implementation below stays integer-only; the asymptotic interpretation is
research prose, not an executable floating-point dependency.
"""

from __future__ import annotations

from .core import integer_nth_root
from .p018_power_coalescence import exact_root_fiber_capacity


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def state_coalescence_horizon(n: int, root_exp: int) -> int:
    """Return H_r(n)=R_{r+1}(r*n-1) for n>=1,r>=1."""
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")
    return integer_nth_root(root_exp * n - 1, root_exp + 1)


def state_coalescence_multiplicity_cap(
    n: int, root_exp: int, target_root: int
) -> int | None:
    """Return the state-specific graded cap for t>0.

    Any positive-root denominator fiber has size at most

        1 + floor((r*n-1)/t^(r+1)).

    The root-zero terminal fiber is outside this bound and returns ``None``.
    """
    for name, value in (
        ("n", n),
        ("root_exp", root_exp),
        ("target_root", target_root),
    ):
        _require_int(name, value)
    if n < 1 or root_exp < 1 or target_root < 0:
        raise ValueError("n/root_exp positive and target_root nonnegative required")
    if target_root == 0:
        return None
    return 1 + (root_exp * n - 1) // target_root ** (root_exp + 1)


def quotient_root_state_decomposition(n: int, root_exp: int) -> dict[str, object]:
    """Return the exact high-singleton / low-compressed state decomposition."""
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")

    horizon = state_coalescence_horizon(n, root_exp)
    high_denominator_max = n // (horizon + 1) ** root_exp
    high_denominators = tuple(range(1, high_denominator_max + 1))
    high_roots = tuple(
        integer_nth_root(n // divisor, root_exp)
        for divisor in high_denominators
    )
    if any(root <= horizon for root in high_roots):
        raise AssertionError("high denominator branch fell below its root horizon")
    if len(high_roots) != len(set(high_roots)):
        raise AssertionError("high quotient-root branch is not injective")

    low_roots = tuple(
        target
        for target in range(1, horizon + 1)
        if exact_root_fiber_capacity(n, root_exp, target) > 0
    )
    if set(high_roots).intersection(low_roots):
        raise AssertionError("high and low root branches overlap")

    distinct_roots = tuple(sorted((*low_roots, *high_roots)))
    exact_count = len(distinct_roots)
    upper_bound = high_denominator_max + horizon
    if exact_count > upper_bound:
        raise AssertionError("root-state decomposition exceeded H+D bound")

    # The denominator threshold itself is exact: just below/above it roots fall
    # on opposite sides of the horizon.
    if high_denominator_max >= 1:
        last_high = integer_nth_root(n // high_denominator_max, root_exp)
        if last_high <= horizon:
            raise AssertionError("last high denominator missed the high branch")
    if high_denominator_max < n:
        first_low = integer_nth_root(n // (high_denominator_max + 1), root_exp)
        if first_low > horizon:
            raise AssertionError("first low denominator remained above horizon")

    return {
        "n": n,
        "root_exp": root_exp,
        "horizon": horizon,
        "high_denominator_max": high_denominator_max,
        "high_denominators": high_denominators,
        "high_roots": high_roots,
        "low_roots": low_roots,
        "distinct_roots": distinct_roots,
        "distinct_root_count": exact_count,
        "state_count_lower_bound": high_denominator_max,
        "state_count_upper_bound": upper_bound,
    }


def naive_positive_quotient_root_states(n: int, root_exp: int) -> tuple[int, ...]:
    """Reference-only full scan used to validate the compressed decomposition."""
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")
    return tuple(
        sorted(
            {
                integer_nth_root(n // divisor, root_exp)
                for divisor in range(1, n + 1)
            }
        )
    )
