"""Closed-form minimum integer impulse on one uniform 1D contact chain.

This is an E001 specialization of the delivered-contact network from
``material_contact_network_impulse_1d``.  It does not claim a new general
obstacle/graph-Laplacian theorem.

Assume ``n>=1`` consecutive contacts join ``n+1`` equal-mass bodies, every
contact normal points from body ``i`` to ``i+1``, and every initial contact score
is the same closing value ``-q`` with ``q>0``.  The coupling matrix is the path
Gram

    K = tridiag(-1, 2, -1).

We seek non-negative integer delivered impulses ``j`` such that

    -q*1 + K j >= 0.

Put boundary values ``j_0=j_{n+1}=0`` and first differences
``d_i=j_i-j_{i-1}``.  Then feasibility is exactly

    d_i - d_{i+1} >= q.

Writing ``e_i=d_i+q(i-1)`` turns this into a non-increasing integer sequence
with fixed total.  The most balanced such sequence is majorized by every other
one, hence every feasible impulse vector dominates the closed form below
coordinatewise.  Therefore the returned vector is the unique componentwise
least feasible integer impulse vector and, in particular, the unique minimum of
total delivered impulse.

If ``q*n`` is even, all contacts can finish exactly comoving and

    j_i = q*i*(n+1-i)/2.

If ``q*n`` is odd (necessarily both ``q`` and ``n`` odd), integer momentum cannot
be shared equally among the even number ``n+1`` of equal-mass bodies.  Let
``a_i=min(i,n+1-i)``.  Then

    j_i = a_i * (q*(n+1-a_i)+1) / 2,

and the final score is zero on every contact except the central one, whose score
is exactly ``+1``.  This single surplus is an integrality/consensus obstruction,
not an energy or constitutive claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_incidence_matrix,
    contact_relative_scores,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def uniform_chain_minimum_impulse_vector(
    contact_count: int,
    closing_score_magnitude: int,
) -> tuple[int, ...]:
    """Return the unique componentwise-least feasible impulse vector."""
    _require_positive("contact_count", contact_count)
    _require_positive("closing_score_magnitude", closing_score_magnitude)
    n = contact_count
    q = closing_score_magnitude
    body_count = n + 1

    if (q * n) % 2 == 0:
        result = tuple(
            q * index * (body_count - index) // 2
            for index in range(1, n + 1)
        )
    else:
        result = tuple(
            (lambda a: a * (q * (body_count - a) + 1) // 2)(
                min(index, body_count - index)
            )
            for index in range(1, n + 1)
        )

    if any(value < 0 for value in result):
        raise AssertionError("uniform-chain closed form produced a negative impulse")
    return result


def uniform_chain_score_increment(
    contact_count: int,
    closing_score_magnitude: int,
) -> tuple[int, ...]:
    """Return ``K j*`` for the closed-form path solution."""
    impulses = uniform_chain_minimum_impulse_vector(
        contact_count, closing_score_magnitude
    )
    return tuple(
        2 * impulses[index]
        - (impulses[index - 1] if index else 0)
        - (impulses[index + 1] if index + 1 < len(impulses) else 0)
        for index in range(len(impulses))
    )


def uniform_chain_minimum_total_impulse(
    contact_count: int,
    closing_score_magnitude: int,
) -> int:
    """Return the exact minimum total delivered impulse in closed form."""
    _require_positive("contact_count", contact_count)
    _require_positive("closing_score_magnitude", closing_score_magnitude)
    n = contact_count
    q = closing_score_magnitude
    if (q * n) % 2 == 0:
        numerator = q * n * (n + 1) * (n + 2)
        if numerator % 12:
            raise AssertionError("even-parity total-impulse numerator lost divisibility")
        result = numerator // 12
    else:
        numerator = (
            2 * q * n * (n + 1) * (n + 2)
            + 3 * (n + 1) * (n + 1)
        )
        if numerator % 24:
            raise AssertionError("odd-parity total-impulse numerator lost divisibility")
        result = numerator // 24

    if result != sum(uniform_chain_minimum_impulse_vector(n, q)):
        raise AssertionError("minimum-total closed form disagrees with impulse vector")
    return result


def uniform_chain_parity_surplus_contact(
    contact_count: int,
    closing_score_magnitude: int,
) -> int | None:
    """Return the zero-based central surplus contact, or ``None`` when absent."""
    _require_positive("contact_count", contact_count)
    _require_positive("closing_score_magnitude", closing_score_magnitude)
    if (contact_count * closing_score_magnitude) % 2 == 0:
        return None
    return contact_count // 2


def uniform_chain_candidate_is_feasible(
    contact_count: int,
    closing_score_magnitude: int,
    impulse_vector: tuple[int, ...] | list[int],
) -> bool:
    """Check the path inequalities directly, independently of network objects."""
    _require_positive("contact_count", contact_count)
    _require_positive("closing_score_magnitude", closing_score_magnitude)
    impulses = tuple(impulse_vector)
    if len(impulses) != contact_count:
        raise ValueError("impulse_vector must match contact_count")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in impulses
    ):
        raise ValueError("impulse_vector entries must be non-negative integers")
    q = closing_score_magnitude
    return all(
        2 * impulses[index]
        - (impulses[index - 1] if index else 0)
        - (impulses[index + 1] if index + 1 < len(impulses) else 0)
        >= q
        for index in range(len(impulses))
    )


def _validate_uniform_chain_state(state: ContactNetworkMomentum1D) -> int:
    contact_count = len(state.contacts)
    if contact_count < 1 or len(state.masses) != contact_count + 1:
        raise ValueError("uniform chain requires n contacts on n+1 bodies")
    if len(set(state.masses)) != 1:
        raise ValueError("uniform-chain closed form requires equal masses")

    expected_contacts = tuple(
        ContactChannel1D(index, index + 1, 1)
        for index in range(contact_count)
    )
    if state.contacts != expected_contacts:
        raise ValueError("uniform-chain closed form requires canonical consecutive +1 contacts")

    scores = contact_relative_scores(state)
    if not scores or any(score >= 0 for score in scores):
        raise ValueError("uniform-chain closed form requires strictly closing contacts")
    if len(set(scores)) != 1:
        raise ValueError("uniform-chain closed form requires one common closing score")
    return -scores[0]


@dataclass(frozen=True)
class UniformChainImpulseSolution1D:
    before: ContactNetworkMomentum1D
    contact_count: int
    closing_score_magnitude: int
    impulse_vector: tuple[int, ...]
    minimum_total_impulse: int
    score_increment: tuple[int, ...]
    final_scores: tuple[int, ...]
    final_momenta: tuple[int, ...]
    parity_surplus_contact: int | None
    exact_comoving_consensus: bool


def solve_uniform_chain_nonclosing_impulse(
    state: ContactNetworkMomentum1D,
) -> UniformChainImpulseSolution1D:
    """Apply and certify the closed-form minimum impulse to one uniform chain."""
    q = _validate_uniform_chain_state(state)
    n = len(state.contacts)
    impulses = uniform_chain_minimum_impulse_vector(n, q)
    step = apply_contact_impulse_vector(state, impulses)
    increments = uniform_chain_score_increment(n, q)
    expected_final = tuple(
        increment - q
        for increment in increments
    )
    if step.relative_scores_after != expected_final:
        raise AssertionError("uniform-chain network application disagrees with closed form")
    if any(score < 0 for score in expected_final):
        raise AssertionError("uniform-chain closed form left a closing contact")

    parity_contact = uniform_chain_parity_surplus_contact(n, q)
    if parity_contact is None:
        if any(expected_final):
            raise AssertionError("even-parity chain failed exact comoving consensus")
        exact_consensus = True
    else:
        if tuple(
            1 if index == parity_contact else 0
            for index in range(n)
        ) != expected_final:
            raise AssertionError("odd-parity chain lost its unique central surplus")
        exact_consensus = False

    # Cross-check that this really is the path Gram already declared by the
    # contact-network owner, rather than a second independently defined coupling.
    expected_gram = tuple(
        tuple(
            2 if row == col else -1 if abs(row - col) == 1 else 0
            for col in range(n)
        )
        for row in range(n)
    )
    if contact_coupling_gram(state) != expected_gram:
        raise AssertionError("uniform chain no longer has the expected path Gram")
    expected_incidence = tuple(
        tuple(
            -1 if edge == body else 1 if edge + 1 == body else 0
            for edge in range(n)
        )
        for body in range(n + 1)
    )
    if contact_incidence_matrix(state) != expected_incidence:
        raise AssertionError("uniform chain no longer has the expected incidence matrix")

    return UniformChainImpulseSolution1D(
        before=state,
        contact_count=n,
        closing_score_magnitude=q,
        impulse_vector=impulses,
        minimum_total_impulse=uniform_chain_minimum_total_impulse(n, q),
        score_increment=increments,
        final_scores=expected_final,
        final_momenta=step.after.momenta,
        parity_surplus_contact=parity_contact,
        exact_comoving_consensus=exact_consensus,
    )
