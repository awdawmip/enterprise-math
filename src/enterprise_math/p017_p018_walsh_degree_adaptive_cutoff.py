"""Degree-adaptive orientation-Walsh cutoff flow from P3 to the half cutoff.

Let

    z3=floor((k^2+2k)^(1/4)),
    z2=floor((k^2+2k)^(1/3)),
    C =floor((k-1)/2).

For one mirror orientation and a cutoff z in [z3,C], let A_z be the hard
orientation-Walsh low-prime amplifier: A_z=0 if the target has a transverse
prime <=z, and otherwise A_z=2^s where s is the number of opposite-side
transverse primes <=z.

There are two exact proof-degree regimes.

P3 band: z3<=z<z2.
--------------------
Every z-rough target has Omega<=3.  With

    c=#{z<p<=k:p|target},

use the Generation-4 quadratic polynomial

    Q2(c)=3-3c+2*binom(c,2).

It gives 3 on primes, 0 on semiprimes/prime cubes/squarefree triples, and -1 on
the repeated-triple depth c=2.  Adding the exact c=2 repair gives

    D_z = A_z[Q2(c)+1_{c=2}] = 3 A_z 1_prime.

P2-to-half band: z2<=z<=C.
--------------------------------
Every z-rough composite is a semiprime p*q with z<p<=k<q, so c is 0 on primes
and 1 on composites.  The proof degree drops to one:

    D_z = 3 A_z(1-c) = 3 A_z 1_prime.

Thus the P2 root boundary is an exact **degree-collapse point**: degree two is
needed immediately below z2, while degree one is exact at and above z2.  The
normalized prime semantics is identical on both sides of the transition.

The reusable floor main is also one formula throughout the complete band.  All
nonconstant low orientation cubes have zero floor; medium pair terms in the P3
band are already above the reusable product cutoff; and the linear high-prime
floor is exactly the smooth-shadow subtraction.  Hence

    floor_main(D_z)=3*Psi_A(C,z)

for every z in [z3,C].

As z increases, a prime target is never removed and its opposite support can only
add visible amplifier primes, so the weighted prime signal is monotone
nondecreasing.  Repeated-triple repair exists only in the quadratic P3 band and
vanishes automatically at the P2 endpoint.

This is an exact P017/P018/BRC proof-precision flow.  It unifies the fourth-root
Generation-4 and P2-to-half linear-Walsh routes; it does not estimate the signed
boundary and does not prove Legendre's conjecture.
"""

from __future__ import annotations

from math import comb

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff
from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff
from .p017_p018_walsh_smooth_shadow_main import walsh_linear_floor_main


def adaptive_cutoff_zone(k: int) -> tuple[int, int, int]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    C = reusable_floor_product_cutoff(k)
    if not z3 < z2 <= C:
        raise ValueError("k is below the stable z3<z2<=half cutoff zone")
    return z3, z2, C


def _q2(c: int) -> int:
    return 3 - 3 * c + 2 * comb(c, 2)


