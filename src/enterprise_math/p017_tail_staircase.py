"""Global order-reversing tail staircase for P017 exact full cores.

For an anchor-surviving signed mirror incidence x (lower x=+r, upper x=-r),
write M-x=d*q using the canonical full k-smooth core d.  Whenever 1<d<k,
L020 makes q a prime >k.  Exact quotient windows for distinct odd cores below k
are strictly ordered and disjoint, so tail values are globally non-reusable and
strictly decrease as the core value increases.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_cofactor_window import square_basin_smooth_tail


def exact_quotient_window(k: int, divisor: int) -> tuple[int, int]:
    """Return the raw quotient interval of divisor-multiples in the square basin."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor <= 0:
        raise ValueError("divisor must be a positive integer")
    return (k * k) // divisor + 1, (k * (k + 2)) // divisor


def odd_core_window_separation(k: int, smaller: int, larger: int) -> dict[str, int]:
    """TS01: distinct odd cores d<e<k have W_e strictly below W_d.

    Because e-d>=2 and d<k,

        k(e-d) > 2d,

    equivalently d(k+2)<ek.  Hence k(k+2)/e < k^2/d, which separates the
    integer quotient windows strictly.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >= 3")
    for name, value in (("smaller", smaller), ("larger", larger)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or value % 2 == 0:
            raise ValueError(f"{name} must be a positive odd integer")
    if not (smaller < larger < k):
        raise ValueError("require smaller < larger < k")

    small_window = exact_quotient_window(k, smaller)
    large_window = exact_quotient_window(k, larger)
    if not large_window[1] < small_window[0]:
        raise AssertionError("odd exact quotient windows failed strict reverse ordering")
    return {
        "smaller_core": smaller,
        "larger_core": larger,
        "smaller_window_min": small_window[0],
        "smaller_window_max": small_window[1],
        "larger_window_min": large_window[0],
        "larger_window_max": large_window[1],
        "integer_gap": small_window[0] - large_window[1] - 1,
    }


def small_core_tail_incidences(k: int) -> tuple[dict[str, int | str], ...]:
    """Return all anchor-surviving signed sides whose exact full core is in (1,k)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    center = k * (k + 1)
    rows: list[dict[str, int | str]] = []
    for radius in range(1, k):
        if gcd(radius, center) != 1:
            continue
        for side, signed_point, state in (
            ("lower", radius, center - radius),
            ("upper", -radius, center + radius),
        ):
            data = square_basin_smooth_tail(k, state)
            core = int(data["smooth_core"])
            tail = int(data["tail"])
            if not (1 < core < k):
                continue
            if core % 2 == 0 or gcd(core, center) != 1:
                raise AssertionError("anchor-surviving small full core must be odd and transverse")
            if tail <= k or not is_prime(tail):
                raise AssertionError("L020 small-core tail must be one prime >k")
            if state != core * tail:
                raise AssertionError("full-core/tail state reconstruction failed")
            window = exact_quotient_window(k, core)
            if not (window[0] <= tail <= window[1]):
                raise AssertionError("exact tail escaped its quotient window")
            rows.append(
                {
                    "radius": radius,
                    "side": side,
                    "signed_point": signed_point,
                    "state": state,
                    "core": core,
                    "tail_prime": tail,
                }
            )
    return tuple(rows)


def global_tail_staircase(k: int) -> dict[str, object]:
    """TS02: all small-core large-prime tails are globally distinct and anti-monotone.

    Equal cores give distinct tails because x -> (M-x)/d is injective on signed
    incidences.  Distinct odd cores have disjoint reverse-ordered quotient windows
    by TS01.  Thus every small-core side consumes one globally unique prime tail.
    """
    rows = list(small_core_tail_incidences(k))
    tails = [int(row["tail_prime"]) for row in rows]
    if len(tails) != len(set(tails)):
        raise AssertionError("large-prime tail resource was reused globally")

    by_core: dict[int, list[int]] = {}
    for row in rows:
        by_core.setdefault(int(row["core"]), []).append(int(row["tail_prime"]))
    cores = sorted(by_core)
    for i, smaller in enumerate(cores):
        for larger in cores[i + 1 :]:
            odd_core_window_separation(k, smaller, larger)
            if min(by_core[smaller]) <= max(by_core[larger]):
                raise AssertionError("tail staircase lost strict reverse ordering")

    return {
        "k": k,
        "incidences": tuple(rows),
        "incidence_count": len(rows),
        "distinct_tail_count": len(set(tails)),
        "cores": tuple(cores),
        "tails_by_core": {core: tuple(sorted(values)) for core, values in by_core.items()},
    }
