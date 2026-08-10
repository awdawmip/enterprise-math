"""Critical one-half exponent boundary for the explicit PCC route.

Combine the elementary direct reverse bounds:

* nonunit triples: sigma_proj <= c^(1-1/(2M))/2 under c<R^M;
* Pasten-nonexceptional unit triples: sigma_proj <= c^(3/2-1/M)/2.

The unit exponent is the worse one.  As M->1+ it tends to 1/2.  Therefore the
full Masser-Oesterle abc conjecture (which supplies every exponent M>1) implies
PCC_eta for every eta>1/2 outside Pasten's same exceptional family.

Conversely PCC_eta implies Oesterle-abc for every M>1/(1-eta).  This threshold
lies below 2 exactly when eta<1/2.  Hence eta=1/2 is the logical crossing point
of the current projective implication diagram.

This module stores exact rational threshold arithmetic only; it does not assert
any conjectural condition is proved.
"""

from __future__ import annotations

from fractions import Fraction

from .abc_composite_unit_projective_bound import (
    oesterle_to_composite_unit_projective_eta_threshold,
)
from .abc_effective_exponent_transfer import oesterle_threshold_from_effective_eta
from .abc_nonunit_projective_bound import (
    oesterle_to_nonunit_projective_eta_threshold,
)


HALF = Fraction(1, 2)


def direct_global_projective_eta_threshold_from_oesterle(M: Fraction) -> Fraction:
    """Return the worse direct projective threshold over nonexceptional slices."""
    nonunit = oesterle_to_nonunit_projective_eta_threshold(M)
    unit = oesterle_to_composite_unit_projective_eta_threshold(M)
    if unit < nonunit:
        raise AssertionError("composite-unit threshold should dominate nonunit threshold")
    return unit


def pcc_eta_implies_oesterle_below_two(eta: Fraction) -> bool:
    """Return whether the PCC->Oesterle threshold leaves room below exponent two."""
    if not isinstance(eta, Fraction) or not Fraction(0, 1) < eta < Fraction(1, 1):
        raise ValueError("eta must lie strictly between zero and one")
    threshold = oesterle_threshold_from_effective_eta(eta)
    return threshold < 2


def pcc_oesterle_threshold(eta: Fraction) -> Fraction:
    """Return the strict Oesterle threshold ``1/(1-eta)`` supplied by PCC_eta."""
    return oesterle_threshold_from_effective_eta(eta)


def masser_abc_can_force_projective_eta(target_eta: Fraction) -> tuple[Fraction, Fraction]:
    """Return a valid radical exponent M whose direct threshold is below target eta.

    This is possible exactly for target_eta>1/2 because the composite-unit
    threshold is ``3/2-1/M`` and tends to 1/2 as M tends to one from above.
    The returned pair is ``(M, threshold)``.
    """
    if not isinstance(target_eta, Fraction) or not HALF < target_eta < 1:
        raise ValueError("target_eta must lie strictly between 1/2 and one")
    # Need M < 1/(1-(target_eta-1/2)).  Choose a simple midpoint between 1
    # and that upper bound, which remains <2 for all target_eta<1.
    epsilon = target_eta - HALF
    upper = Fraction(1, 1) / (Fraction(1, 1) - epsilon)
    M = (Fraction(1, 1) + upper) / 2
    if not Fraction(1, 1) < M < Fraction(2, 1):
        raise AssertionError("constructed radical exponent left the direct-bound domain")
    threshold = direct_global_projective_eta_threshold_from_oesterle(M)
    if not threshold < target_eta:
        raise AssertionError("constructed M failed target projective exponent")
    return M, threshold
