"""P3-to-P2 bridge: cubic routing isolates the balanced triple regime.

Let U=k^2+2k.  At the minimal P3 product cutoff

    z3=floor(U^(1/4)),

any rough survivor has Omega<=3.  If it is a genuine triple-prime state

    n=a*b*c,   a<=b<=c,

then all factors exceed z3 and the least factor also satisfies

    a<=z2=floor(U^(1/3)).

Compare the P018 cubic candidate horizon

    H=floor((2k^2-1)^(1/3))+1

and define the exact low-channel threshold

    L=floor(k^2/(H+1)^2)+1.

For the quotient channel attached to the least factor a,

    j_a=floor(sqrt(floor(k^2/a))).

Then

    a<L  => j_a>H,
    a>=L => j_a<=H.

Thus the existing cubic-high injectivity regime contains every *unbalanced*
triple with least factor below L.  All remaining cubic-low ambiguity is
confined to triples with a>=L.  Since b,c>=a, those ambiguous triples satisfy

    L <= a <= b <= c <= U/L^2.

Hence every unresolved factor is on the X^(1/3) scale for X=k^2.  Asymptotically

    L ~ 2^(-2/3) k^(2/3),
    U/L^2 ~ 2^(4/3) k^(2/3).

The cubic collision zone is therefore exactly a balanced three-factor box, the
same geometry usually associated with a Type-III/trilinear analytic regime.
This theorem is a routing/localization statement only: cubic-high uniqueness
does not by itself prove that the unbalanced triple states are absent, and the
balanced box still requires new counting/cancellation input.
"""

from __future__ import annotations

from math import isqrt

from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
    square_interval_upper,
)
from .p017_p018_cubic_ambiguity_hierarchy import low_partner_core_floor
from .p017_p018_cubic_high_channel import cubic_candidate_horizon
from .p017_p018_hard_core_bridge import base_root_index
from .legendre import is_prime, primes_up_to


def p3_rough_triple_states(k: int) -> dict[str, object]:
    """Enumerate bounded P3-cutoff triple-prime survivors for regression research."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    upper = square_interval_upper(k)
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    offsets = rough_survivor_offsets(k, z3)
    factor_primes = tuple(p for p in primes_up_to(k) if p > z3)

    triples: list[tuple[int, int, int, int, int]] = []
    for r in offsets:
        value = k * k + r
        if is_prime(value):
            continue
        factors: list[int] = []
        remainder = value
        for p in factor_primes:
            while remainder % p == 0:
                factors.append(p)
                remainder //= p
            if remainder == 1:
                break
            if p * p > remainder:
                break
        if remainder > 1:
            factors.append(remainder)
        factors.sort()
        if len(factors) == 3 and all(is_prime(f) for f in factors):
            a, b, c = factors
            if not (z3 < a <= b <= c):
                raise AssertionError("P3 rough triple lost its factor ordering/cutoff")
            if a > z2:
                raise AssertionError("triple least factor exceeded the cubic product cutoff")
            triples.append((a, b, c, value, r))

    return {
        "k": k,
        "upper": upper,
        "p3_cutoff": z3,
        "p2_cutoff": z2,
        "triple_states": tuple(triples),
        "triple_count": len(triples),
    }


def p3_cubic_type3_partition(k: int) -> dict[str, object]:
    """Partition P3 triple survivors into cubic-high and balanced cubic-low rows."""
    data = p3_rough_triple_states(k)
    upper = int(data["upper"])
    z2 = int(data["p2_cutoff"])
    horizon = cubic_candidate_horizon(k)
    lower = low_partner_core_floor(k)

    high_rows: list[tuple[int, int, int, int, int, int]] = []
    balanced_rows: list[tuple[int, int, int, int, int, int]] = []

    for a, b, c, value, r in data["triple_states"]:
        root = base_root_index(k, a)
        if a < lower:
            if root <= horizon:
                raise AssertionError("a<L failed to force a cubic-high quotient channel")
            high_rows.append((a, b, c, root, value, r))
        else:
            if root > horizon:
                raise AssertionError("a>=L failed to remain in the cubic-low zone")
            if not (lower <= a <= b <= c):
                raise AssertionError("balanced cubic-low factor ordering failed")
            if c * lower * lower > upper:
                raise AssertionError("balanced triple cofactor exceeded U/L^2")
            balanced_rows.append((a, b, c, root, value, r))

    if lower > z2 + 1:
        raise AssertionError("cubic-low threshold unexpectedly cleared the P2 cutoff")

    return {
        **data,
        "cubic_horizon": horizon,
        "cubic_low_factor_floor": lower,
        "balanced_factor_ceiling_numerator": upper,
        "balanced_factor_ceiling_denominator": lower * lower,
        "cubic_high_unbalanced_triples": tuple(high_rows),
        "cubic_low_balanced_triples": tuple(balanced_rows),
        "all_triples_partitioned": len(high_rows) + len(balanced_rows) == data["triple_count"],
        "route_status": "BALANCED_TYPE_III_BOX_ISOLATED",
    }
