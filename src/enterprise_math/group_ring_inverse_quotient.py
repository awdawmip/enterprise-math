"""Candidate BRC mass-only specialization: inversion-orbit collision readout.

For the abelian unit group modulo n, u and u**(-1) have equal total transition
mass into inversion orbits under 2[e]+[g]+[g**(-1)].  Aggregate ORBIT mass (not
per-member mass).  The identity is a singleton, so every prefix identity
coefficient is retained exactly.  This does not retain oriented atom labels,
unequal +/- weights, or arbitrary later observations.  No order is supplied to
the online algorithm, and no subgroup is enumerated before compression.

State-count savings do not imply the same RAM or time savings: each online key
stores both inverse residues.  A hard budget returns an explicit unfinished
status; it never means no factor or no collision.  No new top-level BRC family.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from types import SimpleNamespace

from .brc_control_mass import ControlMassQuotient

Orbit = tuple[int, int]


def _integer(name: str, value: int, lower: int) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f'{name} must be an integer >= {lower}')
    return value


def _orbit(u: int, inverse_u: int) -> Orbit:
    return (u, inverse_u) if u <= inverse_u else (inverse_u, u)


@dataclass(frozen=True)
class InverseCollisionResult:
    n: int
    a: int
    requested_m: int
    completed_m: int
    status: str
    collision_by_depth: tuple[int, ...]
    orbit_states_by_depth: tuple[int, ...]
    full_support_by_depth: tuple[int, ...]
    attempted_row_updates: int
    certified_order: int | None

    @property
    def collision_mass(self) -> int:
        """Exact at completed_m only, including when a later step hit a budget."""
        return self.collision_by_depth[-1]


def inverse_collision_mass(
    n: int, a: int, m: int | None = None, *, max_states: int = 100_000
) -> InverseCollisionResult:
    """Compute dyadic collision mass on inverse orbits with exact integers.

    Default Q=2**m >= n**2 is the sufficient order-rounding window inherited
    from POWER.  Smaller explicit m is a valid mass query, not a certified order
    query.  The retained pair (u,u^-1) makes all later updates inversion-free;
    only the initial inverse of a is computed.  Max_states caps each frontier,
    not bytes or the combined old/new frontier storage.
    """
    _integer('n', n, 3)
    _integer('a', a, 2)
    if a >= n or gcd(a, n) != 1:
        raise ValueError('a must be a unit with 1 < a < n')
    m = max(4, (n*n - 1).bit_length()) if m is None else _integer('m', m, 0)
    _integer('max_states', max_states, 1)
    counts: dict[Orbit, int] = {(1, 1): 1}
    g, gi = a, pow(a, -1, n)
    masses, sizes, support = [1], [1], [1]
    attempted = 0
    status = 'COMPLETE'
    for depth in range(m):
        # Exact fixed-suffix shortcut: every remaining multiplier is then 4[e].
        # Counts need not be rescaled/materialized because only readouts return.
        if g == 1:
            for _ in range(depth, m):
                masses.append(4*masses[-1])
                sizes.append(sizes[-1])
                support.append(support[-1])
            break
        nxt: dict[Orbit, int] = {}
        exhausted = False
        for key, mass in counts.items():
            attempted += 1
            u, ui = key
            if len(nxt) >= max_states and key not in nxt:
                exhausted = True
                break
            nxt[key] = nxt.get(key, 0) + 2*mass
            v, vi = u*g % n, ui*gi % n
            target = (v, vi) if v <= vi else (vi, v)
            if len(nxt) >= max_states and target not in nxt:
                exhausted = True
                break
            nxt[target] = nxt.get(target, 0) + mass
            v, vi = u*gi % n, ui*g % n
            target = (v, vi) if v <= vi else (vi, v)
            if len(nxt) >= max_states and target not in nxt:
                exhausted = True
                break
            nxt[target] = nxt.get(target, 0) + mass
        if exhausted:
            status = 'BUDGET_EXHAUSTED'
            break
        counts = nxt
        if sum(counts.values()) != 1 << (2*(depth+1)):
            raise ArithmeticError('positive branch mass was not preserved')
        masses.append(counts.get((1, 1), 0))
        sizes.append(len(counts))
        support.append(sum(1 if u == ui else 2 for u, ui in counts))
        g, gi = g*g % n, gi*gi % n
    completed = len(masses)-1
    order = None
    if status == 'COMPLETE' and (1 << m) >= n*n:
        q = 1 << m
        order = (2*q*q + masses[-1]) // (2*masses[-1])
        if pow(a, order, n) != 1:
            raise ArithmeticError('certified-window order roundtrip failed')
    return InverseCollisionResult(n, a, m, completed, status, tuple(masses),
                                  tuple(sizes), tuple(support), attempted, order)


@dataclass(frozen=True)
class _Mass:
    """Exact mass-only adapter for the existing ControlMassQuotient contract."""
    total_mass: int

    def forget_effects(self):
        return self


def certify_inverse_partition(
    n: int, units: tuple[int, ...], multiplier: int, *,
    positive_weight: int = 1, negative_weight: int = 1
) -> ControlMassQuotient:
    """Small finite diagnostic using the UNCHANGED BRC mass checker.

    This explicit finite certificate is not called by the online solver: matrix
    construction is deliberately separated from its algorithmic cost.  A
    multiplier-closed inversion-closed unit subset suffices.  Unequal +/- weights
    are allowed here to test rejection of an unsafe partition, not in the solver.
    Identity observation is checked independently of mass lumpability.
    """
    _integer('n', n, 3)
    _integer('multiplier', multiplier, 1)
    _integer('positive_weight', positive_weight, 0)
    _integer('negative_weight', negative_weight, 0)
    units = tuple(units)
    if not units or len(set(units)) != len(units) or 1 not in units:
        raise ValueError('distinct units including identity required')
    if any(type(u) is not int or not 1 <= u < n or gcd(u, n) != 1 for u in units):
        raise ValueError('invalid unit population')
    if multiplier >= n or gcd(multiplier, n) != 1:
        raise ValueError('multiplier must be a unit')
    indices = {u: i for i, u in enumerate(units)}
    gi = pow(multiplier, -1, n)
    labels, class_ids, blocks = [], {}, []
    for i, u in enumerate(units):
        ui = pow(u, -1, n)
        if ui not in indices:
            raise ValueError('population not closed under inversion')
        key = _orbit(u, ui)
        labels.append(class_ids.setdefault(key, len(class_ids)))
        for v, w in ((u, 2), (u*multiplier % n, positive_weight),
                     (u*gi % n, negative_weight)):
            if v not in indices:
                raise ValueError('population not closed under multiplier')
            blocks.append((i, indices[v], _Mass(w)))
    identity_label = labels[indices[1]]
    if sum(label == identity_label for label in labels) != 1:
        raise ArithmeticError('identity observer erased')
    packet = SimpleNamespace(state_count=len(units), blocks=tuple(blocks))
    return ControlMassQuotient.compile(packet, tuple(labels))


def cyclic_return_signatures(order: int) -> tuple[tuple[int, ...], ...]:
    """Exact diagnostics for repeated 2I+shift+inverse-shift, NOT order finding.

    Each row lists return mass from one cyclic position for t=0..floor(r/2).
    Different distances have different first-positive times; opposite positions
    have identical signatures.  Used to check the scoped minimality theorem.
    """
    _integer('order', order, 1)
    current = [int(i == 0) for i in range(order)]
    columns = [tuple(current)]
    for _ in range(order//2):
        current = [2*current[i]+current[(i-1) % order]+current[(i+1) % order]
                   for i in range(order)]
        columns.append(tuple(current))
    return tuple(tuple(col[i] for col in columns) for i in range(order))
