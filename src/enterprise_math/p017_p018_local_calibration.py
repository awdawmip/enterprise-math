"""Exact local calibration between radius residues and singular core Euler mass.

Let M=k(k+1) and let p be an odd transverse prime, p∤M.  For a residual
hard-core radius with ordered full cores a,b and S=ab, the large tails exceed k,
so p<=k cannot hide in a tail.  Therefore

    p | S
      iff p divides one of M-r, M+r
      iff r = +M or -M (mod p).

The two special radius classes are distinct because p is odd and p∤M.  Thus the
local radius partition has exact proportions

    p|S      : 2/p,
    p∤S      : (p-2)/p.

Now inspect the singular-weighted leading core Euler mass before zeta-square
extraction.  At p:

* if p∤S, the generic two-linear-form factor contributes

      c_p = p(p-2)/(p-1)^2;

* if p|S, summing all positive prime-power exponents and the two possible side
  assignments contributes

      sum_{a>=1} 2/phi(p^a) = 2p/(p-1)^2.

The total local mass is p^2/(p-1)^2.  Normalizing the two branches therefore
gives exactly

    [2p/(p-1)^2] / [p^2/(p-1)^2] = 2/p,

and

    [p(p-2)/(p-1)^2] / [p^2/(p-1)^2] = (p-2)/p.

Hence the singular core Euler model is **locally calibrated exactly** to the
finite radius residue demand at every transverse odd prime.  The near saturation
seen at p=3 on anchor-critical scales is the first instance of a universal
identity, not an accident.

Consequence / negative boundary:
Any argument that only multiplies independent one-prime local densities cannot
create a new leading deficit between residual radius demand and singular core
mass.  New leverage must use cross-prime correlation, finite-boundary effects,
higher collision moments (for example CG11/Vandermonde coupling), or genuinely
nonlocal analytic input.

This is an exact arithmetic identity, not a sieve asymptotic and not a Legendre
proof.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def reduced_pair(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def transverse_radius_residue_split(prime: int) -> dict[str, object]:
    """Return the exact two-special / p-2-ordinary residue proportions."""
    _require_odd_prime(prime)
    p = prime
    return {
        "prime": p,
        "core_present_residue_count": 2,
        "core_absent_residue_count": p - 2,
        "core_present_density": reduced_pair(2, p),
        "core_absent_density": reduced_pair(p - 2, p),
    }


def singular_core_local_split(prime: int) -> dict[str, object]:
    """Return the normalized local Euler mass split by whether p divides S."""
    _require_odd_prime(prime)
    p = prime

    core_absent_mass = reduced_pair(p * (p - 2), (p - 1) ** 2)
    core_present_mass = reduced_pair(2 * p, (p - 1) ** 2)
    total_mass = reduced_pair(p * p, (p - 1) ** 2)

    present_share = reduced_pair(
        core_present_mass[0] * total_mass[1],
        core_present_mass[1] * total_mass[0],
    )
    absent_share = reduced_pair(
        core_absent_mass[0] * total_mass[1],
        core_absent_mass[1] * total_mass[0],
    )

    if present_share != reduced_pair(2, p):
        raise AssertionError("core-present Euler share is not 2/p")
    if absent_share != reduced_pair(p - 2, p):
        raise AssertionError("core-absent Euler share is not (p-2)/p")

    return {
        "prime": p,
        "core_absent_mass": core_absent_mass,
        "core_present_mass": core_present_mass,
        "total_mass": total_mass,
        "core_present_share": present_share,
        "core_absent_share": absent_share,
    }


def local_radius_euler_calibration(prime: int) -> dict[str, object]:
    """Certify exact equality of radius-residue and Euler-mass branch shares."""
    radius = transverse_radius_residue_split(prime)
    euler = singular_core_local_split(prime)
    if radius["core_present_density"] != euler["core_present_share"]:
        raise AssertionError("core-present local calibration failed")
    if radius["core_absent_density"] != euler["core_absent_share"]:
        raise AssertionError("core-absent local calibration failed")
    return {
        "prime": prime,
        "core_present_share": radius["core_present_density"],
        "core_absent_share": radius["core_absent_density"],
        "radius_residue_split": radius,
        "singular_euler_split": euler,
        "calibrated": True,
    }
