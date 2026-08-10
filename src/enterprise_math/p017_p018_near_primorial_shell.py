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

The sequence R_s is strictly increasing, since

    R_s/R_{s-1} = p_{J+s}/p_{J-s+1} > 1.

Therefore the first s with R_s>=k excludes every candidate with s or more
outsider replacements.  Define the replacement depth T as the largest s with
R_s<k.  Every reusable terminal radical differs from P_J by at most T outsider
replacements.

There is also an exact replacement formula.  If O is an s-subset of the first
J primes and V is an s-subset of the outsider primes, then replacing O by V
gives

    D = P_J * product(V) / product(O),

and D<k is equivalent, without division, to

    P_J * product(V) < k * product(O).

Every J-prime radical D<k has a unique pair (O,V), namely its symmetric
difference with the first-J prime set.  Thus the terminal radical shell is the
disjoint union of these finite replacement classes for 0<=s<=T.

The implementation is intentionally scale-local.  The profile needs only the
first 2J transverse primes, not the full prime list through k.  Exact candidate
generation enumerates outsiders only through the product-derived cutoff for the
current omitted base set.  This preserves the mathematical shell while making
large critical scales executable.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import is_prime
from .p017_p018_near_primorial_precision import near_primorial_adaptive_order
from .p017_p018_transverse_primorial import transverse_odd_prime_prefix


def _transverse_odd_primes_through(k: int, cutoff: int) -> tuple[int, ...]:
    """Return odd transverse primes <=min(k,cutoff) without sieving to k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    center = k * (k + 1)
    upper = min(k, cutoff)
    result: list[int] = []
    candidate = 3
    while candidate <= upper:
        if center % candidate != 0 and is_prime(candidate):
            result.append(candidate)
        candidate += 2
    return tuple(result)


def near_primorial_replacement_profile(k: int) -> dict[str, object]:
    """Return R_s and the maximal feasible outsider replacement depth T."""
    data = near_primorial_adaptive_order(k)
    j = int(data["transverse_primorial_depth"])
    if data["J_parity"] != "EVEN" or j <= 0:
        raise ValueError("replacement shell exists only for positive even J")

    # s replacements can need p_{J+s}; s<=J, so the first 2J primes suffice.
    primes = transverse_odd_prime_prefix(k, 2 * j)
    if len(primes) < j:
        raise AssertionError("J exceeds available transverse prime count")
    base_primes = tuple(int(p) for p in primes[:j])
    base = prod(base_primes)
    if base >= k:
        raise AssertionError("P_J must fit below k")

    rows: list[dict[str, object]] = []
    depth = 0
    previous = 0
    for replacements in range(0, j + 1):
        if replacements == 0:
            minimum = base
            outsiders: tuple[int, ...] = ()
            kept = base_primes
        else:
            if j + replacements > len(primes):
                break
            kept = base_primes[: j - replacements]
            outsiders = tuple(int(p) for p in primes[j : j + replacements])
            minimum = prod(kept) * prod(outsiders)
        feasible = minimum < k
        if minimum <= previous:
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

    blocking_prime = None
    one_more = transverse_odd_prime_prefix(k, j + 1)
    if len(one_more) > j:
        blocking_prime = int(one_more[j])

    return {
        **data,
        "base_primorial_primes": base_primes,
        "base_primorial_product": base,
        "blocking_prime": blocking_prime,
        "replacement_rows": tuple(rows),
        "replacement_depth": depth,
        "first_forbidden_replacement_count": depth + 1,
    }


def near_primorial_radical_candidates(k: int) -> dict[str, object]:
    """Enumerate the exact J-prime D<k shell through local replacement cutoffs."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    depth = int(profile["replacement_depth"])
    base_primes = tuple(int(p) for p in profile["base_primorial_primes"])
    base = int(profile["base_primorial_product"])
    largest_base = base_primes[-1]

    rows: list[dict[str, object]] = []
    for replacements in range(0, depth + 1):
        if replacements == 0:
            rows.append(
                {
                    "radical": base,
                    "radical_primes": base_primes,
                    "replacements": 0,
                    "omitted_base_primes": (),
                    "outside_primes": (),
                }
            )
            continue

        for omitted in combinations(base_primes, replacements):
            omitted_product = prod(omitted)
            # Every outsider is at most the product cutoff obtained by setting
            # all other outsider factors to one.  Generate only to this local
            # bound, then enforce the exact joint-product inequality below.
            outsider_cutoff = (k * omitted_product - 1) // base
            eligible = tuple(
                p
                for p in _transverse_odd_primes_through(k, outsider_cutoff)
                if p > largest_base
            )
            if len(eligible) < replacements:
                continue
            for outside in combinations(eligible, replacements):
                outside_product = prod(outside)
                if base * outside_product >= k * omitted_product:
                    continue
                omitted_set = set(omitted)
                kept = tuple(p for p in base_primes if p not in omitted_set)
                radical_primes = tuple(sorted((*kept, *outside)))
                radical = prod(radical_primes)
                if radical >= k or len(radical_primes) != j:
                    raise AssertionError("replacement formula produced an invalid terminal radical")
                rows.append(
                    {
                        "radical": radical,
                        "radical_primes": radical_primes,
                        "replacements": replacements,
                        "omitted_base_primes": tuple(omitted),
                        "outside_primes": tuple(outside),
                    }
                )

    rows.sort(key=lambda row: int(row["radical"]))
    radicals = tuple(int(row["radical"]) for row in rows)
    if len(set(radicals)) != len(radicals):
        raise AssertionError("replacement formula produced duplicate terminal radicals")

    by_depth: dict[int, int] = {}
    for row in rows:
        count = int(row["replacements"])
        by_depth[count] = by_depth.get(count, 0) + 1

    return {
        **profile,
        "candidate_rows": tuple(rows),
        "candidate_radicals": radicals,
        "candidate_count": len(rows),
        "candidate_count_by_replacement_depth": tuple(sorted(by_depth.items())),
    }


def _squarefree_prime_factors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    remaining = value
    factors: list[int] = []
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            remaining //= candidate
            if remaining % candidate == 0:
                raise ValueError("radical must be squarefree")
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def terminal_radical_replacement_count(k: int, radical: int) -> dict[str, object]:
    """Classify one J-prime reusable radical by outsiders beyond the first J primes."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    if isinstance(radical, bool) or not isinstance(radical, int) or not (1 <= radical <= k - 1):
        raise ValueError("radical must satisfy 1<=D<=k-1")

    factors = _squarefree_prime_factors(radical)
    center = k * (k + 1)
    if len(factors) != j:
        raise ValueError("terminal radical must have exactly J distinct primes")
    if any(p == 2 or p > k or center % p == 0 or not is_prime(p) for p in factors):
        raise ValueError("terminal radical primes must be odd transverse primes <=k")

    first = set(int(p) for p in profile["base_primorial_primes"])
    outsider_count = sum(prime not in first for prime in factors)
    if outsider_count > int(profile["replacement_depth"]):
        raise AssertionError("terminal radical exceeded the near-primorial replacement depth")

    return {
        **profile,
        "radical": radical,
        "radical_primes": factors,
        "outsider_count": outsider_count,
        "within_replacement_depth": True,
    }
