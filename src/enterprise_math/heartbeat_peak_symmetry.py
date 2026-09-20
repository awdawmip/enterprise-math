"""Certified orbit-first discovery of native-X6 carry-peak observations.

A finite native-axis/control permutation group is checked against the *whole*
projective linear transition law before lattice exploration. Only orbit
representatives are expanded. This is a frozen-law HIT/UNKNOWN observer, not a
codec for labeled spatial trajectories or a license for arbitrary reweighting.
The certificate remains valid at every threshold, but its finite automaton does
not. No changes to P000, existing BRC atoms, or native coordinate dimensions.
"""
from __future__ import annotations
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb

from .brc_transport import eye, matrix, mm, inv
from .brc_control_port import ControlPacket
from .heartbeat_carry_peak import (PeakState, PeakEdge, _atoms,
    projective_lattice_key, HIT, UNKNOWN)
from .heartbeat_switching_carry import _prime, _nat, linear_carry_spread
from .heartbeat_peak_quotient import PeakChain, passage_law

N = 6
IDENTITY_AXES = tuple(range(N))


def _perm(values, n):
    values = tuple(values)
    if len(values) != n or any(type(x) is not int for x in values) or set(values) != set(range(n)):
        raise ValueError('a genuine permutation of the declared domain is required')
    return values


@dataclass(frozen=True, order=True)
class AxisControlSymmetry:
    axes: tuple[int, ...]
    controls: tuple[int, ...]

    def __post_init__(self):
        object.__setattr__(self, 'axes', _perm(self.axes, N))
        object.__setattr__(self, 'controls', _perm(self.controls, len(self.controls)))
        if not self.controls:
            raise ValueError('nonempty control domain required')

    def then(self, later):
        if len(self.controls) != len(later.controls):
            raise ValueError('control domains differ')
        return AxisControlSymmetry(tuple(later.axes[i] for i in self.axes),
                                   tuple(later.controls[i] for i in self.controls))

    def inverse(self):
        return AxisControlSymmetry(tuple(self.axes.index(i) for i in range(N)),
            tuple(self.controls.index(i) for i in range(len(self.controls))))


def _group(generators, state_count, limit):
    identity = AxisControlSymmetry(IDENTITY_AXES, tuple(range(state_count)))
    generators = tuple(generators)
    for g in generators:
        if not isinstance(g, AxisControlSymmetry) or len(g.controls) != state_count:
            raise ValueError('symmetry control domain does not match packet')
    found, queue = {identity}, deque([identity])
    while queue:
        g = queue.popleft()
        for h in generators:
            k = g.then(h)
            if k not in found:
                if len(found) >= limit:
                    raise ValueError('finite symmetry group exceeds explicit group limit')
                found.add(k); queue.append(k)
    return tuple(sorted(found))


@lru_cache(maxsize=4096)
def _projective_action(a):
    # Equality up to rational scalar, NOT equality just of Smith factors.
    pivot = next(x for row in a for x in row if x)
    return tuple(tuple(x/pivot for x in row) for row in a)


def _conjugate(a, axes):
    inverse = tuple(axes.index(i) for i in range(N))
    return tuple(tuple(a[inverse[i]][inverse[j]] for j in range(N)) for i in range(N))


def _law(atoms, g=None):
    row = defaultdict(F)
    for source, target, weight, a, count in atoms:
        if g is not None:
            source, target = g.controls[source], g.controls[target]
            a = _conjugate(a, g.axes)
        row[(source, target, _projective_action(a))] += weight*count
    return dict(row)


@dataclass(frozen=True)
class SymmetryCertificate:
    packet_digest: str
    generators: tuple[AxisControlSymmetry, ...]
    elements: tuple[AxisControlSymmetry, ...]
    state_count: int
    checked_generator_atoms: int
    group_limit: int


