"""Exact quotient-root state decomposition from the coalescence horizon.

For one fixed positive integer state ``n`` and root exponent ``r>=1``, define

    phi(d) = R_r(floor(n/d)),   1<=d<=n.

The graded coalescence law gives the state-specific collision horizon

    H = H_r(n) = R_{r+1}(r*n - 1).

Put

    D = D_r(n) = floor(n/(H+1)^r).

Then the denominator axis splits exactly:

* ``1<=d<=D`` gives ``phi(d)>H`` and these high roots are pairwise distinct;
* ``d>D`` gives ``phi(d)<=H``.

The low branch is even more rigid.  Every root ``1<=t<=H-1`` is guaranteed to
occur.  Indeed ``t+1<=H`` gives

    t*(t+1)^r <= (H-1)*H^r < H^(r+1) <= r*n-1.

Classical Bernoulli gives ``(t+1)^r-t^r >= r*t^(r-1)``, hence

    n/t^r - n/(t+1)^r > 1,

so the exact denominator fiber is nonempty.  Only the final low root ``t=H``
may be absent.

Consequently the number ``N_r(n)`` of distinct positive quotient-root states
has the almost-closed exact formula

    N_r(n) = D + H - 1 + epsilon,               H>=1,

where ``epsilon`` is 1 exactly when the horizon fiber is nonempty.  For the
single exceptional ``H=0`` case the count is simply ``D``.

Equivalently,

    N_r(n) in {D+H-1, D+H}.

Thus the state count can be computed from two integer-root/division scales and
one boundary-fiber test; enumerating the states themselves costs only ``O(D+H)``
outputs rather than scanning all ``d<=n``.

Since ``H~(r*n)^(1/(r+1))`` and ``D~n/H^r``, the count is
``Theta(n^(1/(r+1)))``.  Balancing ``H+n/H^r`` gives the continuous leading
upper coefficient ``(r+1) r^{-r/(r+1)}``.  At ``r=1`` this is the classical
``2*sqrt(n)`` quotient-block scale; higher r give the exact root-compressed
analogue.  The implementation stays integer-only.
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


def horizon_fiber_present(n: int, root_exp: int) -> bool:
    """Return whether the only optional low root t=H_r(n) is realized."""
    horizon = state_coalescence_horizon(n, root_exp)
    if horizon == 0:
        return False
    return exact_root_fiber_capacity(n, root_exp, horizon) > 0


def exact_distinct_root_state_count(n: int, root_exp: int) -> dict[str, int | bool]:
    """Compute N_r(n) from H,D and one horizon-fiber bit.

    No denominator scan and no loop over all low root states is required.
    """
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")

    horizon = state_coalescence_horizon(n, root_exp)
    high_denominator_max = n // (horizon + 1) ** root_exp
    if horizon == 0:
        count = high_denominator_max
        epsilon = False
    else:
        epsilon = horizon_fiber_present(n, root_exp)
        count = high_denominator_max + horizon - 1 + int(epsilon)
    return {
        "n": n,
        "root_exp": root_exp,
        "horizon": horizon,
        "high_denominator_max": high_denominator_max,
        "horizon_fiber_present": epsilon,
        "distinct_root_count": count,
    }


def quotient_root_state_decomposition(n: int, root_exp: int) -> dict[str, object]:
    """Return the exact high-singleton / contiguous-low state decomposition."""
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")

    closed_count = exact_distinct_root_state_count(n, root_exp)
    horizon = int(closed_count["horizon"])
    high_denominator_max = int(closed_count["high_denominator_max"])
    high_denominators = tuple(range(1, high_denominator_max + 1))
    high_roots = tuple(
        integer_nth_root(n // divisor, root_exp)
        for divisor in high_denominators
    )
    if any(root <= horizon for root in high_roots):
        raise AssertionError("high denominator branch fell below its root horizon")
    if len(high_roots) != len(set(high_roots)):
        raise AssertionError("high quotient-root branch is not injective")

    if horizon == 0:
        low_roots: tuple[int, ...] = ()
    else:
        guaranteed_low = tuple(range(1, horizon))
        for target in guaranteed_low:
            if exact_root_fiber_capacity(n, root_exp, target) <= 0:
                raise AssertionError("guaranteed low root fiber is empty")
        low_roots = guaranteed_low + (
            (horizon,) if bool(closed_count["horizon_fiber_present"]) else ()
        )

    if set(high_roots).intersection(low_roots):
        raise AssertionError("high and low root branches overlap")

    distinct_roots = tuple(sorted((*low_roots, *high_roots)))
    exact_count = len(distinct_roots)
    if exact_count != closed_count["distinct_root_count"]:
        raise AssertionError("enumerated root states disagree with closed count")
    upper_bound = high_denominator_max + horizon
    lower_bound = high_denominator_max + max(0, horizon - 1)
    if not lower_bound <= exact_count <= upper_bound:
        raise AssertionError("root-state count left the two-point H+D band")

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
        "horizon_fiber_present": bool(closed_count["horizon_fiber_present"]),
        "distinct_root_count": exact_count,
        "state_count_lower_bound": lower_bound,
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
