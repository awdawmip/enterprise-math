"""Exact causal word normal form for E001 contact-score impulse actions.

The E001 contact-network mother algebra gives an integer contact-score state

    r in Z^m

and a fixed integer coupling matrix ``K``.  Delivering one unit impulse on
contact ``i`` adds column ``i`` of ``K``.  The local causal action is enabled
only while that contact is closing:

    G_i(r) = r + K e_i,       defined iff r_i < 0.

For a literal contact word, let ``j_t`` be the vector of action counts before
one step.  When contact ``i`` is selected at that step, legality is

    r_i + (K j_t)_i < 0.

Therefore the entire word domain and exact final contact-score state are
captured by two finite coordinates:

    Delta = K j_final,
    H_i = max {(K j_t)_i : step t selects contact i},

with ``H_i=None`` when the word never selects contact ``i``.  The induced
partial affine map is exactly

    r -> r + Delta

on the rectangular domain

    r_i < -H_i                 for every used contact i.

Literal ordering is no longer needed after ``(Delta,H)`` is known.

The profile is closed under causal concatenation.  If ``p`` runs before ``q``,

    Delta_(pq) = Delta_p + Delta_q,
    H_(pq) = max_coordinatewise(H_p, Delta_p + H_q),

where ``None`` means no requirement / negative infinity.  Distinct profiles
induce distinct partial maps on ``Z^m``; the module constructs a separating
integer state.

A zero-shift profile ``Delta=0`` is a partial identity and is idempotent.
Zero-shift profiles compose by componentwise maximum of their requirements,
which is exactly intersection of their rectangular domains.  Thus kernel words
do not necessarily collapse to one group identity: they form a semilattice of
causal domain idempotents.

For distinct unit actions, unguarded score additions commute automatically,
but the guarded partial maps commute on the whole score space exactly when
both directed cross couplings vanish:

    K_ij = K_ji = 0.

For symmetric contact Gram matrices this reduces to ``K_ij=0``.  This is
strictly stronger than the nonpositive-cross-coupling condition that guarantees
no cross-disable inside the restricted region where both contacts are already
closing.

For a contact Gram ``K=B^T D B``, the previously established E001 identity
``ker K = ker B`` means cycle-space impulse counts have zero body/contact-score
shift.  Any legal word carrying such a count vector is therefore a partial
identity at this coarse state layer.  Repeating the same zero-shift word does
not change its coarse partial map, although contact-local witness/damage/history
observables may still distinguish the repetitions.  This module does not erase
such richer witness state automatically.

Partial transformations, affine guards, max-plus requirement propagation and
idempotent domain restrictions are standard prior mathematics.  The project
result is the exact E001/P024 specialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _square_integer_matrix(matrix: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in matrix)
    if not rows:
        raise ValueError("coupling matrix must be nonempty")
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("coupling matrix must be square")
    for row in rows:
        for value in row:
            _require_int("coupling entry", value)
    return rows


def _integer_vector(
    values: Sequence[int] | Iterable[int],
    size: int,
    *,
    name: str,
) -> Vector:
    result = tuple(values)
    if len(result) != size:
        raise ValueError(f"{name} must have length {size}")
    for value in result:
        _require_int(name, value)
    return result


def _column(matrix: Matrix, index: int) -> Vector:
    return tuple(row[index] for row in matrix)


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def _optional_max(
    left: int | None,
    right: int | None,
) -> int | None:
    if left is None:
        return right
    if right is None:
        return left
    return max(left, right)


@dataclass(frozen=True)
class ContactGuardedWordProfile:
    """Exact partial-affine operation induced on contact-score state."""

    score_shift: Vector
    requirements: tuple[int | None, ...]

    @property
    def dimension(self) -> int:
        return len(self.score_shift)

    @property
    def is_partial_identity(self) -> bool:
        return all(value == 0 for value in self.score_shift)


@dataclass(frozen=True)
class ContactGuardedOutcome:
    defined: bool
    state: Vector | None


def _validate_profile(profile: ContactGuardedWordProfile) -> None:
    if not isinstance(profile, ContactGuardedWordProfile):
        raise TypeError("profile must be ContactGuardedWordProfile")
    if not profile.score_shift:
        raise ValueError("profile dimension must be positive")
    if len(profile.requirements) != len(profile.score_shift):
        raise ValueError("requirements must match score-shift dimension")
    for value in profile.score_shift:
        _require_int("score_shift", value)
    for value in profile.requirements:
        if value is not None:
            _require_int("requirement", value)


def empty_contact_guarded_profile(
    dimension: int,
) -> ContactGuardedWordProfile:
    _require_int("dimension", dimension)
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    return ContactGuardedWordProfile(
        score_shift=(0,) * dimension,
        requirements=(None,) * dimension,
    )


def contact_word_action_counts(
    word: Iterable[int],
    dimension: int,
) -> Vector:
    _require_int("dimension", dimension)
    if dimension <= 0:
        raise ValueError("dimension must be positive")
    counts = [0] * dimension
    for action in tuple(word):
        _require_int("action", action)
        if not 0 <= action < dimension:
            raise ValueError("contact action index is outside the score space")
        counts[action] += 1
    return tuple(counts)


def contact_guarded_word_profile(
    coupling: Sequence[Sequence[int]],
    word: Iterable[int],
) -> ContactGuardedWordProfile:
    """Compile one literal contact-action word to exact ``(Delta,H)``."""
    matrix = _square_integer_matrix(coupling)
    dimension = len(matrix)
    actions = tuple(word)

    delta = (0,) * dimension
    requirements: list[int | None] = [None] * dimension

    for action in actions:
        _require_int("action", action)
        if not 0 <= action < dimension:
            raise ValueError("contact action index is outside the score space")
        current_requirement = delta[action]
        requirements[action] = _optional_max(
            requirements[action],
            current_requirement,
        )
        delta = _add(delta, _column(matrix, action))

    return ContactGuardedWordProfile(
        score_shift=delta,
        requirements=tuple(requirements),
    )


def contact_profile_defined(
    state: Sequence[int],
    profile: ContactGuardedWordProfile,
) -> bool:
    """Whether one profile is causally executable from ``state``."""
    _validate_profile(profile)
    values = _integer_vector(
        state,
        profile.dimension,
        name="state",
    )
    return all(
        requirement is None or value < -requirement
        for value, requirement in zip(
            values,
            profile.requirements,
            strict=True,
        )
    )


def apply_contact_guarded_profile(
    state: Sequence[int],
    profile: ContactGuardedWordProfile,
) -> ContactGuardedOutcome:
    """Apply the compiled partial affine map."""
    _validate_profile(profile)
    values = _integer_vector(
        state,
        profile.dimension,
        name="state",
    )
    if not contact_profile_defined(values, profile):
        return ContactGuardedOutcome(False, None)
    return ContactGuardedOutcome(
        True,
        _add(values, profile.score_shift),
    )


def apply_contact_guarded_word(
    coupling: Sequence[Sequence[int]],
    state: Sequence[int],
    word: Iterable[int],
) -> ContactGuardedOutcome:
    """Direct literal-word oracle for the guarded contact-score dynamics."""
    matrix = _square_integer_matrix(coupling)
    dimension = len(matrix)
    current = _integer_vector(state, dimension, name="state")

    for action in tuple(word):
        _require_int("action", action)
        if not 0 <= action < dimension:
            raise ValueError("contact action index is outside the score space")
        if current[action] >= 0:
            return ContactGuardedOutcome(False, None)
        current = _add(current, _column(matrix, action))
    return ContactGuardedOutcome(True, current)


def compose_contact_guarded_profiles(
    first: ContactGuardedWordProfile,
    second: ContactGuardedWordProfile,
) -> ContactGuardedWordProfile:
    """Exact profile for running ``first`` and then ``second``."""
    _validate_profile(first)
    _validate_profile(second)
    if first.dimension != second.dimension:
        raise ValueError("profile dimensions must agree")

    shifted_second_requirements = tuple(
        None if requirement is None else shift + requirement
        for shift, requirement in zip(
            first.score_shift,
            second.requirements,
            strict=True,
        )
    )
    return ContactGuardedWordProfile(
        score_shift=_add(first.score_shift, second.score_shift),
        requirements=tuple(
            _optional_max(left, right)
            for left, right in zip(
                first.requirements,
                shifted_second_requirements,
                strict=True,
            )
        ),
    )


def contact_guarded_profile_power(
    profile: ContactGuardedWordProfile,
    exponent: int,
) -> ContactGuardedWordProfile:
    """Exact closed form for one profile power.

    For ``n>=1`` the score shift is ``n*Delta``.  A used guard coordinate with
    requirement ``H_i`` tightens only when the macro shift on that coordinate is
    positive:

        H_i^(n) = H_i + (n-1)*max(Delta_i,0).

    ``None`` remains unconstrained.  In particular every zero-shift profile is
    idempotent.
    """
    _validate_profile(profile)
    _require_int("exponent", exponent)
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    if exponent == 0:
        return empty_contact_guarded_profile(profile.dimension)

    requirements = tuple(
        (
            None
            if requirement is None
            else requirement
            + (exponent - 1) * max(shift, 0)
        )
        for shift, requirement in zip(
            profile.score_shift,
            profile.requirements,
            strict=True,
        )
    )
    return ContactGuardedWordProfile(
        score_shift=tuple(
            exponent * shift
            for shift in profile.score_shift
        ),
        requirements=requirements,
    )


def contact_guarded_profile_repetition_capacity(
    state: Sequence[int],
    profile: ContactGuardedWordProfile,
) -> int | None:
    """Maximum positive repetitions from ``state``; ``None`` means unbounded.

    Return ``0`` if the macro profile is not legal even once.  Otherwise every
    used coordinate with positive macro shift ``Delta_i`` imposes

        n <= 1 + floor((-1-r_i-H_i)/Delta_i).

    Coordinates with nonpositive macro shift never create a later failure.
    """
    _validate_profile(profile)
    values = _integer_vector(
        state,
        profile.dimension,
        name="state",
    )
    if not contact_profile_defined(values, profile):
        return 0

    finite_bounds = []
    for value, shift, requirement in zip(
        values,
        profile.score_shift,
        profile.requirements,
        strict=True,
    ):
        if requirement is None or shift <= 0:
            continue
        slack = -1 - value - requirement
        if slack < 0:
            raise AssertionError("defined profile has negative repetition slack")
        finite_bounds.append(1 + slack // shift)

    if not finite_bounds:
        return None
    return min(finite_bounds)


def _common_domain_point(
    left: ContactGuardedWordProfile,
    right: ContactGuardedWordProfile,
) -> Vector:
    values = []
    for first, second in zip(
        left.requirements,
        right.requirements,
        strict=True,
    ):
        bounds = []
        if first is not None:
            bounds.append(-first)
        if second is not None:
            bounds.append(-second)
        values.append(min(bounds) - 1 if bounds else 0)
    return tuple(values)


def contact_profile_separating_state(
    left: ContactGuardedWordProfile,
    right: ContactGuardedWordProfile,
) -> Vector:
    """Construct a state distinguishing any two distinct profiles."""
    _validate_profile(left)
    _validate_profile(right)
    if left.dimension != right.dimension:
        raise ValueError("profile dimensions must agree")
    if left == right:
        raise ValueError("equal profiles have no separating state")

    for index, (first, second) in enumerate(
        zip(left.requirements, right.requirements, strict=True)
    ):
        if first == second:
            continue
        state = list(_common_domain_point(left, right))
        if first is None:
            assert second is not None
            state[index] = -second
        elif second is None:
            state[index] = -first
        elif first > second:
            state[index] = -first
        else:
            state[index] = -second
        return tuple(state)

    if left.score_shift != right.score_shift:
        return _common_domain_point(left, right)

    raise AssertionError("distinct profiles lost every separating coordinate")


def zero_shift_domain_product(
    left: ContactGuardedWordProfile,
    right: ContactGuardedWordProfile,
) -> ContactGuardedWordProfile:
    """Compose two partial identities; requirements join by componentwise max."""
    _validate_profile(left)
    _validate_profile(right)
    if not left.is_partial_identity or not right.is_partial_identity:
        raise ValueError("zero-shift domain product requires partial identities")
    return compose_contact_guarded_profiles(left, right)


def unit_contact_actions_commute_extensionally(
    coupling: Sequence[Sequence[int]],
    left_action: int,
    right_action: int,
) -> bool:
    """Exact global partial-map commutativity criterion for two unit actions.

    Unguarded additions always commute.  With contact-local closing guards,
    distinct unit actions commute as partial maps on the whole score space
    exactly when neither action shifts the other action's guarded coordinate:

        K[left,right] = K[right,left] = 0.

    For symmetric contact Gram matrices this reduces to one off-diagonal zero.
    """
    matrix = _square_integer_matrix(coupling)
    dimension = len(matrix)
    _require_int("left_action", left_action)
    _require_int("right_action", right_action)
    if not 0 <= left_action < dimension:
        raise ValueError("left_action is outside the score space")
    if not 0 <= right_action < dimension:
        raise ValueError("right_action is outside the score space")
    if left_action == right_action:
        return True

    predicted = (
        matrix[left_action][right_action] == 0
        and matrix[right_action][left_action] == 0
    )
    left = contact_guarded_word_profile(
        matrix,
        (left_action, right_action),
    )
    right = contact_guarded_word_profile(
        matrix,
        (right_action, left_action),
    )
    if (left == right) != predicted:
        raise AssertionError("unit guarded commutativity disagrees with cross coupling")
    return predicted


def guarded_contact_family_is_globally_commutative(
    coupling: Sequence[Sequence[int]],
) -> bool:
    """Whether every pair of unit guarded contact actions commutes globally."""
    matrix = _square_integer_matrix(coupling)
    dimension = len(matrix)
    return all(
        unit_contact_actions_commute_extensionally(matrix, left, right)
        for left in range(dimension)
        for right in range(left + 1, dimension)
    )
