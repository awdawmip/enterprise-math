"""Finite cubic full-forcing band arithmetic for R005-B.

This module combines the lower-cofactor finite closure with an independent
uniform post-horizon gap cap.  External gap caps themselves are premises of the
companion research note; the functions here are exact integer reductions only.
"""

from math import isqrt

from .prime_collapse_field import factor_horizon


def cubic_upper_closed_by_gap_cap(k: int, max_gap: int) -> bool:
    """Return whether a uniform post-horizon gap cap closes the cubic upper band.

    Put A=k^3, U=(k+1)^3-1, S=floor(sqrt(A)), F=floor(sqrt(U)).  If the next
    prime after F satisfies R-F<=G, then an upper pure-cap obstruction can only
    exist if

        (F+G)*S > U.

    Thus ``(F+G)*S<=U`` is an exact sufficient certificate that every cubic
    upper-band candidate is forced.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if max_gap <= 0:
        raise ValueError("max_gap must be positive")
    upper = (k + 1) ** 3 - 1
    root_lower = isqrt(k**3)
    horizon = factor_horizon(k, 3)
    return (horizon + max_gap) * root_lower <= upper


def cubic_last_upper_not_closed_by_gap_cap(k_limit: int, max_gap: int) -> int:
    """Return the last k<=k_limit not closed by the selected uniform gap cap.

    This is a finite exact scan because the threshold has integer carry teeth
    and need not be monotone at every adjacent k.
    """
    if k_limit < 1:
        raise ValueError("k_limit must be positive")
    last = 0
    for k in range(1, k_limit + 1):
        if not cubic_upper_closed_by_gap_cap(k, max_gap):
            last = k
    return last


def cubic_upper_certificate_kind(k: int, q: int, max_gap: int) -> str:
    """Return the certificate form guaranteed for one upper-band candidate.

    Preconditions: q is a positive integer candidate with q*F>A and the selected
    uniform gap cap closes the upper band at k.

    - if q^2>A, q^2 itself lies in the basin and has singleton q-support;
    - otherwise q<=S and q*(F+G)<=S*(F+G)<=U, so the actual next prime R<=F+G
      gives the e=1 singleton-support certificate qR.

    The function reports only which proof branch applies; it does not compute R.
    """
    if k < 1 or q < 2:
        raise ValueError("require positive k and q>=2")
    lower = k**3
    horizon = factor_horizon(k, 3)
    if q > horizon or q * horizon <= lower:
        raise ValueError("q must lie in the cubic upper candidate band")
    if not cubic_upper_closed_by_gap_cap(k, max_gap):
        raise ValueError("selected gap cap does not close the upper band at k")
    return "SQUARE" if q * q > lower else "NEXT_PRIME"
