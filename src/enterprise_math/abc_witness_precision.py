"""Finite relation-conditioned witness precision for the P025 abc pressure test.

Pasten's arithmetic-derivative construction associates to a chosen primitive
relation ``a+b=c`` an integer lattice of derivation coordinates on the prime
support of ``abc``.  This module does not claim that construction as new.  It
extracts an exact finite-state view useful for Enterprise Math:

* the additive condition is one integer linear form ``alpha``;
* Wronskian degeneracy is a second integer linear form ``beta``;
* admissible non-degenerate witnesses form a normed lattice flag;
* the first L-infinity radius containing a non-degenerate witness is a finite
  task-relative witness horizon.

The functions are intended as exact reference tools for small support sets and
architecture tests, not as an efficient lattice-reduction implementation.
"""

from __future__ import annotations

from itertools import product
from math import gcd

from .abc_support import abc_support_state, prime_factorization


def _primitive_vector(entries: tuple[int, ...]) -> tuple[int, ...]:
    """Normalize a nonzero integer vector by content and global sign."""
    if not entries or all(entry == 0 for entry in entries):
        raise ValueError("vector must be nonempty and nonzero")
    content = 0
    for entry in entries:
        content = gcd(content, abs(entry))
    normalized = tuple(entry // content for entry in entries)
    first_nonzero = next(entry for entry in normalized if entry != 0)
    if first_nonzero < 0:
        normalized = tuple(-entry for entry in normalized)
    return normalized


def _valuation(n: int, prime: int) -> int:
    for p, exponent in prime_factorization(n):
        if p == prime:
            return exponent
    return 0


def witness_coordinates(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the sorted prime coordinates supporting a primitive abc state."""
    data = abc_support_state(a, b, c)
    return tuple(sorted(set().union(*(set(s) for s in data["supports"]))))


def additive_relation_vector(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the primitive integer normal for Pasten's additive condition.

    In coordinate ``x_p = psi(xi_p)``, additivity for the chosen equation is

        d^psi(a) + d^psi(b) - d^psi(c) = 0.

    Since ``n * v_p(n) / p`` is integral when ``p|n``, this gives one exact
    integer linear form.  Primitive normalization removes irrelevant global
    scaling of the same kernel lattice.
    """
    coordinates = witness_coordinates(a, b, c)
    raw: list[int] = []
    for prime in coordinates:
        coefficient = 0
        va = _valuation(a, prime)
        vb = _valuation(b, prime)
        vc = _valuation(c, prime)
        if va:
            coefficient += a * va // prime
        if vb:
            coefficient += b * vb // prime
        if vc:
            coefficient -= c * vc // prime
        raw.append(coefficient)
    return _primitive_vector(tuple(raw))


def wronskian_relation_vector(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return a primitive integer normal for W^psi(a,b)=0.

    ``W^psi(a,b)=a*d^psi(b)-b*d^psi(a)`` is an integer linear form in the
    same prime-coordinate vector.  A witness is non-degenerate exactly when
    this form is nonzero.
    """
    coordinates = witness_coordinates(a, b, c)
    raw: list[int] = []
    for prime in coordinates:
        va = _valuation(a, prime)
        vb = _valuation(b, prime)
        coefficient = 0
        if vb:
            coefficient += a * b * vb // prime
        if va:
            coefficient -= a * b * va // prime
        raw.append(coefficient)
    return _primitive_vector(tuple(raw))


def _dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimension")
    return sum(a * b for a, b in zip(left, right, strict=True))


def witness_flag(a: int, b: int, c: int) -> dict[str, object]:
    """Return the finite lattice-flag signature for the chosen abc relation."""
    coordinates = witness_coordinates(a, b, c)
    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    return {
        "coordinates": coordinates,
        "additive_normal": alpha,
        "degeneracy_normal": beta,
        "rank_ambient": len(coordinates),
        "rank_additive_kernel": len(coordinates) - 1,
    }


def is_additive_witness(a: int, b: int, c: int, vector: tuple[int, ...]) -> bool:
    """Check membership in the exact additive witness lattice."""
    alpha = additive_relation_vector(a, b, c)
    return _dot(alpha, vector) == 0


def is_nondegenerate_witness(
    a: int, b: int, c: int, vector: tuple[int, ...]
) -> bool:
    """Check additive membership and nonzero arithmetic Wronskian."""
    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    return _dot(alpha, vector) == 0 and _dot(beta, vector) != 0


def bounded_nondegenerate_witnesses(
    a: int, b: int, c: int, bound: int, *, state_cap: int = 2_000_000
) -> tuple[tuple[int, ...], ...]:
    """Enumerate all non-degenerate witnesses in the L-infinity ball.

    This exact brute-force routine is deliberately limited to small support
    dimensions.  It exists to calibrate the precision semantics, not to replace
    Geometry-of-Numbers or lattice-reduction algorithms.
    """
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a non-negative integer")
    if isinstance(state_cap, bool) or not isinstance(state_cap, int) or state_cap <= 0:
        raise ValueError("state_cap must be a positive integer")
    dimension = len(witness_coordinates(a, b, c))
    state_count = (2 * bound + 1) ** dimension
    if state_count > state_cap:
        raise ValueError("witness ball exceeds exact enumeration state_cap")
    values = range(-bound, bound + 1)
    return tuple(
        vector
        for vector in product(values, repeat=dimension)
        if is_nondegenerate_witness(a, b, c, vector)
    )


def minimal_witness_cost(
    a: int, b: int, c: int, *, max_bound: int = 32, state_cap: int = 2_000_000
) -> int:
    """Return the first exact L-infinity radius containing a witness.

    Raises ``ValueError`` if no witness is found within the supplied finite
    search horizon.  This is an exact bounded reference oracle, not an
    asymptotic claim.
    """
    if isinstance(max_bound, bool) or not isinstance(max_bound, int) or max_bound < 1:
        raise ValueError("max_bound must be a positive integer")
    for bound in range(1, max_bound + 1):
        if bounded_nondegenerate_witnesses(
            a, b, c, bound, state_cap=state_cap
        ):
            return bound
    raise ValueError("no non-degenerate witness found within max_bound")


def same_radical_state_witness_precision_counterexample() -> dict[str, object]:
    """Show witness precision does not descend through the radical triple state.

    ``1+2=3`` and ``1+8=9`` have the same full radical triple ``(1,2,3)``.
    Their primitive additive normals are respectively ``(1,-1)`` and
    ``(2,-1)`` on coordinates ``(2,3)``, so the minimum non-degenerate
    L-infinity witness costs are 1 and 2.
    """
    first = (1, 2, 3)
    second = (1, 8, 9)
    radical_first = tuple(int(x) for x in abc_support_state(*first)["radicals"])
    radical_second = tuple(int(x) for x in abc_support_state(*second)["radicals"])
    if radical_first != radical_second:
        raise AssertionError("counterexample lost equal radical coarse state")
    first_flag = witness_flag(*first)
    second_flag = witness_flag(*second)
    first_cost = minimal_witness_cost(*first)
    second_cost = minimal_witness_cost(*second)
    if first_cost == second_cost:
        raise AssertionError("counterexample lost distinct witness precision")
    return {
        "triples": (first, second),
        "radical_state": radical_first,
        "additive_normals": (
            first_flag["additive_normal"],
            second_flag["additive_normal"],
        ),
        "minimum_witness_costs": (first_cost, second_cost),
    }


def primitive_kernel_signature_complete(
    left: tuple[int, ...], right: tuple[int, ...]
) -> bool:
    """Executable finite statement for the primitive normal signature.

    For nonzero integer row vectors, equality after primitive sign-normalization
    is exactly the canonical representation of the same rational hyperplane.
    In the P025 witness setting this is the complete normal signature used to
    identify the additive kernel lattice.  The mathematical completeness claim
    is elementary rank-one lattice theory and is documented separately.
    """
    return _primitive_vector(left) == _primitive_vector(right)
