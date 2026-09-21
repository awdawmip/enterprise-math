"""Finite congruence-image frames for fixed-threshold native-X6 BRC peaks.

Frames preserve Z_p^6; they are analysis symmetries, not native rotations or
fractional Cell moves. Their rational lifts need NOT form a finite group.
Only the finite PGL image acts on safe homothety classes. Fixed-law first-hit
observations are preserved; atom words, larger thresholds and raw coordinates
are not. Existing lattice, BRC, germ and probability implementations are reused.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache

from .brc_transport import matrix, eye, inv, mm
from .brc_control_port import ControlPacket
from .heartbeat_switching_carry import _prime, _nat, _minimum, linear_carry_spread
from .heartbeat_carry_peak import PeakState, PeakEdge, HIT, UNKNOWN, _atoms, projective_lattice_key
from .heartbeat_peak_orbits import _digest, _row_equal, _safe_controls
from .heartbeat_peak_quotient import PeakChain

N = 6
I = eye(N)
IK = tuple(tuple(int(i == j) for j in range(N)) for i in range(N))


def _positive(x):
    x = _nat(x)
    if not x:
        raise ValueError('positive integer required')
    return x


def _local_frame(a, p):
    a = matrix(a)
    if len(a) != N or len(a[0]) != N:
        raise ValueError('six-dimensional frame required')
    if _minimum(a, p) < 0 or _minimum(inv(a), p) < 0:
        raise ValueError('frame must preserve the standard p-lattice')
    return a


def _normalize(rows, p, depth):
    modulus = p**depth
    flat = tuple(x % modulus for row in rows for x in row)
    pivot = next(x for x in flat if x % p)
    u = pow(pivot, -1, modulus)
    flat = tuple(u*x % modulus for x in flat)
    return tuple(tuple(flat[N*i:N*(i+1)]) for i in range(N))


def projective_frame_key(basis, prime: int, depth: int):
    """Exact GL_6(Z_p) / (units*(I+p^depth M_6)) key; depth>=1."""
    p, d = _prime(prime), _positive(depth)
    a = _local_frame(basis, p)
    modulus = p**d
    rows = tuple(tuple(v.numerator * pow(v.denominator, -1, modulus) % modulus
                       for v in row) for row in a)
    return _normalize(rows, p, d)


def _multiply(a, b, p, depth):
    modulus = p**depth
    return _normalize(tuple(tuple(sum(a[i][k]*b[k][j] for k in range(N)) % modulus
                                  for j in range(N)) for i in range(N)), p, depth)


def _closure(generators, p, depth, cap):
    found, todo = {IK}, deque([IK])
    while todo:
        a = todo.popleft()
        for g in generators:
            b = _multiply(g, a, p, depth)
            if b not in found:
                if len(found) >= cap:
                    raise ValueError('GROUP_LIMIT: no completeness claim within this budget')
                found.add(b)
                todo.append(b)
    return (IK,) + tuple(sorted(found-{IK}))


@dataclass(frozen=True)
class FiniteProjectiveImage:
    prime: int
    depth: int
    generators: tuple
    keys: tuple

    @classmethod
    def generated(cls, prime, depth, generators=(), *, max_group=4096):
        p, d, cap = _prime(prime), _positive(depth), _positive(max_group)
        generators = tuple(_local_frame(g, p) for g in generators)
        keys = tuple(projective_frame_key(g, p, d) for g in generators)
        return cls(p, d, generators, _closure(keys, p, d, cap))

    def verify(self):
        expected = self.generated(self.prime, self.depth, self.generators,
                                  max_group=len(self.keys))
        if expected != self:
            raise ValueError('invalid finite congruence image')
        return True


def shear_frame_period(prime: int, threshold: int, coefficient: int = 1) -> int:
    """Effective order of I+coefficient*E_ij on ALL safe lattices, i!=j."""
    p, r = _prime(prime), _positive(threshold)
    if type(coefficient) is not int:
        raise TypeError('integer shear coefficient required')
    if not coefficient:
        return 1
    n, v = abs(coefficient), 0
    while n % p == 0:
        n //= p
        v += 1
    return p**max(0, r-1-v)


def symmetry_guard_depth(packet: ControlPacket, prime: int, threshold: int) -> int:
    """m+C suffices for lift-independent conjugated action-germ tests.

    m=R-1, C=max kappa_p(A). It is a guard for the full action-germ certificate,
    not a minimal precision theorem for every HIT-only observation.
    """
    p, r = _prime(prime), _positive(threshold)
    if r < 2:
        raise ValueError('use the inherited standard-lattice method for threshold 1')
    return r-1 + max(linear_carry_spread(a, p) for _, _, _, a, _ in _atoms(packet))


def _check_subgroup(keys, p, depth):
    allowed = set(keys)
    if IK not in allowed:
        raise ArithmeticError('identity missing')
    generators, generated = [], {IK}
    for g in keys:
        if g not in generated:
            generators.append(g)
            generated = set(_closure(tuple(generators), p, depth, len(allowed)))
            if not generated <= allowed:
                raise ArithmeticError('admitted frames are not a subgroup')
    return tuple(generators)


@dataclass(frozen=True)
class ProjectivePeakCertificate:
    packet_digest: str
    prime: int
    threshold: int
    guard_depth: int
    ambient: FiniteProjectiveImage
    admitted: tuple
    effective: tuple
    row_checks: int
    scalar_safe_controls: tuple[int, ...]


def discover_projective_symmetry(packet, prime, threshold, generators=(), *, max_group=4096):
    """Complete stabilizer for a declared finite guarded congruence ambient.

    Not a search of all GL_6(Z_p) unless the generators cover its guarded
    projective image. Exact on the full action-germ/weight-row test only.
    Control labels are fixed. Rational lifts can have infinite order.
    """
    p, r, cap = _prime(prime), _positive(threshold), _positive(max_group)
    generators = tuple(_local_frame(g, p) for g in generators)
    return _discover(packet, p, r, generators, cap)


@lru_cache(maxsize=64)
def _discover(packet, p, r, generators, cap):
    depth = symmetry_guard_depth(packet, p, r)
    ambient = FiniteProjectiveImage.generated(p, depth, generators, max_group=cap)
    atoms = _atoms(packet)
    rows = tuple(tuple((t, w*n, a) for s, t, w, a, n in atoms if s == c)
                 for c in range(packet.state_count))
    admitted, checks = [], 0
    for key in ambient.keys:
        g = matrix(key)
        gi = inv(g)
        valid = True
        for row in rows:
            transformed = tuple((t, w, mm(mm(g, a), gi)) for t, w, a in row)
            checks += 1
            if not _row_equal(transformed, row, p, r, 'threshold'):
                valid = False
                break
        if valid:
            admitted.append(key)
    _check_subgroup(tuple(admitted), p, depth)
    effective = set(projective_frame_key(g, p, r-1) for g in admitted)
    effective = (IK,) + tuple(sorted(effective-{IK}))
    _check_subgroup(effective, p, r-1)
    return ProjectivePeakCertificate(_digest(packet), p, r, depth, ambient,
                                     tuple(admitted), effective, checks,
                                     _safe_controls(packet, atoms))


def _verify(packet, cert):
    if not isinstance(cert, ProjectivePeakCertificate):
        raise TypeError('ProjectivePeakCertificate required')
    expected = discover_projective_symmetry(packet, cert.prime, cert.threshold,
        cert.ambient.generators, max_group=len(cert.ambient.keys))
    if cert != expected:
        raise ValueError('source, threshold or group certificate mismatch')


@dataclass(frozen=True)
class ProjectivePeakAutomaton:
    certificate: ProjectivePeakCertificate
    initial_control: int
    max_states: int
    states: tuple
    edges: tuple
    complete: bool
    atom_successors: int


def compile_projective_peak(packet, certificate, *, initial_control=0, max_states=10000):
    """Generate finite-image orbit representatives; never build a raw full graph."""
    _verify(packet, certificate)
    cap = _positive(max_states)
    if type(initial_control) is not int or not 0 <= initial_control < packet.state_count:
        raise ValueError('invalid initial control')
    p, r = certificate.prime, certificate.threshold
    atoms = _atoms(packet)
    @lru_cache(maxsize=16384)
    def canonical(c, lattice):
        if c in certificate.scalar_safe_controls:
            return PeakState(-3, IK)
        return min((PeakState(c, projective_lattice_key(mm(matrix(g), matrix(lattice)), p))
                    for g in certificate.effective), key=lambda x: (x.control, x.lattice))
    seed = canonical(initial_control, IK)
    states, index, todo, edges = [seed], {seed: 0}, deque([0]), []
    partial, successors = False, 0
    while todo:
        i = todo.popleft()
        state = states[i]
        if state.control == -3:
            edges.append(PeakEdge(i, i, -1, F(1), 1))
            continue
        for j, (s, c, w, a, n) in enumerate(atoms):
            if s != state.control:
                continue
            successors += 1
            moved = mm(a, matrix(state.lattice))
            if linear_carry_spread(moved, p) >= r:
                target = HIT
            else:
                nxt = canonical(c, projective_lattice_key(moved, p))
                if nxt in index:
                    target = index[nxt]
                elif len(states) < cap:
                    target = len(states)
                    states.append(nxt)
                    index[nxt] = target
                    todo.append(target)
                else:
                    target, partial = UNKNOWN, True
            edges.append(PeakEdge(i, target, j, w, n))
    return ProjectivePeakAutomaton(certificate, initial_control, cap, tuple(states),
                                   tuple(edges), not partial, successors)


def projective_peak_chain(packet, automaton):
    """Recheck the certificate and retained edges, then reuse PeakChain/star.

    Original atom weight/multiplicity remain on representative edges. No global
    atom-word equivalence is claimed, so analytic channels are not exported.
    """
    if not isinstance(automaton, ProjectivePeakAutomaton):
        raise TypeError('ProjectivePeakAutomaton required')
    expected = compile_projective_peak(packet, automaton.certificate,
        initial_control=automaton.initial_control, max_states=automaton.max_states)
    if expected != automaton:
        raise ValueError('altered compiled automaton')
    n = len(automaton.states)
    k = [[F(0)]*(n+2) for _ in range(n+2)]
    for e in automaton.edges:
        t = n if e.target == HIT else n+1 if e.target == UNKNOWN else e.target
        k[e.source][t] += e.mass
    k[n][n] = k[n+1][n+1] = F(1)
    return PeakChain(tuple(tuple(row) for row in k), ('SAFE',)*n+('HIT', 'UNKNOWN'),
                     duration=packet.duration, complete=automaton.complete,
                     source_digest=_digest(automaton))
