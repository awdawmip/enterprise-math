"""Quartic Euclidean support bound for nonzero mixed Walsh boundary.

Let k>=3, K=k-1 and

    H=floor(k/2),

so the positive odd radii 1<=r<k are r=2t+1 with 0<=t<H.  For an odd
squarefree conductor q write

    H=A*q+h,       0<=h<q.

A nonconstant orientation root cube has zero contribution from every complete
q-block in the t-coordinate.  Hence its finite boundary depends only on the
prefix 0<=t<h.

Suppose a mixed split q=a*b with (a,b)=1 hits one boundary index t<h:

    a | M-(2t+1),
    b | M+(2t+1),
    M=k(k+1).

Substituting H=Aq+h reduces M modulo both a and b to a positive quadratic in h.
For even k=2H,

    M == 2h(2h+1) (mod a,b),

while for odd k=2H+1,

    M == 2(h+1)(2h+1) (mod a,b).

In either parity, the positive representatives of M-(2t+1) and M+(2t+1)
modulo the orientation factors are strictly below

    4(h+1)^2.

Therefore every actual mixed boundary hit satisfies

    a < 4(h+1)^2,
    b < 4(h+1)^2,
    q=ab < 16(h+1)^4.

Thus a nonzero mixed conductor q forces the Euclidean boundary prefix to have
quartic-root length h > q^(1/4)/2 - 1.  If b=min(a,b), then b<=sqrt(q) and the
same theorem gives h > sqrt(b)/2 - 1.  The reciprocal/Kloosterman denominator
is therefore automatically in a square-root-length regime.

This recovers the P018 fourth-root scale internally from the half-cutoff
orientation-Walsh boundary geometry.  It is an exact support theorem, not a
Kloosterman cancellation estimate and not a Legendre proof.
"""

from __future__ import annotations

from math import gcd


def positive_odd_radius_count(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    return k // 2


def mixed_boundary_euclidean_hit(k: int, conductor: int, a: int, b: int, t: int) -> dict[str, object]:
    """Verify the exact quartic support inequalities for one declared boundary hit."""
    for name, value in (("conductor", conductor), ("a", a), ("b", b), ("t", t)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if a <= 1 or b <= 1 or a * b != conductor or gcd(a, b) != 1:
        raise ValueError("require mixed coprime split q=a*b with a,b>1")
    if conductor % 2 == 0:
        raise ValueError("conductor must be odd")

    H = positive_odd_radius_count(k)
    block_count, h = divmod(H, conductor)
    if not (0 <= t < h):
        raise ValueError("t must lie in the incomplete boundary prefix 0<=t<h")
    radius = 2 * t + 1
    M = k * (k + 1)
    if (M - radius) % a or (M + radius) % b:
        raise ValueError("declared split does not hit this boundary radius")

    if k % 2 == 0:
        center_representative = 2 * h * (2 * h + 1)
        parity_kind = "EVEN_K"
    else:
        center_representative = 2 * (h + 1) * (2 * h + 1)
        parity_kind = "ODD_K"
    if (center_representative - M) % conductor:
        raise AssertionError("Euclidean center representative is not congruent to M mod q")

    lower_rep = center_representative - radius
    upper_rep = center_representative + radius
    if lower_rep <= 0 or upper_rep <= 0:
        raise AssertionError("boundary representatives must be positive")
    ceiling = 4 * (h + 1) * (h + 1)
    if not (lower_rep < ceiling and upper_rep < ceiling):
        raise AssertionError("orientation representative escaped quartic boundary ceiling")
    if lower_rep % a or upper_rep % b:
        raise AssertionError("orientation factors do not divide Euclidean representatives")
    if not (a < ceiling and b < ceiling and conductor < ceiling * ceiling):
        raise AssertionError("quartic conductor support bound failed")

    small = min(a, b)
    # Equivalent integer-safe square-root-length implication:
    # small < 4(h+1)^2.
    if not small < 4 * (h + 1) ** 2:
        raise AssertionError("small mixed denominator escaped square-root-length regime")

    return {
        "k": k,
        "center_M": M,
        "positive_odd_radius_count_H": H,
        "conductor_q": conductor,
        "block_count_floor_H_over_q": block_count,
        "boundary_prefix_h": h,
        "boundary_index_t": t,
        "radius": radius,
        "positive_factor_a": a,
        "negative_factor_b": b,
        "parity_kind": parity_kind,
        "euclidean_center_representative": center_representative,
        "lower_orientation_representative": lower_rep,
        "upper_orientation_representative": upper_rep,
        "factor_ceiling_4_hplus1_sq": ceiling,
        "conductor_ceiling_16_hplus1_pow4": ceiling * ceiling,
        "small_mixed_denominator": small,
        "quartic_boundary_support": True,
        "small_denominator_square_root_length": True,
    }


def quartic_boundary_implication(h: int, conductor: int) -> dict[str, int | bool]:
    """Return the integer form q<16(h+1)^4 => h is quartic-root scale for q."""
    if h < 0 or conductor < 1:
        raise ValueError("h must be nonnegative and conductor positive")
    ceiling = 16 * (h + 1) ** 4
    return {
        "boundary_prefix_h": h,
        "conductor_q": conductor,
        "quartic_ceiling": ceiling,
        "compatible_with_nonzero_mixed_boundary": conductor < ceiling,
    }
