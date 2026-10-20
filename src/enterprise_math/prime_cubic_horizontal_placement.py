"""Exact horizontal certificate-placement coordinates for cubic R005-B.

The functions in this module compile where two declared certificate resources
act on the lower cofactor band q>k:

* an exhaustive cofactor-gap certificate valid below an integer scale X;
* an effective relative prime-interval row valid from an integer scale x0 and
  with interval parameter Delta.

No external prime theorem or database is verified here.
"""

from math import isqrt


def cubic_bounds(k: int) -> tuple[int, int, int]:
    """Return (A,U,F) for the cubic basin."""
    if k < 1:
        raise ValueError("k must be positive")
    a = k**3
    u = (k + 1) ** 3 - 1
    return a, u, isqrt(u)


def lower_band_q_max(k: int) -> int:
    """Largest integer q satisfying q*F_3(k)<=k^3."""
    a, _, f = cubic_bounds(k)
    return a // f


def horizontal_cofactor_upper_scale_max(k: int) -> int:
    """Largest floor(U/q) over integer q>k.

    The maximum is attained at q=k+1 and equals (k+1)^2-1.
    """
    if k < 1:
        raise ValueError("k must be positive")
    return (k + 1) ** 2 - 1


def database_overflow_q_max(k: int, coverage_limit: int) -> int:
    """Largest integer q whose lower cofactor point A/q is not below X.

    A database valid for gap starts below X automatically covers q when
    A/q<X, equivalently q>floor(A/X).  Thus possible overflow has q<=A//X.
    """
    if coverage_limit <= 0:
        raise ValueError("coverage_limit must be positive")
    return k**3 // coverage_limit


def effective_row_q_max(k: int, scale_min: int) -> int:
    """Largest q whose cofactor upper endpoint U/q reaches integer scale x0."""
    if scale_min <= 0:
        raise ValueError("scale_min must be positive")
    _, u, _ = cubic_bounds(k)
    return u // scale_min


def effective_row_fits_cubic(k: int, delta: int) -> bool:
    """Exact q-independent relative-width fit condition."""
    if delta <= 1:
        raise ValueError("delta must exceed 1")
    return 3 * (k + 1) * (delta - 1) > k * k


def effective_row_visible_horizontally(k: int, scale_min: int) -> bool:
    """Whether any integer q>k has U/q>=x0."""
    if scale_min <= 0:
        raise ValueError("scale_min must be positive")
    _, u, _ = cubic_bounds(k)
    return scale_min * (k + 1) <= u


def real_seam_sufficient(k: int, coverage_limit: int, scale_min: int) -> bool:
    """Sufficient real-valued no-hole condition between database and row.

    Database coverage starts when q>A/X; effective coverage reaches through
    q<=U/x0.  The real intervals overlap when A/X<=U/x0, i.e. x0*A<=X*U.
    """
    if coverage_limit <= 0 or scale_min <= 0:
        raise ValueError("scales must be positive")
    a, u, _ = cubic_bounds(k)
    return scale_min * a <= coverage_limit * u


def unresolved_lower_q_interval(
    k: int,
    coverage_limit: int,
    *,
    scale_min: int | None = None,
    delta: int | None = None,
) -> tuple[int, int]:
    """Return exact integer q cursor not covered by the declared resources.

    The interval is restricted to q>k and the lower cofactor band qF<=A.
    Database overflow requires q<=floor(A/X).  If a supplied effective row is
    both horizontally visible and strong enough, it covers q<=floor(U/x0), so
    the unresolved cursor starts one integer later.

    An empty cursor is represented by lower>upper.
    """
    if coverage_limit <= 0:
        raise ValueError("coverage_limit must be positive")
    hi = min(lower_band_q_max(k), database_overflow_q_max(k, coverage_limit))
    lo = k + 1
    if (scale_min is None) != (delta is None):
        raise ValueError("scale_min and delta must be supplied together")
    if scale_min is not None and delta is not None:
        if effective_row_visible_horizontally(k, scale_min) and effective_row_fits_cubic(k, delta):
            lo = max(lo, effective_row_q_max(k, scale_min) + 1)
    return lo, hi


def unresolved_lower_q_width(*args, **kwargs) -> int:
    """Number of integer coordinates in the unresolved cursor."""
    lo, hi = unresolved_lower_q_interval(*args, **kwargs)
    return max(0, hi - lo + 1)


def square_boundary_cursor_width(boundary_k: int, offset: int) -> int:
    """Exact database-overflow width for X=K^2 and k=K+d.

    For K>0,d>=0,

        floor((K+d)^3/K^2)-(K+d)
        = 2d + floor(3d^2/K + d^3/K^2).
    """
    if boundary_k <= 0 or offset < 0:
        raise ValueError("boundary_k must be positive and offset nonnegative")
    k = boundary_k + offset
    return k**3 // (boundary_k * boundary_k) - k


def linear_cursor_offset_limit(boundary_k: int) -> int:
    """Largest d for which the square-boundary cursor width is exactly 2d."""
    if boundary_k <= 0:
        raise ValueError("boundary_k must be positive")
    # Need 3*d^2/K + d^3/K^2 < 1.
    lo = 0
    hi = 1
    k = boundary_k
    while 3 * hi * hi * k + hi**3 < k * k:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if 3 * mid * mid * k + mid**3 < k * k:
            lo = mid
        else:
            hi = mid
    return lo
