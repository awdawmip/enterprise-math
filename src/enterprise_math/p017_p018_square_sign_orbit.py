"""Sign-orbit invariance of fixed-cutoff square-phase observables.

The square-root diagonal leaves an apparently Archimedean datum: the relevant
common root is the literal small integer k.  This file records a sharp negative
boundary on how that datum may be used.

Fix a cutoff z and horizon H and put

    P_z = product_(p<=z) p,
    S_{z,H}(x) = #{1<=r<=H : gcd(x^2+r, P_z)=1}.

If x^2=k^2 (mod P_z), then S_{z,H}(x)=S_{z,H}(k) exactly.  For every odd prime
p<=z not dividing k, the local square-root equation permits the independent
sign choices x=+k or -k (mod p).  CRT therefore creates

    2^#{odd p<=z : p does not divide k}

distinct residue classes modulo P_z with the same fixed-cutoff square phase and
hence the same entire rough-survivor pattern.  Primes p|k contribute only the
zero root, and p=2 has only one residue-class sign.

Thus a fixed-cutoff language based only on x^2 modulo the wheel cannot detect
which CRT lift is small.  To exploit the Legendre diagonal one must use the
moving self-reference

    evaluation point x = cutoff z,
    horizon H = 2x,

or an equivalent operation that changes the future language when x changes.
Replacing k by a huge sign-twisted lift while keeping z=k and H=2k preserves
all fixed-cutoff observations, so lift height is not encoded there.

This is an information boundary, not a proof or disproof of Legendre's
conjecture.
"""

from __future__ import annotations

from itertools import product
from math import gcd

from .legendre import primes_up_to


def primorial(limit: int) -> int:
    """Return the square-free product of primes <=limit."""
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    wheel = 1
    for p in primes_up_to(limit):
        wheel *= p
    return wheel


def fixed_cutoff_square_survivors(x: int, cutoff: int, horizon: int) -> tuple[int, ...]:
    """Return offsets r<=horizon with x^2+r coprime to the cutoff wheel."""
    if isinstance(x, bool) or not isinstance(x, int):
        raise ValueError("x must be an integer")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a nonnegative integer")
    wheel = primorial(cutoff)
    return tuple(
        r for r in range(1, horizon + 1) if gcd(x * x + r, wheel) == 1
    )


def square_sign_orbit(k: int, cutoff: int) -> dict[str, object]:
    """Enumerate CRT classes x mod P_cutoff satisfying x^2=k^2 mod P_cutoff.

    This routine is intended for bounded regressions; the orbit grows
    exponentially with the number of non-anchor odd primes.
    """
    if isinstance(k, bool) or not isinstance(k, int):
        raise ValueError("k must be an integer")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")

    primes = tuple(primes_up_to(cutoff))
    wheel = primorial(cutoff)
    local_choices: list[tuple[int, tuple[int, ...]]] = []
    free_odd_primes: list[int] = []

    for p in primes:
        residue = k % p
        if p == 2 or residue == 0:
            choices = (residue,)
        else:
            choices = tuple(sorted({residue, (-residue) % p}))
            if len(choices) != 2:
                raise AssertionError("non-anchor odd prime lost its two sign roots")
            free_odd_primes.append(p)
        local_choices.append((p, choices))

    orbit: set[int] = set()
    for signs in product(*(choices for _p, choices in local_choices)):
        x = 0
        modulus = 1
        for (p, _choices), residue in zip(local_choices, signs):
            correction = ((residue - x) * pow(modulus, -1, p)) % p if modulus > 1 else residue
            x = (x + modulus * correction) % (modulus * p)
            modulus *= p
        if modulus != wheel:
            raise AssertionError("sign-orbit CRT modulus mismatch")
        if (x * x - k * k) % wheel != 0:
            raise AssertionError("sign-orbit class lost its square phase")
        orbit.add(x)

    expected = 1 << len(free_odd_primes)
    if len(orbit) != expected:
        raise AssertionError("sign-orbit multiplicity failed to factor locally")

    return {
        "k": k,
        "cutoff": cutoff,
        "wheel": wheel,
        "free_odd_primes": tuple(free_odd_primes),
        "orbit": tuple(sorted(orbit)),
        "orbit_size": len(orbit),
        "expected_orbit_size": expected,
        "all_classes_share_square_phase": True,
    }


def verify_fixed_cutoff_orbit_invariance(k: int, cutoff: int, horizon: int) -> dict[str, object]:
    """Verify that every sign-twisted CRT lift has the same survivor offsets."""
    data = square_sign_orbit(k, cutoff)
    baseline = fixed_cutoff_square_survivors(k, cutoff, horizon)
    patterns = tuple(
        fixed_cutoff_square_survivors(x, cutoff, horizon) for x in data["orbit"]
    )
    if any(pattern != baseline for pattern in patterns):
        raise AssertionError("fixed-cutoff survivor pattern changed along a sign orbit")
    return {
        **data,
        "horizon": horizon,
        "survivor_offsets": baseline,
        "survivor_count": len(baseline),
        "fixed_cutoff_orbit_invariant": True,
        "moving_diagonal_data_required": True,
    }
