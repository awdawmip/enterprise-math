"""Power-scale resource supplied by the exact Walsh smooth-shadow main.

Let C=floor((k-1)/2), let A be the squarefree product of effective odd anchor
primes, and choose z<=C with (z+1)^2>C.  The exact Walsh floor theorem gives the
one-orientation main

    Psi_A(C,z)=#{m<=C:gcd(m,A)=1,P^+(m)<=z}.

Every anchor-coprime integer m<=z is automatically z-smooth, hence

    Psi_A(C,z) >= Phi_A(z):=#{m<=z:gcd(m,A)=1}.

Inclusion-exclusion gives the exact identity

    Phi_A(z)=sum_{d|A} mu(d) floor(z/d)

and therefore the finite lower estimate

    Phi_A(z) >= z*phi(A)/A - 2^omega(A).

The anchor structure makes this a genuine power resource uniformly in k.  If
w=omega(A), then the w distinct odd primes dividing A are at least 3,4,...,w+2,
so

    (w+2)!/2 <= A <= k(k+1) < 2k^2.

Thus w=O(log k/log log k), whence

    phi(A)/A >= (2/3)^w = k^(-o(1)),
    2^w = k^(o(1)).

Consequently for every fixed power cutoff z=k^(alpha+o(1)) with alpha>0,

    Psi_A(C,z) >= k^(alpha-o(1)).

This turns any future signed-boundary estimate

    |B(k,z)| <= k^(beta+o(1)),       beta<alpha,

into an asymptotically sufficient inequality `|B|<Psi_A(C,z)`.  In particular,
at the half cutoff alpha=1, **any fixed sublinear power saving** on the complete
signed boundary would suffice for all sufficiently large k.

This module records an exact finite lower resource and its elementary asymptotic
interpretation.  It does not prove a boundary power saving and does not prove
Legendre.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod

from .legendre import squarefree_divisors_with_mu
from .p017_p018_effective_anchor import effective_odd_anchor_primes
from .p017_p018_walsh_smooth_shadow_main import anchor_coprime_smooth_shadow


def anchor_coprime_prefix_resource(k: int, cutoff: int) -> dict[str, object]:
    """Return exact Phi_A(z) and the inclusion-exclusion lower comparison."""
    data = anchor_coprime_smooth_shadow(k, cutoff)
    z = int(data["cutoff"])
    anchors = tuple(int(p) for p in data["effective_odd_anchors"])
    A = prod(anchors, start=1)
    rows = squarefree_divisors_with_mu(list(anchors))
    exact = sum(mu * (z // d) for d, mu in rows)
    phi_num = prod((p - 1 for p in anchors), start=1)
    phi_den = prod(anchors, start=1)
    density = Fraction(phi_num, phi_den) if anchors else Fraction(1, 1)
    continuous = Fraction(z, 1) * density
    error_budget = 2 ** len(anchors)
    lower = continuous - error_budget

    direct = sum(1 for m in range(1, z + 1) if all(m % p for p in anchors))
    if exact != direct:
        raise AssertionError("anchor-coprime prefix inclusion-exclusion failed")
    if Fraction(exact, 1) < lower:
        raise AssertionError("anchor-coprime prefix fell below the floor-error lower comparison")
    psi = int(data["smooth_shadow_count_Psi"])
    if psi < exact:
        raise AssertionError("smooth shadow failed to contain the anchor-coprime cutoff prefix")

    return {
        "k": k,
        "cutoff": z,
        "effective_odd_anchors": anchors,
        "effective_anchor_product": A,
        "anchor_count_omega": len(anchors),
        "exact_anchor_coprime_prefix_Phi": exact,
        "anchor_density_phi_over_A": density,
        "continuous_anchor_prefix_main": continuous,
        "floor_error_budget_2_to_omega": error_budget,
        "certified_fractional_lower_bound": lower,
        "smooth_shadow_Psi": psi,
        "smooth_shadow_dominates_prefix": True,
    }


def anchor_factorial_height_certificate(k: int) -> dict[str, object]:
    """Verify (w+2)!/2 <= A <= k(k+1) for the actual effective anchor product."""
    anchors = effective_odd_anchor_primes(k)
    A = prod(anchors, start=1)
    factorial_lower = 1
    for value in range(3, len(anchors) + 3):
        factorial_lower *= value
    if factorial_lower > A:
        raise AssertionError("distinct odd anchor product fell below 3*4*...*(w+2)")
    if A > k * (k + 1):
        raise AssertionError("effective anchor product escaped k(k+1)")
    return {
        "k": k,
        "anchor_count_omega": len(anchors),
        "effective_anchor_product": A,
        "factorial_lower_bound": factorial_lower,
        "center_upper_bound": k * (k + 1),
        "factorial_height_certificate": True,
        "asymptotic_consequence": "omega(A)=O(log k/log log k); phi(A)/A=k^-o(1); 2^omega(A)=k^o(1)",
    }


def boundary_power_sufficiency_target(k: int, cutoff: int) -> dict[str, object]:
    """Return the exact finite resource a future boundary theorem must beat."""
    resource = anchor_coprime_prefix_resource(k, cutoff)
    psi = int(resource["smooth_shadow_Psi"])
    return {
        **resource,
        "exact_boundary_loss_ceiling_needed_for_certificate": psi - 1,
        "strict_target": "SIGNED_BOUNDARY_LOSS < smooth_shadow_Psi",
        "power_target_interpretation": (
            "If cutoff=k^(alpha+o(1)) and boundary=O(k^(beta+o(1))) with beta<alpha, "
            "the certificate holds for all sufficiently large k."
        ),
    }
