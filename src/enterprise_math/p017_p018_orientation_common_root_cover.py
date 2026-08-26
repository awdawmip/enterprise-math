"""Negative boundary: common +/-M mirror-root structure alone does not prevent coverage.

P017 L043 says that a physical prime-free mirror basin would be covered by two
orientation classes at each surviving radius:

    lower composite: p | M-r  <=> M = r  (mod p),
    upper composite: p | M+r  <=> M = -r (mod p).

One might hope that requiring all these classes to arise from the *same* residue
M modulo every small prime is already much stronger than an arbitrary covering.
It is not.

At k=73 there is an explicit assignment of one nonzero residue a_p modulo every
odd prime p<73 such that the classes a_p cover every signed odd radius

    {+/-1,+/-3,...,+/-71}.

By CRT these local residues come from one common integer M_0.  Therefore every
odd mirror state M_0-r and M_0+r has a divisor p<73; even offsets are composite
by parity after choosing an even lift of M_0.  Thus the common-root +/-M geometry
by itself allows a complete centered prime-free window.

For the stored witness the odd primorial is

    P = 278970415063349480483707695,

one CRT residue is

    186223063681305470464114469,

and the minimum centered representative has absolute height

    92747351382044010019593226.

The physical pronic center at the same k would be only

    k(k+1)=5402.

Hence the genuinely distinguishing input is the **low height / pronic diagonal**,
not merely that all +/- root classes share one CRT origin.

There is a precise prime-gap interpretation.  Any even common root M_0 whose
small-prime classes cover every signed odd radius |r|<k creates a prime-free
interval (M_0-k,M_0+k): odd offsets have a factor <k and even offsets are even.
Consequently any theorem asserting a prime in every sufficiently large interval
[x-x^theta,x] implies a root-height lower bound M_0 > k^(1/theta) (up to the
threshold/constants of that theorem).  The current 0.52 short-prime exponent
therefore corresponds to exponent 25/13 ~= 1.923 on root height, still below the
physical k^2 scale.  This shows why the root-height coordinate does not evade the
classical square-root prime-gap barrier.

This file records an exact finite counterexample and a conditional translation;
it does not claim a prime-gap theorem or a Legendre proof.
"""

from __future__ import annotations

from math import prod

from .legendre import primes_up_to


K73_COMMON_ROOT_RESIDUES = {
    3: 2,
    5: 4,
    7: 6,
    11: 10,
    13: 12,
    17: 16,
    19: 10,
    23: 7,
    29: 3,
    31: 1,
    37: 15,
    41: 24,
    43: 37,
    47: 31,
    53: 20,
    59: 54,
    61: 57,
    67: 45,
    71: 68,
}


def crt_common_root(residues: dict[int, int]) -> dict[str, int]:
    """Return the canonical and minimum-centered CRT representatives."""
    if not residues:
        raise ValueError("residues must be nonempty")
    moduli = tuple(sorted(int(p) for p in residues))
    modulus = prod(moduli)
    root = 0
    for p in moduli:
        a = int(residues[p]) % p
        if a == 0:
            raise ValueError("common-root witness requires nonzero local residues")
        cofactor = modulus // p
        root += a * cofactor * pow(cofactor, -1, p)
    root %= modulus
    centered = root if root <= modulus // 2 else root - modulus
    return {
        "modulus": modulus,
        "canonical_root": root,
        "centered_root": centered,
        "centered_root_height": abs(centered),
    }


def symmetric_cover_profile(k: int, residues: dict[int, int]) -> dict[str, object]:
    """Verify one common-root residue assignment covers every signed odd radius."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    expected_primes = tuple(p for p in primes_up_to(k - 1) if p % 2 == 1)
    if tuple(sorted(residues)) != expected_primes:
        raise ValueError("residue assignment must contain every odd prime below k exactly once")

    crt = crt_common_root(residues)
    rows: list[dict[str, object]] = []
    complete = True
    for radius in range(1, k, 2):
        lower_cover = tuple(
            p for p, a in residues.items()
            if (int(a) - radius) % int(p) == 0
        )
        upper_cover = tuple(
            p for p, a in residues.items()
            if (int(a) + radius) % int(p) == 0
        )
        if not lower_cover or not upper_cover:
            complete = False
        rows.append(
            {
                "radius": radius,
                "lower_cover_primes": lower_cover,
                "upper_cover_primes": upper_cover,
                "both_orientations_covered": bool(lower_cover and upper_cover),
            }
        )

    if complete:
        root = int(crt["canonical_root"])
        for p, a in residues.items():
            if root % p != a % p:
                raise AssertionError("CRT root does not realize stored local residue")
    return {
        "k": k,
        **crt,
        "physical_pronic_center": k * (k + 1),
        "root_height_to_physical_center_ratio": (
            int(crt["centered_root_height"]) / (k * (k + 1))
        ),
        "complete_signed_odd_cover": complete,
        "rows": tuple(rows),
    }


def k73_common_root_negative_witness() -> dict[str, object]:
    """Return and verify the explicit k=73 symmetric common-root cover."""
    data = symmetric_cover_profile(73, dict(K73_COMMON_ROOT_RESIDUES))
    if not bool(data["complete_signed_odd_cover"]):
        raise AssertionError("stored k=73 common-root witness does not cover all signed radii")
    if int(data["modulus"]) != 278970415063349480483707695:
        raise AssertionError("stored k=73 odd primorial changed")
    if int(data["canonical_root"]) != 186223063681305470464114469:
        raise AssertionError("stored k=73 CRT root changed")
    if int(data["centered_root_height"]) != 92747351382044010019593226:
        raise AssertionError("stored k=73 centered root height changed")
    if int(data["physical_pronic_center"]) != 5402:
        raise AssertionError("k=73 physical pronic center changed")
    return {
        **data,
        "negative_boundary": (
            "common +/-M CRT origin and disjoint mirror orientations are not sufficient without low-height/pronic coupling"
        ),
    }


def root_height_exponent_from_short_prime_exponent(theta: float) -> float:
    """Translate a universal short-prime exponent theta into the root-height exponent 1/theta."""
    if not (0.0 < float(theta) < 1.0):
        raise ValueError("theta must lie in (0,1)")
    return 1.0 / float(theta)
