"""Exact centered boundary carries for P017 signed divisor incidences.

Fix k>=2, M=k(k+1), K=k-1 and a positive odd divisor D transverse to M.
There are two layers.

Raw parity/divisibility layer
-----------------------------
Signed points satisfying

    -K<=x<=K,  x odd,  D|M-x

form one residue class modulo 2D.  Write K=qD+s, 0<=s<D, and let y be the
unique centered odd representative of M modulo D with -D<y<D.  Then

    F_raw(D)=q+eta_D,

where eta_D is binary:

    eta_D=1 iff |y|<=s       when q is even,
    eta_D=1 iff |y|>=D-s     when q is odd.

Thus the raw CG12 capacity differs from q+1 by at most one symbol.

Anchor-surviving layer
----------------------
P017 moments use only radii with gcd(x,M)=1.  Let A_eff be the product of the
distinct effective odd anchor primes p|M with p<k.  Möbius inclusion-exclusion
gives the exact filtered fiber

    F_surv(D)
      = sum_{a|A_eff} mu(a) N(a,D),

where N(a,D) counts odd signed points with a|x and D|M-x.  Since gcd(a,D)=1,
those conditions again define one residue class modulo 2aD, so every N(a,D)
has its own binary centered carry.  Hence the general finite correction is a
**Möbius-signed carry spectrum**, not one bit.

When there is no effective odd anchor, A_eff=1 and the spectrum collapses to the
single raw carry bit.  This is why the simpler formula is exact on the critical
power-of-two/prime families but not on a general scale.

For every j the transverse support moment has the exact finite expansion

    S_j(k)=sum_{D squarefree, omega(D)=j, p|D=>p<=k,p∤M} F_surv(D).

This is classical inclusion-exclusion plus exact centered CRT counting; the
project-specific value is the finite carry coordinate and its separation of
bulk density from anchor/boundary corrections.
"""

from __future__ import annotations

from itertools import combinations
from math import gcd, prod

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_p018_effective_anchor import effective_odd_anchor_primes
from .p017_p018_token_remainder_repair import raw_signed_token_fiber


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def _centered_class_count(limit: int, base_modulus: int, odd_residue_mod_2base: int) -> dict[str, int | bool]:
    """Count one odd residue class modulo 2*base_modulus in [-limit,limit]."""
    if base_modulus <= 0 or base_modulus % 2 == 0:
        raise ValueError("base_modulus must be positive odd")
    period = 2 * base_modulus
    residue = odd_residue_mod_2base % period
    if residue % 2 == 0:
        raise ValueError("residue must be odd modulo the even period")

    centered = residue if residue < base_modulus else residue - period
    if not (-base_modulus < centered < base_modulus):
        raise AssertionError("odd residue failed centered normalization")

    coarse, remainder = divmod(limit, base_modulus)
    if coarse % 2 == 0:
        carry = int(abs(centered) <= remainder)
        branch = "EVEN_COARSE"
    else:
        carry = int(abs(centered) >= base_modulus - remainder)
        branch = "ODD_COARSE"
    exact = coarse + carry

    first_index = _ceil_div(-limit - residue, period)
    last_index = (limit - residue) // period
    direct = max(0, last_index - first_index + 1)
    if exact != direct:
        raise AssertionError("centered binary carry did not equal direct residue-class count")

    return {
        "base_modulus": base_modulus,
        "period": period,
        "odd_residue": residue,
        "centered_odd_residue": centered,
        "coarse_quotient": coarse,
        "boundary_remainder": remainder,
        "coarse_parity_even": coarse % 2 == 0,
        "branch": branch,
        "boundary_carry": carry,
        "exact_count": exact,
    }