def certify_peak_symmetry(packet: ControlPacket, generators=(), *, group_limit=4096):
    """Sufficient all-lattice equivariance certificate, independent of threshold.

    Checks mass of every (source, target, projective-linear-action) atom class.
    Scalar expansion and affine offsets are outside this peak-only observer.
    Individual original atom labels are NOT fixed by the symmetry.
    """
    atoms = _atoms(packet)
    limit = _nat(group_limit)
    if limit < 1:
        raise ValueError('positive group limit required')
    generators = tuple(generators)
    elements = _group(generators, packet.state_count, limit)
    original = _law(atoms)
    for g in generators:
        changed = _law(atoms, g)
        if changed != original:
            keys = sorted(set(original) | set(changed))
            key = next(k for k in keys if original.get(k, F(0)) != changed.get(k, F(0)))
            raise ValueError('symmetry law mismatch at source/target '+str(key[:2])+
                             ': '+str(original.get(key,F(0)))+' != '+str(changed.get(key,F(0))))
    return SymmetryCertificate(sha256(repr(packet).encode()).hexdigest(), generators,
        elements, packet.state_count, len(atoms)*len(generators), limit)


def verify_peak_symmetry(packet, certificate):
    if not isinstance(certificate, SymmetryCertificate):
        raise TypeError('SymmetryCertificate required')
    if certify_peak_symmetry(packet, certificate.generators,
                             group_limit=certificate.group_limit) != certificate:
        raise ValueError('symmetry certificate content or source changed')
    return True


def retained_symmetries(packet, parent_certificate):
    """Compute the exact kernel stabilizer inside a previously listed group.

    The returned group is recertified for this packet. A changed law is never
    silently forced back to the old symmetric law. Returns (certificate, order).
    """
    if packet.state_count != parent_certificate.state_count:
        raise ValueError('same control domain required')
    parent = _group(parent_certificate.generators, packet.state_count,
                    parent_certificate.group_limit)
    if parent != parent_certificate.elements:
        raise ValueError('invalid parent group')
    atoms = _atoms(packet); law = _law(atoms)
    keep = tuple(g for g in parent if _law(atoms,g) == law)
    generators = []
    generated = set(_group((),packet.state_count,len(parent)))
    for g in keep:
        if g not in generated:
            generators.append(g)
            generated = set(_group(generators,packet.state_count,len(parent)))
    if generated != set(keep):
        raise ArithmeticError('kernel stabilizer failed closure')
    cert = certify_peak_symmetry(packet,generators,group_limit=len(parent))
    return cert, len(keep)


def _frozen_controls(packet, prime):
    """Closed controls whose every action has zero carry spread forever."""
    atoms = _atoms(packet); keep = set(range(packet.state_count))
    while True:
        fresh = {s for s in keep if all(t in keep and linear_carry_spread(a,prime)==0
                 for u,t,_w,a,_n in atoms if u==s)}
        if fresh == keep:
            return frozenset(keep)
        keep = fresh


def _permuted_lattice(lattice, axes, prime):
    # A right column permutation leaves a diagonal lattice unchanged; use this
    # proved diagonal fast path, not a Smith-spectrum shortcut on general input.
    inverse = tuple(axes.index(i) for i in range(N))
    if all(not lattice[i][j] for i in range(N) for j in range(N) if i!=j):
        values = tuple(lattice[i][i] for i in inverse)
        return tuple(tuple(values[i] if i==j else 0 for j in range(N)) for i in range(N))
    return projective_lattice_key(tuple(lattice[i] for i in inverse), prime)


class _Canonicalizer:
    def __init__(self, certificate, prime, frozen):
        self.certificate, self.prime, self.frozen = certificate, prime, frozen
        self.cache = {}; self.images = 0
        self.identity = projective_lattice_key(eye(N),prime)

    def __call__(self, state):
        if state in self.cache:
            return self.cache[state]
        if state.control in self.frozen:
            result = PeakState(min(g.controls[state.control] for g in self.certificate.elements),
                               self.identity)
        else:
            candidates=[]
            for g in self.certificate.elements:
                candidates.append((g.controls[state.control],
                    _permuted_lattice(state.lattice,g.axes,self.prime)))
            self.images += len(candidates)
            c,lattice = min(candidates)
            result = PeakState(c,lattice)
        self.cache[state] = result
        return result


