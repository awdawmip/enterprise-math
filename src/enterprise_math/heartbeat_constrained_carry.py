"""Constrained X6 carry: forward lattice inclusions and exact monomial debt.

Research candidate, not Foundation. The graph is the DECLARED allowed finite
control language. Linear p-Smith spread is the only observer certified here.
Weights, multiplicities, translations and branch histories stay in ControlPacket;
none are reconstructed from these certificates. Pair/phase states are not axes.

The lattice search reuses the previous exact HNF/path-column implementation.
The monomial classifier is a max-plus Bellman-Ford specialization, not a new
shortest-path algorithm. All numerical decisions use integers/Fractions.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from typing import Sequence

from sympy import Matrix as SM
from .brc_transport import Matrix, matrix, eye, inv, mm, mv, sm
from .brc_control_port import ControlPacket
from .heartbeat_switching_carry import _nat, _prime, _valuation, _minimum, linear_carry_spread
from .heartbeat_lattice_search import _hnf_basis, _reachable_basis, _same_local_lattice

N = 6
PAIR_AXES = tuple((i, j) for i in range(N) for j in range(N) if i != j)
PAIR_ID = {pair: i for i, pair in enumerate(PAIR_AXES)}


@dataclass(frozen=True)
class LinearEdge:
    source: int
    target: int
    action: Matrix

    def __post_init__(self):
        object.__setattr__(self, 'action', matrix(self.action))
        a = self.action
        if len(a) != N or len(a[0]) != N:
            raise ValueError('exactly six spatial coordinates required')
        if any(x.denominator != 1 for row in a for x in row):
            raise ValueError('integer native actions required')
        if not SM(a).det():
            raise ValueError('nonsingular action required')


@dataclass(frozen=True)
class ControlGraph:
    state_count: int
    edges: tuple[LinearEdge, ...]
    packet_digest: str | None = None

    def __post_init__(self):
        if type(self.state_count) is not int or self.state_count < 1:
            raise ValueError('positive control-state count required')
        if type(self.edges) is not tuple or any(not isinstance(e, LinearEdge) for e in self.edges):
            raise TypeError('immutable LinearEdge tuple required')
        for e in self.edges:
            if any(type(v) is not int or not 0 <= v < self.state_count for v in (e.source, e.target)):
                raise ValueError('control endpoint outside declared graph')

    @property
    def digest(self):
        return sha256(repr(self).encode()).hexdigest()


def packet_control_graph(packet: ControlPacket) -> ControlGraph:
    """Extract a source-bound linear SUPPORT observer; never execute its quotient.

    Each positive histogram atom is retained as an indexed edge. Affine offsets,
    weights and multiplicities remain untouched in the original packet and are
    bound by packet_digest. Only integer affine effects are accepted.
    """
    if not isinstance(packet, ControlPacket):
        raise TypeError('ControlPacket required')
    edges = []
    for s, t, histogram in packet.blocks:
        for _weight, action, _count in histogram.entries:
            if any(x.denominator != 1 for x in action.b):
                raise ValueError('integer affine offset required')
            edges.append(LinearEdge(s, t, action.a))
    return ControlGraph(packet.state_count, tuple(edges), sha256(repr(packet).encode()).hexdigest())


def _phase_layout(graph, p):
    degrees = tuple(_valuation(F(SM(e.action).det()), p) for e in graph.edges)
    outgoing = [[] for _ in range(graph.state_count)]
    for i, e in enumerate(graph.edges):
        outgoing[e.source].append(i)
    seen = {(s, 0) for s in range(graph.state_count)}
    queue = deque(sorted(seen))
    while queue:
        s, h = queue.popleft()
        for i in outgoing[s]:
            node = (graph.edges[i].target, (h + degrees[i]) % N)
            if node not in seen:
                seen.add(node)
                queue.append(node)
    nodes = tuple(sorted(seen))
    pos = {node: i for i, node in enumerate(nodes)}
    lifted = []
    for u, (s, h) in enumerate(nodes):
        for i in outgoing[s]:
            k, target_h = divmod(h + degrees[i], N)
            v = pos[(graph.edges[i].target, target_h)]
            lifted.append((u, v, i, k, sm(F(p)**(-k), graph.edges[i].action)))
    return degrees, nodes, tuple(lifted)


def _reachable_pairs(size, edges):
    outgoing = [[] for _ in range(size)]
    for u, v, *_ in edges:
        outgoing[u].append(v)
    pairs = []
    for source in range(size):
        seen = {source}
        queue = deque([source])
        while queue:
            for target in outgoing[queue.popleft()]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        pairs.extend((source, target) for target in sorted(seen))
    return tuple(pairs)


@dataclass(frozen=True)
class GraphColumn:
    axis: int
    word: tuple[int, ...]
    vector: tuple[F, ...]
    source_node: tuple[int, int]
    target_node: tuple[int, int]


@dataclass(frozen=True)
class InclusionCertificate:
    prime: int
    source_digest: str
    nodes: tuple[tuple[int, int], ...]
    bases: tuple[Matrix, ...]
    basis_spreads: tuple[int, ...]
    volume_potential: tuple[int, ...]
    edge_slacks: tuple[tuple[int, int, int, int], ...]
    endpoint_bounds: tuple[tuple[int, int, int], ...]
    all_path_spread_bound: int


def certify_graph_inclusions(graph: ControlGraph, bases, prime: int) -> InclusionCertificate:
    """Check FORWARD inclusions; no all-edge inverse-integrality requirement.

    For e:s->t, U_e=S_t^-1 p^-k A_e S_s is p-integral and
    v_p(det U_e)=g_s-g_t>=0, where g_s=v_p(det S_s)-phase_s.
    Thus all cycle slacks vanish and all path slacks telescope. The endpoint
    spread bound is kappa(S_s)+kappa(S_t)+g_s-g_t.
    This verifier does not use HNF or replay closure history.
    """
    if not isinstance(graph, ControlGraph):
        raise TypeError('ControlGraph required')
    p = _prime(prime)
    _degrees, nodes, edges = _phase_layout(graph, p)
    bases = tuple(matrix(b) for b in bases)
    if len(bases) != len(nodes) or any(len(b) != N or len(b[0]) != N for b in bases):
        raise ValueError('one six-axis basis per lifted node required')
    inverses = tuple(inv(b) for b in bases)
    widths = tuple(linear_carry_spread(b, p) for b in bases)
    potential = tuple(_valuation(F(SM(b).det()), p)-h for b, (_s, h) in zip(bases, nodes))
    slacks = []
    for u, v, i, k, _b in edges:
        local = sm(F(p)**(-k), mm(mm(inverses[v], graph.edges[i].action), bases[u]))
        if _minimum(local, p) < 0:
            raise ValueError('normalized edge violates forward lattice inclusion')
        slack = _valuation(F(SM(local).det()), p)
        if slack != potential[u]-potential[v] or slack < 0:
            raise ArithmeticError('determinant potential identity failed')
        slacks.append((u, v, i, slack))
    bounds = tuple((u, v, widths[u]+widths[v]+potential[u]-potential[v])
                   for u, v in _reachable_pairs(len(nodes), edges))
    return InclusionCertificate(p, graph.digest, nodes, bases, widths, potential,
                                tuple(slacks), bounds, max(b for _u, _v, b in bounds))


@dataclass(frozen=True)
class GraphLatticeResult:
    status: str
    prime: int
    source_digest: str
    depth_budget: int
    nodes: tuple[tuple[int, int], ...]
    rounds: int
    bases: tuple[Matrix, ...]
    index_history: tuple[tuple[int, ...], ...]
    spanning_columns: tuple[tuple[GraphColumn, ...], ...]
    escape: GraphColumn | None
    certificate: InclusionCertificate | None


def find_graph_lattices(graph: ControlGraph, prime: int, *, depth_budget: int,
                        max_rounds: int | None = None) -> GraphLatticeResult:
    """General finite directed graphs, including sinks and one-way SCC edges.

    All original ports are allowed starts. At most 6*q*R+1 rounds decide the
    depth-R box, q<=6*state_count. Escape is a real LEGAL path and budget-only.
    Each lifted node keeps six actual path columns, not six arbitrary histories.
    """
    if not isinstance(graph, ControlGraph):
        raise TypeError('ControlGraph required')
    p, budget = _prime(prime), _nat(depth_budget)
    _degrees, nodes, edges = _phase_layout(graph, p)
    q = len(nodes)
    limit = N*q*budget+1
    if max_rounds is not None:
        limit = min(limit, _nat(max_rounds))
    seeds = tuple(tuple(GraphColumn(i, (), tuple(F(i == j) for j in range(N)), node, node)
                        for i in range(N)) for node in nodes)
    bases, columns = (eye(N),)*q, seeds
    history = [tuple(0 for _ in nodes)]

    def result(status, rounds, escape=None):
        cert = certify_graph_inclusions(graph, bases, p) if status == 'FIXED_LATTICES' else None
        return GraphLatticeResult(status, p, graph.digest, budget, nodes, rounds,
                                  bases, tuple(history), columns, escape, cert)

    for round_number in range(1, limit+1):
        candidates = [list(seed)+list(cols) for seed, cols in zip(seeds, columns)]
        for u, v, i, _k, b in edges:
            for col in columns[u]:
                moved = GraphColumn(col.axis, col.word+(i,), mv(b, col.vector), col.source_node, nodes[v])
                if min(_valuation(x, p) for x in moved.vector if x) < -budget:
                    return result('ESCAPING_PATH', round_number, moved)
                candidates[v].append(moved)
        next_bases = tuple(_hnf_basis(c, p) for c in candidates)
        if all(_same_local_lattice(old, new, p) for old, new in zip(bases, next_bases)):
            return result('FIXED_LATTICES', round_number)
        depths = tuple(-_valuation(F(SM(b).det()), p) for b in next_bases)
        if sum(depths) <= sum(history[-1]) or sum(depths) > N*q*budget:
            raise ArithmeticError('finite total lattice-index budget violated')
        for old, new in zip(bases, next_bases):
            if _minimum(mm(inv(new), old), p) < 0:
                raise ArithmeticError('closure lost previous lattice')
        bases = next_bases
        columns = tuple(_reachable_basis(c, b, p) for c, b in zip(candidates, bases))
        history.append(depths)
    if limit == N*q*budget+1:
        raise ArithmeticError('proved graph closure bound exceeded')
    return result('SEARCH_LIMIT', limit)


def replay_graph_word(graph: ControlGraph, source: int, word: Sequence[int]):
    """Reconstruct the original integer matrix and validate the full control path."""
    if type(source) is not int or not 0 <= source < graph.state_count:
        raise ValueError('invalid starting control')
    state, action = source, eye(N)
    for i in word:
        if type(i) is not int or not 0 <= i < len(graph.edges):
            raise ValueError('unknown edge index')
        e = graph.edges[i]
        if e.source != state:
            raise ValueError('illegal edge succession')
        state, action = e.target, mm(e.action, action)
    return state, action


def verify_graph_lattice_result(graph: ControlGraph, result: GraphLatticeResult) -> bool:
    if not isinstance(result, GraphLatticeResult):
        raise TypeError('GraphLatticeResult required')
    p, budget = _prime(result.prime), _nat(result.depth_budget)
    degrees, nodes, _edges = _phase_layout(graph, p)
    if graph.digest != result.source_digest or nodes != result.nodes:
        raise ValueError('graph or phase-layout source drift')
    _nat(result.rounds)
    if result.status == 'FIXED_LATTICES':
        if result.escape is not None:
            raise ValueError('fixed result carries an escape')
        for b in result.bases:
            if _minimum(b, p) < -budget or _minimum(inv(b), p) < 0:
                raise ValueError('basis not in standard-to-budget lattice box')
        if certify_graph_inclusions(graph, result.bases, p) != result.certificate:
            raise ValueError('inclusion certificate mismatch')
    elif result.status == 'ESCAPING_PATH':
        col = result.escape
        if col is None or not col.word or len(col.word) > result.rounds or col.source_node not in nodes:
            raise ValueError('missing or invalid escape path')
        if type(col.axis) is not int or not 0 <= col.axis < N:
            raise ValueError('invalid native source axis')
        target, a = replay_graph_word(graph, col.source_node[0], col.word)
        k, h = divmod(col.source_node[1]+sum(degrees[i] for i in col.word), N)
        vector = tuple(F(p)**(-k)*a[j][col.axis] for j in range(N))
        if col.target_node != (target, h) or vector != col.vector:
            raise ValueError('escape target or vector mismatch')
        if min(_valuation(x, p) for x in vector if x) >= -budget or linear_carry_spread(a, p) <= budget:
            raise ValueError('path does not witness the claimed budget escape')
        if result.certificate is not None:
            raise ValueError('escape carries a positive certificate')
    else:
        raise ValueError('SEARCH_LIMIT is not a terminal certificate')
    return True


def _monomial_data(graph, p):
    permutations, depths = [], []
    for edge in graph.edges:
        a = edge.action
        columns = [tuple(i for i in range(N) if a[i][j]) for j in range(N)]
        if any(len(c) != 1 for c in columns) or len({c[0] for c in columns}) != N:
            raise ValueError('exact classifier requires monomial actions, not general axis mixing')
        perm = tuple(c[0] for c in columns)
        permutations.append(perm)
        depths.append(tuple(_valuation(a[perm[i]][i], p) for i in range(N)))
    return tuple(permutations), tuple(depths)


def _initial_states(graph, initial_states):
    starts = tuple(range(graph.state_count)) if initial_states is None else tuple(initial_states)
    if not starts or any(type(s) is not int or not 0 <= s < graph.state_count for s in starts):
        raise ValueError('nonempty valid initial-control set required')
    return tuple(sorted(set(starts)))


def _pair_edges(graph, permutations, depths):
    out = []
    for k, edge in enumerate(graph.edges):
        perm, vals = permutations[k], depths[k]
        for a, (i, j) in enumerate(PAIR_AXES):
            u = 30*edge.source+a
            v = 30*edge.target+PAIR_ID[(perm[i], perm[j])]
            out.append((u, v, vals[i]-vals[j], k))
    return tuple(out)


@dataclass(frozen=True)
class PairPath:
    source: int
    source_axes: tuple[int, int]
    word: tuple[int, ...]
    target: int
    target_axes: tuple[int, int]
    debt: int


def _pair_walk(graph, permutations, depths, source, axes, word):
    if type(source) is not int or not 0 <= source < graph.state_count or axes not in PAIR_ID:
        raise ValueError('invalid pair-witness source')
    s, pair, cost = source, axes, 0
    trace = [(source, axes, 0)]
    for k in word:
        if type(k) is not int or not 0 <= k < len(graph.edges) or graph.edges[k].source != s:
            raise ValueError('illegal monomial witness path')
        i, j = pair
        cost += depths[k][i]-depths[k][j]
        pair = (permutations[k][i], permutations[k][j])
        s = graph.edges[k].target
        trace.append((s, pair, cost))
    return PairPath(source, axes, tuple(word), s, pair, cost), tuple(trace)


@dataclass(frozen=True)
class MonomialCarryResult:
    status: str
    prime: int
    source_digest: str
    initial_states: tuple[int, ...]
    pair_state_count: int
    rounds: int
    exact_spread_bound: int | None
    potentials: tuple[int | None, ...]
    attaining_path: PairPath | None
    cycle_prefix: PairPath | None
    positive_cycle: PairPath | None


def classify_monomial_carry(graph: ControlGraph, prime: int, *, initial_states=None) -> MonomialCarryResult:
    """Complete decision, with SHARP bound or repeatable positive-cycle witness.

    A monomial edge transports an ordered pair of axes and adds the difference
    of their p-depths. The finite graph has 30*state_count nodes and 30*edges
    edges. Bellman-Ford uses <=30*state_count rounds of integer relaxations.
    Trace copying and integer bit lengths are additional implementation costs.
    """
    if not isinstance(graph, ControlGraph):
        raise TypeError('ControlGraph required')
    p = _prime(prime)
    starts = _initial_states(graph, initial_states)
    permutations, depths = _monomial_data(graph, p)
    edges = _pair_edges(graph, permutations, depths)
    size = 30*graph.state_count
    values = [None]*size
    paths = [None]*size
    for s in starts:
        for a, pair in enumerate(PAIR_AXES):
            values[30*s+a] = 0
            paths[30*s+a] = (s, pair, ())
    for round_number in range(1, size+1):
        new_values, new_paths = list(values), list(paths)
        changed = []
        for u, v, debt, k in edges:
            if values[u] is None:
                continue
            candidate = values[u]+debt
            if new_values[v] is None or candidate > new_values[v]:
                s, pair, word = paths[u]
                new_values[v], new_paths[v] = candidate, (s, pair, word+(k,))
                changed.append(v)
        if not changed:
            best = max(v for v in values if v is not None)
            target = values.index(best)
            path, _ = _pair_walk(graph, permutations, depths, *paths[target])
            return MonomialCarryResult('BOUNDED_EXACT', p, graph.digest, starts, size,
                round_number, best, tuple(values), path, None, None)
        values, paths = new_values, new_paths
        if round_number == size:
            # The improved length-size walk has a positive repeated-node segment:
            # otherwise removing its cycles contradicts the previous DP optimum.
            source, axes, word = paths[changed[-1]]
            _path, trace = _pair_walk(graph, permutations, depths, source, axes, word)
            seen = {}
            for stop, (state, pair, weight) in enumerate(trace):
                key = (state, pair)
                if key in seen:
                    begin, minimum = seen[key]
                    if weight > minimum:
                        prefix, _ = _pair_walk(graph, permutations, depths, source, axes, word[:begin])
                        cycle, _ = _pair_walk(graph, permutations, depths, state, pair, word[begin:stop])
                        return MonomialCarryResult('UNBOUNDED_CYCLE', p, graph.digest, starts,
                            size, round_number, None, (), None, prefix, cycle)
                    if weight < minimum:
                        seen[key] = (stop, weight)
                else:
                    seen[key] = (stop, weight)
            raise ArithmeticError('Bellman-Ford improvement lacks positive cycle witness')
    raise ArithmeticError('unreachable classifier exit')


def verify_monomial_carry_result(graph: ControlGraph, result: MonomialCarryResult) -> bool:
    """Check finite potentials + attaining path, or legal prefix + positive cycle.

    No Bellman-Ford replay and no inference from a finite number of failed radii.
    The negative certificate implies spread(prefix cycle^n)>=prefix.debt+n*cycle.debt.
    """
    if not isinstance(result, MonomialCarryResult):
        raise TypeError('MonomialCarryResult required')
    p = _prime(result.prime)
    if graph.digest != result.source_digest or result.pair_state_count != 30*graph.state_count:
        raise ValueError('source graph or pair-layout mismatch')
    starts = _initial_states(graph, result.initial_states)
    if starts != result.initial_states:
        raise ValueError('initial states not canonical')
    permutations, depths = _monomial_data(graph, p)

    def recheck(path):
        if not isinstance(path, PairPath):
            raise ValueError('PairPath witness required')
        actual, _ = _pair_walk(graph, permutations, depths, path.source, path.source_axes, path.word)
        if actual != path:
            raise ValueError('pair-path witness mismatch')
        return actual

    if result.status == 'BOUNDED_EXACT':
        bound = _nat(result.exact_spread_bound)
        values = result.potentials
        if len(values) != result.pair_state_count or any(v is not None and type(v) is not int for v in values):
            raise ValueError('invalid integer-potential layout')
        for s in starts:
            if any(values[30*s+a] is None or values[30*s+a] < 0 for a in range(30)):
                raise ValueError('initial super-source potential omitted')
        for u, v, debt, _k in _pair_edges(graph, permutations, depths):
            if values[u] is not None and (values[v] is None or values[v] < values[u]+debt):
                raise ValueError('potential inequality fails')
        if max(v for v in values if v is not None) != bound:
            raise ValueError('bound does not match certified potential maximum')
        witness = recheck(result.attaining_path)
        if witness.source not in starts or witness.debt != bound:
            raise ValueError('bound has no attaining legal path')
        if result.cycle_prefix is not None or result.positive_cycle is not None:
            raise ValueError('bounded certificate has a divergent cycle')
    elif result.status == 'UNBOUNDED_CYCLE':
        prefix, cycle = recheck(result.cycle_prefix), recheck(result.positive_cycle)
        if prefix.source not in starts or (prefix.target, prefix.target_axes) != (cycle.source, cycle.source_axes):
            raise ValueError('cycle is not reachable from allowed initialization')
        if not cycle.word or (cycle.source, cycle.source_axes) != (cycle.target, cycle.target_axes) or cycle.debt <= 0:
            raise ValueError('cycle is not closed and positive in the axis-pair graph')
        if result.exact_spread_bound is not None or result.attaining_path is not None or result.potentials:
            raise ValueError('unbounded certificate carries a bounded result')
    else:
        raise ValueError('unknown monomial classification')
    return True
