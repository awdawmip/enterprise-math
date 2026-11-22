"""Elementary logarithmic-strength resource for the half-cutoff Walsh smooth shadow.

Put

    C=floor((k-1)/2)

and let A be the squarefree product of the effective odd anchor primes.  At the
half cutoff every m<=C is automatically C-smooth, so the exact smooth-shadow
main is simply

    Psi_A(C,C)=#{1<=m<=C:(m,A)=1}.

Write the distinct odd anchor primes increasingly as p_1<...<p_w.  Since the
j-th distinct odd prime is at least j+2,

    (p_j-1)/p_j >= (j+1)/(j+2),

and therefore the Euler density has the completely elementary lower bound

    phi(A)/A >= product_(j=1)^w (j+1)/(j+2) = 2/(w+2).

Inclusion--exclusion gives

    Psi_A(C,C)
      = sum_(d|A) mu(d) floor(C/d)
      >= C*phi(A)/A - 2^w
      >= 2C/(w+2) - 2^w.

The existing factorial-height certificate gives

    3*4*...*(w+2)=(w+2)!/2 <= A <= k(k+1)<2k^2,

hence w=O(log k/log log k) and 2^w=k^o(1).  Consequently

    Psi_A(C,C) = Omega(k log log k / log k)

uniformly along the square diagonal.  Thus a future signed-boundary theorem of
size o(k log log k/log k) already beats the exact half-cutoff resource; in
particular O(k/log k) would be more than sufficient for all sufficiently large
k.

This strengthens the earlier k^(1-o(1)) resource without using Mertens' theorem
or any prime-distribution asymptotic.  The asymptotic big-Omega statement uses
only the factorial growth consequence above.  This module does not prove the
required boundary estimate and does not prove Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, prod

from .p017_p018_effective_anchor import effective_odd_anchor_primes
from .p017_p018_walsh_smooth_shadow_main import anchor_coprime_smooth_shadow


def half_cutoff_log_resource(k: int) -> dict[str, object]:
    """Return the exact half-cutoff shadow and its elementary 2/(w+2) lower resource."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    C = (k - 1) // 2
    anchors = tuple(int(p) for p in effective_odd_anchor_primes(k))
    A = prod(anchors, start=1)
    w = len(anchors)

    # Exact half-cutoff smooth shadow.  All m<=C are C-smooth.
    shadow = anchor_coprime_smooth_shadow(k, C)
    psi = int(shadow["smooth_shadow_count_Psi"])
    direct = sum(1 for m in range(1, C + 1) if gcd(m, A) == 1)
    if psi != direct:
        raise AssertionError("half-cutoff smooth shadow is not the anchor-coprime prefix")

    phi_num = prod((p - 1 for p in anchors), start=1)
    phi_den = A
    phi_ratio = Fraction(phi_num, phi_den) if A > 1 else Fraction(1, 1)
    telescoping_density_lower = Fraction(2, w + 2)
    if phi_ratio < telescoping_density_lower:
        raise AssertionError("anchor Euler density fell below 2/(w+2)")

    continuous_lower = Fraction(C, 1) * phi_ratio - 2**w
    elementary_lower = Fraction(2 * C, w + 2) - 2**w
    if Fraction(psi, 1) < continuous_lower:
        raise AssertionError("exact shadow fell below inclusion-exclusion floor bound")
    if continuous_lower < elementary_lower:
        raise AssertionError("Euler-density bound failed to imply elementary lower resource")

    factorial_lower = 1
    for value in range(3, w + 3):
        factorial_lower *= value
    if factorial_lower > A:
        raise AssertionError("distinct odd anchor product fell below 3*4*...*(w+2)")
    if A > k * (k + 1):
        raise AssertionError("effective anchor product escaped the pronic center")

    return {
        "k": k,
        "half_cutoff_C": C,
        "effective_odd_anchors": anchors,
        "effective_anchor_product_A": A,
        "anchor_count_w": w,
        "exact_half_smooth_shadow_Psi": psi,
        "exact_anchor_coprime_prefix": direct,
        "anchor_density_phi_over_A": phi_ratio,
        "telescoping_density_lower_2_over_wplus2": telescoping_density_lower,
        "continuous_floor_lower": continuous_lower,
        "elementary_log_resource_lower": elementary_lower,
        "factorial_anchor_height_lower": factorial_lower,
        "pronic_center_upper": k * (k + 1),
        "exact_resource_identity": True,
        "asymptotic_resource": "Psi_A(C,C)=Omega(k log log k/log k)",
        "sufficient_future_boundary_scale": "o(k log log k/log k); in particular O(k/log k)",
    }