@dataclass(frozen=True)
class OrbitPeakAutomaton:
    prime: int
    threshold: int
    certificate: SymmetryCertificate
    initial_control: int
    duration: int
    status: str
    states: tuple[PeakState, ...]
    edges: tuple[PeakEdge, ...]
    initial_hit: bool
    state_budget: int
    frozen_controls: tuple[int, ...]
    canonicalized_successors: int
    orbit_images_examined: int
    expanded_representatives: int

    @property
    def complete(self):
        return self.status == 'COMPLETE'


def compile_orbit_peak(packet, prime, threshold, certificate, *,
                       initial_control=0, max_states=10000, collapse_frozen=True):
    """Discover only certified orbit representatives; never build the full graph.

    All outgoing atoms of each representative are retained with their original
    weights/counts. They are representative-frame annotations, NOT a globally
    unchanged literal action word. Orbit cardinalities are never multiplied
    into probabilities. Incomplete orbit discoveries keep UNKNOWN separately.
    """
    verify_peak_symmetry(packet,certificate)
    p,r,cap = _prime(prime),_nat(threshold),_nat(max_states)
    if not cap or type(initial_control) is not int or not 0 <= initial_control < packet.state_count:
        raise ValueError('positive budget and valid initial control required')
    if type(collapse_frozen) is not bool:
        raise TypeError('collapse_frozen must be bool')
    frozen = _frozen_controls(packet,p) if collapse_frozen else frozenset()
    canonical = _Canonicalizer(certificate,p,frozen)
    if r==0:
        return OrbitPeakAutomaton(p,r,certificate,initial_control,packet.duration,'COMPLETE',(),(),
                                  True,cap,tuple(sorted(frozen)),0,0,0)
    seed = canonical(PeakState(initial_control,canonical.identity))
    states, index, edges, todo = [seed],{seed:0},[],deque([0])
    outgoing = [[] for _ in range(packet.state_count)]
    for atom_id,atom in enumerate(_atoms(packet)):
        outgoing[atom[0]].append((atom_id,atom))
    partial=False; transitions={}
    while todo:
        source=todo.popleft(); state=states[source]
        for atom_id,(_s,t,w,a,count) in outgoing[state.control]:
            if state.control in frozen:
                successor=canonical(PeakState(t,canonical.identity))
            else:
                key=(state.lattice,a)
                if key not in transitions:
                    moved=mm(a,matrix(state.lattice))
                    transitions[key]=None if linear_carry_spread(moved,p)>=r else projective_lattice_key(moved,p)
                lattice=transitions[key]
                successor=None if lattice is None else canonical(PeakState(t,lattice))
            if successor is None:
                target=HIT
            elif successor in index:
                target=index[successor]
            elif len(states)<cap:
                target=len(states); index[successor]=target
                states.append(successor); todo.append(target)
            else:
                target=UNKNOWN; partial=True
            edges.append(PeakEdge(source,target,atom_id,w,count))
    return OrbitPeakAutomaton(p,r,certificate,initial_control,packet.duration,
        'STATE_LIMIT' if partial else 'COMPLETE',tuple(states),tuple(edges),False,cap,
        tuple(sorted(frozen)),len(canonical.cache),canonical.images,len(states))


def verify_orbit_peak(packet, automaton):
    """Reconstruct only the reduced discovery and compare every delivered field."""
    if not isinstance(automaton,OrbitPeakAutomaton):
        raise TypeError('OrbitPeakAutomaton required')
    wanted=compile_orbit_peak(packet,automaton.prime,automaton.threshold,automaton.certificate,
        initial_control=automaton.initial_control,max_states=automaton.state_budget,
        collapse_frozen=bool(automaton.frozen_controls))
    if wanted!=automaton:
        raise ValueError('orbit automaton payload differs from certified discovery')
    return True


def orbit_peak_chain(packet, automaton):
    """Reuse the inherited PeakChain probability/first-passage interfaces.

    Do not attach representative-frame atom ids as global literal channels.
    They remain available in automaton.edges for audit, but channels=() here.
    """
    verify_orbit_peak(packet,automaton)
    if automaton.initial_hit:
        return PeakChain(((F(1),),),('HIT',),duration=packet.duration)
    n=len(automaton.states); kernel=[[F(0)]*(n+2) for _ in range(n+2)]
    for e in automaton.edges:
        target=n if e.target==HIT else n+1 if e.target==UNKNOWN else e.target
        kernel[e.source][target]+=e.mass
    kernel[n][n]=kernel[n+1][n+1]=F(1)
    return PeakChain(tuple(tuple(row) for row in kernel),('SAFE',)*n+('HIT','UNKNOWN'),
        duration=packet.duration,complete=automaton.complete,
        source_digest=sha256(repr(automaton).encode()).hexdigest())


