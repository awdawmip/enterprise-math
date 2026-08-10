"""Exact rational exponent bookkeeping for the Effective Small Derivatives route.

Pasten proves:

* Small Derivatives with exponent eta implies Oesterle-abc for every
  M > 1/(1-eta).
* Oesterle-abc with 1<M<2 implies Small Derivatives for every
  eta > 1-(2-M)/(4M).

P025's intrinsic Wronskian normalization weakens Small Derivatives to ESD
``mu/eta_min < c^eta`` while preserving the first Wronskian-to-abc argument.
The reverse arrow is inherited because ordinary SD implies ESD pointwise.

This module stores only the exact rational threshold maps; it does not assert
that any conjectural hypothesis is proved.
"""

from __future__ import annotations

from fractions import Fraction


def oesterle_threshold_from_effective_eta(eta: Fraction) -> Fraction:
    """Return the strict threshold ``1/(1-eta)`` from ESD_eta to Oesterle M."""
    if not isinstance(eta, Fraction) or not Fraction(0, 1) < eta < Fraction(1, 1):
        raise ValueError("eta must be a Fraction strictly between zero and one")
    return Fraction(1, 1) / (Fraction(1, 1) - eta)


def pasten_eta_threshold_from_oesterle(M: Fraction) -> Fraction:
    """Return Pasten's strict SD/ESD eta threshold from an Oesterle exponent M.

    Theorem 4.5 gives every

        eta > 1 - (2-M)/(4M).
    """
    if not isinstance(M, Fraction) or not Fraction(1, 1) < M < Fraction(2, 1):
        raise ValueError("M must be a Fraction strictly between one and two")
    return Fraction(1, 1) - (Fraction(2, 1) - M) / (4 * M)


def ordinary_sd_implies_effective_sd(mu: int, eta_min: int, c: int, p: int, q: int) -> bool:
    """Check the pointwise implication ``mu<c^(p/q) => mu/eta<c^(p/q)`` exactly."""
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (mu, eta_min, c, p, q)):
        raise ValueError("all inputs must be integers")
    if mu <= 0 or eta_min <= 0 or c <= 1 or not 0 < p < q:
        raise ValueError("require positive mu/eta, c>1, and 0<p<q")
    ordinary = mu**q < c**p
    effective = mu**q < eta_min**q * c**p
    if ordinary and not effective:
        raise AssertionError("ordinary small derivative must imply effective small derivative")
    return (not ordinary) or effective
