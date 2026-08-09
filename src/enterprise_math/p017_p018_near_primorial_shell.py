"""Replacement-depth structure of the even-J near-primorial error shell.

Suppose the product-adaptive terminal order has positive even

    J=J_perp(k)

and therefore m_*=J-1.  Reusable squarefree token radicals contain exactly J
transverse odd primes and have product <k.

Let

    p_1 < p_2 < ...

be the transverse odd primes and P_J=p_1...p_J<k.  A J-prime candidate that
uses exactly s primes beyond p_J must omit exactly s primes from the first J.
Among all such candidates, the minimum product is obtained by keeping the
smallest J-s original primes and inserting the smallest s outsiders:

    R_s(k)
      = (p_1...p_{J-s}) (p_{J+1}...p_{J+s}).

Therefore

    R_s(k) >= k

excludes every candidate with s or more?  More precisely, it excludes every
candidate with exactly s outsiders; because R_s is strictly increasing once the
prime list is fixed in this replacement construction, the first failing s also
excludes all larger replacement counts.  Define the replacement depth T as the
largest s for which R_s<k.

Then every reusable terminal radical differs from the minimal primorial P_J by
at most T replacements from outside the first J primes.

This creates a third finite precision coordinate after support depth J and
product cutoff k: the near-primorial shell has bounded replacement depth before
any CRT/cofactor test is applied.
"""

from __future__ import annotations

from math import prod

from .legendre import primes_up_to
from .p017_p018_near_primorial_precision import near_primorial_adaptive_order


def _transverse_odd_primes(k: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    center = k * (k + 1)
    return tuple(
        p for p in primes_up_to(k)
        if p != 2 and center % p != 0
    )


def near_primorial_replacement_profile(k: int) -> dict[str, object]:
    """Return R_s and the maximal feasible outsider replacement depth T."""
    data = near_primorial_adaptive_order(k)
    j = int(data["transverse_primorial_depth"])
    if data["J_parity"] != "EVEN" or j <= 0:
        raise ValueError("replacement shell exists only for positive even J")

    primes = _transverse_odd_primes(k)
    if len(primes) < j:
        raise AssertionError("J exceeds available transverse prime count")
    base = prod(primes[:j])
    if base >= k:
        raise AssertionError("P_J must fit below k")

    rows: list[dict[str, object]] = []
    depth = 0
    previous = base
    for replacements in range(0, j + 1):
        if replacements == 0:
            minimum = base
            outsiders: tuple[int, ...] = ()
            kept = tuple(primes[:j])
        else:
            if j + replacements > len(primes):
                break
            kept = tuple(primes[: j - replacements])
            outsiders = tuple(primes[j : j + replacements])
            minimum = prod(kept) * prod(outsiders)
        feasible = minimum < k
        if replacements > 0 and minimum <= previous:
            # R_s need not be compared to arbitrary candidate products, but the
            # canonical minimum replacement sequence itself must strictly grow:
            # R_s/R_{s-1}=p_{J+s}/p_{J-s+1}>1.
            raise AssertionError("minimum replacement product failed to increase")
        previous = minimum
        if feasible:
            depth = replacements
        rows.append(
            {
                "replacements": replacements,
                "kept_prefix_primes": kept,
                "minimum_outside_primes": outsiders,
                "minimum_product": minimum,
                "feasible_below_k": feasible,
            }
        )
        if not feasible:
            break

    return {
        **data,
        "base_primorial_product": base,
        "replacement_rows": tuple(rows),
        "replacement_depth": depth,
        "first_forbidden_replacement_count": depth + 1,
    }


def terminal_radical_replacement_count(k: int, radical: int) -> dict[str, object]:
    """Classify one J-prime reusable radical by outsiders beyond the first J primes."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    if isinstance(radical, bool) or not isinstance(radical, int) or not (1 <= radical <= k - 1):
        raise ValueError("radical must satisfy 1<=D<=k-1")

    primes = _transverse_odd_primes(k)
    first = set(primes[:j])
    remaining = radical
    factors: list[int] = []
    for prime in primes:
        if remaining % prime == 0:
            factors.append(prime)
            remaining //= prime
            if remaining % prime == 0:
                raise ValueError("radical must be squarefree")
        if remaining == 1:
            break
    if remaining != 1 or len(factors) != j:
        raise ValueError("terminal radical must have exactly J distinct transverse primes")

    outsider_count = sum(prime not in first for prime in factors)
    if outsider_count > int(profile["replacement_depth"]):
        raise AssertionError("terminal radical exceeded the near-primorial replacement depth")

    return {
        **profile,
        "radical": radical,
        "radical_primes": tuple(factors),
        "outsider_count": outsider_count,
        "within_replacement_depth": True,
    }
