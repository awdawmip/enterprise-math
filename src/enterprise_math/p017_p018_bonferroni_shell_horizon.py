"""Integer shell horizon for Bonferroni proof-precision defects.

Let k^2 < n < (k+1)^2 be one P017 square-basin state and let its declared
small-prime support contain c distinct primes dividing n.  For a positive odd
Bonferroni order

    m = 2h+1,

point defect is possible only when c >= m+1 = 2(h+1).  If p is the least prime
in that support, then

    p^(2(h+1)) <= n < (k+1)^2,

hence p^(h+1) < k+1.  The latter quantity is integral, so

    p^(h+1) <= k,
    p <= R_{h+1}(k).

Thus the order-(2h+1) proof-precision defect is confined to least-prime shells
at or below the exact integer root horizon R_{h+1}(k).  In particular:

* order 3 defect lies only in least-prime shells p <= R_2(k);
* order 5 defect lies only in least-prime shells p <= R_3(k).

This gives a direct bridge between combinatorial proof precision and the
integer-root scale hierarchy used by P018.  It is stronger than a real-valued
O(k^(2/(m+1))) statement because the endpoint is an exact integer root.

There is a second rigidity in the residual S<k hard core.  Let P_odd(j) denote
the product of the first j odd primes.  If

    P_odd(m+2) < k <= P_odd(m+3),

then any residual order-m defect has exactly m+2 distinct core primes in total,
and the two mirror supports split as (m+1,1) or (1,m+1).  Its total pair defect
is exactly one.  So the first scale band in which order-m residual defect can
appear has a completely rigid support shape.

These are exact arithmetic localization statements.  They do not prove that a
defect row exists, do not prove Legendre's conjecture, and do not replace the
cross-cell capacity problem.
"""

from __future__ import annotations

from math import comb

from .core import integer_nth_root
from .legendre import is_prime
from .p017_p018_bonferroni_primorial import distinct_prime_count, odd_primorial
from .p017_p018_hard_core_partition import residual_hard_core_record


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _precision_depth(order: int) -> int:
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    return (order + 1) // 2


def bonferroni_least_factor_horizon(k: int, order: int) -> dict[str, int]:
    """Return the exact least-prime shell horizon R_{(m+1)/2}(k)."""
    _require_k(k)
    depth = _precision_depth(order)
    horizon = integer_nth_root(k, depth)
    return {
        "k": k,
        "order": order,
        "root_depth": depth,
        "least_factor_horizon": horizon,
    }


def defect_shell_localization(
    k: int,
    state: int,
    support: tuple[int, ...],
    order: int,
) -> dict[str, object]:
    """Certify that any order-m defect row has least support prime <=R_h(k)."""
    _require_k(k)
    depth = _precision_depth(order)
    if isinstance(state, bool) or not isinstance(state, int):
        raise ValueError("state must be an integer")
    if not k * k < state < (k + 1) * (k + 1):
        raise ValueError("state must lie in the open k-th square basin")
    if len(set(support)) != len(support):
        raise ValueError("support primes must be distinct")
    normalized = tuple(sorted(support))
    for prime in normalized:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime < 2
            or prime > k
            or not is_prime(prime)
            or state % prime != 0
        ):
            raise ValueError("support entries must be distinct primes <=k dividing state")

    defect_possible = len(normalized) >= order + 1
    horizon = integer_nth_root(k, depth)
    result: dict[str, object] = {
        "k": k,
        "state": state,
        "order": order,
        "root_depth": depth,
        "support": normalized,
        "support_size": len(normalized),
        "least_factor_horizon": horizon,
        "defect_possible": defect_possible,
    }
    if not defect_possible:
        return result

    least = normalized[0]
    if least ** (2 * depth) > state:
        raise AssertionError("distinct support factors violated the power lower bound")
    if least**depth > k:
        raise AssertionError("Bonferroni defect escaped its exact integer-root shell horizon")
    if least > horizon:
        raise AssertionError("least support prime exceeded R_h(k)")

    return {
        **result,
        "least_support_prime": least,
        "least_factor_power": least**depth,
        "localized": True,
    }


def residual_first_defect_band_rigidity(
    k: int,
    radius: int,
    order: int,
) -> dict[str, object]:
    """Classify residual defect shape in its first odd-primorial scale band.

    The function requires P_odd(m+2) < k <= P_odd(m+3).  If either mirror side
    has positive order-m point defect, then total distinct core support is forced
    to m+2 and the side sizes are exactly (m+1,1), so total pair defect equals 1.
    """
    _require_k(k)
    _precision_depth(order)
    lower_barrier = odd_primorial(order + 2)
    upper_barrier = odd_primorial(order + 3)
    if not lower_barrier < k <= upper_barrier:
        raise ValueError("k must lie in the first residual defect band")

    data = residual_hard_core_record(k, radius)
    lower_support = distinct_prime_count(int(data["lower_core"]))
    upper_support = distinct_prime_count(int(data["upper_core"]))
    total_support = lower_support + upper_support
    lower_defect = comb(lower_support - 1, order) if lower_support > order else 0
    upper_defect = comb(upper_support - 1, order) if upper_support > order else 0
    total_defect = lower_defect + upper_defect

    if total_defect:
        if total_support != order + 2:
            raise AssertionError("first-band residual defect did not have exactly m+2 core primes")
        if sorted((lower_support, upper_support)) != [1, order + 1]:
            raise AssertionError("first-band residual defect did not have the rigid (m+1,1) split")
        if total_defect != 1:
            raise AssertionError("first-band residual pair defect is not exactly one")
        if int(data["core_product"]) < lower_barrier:
            raise AssertionError("first-band defect core product fell below P_odd(m+2)")

    return {
        **data,
        "order": order,
        "first_band_lower_barrier": lower_barrier,
        "first_band_upper_barrier": upper_barrier,
        "lower_support_size": lower_support,
        "upper_support_size": upper_support,
        "total_support_size": total_support,
        "lower_point_defect": lower_defect,
        "upper_point_defect": upper_defect,
        "total_pair_defect": total_defect,
        "rigid_first_band_defect": total_defect == 1,
    }