def raw_signed_divisor_boundary_carry(k: int, divisor: int) -> dict[str, int | bool]:
    """Return the raw one-bit carry before anchor survival is imposed."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if (
        isinstance(divisor, bool)
        or not isinstance(divisor, int)
        or divisor <= 0
        or divisor % 2 == 0
    ):
        raise ValueError("divisor must be a positive odd integer")
    center = k * (k + 1)
    if gcd(divisor, center) != 1:
        raise ValueError("divisor must be transverse to M=k(k+1)")

    residue = center % divisor
    if residue % 2 == 0:
        residue += divisor
    data = _centered_class_count(k - 1, divisor, residue)
    universal = (k - 1) // divisor + 1
    savings = universal - int(data["exact_count"])
    if savings not in (0, 1):
        raise AssertionError("raw CG12 boundary correction is not binary")
    return {
        "k": k,
        "center": center,
        "divisor": divisor,
        **data,
        "raw_signed_fiber_size": int(data["exact_count"]),
        "cg12_universal_capacity": universal,
        "raw_boundary_savings": savings,
    }


def _anchor_divisor_crt_term(k: int, divisor: int, anchor_divisor: int, mu: int) -> dict[str, int]:
    """Count odd x with anchor_divisor|x and divisor|M-x by one CRT class."""
    center = k * (k + 1)
    if anchor_divisor <= 0 or anchor_divisor % 2 == 0 or center % anchor_divisor:
        raise ValueError("anchor_divisor must be a positive odd divisor of M")
    if gcd(anchor_divisor, divisor) != 1:
        raise AssertionError("anchor and transverse divisor are not coprime")

    # Put x=a*t.  Then t = M*a^{-1} (mod D).
    t_residue = (center * pow(anchor_divisor, -1, divisor)) % divisor
    combined = anchor_divisor * divisor
    residue = anchor_divisor * t_residue
    if residue % 2 == 0:
        residue += combined
    data = _centered_class_count(k - 1, combined, residue)
    return {
        "anchor_divisor": anchor_divisor,
        "mu": mu,
        "combined_base_modulus": combined,
        "odd_residue": int(data["odd_residue"]),
        "coarse_quotient": int(data["coarse_quotient"]),
        "boundary_carry": int(data["boundary_carry"]),
        "exact_count": int(data["exact_count"]),
    }


def anchor_surviving_divisor_boundary_carry(k: int, divisor: int) -> dict[str, object]:
    """Return the exact anchor-filtered D fiber as a Möbius-signed carry spectrum."""
    raw = raw_signed_divisor_boundary_carry(k, divisor)
    anchors = effective_odd_anchor_primes(k)
    terms = squarefree_divisors_with_mu(list(anchors))

    rows: list[dict[str, int]] = []
    bulk = 0
    carries = 0
    exact = 0
    for anchor_divisor, mu in terms:
        row = _anchor_divisor_crt_term(k, divisor, anchor_divisor, mu)
        rows.append(row)
        bulk += mu * int(row["coarse_quotient"])
        carries += mu * int(row["boundary_carry"])
        exact += mu * int(row["exact_count"])

    raw_points = tuple(int(x) for x in raw_signed_token_fiber(k, divisor)["raw_signed_points"])
    direct = sum(1 for point in raw_points if gcd(point, int(raw["center"])) == 1)
    if exact != bulk + carries:
        raise AssertionError("anchor Möbius bulk/carry decomposition failed")
    if exact != direct:
        raise AssertionError("anchor Möbius carry spectrum missed direct surviving incidences")
    if not anchors:
        if len(rows) != 1 or exact != int(raw["raw_signed_fiber_size"]):
            raise AssertionError("zero-effective-anchor scale failed to reduce to one raw carry")

    return {
        **raw,
        "effective_odd_anchor_primes": anchors,
        "mobius_rows": tuple(rows),
        "anchor_mobius_bulk_mass": bulk,
        "anchor_mobius_boundary_carry_mass": carries,
        "anchor_surviving_fiber_size": exact,
        "anchor_filter_savings": int(raw["raw_signed_fiber_size"]) - exact,
        "critical_single_carry_regime": not anchors,
    }


def transverse_support_moment_from_boundary_carries(k: int, order: int) -> dict[str, object]:
    """Reconstruct S_order exactly from anchor-Möbius divisor carry spectra.

    This enumerator is for bounded regression; the finite identity itself is
    exact for every k.
    """
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    center = k * (k + 1)
    transverse = tuple(
        p for p in primes_up_to(k) if p % 2 == 1 and center % p != 0
    )

    bulk = 0
    carries = 0
    exact = 0
    term_count = 0
    rows: list[dict[str, object]] = []
    for subset in combinations(transverse, order):
        divisor = prod(subset)
        data = anchor_surviving_divisor_boundary_carry(k, divisor)
        bulk += int(data["anchor_mobius_bulk_mass"])
        carries += int(data["anchor_mobius_boundary_carry_mass"])
        exact += int(data["anchor_surviving_fiber_size"])
        term_count += 1
        rows.append(
            {
                "primes": subset,
                "divisor": divisor,
                "mobius_bulk": int(data["anchor_mobius_bulk_mass"]),
                "mobius_boundary_carry": int(data["anchor_mobius_boundary_carry_mass"]),
                "exact_surviving_fiber": int(data["anchor_surviving_fiber_size"]),
            }
        )

    if exact != bulk + carries:
        raise AssertionError("global support moment failed bulk + Möbius carry reconstruction")
    return {
        "k": k,
        "order": order,
        "transverse_prime_count": len(transverse),
        "squarefree_divisor_term_count": term_count,
        "anchor_mobius_bulk_mass": bulk,
        "anchor_mobius_boundary_carry_mass": carries,
        "exact_support_moment": exact,
        "rows": tuple(rows),
    }
