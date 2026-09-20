"""Exact bounded-depth common-lattice search for Heartbeat World's native X6.

Research candidate. Actions are nonsingular integer 6x6 matrices. The direct
finder requires integral mean determinant depth; the phase finder removes
that restriction with at most six determinant-residue ports. Both construct
least invariant Z_p over-lattices containing the standard lattice.
It never replaces BRC probabilities or paths by the module-span observer.

SymPy's exact integer Hermite normal form provides the basis operation;
existing BRC Fraction arithmetic, carry-spread and lattice certificates are
reused. Rational lattice vectors are algebraic witnesses, not fractional
native Cell moves. A depth-budget escape is NOT a proof of unboundedness.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from math import lcm
from typing import Sequence

from sympy import Matrix as SM
from sympy.matrices.normalforms import hermite_normal_form

from .brc_transport import Matrix, matrix, eye, inv, mm, mv, sm
from .brc_control_port import ControlPacket
from .heartbeat_switching_carry import (
    _nat, _prime, _valuation, _minimum, linear_carry_spread,
    certify_lattice_ports, LatticePortCertificate,
)

N = 6


def _integer_family(actions, p):
    p = _prime(p)
    actions = tuple(matrix(a) for a in actions)
    if not actions:
        raise ValueError('a nonempty action family is required')
    degrees = []
    for a in actions:
        if len(a) != N or len(a[0]) != N:
            raise ValueError('exactly six native axes required')
        if any(v.denominator != 1 for row in a for v in row):
            raise ValueError('integer native linear actions required')
        det = int(SM(a).det())
        if not det:
            raise ValueError('nonsingular actions required')
        degree = _valuation(det, p)
        degrees.append(degree)
    return actions, tuple(degrees)


def _integer_actions(actions, p):
    actions, degrees = _integer_family(actions, p)
    if any(d % N for d in degrees):
        raise ValueError('fractional mean depth: use find_phase_lattice')
    return actions, tuple(d // N for d in degrees)


def _digest(actions, p):
    return sha256(repr((actions, p)).encode('utf-8')).hexdigest()


def _radius(a, p):
    return max(0, -_minimum(a, p))


@dataclass(frozen=True)
class ReachableColumn:
    """An actual normalized action word applied to one native unit vector."""
    axis: int
    word: tuple[int, ...]
    vector: tuple[F, ...]
    source_phase: int = 0
    target_phase: int = 0


@dataclass(frozen=True)
class ClosureStage:
    round: int
    basis: Matrix
    radius: int
    index_depth: int


@dataclass(frozen=True)
class LatticeSearchResult:
    status: str
    prime: int
    source_digest: str
    scales: tuple[int, ...]
    depth_budget: int
    rounds: int
    basis: Matrix
    history: tuple[ClosureStage, ...]
    spanning_columns: tuple[ReachableColumn, ...]
    escape: ReachableColumn | None
    all_word_spread_bound: int | None


def reachable_column_action(actions, prime, column: ReachableColumn) -> Matrix:
    """Reconstruct the actual INTEGER action, never its normalized surrogate."""
    actions, _ = _integer_family(actions, prime)
    if type(column.axis) is not int or not 0 <= column.axis < N:
        raise ValueError('native axis index outside range')
    out = eye(N)
    for index in column.word:
        if type(index) is not int or not 0 <= index < len(actions):
            raise ValueError('unknown action in witness word')
        out = mm(actions[index], out)
    return out


def _same_local_lattice(a, b, p):
    return _minimum(mm(inv(a), b), p) >= 0 and _minimum(mm(inv(b), a), p) >= 0


def _hnf_basis(columns: Sequence[ReachableColumn], p: int) -> Matrix:
    # Identity is among the inputs, and denominators are powers of p.
    # Thus the integer over-lattice has p-power index, and its localization
    # is exactly the intended Z_p lattice (not an unrelated real lattice).
    denominator = 1
    for col in columns:
        for value in col.vector:
            denominator = lcm(denominator, value.denominator)
    q = denominator
    while q % p == 0:
        q //= p
    if q != 1:
        raise ArithmeticError('unexpected non-p denominator in reachable generators')
    values = SM(N, len(columns), lambda i, j: int(columns[j].vector[i]*denominator))
    h = hermite_normal_form(values)
    if h.shape != (N, N):
        raise ArithmeticError('identity-seeded lattice lost full rank')
    return matrix(tuple(tuple(F(int(h[i, j]), denominator) for j in range(N)) for i in range(N)))


def _reachable_basis(columns, basis, p):
    """Keep six actual path-columns via independence modulo p (Nakayama).

    HNF basis vectors themselves can be combinations of many paths. Keeping
    actual columns here is what permits an escaping WORD, rather than a
    merely formal linear combination, to be returned later.
    """
    inverse = inv(basis)
    echelon = {}
    selected = []
    for col in columns:
        coeff = mv(inverse, col.vector)
        if any(v and _valuation(v, p) < 0 for v in coeff):
            raise ArithmeticError('generated column outside computed lattice')
        row = [(v.numerator % p) * pow(v.denominator % p, -1, p) % p for v in coeff]
        for pivot in sorted(echelon):
            multiple = row[pivot]
            if multiple:
                row = [(a-multiple*b) % p for a, b in zip(row, echelon[pivot])]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is not None:
            inverse_pivot = pow(row[pivot], -1, p)
            echelon[pivot] = [(v*inverse_pivot) % p for v in row]
            selected.append(col)
            if len(selected) == N:
                return tuple(selected)
    raise ArithmeticError('could not select a reachable local basis')


def find_common_lattice(actions, prime: int, *, depth_budget: int,
                        max_rounds: int | None = None) -> LatticeSearchResult:
    """Return FIXED_LATTICE, ESCAPING_WORD, or a genuine SEARCH_LIMIT.

    With no smaller resource cap, at most 6*depth_budget+1 closure rounds
    decide whether the least invariant over-lattice lies in p^-R Z_p^6.
    An escaping word refutes this depth budget, not all larger budgets.
    On success the returned endpoint certificate bounds all-word spread.
    """
    p = _prime(prime)
    budget = _nat(depth_budget)
    actions, scales = _integer_actions(actions, p)
    limit = N*budget+1
    if max_rounds is not None:
        limit = min(limit, _nat(max_rounds))
    normalized = tuple(sm(F(p)**(-k), a) for a, k in zip(actions, scales))
    digest = _digest(actions, p)
    seeds = tuple(ReachableColumn(i, (), tuple(F(j == i) for j in range(N))) for i in range(N))
    basis = eye(N)
    columns = seeds
    history = [ClosureStage(0, basis, 0, 0)]

    def result(status, rounds, escape=None):
        bound = 2*linear_carry_spread(basis, p) if status == 'FIXED_LATTICE' else None
        return LatticeSearchResult(status, p, digest, scales, budget, rounds,
                                   basis, tuple(history), columns, escape, bound)

    for round_number in range(1, limit+1):
        candidates = list(seeds)+list(columns)
        for index, b in enumerate(normalized):
            for col in columns:
                moved = ReachableColumn(col.axis, col.word+(index,), mv(b, col.vector))
                if min(_valuation(v, p) for v in moved.vector if v) < -budget:
                    return result('ESCAPING_WORD', round_number, moved)
                candidates.append(moved)
        next_basis = _hnf_basis(candidates, p)
        if _minimum(mm(inv(next_basis), basis), p) < 0:
            raise ArithmeticError('closure must include its predecessor')
        if _same_local_lattice(basis, next_basis, p):
            return result('FIXED_LATTICE', round_number)
        depth = -_valuation(F(SM(next_basis).det()), p)
        if depth <= history[-1].index_depth or depth > N*budget:
            raise ArithmeticError('finite index-depth argument violated')
        basis = next_basis
        columns = _reachable_basis(candidates, basis, p)
        history.append(ClosureStage(round_number, basis, _radius(basis, p), depth))
    if limit == N*budget+1:
        raise ArithmeticError('proved finite decision bound exceeded')
    return result('SEARCH_LIMIT', limit)


def verify_lattice_search_result(actions, result: LatticeSearchResult) -> bool:
    """Recheck terminal positive/negative evidence without replaying the search.

    This checks witness validity, not the claimed minimality of the search
    history. Minimality follows from the proved closure construction.
    """
    if not isinstance(result, LatticeSearchResult):
        raise TypeError('LatticeSearchResult required')
    p = _prime(result.prime)
    actions, scales = _integer_actions(actions, p)
    if _digest(actions, p) != result.source_digest or scales != result.scales:
        raise ValueError('action/source binding mismatch')
    _nat(result.depth_budget)
    basis = matrix(result.basis)
    if len(basis) != N or len(basis[0]) != N:
        raise ValueError('six-axis basis required')
    if result.status == 'FIXED_LATTICE':
        if result.escape is not None or _radius(basis, p) > result.depth_budget:
            raise ValueError('invalid fixed-lattice radius or escape')
        inverse = inv(basis)
        if _minimum(inverse, p) < 0:
            raise ValueError('basis does not contain standard lattice')
        for a, k in zip(actions, scales):
            b = sm(F(p)**(-k), mm(mm(inverse, a), basis))
            if _minimum(b, p) < 0 or _minimum(inv(b), p) < 0:
                raise ValueError('normalized action does not preserve returned lattice')
        if result.all_word_spread_bound != 2*linear_carry_spread(basis, p):
            raise ValueError('incorrect endpoint bound')
    elif result.status == 'ESCAPING_WORD':
        col = result.escape
        if col is None or not col.word or len(col.word) > result.rounds:
            raise ValueError('missing or overlong witness')
        a = reachable_column_action(actions, p, col)
        k = sum(scales[i] for i in col.word)
        v = tuple(F(p)**(-k)*a[i][col.axis] for i in range(N))
        if v != col.vector or min(_valuation(z, p) for z in v if z) >= -result.depth_budget:
            raise ValueError('word does not escape declared budget')
        if linear_carry_spread(a, p) <= result.depth_budget:
            raise ArithmeticError('unit-determinant normalization failed to imply spread witness')
    else:
        raise ValueError('resource-limited output is not a terminal certificate')
    return True


def bind_single_port_packet(packet: ControlPacket, result: LatticeSearchResult) -> LatticePortCertificate:
    """Apply a found common basis to the ACTUAL BRC packet with weights intact.

    The existing certificate uses one scale per block; mixed mean scales in
    one block therefore require a separate port refinement, not averaging.
    """
    if not isinstance(packet, ControlPacket) or packet.state_count != 1:
        raise ValueError('one-control-port packet required for this adapter')
    atoms = tuple(atom for source, target, h in packet.blocks for atom in h.entries)
    actions = tuple(action.a for _weight, action, _count in atoms)
    verify_lattice_search_result(actions, result)
    if result.status != 'FIXED_LATTICE' or len(set(result.scales)) != 1:
        raise ValueError('fixed lattice and one common block scale required')
    return certify_lattice_ports(packet, (result.basis,), result.prime, {(0, 0): result.scales[0]})


@dataclass(frozen=True)
class PhaseLatticeSearchResult:
    status: str
    prime: int
    source_digest: str
    degrees: tuple[int, ...]
    phases: tuple[int, ...]
    depth_budget: int
    rounds: int
    bases: tuple[Matrix, ...]
    history: tuple[tuple[ClosureStage, ...], ...]
    spanning_columns: tuple[tuple[ReachableColumn, ...], ...]
    escape: ReachableColumn | None
    all_word_spread_bound: int | None


def _determinant_phases(degrees):
    phases = {0}
    while True:
        expanded = phases | {(h+d) % N for h in phases for d in degrees}
        if expanded == phases:
            return tuple(sorted(phases))
        phases = expanded


def find_phase_lattice(actions, prime: int, *, depth_budget: int,
                       max_rounds: int | None = None) -> PhaseLatticeSearchResult:
    """Remove fractional mean-depth obstruction with at most six clock ports.

    Port h is cumulative determinant valuation mod 6, not an extra spatial
    coordinate or the full time. Edge j takes h to (h+d_j)%6 and uses integer
    scale k=(h+d_j)//6. Every input action is available at every clock port.
    This graph is strongly connected, so stable forward inclusions are
    automatically lattice bijections after normalization.

    A depth-R decision requires at most 6*len(phases)*R+1 closure rounds.
    The path returned on escape is a real product of the original actions.
    A smaller explicit max_rounds may instead yield SEARCH_LIMIT.
    """
    p = _prime(prime)
    budget = _nat(depth_budget)
    actions, degrees = _integer_family(actions, p)
    phases = _determinant_phases(degrees)
    position = {h: i for i, h in enumerate(phases)}
    q = len(phases)
    limit = N*q*budget+1
    if max_rounds is not None:
        limit = min(limit, _nat(max_rounds))
    edges = []
    for h in phases:
        for j, (a, d) in enumerate(zip(actions, degrees)):
            k, target = divmod(h+d, N)
            edges.append((h, target, j, sm(F(p)**(-k), a)))
    seeds = tuple(tuple(ReachableColumn(i, (), tuple(F(j == i) for j in range(N)), h, h)
                        for i in range(N)) for h in phases)
    bases = (eye(N),)*q
    columns = seeds
    history = [tuple(ClosureStage(0, a, 0, 0) for a in bases)]
    digest = _digest(actions, p)

    def result(status, rounds, escape=None):
        bound = 2*max(linear_carry_spread(s, p) for s in bases) if status == 'FIXED_LATTICE' else None
        return PhaseLatticeSearchResult(status, p, digest, degrees, phases, budget,
            rounds, bases, tuple(history), columns, escape, bound)

    for round_number in range(1, limit+1):
        candidates = [list(seed)+list(cols) for seed, cols in zip(seeds, columns)]
        for source, target, j, b in edges:
            for col in columns[position[source]]:
                moved = ReachableColumn(col.axis, col.word+(j,), mv(b, col.vector),
                                        col.source_phase, target)
                if min(_valuation(v, p) for v in moved.vector if v) < -budget:
                    return result('ESCAPING_WORD', round_number, moved)
                candidates[position[target]].append(moved)
        next_bases = tuple(_hnf_basis(c, p) for c in candidates)
        for old, new in zip(bases, next_bases):
            if _minimum(mm(inv(new), old), p) < 0:
                raise ArithmeticError('port closure lost predecessor')
        if all(_same_local_lattice(a, b, p) for a, b in zip(bases, next_bases)):
            answer = result('FIXED_LATTICE', round_number)
            verify_phase_lattice_result(actions, answer)
            return answer
        depths = tuple(-_valuation(F(SM(b).det()), p) for b in next_bases)
        if sum(depths) <= sum(s.index_depth for s in history[-1]) or sum(depths) > N*q*budget:
            raise ArithmeticError('finite multiport index bound violated')
        bases = next_bases
        columns = tuple(_reachable_basis(c, b, p) for c, b in zip(candidates, bases))
        history.append(tuple(ClosureStage(round_number, b, _radius(b, p), d)
                             for b, d in zip(bases, depths)))
    if limit == N*q*budget+1:
        raise ArithmeticError('proved phase-lattice decision bound exceeded')
    return result('SEARCH_LIMIT', limit)


def verify_phase_lattice_result(actions, result: PhaseLatticeSearchResult) -> bool:
    """Terminal certificate recheck independent of HNF and search history."""
    if not isinstance(result, PhaseLatticeSearchResult):
        raise TypeError('PhaseLatticeSearchResult required')
    p = _prime(result.prime)
    actions, degrees = _integer_family(actions, p)
    if _digest(actions, p) != result.source_digest or degrees != result.degrees:
        raise ValueError('action/source binding mismatch')
    phases = _determinant_phases(degrees)
    if result.phases != phases or len(result.bases) != len(phases):
        raise ValueError('determinant clock mismatch')
    _nat(result.depth_budget)
    if result.status == 'ESCAPING_WORD':
        col = result.escape
        if col is None or not col.word or len(col.word) > result.rounds or col.source_phase not in phases:
            raise ValueError('invalid escaping witness')
        a = reachable_column_action(actions, p, col)
        degree = sum(degrees[j] for j in col.word)
        k, target = divmod(col.source_phase+degree, N)
        v = tuple(F(p)**(-k)*a[i][col.axis] for i in range(N))
        if target != col.target_phase or v != col.vector:
            raise ValueError('witness phase or vector mismatch')
        if min(_valuation(z, p) for z in v if z) >= -result.depth_budget:
            raise ValueError('word does not escape')
        if linear_carry_spread(a, p) <= result.depth_budget:
            raise ArithmeticError('phase determinant bound did not imply spread escape')
        return True
    if result.status != 'FIXED_LATTICE' or result.escape is not None:
        raise ValueError('resource-limited output is not a terminal certificate')
    bases = {h: matrix(b) for h, b in zip(phases, result.bases)}
    for b in bases.values():
        if len(b) != N or len(b[0]) != N or _radius(b, p) > result.depth_budget:
            raise ValueError('invalid basis or radius')
        if _minimum(inv(b), p) < 0:
            raise ValueError('basis must contain standard lattice')
    for h in phases:
        for a, d in zip(actions, degrees):
            k, target = divmod(h+d, N)
            b = sm(F(p)**(-k), mm(mm(inv(bases[target]), a), bases[h]))
            if _minimum(b, p) < 0 or _minimum(inv(b), p) < 0:
                raise ValueError('edge does not preserve returned lattice ports')
    if result.all_word_spread_bound != 2*max(linear_carry_spread(b, p) for b in bases.values()):
        raise ValueError('incorrect all-word bound')
    return True


def phase_edge_certificates(actions, result: PhaseLatticeSearchResult) -> tuple[LatticePortCertificate, ...]:
    """Run the existing BRC lattice verifier on every clock-lifted edge.

    Each edge is certified separately with the SAME bases, preserving the
    old one-scale-per-block interface. This is a linear-law adapter, not an
    assignment of random branch probabilities to an input action family.
    """
    from .brc_transport import Affine
    verify_phase_lattice_result(actions, result)
    if result.status != 'FIXED_LATTICE':
        raise ValueError('a positive result is required')
    actions, degrees = _integer_family(actions, result.prime)
    ids = {h: i for i, h in enumerate(result.phases)}
    certificates = []
    for h in result.phases:
        for a, degree in zip(actions, degrees):
            k, target = divmod(h+degree, N)
            s, t = ids[h], ids[target]
            packet = ControlPacket.from_edges(len(ids), 0, 1, [(s, t, 1, Affine(a, (0,)*N), 1)])
            certificates.append(certify_lattice_ports(packet, result.bases, result.prime, {(s, t): k}))
    return tuple(certificates)
