"""Archimedean height gap for simultaneous square-phase CRT roots.

Earlier square-phase work deliberately avoided claiming that the distinguished
integer k was the least positive CRT root before such a statement had been
proved.  For the *complete simultaneous square congruence* there is a simple
criterion which now settles that point.

Let

    P_z = product_(p<=z) p

and suppose P_z>k^2.  If a positive representative x in [1,P_z) satisfies

    x^2 = k^2 (mod P_z),

then either x=k or

    x >= sqrt(P_z+k^2).

Indeed P_z divides x^2-k^2.  A solution 0<x<k would give the nonzero multiple
k^2-x^2 of P_z strictly between 0 and P_z, impossible.  A solution x>k is
either x=k or has x^2-k^2>=P_z.

Thus, under P_z>k^2, k is the unique least positive representative of its
square-phase sign orbit and every nontrivial sign-twisted lift is separated by
an immediate jump to square-root-of-primorial scale.

This height theorem does not undo the fixed-cutoff invariance theorem: all of
those huge lifts still have exactly the same x^2 modulo P_z and therefore the
same fixed-cutoff survivor pattern.  The only possible proof leverage is in a
language that couples the representative's actual height back into the moving
cutoff/horizon.
"""

from __future__ import annotations

from math import isqrt

from .p017_p018_square_sign_orbit import primorial, square_sign_orbit


def square_phase_lift_height_gap(k: int, cutoff: int) -> dict[str, object]:
    """Verify the exact height gap when the cutoff primorial exceeds k^2."""
    if isinstance(k, bool) or not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")

    wheel = primorial(cutoff)
    if wheel <= k * k:
        raise ValueError("height-gap theorem requires P_cutoff > k^2")

    # The exact integer threshold for x^2 >= P+k^2.
    target = wheel + k * k
    lower_bound = isqrt(target)
    if lower_bound * lower_bound < target:
        lower_bound += 1

    # Bounded enumeration is only used when the orbit is reasonably small.
    data = square_sign_orbit(k, cutoff)
    orbit = tuple(int(x) for x in data["orbit"])
    positive = tuple(sorted(x for x in orbit if x > 0))
    if k % wheel not in orbit:
        raise AssertionError("distinguished root is absent from its sign orbit")
    if not positive or positive[0] != k:
        raise AssertionError("k is not the least positive square-phase lift")

    nontrivial = tuple(x for x in positive if x != k)
    if any(x < lower_bound for x in nontrivial):
        raise AssertionError("nontrivial square-phase lift entered the forbidden height gap")

    return {
        **data,
        "distinguished_root": k,
        "primorial_exceeds_k_squared": True,
        "least_positive_lift": positive[0],
        "nontrivial_lift_lower_bound": lower_bound,
        "nontrivial_positive_lifts": nontrivial,
        "height_gap_verified": True,
    }


def prove_height_gap_for_residue(x: int, k: int, cutoff: int) -> dict[str, object]:
    """Check the height dichotomy without enumerating the full sign orbit."""
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer")
    if isinstance(k, bool) or not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    wheel = primorial(cutoff)
    if wheel <= k * k:
        raise ValueError("height-gap theorem requires P_cutoff > k^2")
    if (x * x - k * k) % wheel != 0:
        raise ValueError("x is not in the square-phase root class of k")

    if x < k:
        raise AssertionError("P>k^2 forbids a smaller positive square-phase lift")
    if x == k:
        return {
            "x": x,
            "k": k,
            "wheel": wheel,
            "distinguished": True,
            "height_gap_verified": True,
        }

    if x * x - k * k < wheel:
        raise AssertionError("nontrivial lift failed the P-divisibility height bound")
    return {
        "x": x,
        "k": k,
        "wheel": wheel,
        "distinguished": False,
        "height_gap_verified": True,
    }
