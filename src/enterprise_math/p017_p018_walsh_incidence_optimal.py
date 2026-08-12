"""Root-pattern-L1-optimal boundary-only orientation-Walsh compiler.

There are two different notions of a minimal one-sided Walsh prime detector.
The pointwise-minimal compiler minimizes the prime-side weight h(S) itself.  For
analytic boundary estimates, however, the relevant cost is the coefficient mass
of the lower-incidence expansion.

Write a normalized one-sided detector as

    F_h(L,U)=h(L) 1_{U empty},      h(empty)=1,

on disjoint lower/upper mirror supports.  Expand the opposite-side support
weight uniquely as

    h(S)=sum_{T subseteq S} alpha(T).

After multiplying by the upper prime detector prod_p(1-u_p), the coefficient of
a selected root pattern whose lower-oriented subset is T and whose remaining
selected primes point upper is

    alpha(T) (-1)^(|V|-|T|).

Hence the complete root-pattern L1 cost at a selected support V is

    L(V)=sum_{T subseteq V} |alpha(T)|.

Let

    C_k=floor((k-1)/2)

be the exact reusable-floor cutoff from the parity/anchor-aware Walsh analysis.
For every nonempty selected set V with rad(V)<=C_k, boundary-only precision
requires the orientation-summed floor coefficient

    beta(V)=sum_{T subseteq V} (-1)^(|V|-|T|) alpha(T)

to vanish.  Since every subset of a reusable-floor set is reusable-floor too and
alpha(empty)=1, these equations recursively force

    alpha(T)=1                 whenever rad(T)<=C_k.

Therefore every normalized boundary-only detector obeys the pointwise analytic
lower bound

    L(V) >= #{T subseteq V : rad(T)<=C_k}.

The bound is attained simultaneously for every V by the unique incidence choice

    alpha_*(T)=1  if rad(T)<=C_k,
               0  otherwise.

Its support weight is therefore

    h_*(S)=#{T subseteq S : rad(T)<=C_k},

namely the number of squarefree opposite-side divisors that remain inside the
reusable-floor modulus range.  This compiler is positive because the empty
subset is always counted, and it detects the same prime side exactly.

Thus h_* is the unique simultaneous root-pattern-L1 minimizer among normalized
boundary-only detectors.  It lies between the pointwise-minimal and hard Walsh
weights:

    h_pointwise_min(S) <= h_*(S) <= 2^|S|.

On an actual prime side with opposite radical R, h_*(S) is simply

    #{d|R : d squarefree and d<=C_k}.

So divisor switching needs only the floor-relevant moduli d<=C_k, while still
preserving positivity exactly through d=1.  This is an analytic proof-precision
compiler, not a short-window distribution theorem or a Legendre proof.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import is_prime
from .p017_p018_walsh_dual_titchmarsh import walsh_prime_divisor_weight
from .p017_p018_walsh_minimal_boundary_amplifier import (
    minimal_boundary_amplifier_weight,
    reusable_floor_product_cutoff,
)


def _normalized_support(support: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in support))
    if len(set(normalized)) != len(normalized):
        raise ValueError("support must contain distinct primes")
    if any(p < 3 or p % 2 == 0 for p in normalized):
        raise ValueError("support entries must be odd integers >=3")
    return normalized


def incidence_optimal_alpha(k: int, support: tuple[int, ...]) -> int:
    """Return alpha_*(T), the unique simultaneous L1-optimal incidence coefficient."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    normalized = _normalized_support(support)
    radical = prod(normalized, start=1)
    return int(radical <= reusable_floor_product_cutoff(k))


