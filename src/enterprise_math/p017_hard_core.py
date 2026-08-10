"""Discovery-stage P017 residual hard-core geometry.

This module isolates the mirror branch left after canonical L053.  It records a
sequence of coupled WIP refinements:

1. full-core congruence modulo odd S=S_-S_+ plus anchor-forced odd radius parity
   gives one class modulo 2S, so multiple parity-compatible lifts require 2S<k;
2. inside a fixed full-core cell, the radius lifts form a one-dimensional affine
   orbit and the two large tails move by opposite fixed steps while preserving
   a weighted conservation law;
3. the two affine tail forms have constant linear resultant 4k(k+1), giving an
   exact local sieve signature: one excluded lift residue for odd primes dividing
   M*S and two distinct excluded residues for every other odd prime <=k;
4. therefore every finite odd-prime wheel remains locally admissible: no fixed
   congruence modulus can eliminate a residual cell by itself;
5. tail separation is >k+5 when S<k, >3k+9 in the parity multi-lift region 2S<k,
   and >11k+25 in the generic ternary-wheel multi-lift regime 3∤MS, 6S<k.

These are discovery results, not a canonical L055.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_mirror import anchor_surviving_radius, mirror_center, mirror_pair
from .p017_mirror_crt import observed_mirror_full_core_idempotent


def anchor_parity_full_core_capacity(k: int, radius: int) -> dict[str, object]:
    """Refine the canonical L053 full-core progression by mandatory odd parity.

    Canonical L053 places the observed radius in one residue class modulo the
    odd full-core modulus S. Anchor survival also forces r odd because 2 divides
    M=k(k+1). Since gcd(2,S)=1, these two conditions form one residue class
    modulo 2S. Therefore bounded parity-compatible lifts in 1<=r<k are spaced
    by 2S, and 2S>=k implies capacity at most one.
    """
    data = observed_mirror_full_core_idempotent(k, radius)
    modulus = int(data["modulus"])
    if modulus % 2 == 0:
        raise AssertionError("canonical L053 full-core modulus must be odd")
    if radius % 2 == 0:
        raise AssertionError("anchor-surviving radius must be odd")

    raw_lifts = list(data["full_core_lifts"])
    parity_lifts = [candidate for candidate in raw_lifts if candidate % 2 == 1]
    anchor_lifts = [
        candidate
        for candidate in parity_lifts
        if anchor_surviving_radius(k, candidate)
    ]
    if radius not in anchor_lifts:
        raise AssertionError("observed radius escaped its parity/anchor refinement")
    for left, right in zip(parity_lifts, parity_lifts[1:]):
        if right - left != 2 * modulus:
            raise AssertionError("parity-compatible full-core lifts are not 2S-spaced")
    if 2 * modulus >= k and len(parity_lifts) > 1:
        raise AssertionError("2S>=k should force at most one parity-compatible lift")
    if not set(anchor_lifts).issubset(parity_lifts):
        raise AssertionError("anchor filtering increased parity capacity")

    return {
        **data,
        "raw_full_core_lifts": raw_lifts,
        "parity_full_core_lifts": parity_lifts,
        "anchor_full_core_lifts": anchor_lifts,
        "parity_modulus": 2 * modulus,
        "parity_capacity": len(parity_lifts),
        "anchor_capacity": len(anchor_lifts),
    }


def residual_hard_core_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Return the WIP hard-core tail-gap data under S_-*S_+<k.

    Assumptions:
    - 1 <= radius < k and the radius survives the anchor sieve;
    - both mirror states M-radius and M+radius are composite;
    - with full k-smooth cores a,b, one has a*b < k.

    Conclusion:
        abs(q_- - q_+) > k+5,
    hence, because both tails are odd primes,
        abs(q_- - q_+) >= k+6  if k is even,
        abs(q_- - q_+) >= k+7  if k is odd.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(radius, bool) or not isinstance(radius, int):
        raise ValueError("radius must be an integer")
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    center = mirror_center(k)
    lower, upper = mirror_pair(k, radius)
    lower_data = square_basin_smooth_tail(k, lower)
    upper_data = square_basin_smooth_tail(k, upper)
    if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
        raise ValueError("both mirror states must be composite")

    a = int(lower_data["smooth_core"])
    b = int(upper_data["smooth_core"])
    q_minus = int(lower_data["tail"])
    q_plus = int(upper_data["tail"])
    if a <= 1 or b <= 1:
        raise AssertionError("composite hard-core state lost its smooth core")
    if a * b >= k:
        raise ValueError("residual hard-core condition requires S_-*S_+ < k")
    if gcd(a, b) != 1:
        raise AssertionError("surviving mirror cores must be coprime")
    if a % 2 == 0 or b % 2 == 0:
        raise AssertionError("anchor-surviving full cores must be odd")
    if gcd(a * b, center) != 1:
        raise AssertionError("anchor-surviving full cores must be transverse to M")
    if q_minus <= k or q_plus <= k or not is_prime(q_minus) or not is_prime(q_plus):
        raise AssertionError("residual hard-core tails must be primes > k")

    gap = abs(q_minus - q_plus)
    # Distinct coprime odd cores satisfy |a-b|>=2 and a+b<=ab.
    # In the worse orientation a<b:
    #   q_- - q_+ = ((b-a)M-(a+b)r)/(ab)
    #               >= [2k(k+1)-ab(k-1)]/(ab)
    #               >= [k^2+4k-1]/(k-1) > k+5.
    if gap <= k + 5:
        raise AssertionError("hard-core large-prime tails were not k-scale separated")

    parity_bound = k + 6 if k % 2 == 0 else k + 7
    if gap < parity_bound or gap % 2:
        raise AssertionError("odd-prime parity sharpening failed")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "lower": lower,
        "upper": upper,
        "lower_core": a,
        "upper_core": b,
        "core_product": a * b,
        "lower_tail": q_minus,
        "upper_tail": q_plus,
        "tail_gap": gap,
        "parity_lower_bound": parity_bound,
    }


def full_core_affine_orbit(k: int, radius: int) -> dict[str, object]:
    """Expose the exact one-dimensional affine orbit of one residual core cell.

    Let a=S_-, b=S_+, S=ab and use the observed radius as t=0.  Every
    parity-compatible L053 lift has

        r_t   = r + 2S t,
        q_-(t)= q_-(0) - 2b t,
        q_+(t)= q_+(0) + 2a t.

    The weighted conservation law

        a*q_-(t) + b*q_+(t) = 2M

    is independent of t.  The linear resultant of the two tail forms is

        (2a)q_-(0) - (-2b)q_+(0) = 4M,

    also independent of the cell orientation.

    Other lifts in this congruence cell need not keep a,b as their *full* smooth
    cores; that happens exactly when the affine tails remain k-rough, which in
    this square-basin residual regime means prime >k.
    """
    data = residual_hard_core_tail_gap(k, radius)
    capacity = anchor_parity_full_core_capacity(k, radius)
    a = int(data["lower_core"])
    b = int(data["upper_core"])
    s = a * b
    m = int(data["center"])
    q_minus = int(data["lower_tail"])
    q_plus = int(data["upper_tail"])

    if a * q_minus + b * q_plus != 2 * m:
        raise AssertionError("mirror-tail weighted conservation failed at t=0")
    resultant = 2 * a * q_minus + 2 * b * q_plus
    if resultant != 4 * m:
        raise AssertionError("affine tail resultant is not 4M")

    orbit: list[dict[str, int | bool]] = []
    for candidate in capacity["parity_full_core_lifts"]:
        delta = int(candidate) - radius
        if delta % (2 * s):
            raise AssertionError("parity lift left the 2S affine lattice")
        t = delta // (2 * s)
        lower_tail = q_minus - 2 * b * t
        upper_tail = q_plus + 2 * a * t
        if m - int(candidate) != a * lower_tail:
            raise AssertionError("lower affine tail transport failed")
        if m + int(candidate) != b * upper_tail:
            raise AssertionError("upper affine tail transport failed")
        if a * lower_tail + b * upper_tail != 2 * m:
            raise AssertionError("weighted conservation failed along affine orbit")
        orbit.append(
            {
                "t": t,
                "radius": int(candidate),
                "lower_tail_form": lower_tail,
                "upper_tail_form": upper_tail,
                "anchor_survives": anchor_surviving_radius(k, int(candidate)),
                "both_tail_forms_prime": (
                    lower_tail > k
                    and upper_tail > k
                    and is_prime(lower_tail)
                    and is_prime(upper_tail)
                ),
            }
        )

    return {
        **data,
        "step_radius": 2 * s,
        "step_lower_tail": -2 * b,
        "step_upper_tail": 2 * a,
        "linear_resultant": resultant,
        "orbit": orbit,
    }


def hard_core_local_sieve_signature(k: int, radius: int, prime: int) -> dict[str, object]:
    """Count forbidden lift-index residues for one odd prime <=k.

    Use the affine orbit with t=0 at the observed hard-core radius.  For an odd
    prime ell<=k, a lift index is locally forbidden when either affine tail form
    is 0 mod ell.  If ell divides M, anchor survival additionally forbids the
    unique index where r_t=0 mod ell; this is the same residue as both tail zeros.

    Exact local signature:

        nu_ell = 1  if ell | M*S,
        nu_ell = 2  if ell does not divide M*S.

    In the generic case the two tail roots are distinct because their linear
    resultant is 4M.  Thus nu_ell<ell for every odd ell: no odd prime supplies a
    complete local obstruction.
    """
    if isinstance(prime, bool) or not isinstance(prime, int):
        raise ValueError("prime must be an integer")
    if prime < 3 or prime > k or not is_prime(prime):
        raise ValueError("prime must be an odd prime <= k")

    data = residual_hard_core_tail_gap(k, radius)
    a = int(data["lower_core"])
    b = int(data["upper_core"])
    s = a * b
    m = int(data["center"])
    q_minus = int(data["lower_tail"])
    q_plus = int(data["upper_tail"])

    forbidden: set[int] = set()
    reasons: dict[int, tuple[str, ...]] = {}
    for t in range(prime):
        local_reasons: list[str] = []
        r_t = radius + 2 * s * t
        lower_tail = q_minus - 2 * b * t
        upper_tail = q_plus + 2 * a * t
        if m % prime == 0 and r_t % prime == 0:
            local_reasons.append("anchor")
        if lower_tail % prime == 0:
            local_reasons.append("lower_tail")
        if upper_tail % prime == 0:
            local_reasons.append("upper_tail")
        if local_reasons:
            forbidden.add(t)
            reasons[t] = tuple(local_reasons)

    expected = 1 if (m * s) % prime == 0 else 2
    if len(forbidden) != expected:
        raise AssertionError("hard-core local sieve signature changed")
    allowed = tuple(t for t in range(prime) if t not in forbidden)
    if not allowed:
        raise AssertionError("an odd prime produced a complete local obstruction")

    return {
        "k": k,
        "radius": radius,
        "prime": prime,
        "core_product": s,
        "forbidden_residues": tuple(sorted(forbidden)),
        "allowed_residues": allowed,
        "forbidden_count": len(forbidden),
        "allowed_count": len(allowed),
        "reasons": reasons,
        "generic_two_root_case": (m * s) % prime != 0,
    }


def finite_odd_wheel_admissibility(
    k: int, radius: int, primes: tuple[int, ...]
) -> dict[str, object]:
    """Prove that any finite odd-prime wheel leaves admissible lift classes.

    Local allowed sets combine by the classical Chinese remainder theorem.
    Consequently the number of allowed classes modulo the wheel product is the
    product of the local allowed counts and is always positive.  This is a
    negative-boundary result: fixed finite congruence elimination alone cannot
    kill a residual full-core cell.
    """
    if not primes:
        raise ValueError("primes must be nonempty")
    if len(set(primes)) != len(primes):
        raise ValueError("primes must be distinct")

    signatures = [hard_core_local_sieve_signature(k, radius, p) for p in primes]
    modulus = 1
    allowed_count = 1
    for signature in signatures:
        modulus *= int(signature["prime"])
        allowed_count *= int(signature["allowed_count"])
    if allowed_count <= 0:
        raise AssertionError("finite odd wheel unexpectedly killed every class")

    return {
        "k": k,
        "radius": radius,
        "wheel_modulus": modulus,
        "allowed_class_count": allowed_count,
        "local_signatures": tuple(signatures),
    }


def generic_ternary_wheel_capacity(k: int, radius: int) -> dict[str, object]:
    """Exploit the unique surviving mod-3 lift class when 3 does not divide M*S.

    In the generic ell=3 case the two tail forms exclude two distinct residues,
    leaving exactly one t class modulo 3.  Hence tail-3-rough parity lifts are
    spaced by 6S.  Therefore two prime-tail lifts in the same cell can exist only
    if 6S<k.
    """
    if k < 3:
        raise ValueError("k must be at least 3")
    data = full_core_affine_orbit(k, radius)
    s = int(data["core_product"])
    m = int(data["center"])
    if (m * s) % 3 == 0:
        raise ValueError("generic ternary-wheel refinement requires 3 not dividing M*S")
    signature = hard_core_local_sieve_signature(k, radius, 3)
    if signature["allowed_count"] != 1:
        raise AssertionError("generic mod-3 wheel should leave one lift-index class")
    allowed_t = int(signature["allowed_residues"][0])

    ternary_safe: list[dict[str, int | bool]] = []
    for point in data["orbit"]:
        t = int(point["t"])
        if t % 3 != allowed_t:
            continue
        if int(point["lower_tail_form"]) % 3 == 0:
            raise AssertionError("ternary-safe lower tail is divisible by 3")
        if int(point["upper_tail_form"]) % 3 == 0:
            raise AssertionError("ternary-safe upper tail is divisible by 3")
        ternary_safe.append(point)

    for left, right in zip(ternary_safe, ternary_safe[1:]):
        if int(right["radius"]) - int(left["radius"]) != 6 * s:
            raise AssertionError("generic ternary-safe lifts are not 6S-spaced")
    if 6 * s >= k and len(ternary_safe) > 1:
        raise AssertionError("6S>=k should force at most one generic ternary-safe lift")

    return {
        **data,
        "ternary_allowed_t_mod_3": allowed_t,
        "ternary_safe_lifts": ternary_safe,
        "ternary_step_radius": 6 * s,
        "ternary_capacity": len(ternary_safe),
    }


def residual_multi_lift_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Strengthen the tail gap in the parity region capable of multiple lifts.

    The parity refinement shows that multiple candidates for one full-core cell
    require 2ab<k. Then 2ab<=k-1, so the same mirror identity gives

        |q_- - q_+|
        >= 2k(k+1)/(ab) - (k-1)
        >= 4k(k+1)/(k-1) - (k-1)
        = 3k + 9 + 8/(k-1)
        > 3k+9.
    """
    data = residual_hard_core_tail_gap(k, radius)
    core_product = int(data["core_product"])
    if 2 * core_product >= k:
        raise ValueError("multiple-lift residual condition requires 2*S_-*S_+ < k")

    gap = int(data["tail_gap"])
    if gap <= 3 * k + 9:
        raise AssertionError("multi-lift hard-core tails were not 3k-scale separated")
    parity_bound = 3 * k + 10 if k % 2 == 0 else 3 * k + 11
    if gap < parity_bound or gap % 2:
        raise AssertionError("multi-lift odd-prime parity sharpening failed")

    return {
        **data,
        "multi_lift_parity_lower_bound": parity_bound,
    }


def residual_generic_ternary_multi_lift_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Sharpen the tail gap when a generic mod-3 cell can support two lifts.

    If 3 does not divide M*S, two prime-tail lifts require 6S<k by the unique
    allowed t class modulo 3.  Hence 6S<=k-1, and

        |q_- - q_+|
        >= 2k(k+1)/S - (k-1)
        >= 12k(k+1)/(k-1) - (k-1)
        = 11k + 25 + 24/(k-1)
        > 11k+25.
    """
    data = residual_hard_core_tail_gap(k, radius)
    s = int(data["core_product"])
    m = int(data["center"])
    if (m * s) % 3 == 0:
        raise ValueError("generic ternary branch requires 3 not dividing M*S")
    if 6 * s >= k:
        raise ValueError("generic multi-lift branch requires 6*S < k")

    gap = int(data["tail_gap"])
    if gap <= 11 * k + 25:
        raise AssertionError("generic ternary multi-lift tails missed the 11k-scale gap")
    parity_bound = 11 * k + 26 if k % 2 == 0 else 11 * k + 27
    if gap < parity_bound or gap % 2:
        raise AssertionError("generic ternary tail-gap parity sharpening failed")

    return {
        **data,
        "generic_ternary_parity_lower_bound": parity_bound,
    }
