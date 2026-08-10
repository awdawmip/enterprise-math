"""Elementary almost-all Oesterle-abc consequence of projective sparsity.

Fix M>1 and choose eta with

    0 < eta < 1-1/M.

PCC_eta gives, for the c-oriented term,

    R > (log 2) * c^(1-eta) / log c.

Since 1-eta>1/M, this exceeds c^(1/M) for all sufficiently large c, so every
large Oesterle-M failure ``c>=R^M`` must also be a PCC_eta failure.

Stage 50 bounds PCC_eta failures through height X by O(X^(2-eta/2)).  Taking
eta arbitrarily close to 1-1/M yields the exponent

    3/2 + 1/(2M) + delta

for every delta>0 (within the nontrivial range; larger delta is automatic).

This is a deliberately elementary, noncompetitive almost-all abc estimate used
to close the P025 architecture loop.  Stronger exceptional-set results are
external prior art.
"""

from __future__ import annotations

from fractions import Fraction


def pcc_eta_margin_for_oesterle(M: Fraction, eta: Fraction) -> Fraction:
    """Return ``(1-eta)-1/M``; positivity is the asymptotic implication margin."""
    if not isinstance(M, Fraction) or M <= 1:
        raise ValueError("M must be a rational exponent >1")
    if not isinstance(eta, Fraction) or not Fraction(0, 1) < eta < Fraction(1, 1):
        raise ValueError("eta must lie strictly between zero and one")
    return Fraction(1, 1) - eta - Fraction(1, 1) / M


def almost_all_oesterle_exponent(M: Fraction, delta: Fraction) -> Fraction:
    """Return ``3/2+1/(2M)+delta`` from a near-optimal PCC eta choice.

    Choose ``eta=1-1/M-2*delta``.  Then Stage 50 gives

        2-eta/2 = 3/2+1/(2M)+delta.

    The function requires eta>0; for larger delta the stated big-O exponent is
    weaker and can be obtained trivially from a smaller positive eta.
    """
    if not isinstance(M, Fraction) or M <= 1:
        raise ValueError("M must be a rational exponent >1")
    if not isinstance(delta, Fraction) or delta <= 0:
        raise ValueError("delta must be positive")
    eta = Fraction(1, 1) - Fraction(1, 1) / M - 2 * delta
    if eta <= 0:
        raise ValueError("delta too large for the near-optimal positive eta construction")
    margin = pcc_eta_margin_for_oesterle(M, eta)
    if margin != 2 * delta:
        raise AssertionError("near-optimal eta lost Oesterle exponent margin")
    return Fraction(3, 2) + Fraction(1, 2) / M + delta


def near_optimal_pcc_eta(M: Fraction, delta: Fraction) -> Fraction:
    """Return the eta producing the displayed almost-all exponent."""
    exponent = almost_all_oesterle_exponent(M, delta)
    eta = 4 - 2 * exponent
    expected = Fraction(1, 1) - Fraction(1, 1) / M - 2 * delta
    if eta != expected:
        raise AssertionError("tail exponent inversion failed")
    return eta
