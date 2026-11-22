"""Exact Euclidean chart for the P017×P018 thin square-basin strip.

This module records the exact integer coordinate change that straightens the
physical hyperbolic strip |mn-M|<k, with M=k(k+1), into a quotient/remainder
chart.  It also records the additive-reciprocity normalization of the associated
inverse-residue phase.

Fix a positive factor n and write

    M = n Q + t,      0 <= t < n.

Every integer m in the physical strip has a unique representation

    m = Q + j

with

    |n j - t| < k.

The opposite mirror state is then

    2M-mn = n(Q-j)+2t.

Hence for an odd divisor channel d coprime to n,

    d | 2M-mn
      iff
    j = Q + 2 t n^{-1}  (mod d).

Thus each dyadic n~N block becomes a finite chart of approximate dimensions

    N  x  (k/N),

so its physical lattice-point area is O(k), independent of the ambient height
M~k^2.  The exact object controlling future divisor refinements is the Euclidean
state (Q mod d,t), not the full center M.

There is a second exact normalization at the Fourier level.  Let (m,d)=1 and
let \bar m mod d and \bar d mod m denote multiplicative inverses.  The thin-strip
completion phase

    Phi = h M/(m d) - 2 M h \bar m/d

satisfies additive reciprocity

    Phi = 2 M h \bar d/m - h M/(m d)     (mod 1).

Writing

    M = m q + u,      0<=u<m,
    q = d a + v,      0<=v<d,

so that R_(md)(M)=m v+u, gives the exact finite-coordinate form

    Phi = 2 h u \bar d/m - h v/d - h u/(m d)       (mod 1)

or equivalently

    Phi = 2 h R_m(M) \bar d/m - h R_(md)(M)/(m d)  (mod 1).

The large height M disappears from the modular oscillation coefficients.  This
is a P018 quotient/remainder interface to the P017 parity-sensitive Walsh
analysis.  It is an exact representation theorem only; it does not assert a
Kloosterman bound, a Bombieri--Vinogradov theorem, or Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def euclidean_thin_strip_chart(k: int, n: int) -> dict[str, object]:
    """Return all exact m=Q+j states with |mn-M|<k for one factor n."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    M = k * (k + 1)
    Q, t = divmod(M, n)

    # Solve -k < n*j-t < k exactly.
    j_min = (-k + t) // n + 1
    j_max = (k - 1 + t) // n
    rows: list[dict[str, int]] = []
    for j in range(j_min, j_max + 1):
        m = Q + j
        if m <= 0:
            continue
        radius = m * n - M
        if not (-k < radius < k):
            raise AssertionError("Euclidean chart emitted a state outside the thin strip")
        opposite = 2 * M - m * n
        if opposite != n * (Q - j) + 2 * t:
            raise AssertionError("opposite-state Euclidean identity failed")
        rows.append(
            {
                "j": j,
                "m": m,
                "radius": radius,
                "state": m * n,
                "opposite_state": opposite,
            }
        )

    direct = tuple(
        m
        for m in range(max(1, (M - k) // n - 2), (M + k) // n + 3)
        if -k < m * n - M < k
    )
    chart = tuple(row["m"] for row in rows)
    if chart != direct:
        raise AssertionError("Euclidean strip chart did not equal direct thin-strip enumeration")

    return {
        "k": k,
        "center": M,
        "factor_n": n,
        "quotient_Q": Q,
        "remainder_t": t,
        "j_min": j_min,
        "j_max": j_max,
        "chart_width": len(rows),
        "rows": tuple(rows),
    }


def euclidean_divisor_channel(k: int, n: int, j: int, d: int) -> dict[str, object]:
    """Verify d|2M-mn iff j=Q+2t*n^{-1} mod d for one chart state."""
    if isinstance(d, bool) or not isinstance(d, int) or d < 1 or d % 2 == 0:
        raise ValueError("d must be a positive odd integer")
    data = euclidean_thin_strip_chart(k, n)
    row = next((row for row in data["rows"] if int(row["j"]) == j), None)
    if row is None:
        raise ValueError("j must belong to the physical thin-strip chart")
    if gcd(n, d) != 1:
        raise ValueError("channel theorem requires gcd(n,d)=1")

    Q = int(data["quotient_Q"])
    t = int(data["remainder_t"])
    inverse_n = pow(n, -1, d)
    channel = (Q + 2 * t * inverse_n) % d
    opposite = int(row["opposite_state"])
    direct = opposite % d == 0
    residue = j % d == channel
    if direct != residue:
        raise AssertionError("Euclidean divisor channel equivalence failed")
    return {
        **data,
        "selected_j": j,
        "divisor": d,
        "inverse_n_mod_d": inverse_n,
        "channel_residue": channel,
        "direct_divisibility": direct,
        "channel_selected": residue,
        "divisor_channel_identity": True,
    }


def reciprocity_integer(m: int, d: int) -> int:
    """Return the integer \bar m/d + \bar d/m - 1/(md)."""
    if isinstance(m, bool) or not isinstance(m, int) or m < 1:
        raise ValueError("m must be positive")
    if isinstance(d, bool) or not isinstance(d, int) or d < 1:
        raise ValueError("d must be positive")
    if gcd(m, d) != 1:
        raise ValueError("m and d must be coprime")
    inv_m = pow(m, -1, d)
    inv_d = pow(d, -1, m)
    numerator = inv_m * m + inv_d * d - 1
    if numerator % (m * d):
        raise AssertionError("additive reciprocity difference is not integral")
    return numerator // (m * d)


def euclidean_normalized_reciprocity_phase(
    center: int,
    m: int,
    d: int,
    h: int,
) -> dict[str, object]:
    """Verify the exact quotient/remainder normalization of the reciprocity phase.

    Returned phase values are Fractions.  Equality is asserted modulo integers,
    so no floating point or complex exponential is used.
    """
    if isinstance(center, bool) or not isinstance(center, int) or center < 1:
        raise ValueError("center must be a positive integer")
    if isinstance(h, bool) or not isinstance(h, int):
        raise ValueError("h must be an integer")
    if m < 1 or d < 1 or gcd(m, d) != 1:
        raise ValueError("m,d must be positive and coprime")

    inv_m = pow(m, -1, d)
    inv_d = pow(d, -1, m)
    original = Fraction(h * center, m * d) - Fraction(2 * center * h * inv_m, d)
    reciprocal = Fraction(2 * center * h * inv_d, m) - Fraction(h * center, m * d)
    if (original - reciprocal).denominator != 1:
        raise AssertionError("additive reciprocity phase identity failed modulo one")

    q, u = divmod(center, m)
    a, v = divmod(q, d)
    md_remainder = m * v + u
    if md_remainder != center % (m * d):
        raise AssertionError("nested Euclidean state did not reconstruct R_md(center)")

    normalized = (
        Fraction(2 * h * u * inv_d, m)
        - Fraction(h * v, d)
        - Fraction(h * u, m * d)
    )
    compact = Fraction(2 * h * u * inv_d, m) - Fraction(h * md_remainder, m * d)
    if normalized != compact:
        raise AssertionError("expanded and compact Euclidean phases disagree")
    if (reciprocal - normalized).denominator != 1:
        raise AssertionError("Euclidean normalized phase is not congruent modulo one")

    return {
        "center": center,
        "m": m,
        "d": d,
        "h": h,
        "inverse_m_mod_d": inv_m,
        "inverse_d_mod_m": inv_d,
        "quotient_q": q,
        "remainder_u": u,
        "nested_quotient_a": a,
        "nested_remainder_v": v,
        "remainder_mod_md": md_remainder,
        "original_phase": original,
        "reciprocal_phase": reciprocal,
        "euclidean_normalized_phase": normalized,
        "phase_difference_integer": int(reciprocal - normalized),
        "euclidean_phase_identity": True,
    }
