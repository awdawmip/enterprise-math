"""Exact threshold reachability for BRC native-X6 linear carry peaks.

Keep oriented p-adic lattices modulo scalar homothety, not just Smith factors.
At fixed threshold R there are finitely many safe lattice states. Compile only
reachable ones, retain ControlPacket ports and original atom weights/counts,
and use the existing positive recurrent-mass star for first-passage mass.
A state budget returns a certified lower/upper interval, never false safety.

Observer: max-minus-min p-Smith depth at declared arrow boundaries. No affine
position, full time, scalar expansion, residual element, path-identity, physical
heat or semantic-memory claim. Input probabilities are fixed by the retained
control state; no independent resampling or normalization is silently added.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import lcm
from typing import Iterable

from sympy import Matrix as SM
from sympy.matrices.normalforms import hermite_normal_form
from .brc_transport import Matrix, matrix, eye, inv, mm, sm
from .brc_control_port import ControlPacket
from .brc_weighted_recurrent import finite_recurrent_mass_analysis
from .heartbeat_switching_carry import _nat, _prime, _minimum, _valuation, linear_carry_spread

N = 6
HIT = -1
UNKNOWN = -2
IntMatrix = tuple[tuple[int, ...], ...]


@lru_cache(maxsize=16384)
def _normal_form(a: Matrix, p: int) -> IntMatrix:
    inverse = inv(a)  # validates invertibility
    low = _minimum(a, p)
    width = -low - _minimum(inverse, p)
    if width < 0:
        raise ArithmeticError('negative Smith spread')
    c = sm(F(p)**(-low), a)
    denominator = lcm(*(v.denominator for row in c for v in row))
    if denominator % p == 0:
        raise ArithmeticError('normalized entries must be p-integral')
    # p^width Z_p^6 is contained in the normalized image. Adding it changes
    # no local lattice and removes every irrelevant prime from the Z-index.
    columns = SM(N, 2*N, lambda i, j:
                 int(denominator*c[i][j]) if j < N
                 else p**width * int(i == j-N))
    h = hermite_normal_form(columns)
    result = tuple(tuple(int(h[i, j]) for j in range(N)) for i in range(N))
    if _minimum(matrix(result), p) != 0 or linear_carry_spread(result, p) != width:
        raise ArithmeticError('projective HNF lost the local lattice')
    return result


def projective_lattice_key(basis, prime: int) -> IntMatrix:
    """Canonical oriented homothety class of basis Z_p^6, computed rationally.

    A rational basis is a lattice witness, NOT an allowed fractional Cell move.
    The canonical key is independent of the right GL_6(Z_p) basis and of scalars.
    """
    p = _prime(prime)
    a = matrix(basis)
    if len(a) != N or len(a[0]) != N:
        raise ValueError('exactly six native coordinates required')
    return _normal_form(a, p)


def _atoms(packet: ControlPacket):
    if not isinstance(packet, ControlPacket):
        raise TypeError('ControlPacket required')
    if packet.duration < 1:
        raise ValueError('one positive-duration monitored arrow is required')
    atoms, totals = [], [F(0)]*packet.state_count
    for source, target, histogram in packet.blocks:
        for weight, action, count in histogram.entries:
            if any(v.denominator != 1 for row in action.a for v in row):
                raise ValueError('integer native linear actions required')
            if any(v.denominator != 1 for v in action.b):
                raise ValueError('integer native affine offsets required')
            inv(action.a)
            totals[source] += weight*count
            atoms.append((source, target, weight, action.a, count))
    if any(total != 1 for total in totals):
        raise ValueError('exact row-stochastic mass required; no implicit normalization')
    return tuple(atoms)


@dataclass(frozen=True)
class PeakState:
    control: int
    lattice: IntMatrix


@dataclass(frozen=True)
class PeakEdge:
    source: int
    target: int  # HIT / UNKNOWN or a safe state index
    atom: int    # original canonical packet atom, preserving occurrence type
    weight: F
    multiplicity: int

    @property
    def mass(self) -> F:
        return self.weight*self.multiplicity


@dataclass(frozen=True)
class CarryPeakAutomaton:
    prime: int
    threshold: int
    packet_digest: str
    duration: int
    status: str
    states: tuple[PeakState, ...]
    edges: tuple[PeakEdge, ...]
    initial_hit: bool
    state_budget: int

    @property
    def complete(self) -> bool:
        return self.status == 'COMPLETE'


def compile_carry_peak(packet: ControlPacket, prime: int, threshold: int, *,
                       initial_control: int = 0, max_states: int = 10000) -> CarryPeakAutomaton:
    """Compile event sup_t kappa(P_t) >= threshold, starting from identity.

    COMPLETE preserves the exact infinite-time threshold event. STATE_LIMIT
    preserves known edges and routes every omitted safe successor to UNKNOWN;
    the probability interface returns an honest enclosure for the real event.
    Absolute time is external; duration counts fixed monitored arrow lengths.
    """
    p, r, cap = _prime(prime), _nat(threshold), _nat(max_states)
    if cap == 0:
        raise ValueError('positive state budget required')
    atoms = _atoms(packet)
    if type(initial_control) is not int or not 0 <= initial_control < packet.state_count:
        raise ValueError('initial control outside packet')
    digest = sha256(repr(packet).encode()).hexdigest()
    if r == 0:
        return CarryPeakAutomaton(p, r, digest, packet.duration, 'COMPLETE', (), (), True, cap)
    seed = PeakState(initial_control, projective_lattice_key(eye(N), p))
    states, positions, edges = [seed], {seed: 0}, []
    todo = deque([0])
    outgoing = [[] for _ in range(packet.state_count)]
    for j, atom in enumerate(atoms):
        outgoing[atom[0]].append((j, atom))
    partial = False
    # Transition cache includes orientation, never just the sorted Smith tuple.
    cache = {}
    while todo:
        source = todo.popleft()
        state = states[source]
        for j, (_s, target_control, weight, a, count) in outgoing[state.control]:
            key = (state.lattice, a)
            if key not in cache:
                moved = mm(a, matrix(state.lattice))
                cache[key] = (None if linear_carry_spread(moved, p) >= r
                              else projective_lattice_key(moved, p))
            lattice = cache[key]
            if lattice is None:
                target = HIT
            else:
                successor = PeakState(target_control, lattice)
                if successor in positions:
                    target = positions[successor]
                elif len(states) < cap:
                    target = len(states)
                    positions[successor] = target
                    states.append(successor)
                    todo.append(target)
                else:
                    target = UNKNOWN
                    partial = True
            edges.append(PeakEdge(source, target, j, weight, count))
    return CarryPeakAutomaton(p, r, digest, packet.duration,
                              'STATE_LIMIT' if partial else 'COMPLETE',
                              tuple(states), tuple(edges), False, cap)


def verify_peak_automaton(packet: ControlPacket, automaton: CarryPeakAutomaton) -> bool:
    """Recompute every local transition/canonical lattice and probability row.

    This validates the delivered automaton, not an independent formal proof.
    It does not silently repair a mismatched source, missing atom or wrong edge.
    """
    if not isinstance(automaton, CarryPeakAutomaton):
        raise TypeError('CarryPeakAutomaton required')
    if automaton.packet_digest != sha256(repr(packet).encode()).hexdigest():
        raise ValueError('packet digest mismatch')
    _prime(automaton.prime); _nat(automaton.threshold)
    if automaton.duration != packet.duration or automaton.status not in ('COMPLETE', 'STATE_LIMIT'):
        raise ValueError('invalid time or status')
    atoms = _atoms(packet)
    if automaton.initial_hit:
        if automaton.threshold != 0 or automaton.states or automaton.edges or not automaton.complete:
            raise ValueError('invalid initial-hit result')
        return True
    if not automaton.states or automaton.states[0].lattice != projective_lattice_key(eye(N), automaton.prime):
        raise ValueError('invalid identity start')
    if len(set(automaton.states)) != len(automaton.states):
        raise ValueError('duplicate safe states')
    by_source = [[] for _ in automaton.states]
    for edge in automaton.edges:
        if type(edge.source) is not int or not 0 <= edge.source < len(by_source):
            raise ValueError('edge outside automaton')
        by_source[edge.source].append(edge)
    partial = False
    for i, state in enumerate(automaton.states):
        if state.lattice != projective_lattice_key(state.lattice, automaton.prime):
            raise ValueError('noncanonical lattice')
        if linear_carry_spread(state.lattice, automaton.prime) >= automaton.threshold:
            raise ValueError('unsafe state stored as safe')
        expected = [j for j, atom in enumerate(atoms) if atom[0] == state.control]
        if sorted(e.atom for e in by_source[i]) != expected:
            raise ValueError('missing or duplicated original atom')
        for edge in by_source[i]:
            s, t, weight, a, count = atoms[edge.atom]
            if (weight, count) != (edge.weight, edge.multiplicity):
                raise ValueError('changed BRC weight or multiplicity')
            moved = mm(a, matrix(state.lattice))
            unsafe = linear_carry_spread(moved, automaton.prime) >= automaton.threshold
            if unsafe:
                if edge.target != HIT:
                    raise ValueError('unsafe successor not marked HIT')
            elif edge.target == UNKNOWN:
                partial = True
            else:
                if not 0 <= edge.target < len(automaton.states):
                    raise ValueError('safe successor index invalid')
                wanted = PeakState(t, projective_lattice_key(moved, automaton.prime))
                if automaton.states[edge.target] != wanted:
                    raise ValueError('oriented successor mismatch')
        if sum((e.mass for e in by_source[i]), F(0)) != 1:
            raise ValueError('probability row changed')
    if partial == automaton.complete:
        raise ValueError('incorrect completeness claim')
    return True


@dataclass(frozen=True)
class PeakProbability:
    status: str
    lower: F
    upper: F
    exact: F | None
    hit_weighted_first_time: F | None
    conditional_first_time: F | None
    useful_states: int
    recurrent_star_verified: bool


def _hitting(automaton: CarryPeakAutomaton, targets: frozenset[int], z: F = F(1)):
    # Remove states with no positive-support route to targets before inversion.
    # Otherwise safe recurrent classes would make I-Q singular unnecessarily.
    n = len(automaton.states)
    incoming = [[] for _ in range(n)]
    useful = set()
    for e in automaton.edges:
        if e.target in targets:
            useful.add(e.source)
        elif e.target >= 0:
            incoming[e.target].append(e.source)
    todo = list(useful)
    while todo:
        for s in incoming[todo.pop()]:
            if s not in useful:
                useful.add(s); todo.append(s)
    keep = tuple(sorted(useful)); index = {s: i for i, s in enumerate(keep)}
    if not keep:
        return (F(0),)*n, (F(0),)*n, 0, True
    q, b = [[F(0)]*len(keep) for _ in keep], [F(0)]*len(keep)
    for edge in automaton.edges:
        if edge.source not in index:
            continue
        i = index[edge.source]
        if edge.target in targets:
            b[i] += edge.mass
        elif edge.target in index:
            q[i][index[edge.target]] += edge.mass
    analysis = finite_recurrent_mass_analysis(tuple(tuple(z*x for x in row) for row in q))
    if not analysis.stable or not analysis.verify_stable_certificate():
        raise ValueError('requested first-passage exponential moment not certified finite')
    star = analysis.star
    h = tuple(sum((star[i][j]*z*b[j] for j in range(len(keep))), F(0)) for i in range(len(keep)))
    # At z=1, (I-Q)^-1 h = E[T; hit]. No claim for missing paths in partial graph.
    m = tuple(sum((star[i][j]*h[j] for j in range(len(keep))), F(0)) for i in range(len(keep)))
    hf, mf = [F(0)]*n, [F(0)]*n
    for s, i in index.items():
        hf[s], mf[s] = h[i], m[i]
    return tuple(hf), tuple(mf), len(keep), True


def peak_probability(packet: ControlPacket, automaton: CarryPeakAutomaton) -> PeakProbability:
    """Exact ever-crossing probability or rigorous state-budget interval."""
    verify_peak_automaton(packet, automaton)
    if automaton.initial_hit:
        return PeakProbability('EXACT', F(1), F(1), F(1), F(0), F(0), 0, True)
    h, m, useful, valid = _hitting(automaton, frozenset((HIT,)))
    low = h[0]
    if automaton.complete:
        return PeakProbability('EXACT', low, low, low, m[0], m[0]/low if low else None, useful, valid)
    upper, _, _, valid2 = _hitting(automaton, frozenset((HIT, UNKNOWN)))
    if not 0 <= low <= upper[0] <= 1:
        raise ArithmeticError('invalid first-passage enclosure')
    return PeakProbability('STATE_LIMIT_INTERVAL', low, upper[0], None, None, None, useful, valid and valid2)


def first_hit_generating_value(packet: ControlPacket, automaton: CarryPeakAutomaton, z) -> F:
    """E[z^T ; ever hit], T in monitored arrows. Reject incomplete automata.

    This is a first-hit statistic, not a sum of all visits. For z>1 an exact
    positive-star check is required; failure is not evidence of unbounded peaks.
    """
    verify_peak_automaton(packet, automaton)
    if not automaton.complete:
        raise ValueError('complete automaton required for exact generating value')
    if isinstance(z, bool) or not isinstance(z, (int, F)) or z < 0:
        raise ValueError('nonnegative exact rational z required')
    if automaton.initial_hit:
        return F(1)
    return _hitting(automaton, frozenset((HIT,)), F(z))[0][0]


def first_passage_prefix(packet: ControlPacket, automaton: CarryPeakAutomaton, steps: int):
    """Exact finite first-hit masses and unresolved/surviving probability mass."""
    verify_peak_automaton(packet, automaton)
    steps = _nat(steps)
    if automaton.initial_hit:
        return {'hit_by_step': (F(1),)+(F(0),)*steps, 'unknown_mass': F(0), 'surviving_mass': F(0)}
    alive = {0: F(1)}; hits = [F(0)]; unknown = F(0)
    outgoing = [[] for _ in automaton.states]
    for edge in automaton.edges:
        outgoing[edge.source].append(edge)
    for _ in range(steps):
        fresh, hit = {}, F(0)
        for i, mass in alive.items():
            for edge in outgoing[i]:
                amount = mass*edge.mass
                if edge.target == HIT:
                    hit += amount
                elif edge.target == UNKNOWN:
                    unknown += amount
                else:
                    fresh[edge.target] = fresh.get(edge.target, F(0))+amount
        hits.append(hit); alive = fresh
    survival = sum(alive.values(), F(0))
    if sum(hits) + unknown + survival != 1:
        raise ArithmeticError('first-passage mass was duplicated or lost')
    return {'hit_by_step': tuple(hits), 'unknown_mass': unknown, 'surviving_mass': survival}


def killed_symmetric_debt_tail(continuation, threshold: int) -> F:
    """Closed form 1/T_R(1/c) for killed fair U/V debt, starting at zero.

    Each monitored step stops with probability 1-c, or moves +/-1 with c/2.
    No general heartbeat program is inferred from this diagnostic subfamily.
    """
    if isinstance(continuation, bool) or not isinstance(continuation, (int, F)):
        raise ValueError('exact continuation probability required')
    c, r = F(continuation), _nat(threshold)
    if not 0 <= c <= 1:
        raise ValueError('continuation probability outside [0,1]')
    if r == 0:
        return F(1)
    if c == 0:
        return F(0)
    before, now, x = F(1), 1/c, 1/c
    for _ in range(1, r):
        before, now = now, 2*x*now-before
    return 1/now


@dataclass(frozen=True)
class PeakRiskSelection:
    status: str
    threshold: int | None
    risk_limit: F
    certified_minimal_in_range: bool
    checked_intervals: tuple[tuple[int, F, F], ...]


def select_peak_threshold(packet: ControlPacket, prime: int, risk_limit, *,
                          max_threshold: int, max_states: int = 10000) -> PeakRiskSelection:
    """Find a certified risk threshold in the explicit positive-integer range.

    A state-budget interval never becomes a false minimum certificate. If a
    smaller threshold remains ambiguous, return admissibility without minimality.
    Failure to find one inside this finite search range proves no global no-go.
    """
    if isinstance(risk_limit, bool) or not isinstance(risk_limit, (int, F)) or not 0 <= risk_limit <= 1:
        raise ValueError('exact rational risk limit in [0,1] required')
    maximum = _nat(max_threshold)
    if maximum < 1:
        raise ValueError('positive maximum threshold required')
    risk = F(risk_limit); rows=[]; smaller_excluded=True
    for threshold in range(1, maximum+1):
        automaton = compile_carry_peak(packet, prime, threshold, max_states=max_states)
        probability = peak_probability(packet, automaton)
        rows.append((threshold, probability.lower, probability.upper))
        if probability.upper <= risk:
            return PeakRiskSelection('CERTIFIED_MINIMUM' if smaller_excluded else 'CERTIFIED_ADMISSIBLE_MINIMALITY_UNRESOLVED',
                                     threshold, risk, smaller_excluded, tuple(rows))
        if probability.lower <= risk:
            smaller_excluded=False
    return PeakRiskSelection('NO_CERTIFICATE_WITHIN_RANGE', None, risk, False, tuple(rows))
