"""Square covering height and its exact relation to Legendre failure.

For y>=2 let

    P_y = product_(p<=y) p

and call x a fixed-y square covering root when

    gcd(x^2+r, P_y) > 1              for every 1<=r<=2y.

Define the square covering height

    h(y) = min{x>=1 : x is a fixed-y square covering root},

with h(y)=infinity if no such root exists.

Two elementary facts turn h into an exact global reformulation of Legendre's
conjecture.

(1) Bertrand floor.  Every fixed-y covering root satisfies x^2>=y.  If x^2<y,
Bertrand's postulate supplies a prime q with y<q<2y.  Then

    1 <= q-x^2 <= 2y,

and q>y is coprime to P_y, contradicting full coverage.

(2) Diagonal implication.  If a fixed-y covering root has x<=y, then (1) gives
x^2>=y.  The first 2x offsets are part of the fixed-y covered horizon.  Every
number x^2+r there is >y, so if one were prime it would be coprime to P_y.
Thus all 1<=r<=2x are composite and the consecutive-square interval at x is a
Legendre counterexample.

Conversely, if y itself is a Legendre counterexample, then every
``y^2+r`` with 1<=r<=2y is composite and has a prime factor <=y, so x=y is a
fixed-y covering root.

Therefore

    Legendre holds for every k
      iff
    h(y)>y for every y.

More locally, ``h(y)<=y`` is equivalent to the existence of a Legendre
counterexample at some x<=y.

This reformulation does not solve the height inequality.  Its purpose is to
isolate the genuinely Archimedean invariant left after fixed-cutoff phase data
and CRT sign compatibility have been shown insufficient.
"""

from __future__ import annotations

from math import gcd, isqrt

from .legendre import (
    bounded_common_root_witness,
    direct_square_interval_prime_count,
    primes_up_to,
)
from .p017_p018_square_sign_orbit import primorial, square_sign_orbit


def is_fixed_y_square_covering_root(x: int, y: int) -> bool:
    """Return whether x^2+1,...,x^2+2y are all hit by primes <=y."""
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer")
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")
    wheel = primorial(y)
    return all(gcd(x * x + r, wheel) > 1 for r in range(1, 2 * y + 1))


def bertrand_survivor_below_sqrt_y(x: int, y: int) -> dict[str, int | bool]:
    """Exhibit a prime survivor whenever x^2<y.

    This executable helper finds the Bertrand prime by finite search.  The
    mathematical existence statement is the classical Bertrand postulate.
    """
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer")
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")
    if x * x >= y:
        raise ValueError("Bertrand floor helper requires x^2<y")

    q = next((p for p in primes_up_to(2 * y) if y < p < 2 * y), None)
    if q is None:
        raise AssertionError("finite Bertrand witness was not found")
    r = q - x * x
    if not (1 <= r <= 2 * y):
        raise AssertionError("Bertrand prime missed the fixed-y horizon")
    if gcd(q, primorial(y)) != 1:
        raise AssertionError("prime above y was not coprime to P_y")
    return {
        "x": x,
        "y": y,
        "prime_survivor": q,
        "offset": r,
        "rules_out_cover": True,
    }


def covering_root_at_or_below_diagonal_forces_counterexample(
    x: int, y: int
) -> dict[str, int | bool]:
    """Verify: fixed-y cover with x<=y forces a Legendre counterexample at x."""
    if isinstance(x, bool) or not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer")
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")
    if x > y:
        raise ValueError("the diagonal implication requires x<=y")
    if not is_fixed_y_square_covering_root(x, y):
        raise ValueError("x is not a fixed-y square covering root")

    if x * x < y:
        # This branch is mathematically impossible by Bertrand; expose the
        # concrete survivor if an upstream change ever violates the premise.
        witness = bertrand_survivor_below_sqrt_y(x, y)
        raise AssertionError(
            f"cover contradicts Bertrand survivor {witness['prime_survivor']}"
        )

    # Since x^2>=y, every state in the x-square interval is strictly above y.
    wheel = primorial(y)
    for r in range(1, 2 * x + 1):
        value = x * x + r
        if value <= y:
            raise AssertionError("diagonal covered state did not lie above cutoff")
        if gcd(value, wheel) == 1:
            raise AssertionError("fixed-y cover lost an offset from the x interval")

    prime_count = direct_square_interval_prime_count(x)
    if prime_count != 0:
        raise AssertionError("fixed-y diagonal cover failed to force a prime-free interval")
    return {
        "x": x,
        "y": y,
        "x_squared_at_least_y": True,
        "prime_count_at_x": prime_count,
        "legendre_counterexample_at_x": True,
    }


def bounded_square_covering_height(y: int, max_x: int) -> dict[str, object]:
    """Search h(y) only up to max_x; absence above max_x is not asserted."""
    if isinstance(y, bool) or not isinstance(y, int) or y < 2:
        raise ValueError("y must be an integer >=2")
    if isinstance(max_x, bool) or not isinstance(max_x, int) or max_x < 1:
        raise ValueError("max_x must be a positive integer")
    first = next(
        (x for x in range(1, max_x + 1) if is_fixed_y_square_covering_root(x, y)),
        None,
    )
    return {
        "y": y,
        "searched_through": max_x,
        "first_covering_root_in_search": first,
        "no_covering_root_in_search": first is None,
        "bertrand_floor": isqrt(y - 1) + 1,
    }


def bounded_common_root_minimum_sign_lift() -> dict[str, object]:
    """Minimize the existing y=73 covering witness over its square sign orbit.

    The legacy witness supplies one covering root for y=73.  Every sign-twisted
    square root modulo P_73 has the same fixed-cutoff cover.  Enumerating its
    finite 2^17 orbit gives a much smaller, but still enormous, covering root.
    This is bounded experimental/certificate data, not a theorem about h(73):
    another square phase could in principle have a smaller covering root.
    """
    y, witness_root, wheel = bounded_common_root_witness()
    if y != 73 or wheel != primorial(y):
        raise AssertionError("legacy bounded-common-root witness changed")

    orbit = square_sign_orbit(witness_root, y)
    positive = tuple(x for x in orbit["orbit"] if int(x) > 0)
    minimum = min(int(x) for x in positive)
    expected = 54983378811556946852865
    if minimum != expected:
        raise AssertionError("y=73 covering sign-orbit minimum changed")
    if not is_fixed_y_square_covering_root(minimum, y):
        raise AssertionError("minimum sign lift lost the legacy full cover")

    sqrt_wheel = isqrt(wheel)
    return {
        "y": y,
        "legacy_root": witness_root,
        "wheel": wheel,
        "free_sign_primes": orbit["free_odd_primes"],
        "orbit_size": orbit["orbit_size"],
        "minimum_positive_sign_lift": minimum,
        "minimum_over_y_ratio": minimum / y,
        "minimum_over_floor_sqrt_wheel_ratio": minimum / sqrt_wheel,
        "full_cover_verified": True,
        "not_a_global_h_y_minimality_claim": True,
    }
