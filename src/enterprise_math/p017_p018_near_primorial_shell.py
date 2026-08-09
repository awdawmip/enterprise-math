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

This creates a third finite precision coordinate after support depth J and
product cutoff k: the near-primorial shell has bounded replacement depth before
any CRT/cofactor test is applied.
"""

from __future__ import annotations

from itertools import combinations
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
    previous = 0
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

    return {
        **data,
        "base_primorial_primes": tuple(primes[:j]),
        "base_primorial_product": base,
        "replacement_rows": tuple(rows),
        "replacement_depth": depth,
        "first_forbidden_replacement_count": depth + 1,
    }


def near_primorial_radical_candidates(k: int) -> dict[str, object]:
    """Enumerate the exact J-prime D<k shell through the replacement formula."""
    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    depth = int(profile["replacement_depth"])
    base_primes = tuple(int(p) for p in profile["base_primorial_primes"])
    base = int(profile["base_primorial_product"])
    primes = _transverse_odd_primes(k)
    outsider_primes = primes[j:]

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
            # From base*out_product < k*omitted_product, each outsider is below
            # this integer cutoff.  It makes the exact combination search small.
            outsider_cutoff = (k * omitted_product - 1) // base
            eligible = tuple(p for p in outsider_primes if p <= outsider_cutoff)
            if len(eligible) < replacements:
                continue
            for outside in combinations(eligible, replacements):
                outside_product = prod(outside)
                if base * outside_product >= k * omitted_product:
                    continue
                kept = tuple(p for p in base_primes if p not in omitted)
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
