"""Prior-art parameter bridge: Iwaniec--Laborde level vs square root cutoffs.

This module records exact rational arithmetic extracted from the 1981 paper
"P2 in short intervals".  It does not reprove their analytic estimates.

Their interval length is y=x^theta.  With a=6, the final parameter identity
(19) gives

    log D / log x = 2*theta - 5/14.

At their proved theta=9/20 this is

    delta = 19/35.

The dimension-one lower linear sieve has parameter

    s = log D / log z.

For the root-certified P3 cutoff z=x^(1/4),

    s3 = 4*delta = 76/35 > 2,

so this prior-art bilinear level crosses the positive lower-sieve threshold.
For the minimal P2 cutoff z=x^(1/3),

    s2 = 3*delta = 57/35 < 2,

so the same unsigned lower linear sieve is still below its positive range.

If one only takes the formal theta -> 1/2 endpoint of the same parameter
formula, delta -> 9/14.  This is still short of the direct P2 lower-sieve level
2/3 by exactly 1/42.  This endpoint arithmetic is a scale diagnostic, not a
claim that the 1981 theorem includes theta=1/2 with unchanged constants.

The bridge explains why the root P3 layer is naturally reachable by the
classical bilinear remainder technology while the direct root-P2 lower sieve is
not.  Iwaniec--Laborde nevertheless reach P2 by weighted-sieve arguments; the
1/42 gap is only for the *direct minimal-root lower linear sieve* route.
"""

from __future__ import annotations

from fractions import Fraction

IWANIEC_LABORDE_THETA = Fraction(9, 20)
IWANIEC_LABORDE_LEVEL = Fraction(19, 35)
P3_ROOT_EXPONENT = Fraction(1, 4)
P2_ROOT_EXPONENT = Fraction(1, 3)
P1_ROOT_EXPONENT = Fraction(1, 2)
FORMAL_SQUARE_ENDPOINT_THETA = Fraction(1, 2)
FORMAL_SQUARE_ENDPOINT_LEVEL = Fraction(9, 14)


def bilinear_level_exponent(theta: Fraction) -> Fraction:
    """Return delta(theta)=2 theta - 5/14 from the 1981 parameter identity."""
    if not isinstance(theta, Fraction):
        theta = Fraction(theta)
    return 2 * theta - Fraction(5, 14)


def root_sieve_parameter(theta: Fraction, root_exponent: Fraction) -> Fraction:
    """Return s=delta/root_exponent for a root cutoff z=x^root_exponent."""
    if not isinstance(root_exponent, Fraction):
        root_exponent = Fraction(root_exponent)
    if root_exponent <= 0:
        raise ValueError("root_exponent must be positive")
    return bilinear_level_exponent(theta) / root_exponent


def iwaniec_root_level_ledger() -> dict[str, object]:
    """Return the exact proved-theta and formal-square endpoint ledger."""
    theta = IWANIEC_LABORDE_THETA
    delta = bilinear_level_exponent(theta)
    if delta != IWANIEC_LABORDE_LEVEL:
        raise AssertionError("1981 level arithmetic changed")

    s3 = root_sieve_parameter(theta, P3_ROOT_EXPONENT)
    s2 = root_sieve_parameter(theta, P2_ROOT_EXPONENT)
    if not s3 > 2:
        raise AssertionError("1981 bilinear level should cross the P3 lower-sieve threshold")
    if not s2 < 2:
        raise AssertionError("1981 bilinear level should remain below the direct P2 lower-sieve threshold")

    endpoint_delta = bilinear_level_exponent(FORMAL_SQUARE_ENDPOINT_THETA)
    if endpoint_delta != FORMAL_SQUARE_ENDPOINT_LEVEL:
        raise AssertionError("formal theta=1/2 level arithmetic changed")
    endpoint_p2_deficit = 2 * P2_ROOT_EXPONENT - endpoint_delta
    if endpoint_p2_deficit != Fraction(1, 42):
        raise AssertionError("formal direct-P2 level deficit should be exactly 1/42")

    return {
        "proved_theta": theta,
        "proved_level_exponent": delta,
        "p3_root_exponent": P3_ROOT_EXPONENT,
        "p3_s": s3,
        "p3_positive_lower_sieve_margin_in_s": s3 - 2,
        "p3_level_margin": delta - 2 * P3_ROOT_EXPONENT,
        "p2_root_exponent": P2_ROOT_EXPONENT,
        "p2_s": s2,
        "p2_direct_lower_sieve_level_deficit": 2 * P2_ROOT_EXPONENT - delta,
        "formal_square_theta": FORMAL_SQUARE_ENDPOINT_THETA,
        "formal_square_level_exponent": endpoint_delta,
        "formal_square_p3_s": endpoint_delta / P3_ROOT_EXPONENT,
        "formal_square_p2_s": endpoint_delta / P2_ROOT_EXPONENT,
        "formal_square_direct_p2_level_deficit": endpoint_p2_deficit,
        "status": "PRIOR_ART_LEVEL_TO_ROOT_CUTOFF_ALIGNMENT",
    }
