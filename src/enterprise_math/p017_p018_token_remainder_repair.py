"""Exact quotient-remainder repair for reused signed divisor tokens.

Fix P017 center M=k(k+1), signed window

    -(k-1) <= x <= k-1,

and a positive odd transverse divisor D with D | M-x.

Two finite fibers must be distinguished.

**Raw parity/divisibility fiber.**  Parity plus D|M-x give one residue class
modulo 2D.  Its size F_raw differs from the CG12 universal capacity

    C_D=floor((k-1)/D)+1

by at most one symbol:

    F_raw in {C_D-1,C_D}.

**Anchor-surviving fiber.**  P017 signed states additionally require
`gcd(x,M)=1`.  Odd anchor primes can delete internal points of the raw arithmetic
progression, so the actual size F_surv may be smaller by more than one.  On the
zero-effective-anchor critical families the two fibers coincide exactly.

For the raw progression, define

    u=(M-x)/D.

Adjacent raw points differ by 2D, hence adjacent u-values differ by two.  If the
raw fiber has R points, `u mod 2R` is injective on the whole raw fiber and
therefore also on its anchor-surviving subset.  The surviving subset realizes
exactly F_surv distinct remainder symbols.  Exact incidence identity thus needs
an alphabet of F_surv symbols; the arithmetic remainder modulus 2R is a natural
P007-style realization of that minimal alphabet.  When no effective odd anchor
exists, R=F_surv and the modulus tightens to 2F_surv.

This distinction corrects the tempting but false general identification of the
raw one-bit boundary correction with the fully anchor-filtered token fiber.
"""

from __future__ import annotations

from math import gcd

from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def raw_signed_token_fiber(k: int, divisor: int) -> dict[str, object]:
    """Return the exact parity/divisibility fiber before anchor filtering."""
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
    modulus = 2 * divisor
    limit = k - 1
    first_index = _ceil_div(-limit - residue, modulus)
    last_index = (limit - residue) // modulus

    if first_index > last_index:
        points: tuple[int, ...] = ()
    else:
        points = tuple(
            residue + modulus * index
            for index in range(first_index, last_index + 1)
        )

    universal_capacity = (k - 1) // divisor + 1
    raw_boundary_savings = universal_capacity - len(points)
    if len(points) > universal_capacity:
        raise AssertionError("raw signed token fiber exceeded the CG12 universal capacity")
    if raw_boundary_savings not in (0, 1):
        raise AssertionError("raw finite boundary changed capacity by more than one symbol")
    for point in points:
        if point % 2 == 0 or not -(k - 1) <= point <= k - 1:
            raise AssertionError("raw token point left the parity/window domain")
        if (center - point) % divisor:
            raise AssertionError("raw token point lost D | M-x")

    return {
        "k": k,
        "center": center,
        "divisor": divisor,
        "odd_residue_mod_2D": residue,
        "modulus": modulus,
        "raw_signed_points": points,
        "raw_fiber_size": len(points),
        "universal_capacity": universal_capacity,
        "raw_boundary_savings": raw_boundary_savings,
        "raw_capacity_is_universal_or_one_less": True,
    }


def signed_token_fiber(k: int, divisor: int) -> dict[str, object]:
    """Return the exact anchor-surviving signed incidence fiber."""
    raw = raw_signed_token_fiber(k, divisor)
    center = int(raw["center"])
    raw_points = tuple(int(x) for x in raw["raw_signed_points"])
    surviving = tuple(x for x in raw_points if gcd(x, center) == 1)
    anchor_savings = len(raw_points) - len(surviving)
    if anchor_savings < 0:
        raise AssertionError("anchor filtering increased the token fiber")

    anchors = effective_odd_anchor_primes(k)
    if not anchors and surviving != raw_points:
        raise AssertionError("zero-effective-anchor scale changed under anchor filtering")

    return {
        **raw,
        "effective_odd_anchor_primes": anchors,
        "signed_points": surviving,
        "actual_fiber_size": len(surviving),
        "anchor_filter_savings": anchor_savings,
        # Compatibility alias: total savings from the universal CG12 ceiling.
        "boundary_savings": int(raw["universal_capacity"]) - len(surviving),
        "raw_and_surviving_fibers_coincide": surviving == raw_points,
    }


def quotient_remainder_token_repair(k: int, divisor: int) -> dict[str, object]:
    """Return an exact remainder repair of one nonempty anchor-surviving D-fiber."""
    fiber = signed_token_fiber(k, divisor)
    points = tuple(int(x) for x in fiber["signed_points"])
    raw_points = tuple(int(x) for x in fiber["raw_signed_points"])
    size = len(points)
    raw_size = len(raw_points)
    if size == 0:
        raise ValueError("token has no anchor-surviving signed incidence in the finite window")
    if raw_size == 0:
        raise AssertionError("surviving token fiber exists without a raw fiber")

    center = int(fiber["center"])
    repair_modulus = 2 * raw_size
    raw_quotients = tuple((center - point) // divisor for point in raw_points)
    for left, right in zip(raw_quotients, raw_quotients[1:]):
        if left - right != 2:
            raise AssertionError("adjacent raw token quotients are not separated by exactly two")

    rows: list[dict[str, int]] = []
    residues: list[int] = []
    for point in points:
        quotient = (center - point) // divisor
        if quotient <= 0 or quotient % 2 == 0:
            raise AssertionError("signed odd token quotient is not positive odd")
        repair = quotient % repair_modulus
        raw_index = raw_points.index(point)
        rows.append(
            {
                "raw_fiber_index": raw_index,
                "signed_point": point,
                "state": center - point,
                "squarefree_quotient": quotient,
                "repair_remainder": repair,
            }
        )
        residues.append(repair)

    if len(set(residues)) != size:
        raise AssertionError("u mod 2F_raw failed to separate the anchor-surviving token fiber")
    if any(residue % 2 == 0 for residue in residues):
        raise AssertionError("token repair used an impossible even residue symbol")

    return {
        **fiber,
        "repair_modulus": repair_modulus,
        "repair_modulus_uses_raw_fiber_size": raw_size,
        "repair_symbol_count": size,
        "minimal_repair_symbol_count_for_exact_incidence": size,
        "repair_is_trivial": size == 1,
        "rows": tuple(rows),
        "repair_residues": tuple(residues),
        "injective_remainder_repair": True,
        "critical_tight_modulus": size == raw_size,
    }
