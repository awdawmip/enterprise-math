"""Exact constrained-graph carry closure and finite recurrent BRC composition.

Research candidate; native X6 linear observer only. Rational lattice bases are
not fractional Cell moves. A finite budget escape is not global unboundedness.
Existing HNF/path-column helpers and recurrent-mass resolvent are reused.
A graph certificate permits forward inclusions: bijectivity is forced only
within strongly connected components. Positive BRC weights remain separate.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from typing import Sequence
from sympy import Matrix as SM
from .brc_transport import Matrix, matrix, eye, inv, mm, mv, sm
from .brc_control_port import ControlPacket
from .brc_control_mass import control_mass_matrix
from .brc_weighted_recurrent import finite_recurrent_mass_analysis
from .heartbeat_switching_carry import _prime, _nat, _valuation, _minimum, linear_carry_spread
from .heartbeat_lattice_search import _integer_family, _hnf_basis, _reachable_basis, _same_local_lattice

N = 6
State = tuple[int, int]  # existing control port, determinant valuation mod 6

def _typed_state(value) -> bool:
    return (isinstance(value, tuple) and len(value) == 2
            and all(type(x) is int for x in value))

@dataclass(frozen=True)
class CarryEdge:
    source: int
    target: int
    action: Matrix

@dataclass(frozen=True)
class GraphColumn:
    axis: int
    word: tuple[int, ...]  # indices of actual input edges, in execution order
    vector: tuple[F, ...]
    source_state: State
    target_state: State

@dataclass(frozen=True)
class GraphCarryResult:
    status: str
    prime: int
    source_digest: str
    states: tuple[State, ...]
    depth_budget: int
    rounds: int
    bases: tuple[Matrix, ...]
    index_depth_history: tuple[tuple[int, ...], ...]
    spanning_columns: tuple[tuple[GraphColumn, ...], ...]
    escape: GraphColumn | None
    potentials: tuple[int, ...]
    # (lifted source index, lifted target index, original edge index, index defect)
    edge_defects: tuple[tuple[int, int, int, int], ...]
    all_path_spread_bound: int | None


def _graph(state_count: int, edges: Sequence[CarryEdge], prime: int):
    p = _prime(prime)
    if type(state_count) is not int or state_count < 1:
        raise ValueError('positive finite control state_count required')
    checked = []
    for e in edges:
        if not isinstance(e, CarryEdge):
            raise TypeError('CarryEdge required')
        if any(type(v) is not int or not 0 <= v < state_count for v in (e.source, e.target)):
            raise ValueError('edge outside control layout')
        checked.append(CarryEdge(e.source, e.target, matrix(e.action)))
    edges = tuple(checked)
    degrees = _integer_family([e.action for e in edges], p)[1] if edges else ()
    states = {(v, 0) for v in range(state_count)}
    while True:
        expanded = states | {(e.target, (h+d) % N) for v, h in states
                            for e, d in zip(edges, degrees) if e.source == v}
        if expanded == states:
            break
        states = expanded
    states = tuple(sorted(states))
    pos = {s: i for i, s in enumerate(states)}
    lifted = []
    for s, (v, h) in enumerate(states):
        for j, (e, d) in enumerate(zip(edges, degrees)):
            if e.source == v:
                k, hp = divmod(h+d, N)
                lifted.append((s, pos[(e.target, hp)], j, k, sm(F(p)**(-k), e.action)))
    digest = sha256(repr((state_count, edges, p)).encode()).hexdigest()
    return edges, degrees, states, tuple(lifted), digest


def _reachability(n, pairs):
    adjacent = [set() for _ in range(n)]
    for s, t in pairs:
        adjacent[s].add(t)
    reached = []
    for s in range(n):
        seen, todo = {s}, [s]
        while todo:
            for t in adjacent[todo.pop()]:
                if t not in seen:
                    seen.add(t); todo.append(t)
        reached.append(frozenset(seen))
    return tuple(reached)


def _summary(bases, states, lifted, p):
    inverses = tuple(inv(b) for b in bases)
    widths = tuple(linear_carry_spread(b, p) for b in bases)
    g = tuple(_valuation(F(SM(b).det()), p)-h for b, (_v, h) in zip(bases, states))
    defects = []
    for s, t, j, _k, b in lifted:
        m = mm(mm(inverses[t], b), bases[s])
        if _minimum(m, p) < 0:
            raise ValueError('normalized edge does not give a forward lattice inclusion')
        defect = _valuation(F(SM(m).det()), p)
        if defect != g[s]-g[t] or defect < 0:
            raise ArithmeticError('determinant potential identity failed')
        defects.append((s, t, j, defect))
    reached = _reachability(len(states), [(s, t) for s, t, *_ in lifted])
    bound = max(widths[s]+widths[t]+g[s]-g[t]
                for s, targets in enumerate(reached) for t in targets)
    return g, tuple(defects), bound


def graph_from_packet(packet: ControlPacket) -> tuple[CarryEdge, ...]:
    """Project only linear support; do NOT replace packet weights or offsets.

    Edge indices address the existing canonical block/atom order. Multiplicity
    provenance stays in the original packet, not in a module-span certificate.
    """
    if not isinstance(packet, ControlPacket):
        raise TypeError('ControlPacket required')
    return tuple(CarryEdge(s, t, a.a) for s, t, h in packet.blocks
                 for _w, a, count in h.entries if count)


def find_graph_lattices(state_count: int, edges: Sequence[CarryEdge], prime: int,
                        *, depth_budget: int, max_rounds: int | None = None) -> GraphCarryResult:
    """Least forward lattices for every legal path on a finite directed graph.

    Seed phase 0 at every original port, then retain all reachable lifted ports.
    At q<=6*state_count lifted ports, 6*q*R+1 rounds suffice for a radius-R
    decision. A caller's smaller limit yields only SEARCH_LIMIT. The basis
    search reuses existing exact HNF and six-actual-column selection unchanged.
    """
    p, budget = _prime(prime), _nat(depth_budget)
    edges, _degrees, states, lifted, digest = _graph(state_count, edges, p)
    q = len(states); decision_limit = N*q*budget+1
    limit = decision_limit if max_rounds is None else min(decision_limit, _nat(max_rounds))
    seeds = tuple(tuple(GraphColumn(i, (), tuple(F(j == i) for j in range(N)), s, s)
                        for i in range(N)) for s in states)
    bases, columns = (eye(N),)*q, seeds
    history = [(0,)*q]

    def result(status, rounds, escape=None):
        g, defects, bound = _summary(bases, states, lifted, p) if status == 'FIXED_LATTICES' else ((), (), None)
        return GraphCarryResult(status, p, digest, states, budget, rounds, bases,
                                tuple(history), columns, escape, g, defects, bound)

    for r in range(1, limit+1):
        candidates = [list(seed)+list(cols) for seed, cols in zip(seeds, columns)]
        for s, t, j, _k, b in lifted:
            for col in columns[s]:
                moved = GraphColumn(col.axis, col.word+(j,), mv(b, col.vector), col.source_state, states[t])
                if min(_valuation(v, p) for v in moved.vector if v) < -budget:
                    return result('ESCAPING_WORD', r, moved)
                candidates[t].append(moved)
        next_bases = tuple(_hnf_basis(c, p) for c in candidates)
        if any(_minimum(mm(inv(new), old), p) < 0 for old, new in zip(bases, next_bases)):
            raise ArithmeticError('closure lost predecessor')
        if all(_same_local_lattice(a, b, p) for a, b in zip(bases, next_bases)):
            answer = result('FIXED_LATTICES', r)
            verify_graph_result(state_count, edges, answer)
            return answer
        depths = tuple(-_valuation(F(SM(b).det()), p) for b in next_bases)
        if sum(depths) <= sum(history[-1]) or sum(depths) > N*q*budget:
            raise ArithmeticError('finite index bound violated')
        bases = next_bases
        columns = tuple(_reachable_basis(c, b, p) for c, b in zip(candidates, bases))
        history.append(depths)
    if limit == decision_limit:
        raise ArithmeticError('proved graph decision bound exceeded')
    return result('SEARCH_LIMIT', limit)


def replay_graph_word(state_count: int, edges: Sequence[CarryEdge], prime: int,
                      source_state: State, word: tuple[int, ...]):
    """Replay genuine legal input edges; return integer action, scale and end."""
    edges, degrees, states, _lifted, _digest = _graph(state_count, edges, prime)
    if not _typed_state(source_state) or source_state not in states:
        raise ValueError('unknown lifted source state')
    current = source_state; action = eye(N); scale = 0
    for j in word:
        if type(j) is not int or not 0 <= j < len(edges):
            raise ValueError('unknown actual edge')
        e = edges[j]
        if e.source != current[0]:
            raise ValueError('witness word violates a control port')
        k, h = divmod(current[1]+degrees[j], N)
        scale += k; current = (e.target, h); action = mm(e.action, action)
    return action, scale, current


def verify_graph_result(state_count: int, edges: Sequence[CarryEdge], result: GraphCarryResult) -> bool:
    """Terminal evidence check, independent of HNF or closure history replay.

    Validates returned forward inclusions or an actual legal escape, not
    minimality of the search transcript or global nonexistence of any lattice.
    """
    if not isinstance(result, GraphCarryResult):
        raise TypeError('GraphCarryResult required')
    p = _prime(result.prime); budget = _nat(result.depth_budget)
    edges, _degrees, states, lifted, digest = _graph(state_count, edges, p)
    if (result.source_digest != digest or result.states != states
            or any(not _typed_state(x) for x in result.states)):
        raise ValueError('graph/source binding mismatch')
    if _nat(result.rounds) > N*len(states)*budget+1:
        raise ValueError('round count exceeds decision budget')
    if result.status == 'ESCAPING_WORD':
        col = result.escape
        if (not isinstance(col, GraphColumn) or type(col.axis) is not int or not 0 <= col.axis < N
                or not col.word or len(col.word) > result.rounds):
            raise ValueError('invalid actual path column')
        a, k, target = replay_graph_word(state_count, edges, p, col.source_state, col.word)
        vector = tuple(F(p)**(-k)*a[i][col.axis] for i in range(N))
        if not _typed_state(col.target_state) or col.target_state != target or col.vector != vector:
            raise ValueError('path replay differs from witness')
        if min(_valuation(v, p) for v in vector if v) >= -budget:
            raise ValueError('witness is inside budget')
        if linear_carry_spread(a, p) <= budget:
            raise ArithmeticError('escape did not imply actual carry spread')
        if result.all_path_spread_bound is not None or result.potentials or result.edge_defects:
            raise ValueError('escape cannot claim a positive certificate')
        return True
    if result.status != 'FIXED_LATTICES' or result.escape is not None:
        raise ValueError('resource limit is not terminal mathematical evidence')
    if len(result.bases) != len(states):
        raise ValueError('one basis per lifted state required')
    bases = tuple(matrix(b) for b in result.bases)
    for b in bases:
        if len(b) != N or len(b[0]) != N or _minimum(b, p) < -budget or _minimum(inv(b), p) < 0:
            raise ValueError('invalid full-rank basis or standard-lattice sandwich')
    g, defects, bound = _summary(bases, states, lifted, p)
    if (any(type(v) is not int for v in result.potentials)
            or type(result.all_path_spread_bound) is not int
            or any(not isinstance(e, tuple) or len(e) != 4
                   or any(type(v) is not int for v in e) for e in result.edge_defects)
            or (result.potentials, result.edge_defects, result.all_path_spread_bound) != (g, defects, bound)):
        raise ValueError('incorrect defect potential or endpoint bound')
    return True


def graph_endpoint_bound(state_count, edges, result, source_state, target_state) -> int:
    verify_graph_result(state_count, edges, result)
    if result.status != 'FIXED_LATTICES':
        raise ValueError('fixed forward lattice certificate required')
    _e, _d, states, lifted, _sha = _graph(state_count, edges, result.prime)
    pos = {s: i for i, s in enumerate(states)}
    if (not _typed_state(source_state) or not _typed_state(target_state)
            or source_state not in pos or target_state not in pos):
        raise ValueError('unknown endpoint')
    s, t = pos[source_state], pos[target_state]
    if t not in _reachability(len(states), [(u, v) for u, v, *_ in lifted])[s]:
        raise ValueError('no admissible path between endpoints')
    return (linear_carry_spread(result.bases[s], result.prime)
            + linear_carry_spread(result.bases[t], result.prime)
            + result.potentials[s]-result.potentials[t])


@dataclass(frozen=True)
class BottomAbsorption:
    """Exact probabilities only; does not decide whether a class has bounded carry."""
    mass_matrix: tuple[tuple[F, ...], ...]
    bottom_components: tuple[tuple[int, ...], ...]
    transient_states: tuple[int, ...]
    absorption_probabilities: tuple[tuple[F, ...], ...]  # initial state x bottom class
    transient_star: tuple[tuple[F, ...], ...]


def bottom_component_absorption(packet: ControlPacket) -> BottomAbsorption:
    """Compose existing BRC mass projection and exact transient Neumann star.

    Requires a finite time-homogeneous row-stochastic packet. A geometric
    classification of each bottom class is a separate proof/certificate input.
    Unknown classes must not be relabeled bad because a finite search escaped.
    """
    if not isinstance(packet, ControlPacket):
        raise TypeError('ControlPacket required')
    w = control_mass_matrix(packet); n = len(w)
    if any(sum(row) != 1 for row in w):
        raise ValueError('exactly row-stochastic BRC mass required; no implicit normalization')
    pairs = [(i, j) for i in range(n) for j in range(n) if w[i][j] > 0]
    reach = _reachability(n, pairs)
    remaining = set(range(n)); components = []
    while remaining:
        i = min(remaining)
        comp = tuple(j for j in sorted(remaining) if j in reach[i] and i in reach[j])
        remaining.difference_update(comp); components.append(comp)
    bottom = tuple(c for c in components if all(t in c for s, t in pairs if s in c))
    recurrent = set(v for c in bottom for v in c)
    transient = tuple(i for i in range(n) if i not in recurrent)
    star = ()
    if transient:
        q = tuple(tuple(w[i][j] for j in transient) for i in transient)
        analysis = finite_recurrent_mass_analysis(q)
        if not analysis.stable or not analysis.verify_stable_certificate():
            raise ArithmeticError('finite transient support lacks the required exact star')
        star = analysis.star
    rows = []
    for i in range(n):
        if i in recurrent:
            rows.append(tuple(F(i in c) for c in bottom))
        else:
            a = transient.index(i)
            rows.append(tuple(sum((star[a][b]*sum(w[j][k] for k in c)
                                   for b, j in enumerate(transient)), F(0)) for c in bottom))
    answer = tuple(rows)
    if any(any(x < 0 for x in row) or sum(row) != 1 for row in answer):
        raise ArithmeticError('invalid absorption probabilities')
    if any(sum(w[i][j]*answer[j][k] for j in range(n)) != answer[i][k]
           for i in range(n) for k in range(len(bottom))):
        raise ArithmeticError('absorption harmonic identity failed')
    return BottomAbsorption(w, bottom, transient, answer, star)


@dataclass(frozen=True)
class CarryPeakTailBound:
    """Exponential-moment bound for a pathwise MAJORANT, not the exact peak law."""
    z: F
    threshold: int
    bottom_components: tuple[tuple[int, ...], ...]
    bottom_spread_bounds: tuple[int, ...]
    majorant_moments: tuple[F, ...]
    majorant_means: tuple[F, ...]
    peak_tail_upper_bounds: tuple[F, ...]
    weighted_transient_matrix: tuple[tuple[F, ...], ...]
    weighted_transient_star: tuple[tuple[F, ...], ...]


def carry_peak_tail_bound(packet: ControlPacket, prime: int,
                          bottom_certificates: Sequence[GraphCarryResult], *,
                          z: F | int, threshold: int) -> CarryPeakTailBound:
    """Certify P(sup_n kappa(P_n)>=threshold) using existing positive BRC star.

    Supply one FIXED_LATTICES certificate per bottom component in canonical
    absorption order. Each uses the original state_count and only that
    component's internal CarryEdges (all other ports are isolated). Their
    graph bindings/inclusions are actually verified; unchecked claimed bounds
    or radius escapes cannot substitute for a good-component proof.

    The majorant is the sum of individual linear spreads before bottom entry,
    plus the certified final-component bound. Its moment and mean are exact;
    its tail is only an upper bound for the real matrix-product peak. A large
    z can fail the moment certificate even when all sample peaks are finite.
    No state-dependent/history-dependent sampling is inferred from packet data.
    """
    p = _prime(prime); threshold = _nat(threshold)
    if type(z) not in (int, F) or z <= 1:
        raise ValueError('exact rational z>1 required; floats and booleans rejected')
    z = F(z)
    absorption = bottom_component_absorption(packet)
    edges = graph_from_packet(packet); n = packet.state_count
    _graph(n, edges, p)  # validate every action, including transient ones
    bottom = absorption.bottom_components
    if len(bottom_certificates) != len(bottom):
        raise ValueError('one verified certificate per bottom component required')
    bounds = []
    for component, certificate in zip(bottom, bottom_certificates):
        internal = tuple(e for e in edges if e.source in component and e.target in component)
        if not isinstance(certificate, GraphCarryResult) or certificate.prime != p:
            raise ValueError('bottom certificate has the wrong prime or type')
        verify_graph_result(n, internal, certificate)
        if certificate.status != 'FIXED_LATTICES':
            raise ValueError('a radius escape is not a good-component certificate')
        bounds.append(certificate.all_path_spread_bound)
    bounds = tuple(bounds)
    component_of = {v: k for k, c in enumerate(bottom) for v in c}
    transient = absorption.transient_states
    pos = {s: i for i, s in enumerate(transient)}
    qz = [[F(0) for _ in transient] for _ in transient]
    rz = [F(0) for _ in transient]
    reward = [F(0) for _ in transient]
    for s, t, histogram in packet.blocks:
        if s not in pos:
            continue
        i = pos[s]
        for weight, action, count in histogram.entries:
            probability = weight*count
            cost = linear_carry_spread(action.a, p)
            reward[i] += probability*cost
            if t in pos:
                qz[i][pos[t]] += probability*z**cost
            else:
                bound = bounds[component_of[t]]
                rz[i] += probability*z**(cost+bound)
                reward[i] += probability*bound
    qz = tuple(tuple(row) for row in qz)
    starz = ()
    if transient:
        analysis = finite_recurrent_mass_analysis(qz)
        if not analysis.stable or not analysis.verify_stable_certificate():
            raise ValueError('z too large for this majorant moment; not proof of unbounded peaks')
        starz = analysis.star
    moments, means = [], []
    for s in range(n):
        if s in component_of:
            b = bounds[component_of[s]]
            moments.append(z**b); means.append(F(b))
        else:
            i = pos[s]
            moments.append(sum((starz[i][j]*rz[j] for j in range(len(transient))), F(0)))
            means.append(sum((absorption.transient_star[i][j]*reward[j]
                              for j in range(len(transient))), F(0)))
    if any(m < 1 for m in moments) or any(m < 0 for m in means):
        raise ArithmeticError('invalid nonnegative cost majorant')
    tails = tuple(min(F(1), m/z**threshold) for m in moments)
    return CarryPeakTailBound(z, threshold, bottom, bounds, tuple(moments), tuple(means),
                             tails, qz, starz)
