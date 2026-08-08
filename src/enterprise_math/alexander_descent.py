"""Alexander-dual threshold descent for the Legendre pressure test.

The combinatorial Alexander-duality theorem is established mathematics.  This
module specializes it to finite square-free prime-product threshold complexes
and records the extra half-scale bound forced by a consecutive-square basin.
Nothing here proves Legendre's conjecture.
"""

from __future__ import annotations

from .core import integer_nth_root
from .cutoff_pairing import mobius_divisor_tail


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def _require_distinct_primes(primes: list[int]) -> None:
    if not primes:
        raise ValueError("primes must be nonempty")
    if len(primes) != len(set(primes)):
        raise ValueError("primes must be distinct")
    for p in primes:
        if isinstance(p, bool) or not isinstance(p, int) or p < 2:
            raise ValueError("primes must contain integers >= 2")


def squarefree_product(primes: list[int]) -> int:
    """Return the product of a nonempty distinct-prime support."""
    _require_distinct_primes(primes)
    product = 1
    for p in primes:
        product *= p
    return product


def alexander_dual_threshold(primes: list[int], threshold: int) -> int:
    """Return the exact multiplicative threshold of the Alexander dual.

    For G=product(primes) and K(G,T)={F: product(F)<=T}, with G>T>=1,

        K(G,T)^* = K(G, floor((G-1)/T)).

    The strict complement condition G/product(F)>T is the reason for ``G-1``.
    """
    _require_positive("threshold", threshold)
    product = squarefree_product(primes)
    if product <= threshold:
        raise ValueError("the full support must lie above the threshold")
    return (product - 1) // threshold


def alexander_dual_tail_identity(
    primes: list[int], threshold: int
) -> tuple[int, int, int, int]:
    """Return both sides of the exact Alexander-dual Möbius-tail identity.

    If r is the number of support primes and T* is the dual threshold, then

        Tail(G,T) = (-1)^(r-3) Tail(G,T*).

    The return value is ``(tail, dual_threshold, dual_tail, signed_dual_tail)``.
    """
    dual_threshold = alexander_dual_threshold(primes, threshold)
    tail = mobius_divisor_tail(primes, threshold)
    dual_tail = mobius_divisor_tail(primes, dual_threshold)
    sign = -1 if (len(primes) - 3) % 2 else 1
    return tail, dual_threshold, dual_tail, sign * dual_tail


def square_basin_half_scale_bound(k: int) -> int:
    """Return the exact universal upper bound floor((k+1)/2)."""
    _require_positive("k", k)
    return (k + 1) // 2


def square_basin_dual_threshold(
    k: int, n: int, primes: list[int]
) -> tuple[int, int]:
    """Return the per-state dual threshold and its square-basin upper bound.

    ``n`` must be an interior state k^2<n<(k+1)^2 and every support prime must
    divide n.  For G=product(primes)>2k,

        T* = floor((G-1)/(2k)) <= floor((k+1)/2).
    """
    _require_positive("k", k)
    _require_positive("n", n)
    _require_distinct_primes(primes)
    if not (k * k < n < (k + 1) * (k + 1)):
        raise ValueError("n must lie strictly between consecutive squares")
    if any(n % p != 0 for p in primes):
        raise ValueError("every support prime must divide n")
    product = squarefree_product(primes)
    threshold = 2 * k
    if product <= threshold:
        raise ValueError("the support product must cross the large cutoff")
    dual_threshold = (product - 1) // threshold
    upper = square_basin_half_scale_bound(k)
    if dual_threshold > upper:
        raise AssertionError("square-basin half-scale bound violated")
    return dual_threshold, upper


def large_divisor_cofactor_descent(k: int, n: int, divisor: int) -> tuple[int, int]:
    """Return the cofactor of any divisor above 2k and the half-scale bound.

    If n is in the square-basin interior, divisor|n, and divisor>2k, then

        n/divisor <= floor((k+1)/2).
    """
    _require_positive("k", k)
    _require_positive("n", n)
    _require_positive("divisor", divisor)
    if not (k * k < n < (k + 1) * (k + 1)):
        raise ValueError("n must lie strictly between consecutive squares")
    if n % divisor != 0:
        raise ValueError("divisor must divide n")
    if divisor <= 2 * k:
        raise ValueError("divisor must lie above the 2k cutoff")
    cofactor = n // divisor
    upper = square_basin_half_scale_bound(k)
    if cofactor > upper:
        raise AssertionError("large-divisor cofactor failed to descend")
    return cofactor, upper


def cutoff_edge_cofactor_window(
    k: int, n: int, least_prime: int, reduced_divisor: int
) -> tuple[int, int]:
    """Return the cofactor on a cutoff edge and verify its exact window.

    For b=p*c with c<=2k<p*c and b|n, n in the square basin,

        2*p*h >= k+1,
        h <= floor((k+1)/2),

    where h=n/b.
    """
    _require_positive("least_prime", least_prime)
    _require_positive("reduced_divisor", reduced_divisor)
    boundary = least_prime * reduced_divisor
    if reduced_divisor > 2 * k or boundary <= 2 * k:
        raise ValueError("the divisor pair must cross the 2k cutoff")
    cofactor, upper = large_divisor_cofactor_descent(k, n, boundary)
    if 2 * least_prime * cofactor < k + 1:
        raise AssertionError("cutoff-edge lower cofactor bound violated")
    return cofactor, upper


def alexander_dual_dimension(vertex_count: int, dimension: int) -> int:
    """Return the homological dimension paired by combinatorial Alexander duality."""
    _require_positive("vertex_count", vertex_count)
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < -1:
        raise ValueError("dimension must be an integer >= -1")
    return vertex_count - dimension - 3


def two_sided_root_bounds(
    primes: list[int], threshold: int, dimension: int
) -> tuple[int, int | None, int]:
    """Return the original and Alexander-dual necessary least-prime bounds.

    This helper is intended for a homology dimension known to be nonzero.
    The original quota shell gives p<=R_{s+1}(T).  Combinatorial Alexander
    duality sends it to dimension r-s-3 at T*.  When that dual dimension is
    nonnegative, the dual shell gives

        p<=R_{r-s-2}(T*).

    The return value is ``(original_bound, dual_bound_or_None, dual_threshold)``.
    """
    _require_distinct_primes(primes)
    _require_positive("threshold", threshold)
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 0:
        raise ValueError("dimension must be a non-negative integer")
    dual_threshold = alexander_dual_threshold(primes, threshold)
    original_bound = integer_nth_root(threshold, dimension + 1)
    dual_dimension = alexander_dual_dimension(len(primes), dimension)
    if dual_dimension < 0:
        return original_bound, None, dual_threshold
    dual_bound = integer_nth_root(dual_threshold, dual_dimension + 1)
    return original_bound, dual_bound, dual_threshold


def legendre_one_dimensional_root_squeeze(
    k: int, n: int, primes: list[int]
) -> tuple[int, int | None, int, int]:
    """Specialize the two-sided bound to the leading negative 1D shell layer.

    For a state support whose 1-dimensional threshold homology is nonzero,
    the necessary bounds are

        p<=R_2(2k)

    and, for support size r>=4,

        p<=R_{r-3}(T*) <= R_{r-3}(floor((k+1)/2)).

    The caller is responsible for establishing that beta_1 is nonzero.
    """
    dual_threshold, half_scale = square_basin_dual_threshold(k, n, primes)
    original, dual, recomputed = two_sided_root_bounds(primes, 2 * k, 1)
    if recomputed != dual_threshold:
        raise AssertionError("dual thresholds disagree")
    return original, dual, dual_threshold, half_scale
