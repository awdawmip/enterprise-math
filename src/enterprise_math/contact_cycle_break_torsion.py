"""Torsion preservation when one contact breaks a coherent weighted cycle.

For a coherently oriented n-contact cycle with positive integer body weights,
let ``B`` be incidence and ``K=B^T D B``.  The all-ones contact vector is a
primitive kernel generator, so ``coker K`` has one free Z direction plus finite
torsion.

Delete any one contact.  The remaining contacts form a spanning tree and the
new contact Gram is exactly the corresponding principal minor ``K_red``.

Because ``K*1=0``, every vector in ``im K`` has contact-coordinate sum zero.
On the degree-zero target lattice, deleting the broken contact coordinate is an
exact quotient isomorphism:

    {c in Z^n : sum c = 0} / im(K)
        ~= Z^(n-1) / im(K_red).

Constructively, if the reduced target is hit by ``K_red*j``, insert zero in the
broken source coordinate.  The surviving output coordinates are correct by
construction and the missing output coordinate is forced by zero total sum.

Hence the first non-bridge break of a coherent cycle removes exactly the free
cycle ambiguity while preserving the complete finite torsion/reachability
obstruction.  The statement holds for arbitrary positive integer body weights.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .contact_forest_reachability import apply_integer_matrix
from .contact_weighted_forest_reachability import (
    common_weight_tree_cokernel_invariant_factors,
    solve_weighted_forest_contact_target,
    weighted_forest_contact_gram,
    weighted_tree_determinant,
)


Edge = tuple[int, int]
Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def coherent_cycle_edges(body_count: int) -> tuple[Edge, ...]:
    _require_int("body_count", body_count)
    if body_count < 3:
        raise ValueError("coherent cycle requires at least three bodies")
    return tuple((index, (index + 1) % body_count) for index in range(body_count))


def _positive_weights(values: Sequence[int] | Iterable[int]) -> Vector:
    result = tuple(values)
    if len(result) < 3:
        raise ValueError("cycle body weights require at least three entries")
    for value in result:
        _require_int("body weight", value)
        if value <= 0:
            raise ValueError("body weights must be positive")
    return result


def weighted_cycle_contact_gram(
    body_weights: Sequence[int] | Iterable[int],
) -> Matrix:
    weights = _positive_weights(body_weights)
    n = len(weights)
    edges = coherent_cycle_edges(n)
    rows = [[0] * n for _ in range(n)]
    for edge, (tail, head) in enumerate(edges):
        rows[tail][edge] = -1
        rows[head][edge] = 1
    return tuple(
        tuple(
            sum(
                weights[body] * rows[body][left] * rows[body][right]
                for body in range(n)
            )
            for right in range(n)
        )
        for left in range(n)
    )


def surviving_tree_edges(
    body_count: int,
    removed_contact: int,
) -> tuple[Edge, ...]:
    edges = coherent_cycle_edges(body_count)
    _require_int("removed_contact", removed_contact)
    if not 0 <= removed_contact < body_count:
        raise ValueError("removed_contact is outside the cycle")
    return tuple(
        edge for index, edge in enumerate(edges) if index != removed_contact
    )


def cycle_principal_minor_after_break(
    body_weights: Sequence[int],
    removed_contact: int,
) -> Matrix:
    weights = _positive_weights(body_weights)
    gram = weighted_cycle_contact_gram(weights)
    if not 0 <= removed_contact < len(weights):
        raise ValueError("removed_contact is outside the cycle")
    keep = tuple(index for index in range(len(weights)) if index != removed_contact)
    return tuple(
        tuple(gram[left][right] for right in keep)
        for left in keep
    )


def reduced_degree_zero_target(
    target: Sequence[int] | Iterable[int],
    removed_contact: int,
) -> Vector:
    values = tuple(target)
    for value in values:
        _require_int("target", value)
    if len(values) < 3:
        raise ValueError("cycle target must have at least three coordinates")
    if sum(values) != 0:
        raise ValueError("torsion target must have contact-coordinate sum zero")
    _require_int("removed_contact", removed_contact)
    if not 0 <= removed_contact < len(values):
        raise ValueError("removed_contact is outside the target")
    return tuple(
        value for index, value in enumerate(values) if index != removed_contact
    )


def lift_reduced_degree_zero_target(
    reduced_target: Sequence[int] | Iterable[int],
    removed_contact: int,
) -> Vector:
    reduced = tuple(reduced_target)
    for value in reduced:
        _require_int("reduced_target", value)
    body_count = len(reduced) + 1
    if body_count < 3:
        raise ValueError("reduced cycle target must have at least two coordinates")
    _require_int("removed_contact", removed_contact)
    if not 0 <= removed_contact < body_count:
        raise ValueError("removed_contact is outside the lifted target")
    missing = -sum(reduced)
    result = []
    cursor = 0
    for index in range(body_count):
        if index == removed_contact:
            result.append(missing)
        else:
            result.append(reduced[cursor])
            cursor += 1
    return tuple(result)


def lift_reduced_cycle_impulse(
    reduced_impulse: Sequence[int] | Iterable[int],
    removed_contact: int,
) -> Vector:
    reduced = tuple(reduced_impulse)
    for value in reduced:
        _require_int("reduced_impulse", value)
    body_count = len(reduced) + 1
    if body_count < 3:
        raise ValueError("reduced cycle impulse must have at least two coordinates")
    _require_int("removed_contact", removed_contact)
    if not 0 <= removed_contact < body_count:
        raise ValueError("removed_contact is outside the lifted impulse")
    result = []
    cursor = 0
    for index in range(body_count):
        if index == removed_contact:
            result.append(0)
        else:
            result.append(reduced[cursor])
            cursor += 1
    return tuple(result)


def solve_cycle_degree_zero_target(
    body_weights: Sequence[int],
    target: Sequence[int],
    removed_contact: int = 0,
) -> Vector | None:
    """Solve ``Kj=target`` modulo the cycle kernel via one broken-edge tree."""
    weights = _positive_weights(body_weights)
    if len(target) != len(weights):
        raise ValueError("target must have one coordinate per cycle contact")
    reduced = reduced_degree_zero_target(target, removed_contact)
    tree_edges = surviving_tree_edges(len(weights), removed_contact)
    reduced_impulse = solve_weighted_forest_contact_target(
        len(weights),
        tree_edges,
        weights,
        reduced,
    )
    if reduced_impulse is None:
        return None
    full = lift_reduced_cycle_impulse(reduced_impulse, removed_contact)
    if apply_integer_matrix(weighted_cycle_contact_gram(weights), full) != tuple(target):
        raise AssertionError("lifted cycle impulse missed the full degree-zero target")
    return full


def cycle_degree_zero_target_is_reachable(
    body_weights: Sequence[int],
    target: Sequence[int],
    removed_contact: int = 0,
) -> bool:
    return solve_cycle_degree_zero_target(
        body_weights,
        target,
        removed_contact,
    ) is not None


def cycle_finite_torsion_order(body_weights: Sequence[int]) -> int:
    """Order of the torsion part of the coherent cycle Gram cokernel."""
    weights = _positive_weights(body_weights)
    return weighted_tree_determinant(weights)


@dataclass(frozen=True)
class CycleBreakTorsionReport:
    body_count: int
    removed_contact: int
    before_free_rank: int
    after_free_rank: int
    finite_torsion_order_before: int
    finite_cokernel_order_after: int
    common_weight_torsion_invariant_factors: tuple[int, ...] | None

    @property
    def free_rank_drop(self) -> int:
        return self.before_free_rank - self.after_free_rank

    @property
    def finite_torsion_order_preserved(self) -> bool:
        return (
            self.finite_torsion_order_before
            == self.finite_cokernel_order_after
        )


def cycle_break_torsion_report(
    body_weights: Sequence[int],
    removed_contact: int,
) -> CycleBreakTorsionReport:
    weights = _positive_weights(body_weights)
    if not 0 <= removed_contact < len(weights):
        raise ValueError("removed_contact is outside the cycle")
    tree_edges = surviving_tree_edges(len(weights), removed_contact)
    tree_gram = weighted_forest_contact_gram(
        len(weights),
        tree_edges,
        weights,
    )
    # The tree determinant is the finite order after the break.  The cycle
    # degree-zero/reduced isomorphism identifies the same value before it.
    after_order = weighted_tree_determinant(weights)
    if len(tree_gram) != len(weights) - 1:
        raise AssertionError("cycle break did not produce a spanning tree Gram")

    common: tuple[int, ...] | None
    if len(set(weights)) == 1:
        common = common_weight_tree_cokernel_invariant_factors(
            len(weights),
            weights[0],
        )
    else:
        common = None

    return CycleBreakTorsionReport(
        body_count=len(weights),
        removed_contact=removed_contact,
        before_free_rank=1,
        after_free_rank=0,
        finite_torsion_order_before=cycle_finite_torsion_order(weights),
        finite_cokernel_order_after=after_order,
        common_weight_torsion_invariant_factors=common,
    )
