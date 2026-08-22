"""Deterministic matching normal form for the Prime-BRC silent semiprime core.

Depends on :mod:`prime_brc_silent_core`.  For k>=10 every anchor-surviving
polarity-silent composite is already known to be a semiprime p*q with
k/2<p<=k<q.  This module sharpens the ambiguity:

* silence of q>k forces q<=2k-1;
* for one fixed p there is one *deterministic integer candidate* q_*(k,p),
  selected only by the p-carry class and parity of Q=floor(M/p);
* silent semiprimes form a partial matching between primes in (k/2,k] and
  primes in (k,2k): no p or q can occur twice.

These are ambiguity-capacity theorems, not prime-existence theorems.
"""

from __future__ import annotations

from math import gcd

from .prime_brc_phase import square_basin_frame, square_midpoint_defect
from .prime_brc_silent_core import (
    _is_prime,
    least_prime_factor,
    polarity_silent,
    silent_core_capacity,
    silent_fixed_p_certificate,
)


def deterministic_silent_candidate(k: int, p: int) -> dict[str, object]:
    """Return the unique integer q_* that can still be silent in a fixed p shell.

    The fixed-p theorem has chi_p=0, hence the two directional carry bits are
    equal.  Put c in {0,1} for that common carry bit and Q=floor(M/p).

    If c=0, there are only two p-hits, with cofactors Q,Q+1.  Exactly one has
    odd parity and can be a prime >2.

    If c=1, the four cofactors are Q-1,Q,Q+1,Q+2.  The fixed-p obstruction
    proved in ``silent_fixed_p_certificate`` eliminates one member of the only
    possible odd-prime pair.  Thus exactly one *integer* candidate remains:

      c=0: Q (Q odd), Q+1 (Q even)
      c=1: Q+2 (Q odd), Q-1 (Q even).

    Whether q_* is actually prime and silent is a separate arithmetic event.
    """
    base = silent_fixed_p_certificate(k, p)
    carry = int(base["lower_carry_bit"])
    if carry != int(base["upper_carry_bit"]):
        raise AssertionError("chi_p=0 lost complementary carry equality")
    Q = int(base["Q"])
    odd = Q % 2 == 1
    if carry == 0:
        q_star = Q if odd else Q + 1
        side = -1 if odd else 1
    elif carry == 1:
        q_star = Q + 2 if odd else Q - 1
        side = 1 if odd else -1
    else:
        raise AssertionError("silent carry class escaped {0,1}")

    frame = square_basin_frame(k)
    n = p * q_star
    if not frame["lower"] < n < frame["upper"]:
        raise AssertionError("deterministic q_* left the strict square basin")
    radius = abs(n - frame["center"])
    if (1 if n > frame["center"] else -1) != side:
        raise AssertionError("q_* side formula disagrees with the p-hit ordering")
    if q_star <= k:
        raise AssertionError("silent-core cofactor candidate failed q_*>k")

    anchor_survives = 1 <= radius < k and gcd(radius, frame["center"]) == 1
    q_is_prime = _is_prime(q_star)
    is_silent = anchor_survives and q_is_prime and polarity_silent(k, n)
    return {
        **base,
        "carry_class": carry,
        "Q_is_odd": odd,
        "q_star": q_star,
        "side": side,
        "n_star": n,
        "radius_star": radius,
        "anchor_survives": anchor_survives,
        "q_star_is_prime": q_is_prime,
        "q_star_is_silent": is_silent,
    }


def silent_matching(k: int) -> dict[str, object]:
    """Return the exact silent-core partial matching for one k>=10.

    For a silent semiprime n=p*q, q>k and chi_q=0.  Each half interval has
    length <=k+1<q+1, hence contains at most one q-multiple.  Silence therefore
    means there is one q-hit on each side, and the two hits are consecutive
    multiples of q.  Since both are strict interior integers, their separation
    gives q<=2k-1.

    If two silent semiprimes shared the same q, their p-values would be those
    two consecutive multiplier indices and hence differ by one.  But k>=10
    gives p>k/2>=5, so both p-values are odd primes and cannot differ by one.
    Together with the fixed-p theorem, the silent core is a matching.
    """
    data = silent_core_capacity(k)
    pairs: list[tuple[int, int, int, int, int]] = []
    used_p: set[int] = set()
    used_q: set[int] = set()
    for radius, side, n, p, q in data["silent_endpoints"]:
        if not (2 * p > k and p <= k < q <= 2 * k - 1):
            raise AssertionError("silent matching factor range failed")
        if p in used_p:
            raise AssertionError("silent matching reused a least prime p")
        if q in used_q:
            raise AssertionError("silent matching reused a cofactor prime q")
        candidate = deterministic_silent_candidate(k, p)
        if int(candidate["q_star"]) != q or not bool(candidate["q_star_is_silent"]):
            raise AssertionError("silent endpoint escaped its deterministic q_* branch")
        used_p.add(p)
        used_q.add(q)
        pairs.append((p, q, radius, side, n))

    lower_primes = tuple(p for p in range(k // 2 + 1, k + 1) if _is_prime(p))
    upper_primes = tuple(q for q in range(k + 1, 2 * k) if _is_prime(q))
    matching_bound = min(len(lower_primes), len(upper_primes))
    if len(pairs) > matching_bound:
        raise AssertionError("silent matching exceeded a bipartite vertex class")
    return {
        "k": k,
        "pairs": tuple(pairs),
        "matching_size": len(pairs),
        "lower_prime_vertices": lower_primes,
        "upper_prime_vertices": upper_primes,
        "matching_bound": matching_bound,
        "status": "EXACT_PARTIAL_MATCHING_NOT_PRIME_EXISTENCE",
    }


def verify_all_silent_use_q_star(k: int) -> bool:
    """Small deterministic theorem-replay helper."""
    data = silent_matching(k)
    for p, q, _radius, _side, _n in data["pairs"]:
        if deterministic_silent_candidate(k, p)["q_star"] != q:
            return False
    return True
