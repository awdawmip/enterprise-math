"""Quotient-strip smoothing/reuse Pareto for Euclidean Walsh aggregates.

Let m be a positive odd cross-orientation modulus in the physical positive-radius
world 1<=r<k.  Odd parity plus the CRT root conditions form one residue class
modulo 2m, so every fixed root pattern has capacity

    cap(k,m) <= floor((k-1)/(2m)) + 1.

For m<=k define the quotient strip

    a=floor(k/m)>=1.

Since k<(a+1)m,

    floor((k-1)/(2m))+1 <= floor(a/2)+1.

Thus the quotient variable used by the reciprocal-Mobius aggregate is also an
exact reuse-depth coordinate.

In p017_p018_walsh_mobius_harmonic_aggregate the second conductor axis is
compressed to

    H_A(a)=sum_(ell<=a, ell squarefree transverse, gcd(ell,A)=1) mu(ell)/ell.

Because every nontrivial transverse ell is odd and at least three,

    H_A(1)=H_A(2)=1.

These are the least-smoothed strips, but they have the smallest physical reuse:

* a=1: cap<=1, so every fixed root pattern is globally single-use;
* a=2: cap<=2;
* in general: cap<=floor(a/2)+1.

Therefore the apparent analytic hard core has a built-in Pareto: small quotient
strips have no reciprocal-Mobius cancellation but almost no reuse, while larger
strips allow more reuse but expose a richer Mobius future language.  The theorem
does not assert H_A(a) is small for every larger a and does not bound the sum of
all root patterns in a strip.
"""

from __future__ import annotations

from .p017_p018_walsh_mobius_harmonic_aggregate import reciprocal_mobius_kernel


def quotient_strip_index(k: int, modulus: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    return k // modulus


def odd_root_capacity(k: int, modulus: int) -> int:
    """Return the one-class modulo-2m capacity in 1<=r<k."""
    if quotient_strip_index(k, modulus) < 0:  # pragma: no cover
        raise AssertionError("unreachable")
    return (k - 1) // (2 * modulus) + 1


def quotient_strip_reuse_ceiling(k: int, modulus: int) -> dict[str, object]:
    """Return cap<=floor(a/2)+1 for a=floor(k/m), including the high a=0 case."""
    a = quotient_strip_index(k, modulus)
    capacity = odd_root_capacity(k, modulus)
    if a == 0:
        ceiling = 1
        if capacity > 1:
            raise AssertionError("m>k failed global single-use")
        regime = "HIGH_PRODUCT_SINGLE_USE"
    else:
        ceiling = a // 2 + 1
        if capacity > ceiling:
            raise AssertionError("quotient-strip reuse exceeded floor(a/2)+1")
        regime = "QUOTIENT_STRIP"
    return {
        "k": k,
        "cross_modulus_m": modulus,
        "quotient_strip_a": a,
        "exact_one_class_capacity_ceiling": capacity,
        "strip_reuse_ceiling": ceiling,
        "regime": regime,
        "quotient_controls_reuse": True,
    }


def first_two_strip_pareto(k: int, modulus: int, kernel_A: int = 1) -> dict[str, object]:
    """Expose H_A(a)=1 at a=1,2 and the matching reuse ceilings.

    kernel_A is the conductor product excluded from the reciprocal Mobius
    variable.  The exact reciprocal kernel implementation validates the value.
    """
    data = quotient_strip_reuse_ceiling(k, modulus)
    a = int(data["quotient_strip_a"])
    if a not in (1, 2):
        raise ValueError("declared modulus must lie in quotient strip a=1 or a=2")
    kernel = reciprocal_mobius_kernel(k, kernel_A, a)
    if kernel != 1:
        raise AssertionError("odd-transverse reciprocal kernel should equal one for a=1,2")
    expected_reuse = 1 if a == 1 else 2
    if int(data["strip_reuse_ceiling"]) != expected_reuse:
        raise AssertionError("first-two-strip reuse ceiling changed")
    return {
        **data,
        "reciprocal_mobius_kernel": kernel,
        "kernel_unsmoothed": True,
        "first_strip_single_use": a == 1,
        "second_strip_reuse_at_most_two": a == 2,
        "smoothing_reuse_pareto": True,
    }
