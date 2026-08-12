"""Walsh-amplified Generation-4 quadratic detector at the fourth-root P3 cutoff.

Let z=z3=floor((k^2+2k)^(1/4)), C=floor((k-1)/2), and fix one mirror
orientation.  Use hard orientation-Walsh only on transverse primes <=z:

    A_z = prod_{ell<=z}(1+1_{ell|opposite}-1_{ell|target}).

Thus A_z is zero when the target has a small prime and otherwise equals
2^(# opposite small-prime hits).  On a z-rough target let

    c=#{z<p<=k : p|target}.

The fourth-root product bound gives Omega(target)<=3.  The square-basin factor
geometry then has the exact medium-support types

    prime                         c=0,
    semiprime p*q with q>k       c=1,
    repeated triple              c=2,
    squarefree triple            c=3.

Hence the Generation-4 quadratic polynomial

    Q2(c)=3-3c+2*binom(c,2)

has values 3,0,-1,0.  Therefore

    H=A_z Q2(c)

is positive only on primes, zero on semiprimes and squarefree triples, and
negative only on repeated triples.  Adding the exact repeated-triple correction
A_z*1_{c=2} gives

    H_corr = 3 A_z 1_{target prime},

an exact nonnegative weighted prime detector.

The reusable-floor main is especially simple.  Every nonempty low-band Walsh
orientation cube has zero floor.  The constant term contributes 3*B0 and the
linear medium-prime terms contribute -3*sum Bp.  Since

    (z+1)^2 > sqrt(k^2+2k) > C,

every medium pair product is already above the reusable-floor cutoff, so the
quadratic pair term has no floor.  By the smooth-shadow theorem,

    floor_main(H)=3*Psi_A(C,z).

The repeated-triple correction is also boundary-only: its repeated prime p>z
satisfies p^2>k, so odd p^2 incidences are globally single-use.  This bridge
therefore combines an order-k exact smooth floor resource with a finite signed
boundary problem whose repeated-factor negative class is separately single-use.
It does not estimate the remaining squarefree/signed boundary and does not prove
Legendre.
"""

from __future__ import annotations

from math import comb, prod

from .legendre import is_prime, primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff
from .p017_p018_walsh_smooth_shadow_main import walsh_linear_floor_main


def p3_fourth_root_cutoff(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 10:
        raise ValueError("k must be an integer >=10")
    return int(almost_prime_cutoff(k, 3)["cutoff"])


def g4_quadratic_value(medium_support_size: int) -> int:
    if isinstance(medium_support_size, bool) or not isinstance(medium_support_size, int):
        raise ValueError("medium_support_size must be an integer")
    c = medium_support_size
    if not (0 <= c <= 3):
        raise ValueError("P3 medium support size must lie in 0..3")
    return 3 - 3 * c + 2 * comb(c, 2)


def walsh_g4_orientation_point(k: int, radius: int, orientation: str) -> dict[str, object]:
    """Evaluate A_z Q2(c) and the repeated-triple correction on one orientation."""
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be 'upper' or 'lower'")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    z = p3_fourth_root_cutoff(k)
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

    target_low = tuple(p for p in target_support if p <= z)
    opposite_low = tuple(p for p in opposite_support if p <= z)
    rough = not target_low
    amplifier = 2 ** len(opposite_low) if rough else 0
    medium = tuple(p for p in target_support if p > z)
    c = len(medium) if rough else 0
    if rough and c > 3:
        raise AssertionError("fourth-root rough target exceeded support depth three")

    raw = amplifier * g4_quadratic_value(c) if rough else 0
    repeated = False
    repeated_prime = None
    if rough and c == 2:
        # c=2 at P3 is the repeated-factor triple class.  Recover the repeated
        # medium prime directly and certify its p^2 single-use scale.
        repeated_candidates = [p for p in medium if target_state % (p * p) == 0]
        if len(repeated_candidates) != 1:
            raise AssertionError("P3 support depth two is not a unique repeated-prime triple")
        repeated = True
        repeated_prime = repeated_candidates[0]
        if repeated_prime * repeated_prime <= k:
            raise AssertionError("repeated P3 prime square is not globally single-use")
    correction = amplifier if repeated else 0
    corrected = raw + correction
    target_prime = is_prime(target_state)
    expected = 3 * amplifier if target_prime else 0
    if corrected != expected:
        raise AssertionError("Walsh-G4 repeated repair did not recover exact weighted prime detector")
    if (corrected > 0) != target_prime:
        raise AssertionError("Walsh-G4 corrected detector lost prime positivity")

    return {
        "k": k,
        "radius": radius,
        "orientation": orientation,
        "p3_cutoff": z,
        "target_state": target_state,
        "target_rough": rough,
        "target_medium_support": medium,
        "target_medium_support_size": c,
        "opposite_small_support": opposite_low,
        "low_walsh_amplifier": amplifier,
        "quadratic_value": g4_quadratic_value(c) if rough else None,
        "raw_walsh_g4_weight": raw,
        "repeated_triple": repeated,
        "repeated_prime": repeated_prime,
        "repeated_single_use_correction": correction,
        "corrected_walsh_g4_weight": corrected,
        "target_prime": target_prime,
        "corrected_weight_equals_three_prime_amplifier": True,
    }


def walsh_g4_profile(k: int) -> dict[str, object]:
    """Aggregate both orientations and expose smooth main / repeated-tail structure."""
    z = p3_fourth_root_cutoff(k)
    rows: list[dict[str, object]] = []
    raw_total = 0
    repeated_total = 0
    corrected_total = 0
    repeated_labels: list[tuple[str, int, int]] = []
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        for orientation in ("upper", "lower"):
            row = walsh_g4_orientation_point(k, radius, orientation)
            rows.append(row)
            raw_total += int(row["raw_walsh_g4_weight"])
            repeated_total += int(row["repeated_single_use_correction"])
            corrected_total += int(row["corrected_walsh_g4_weight"])
            if bool(row["repeated_triple"]):
                repeated_labels.append((orientation, int(row["repeated_prime"]), radius))

    # p^2>k gives one signed state per repeated prime across both orientations.
    repeated_primes = [p for _orientation, p, _r in repeated_labels]
    if len(repeated_primes) != len(set(repeated_primes)):
        raise AssertionError("a repeated P3 prime supported two signed repeated-triple states")
    if raw_total + repeated_total != corrected_total:
        raise AssertionError("Walsh-G4 aggregate repair identity failed")

    floor = walsh_linear_floor_main(k, z)
    one_orientation_floor = 3 * int(floor["smooth_shadow_count_Psi"])
    prime_exists = corrected_total > 0
    return {
        "k": k,
        "p3_cutoff": z,
        "one_orientation_quadratic_floor_main": one_orientation_floor,
        "symmetric_quadratic_floor_main": 2 * one_orientation_floor,
        "raw_walsh_g4_weight": raw_total,
        "weighted_repeated_triple_correction": repeated_total,
        "corrected_weighted_prime_signal_times_three": corrected_total,
        "raw_plus_repeated_equals_corrected": True,
        "repeated_prime_labels": tuple(repeated_labels),
        "repeated_prime_global_single_use": True,
        "prime_exists": prime_exists,
        "positive_corrected_iff_prime_exists": prime_exists == any(bool(row["target_prime"]) for row in rows),
        "smooth_shadow": floor,
        "rows": tuple(rows),
    }
