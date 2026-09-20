"""Certified on-the-fly symmetry reduction of Heartbeat World peak lattices.

Fixed positive probability law; oriented X6 lattices modulo scalar homothety.
A finite frame group acts on control ports and the standard p-adic lattice.
Certificates concern the declared peak threshold, not primitive rotations,
spatial paths, original atom words, or arbitrary future probability changes.

This EXTENDS the existing T0_BRC peak compiler. Its canonical lattice codec,
exact matrix operations, PeakChain, probability star and first-passage tools
are reused unchanged. No native fractional Cell motion is introduced.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256

from .brc_transport import Matrix, matrix, eye, inv, mm, sm
from .brc_control_port import ControlPacket
from .heartbeat_switching_carry import _prime, _nat, _minimum, linear_carry_spread
from .heartbeat_carry_peak import (PeakState, PeakEdge, HIT, UNKNOWN, _atoms,
                                   projective_lattice_key)
from .heartbeat_peak_quotient import PeakChain

N = 6
I = eye(N)


def _digest(obj) -> str:
    return sha256(repr(obj).encode('utf-8')).hexdigest()


def _square(a) -> Matrix:
    a = matrix(a)
    if len(a) != N or len(a[0]) != N:
        raise ValueError('six-dimensional matrix required')
    inv(a)
    return a


def _local_unit(a, p):
    return _minimum(a, p) >= 0 and _minimum(inv(a), p) >= 0


@lru_cache(maxsize=32768)
def _germ(a: Matrix, b: Matrix, p: int, threshold: int, mode: str) -> bool:
    # A L and B L are homothetic for every lattice of spread < threshold.
    relative = mm(inv(b), a)
    diagonal = relative[0][0]
    if diagonal and relative == sm(diagonal, I):
        return True
    if mode == 'exact':
        return False
    depth = threshold - 1
    if depth == 0:
        normalized = sm(F(p)**(-_minimum(relative, p)), relative)
        return _local_unit(normalized, p)
    if not diagonal:
        return False
    normalized = sm(1/diagonal, relative)
    defect = tuple(tuple(normalized[i][j]-I[i][j] for j in range(N)) for i in range(N))
    return (_local_unit(normalized, p)
            and (not any(x for row in defect for x in row) or _minimum(defect, p) >= depth))


def threshold_action_equivalent(a, b, prime: int, threshold: int, *, mode='threshold') -> bool:
    """Sufficient exact identity of action on EVERY safe projective lattice.

    E = scalar^-1 B^-1 A in GL_6(Z_p), E == I mod p^(R-1) suffices for R>=2.
    For R=1 all safe lattices are the standard homothety class; local GL is
    sufficient. False rejects this sufficient test, not all possible equivalences.
    The raw matrices are NOT rounded and the returned law is not asymptotic.
    """
    p, r = _prime(prime), _nat(threshold)
    if r < 1 or mode not in ('exact', 'threshold'):
        raise ValueError('positive threshold and exact/threshold mode required')
    return _germ(_square(a), _square(b), p, r, mode)


@dataclass(frozen=True)
class Frame:
    controls: tuple[int, ...]
    basis: Matrix

    def __post_init__(self):
        c = tuple(self.controls)
        if not c or any(type(x) is not int for x in c) or set(c) != set(range(len(c))):
            raise ValueError('control permutation required')
        object.__setattr__(self, 'controls', c)
        object.__setattr__(self, 'basis', _square(self.basis))

    def after(self, earlier: 'Frame') -> 'Frame':
        if len(self.controls) != len(earlier.controls):
            raise ValueError('control layouts differ')
        return Frame(tuple(self.controls[x] for x in earlier.controls), mm(self.basis, earlier.basis))


@dataclass(frozen=True)
class FiniteFrameGroup:
    prime: int
    control_count: int
    frames: tuple[Frame, ...]

    @classmethod
    def generated(cls, prime: int, control_count: int, generators=(), *, max_group=1024):
        p, count, cap = _prime(prime), _nat(control_count), _nat(max_group)
        if count == 0 or cap == 0:
            raise ValueError('positive control count and group budget required')
        identity = Frame(tuple(range(count)), I)
        gens = tuple(generators)
        for g in gens:
            if not isinstance(g, Frame) or len(g.controls) != count or not _local_unit(g.basis, p):
                raise ValueError('frame must permute ports and preserve the standard p-lattice')
        found, todo = {identity}, deque([identity])
        while todo:
            a = todo.popleft()
            for g in gens:
                product = g.after(a)
                if product not in found:
                    if len(found) == cap:
                        raise ValueError('GROUP_LIMIT: no finite-group certificate within budget')
                    found.add(product); todo.append(product)
        frames = (identity,) + tuple(sorted(found-{identity}, key=lambda g:(g.controls,g.basis)))
        return cls(p, count, frames)

    def verify(self):
        if self != FiniteFrameGroup.generated(self.prime, self.control_count,
                                              self.frames, max_group=len(self.frames)):
            raise ValueError('invalid closed finite frame group')
        return True


@dataclass(frozen=True)
class PeakSymmetryCertificate:
    packet_digest: str
    prime: int
    threshold: int
    mode: str
    group: FiniteFrameGroup
    row_comparisons: int
    scalar_safe_controls: tuple[int, ...]


def _scalar_matrix(a):
    return bool(a[0][0]) and a == sm(a[0][0], I)


def _safe_controls(packet, atoms):
    candidate = {c for c in range(packet.state_count)
                 if all(_scalar_matrix(a) for s,t,w,a,n in atoms if s == c)}
    while True:
        nxt = {c for c in candidate if all(t in candidate for s,t,w,a,n in atoms if s == c)}
        if nxt == candidate:
            return tuple(sorted(nxt))
        candidate = nxt


def _buckets(row, p, r, mode):
    buckets = []
    for target, mass, action in row:
        for k, (t, total, representative) in enumerate(buckets):
            if t == target and _germ(action, representative, p, r, mode):
                buckets[k] = (t, total+mass, representative)
                break
        else:
            buckets.append((target, mass, action))
    return buckets


def _row_equal(left, right, p, r, mode):
    a, b = _buckets(left,p,r,mode), _buckets(right,p,r,mode)
    if len(a) != len(b):
        return False
    used = set()
    for target, mass, action in a:
        for j, (t, w, representative) in enumerate(b):
            if j not in used and t == target and w == mass and _germ(action,representative,p,r,mode):
                used.add(j); break
        else:
            return False
    return True


def certify_peak_symmetry(packet: ControlPacket, group: FiniteFrameGroup,
                          threshold: int, *, mode='exact') -> PeakSymmetryCertificate:
    """Check kernel equivariance BEFORE constructing any reachable lattice graph.

    Channels may permute or coalesce; compare total original weight*count.
    Thus this certificate is fixed-law positive-mass, NOT atom-word equivalence.
    Every original atom is retained on representative rows during compilation.
    """
    if not isinstance(packet,ControlPacket) or not isinstance(group,FiniteFrameGroup):
        raise TypeError('ControlPacket and FiniteFrameGroup required')
    group.verify()
    r = _nat(threshold)
    if r < 1 or mode not in ('exact','threshold') or packet.state_count != group.control_count:
        raise ValueError('invalid threshold, mode or port layout')
    atoms, p = _atoms(packet), group.prime
    rows = {s: [(t,w*n,a) for c,t,w,a,n in atoms if c==s] for s in range(packet.state_count)}
    checks=0
    for frame in group.frames:
        si = inv(frame.basis)
        for source in range(packet.state_count):
            transformed = [(frame.controls[t],w,mm(mm(frame.basis,a),si)) for t,w,a in rows[source]]
            if not _row_equal(transformed,rows[frame.controls[source]],p,r,mode):
                raise ValueError(f'UNPROVED_SYMMETRY at source {source}; preserve orientation or refine group')
            checks+=1
    return PeakSymmetryCertificate(_digest(packet),p,r,mode,group,checks,_safe_controls(packet,atoms))


@dataclass(frozen=True)
class OrbitPeakAutomaton:
    certificate: PeakSymmetryCertificate
    duration: int
    initial_control: int
    states: tuple[PeakState, ...]
    edges: tuple[PeakEdge, ...]
    initial_hit: bool
    complete: bool
    max_states: int
    collapse_safe: bool
    expanded_states: int
    atom_successors: int
    canonical_candidates: int


def _canonical_state(control, lattice, cert, collapse_safe):
    # control=-3 is a SAFE observation sink, never a native control or Cell.
    if collapse_safe and control in cert.scalar_safe_controls:
        return PeakState(-3,tuple(tuple(int(x) for x in row) for row in I))
    candidates = [PeakState(g.controls[control],
                  projective_lattice_key(mm(g.basis,matrix(lattice)),cert.prime))
                  for g in cert.group.frames]
    return min(candidates,key=lambda s:(s.control,s.lattice))


def compile_orbit_peak(packet: ControlPacket, certificate: PeakSymmetryCertificate, *,
                       initial_control=0, max_states=10000, collapse_safe=True) -> OrbitPeakAutomaton:
    """Generate only canonical orbit representatives. Never builds the full graph.

    Safe scalar controls are optionally merged using a separate global proof.
    Budgets refer to retained representatives, not raw orbit cardinality. Each
    omitted orbit routes to UNKNOWN; it never becomes a safe stopping state.
    """
    expected = certify_peak_symmetry(packet,certificate.group,certificate.threshold,mode=certificate.mode)
    if expected != certificate:
        raise ValueError('source/certificate mismatch')
    cap = _nat(max_states)
    if cap < 1 or type(initial_control) is not int or not 0 <= initial_control < packet.state_count:
        raise ValueError('invalid initial control or positive state budget')
    if type(collapse_safe) is not bool:
        raise TypeError('collapse_safe must be bool')
    atoms = _atoms(packet)
    outgoing = [[] for _ in range(packet.state_count)]
    for j,atom in enumerate(atoms):
        outgoing[atom[0]].append((j,atom))
    canonical_calls = 0
    @lru_cache(maxsize=32768)
    def canonical(c,l):
        nonlocal canonical_calls
        if not (collapse_safe and c in certificate.scalar_safe_controls):
            canonical_calls += len(certificate.group.frames)
        return _canonical_state(c,l,certificate,collapse_safe)
    seed = canonical(initial_control,projective_lattice_key(I,certificate.prime))
    states, indices, todo, edges = [seed], {seed:0}, deque([0]), []
    partial = False; expansions = successors = 0
    while todo:
        source=todo.popleft(); state=states[source]; expansions+=1
        if state.control == -3:
            edges.append(PeakEdge(source,source,-1,F(1),1)); continue
        for j,(_s,t,w,a,n) in outgoing[state.control]:
            successors+=1
            moved = mm(a,matrix(state.lattice))
            if linear_carry_spread(moved,certificate.prime) >= certificate.threshold:
                target=HIT
            else:
                lattice=projective_lattice_key(moved,certificate.prime)
                nxt=canonical(t,lattice)
                if nxt in indices:
                    target=indices[nxt]
                elif len(states)<cap:
                    target=len(states); states.append(nxt); indices[nxt]=target; todo.append(target)
                else:
                    target=UNKNOWN; partial=True
            edges.append(PeakEdge(source,target,j,w,n))
    return OrbitPeakAutomaton(certificate,packet.duration,initial_control,tuple(states),tuple(edges),False,
                              not partial,cap,collapse_safe,expansions,successors,canonical_calls)


def verify_orbit_peak(packet: ControlPacket, auto: OrbitPeakAutomaton) -> bool:
    """Revalidate the global proof and each retained state's exact successor row.

    Does not enumerate missing raw states; finite-group equivariance supplies
    that universal step. Reproducible checking is not independent formal review.
    """
    if not isinstance(auto,OrbitPeakAutomaton):
        raise TypeError('OrbitPeakAutomaton required')
    cert=auto.certificate
    if certify_peak_symmetry(packet,cert.group,cert.threshold,mode=cert.mode) != cert:
        raise ValueError('certificate/source mismatch')
    if auto.duration != packet.duration or not auto.states or len(set(auto.states))!=len(auto.states):
        raise ValueError('invalid time, empty or duplicate states')
    if len(auto.states)>auto.max_states:
        raise ValueError('state budget mismatch')
    if type(auto.initial_control) is not int or not 0<=auto.initial_control<packet.state_count:
        raise ValueError('invalid initial control')
    seed=_canonical_state(auto.initial_control,projective_lattice_key(I,cert.prime),cert,auto.collapse_safe)
    if auto.states[0]!=seed or auto.initial_hit:
        raise ValueError('wrong seed or initial-hit status')
    atoms=_atoms(packet); seen_unknown=False
    rows=[[] for _ in auto.states]
    for edge in auto.edges:
        if type(edge.source) is not int or not 0<=edge.source<len(rows):
            raise ValueError('edge source outside state set')
        rows[edge.source].append(edge)
    for i,state in enumerate(auto.states):
        if state.control == -3:
            if not auto.collapse_safe or not cert.scalar_safe_controls or rows[i] != [PeakEdge(i,i,-1,F(1),1)]:
                raise ValueError('invalid SAFE sink')
            continue
        if state != _canonical_state(state.control,state.lattice,cert,auto.collapse_safe):
            raise ValueError('noncanonical orbit state')
        if linear_carry_spread(state.lattice,cert.prime)>=cert.threshold:
            raise ValueError('unsafe representative')
        expected=[j for j,atom in enumerate(atoms) if atom[0]==state.control]
        if sorted(e.atom for e in rows[i])!=expected:
            raise ValueError('missing/duplicated representative atom')
        for e in rows[i]:
            _,t,w,a,n=atoms[e.atom]
            if (e.weight,e.multiplicity)!=(w,n):
                raise ValueError('representative branch weights changed')
            moved=mm(a,matrix(state.lattice))
            if linear_carry_spread(moved,cert.prime)>=cert.threshold:
                if e.target!=HIT: raise ValueError('HIT lost')
            elif e.target==UNKNOWN:
                seen_unknown=True
            elif not 0<=e.target<len(auto.states):
                raise ValueError('invalid safe target')
            elif auto.states[e.target] != _canonical_state(t,projective_lattice_key(moved,cert.prime),cert,auto.collapse_safe):
                raise ValueError('wrong orbit successor')
        if sum((e.mass for e in rows[i]),F(0))!=1:
            raise ValueError('probability mass lost')
    if seen_unknown == auto.complete:
        raise ValueError('wrong completeness status')
    if auto.expanded_states != len(auto.states):
        raise ValueError('invalid expansion statistics')
    return True


def orbit_observation_chain(packet, auto) -> PeakChain:
    """Reuse the existing exact first-passage chain, star and conditional tools."""
    verify_orbit_peak(packet,auto)
    n=len(auto.states); size=n+2
    rows=[[F(0)]*size for _ in range(size)]
    for e in auto.edges:
        target=n if e.target==HIT else n+1 if e.target==UNKNOWN else e.target
        rows[e.source][target]+=e.mass
    rows[n][n]=rows[n+1][n+1]=F(1)
    return PeakChain(tuple(tuple(row) for row in rows),('SAFE',)*n+('HIT','UNKNOWN'),
                     duration=auto.duration,complete=auto.complete,source_digest=_digest(auto))


def raw_to_orbit_labels(raw_states, auto) -> tuple[int,...]:
    """Testing/analysis helper; not called by on-the-fly construction."""
    lookup={s:i for i,s in enumerate(auto.states)}
    return tuple(lookup[_canonical_state(s.control,s.lattice,auto.certificate,auto.collapse_safe)]
                 for s in raw_states)


@dataclass(frozen=True)
class SymmetryRefinement:
    certificate: PeakSymmetryCertificate
    offered_group_size: int
    rejected_frames: tuple[int, ...]


def refine_peak_symmetry(packet: ControlPacket, group: FiniteFrameGroup,
                         threshold: int, *, mode='threshold') -> SymmetryRefinement:
    """Discard failing offered frames, not the research object or its residual.

    Produces the subgroup admitted by the chosen exact/threshold germ test.
    It is not a search over all frame groups, nor a proof that rejected frames
    fail every reachable-state-specific quotient. Identity always remains.
    """
    group.verify()
    r=_nat(threshold)
    if r<1 or mode not in ('exact','threshold') or packet.state_count!=group.control_count:
        raise ValueError('invalid threshold, mode or layout')
    atoms=_atoms(packet); p=group.prime
    rows={s:[(t,w*n,a) for c,t,w,a,n in atoms if c==s] for s in range(packet.state_count)}
    accepted=[]; rejected=[]
    for index,frame in enumerate(group.frames):
        si=inv(frame.basis)
        valid=all(_row_equal([(frame.controls[t],w,mm(mm(frame.basis,a),si))
                               for t,w,a in rows[s]],rows[frame.controls[s]],p,r,mode)
                  for s in range(packet.state_count))
        (accepted if valid else rejected).append(frame if valid else index)
    admitted=FiniteFrameGroup.generated(p,packet.state_count,accepted,max_group=len(accepted))
    if set(admitted.frames)!=set(accepted):
        raise ArithmeticError('admitted certificate family not closed under group composition')
    cert=certify_peak_symmetry(packet,admitted,r,mode=mode)
    return SymmetryRefinement(cert,len(group.frames),tuple(rejected))


def canonical_peak_frame(state: PeakState, group: FiniteFrameGroup) -> tuple[PeakState, Frame]:
    """Exact quotient+repair codec for the CURRENT oriented projective lattice.

    Not used for scalar SAFE sinks. Retaining the frame repairs future access
    to original directions; it does not recover common scale or past identity.
    """
    if not isinstance(state,PeakState) or not 0<=state.control<group.control_count:
        raise ValueError('ordinary control/lattice state required')
    group.verify()
    choices=[(PeakState(g.controls[state.control],
               projective_lattice_key(mm(g.basis,matrix(state.lattice)),group.prime)),g)
             for g in group.frames]
    return min(choices,key=lambda pair:(pair[0].control,pair[0].lattice,pair[1].controls,pair[1].basis))


def lift_peak_frame(representative: PeakState, frame: Frame, prime: int) -> PeakState:
    """Undo the explicitly retained finite frame on the current lattice class."""
    p=_prime(prime)
    if not isinstance(frame,Frame) or not _local_unit(frame.basis,p):
        raise ValueError('p-lattice-preserving frame required')
    if not isinstance(representative,PeakState) or not 0<=representative.control<len(frame.controls):
        raise ValueError('ordinary representative required')
    control=frame.controls.index(representative.control)
    return PeakState(control,projective_lattice_key(mm(inv(frame.basis),matrix(representative.lattice)),p))


def action_separation_threshold(a, b, prime: int) -> int | None:
    """First R where this universal congruence certificate distinguishes A,B.

    None means exactly proportional over Q. A finite answer is the cutoff of
    THIS test, not a search for a reachable distinguishing word. No raw lattice
    graph is enumerated. Exact nonproportional rational matrices separate at
    finite precision under this test.
    """
    p=_prime(prime); a,b=_square(a),_square(b)
    if _germ(a,b,p,1,'exact'):
        return None
    if not _germ(a,b,p,1,'threshold'):
        return 1
    relative=mm(inv(b),a); scale=relative[0][0]
    if not scale:
        return 2
    normalized=sm(1/scale,relative)
    if not _local_unit(normalized,p):
        return 2
    defect=tuple(tuple(normalized[i][j]-I[i][j] for j in range(N)) for i in range(N))
    depth=_minimum(defect,p)
    return max(2,depth+2)


@dataclass(frozen=True)
class SymmetryScaleProfile:
    changes: tuple[tuple[int, tuple[Frame, ...]], ...]
    final_test_threshold: int
    exact_limit_group_size: int
    pair_cutoffs_checked: int


def peak_symmetry_scale_profile(packet: ControlPacket, group: FiniteFrameGroup) -> SymmetryScaleProfile:
    """Finite algebraic breakpoints of the admitted symmetry filtration H_R.

    H_(R+1) <= H_R inside the offered finite group; eventually it equals the
    exact projective-action symmetry group. Only coefficient cutoffs are used,
    not construction of the (possibly large) threshold state spaces. This is
    not maximal reachable-state symmetry or an arbitrary nonlinear result.
    """
    group.verify(); atoms=_atoms(packet)
    if packet.state_count!=group.control_count:
        raise ValueError('control layout mismatch')
    cuts={1}; checked=0
    for g in group.frames:
        gi=inv(g.basis)
        for s,t,w,a,n in atoms:
            transformed=mm(mm(g.basis,a),gi)
            for c,d,v,b,m in atoms:
                if c==g.controls[s] and d==g.controls[t]:
                    cutoff=action_separation_threshold(transformed,b,group.prime)
                    if cutoff is not None:cuts.add(cutoff)
                    checked+=1
    changes=[]; previous=None
    for threshold in sorted(cuts):
        admitted=refine_peak_symmetry(packet,group,threshold).certificate.group.frames
        if previous is not None and not set(admitted)<=set(previous):
            raise ArithmeticError('nonmonotone admitted symmetry filtration')
        if admitted!=previous:
            changes.append((threshold,admitted)); previous=admitted
    limit=refine_peak_symmetry(packet,group,1,mode='exact').certificate.group.frames
    if previous!=limit:
        raise ArithmeticError('finite precision did not recover exact projective-action symmetry')
    return SymmetryScaleProfile(tuple(changes),max(cuts),len(limit),checked)
