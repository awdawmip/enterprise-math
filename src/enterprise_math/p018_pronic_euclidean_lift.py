"""Exact Euclidean lift of the pronic center k(k+1).

This is an application-local P018 primitive used by the P017×P018 thin-strip
analysis.  Generic congruence already implies that polynomial evaluation respects
remainder classes; the useful extra coordinate here is the explicit quotient
correction.

Write

    k = a n + b,      0 <= b < n,
    b(b+1) = c n + t, 0 <= t < n.

Then

    k(k+1)
      = n [a^2 n + a(2b+1) + c] + t,

so exactly

    R_n(k(k+1)) = t = R_n(b(b+1)),
    Q_n(k(k+1)) = a^2 n + a(2b+1) + c
                = a(2k-an+1) + Q_n(b(b+1)).

Thus the remainder future of the large pronic center collapses completely to the
small remainder b=R_n(k); the quotient requires only one explicit affine lift.
For a finite divisor future d, Q_n(k(k+1)) mod d is therefore recoverable from
(a mod d,b,c), while the pronic remainder is t.

This does not prove any prime-gap statement.  It is a finite quotient/remainder
state transport lemma for the Euclidean thin-strip chart.
"""

from __future__ import annotations


def pronic_euclidean_lift(k: int, n: int) -> dict[str, int | bool]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 0:
        raise ValueError("k must be a nonnegative integer")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    a, b = divmod(k, n)
    c, t = divmod(b * (b + 1), n)
    center = k * (k + 1)
    Q, R = divmod(center, n)
    lifted_Q = a * a * n + a * (2 * b + 1) + c
    affine_Q = a * (2 * k - a * n + 1) + c

    if R != t:
        raise AssertionError("pronic remainder did not collapse through R_n(k)")
    if Q != lifted_Q or Q != affine_Q:
        raise AssertionError("pronic quotient lift formula failed")
    if not (0 <= b < n and 0 <= t < n):
        raise AssertionError("Euclidean coordinates escaped canonical ranges")
    if c > b:
        raise AssertionError("secondary pronic quotient exceeded the first remainder")

    return {
        "k": k,
        "n": n,
        "center": center,
        "k_quotient_a": a,
        "k_remainder_b": b,
        "small_pronic_quotient_c": c,
        "small_pronic_remainder_t": t,
        "center_quotient_Q": Q,
        "center_remainder_R": R,
        "remainder_collapses_to_small_pronic": True,
        "quotient_lift_exact": True,
    }


def pronic_divisor_future_state(k: int, n: int, d: int) -> dict[str, int | bool]:
    """Return the finite state needed for Q_n(k(k+1)) mod d and R_n(k(k+1))."""
    if isinstance(d, bool) or not isinstance(d, int) or d < 1:
        raise ValueError("d must be a positive integer")
    data = pronic_euclidean_lift(k, n)
    a = int(data["k_quotient_a"])
    b = int(data["k_remainder_b"])
    c = int(data["small_pronic_quotient_c"])
    t = int(data["small_pronic_remainder_t"])
    Q = int(data["center_quotient_Q"])
    reconstructed_mod_d = ((a % d) * (2 * k - a * n + 1) + c) % d
    if reconstructed_mod_d != Q % d:
        raise AssertionError("finite pronic future state lost quotient modulo d")
    return {
        **data,
        "d": d,
        "a_mod_d": a % d,
        "Q_mod_d": Q % d,
        "reconstructed_Q_mod_d": reconstructed_mod_d,
        "future_remainder_t": t,
        "finite_divisor_future_state_exact": True,
    }
