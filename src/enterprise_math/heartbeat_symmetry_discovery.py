"""Automatic positive-native-axis symmetry discovery for BRC carry peaks.

Research candidate. Search scope is S6 with control ports fixed. A discovered
subgroup is complete only for the declared action-germ/weight-row certificate,
NOT for all reachable-state Markov symmetries, signed frames or GL_6(Z_p).

The action germ is exact on every safe *oriented projective lattice*. It need
not be a minimal HIT-only observer. Rational bases are analysis witnesses,
not fractional native Cell moves. All probability and source data stay exact.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import permutations

from .brc_transport import Matrix, matrix, eye, inv, mm, sm
from .brc_control_port import ControlPacket
from .heartbeat_switching_carry import _prime, _nat, _minimum, linear_carry_spread
from .heartbeat_carry_peak import (projective_lattice_key, _atoms, PeakState,
                                   PeakEdge, HIT, UNKNOWN)
from .heartbeat_peak_orbits import (Frame, FiniteFrameGroup, PeakSymmetryCertificate,
                                   OrbitPeakAutomaton, _safe_controls)
from .heartbeat_peak_quotient import PeakChain

N = 6
I = eye(N)
ID = tuple(range(N))
ALL_PERMUTATIONS = tuple(permutations(ID))


@lru_cache(maxsize=64)
def _validated_atoms(packet):
    # ControlPacket and all nested branch records are immutable/hashable.
    return _atoms(packet)


def _square(a) -> Matrix:
    a = matrix(a)
    if len(a) != N or any(len(row) != N for row in a):
        raise ValueError('exactly six native components required')
    inv(a)
    return a


def _parameters(prime, threshold, mode):
    p, r = _prime(prime), _nat(threshold)
    if r < 1 or mode not in ('exact', 'threshold'):
        raise ValueError('positive threshold and exact/threshold mode required')
    return p, r


def _mod(x: F, modulus: int) -> int:
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


@lru_cache(maxsize=65536)
def _fingerprint(a: Matrix, p: int, r: int, mode: str):
    if mode == 'exact':
        pivot = next(x for row in a for x in row if x)
        return ('EXACT_PROJECTIVE', tuple(x/pivot for row in a for x in row))
    h = projective_lattice_key(a, p)
    if r == 1:
        return ('STANDARD_IMAGE', h)
    normalized = sm(F(p)**(-_minimum(a, p)), a)
    unit = mm(inv(matrix(h)), normalized)
    if _minimum(unit, p) < 0 or _minimum(inv(unit), p) < 0:
        raise ArithmeticError('image-lattice basis lost its p-integral unit factor')
    modulus = p**(r-1)
    residues = tuple(_mod(x, modulus) for row in unit for x in row)
    pivot = next(x for x in residues if x % p)
    scale = pow(pivot, -1, modulus)
    return ('ORIENTED_IMAGE_AND_PROJECTIVE_UNIT', h,
            tuple((x*scale) % modulus for x in residues))


def action_germ_key(a, prime: int, threshold: int, *, mode='threshold'):
    """Canonical complete key for all-safe-lattice action equality.

    R>=2: image of the standard lattice, plus its p-integral change-of-basis
    modulo p^(R-1), modulo a common unit scalar. R=1: just the standard image.
    `exact` instead means equality of rational matrices up to scalar.
    """
    p, r = _parameters(prime, threshold, mode)
    return _fingerprint(_square(a), p, r, mode)


def safe_lattice_probes(prime: int, threshold: int) -> tuple[Matrix, ...]:
    """At most eight witnesses: standard, six axis lines, one all-ones line.

    These span lattices Z_p*v + p^(R-1)Z_p^6. The all-ones vector is a
    composite algebraic probe, NOT a new primitive spatial direction.
    """
    p, r = _parameters(prime, threshold, 'threshold')
    if r == 1:
        return (I,)
    depth = p**(r-1)
    probes = [I]
    for k in range(N):
        probes.append(matrix([[int(i == j)*(1 if i == k else depth)
                               for j in range(N)] for i in range(N)]))
    probes.append(matrix([[1 if j == 0 else depth*int(i == j)
                           for j in range(N)] for i in range(N)]))
    return tuple(probes)


@dataclass(frozen=True)
class ActionSeparation:
    prime: int
    threshold: int
    probe_index: int
    input_basis: Matrix
    left_output: tuple
    right_output: tuple


def separate_safe_actions(a, b, prime: int, threshold: int) -> ActionSeparation | None:
    """Return a real safe lattice distinguishing actions, or exact equivalence.

    Different output lattices need not have different immediate HIT labels.
    This is an action-level witness, not an unproved first-passage difference.
    """
    p, r = _parameters(prime, threshold, 'threshold')
    a, b = _square(a), _square(b)
    equal = _fingerprint(a, p, r, 'threshold') == _fingerprint(b, p, r, 'threshold')
    for i, basis in enumerate(safe_lattice_probes(p, r)):
        left = projective_lattice_key(mm(a, basis), p)
        right = projective_lattice_key(mm(b, basis), p)
        if left != right:
            if equal:
                raise ArithmeticError('canonical action key contradicted a safe probe')
            return ActionSeparation(p, r, i, basis, left, right)
    if not equal:
        raise ArithmeticError('eight-probe completeness contradicted the action key')
    return None


def _permutation(p):
    p = tuple(p)
    if len(p) != N or any(type(x) is not int for x in p) or set(p) != set(ID):
        raise ValueError('permutation of six positive native axes required')
    return p


def _compose(p, q):
    return tuple(p[q[j]] for j in ID)


@lru_cache(maxsize=720)
def _basis(p):
    return matrix([[int(i == p[j]) for j in ID] for i in ID])


@lru_cache(maxsize=65536)
def _conjugate(a, perm):
    inverse = tuple(perm.index(i) for i in ID)
    return tuple(tuple(a[inverse[i]][inverse[j]] for j in ID) for i in ID)


def _closure(generators):
    seen, todo = {ID}, deque([ID])
    while todo:
        a = todo.popleft()
        for b in generators:
            c = _compose(b, a)
            if c not in seen:
                seen.add(c); todo.append(c)
    return frozenset(seen)


def _generators(elements):
    elements = frozenset(elements)
    if ID not in elements:
        raise ValueError('group omits identity')
    gens, covered = [], frozenset({ID})
    for perm in sorted(elements):
        if perm not in covered:
            gens.append(perm); covered = _closure(tuple(gens))
            if not covered <= elements:
                raise ValueError('accepted permutations are not a closed subgroup')
    return tuple(gens)


@dataclass(frozen=True)
class AxisPermutationGroup(FiniteFrameGroup):
    """Existing frame-group interface with an efficient exact S6 verifier."""
    def verify(self):
        _prime(self.prime)
        if type(self.control_count) is not int or self.control_count < 1:
            raise ValueError('positive control count required')
        perms = []
        for frame in self.frames:
            if frame.controls != tuple(range(self.control_count)):
                raise ValueError('discovery fixes control ports')
            perm = tuple(next((i for i in ID if frame.basis[i][j] == 1), -1) for j in ID)
            _permutation(perm)
            if frame.basis != _basis(perm):
                raise ValueError('positive permutation frames only')
            perms.append(perm)
        if len(perms) != len(set(perms)):
            raise ValueError('duplicated group frames')
        _generators(perms)
        return True


@lru_cache(maxsize=8192)
def _row_signatures(packet, p, r, mode, atomwise, perm=ID):
    rows = [dict() for _ in range(packet.state_count)]
    for index, (source, target, weight, a, count) in enumerate(_validated_atoms(packet)):
        key = (target, index if atomwise else None,
               _fingerprint(_conjugate(a, perm), p, r, mode))
        rows[source][key] = rows[source].get(key, F(0)) + weight*count
    return tuple(tuple(sorted(row.items())) for row in rows)


@dataclass(frozen=True)
class SymmetryDiscovery:
    packet_digest: str
    prime: int
    threshold: int
    mode: str
    atomwise: bool
    complete: bool
    candidates_tested: int
    accepted: tuple[tuple[int, ...], ...]
    rejected: tuple[tuple[tuple[int, ...], int], ...]
    generators: tuple[tuple[int, ...], ...]
    group: AxisPermutationGroup

    @property
    def status(self):
        return 'COMPLETE_WITHIN_S6_GERM_CONTRACT' if self.complete else 'CANDIDATE_LIMIT'


def discover_axis_symmetries(packet: ControlPacket, prime: int, threshold: int, *,
                             mode='threshold', atomwise=False,
                             max_candidates=720) -> SymmetryDiscovery:
    """Enumerate S6 without caller-provided generators; keep ports fixed.

    Equal action-germ channels are coalesced using ORIGINAL weight*count.
    `atomwise` forbids permutation of original atom IDs. A budgeted result
    remains a sound subgroup, but does not claim maximality or completeness.
    """
    if not isinstance(packet, ControlPacket) or type(atomwise) is not bool:
        raise TypeError('ControlPacket and Boolean atomwise required')
    p, r = _parameters(prime, threshold, mode)
    cap = _nat(max_candidates)
    if cap < 1:
        raise ValueError('positive candidate budget required')
    cap = min(cap, len(ALL_PERMUTATIONS))
    expected = _row_signatures(packet, p, r, mode, atomwise)
    accepted, rejected = [], []
    for perm in ALL_PERMUTATIONS[:cap]:
        rows = _row_signatures(packet, p, r, mode, atomwise, perm)
        bad = next((s for s in range(packet.state_count) if rows[s] != expected[s]), None)
        if bad is None:
            accepted.append(perm)
        else:
            rejected.append((perm, bad))
    # Each admitted permutation is a proven stabilizer. Its generated closure
    # is sound even if the caller did not budget enough to test every candidate.
    closure = _closure(tuple(accepted))
    if set(p for p, _s in rejected) & closure:
        raise ArithmeticError('kernel stabilizer closure contradicted a tested rejection')
    if cap == 720 and closure != frozenset(accepted):
        raise ArithmeticError('complete accepted set is not a subgroup')
    gens = _generators(closure)
    frames = tuple(Frame(tuple(range(packet.state_count)), _basis(p)) for p in sorted(closure))
    group = AxisPermutationGroup(p, packet.state_count, frames)
    group.verify()
    return SymmetryDiscovery(sha256(repr(packet).encode()).hexdigest(), p, r, mode,
        atomwise, cap == 720, cap, tuple(sorted(closure)), tuple(rejected), gens, group)


def verify_symmetry_discovery(packet: ControlPacket, result: SymmetryDiscovery) -> bool:
    """Replay only the declared search budget and compare every field."""
    if not isinstance(result, SymmetryDiscovery):
        raise TypeError('SymmetryDiscovery required')
    expected = discover_axis_symmetries(packet, result.prime, result.threshold,
        mode=result.mode, atomwise=result.atomwise, max_candidates=result.candidates_tested)
    if result != expected:
        raise ValueError('discovery certificate does not match packet/search evidence')
    return True


def _certificate(packet, result):
    verify_symmetry_discovery(packet, result)
    atoms = _validated_atoms(packet)
    rows = _row_signatures(packet, result.prime, result.threshold, result.mode, result.atomwise)
    for perm in result.accepted:
        if _row_signatures(packet, result.prime, result.threshold, result.mode, result.atomwise, perm) != rows:
            raise ValueError("generated permutation failed full coefficient recheck")
    return PeakSymmetryCertificate(result.packet_digest, result.prime, result.threshold,
        result.mode, result.group, len(result.accepted)*packet.state_count,
        _safe_controls(packet, atoms))


def _canonical(control, lattice, cert, generators):
    if control in cert.scalar_safe_controls:
        return PeakState(-3, tuple(tuple(int(x) for x in row) for row in I)), 0
    # Generate the lattice ORBIT, not the whole frame group. Stabilizers need
    # not multiply canonicalization cost. This reuses the old oriented codec.
    seen, todo, edges = {lattice}, deque([lattice]), 0
    while todo:
        a = todo.popleft()
        for perm in generators:
            edges += 1
            inverse = tuple(perm.index(i) for i in ID)
            moved = matrix(tuple(a[inverse[i]] for i in ID))
            b = projective_lattice_key(moved, cert.prime)
            if b not in seen:
                seen.add(b); todo.append(b)
    return PeakState(control, min(seen)), edges


def compile_discovered_peak(packet: ControlPacket, discovery: SymmetryDiscovery, *,
                            initial_control=0, max_states=10000) -> OrbitPeakAutomaton:
    """Discovery -> orbit-only construction; never calls the full graph compiler.

    Extends the inherited compiler with generator-orbit traversal rather than
    enumerating every stabilizer frame per state. Source atoms/weights/counts,
    oriented codec, result type and first-passage calculus remain unchanged.
    """
    cert = _certificate(packet, discovery)
    cap = _nat(max_states)
    if cap < 1 or type(initial_control) is not int or not 0 <= initial_control < packet.state_count:
        raise ValueError('valid initial control and positive state budget required')
    atoms = _validated_atoms(packet)
    outgoing = [[(j, atom) for j, atom in enumerate(atoms) if atom[0] == s]
                for s in range(packet.state_count)]
    work = 0
    @lru_cache(maxsize=32768)
    def canonical(c, l):
        nonlocal work
        state, count = _canonical(c, l, cert, discovery.generators)
        work += count
        return state
    seed = canonical(initial_control, projective_lattice_key(I, cert.prime))
    states, lookup, todo, edges = [seed], {seed: 0}, deque([0]), []
    complete, successors = True, 0
    while todo:
        source = todo.popleft(); state = states[source]
        if state.control == -3:
            edges.append(PeakEdge(source, source, -1, F(1), 1)); continue
        for j, (_s, t, w, a, count) in outgoing[state.control]:
            successors += 1
            moved = mm(a, matrix(state.lattice))
            if linear_carry_spread(moved, cert.prime) >= cert.threshold:
                target = HIT
            else:
                nxt = canonical(t, projective_lattice_key(moved, cert.prime))
                if nxt in lookup:
                    target = lookup[nxt]
                elif len(states) < cap:
                    target = len(states); lookup[nxt] = target; states.append(nxt); todo.append(target)
                else:
                    target = UNKNOWN; complete = False
            edges.append(PeakEdge(source, target, j, w, count))
    return OrbitPeakAutomaton(cert, packet.duration, initial_control, tuple(states), tuple(edges),
        False, complete, cap, True, len(states), successors, work)


def discovered_observation_chain(packet, discovery, auto) -> PeakChain:
    """Replay the representative compiler before exposing the existing readout."""
    expected = compile_discovered_peak(packet, discovery, initial_control=auto.initial_control,
                                        max_states=auto.max_states)
    if auto != expected:
        raise ValueError('representative automaton differs from source/certificate replay')
    n = len(auto.states); rows = [[F(0)]*(n+2) for _ in range(n+2)]
    for e in auto.edges:
        t = n if e.target == HIT else n+1 if e.target == UNKNOWN else e.target
        rows[e.source][t] += e.mass
    rows[n][n] = rows[n+1][n+1] = F(1)
    return PeakChain(tuple(tuple(row) for row in rows), ('SAFE',)*n+('HIT','UNKNOWN'),
        duration=auto.duration, complete=auto.complete,
        source_digest=sha256(repr(auto).encode()).hexdigest())


@dataclass(frozen=True)
class AxisSymmetryProfile:
    prime: int
    packet_digest: str
    atomwise: bool
    changes: tuple[tuple[int, tuple[tuple[int, ...], ...]], ...]
    final_threshold: int
    matrix_pairs_checked: int
    exact_group_order: int


def discover_axis_profile(packet: ControlPacket, prime: int, *, atomwise=False) -> AxisSymmetryProfile:
    """Discover every algebraic symmetry breakpoint inside S6, without raw states.

    Reuses the prior exact pair-separation cutoff. Completeness concerns the
    fixed-control, action-germ row contract, not arbitrary state equivalence.
    """
    from .heartbeat_peak_orbits import action_separation_threshold
    p = _prime(prime)
    if type(atomwise) is not bool:
        raise TypeError('Boolean atomwise required')
    atoms = _validated_atoms(packet)
    cuts, count = {1}, 0
    for perm in ALL_PERMUTATIONS:
        for i, (s, t, _w, a, _n) in enumerate(atoms):
            transformed = _conjugate(a, perm)
            for j, (c, d, _v, b, _m) in enumerate(atoms):
                if (s, t) == (c, d) and (not atomwise or i == j):
                    cutoff = action_separation_threshold(transformed, b, p)
                    if cutoff is not None:
                        cuts.add(cutoff)
                    count += 1
    changes, previous = [], None
    for r in sorted(cuts):
        result = discover_axis_symmetries(packet, p, r, atomwise=atomwise)
        current = result.accepted
        if previous is not None and not set(current) <= set(previous):
            raise ArithmeticError('nonmonotone symmetry filtration')
        if current != previous:
            changes.append((r, current)); previous = current
    exact = discover_axis_symmetries(packet, p, 1, mode='exact', atomwise=atomwise)
    if previous != exact.accepted:
        raise ArithmeticError('finite cutoffs did not attain exact projective-action symmetry')
    return AxisSymmetryProfile(p, sha256(repr(packet).encode()).hexdigest(), atomwise,
                               tuple(changes), max(cuts), count, len(exact.accepted))
