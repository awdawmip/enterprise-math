"""Positive-mass BRC transporters with exact one-digit congruence repair.

Input is two frozen ControlPackets, not untyped numerical matrix propagation.
The observer forgets individual atom labels, affine translations and common
p-scale, but retains target controls and each linear germ's positive mass.
Fixed atom matching is replaced by a positive coupling with exact marginals.
All coupling supports use ONE shared frame. Their projected next-digit repair
union is an affine space, by the finite projective-kernel transporter theorem.

Only one guarded digit is solved symbolically. Support enumeration has an
explicit budget. Partial affine output is sound, not necessarily complete.
Repeated-block models are a declared restriction of six-axis frames, not a
change to the Heartbeat World dimensional definition. No physical attribution.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from hashlib import sha256
from .brc_control_port import ControlPacket
from .brc_transport import matrix, mm, inv, sm, eye
from .heartbeat_congruence_lift import (
    GermLiftProblem, GermLiftCertificate, LinearLiftSpace,
    lift_germ_seed, solve_modular_linear, _normalize_frame, _mod,
)
from .heartbeat_switching_carry import _prime, _minimum, linear_carry_spread
from .heartbeat_peak_orbits import _row_equal


def _nat(x, positive=False):
    if type(x) is not int or x < int(positive):
        raise ValueError('nonnegative/positive integer budget required')
    return x


def _repeated_block(a, size):
    if size not in (1, 2, 3, 6):
        raise ValueError('block size must divide native dimension six')
    b=matrix([row[:size] for row in a[:size]])
    if a != _embed(b):
        raise ValueError('action not in declared identical-block subalgebra')
    return b


def _embed(a):
    n=len(a)
    return matrix([[a[i % n][j % n] if i//n==j//n else 0
                    for j in range(6)] for i in range(6)])


@dataclass(frozen=True)
class WeightedGermAtom:
    """An exact histogram entry: weight and multiplicity never become lift count."""
    source: int
    target: int
    entry: int
    weight: F
    multiplicity: int
    action: tuple
    translation: tuple

    @property
    def mass(self):
        return self.weight*self.multiplicity


@dataclass(frozen=True)
class WeightedLiftProblem:
    left_packet: ControlPacket
    right_packet: ControlPacket
    prime: int
    block_size: int
    left: tuple[WeightedGermAtom, ...]
    right: tuple[WeightedGermAtom, ...]
    guard: int

    @classmethod
    def from_control_packets(cls, left, right, prime, *, block_size=6):
        if not isinstance(left,ControlPacket) or not isinstance(right,ControlPacket):
            raise TypeError('actual ControlPacket carriers required')
        if (left.state_count,left.start,left.duration)!=(right.state_count,right.start,right.duration):
            raise ValueError('identical control and time ports required')
        p=_prime(prime)
        def atoms(packet):
            out=[]
            for source,target,hist in packet.blocks:
                for i,(weight,action,count) in enumerate(hist.entries):
                    if any(x.denominator!=1 for row in action.a for x in row):
                        raise ValueError('integer nonsingular native action required')
                    a=_repeated_block(action.a,block_size)
                    inv(a)
                    out.append(WeightedGermAtom(source,target,i,weight,count,a,action.b))
            return tuple(out)
        a,b=atoms(left),atoms(right)
        if not a or not b:
            raise ValueError('nonempty positive-mass kernels required')
        guard=max(linear_carry_spread(x.action,p) for x in a+b)
        return cls(left,right,p,block_size,a,b,guard)

    @property
    def digest(self):
        return sha256(repr(self).encode()).hexdigest()

    def normalize_seed(self,frame,precision):
        m=_nat(precision,True)
        if len(frame)!=self.block_size:
            raise ValueError('seed frame does not have declared block size')
        return _normalize_frame(frame,self.prime,m+self.guard)

    def primitive(self,atom):
        return sm(F(self.prime)**(-_minimum(atom.action,self.prime)),atom.action)

    def edge_scalar(self,i,j,frame,precision):
        """Existing germ law, with scalar read from a unit entry of the frame."""
        a,b=self.left[i],self.right[j]
        if (a.source,a.target)!=(b.source,b.target):
            return None
        s,pivot=self.normalize_seed(frame,precision)
        s=matrix(s); n=self.block_size; p=self.prime
        v=mm(mm(inv(self.primitive(b)),s),self.primitive(a))
        if _minimum(v,p)<0:
            return None
        u=_mod(v[pivot//n][pivot % n]/s[pivot//n][pivot % n],p**precision)
        if u % p==0:
            return None
        if any(_mod(v[x][y]-u*s[x][y],p**precision)
               for x in range(n) for y in range(n)):
            return None
        return u

    def allowed_edges(self,frame,precision):
        return tuple((i,j,self.edge_scalar(i,j,frame,precision))
                     for i in range(len(self.left)) for j in range(len(self.right))
                     if self.edge_scalar(i,j,frame,precision) is not None)

    def row_certificate(self,frame,precision):
        """Invoke inherited full mass-per-germ row checker on all six axes."""
        s,_=self.normalize_seed(frame,precision);s=_embed(s);si=inv(s)
        for source in range(self.left_packet.state_count):
            left=[(x.target,x.mass,mm(mm(s,_embed(x.action)),si))
                  for x in self.left if x.source==source]
            right=[(x.target,x.mass,_embed(x.action))
                   for x in self.right if x.source==source]
            if not _row_equal(left,right,self.prime,precision+1,'threshold'):
                return False
        return True


@dataclass(frozen=True)
class PositiveTransport:
    left_mass: tuple[F,...]
    right_mass: tuple[F,...]
    entries: tuple[tuple[int,int,F],...]

    def verify(self,allowed):
        allowed=set(allowed)
        if len({(i,j) for i,j,_ in self.entries})!=len(self.entries):
            raise ValueError('duplicate transport edges')
        if any((i,j) not in allowed or q<=0 for i,j,q in self.entries):
            raise ValueError('positive transport on allowed germ edges required')
        if tuple(sum((q for a,_,q in self.entries if a==i),F(0))
                 for i in range(len(self.left_mass)))!=self.left_mass:
            raise ValueError('left marginal mismatch')
        if tuple(sum((q for _,b,q in self.entries if b==j),F(0))
                 for j in range(len(self.right_mass)))!=self.right_mass:
            raise ValueError('right marginal mismatch')
        return True


def _forest_transport(left,right,edges):
    """Unique positive coupling on a forest; leaf elimination is exact."""
    n,m=len(left),len(right);parent=list(range(n+m))
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for i,j in edges:
        a,b=root(i),root(n+j)
        if a==b:
            return None
        parent[a]=b
    adj=[set() for _ in range(n+m)]
    for k,(i,j) in enumerate(edges):
        adj[i].add(k);adj[n+j].add(k)
    if any(not a for a in adj):
        return None
    debt=list(left)+list(right);remaining=set(range(len(edges)));flow={}
    while remaining:
        leaf=next((x for x in range(n+m) if len(adj[x])==1),None)
        if leaf is None:
            return None
        k=next(iter(adj[leaf]));i,j=edges[k];other=n+j if leaf==i else i
        value=debt[leaf]
        if value<=0 or value>debt[other]:
            return None
        flow[k]=value;debt[leaf]=F(0);debt[other]-=value
        adj[leaf].remove(k);adj[other].remove(k);remaining.remove(k)
    if any(debt):
        return None
    return PositiveTransport(tuple(left),tuple(right),tuple((i,j,flow[k]) for k,(i,j) in enumerate(edges)))


def _affine_hull(spaces,n,p):
    """Projection plus exact affine hull, using the inherited F_p solver.

    Sound for this transporter fibre by the prime-field congruence-kernel
    theorem; NOT a generic rule for arbitrary unions of affine spaces.
    """
    nonempty=[s for s in spaces if s.count]
    if not nonempty:
        return None
    origin=nonempty[0].particular[:n]
    directions=[]
    for s in nonempty:
        directions.append(tuple((a-b)%p for a,b in zip(s.particular[:n],origin)))
        directions.extend(v[:n] for v in s.basis)
    annihilator=solve_modular_linear(directions or [(0,)*n],
                                     (0,)*max(1,len(directions)),p).basis
    rows=annihilator or ((0,)*n,)
    rhs=tuple(sum(a*b for a,b in zip(row,origin))%p for row in rows)
    return solve_modular_linear(rows,rhs,p)


@dataclass(frozen=True)
class TransportLiftPiece:
    transport: PositiveTransport
    lift: GermLiftCertificate


@dataclass(frozen=True)
class WeightedLiftResult:
    problem: WeightedLiftProblem
    seed_frame: tuple
    precision: int
    status: str
    support_checks: int
    allowed_edges: tuple
    pieces: tuple[TransportLiftPiece,...]
    repairs: LinearLiftSpace | None

    @property
    def certified_frame_count(self):
        return 0 if self.repairs is None else self.repairs.count

    @property
    def is_complete(self):
        return self.status in ('COMPLETE','NO_LIFTS')

    def frame(self,parameters=()):
        if self.repairs is None:
            raise ValueError('no certified frame family; inspect completeness status')
        z=self.repairs.point(parameters);n=self.problem.block_size
        step=self.problem.prime**(self.precision+self.problem.guard)
        return tuple(tuple(self.seed_frame[i][j]+step*z[n*i+j] for j in range(n))
                     for i in range(n))

    def all_frames(self,*,limit=4096):
        _nat(limit)
        if self.certified_frame_count>limit:
            raise ValueError('FRAME_LIMIT: affine family retained, not enumerated')
        if self.repairs is None:
            return ()
        return tuple(self.frame(c) for c in product(range(self.problem.prime),repeat=len(self.repairs.basis)))

    def verify(self):
        for piece in self.pieces:
            piece.transport.verify([(i,j) for i,j,_ in self.allowed_edges])
            piece.lift.verify()
        if self.repairs is not None:
            self.repairs.verify()
            if not self.problem.row_certificate(self.frame((0,)*len(self.repairs.basis)),self.precision+1):
                raise ValueError('affine origin fails inherited BRC row certificate')
        # Reconstruct the exact recorded support prefix. A limit is not a no-lift.
        repeated=lift_weighted_kernel(self.problem,self.seed_frame,self.precision,
                                      max_support_checks=self.support_checks)
        if repeated!=self:
            raise ValueError('altered or incomplete weighted-lift certificate')
        return True


def lift_weighted_kernel(problem,frame,precision,*,max_support_checks=20000):
    """Complete within a fixed seed fibre if all finite forest supports finish.

    Classical coupling existence is used as an exact typed positive BRC
    extension. Candidate repairs are not sampled, original atoms are not split
    as physical operations, and transports are witnesses rather than weights
    on the repair space. All equations in one support share the same frame.
    """
    if not isinstance(problem,WeightedLiftProblem):
        raise TypeError('typed WeightedLiftProblem required')
    if WeightedLiftProblem.from_control_packets(problem.left_packet,problem.right_packet,problem.prime,block_size=problem.block_size)!=problem:
        raise ValueError('problem has been altered relative to original BRC carriers')
    cap=_nat(max_support_checks);m=_nat(precision,True)
    s,_=problem.normalize_seed(frame,m)
    if not problem.row_certificate(s,m):
        raise ValueError('seed is not a full weighted-germ transporter at this depth')
    allowed=problem.allowed_edges(s,m); scalars={(i,j):u for i,j,u in allowed}
    edges=tuple(scalars);left=tuple(a.mass for a in problem.left);right=tuple(a.mass for a in problem.right)
    pieces=[];checked=0;complete=True
    for size in range(max(len(left),len(right)),min(len(edges),len(left)+len(right)-1)+1):
        for support in combinations(edges,size):
            if checked==cap:
                complete=False;break
            checked+=1
            t=_forest_transport(left,right,support)
            if t is None:
                continue
            t.verify(edges)
            fixed=GermLiftProblem.build([problem.left[i].action for i,j in support],
                                       [problem.right[j].action for i,j in support],problem.prime)
            if fixed.guard!=problem.guard:
                raise ArithmeticError('support must cover all positive atoms and global guard')
            seed=fixed.seed(s,[scalars[i,j] for i,j in support],m)
            pieces.append(TransportLiftPiece(t,lift_germ_seed(fixed,seed)))
        if not complete:
            break
    repairs=_affine_hull([p.lift.space for p in pieces],problem.block_size**2,problem.prime)
    status=('COMPLETE' if repairs is not None else 'NO_LIFTS') if complete else 'SUPPORT_LIMIT'
    return WeightedLiftResult(problem,s,m,status,checked,allowed,tuple(pieces),repairs)
