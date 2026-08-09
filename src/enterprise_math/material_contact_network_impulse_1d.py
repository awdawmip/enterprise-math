"""Integer contact-network impulse coupling for the E001 material world.

This module generalizes the already validated two-body impulse response only at
the *delivered impulse* layer.  Contact discovery and material quantization stay
outside this file.  Each declared contact channel e has endpoints (a,b) and a
normal n_e in {-1,+1}; one non-negative integer j_e is the impulse quantum
already delivered on that channel.

For positive integer masses m_i choose the common mass scale

    L = lcm_i(m_i),   D_i = L / m_i.

Then ``u_i = D_i*p_i`` is an integer common-denominator velocity coordinate. If
B is the signed body/contact incidence matrix (column e has -n_e at a and +n_e
at b), the contact relative-score vector is

    r = B^T D p.

This is not a new relation algebra.  Each component is an integer rescaling of
the corresponding canonical A3 weighted relation entry

    Z_ab = m_b*p_a - m_a*p_b.

For a delivered contact impulse vector j>=0,

    p' = p + B j,
    r' = r + K j,
    K  = B^T D B.

Consequences are exact and integer-only:

* total momentum is preserved because every incidence column sums to zero;
* K is symmetric and satisfies the Gram identity

      x^T K x = sum_i D_i * (B x)_i^2 >= 0;

* two distinct contacts have a nonzero off-diagonal coupling exactly when they
  share a body (for a simple contact graph).  Hence K is diagonal exactly when
  the declared contact graph is a matching.

Therefore a diagonal/pairwise-only nonclosing impulse guess is exact for
body-disjoint contacts but can fail on a contact chain.  The module exposes that
guess as an explicit comparator; it does not silently solve the coupled integer
inequality ``r + K j >= 0``.

This incidence/Gram structure is standard discrete linear algebra; no novelty
claim is made.  The E001 contribution here is its exact finite contact-response
specialization and its connection to the canonical A3 relation state.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .weighted_relation_field import weighted_relation_field


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _ceil_div_positive(numerator: int, denominator: int) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("ceil-div arguments must be positive")
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True, order=True)
class ContactChannel1D:
    body_a: int
    body_b: int
    normal_from_a_to_b: int = 1

    def __post_init__(self) -> None:
        _require_integer("body_a", self.body_a)
        _require_integer("body_b", self.body_b)
        _require_integer("normal_from_a_to_b", self.normal_from_a_to_b)
        if self.body_a == self.body_b:
            raise ValueError("a contact channel must join two distinct bodies")
        if self.normal_from_a_to_b not in (-1, 1):
            raise ValueError("normal_from_a_to_b must be -1 or +1")

    @property
    def unordered_key(self) -> tuple[int, int]:
        return tuple(sorted((self.body_a, self.body_b)))


@dataclass(frozen=True)
class ContactNetworkMomentum1D:
    masses: tuple[int, ...]
    momenta: tuple[int, ...]
    contacts: tuple[ContactChannel1D, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.masses, tuple) or not self.masses:
            raise ValueError("masses must be a nonempty tuple")
        if not isinstance(self.momenta, tuple) or len(self.momenta) != len(self.masses):
            raise ValueError("momenta must match masses")
        for mass in self.masses:
            _require_positive("mass", mass)
        for momentum in self.momenta:
            _require_integer("momentum", momentum)
        if not isinstance(self.contacts, tuple):
            raise ValueError("contacts must be a tuple")

        body_count = len(self.masses)
        seen: set[tuple[int, int]] = set()
        for contact in self.contacts:
            if not isinstance(contact, ContactChannel1D):
                raise ValueError("contacts must contain ContactChannel1D values")
            if not (0 <= contact.body_a < body_count and 0 <= contact.body_b < body_count):
                raise ValueError("contact endpoint is outside the body set")
            if contact.unordered_key in seen:
                raise ValueError("simple contact graph may contain each body pair at most once")
            seen.add(contact.unordered_key)

    @property
    def total_momentum(self) -> int:
        return sum(self.momenta)

    @property
    def common_mass_scale(self) -> int:
        result = 1
        for mass in self.masses:
            result = lcm(result, mass)
        return result

    @property
    def body_scale_weights(self) -> tuple[int, ...]:
        scale = self.common_mass_scale
        return tuple(scale // mass for mass in self.masses)


def contact_incidence_matrix(
    state: ContactNetworkMomentum1D,
) -> tuple[tuple[int, ...], ...]:
    """Return body-by-contact signed incidence B."""
    rows = [[0] * len(state.contacts) for _ in state.masses]
    for edge_index, contact in enumerate(state.contacts):
        normal = contact.normal_from_a_to_b
        rows[contact.body_a][edge_index] = -normal
        rows[contact.body_b][edge_index] = normal
    return tuple(tuple(row) for row in rows)


def scaled_body_velocity_numerators(
    state: ContactNetworkMomentum1D,
) -> tuple[int, ...]:
    """Return integer common-denominator velocity coordinates D_i*p_i."""
    return tuple(
        weight * momentum
        for weight, momentum in zip(state.body_scale_weights, state.momenta)
    )


def contact_relative_scores(
    state: ContactNetworkMomentum1D,
) -> tuple[int, ...]:
    """Return r=B^T D p; negative entries are closing channels."""
    incidence = contact_incidence_matrix(state)
    scaled = scaled_body_velocity_numerators(state)
    return tuple(
        sum(incidence[body][edge] * scaled[body] for body in range(len(state.masses)))
        for edge in range(len(state.contacts))
    )


def contact_relative_scores_from_a3(
    state: ContactNetworkMomentum1D,
) -> tuple[int, ...]:
    """Recover the same scores from canonical A3 weighted relation entries."""
    field = weighted_relation_field(state.masses, state.momenta)
    common_scale = state.common_mass_scale
    scores: list[int] = []
    for contact in state.contacts:
        a, b = contact.body_a, contact.body_b
        divisor = gcd(state.masses[a], state.masses[b])
        relation = field[a][b]
        if relation % divisor != 0:
            raise AssertionError("A3 pair relation lost its capacity-gcd divisibility")
        pair_lcm = lcm(state.masses[a], state.masses[b])
        scale_factor = common_scale // pair_lcm
        scores.append(
            -contact.normal_from_a_to_b
            * scale_factor
            * (relation // divisor)
        )
    result = tuple(scores)
    if result != contact_relative_scores(state):
        raise AssertionError("contact relative score disagrees with A3 relation specialization")
    return result


def contact_coupling_gram(
    state: ContactNetworkMomentum1D,
) -> tuple[tuple[int, ...], ...]:
    """Return K=B^T D B."""
    incidence = contact_incidence_matrix(state)
    weights = state.body_scale_weights
    edge_count = len(state.contacts)
    return tuple(
        tuple(
            sum(
                incidence[body][left]
                * weights[body]
                * incidence[body][right]
                for body in range(len(state.masses))
            )
            for right in range(edge_count)
        )
        for left in range(edge_count)
    )


@dataclass(frozen=True)
class ContactNetworkImpulseStep1D:
    before: ContactNetworkMomentum1D
    impulse_vector: tuple[int, ...]
    momentum_delta: tuple[int, ...]
    coupling_gram: tuple[tuple[int, ...], ...]
    relative_scores_before: tuple[int, ...]
    relative_scores_after: tuple[int, ...]
    after: ContactNetworkMomentum1D


def apply_contact_impulse_vector(
    state: ContactNetworkMomentum1D,
    impulse_vector: tuple[int, ...] | list[int],
) -> ContactNetworkImpulseStep1D:
    """Apply delivered non-negative impulses and verify exact network identities."""
    impulses = tuple(impulse_vector)
    if len(impulses) != len(state.contacts):
        raise ValueError("impulse vector must match contact count")
    for impulse in impulses:
        _require_integer("impulse", impulse)
        if impulse < 0:
            raise ValueError("delivered repulsive impulses must be non-negative")

    incidence = contact_incidence_matrix(state)
    delta = tuple(
        sum(
            incidence[body][edge] * impulses[edge]
            for edge in range(len(state.contacts))
        )
        for body in range(len(state.masses))
    )
    after = ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(
            momentum + change
            for momentum, change in zip(state.momenta, delta)
        ),
        contacts=state.contacts,
    )
    if after.total_momentum != state.total_momentum:
        raise AssertionError("contact incidence update changed total momentum")

    before_scores = contact_relative_scores(state)
    after_scores = contact_relative_scores(after)
    gram = contact_coupling_gram(state)
    expected = tuple(
        before_scores[row]
        + sum(gram[row][col] * impulses[col] for col in range(len(impulses)))
        for row in range(len(impulses))
    )
    if after_scores != expected:
        raise AssertionError("contact score update disagrees with r'=r+Kj")

    return ContactNetworkImpulseStep1D(
        before=state,
        impulse_vector=impulses,
        momentum_delta=delta,
        coupling_gram=gram,
        relative_scores_before=before_scores,
        relative_scores_after=after_scores,
        after=after,
    )


@dataclass(frozen=True)
class ContactCouplingQuadraticIdentity:
    edge_vector: tuple[int, ...]
    edge_quadratic: int
    body_square_sum: int
    body_incidence_image: tuple[int, ...]


def contact_coupling_quadratic_identity(
    state: ContactNetworkMomentum1D,
    edge_vector: tuple[int, ...] | list[int],
) -> ContactCouplingQuadraticIdentity:
    """Verify x^T K x = sum_i D_i (Bx)_i^2 >= 0 exactly."""
    vector = tuple(edge_vector)
    if len(vector) != len(state.contacts):
        raise ValueError("edge vector must match contact count")
    for value in vector:
        _require_integer("edge_vector value", value)

    incidence = contact_incidence_matrix(state)
    gram = contact_coupling_gram(state)
    image = tuple(
        sum(incidence[body][edge] * vector[edge] for edge in range(len(vector)))
        for body in range(len(state.masses))
    )
    lhs = sum(
        vector[row] * gram[row][col] * vector[col]
        for row in range(len(vector))
        for col in range(len(vector))
    )
    rhs = sum(
        weight * value * value
        for weight, value in zip(state.body_scale_weights, image)
    )
    if lhs != rhs or lhs < 0:
        raise AssertionError("contact coupling Gram identity failed")
    return ContactCouplingQuadraticIdentity(
        edge_vector=vector,
        edge_quadratic=lhs,
        body_square_sum=rhs,
        body_incidence_image=image,
    )


def contact_graph_is_matching(state: ContactNetworkMomentum1D) -> bool:
    seen: set[int] = set()
    for contact in state.contacts:
        if contact.body_a in seen or contact.body_b in seen:
            return False
        seen.add(contact.body_a)
        seen.add(contact.body_b)
    return True


def contact_coupling_is_diagonal(state: ContactNetworkMomentum1D) -> bool:
    gram = contact_coupling_gram(state)
    return all(
        row == col or gram[row][col] == 0
        for row in range(len(gram))
        for col in range(len(gram))
    )


def verify_matching_independence_equivalence(state: ContactNetworkMomentum1D) -> bool:
    """For a simple contact graph, K is diagonal iff contacts share no body."""
    matching = contact_graph_is_matching(state)
    diagonal = contact_coupling_is_diagonal(state)
    if matching != diagonal:
        raise AssertionError("matching/diagonal contact-independence equivalence failed")
    return matching


def diagonal_only_nonclosing_impulse_guess(
    state: ContactNetworkMomentum1D,
) -> tuple[int, ...]:
    """Pretend each contact is isolated and ignore off-diagonal K coupling."""
    scores = contact_relative_scores(state)
    gram = contact_coupling_gram(state)
    guesses: list[int] = []
    for edge, score in enumerate(scores):
        diagonal = gram[edge][edge]
        if diagonal <= 0:
            raise AssertionError("contact self-coupling must be positive")
        guesses.append(0 if score >= 0 else _ceil_div_positive(-score, diagonal))
    return tuple(guesses)


def impulse_vector_makes_all_contacts_nonclosing(
    state: ContactNetworkMomentum1D,
    impulse_vector: tuple[int, ...] | list[int],
) -> bool:
    """Whether r+Kj is componentwise non-negative."""
    return all(
        score >= 0
        for score in apply_contact_impulse_vector(state, impulse_vector).relative_scores_after
    )