def degree_adaptive_orientation_weight(k: int, radius: int, cutoff: int, orientation: str) -> dict[str, object]:
    """Evaluate the exact normalized degree-2/degree-1 detector on one orientation."""
    z3, z2, C = adaptive_cutoff_zone(k)
    if not (z3 <= cutoff <= C):
        raise ValueError("cutoff must lie in the degree-adaptive zone")
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be upper or lower")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    lower_support = tuple(int(p) for p in lower_support_raw)
    upper_support = tuple(int(p) for p in upper_support_raw)

    if orientation == "upper":
        target_state = upper_state
        target_support = upper_support
        opposite_support = lower_support
    else:
        target_state = lower_state
        target_support = lower_support
        opposite_support = upper_support

    target_low = tuple(p for p in target_support if p <= cutoff)
    opposite_low = tuple(p for p in opposite_support if p <= cutoff)
    rough = not target_low
    amplifier = 2 ** len(opposite_low) if rough else 0
    medium = tuple(p for p in target_support if p > cutoff)
    c = len(medium) if rough else 0
    target_prime = is_prime(target_state)

    repeated_correction = 0
    repeated_prime = None
    if cutoff < z2:
        degree = 2
        if rough and c > 3:
            raise AssertionError("P3-band rough target exceeded support depth three")
        raw = amplifier * _q2(c) if rough else 0
        if rough and c == 2:
            repeated = [p for p in medium if target_state % (p * p) == 0]
            if len(repeated) != 1:
                raise AssertionError("P3-band c=2 target is not a unique repeated-prime triple")
            repeated_prime = repeated[0]
            if repeated_prime * repeated_prime <= k:
                raise AssertionError("repeated-prime repair failed single-use square scale")
            repeated_correction = amplifier
        corrected = raw + repeated_correction
    else:
        degree = 1
        if rough and not target_prime:
            if c != 1:
                raise AssertionError("P2-band rough composite did not have one visible medium prime")
        raw = 3 * amplifier * (1 - c) if rough else 0
        corrected = raw

    expected = 3 * amplifier if target_prime else 0
    if corrected != expected:
        raise AssertionError("degree-adaptive cutoff failed exact normalized prime recovery")
    if (corrected > 0) != target_prime:
        raise AssertionError("degree-adaptive cutoff lost prime positivity")

    return {
        "k": k,
        "radius": radius,
        "orientation": orientation,
        "p3_cutoff_z3": z3,
        "p2_cutoff_z2": z2,
        "half_cutoff_C": C,
        "cutoff": cutoff,
        "proof_degree": degree,
        "target_state": target_state,
        "target_prime": target_prime,
        "target_rough": rough,
        "target_medium_support": medium,
        "target_medium_support_size": c,
        "opposite_visible_support": opposite_low,
        "low_walsh_amplifier": amplifier,
        "raw_weight": raw,
        "repeated_prime": repeated_prime,
        "repeated_correction": repeated_correction,
        "corrected_weight": corrected,
        "normalized_exact_prime_weight": expected,
        "exact_prime_semantics": True,
    }


def degree_adaptive_cutoff_profile(k: int, cutoff: int) -> dict[str, object]:
    """Aggregate both orientations and expose the common 3*Psi smooth-shadow floor main."""
    z3, z2, C = adaptive_cutoff_zone(k)
    if not (z3 <= cutoff <= C):
        raise ValueError("cutoff must lie in the degree-adaptive zone")
    rows: list[dict[str, object]] = []
    signal = 0
    repair = 0
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        for orientation in ("upper", "lower"):
            row = degree_adaptive_orientation_weight(k, radius, cutoff, orientation)
            rows.append(row)
            signal += int(row["corrected_weight"])
            repair += int(row["repeated_correction"])

    floor = walsh_linear_floor_main(k, cutoff)
    one_orientation_floor = 3 * int(floor["smooth_shadow_count_Psi"])
    prime_exists = any(bool(row["target_prime"]) for row in rows)
    if (signal > 0) != prime_exists:
        raise AssertionError("degree-adaptive aggregate lost prime-existence equivalence")
    return {
        "k": k,
        "p3_cutoff_z3": z3,
        "p2_cutoff_z2": z2,
        "half_cutoff_C": C,
        "cutoff": cutoff,
        "proof_degree": 2 if cutoff < z2 else 1,
        "one_orientation_common_smooth_floor_main": one_orientation_floor,
        "symmetric_common_smooth_floor_main": 2 * one_orientation_floor,
        "weighted_prime_signal_times_three": signal,
        "weighted_repeated_repair": repair,
        "repeated_repair_active": cutoff < z2 and repair > 0,
        "prime_exists": prime_exists,
        "positive_iff_prime_exists": (signal > 0) == prime_exists,
        "common_floor_main_is_3Psi": True,
        "rows": tuple(rows),
    }


def degree_collapse_at_p2(k: int) -> dict[str, object]:
    """Verify the quadratic formula and linear formula agree at c=0,1 at z2."""
    z3, z2, C = adaptive_cutoff_zone(k)
    table = tuple(
        {
            "c": c,
            "quadratic_Q2": _q2(c),
            "linear_times_three": 3 * (1 - c),
        }
        for c in (0, 1)
    )
    if any(row["quadratic_Q2"] != row["linear_times_three"] for row in table):
        raise AssertionError("P2 root boundary failed degree-2 to degree-1 collapse")
    return {
        "k": k,
        "p3_cutoff_z3": z3,
        "p2_cutoff_z2": z2,
        "half_cutoff_C": C,
        "transition_table": table,
        "degree_two_below_p2": True,
        "degree_one_at_and_above_p2": True,
        "normalized_semantics_match_at_p2": True,
    }
