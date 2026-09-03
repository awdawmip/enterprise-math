"""Exact positive-rational BRC feedback condensation and interaction tools.

Foundation extraction of main-backed PRs #1142/#1144/#1146/#1147.
The old finite rational background is first reduced to its exact star, then a
small feedback-event kernel carries all newly created positive total-mass
recurrence.

Subset/Mobius functions are exponential in the number of declared events and
are intended for small explicit feedback sets.  No runtime-speedup theorem is
claimed by this reference implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .brc_weighted_recurrent import (
    RationalInput,
    RationalMatrix,
    RationalMatrixInput,
    finite_recurrent_mass_analysis,
)


@dataclass(frozen=True)
class FeedbackEvent:
    source: int
    target: int
    mass: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.source, bool) or isinstance(self.target, bool):
            raise TypeError("feedback endpoints must be integer indices")
        if not isinstance(self.source, int) or not isinstance(self.target, int):
            raise TypeError("feedback endpoints must be integer indices")
        if isinstance(self.mass, bool) or not isinstance(self.mass, (int, Fraction)):
            raise TypeError("feedback mass must be int or Fraction")
        value = Fraction(self.mass)
        if value <= 0:
            raise ValueError("feedback mass must be positive")
        object.__setattr__(self, "mass", value)


def feedback_event(source: int, target: int, mass: RationalInput) -> FeedbackEvent:
    """Construct a typed positive feedback event without bool-to-int coercion."""
    if isinstance(mass, bool) or not isinstance(mass, (int, Fraction)):
        raise TypeError("feedback mass must be int or Fraction")
    return FeedbackEvent(source, target, Fraction(mass))


def _determinant(matrix: Sequence[Sequence[Fraction | int]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1, 1)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    work = [[Fraction(value) for value in row] for row in matrix]
    out = Fraction(1, 1)
    sign = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0, 1)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def _normalize_events(events: Sequence[FeedbackEvent], vertex_count: int) -> tuple[FeedbackEvent, ...]:
    result: list[FeedbackEvent] = []
    for event in events:
        if not isinstance(event, FeedbackEvent):
            raise TypeError("events must be FeedbackEvent values")
        if not (0 <= event.source < vertex_count and 0 <= event.target < vertex_count):
            raise ValueError("feedback endpoint out of background range")
        result.append(event)
    return tuple(result)


def _kernel_from_star(star: RationalMatrix, events: Sequence[FeedbackEvent]) -> RationalMatrix:
    return tuple(
        tuple(star[row_event.target][col_event.source] * col_event.mass for col_event in events)
        for row_event in events
    )


def feedback_event_kernel(matrix: RationalMatrixInput, events: Sequence[FeedbackEvent]) -> RationalMatrix:
    """Return ``F_rs=S[b_r,a_s]*delta_s`` for a stable old background."""
    background = finite_recurrent_mass_analysis(matrix)
    if not background.stable or background.star is None:
        raise ValueError("feedback condensation requires a stable finite rational background")
    normalized = _normalize_events(events, len(background.mass_matrix))
    return _kernel_from_star(background.star, normalized)


def _updated_star(
    background_star: RationalMatrix,
    events: tuple[FeedbackEvent, ...],
    feedback_star: RationalMatrix,
) -> RationalMatrix:
    n = len(background_star)
    m = len(events)
    return tuple(
        tuple(
            background_star[i][j]
            + sum(
                (
                    background_star[i][events[r].source]
                    * events[r].mass
                    * feedback_star[r][s]
                    * background_star[events[s].target][j]
                    for r in range(m)
                    for s in range(m)
                ),
                Fraction(0, 1),
            )
            for j in range(n)
        )
        for i in range(n)
    )


@dataclass(frozen=True)
class FeedbackCondensationAnalysis:
    events: tuple[FeedbackEvent, ...]
    feedback_kernel: RationalMatrix
    stable: bool
    loop_zeta_factor: Fraction | None
    updated_star: RationalMatrix | None


def feedback_condensation(
    matrix: RationalMatrixInput,
    events: Sequence[FeedbackEvent],
) -> FeedbackCondensationAnalysis:
    """Condense inserted positive events to their exact recurrent event kernel."""
    background = finite_recurrent_mass_analysis(matrix)
    if not background.stable or background.star is None:
        raise ValueError("feedback condensation requires a stable finite rational background")
    normalized = _normalize_events(events, len(background.mass_matrix))
    if not normalized:
        return FeedbackCondensationAnalysis(
            events=(),
            feedback_kernel=(),
            stable=True,
            loop_zeta_factor=Fraction(1, 1),
            updated_star=background.star,
        )
    kernel = _kernel_from_star(background.star, normalized)
    feedback = finite_recurrent_mass_analysis(kernel)
    if not feedback.stable or feedback.star is None:
        return FeedbackCondensationAnalysis(
            events=normalized,
            feedback_kernel=kernel,
            stable=False,
            loop_zeta_factor=None,
            updated_star=None,
        )
    zeta = _determinant(feedback.star)
    if zeta < 1:
        raise AssertionError("positive feedback loop zeta factor must be >=1")
    return FeedbackCondensationAnalysis(
        events=normalized,
        feedback_kernel=kernel,
        stable=True,
        loop_zeta_factor=zeta,
        updated_star=_updated_star(background.star, normalized, feedback.star),
    )


def feedback_additive_radius(
    matrix: RationalMatrixInput,
    source: int,
    target: int,
) -> Fraction | None:
    """Return exact new-edge additive critical mass; ``None`` means infinite radius."""
    background = finite_recurrent_mass_analysis(matrix)
    if not background.stable or background.star is None:
        raise ValueError("feedback radius requires a stable finite rational background")
    n = len(background.mass_matrix)
    if isinstance(source, bool) or isinstance(target, bool) or not isinstance(source, int) or not isinstance(target, int):
        raise TypeError("source/target must be integer indices")
    if not (0 <= source < n and 0 <= target < n):
        raise ValueError("source/target out of range")
    return_mass = background.star[target][source]
    return None if return_mass == 0 else Fraction(1, 1) / return_mass


def conditional_feedback_kernel(
    matrix: RationalMatrixInput,
    installed_events: Sequence[FeedbackEvent],
    candidate_events: Sequence[FeedbackEvent],
) -> RationalMatrix:
    """Return the candidate-event kernel after a stable installed feedback module."""
    installed = feedback_condensation(matrix, installed_events)
    if not installed.stable or installed.updated_star is None:
        raise ValueError("installed feedback module must remain stable")
    normalized_candidates = _normalize_events(candidate_events, len(installed.updated_star))
    return _kernel_from_star(installed.updated_star, normalized_candidates)


def _principal(matrix: RationalMatrix, mask: int) -> RationalMatrix:
    indices = [i for i in range(len(matrix)) if mask & (1 << i)]
    return tuple(tuple(matrix[i][j] for j in indices) for i in indices)


def _kernel_zeta(kernel: RationalMatrix) -> Fraction:
    if not kernel:
        return Fraction(1, 1)
    analysis = finite_recurrent_mass_analysis(kernel)
    if not analysis.stable or analysis.star is None:
        raise ValueError("feedback interaction table requires every selected kernel to be stable")
    return _determinant(analysis.star)


def feedback_subset_zeta_factors(
    matrix: RationalMatrixInput,
    events: Sequence[FeedbackEvent],
) -> tuple[tuple[int, Fraction], ...]:
    """Return exact ``(subset_mask, Z(A))`` table for a fully stable event universe.

    Complexity is exponential in the number of events.
    """
    background = finite_recurrent_mass_analysis(matrix)
    if not background.stable or background.star is None:
        raise ValueError("feedback interactions require a stable finite rational background")
    normalized = _normalize_events(events, len(background.mass_matrix))
    if not normalized:
        return ((0, Fraction(1, 1)),)
    kernel = _kernel_from_star(background.star, normalized)
    full = finite_recurrent_mass_analysis(kernel)
    if not full.stable:
        raise ValueError("full declared feedback universe must be stable before Gamma interactions are formed")
    table: list[tuple[int, Fraction]] = [(0, Fraction(1, 1))]
    for mask in range(1, 1 << len(normalized)):
        table.append((mask, _kernel_zeta(_principal(kernel, mask))))
    return tuple(table)


def feedback_mobius_interaction_factors(
    matrix: RationalMatrixInput,
    events: Sequence[FeedbackEvent],
) -> tuple[tuple[int, Fraction], ...]:
    """Return exact rational all-orders interaction factors ``J_T>=1``.

    Complexity is exponential in the number of events.
    """
    zeta = dict(feedback_subset_zeta_factors(matrix, events))
    event_count = len(events)
    interactions: list[tuple[int, Fraction]] = []
    for mask in range(1, 1 << event_count):
        factor = Fraction(1, 1)
        submask = mask
        while True:
            parity = (mask.bit_count() - submask.bit_count()) & 1
            if parity:
                factor /= zeta[submask]
            else:
                factor *= zeta[submask]
            if submask == 0:
                break
            submask = (submask - 1) & mask
        if factor < 1:
            raise AssertionError("positive feedback Mobius interaction factor must be >=1")
        interactions.append((mask, factor))
    return tuple(interactions)


def feedback_interaction_girth(
    matrix: RationalMatrixInput,
    events: Sequence[FeedbackEvent],
) -> int | None:
    """Return first nonzero interaction order; ``None`` denotes acyclic event support."""
    interactions = feedback_mobius_interaction_factors(matrix, events)
    orders = [mask.bit_count() for mask, factor in interactions if factor > 1]
    return min(orders) if orders else None


def _proper_nonempty_submasks(mask: int):
    submask = (mask - 1) & mask
    while submask:
        yield submask
        submask = (submask - 1) & mask


def _induced_simple_cycle(kernel: RationalMatrix, mask: int) -> bool:
    indices = [i for i in range(len(kernel)) if mask & (1 << i)]
    if len(indices) == 1:
        return kernel[indices[0]][indices[0]] > 0
    allowed = set(indices)
    for i in indices:
        if sum(kernel[i][j] > 0 for j in indices) != 1:
            return False
        if sum(kernel[j][i] > 0 for j in indices) != 1:
            return False
    start = indices[0]
    current = start
    reached = {start}
    for _ in range(len(indices)):
        current = next(j for j in indices if kernel[current][j] > 0)
        reached.add(current)
    return current == start and reached == allowed


def _cycle_product(kernel: RationalMatrix, mask: int) -> Fraction:
    indices = [i for i in range(len(kernel)) if mask & (1 << i)]
    if len(indices) == 1:
        return kernel[indices[0]][indices[0]]
    if not _induced_simple_cycle(kernel, mask):
        raise ValueError("mask does not induce one directed simple cycle")
    start = indices[0]
    current = start
    value = Fraction(1, 1)
    for _ in range(len(indices)):
        nxt = next(j for j in indices if kernel[current][j] > 0)
        value *= kernel[current][nxt]
        current = nxt
    return value


@dataclass(frozen=True)
class FeedbackCircuitAtom:
    event_indices: tuple[int, ...]
    rational_holonomy: Fraction
    interaction_factor: Fraction


def feedback_circuit_atoms(
    matrix: RationalMatrixInput,
    events: Sequence[FeedbackEvent],
) -> tuple[FeedbackCircuitAtom, ...]:
    """Return Möbius-primitive recurrent event supports as exact circuit atoms."""
    background = finite_recurrent_mass_analysis(matrix)
    if not background.stable or background.star is None:
        raise ValueError("feedback circuit atoms require a stable background")
    normalized = _normalize_events(events, len(background.mass_matrix))
    if not normalized:
        return ()
    kernel = _kernel_from_star(background.star, normalized)
    interactions = dict(feedback_mobius_interaction_factors(matrix, normalized))
    atoms: list[FeedbackCircuitAtom] = []
    for mask, factor in interactions.items():
        if factor == 1:
            continue
        if any(interactions[submask] > 1 for submask in _proper_nonempty_submasks(mask)):
            continue
        if not _induced_simple_cycle(kernel, mask):
            raise AssertionError("Möbius-primitive feedback support is not a directed circuit")
        q = _cycle_product(kernel, mask)
        if not (Fraction(0, 1) < q < 1):
            raise AssertionError("stable feedback circuit holonomy must lie in (0,1)")
        if factor != Fraction(1, 1) / (1 - q):
            raise AssertionError("primitive feedback circuit closure disagrees with Mobius factor")
        atoms.append(
            FeedbackCircuitAtom(
                event_indices=tuple(i for i in range(len(normalized)) if mask & (1 << i)),
                rational_holonomy=q,
                interaction_factor=factor,
            )
        )
    return tuple(atoms)