def symmetric_depth_state_counts(threshold):
    """Single-axis increments on six exchangeable axes; one safe stopped class.

    Active oriented states=R^6-(R-1)^6; S6 orbits=binom(R+4,5).
    These are reachable boundary states, not bytes or original path identities.
    """
    r=_nat(threshold)
    if not r:
        raise ValueError('positive threshold required')
    return {'oriented_active':r**6-(r-1)**6,'orbit_active':comb(r+4,5),
            'orbit_safe_with_stop':comb(r+4,5)+1}


def shared_stop_defect_bound(epsilon, stop_probability, horizon=None):
    """Coupling bound for a perturbed law versus a certified symmetric law.

    Premises supplied by the caller: at any common pre-hit state row-TV<=eps;
    the two laws share a terminal no-change decision of probability>=eta.
    Such premises are separate from a symmetry certificate. Signed law defect
    is analytic data, never negative BRC mass. Bound=eps/(eta+eps) at infinity.
    """
    if any(isinstance(x,bool) or not isinstance(x,(int,F)) for x in (epsilon,stop_probability)):
        raise TypeError('exact probabilities required')
    eps,eta=F(epsilon),F(stop_probability)
    if not 0<=eps<=1 or not 0<=eta<=1 or eps+eta>1:
        raise ValueError('invalid shared-stop/TV bounds')
    if horizon is not None:
        horizon=_nat(horizon)
    if not eps:
        return F(0)
    if horizon is None:
        return eps/(eps+eta)
    return eps*(1-(1-eta-eps)**horizon)/(eta+eps)


@dataclass(frozen=True)
class StoppedLawComparison:
    reference_digest: str
    perturbed_digest: str
    prime: int
    stop_control: int
    row_total_variations: tuple[F, ...]
    common_stop: F
    max_defect: F
    all_time_risk_error: F


def certify_stopped_law_comparison(reference, perturbed, prime, *, stop_control):
    """Check the shared-stop coupling premises from two actual BRC packets.

    Same control domain and monitored duration. STOP must be closed and every
    action there must preserve linear carry. Entry into STOP must also preserve
    current carry. Remaining rows are compared by (target, projective action).
    No kernel or branch weight is changed; the output is an error certificate,
    not exact equivalence and not the value of the perturbed risk itself.
    """
    p=_prime(prime)
    if (reference.state_count,reference.duration)!=(perturbed.state_count,perturbed.duration):
        raise ValueError('same control domain and monitored duration required')
    n=reference.state_count
    if type(stop_control) is not int or not 0<=stop_control<n:
        raise ValueError('valid declared stop control required')
    def rows(packet):
        out=[defaultdict(F) for _ in range(n)]
        for s,t,w,a,count in _atoms(packet):
            if s==stop_control and (t!=stop_control or linear_carry_spread(a,p)!=0):
                raise ValueError('declared stop is not closed and carry-preserving')
            if t==stop_control:
                if linear_carry_spread(a,p)!=0:
                    raise ValueError('entry action may hit before stopping')
                key=('STOP',)
            else:
                key=('ACTION',t,_projective_action(a))
            out[s][key]+=w*count
        return out
    left,right=rows(reference),rows(perturbed)
    tv=tuple(sum((abs(left[i].get(k,F(0))-right[i].get(k,F(0)))
                  for k in set(left[i])|set(right[i])),F(0))/2 for i in range(n))
    active=[i for i in range(n) if i!=stop_control]
    eta=min((min(left[i].get(('STOP',),F(0)),right[i].get(('STOP',),F(0)))
             for i in active),default=F(1))
    eps=max(tv,default=F(0))
    return StoppedLawComparison(sha256(repr(reference).encode()).hexdigest(),
        sha256(repr(perturbed).encode()).hexdigest(),p,stop_control,tv,eta,eps,
        shared_stop_defect_bound(eps,eta))
