"""Exact Wronskian slack accounting for the P025 Mason pressure test.

This module does not prove Mason--Stothers and does not claim novelty for the
Wronskian argument.  It isolates two exact integer degree slacks that occur in
the classical proof:

* residual absorption slack: ``deg(W) - residual_degree``;
* witness capacity slack: ``deg(P)+deg(Q)-1-deg(W(P,Q))``.

For non-proportional characteristic-zero polynomials the second slack is exactly
the number of normalized leading coefficient layers that agree at infinity
before the two polynomials first differ.  Integer coefficient tuples are used as
an exact executable specification; coefficients are stored low-degree first.
"""

from __future__ import annotations

from collections.abc import Sequence

Polynomial = tuple[int, ...]


def _trim(poly: Sequence[int]) -> Polynomial:
    if not poly:
        raise ValueError("polynomial coefficient sequence must be nonempty")
    values = list(poly)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("polynomial coefficients must be integers")
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _require_nonzero(poly: Sequence[int], name: str = "polynomial") -> Polynomial:
    result = _trim(poly)
    if result == (0,):
        raise ValueError(f"{name} must be nonzero")
    return result


def polynomial_degree(poly: Sequence[int]) -> int:
    """Return the degree of a nonzero integer polynomial."""
    return len(_require_nonzero(poly)) - 1


def polynomial_derivative(poly: Sequence[int]) -> Polynomial:
    """Return the formal derivative."""
    values = _trim(poly)
    if len(values) == 1:
        return (0,)
    return _trim(tuple(index * values[index] for index in range(1, len(values))))


