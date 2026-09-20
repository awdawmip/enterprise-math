"""Exact thresholded carry-peak observer for finite Heartbeat World BRC controls.

Research candidate, not Foundation. For a fixed prime p and a positive integer
threshold m, homothety classes of the accumulated column lattice are a finite
future-sufficient state while kappa<m. Matrix cancellations and orientation
are retained. Scalar depth, translations, full branch identities and occupancy
are NOT reconstructed. Observations are at packet boundaries; probabilities
must be fixed on the declared finite controls, with exact row sums one.

Canonicalization uses the already-employed exact integer Hermite normal form;
probability evaluation reuses the existing finite positive recurrent BRC star.
A resource-truncated exploration returns an interval, never a false exact law.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import lcm
from typing import Sequence
from .brc_transport import Matrix, matrix, eye, mm, sm
from .brc_control_port import ControlPacket
from .brc_weighted_recurrent import finite_recurrent_mass_analysis
from .heartbeat_switching_carry import _prime, _nat, _minimum, _valuation, linear_carry_spread
from .heartbeat_lattice_search import SM, hermite_normal_form, _same_local_lattice

N = 6
HIT = -1
FRONTIER = -2


@lru_cache(maxsize=8192)
def _canonical(a: Matrix, p: int) -> Matrix:
    if len(a) != N or len(a[0]) != N or not SM(a).det():
        raise ValueError('nonsingular six-axis matrix required')
    c = sm(F(p)**(-_minimum(a, p)), a)
    denominator = 1
    for row in c:
        for v in row:
            denominator = lcm(denominator, v.denominator)
    if denominator % p == 0:
        raise ArithmeticError('normalized matrix must be p-integral')
    integer = SM([[int(v*denominator) for v in row] for row in c])
    depth = _valuation(int(integer.det()), p)
    # Add p^depth Z^6 to remove all non-p primary index. Localizing this
    # integer HNF gives exactly c Z_p^6, not merely its Smith group type.
    basis = hermite_normal_form(integer.row_join((p**depth)*SM.eye(N)))
    out = matrix(tuple(tuple(int(basis[i, j]) for j in range(N)) for i in range(N)))
    if _minimum(out, p) != 0 or not _same_local_lattice(c, out, p):
        raise ArithmeticError('canonical localized lattice verification failed')
    return out


def canonical_carry_lattice(a, prime: int) -> Matrix:
    """Unique integral HNF representative of [a Z_p^6] modulo scalar homothety."""
    return _canonical(matrix(a), _prime(prime))


@dataclass(frozen=True)
class PeakState:
    control: int
    lattice: Matrix


@dataclass(frozen=True)
class PeakKernel:
    prime: int
    threshold: int  # HIT means kappa >= threshold, not kappa > threshold
    source_digest: str
    start_control: int
    packet_duration: int
    states: tuple[PeakState, ...]
    witnesses: tuple[tuple[int, ...], ...]  # flattened original atom indices
    arcs: tuple[tuple[int, int, F], ...]
    hit_witness: tuple[int, ...] | None
    max_states: int
    complete: bool


@dataclass(frozen=True)
class PeakProbability:
    lower: F
    upper: F
    hit_probabilities: tuple[F, ...]
    frontier_probabilities: tuple[F, ...]
    active_states: tuple[int, ...]
    exact: bool


def _atoms(packet: ControlPacket):
    if not isinstance(packet, ControlPacket) or packet.duration < 1:
        raise ValueError('positive-duration finite ControlPacket required')
    atoms = []
    totals = [F(0)]*packet.state_count
    for s, t, histogram in packet.blocks:
        for weight, action, count in histogram.entries:
            a = action.a
            if any(v.denominator != 1 for row in a for v in row) or not SM(a).det():
                raise ValueError('nonsingular INTEGER six-axis linear actions required')
            mass = weight*count
            totals[s] += mass
            atoms.append((s, t, mass, a))
    if any(v != 1 for v in totals):
        raise ValueError('exactly stochastic rows required; no implicit normalization')
    return tuple(atoms)


def _binding(packet):
    return sha256(repr(packet).encode('utf-8')).hexdigest()


def compile_peak_kernel(packet: ControlPacket, prime: int, *, threshold: int,
                        start_control: int = 0, max_states: int = 4096) -> PeakKernel:
    """Explore the exact safe projective-lattice ball, with a sound frontier cap.

    Every retained state is reachable with no previous HIT. Omitting a newly
    discovered safe state redirects only that transition to FRONTIER. There
    is no assumption that the original chain terminates or has bounded carry.
    The same frozen packet is reused; absolute-time dependent laws need an
    adequate finite clock in its controls. Nonzero affine translations are
    deliberately invisible to this LINEAR observer, not asserted to cancel.
    """
    p = _prime(prime)
    if _nat(threshold) < 1 or _nat(max_states) < 1:
        raise ValueError('positive threshold and state budget required')
    atoms = _atoms(packet)
    if type(start_control) is not int or not 0 <= start_control < packet.state_count:
        raise ValueError('invalid starting control')
    outgoing = [[] for _ in range(packet.state_count)]
    for j, atom in enumerate(atoms):
        outgoing[atom[0]].append((j, atom))
    states = [PeakState(start_control, eye(N))]
    words = [()]
    index = {states[0]: 0}
    arcs = {}
    first_hit = None
    cursor = 0
    while cursor < len(states):
        state = states[cursor]
        for j, (_s, t, mass, a) in outgoing[state.control]:
            moved = mm(a, state.lattice)
            if linear_carry_spread(moved, p) >= threshold:
                target = HIT
                if first_hit is None:
                    first_hit = words[cursor]+(j,)
            else:
                nxt = PeakState(t, canonical_carry_lattice(moved, p))
                if nxt not in index and len(states) < max_states:
                    index[nxt] = len(states)
                    states.append(nxt)
                    words.append(words[cursor]+(j,))
                target = index.get(nxt, FRONTIER)
            arcs[cursor, target] = arcs.get((cursor, target), F(0))+mass
        cursor += 1
    edges = tuple((s, t, w) for (s, t), w in sorted(arcs.items()))
    return PeakKernel(p, threshold, _binding(packet), start_control, packet.duration,
                      tuple(states), tuple(words), edges, first_hit, max_states,
                      not any(t == FRONTIER for _, t, _ in edges))


def verify_peak_kernel(packet: ControlPacket, kernel: PeakKernel) -> bool:
    """Check all actual transitions and reachability words, not just a PASS flag."""
    if not isinstance(kernel, PeakKernel) or kernel.source_digest != _binding(packet):
        raise ValueError('kernel/model content mismatch')
    p = _prime(kernel.prime)
    if _nat(kernel.threshold) < 1 or _nat(kernel.max_states) < len(kernel.states):
        raise ValueError('invalid threshold/state budget')
    atoms = _atoms(packet)
    if kernel.packet_duration != packet.duration or not kernel.states:
        raise ValueError('invalid packet time port or empty state set')
    if kernel.states[0] != PeakState(kernel.start_control, eye(N)):
        raise ValueError('initial condition mismatch')
    index = {s: i for i, s in enumerate(kernel.states)}
    if len(index) != len(kernel.states) or len(kernel.witnesses) != len(kernel.states):
        raise ValueError('duplicate states or missing witnesses')
    expected = {}
    for i, state in enumerate(kernel.states):
        if not 0 <= state.control < packet.state_count:
            raise ValueError('unknown control in kernel')
        if canonical_carry_lattice(state.lattice, p) != state.lattice:
            raise ValueError('noncanonical projective lattice')
        if linear_carry_spread(state.lattice, p) >= kernel.threshold:
            raise ValueError('unsafe state retained as safe')
        ctrl, product = kernel.start_control, eye(N)
        for j in kernel.witnesses[i]:
            if type(j) is not int or not 0 <= j < len(atoms):
                raise ValueError('invalid witness atom')
            s, t, _mass, a = atoms[j]
            if s != ctrl:
                raise ValueError('illegal witness control path')
            product, ctrl = mm(a, product), t
            if linear_carry_spread(product, p) >= kernel.threshold:
                raise ValueError('safe-state witness already crossed threshold')
        if PeakState(ctrl, canonical_carry_lattice(product, p)) != state:
            raise ValueError('witness does not reconstruct retained state')
        for s, t, mass, a in atoms:
            if s != state.control:
                continue
            moved = mm(a, state.lattice)
            target = HIT if linear_carry_spread(moved, p) >= kernel.threshold else index.get(
                PeakState(t, canonical_carry_lattice(moved, p)), FRONTIER)
            expected[i, target] = expected.get((i, target), F(0))+mass
    if tuple((s, t, v) for (s, t), v in sorted(expected.items())) != kernel.arcs:
        raise ValueError('kernel transitions do not match the actual model')
    if kernel.complete != (not any(t == FRONTIER for _, t, _ in kernel.arcs)):
        raise ValueError('incorrect completeness label')
    if not kernel.complete and len(kernel.states) != kernel.max_states:
        raise ValueError('unexplained missing safe states')
    has_hit = any(t == HIT for _, t, _ in kernel.arcs)
    if has_hit != (kernel.hit_witness is not None) or (has_hit and not kernel.hit_witness):
        raise ValueError('a reachable hit requires a nonempty actual first-hit witness')
    if kernel.hit_witness is not None:
        ctrl, product = kernel.start_control, eye(N)
        for k, j in enumerate(kernel.hit_witness):
            if type(j) is not int or not 0 <= j < len(atoms):
                raise ValueError('invalid hit witness atom')
            s, t, _, a = atoms[j]
            if ctrl != s:
                raise ValueError('illegal hit witness control path')
            product, ctrl = mm(a, product), t
            crossed = linear_carry_spread(product, p) >= kernel.threshold
            if crossed != (k == len(kernel.hit_witness)-1):
                raise ValueError('witness must end at first crossing')
    return True


def solve_peak_probability(packet: ControlPacket, kernel: PeakKernel) -> PeakProbability:
    """Exact eventual HIT probability, or certified [HIT, HIT+FRONTIER] interval.

    First remove states having no path to either boundary. This is essential:
    harmless closed classes make I-Q singular if blindly sent to a solver.
    """
    verify_peak_kernel(packet, kernel)
    n = len(kernel.states)
    predecessors = [[] for _ in range(n)]
    roots = set()
    for s, t, mass in kernel.arcs:
        if mass <= 0:
            raise ValueError('strictly positive kernel edges required')
        if t < 0:
            roots.add(s)
        else:
            predecessors[t].append(s)
    active = set(roots); queue = deque(roots)
    while queue:
        for s in predecessors[queue.popleft()]:
            if s not in active:
                active.add(s); queue.append(s)
    active = tuple(sorted(active)); pos = {s: i for i, s in enumerate(active)}
    q = [[F(0) for _ in active] for _ in active]
    hit = [F(0) for _ in active]; unknown = [F(0) for _ in active]
    for s, t, mass in kernel.arcs:
        if s not in pos:
            continue
        i = pos[s]
        if t == HIT:
            hit[i] += mass
        elif t == FRONTIER:
            unknown[i] += mass
        elif t in pos:
            q[i][pos[t]] += mass
    h = [F(0)]*n; u = [F(0)]*n
    if active:
        result = finite_recurrent_mass_analysis(q)
        if not result.stable or not result.verify_stable_certificate():
            raise ArithmeticError('target-coaccessible finite kernel is not transient')
        for s, i in pos.items():
            h[s] = sum((result.star[i][j]*hit[j] for j in range(len(active))), F(0))
            u[s] = sum((result.star[i][j]*unknown[j] for j in range(len(active))), F(0))
    if any(v < 0 or v+w > 1 for v, w in zip(h, u)):
        raise ArithmeticError('probability certificate outside [0,1]')
    return PeakProbability(h[0], h[0]+u[0], tuple(h), tuple(u), active, u[0] == 0)


def first_passage_prefix(packet: ControlPacket, kernel: PeakKernel, steps: int):
    """Mass of FIRST hits at ticks 1..steps; the frontier mass remains separate."""
    _nat(steps); verify_peak_kernel(packet, kernel)
    live = [F(0)]*len(kernel.states); live[0] = F(1)
    out = []
    for _ in range(steps):
        nxt = [F(0)]*len(live); hit = frontier = F(0)
        for s, t, mass in kernel.arcs:
            value = live[s]*mass
            if t == HIT:
                hit += value
            elif t == FRONTIER:
                frontier += value
            else:
                nxt[t] += value
        out.append((hit, frontier)); live = nxt
    return tuple(out)


def killed_symmetric_peak(continuation: F | int, threshold: int) -> F:
    """P(max |debt| >= m) for +/-1 steps with mass s/2 each and killing 1-s.

    Returns 1/T_m(1/s) via the exact Chebyshev recurrence. This is a declared
    model, not a universal heartbeat law. At s=1 every finite threshold is hit.
    """
    if type(continuation) not in (int, F) or not 0 <= continuation <= 1:
        raise ValueError('exact rational continuation in [0,1] required')
    if _nat(threshold) < 1:
        raise ValueError('positive threshold required')
    s = F(continuation)
    if s == 0:
        return F(0)
    a, b = F(1), 1/s
    for _ in range(1, threshold):
        a, b = b, 2*b/s-a
    return 1/b