def incidence_optimal_weight(k: int, support: tuple[int, ...]) -> int:
    """Return h_*(S)=number of reusable-floor squarefree support subsets."""
    normalized = _normalized_support(support)
    cutoff = reusable_floor_product_cutoff(k)
    values = [1]
    for prime in normalized:
        values += [value * prime for value in values if value <= cutoff // prime]
    weight = len(values)
    if weight < 1:
        raise AssertionError("incidence-optimal weight lost the empty subset")
    pointwise = minimal_boundary_amplifier_weight(k, normalized)
    hard = 2 ** len(normalized)
    if not (pointwise <= weight <= hard):
        raise AssertionError("incidence-optimal weight left the pointwise/hard Walsh interval")
    return weight


def root_pattern_l1_cost(k: int, selected_support: tuple[int, ...]) -> dict[str, object]:
    """Return the exact minimal root-pattern L1 cost on one selected support V."""
    selected = _normalized_support(selected_support)
    cost = 0
    rows: list[dict[str, object]] = []
    for size in range(len(selected) + 1):
        for subset in combinations(selected, size):
            alpha = incidence_optimal_alpha(k, tuple(subset))
            cost += abs(alpha)
            rows.append({"lower_oriented_subset": subset, "alpha": alpha})
    weight = incidence_optimal_weight(k, selected)
    if cost != weight:
        raise AssertionError("incidence-optimal L1 cost did not equal its divisor-count weight")
    return {
        "k": k,
        "selected_support": selected,
        "reusable_floor_product_cutoff": reusable_floor_product_cutoff(k),
        "minimal_root_pattern_l1_cost": cost,
        "incidence_optimal_weight": weight,
        "hard_walsh_root_pattern_l1_cost": 2 ** len(selected),
        "rows": tuple(rows),
    }


def verify_forced_low_product_incidence(k: int, selected_support: tuple[int, ...]) -> dict[str, object]:
    """Verify beta(V)=0 below the reusable-floor cutoff for alpha_*."""
    selected = _normalized_support(selected_support)
    if not selected:
        raise ValueError("selected_support must be nonempty")
    beta = 0
    for size in range(len(selected) + 1):
        for subset in combinations(selected, size):
            alpha = incidence_optimal_alpha(k, tuple(subset))
            beta += ((-1) ** (len(selected) - size)) * alpha
    radical = prod(selected)
    cutoff = reusable_floor_product_cutoff(k)
    if radical <= cutoff and beta != 0:
        raise AssertionError("forced reusable-floor incidence failed beta=0")
    return {
        "k": k,
        "selected_support": selected,
        "selected_radical": radical,
        "reusable_floor_product_cutoff": cutoff,
        "orientation_floor_coefficient_beta": beta,
        "reusable_floor_set": radical <= cutoff,
        "boundary_only": beta == 0 or radical > cutoff,
    }


def incidence_optimal_prime_weight(k: int, prime_state: int) -> dict[str, object]:
    """Return the floor-critical divisor amplifier attached to one basin prime."""
    row = walsh_prime_divisor_weight(k, prime_state)
    cutoff = reusable_floor_product_cutoff(k)
    divisors = tuple(
        int(d) for d in row["squarefree_transverse_divisors"] if int(d) <= cutoff
    )
    weight = len(divisors)
    support = tuple(int(p) for p in row["opposite_small_transverse_support"])
    if weight != incidence_optimal_weight(k, support):
        raise AssertionError("prime divisor truncation disagrees with incidence-optimal support weight")
    if 1 not in divisors or weight < 1:
        raise AssertionError("incidence-optimal prime weight lost positivity")
    return {
        **row,
        "reusable_floor_product_cutoff": cutoff,
        "incidence_optimal_squarefree_divisors": divisors,
        "incidence_optimal_prime_weight": weight,
        "positive_prime_signal": True,
    }


def incidence_optimal_profile(k: int) -> dict[str, object]:
    """Aggregate the analytically minimal divisor-switched prime detector."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    primes = tuple(n for n in range(k * k + 1, (k + 1) ** 2) if is_prime(n))
    rows = tuple(incidence_optimal_prime_weight(k, prime) for prime in primes)
    optimal = sum(int(row["incidence_optimal_prime_weight"]) for row in rows)
    hard = sum(int(row["walsh_divisor_weight"]) for row in rows)
    if (optimal > 0) != bool(primes):
        raise AssertionError("incidence-optimal detector lost prime-existence equivalence")
    return {
        "k": k,
        "reusable_floor_product_cutoff": reusable_floor_product_cutoff(k),
        "prime_states": primes,
        "hard_walsh_weighted_prime_observable": hard,
        "incidence_optimal_weighted_prime_observable": optimal,
        "incidence_optimal_to_hard_ratio": (optimal / hard) if hard else 1.0,
        "prime_exists": bool(primes),
        "positive_iff_prime_exists": (optimal > 0) == bool(primes),
        "rows": rows,
    }