def polynomial_add(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    """Return the exact polynomial sum."""
    a = _trim(left)
    b = _trim(right)
    size = max(len(a), len(b))
    return _trim(
        tuple(
            (a[index] if index < len(a) else 0)
            + (b[index] if index < len(b) else 0)
            for index in range(size)
        )
    )


def polynomial_subtract(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    """Return the exact polynomial difference."""
    a = _trim(left)
    b = _trim(right)
    size = max(len(a), len(b))
    return _trim(
        tuple(
            (a[index] if index < len(a) else 0)
            - (b[index] if index < len(b) else 0)
            for index in range(size)
        )
    )


def polynomial_scale(poly: Sequence[int], scalar: int) -> Polynomial:
    """Multiply a polynomial by an integer scalar."""
    if isinstance(scalar, bool) or not isinstance(scalar, int):
        raise ValueError("scalar must be an integer")
    values = _trim(poly)
    return _trim(tuple(scalar * value for value in values))


def polynomial_multiply(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    """Return the exact polynomial product."""
    a = _trim(left)
    b = _trim(right)
    if a == (0,) or b == (0,):
        return (0,)
    result = [0] * (len(a) + len(b) - 1)
    for i, left_value in enumerate(a):
        for j, right_value in enumerate(b):
            result[i + j] += left_value * right_value
    return _trim(result)


def wronskian(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    """Return ``P'Q - PQ'``."""
    p = _require_nonzero(left, "left polynomial")
    q = _require_nonzero(right, "right polynomial")
    return polynomial_subtract(
        polynomial_multiply(polynomial_derivative(p), q),
        polynomial_multiply(p, polynomial_derivative(q)),
    )


def wronskian_degree(left: Sequence[int], right: Sequence[int]) -> int:
    """Return the Wronskian degree, rejecting proportional/degenerate pairs."""
    w = wronskian(left, right)
    if w == (0,):
        raise ValueError("Wronskian is zero; pair is degenerate for this diagnostic")
    return len(w) - 1


def wronskian_capacity_slack(left: Sequence[int], right: Sequence[int]) -> int:
    """Return ``deg(P)+deg(Q)-1-deg(W(P,Q))`` exactly."""
    p = _require_nonzero(left, "left polynomial")
    q = _require_nonzero(right, "right polynomial")
    upper = polynomial_degree(p) + polynomial_degree(q) - 1
    witness_degree = wronskian_degree(p, q)
    slack = upper - witness_degree
    if slack < 0:
        raise AssertionError("Wronskian degree exceeded the classical capacity bound")
    return slack


def infinity_contact_depth(left: Sequence[int], right: Sequence[int]) -> int:
    """Return the normalized first-separation depth at infinity.

    If the degrees differ, the leading Wronskian coefficient is already nonzero,
    so the depth is zero.

    If both degrees equal ``d``, let ``a,b`` be their leading coefficients and
    form ``E=bP-aQ``.  For a non-proportional pair, ``deg(E)<d`` and the returned
    depth is ``d-deg(E)``.  Equivalently, after normalizing leading coefficients
    and writing in the coordinate ``t=1/x``, this is the first positive power of
    ``t`` at which the two normalized coefficient jets differ.
    """
    p = _require_nonzero(left, "left polynomial")
    q = _require_nonzero(right, "right polynomial")
    p_degree = polynomial_degree(p)
    q_degree = polynomial_degree(q)
    if p_degree != q_degree:
        if wronskian(p, q) == (0,):
            raise AssertionError("different-degree nonzero polynomials cannot be proportional")
        return 0

    cross_difference = polynomial_subtract(
        polynomial_scale(p, q[-1]),
        polynomial_scale(q, p[-1]),
    )
    if cross_difference == (0,):
        raise ValueError("polynomials are proportional; infinity contact is degenerate")
    return p_degree - polynomial_degree(cross_difference)


def wronskian_contact_profile(
    left: Sequence[int], right: Sequence[int]
) -> dict[str, object]:
    """Return and cross-check capacity slack versus infinity contact depth."""
    p = _require_nonzero(left, "left polynomial")
    q = _require_nonzero(right, "right polynomial")
    witness = wronskian(p, q)
    if witness == (0,):
        raise ValueError("Wronskian is zero; pair is degenerate for this diagnostic")
    capacity_slack = wronskian_capacity_slack(p, q)
    contact_depth = infinity_contact_depth(p, q)
    if capacity_slack != contact_depth:
        raise AssertionError("Wronskian capacity slack disagrees with infinity contact depth")
    return {
        "left_degree": polynomial_degree(p),
        "right_degree": polynomial_degree(q),
        "wronskian": witness,
        "wronskian_degree": polynomial_degree(witness),
        "capacity_slack": capacity_slack,
        "infinity_contact_depth": contact_depth,
    }


def mason_margin_profile(
    degrees: Sequence[int],
    radical_degree: int,
    witness_degree: int,
    target_index: int,
) -> dict[str, int]:
    """Split a Mason proof margin into absorption and capacity slacks.

    For degree triple ``h=(h0,h1,h2)``, total radical degree ``R``, a common
    Wronskian degree ``w``, and target index ``i``, put

    ``D=sum(h)-R``
    ``A=w-D``
    ``C=h_j+h_k-1-w``.

    Under the classical Mason proof inequalities ``D<=w<=h_j+h_k-1``,

    ``R-h_i-1 = A+C``.

    This function checks exactly those integer hypotheses.  The divisibility
    and Wronskian bounds themselves are classical Mason--Stothers inputs and are
    not proved by this executable accounting helper.
    """
    if len(degrees) != 3:
        raise ValueError("degrees must contain exactly three entries")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in degrees
    ):
        raise ValueError("degrees must be non-negative integers")
    for name, value in (
        ("radical_degree", radical_degree),
        ("witness_degree", witness_degree),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if target_index not in (0, 1, 2):
        raise ValueError("target_index must be 0, 1, or 2")

    h = tuple(int(value) for value in degrees)
    residual_degree = sum(h) - radical_degree
    if residual_degree < 0:
        raise ValueError("radical_degree cannot exceed the total degree")

    complement = tuple(index for index in range(3) if index != target_index)
    capacity_upper = h[complement[0]] + h[complement[1]] - 1
    if capacity_upper < 0:
        raise ValueError("complementary degrees do not give a nonnegative Wronskian bound")
    if witness_degree < residual_degree:
        raise ValueError("witness degree is below the residual divisibility requirement")
    if witness_degree > capacity_upper:
        raise ValueError("witness degree exceeds the complementary Wronskian capacity")

    absorption_slack = witness_degree - residual_degree
    capacity_slack = capacity_upper - witness_degree
    theorem_margin = radical_degree - h[target_index] - 1
    if theorem_margin != absorption_slack + capacity_slack:
        raise AssertionError("Mason margin decomposition failed")

    return {
        "target_index": target_index,
        "target_degree": h[target_index],
        "residual_degree": residual_degree,
        "witness_degree": witness_degree,
        "capacity_upper": capacity_upper,
        "absorption_slack": absorption_slack,
        "capacity_slack": capacity_slack,
        "theorem_margin": theorem_margin,
    }


def mason_polynomial_slack_profile(
    polynomials: Sequence[Sequence[int]],
    radical_degree: int,
    target_index: int,
) -> dict[str, object]:
    """Compute the slack profile for an exact polynomial relation ``P0+P1+P2=0``.

    Pairwise coprimality and the supplied radical degree remain caller proof
    obligations.  The helper verifies the additive relation, common-complement
    Wronskian degree, the Mason integer bounds encoded by ``radical_degree``, and
    the equality between capacity slack and infinity contact depth.
    """
    if len(polynomials) != 3:
        raise ValueError("polynomials must contain exactly three entries")
    polys = tuple(_require_nonzero(poly, f"polynomial {index}") for index, poly in enumerate(polynomials))
    relation_sum = polynomial_add(polynomial_add(polys[0], polys[1]), polys[2])
    if relation_sum != (0,):
        raise ValueError("polynomials must satisfy P0+P1+P2=0")
    if target_index not in (0, 1, 2):
        raise ValueError("target_index must be 0, 1, or 2")

    complement = tuple(index for index in range(3) if index != target_index)
    pair_profile = wronskian_contact_profile(
        polys[complement[0]], polys[complement[1]]
    )
    degrees = tuple(polynomial_degree(poly) for poly in polys)
    margin = mason_margin_profile(
        degrees,
        radical_degree,
        int(pair_profile["wronskian_degree"]),
        target_index,
    )
    if margin["capacity_slack"] != pair_profile["infinity_contact_depth"]:
        raise AssertionError("Mason capacity slack is not the computed infinity contact depth")
    return {
        "degrees": degrees,
        "radical_degree": radical_degree,
        **margin,
        "infinity_contact_depth": int(pair_profile["infinity_contact_depth"]),
        "wronskian": pair_profile["wronskian"],
    }
