"""Exact quotient-remainder repair for reused signed divisor tokens.

Fix P017 center M=k(k+1), signed window

    -(k-1) <= x <= k-1,

and a positive odd transverse divisor D with D | M-x.  Parity plus divisibility
put every such signed incidence in one residue class modulo 2D.  Hence the fiber
is a finite arithmetic progression

    x_t = x_0 + 2D t.

Define the squarefree quotient coordinate

    u_t = (M-x_t)/D.

Then

    u_{t+1}=u_t-2.

If the actual D-fiber has F>0 points, the remainder

    rho_t = u_t mod (2F)

is injective on that fiber: two different indices differ by s with
0<|s|<F, so their quotients differ by 2s, which cannot vanish modulo 2F.
Because M is even while x and D are odd, every u_t is odd.  Thus only F residue
symbols are realized modulo 2F, exactly matching the fiber cardinality.

Consequently `(D, u mod 2F)` is an explicit reversible repair of the coarse token
label D.  Its alphabet has exactly F symbols, which is also information-theoretically
minimal for exact incidence identity because the D-fiber itself has F states.
For F=1 the repair is constant and disappears.

CG12 supplies the universal upper bound

    C_D = floor((k-1)/D)+1.

The finite boundary is in fact exact up to one symbol.  The signed interval has
span 2(k-1), while one token period is 2D.  Therefore any residue class modulo
2D occurs either floor((k-1)/D) or one more time:

    F_D in {C_D-1, C_D}.

Thus CG12's universal capacity overestimates the exact finite repair alphabet by
**at most one symbol**.  At k=524287,D=255255 the universal value is 3 while the
actual fiber is 2.

This module computes the exact fiber and repair by integer arithmetic only.  It
is a P017/P007-style specialization; no new generic quotient/remainder theorem
is claimed.
"""

from __future__ import annotations

from math import gcd


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def signed_token_fiber(k: int, divisor: int) -> dict[str, object]:
    """Return the exact signed incidence fiber of one odd transverse divisor."""
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
    boundary_savings = universal_capacity - len(points)
    if len(points) > universal_capacity:
        raise AssertionError("exact signed token fiber exceeded the CG12 universal capacity")
    if boundary_savings not in (0, 1):
        raise AssertionError("finite signed token boundary changed capacity by more than one symbol")
    for point in points:
        if point % 2 == 0 or not -(k - 1) <= point <= k - 1:
            raise AssertionError("signed token point left the parity/window domain")
        if (center - point) % divisor:
            raise AssertionError("signed token point lost D | M-x")

    return {
        "k": k,
        "center": center,
        "divisor": divisor,
        "odd_residue_mod_2D": residue,
        "modulus": modulus,
        "signed_points": points,
        "actual_fiber_size": len(points),
        "universal_capacity": universal_capacity,
        "boundary_savings": boundary_savings,
        "exact_capacity_is_universal_or_one_less": True,
    }


def quotient_remainder_token_repair(k: int, divisor: int) -> dict[str, object]:
    """Return the exact minimal-cardinality remainder repair of one nonempty D-fiber."""
    fiber = signed_token_fiber(k, divisor)
    points = tuple(int(x) for x in fiber["signed_points"])
    size = len(points)
    if size == 0:
        raise ValueError("token has no signed incidence in the finite window")

    center = int(fiber["center"])
    repair_modulus = 2 * size
    rows: list[dict[str, int]] = []
    residues: list[int] = []
    quotients: list[int] = []

    for index, point in enumerate(points):
        quotient = (center - point) // divisor
        if quotient <= 0 or quotient % 2 == 0:
            raise AssertionError("signed odd token quotient is not positive odd")
        repair = quotient % repair_modulus
        rows.append(
            {
                "fiber_index": index,
                "signed_point": point,
                "state": center - point,
                "squarefree_quotient": quotient,
                "repair_remainder": repair,
            }
        )
        quotients.append(quotient)
        residues.append(repair)

    for left, right in zip(quotients, quotients[1:]):
        if left - right != 2:
            raise AssertionError("adjacent token quotients are not separated by exactly two")
    if len(set(residues)) != size:
        raise AssertionError("u mod 2F failed to separate the exact token fiber")
    if any(residue % 2 == 0 for residue in residues):
        raise AssertionError("token repair used an impossible even residue symbol")

    return {
        **fiber,
        "repair_modulus": repair_modulus,
        "repair_symbol_count": size,
        "minimal_repair_symbol_count_for_exact_incidence": size,
        "repair_is_trivial": size == 1,
        "rows": tuple(rows),
        "repair_residues": tuple(residues),
        "injective_remainder_repair": True,
    }
