"""Mass-faithful one-digit BRC symmetry lifting, without atom bijections.

Carrier: an unchanged stochastic native-X6 ControlPacket, its exact atoms,
ports and positive weight/counts. Observer: fixed-p linear carry-peak at
positive-duration arrow boundaries, not raw words, affine position or physics.
This extends the sourced guarded BRC germ-lift interface: coalesce only under
its universal-safe-lattice germ law, match PORT-MASS SIGNATURES, then solve
all compatible shared-frame constraints using its exact finite-field solver.

One seed fixes a projective frame modulo p^(m+C). Its next-layer weighted
kernel symmetries form an affine torsor in M6(F_p)/F_p I (or are empty).
Thus the affine hull of proved lifts is sound even under a matching budget;
completeness requires exhausting the compatible refined-class matchings.
Repair counts are NOT physical branch counts or BRC probability weights.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product

from .brc_control_port import ControlPacket
from .brc_transport import matrix, mm, inv, sm
from .heartbeat_carry_peak import _atoms
from .heartbeat_peak_orbits import threshold_action_equivalent
from .heartbeat_switching_carry import _prime, linear_carry_spread, _minimum
from .heartbeat_congruence_lift import (
    GermLiftProblem, GermLiftCertificate, LinearLiftSpace, lift_germ_seed,
    solve_modular_linear, verify_lifted_peak_frame, _normalize_frame, _mod)

N = 6


def _nat(x, positive=False):
    if type(x) is not int or x < int(positive):
        raise ValueError('nonnegative/positive integer required')
    return x


def _digest(packet):
    return sha256(repr(packet).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class GermMassClass:
    representative: tuple
    atom_indices: tuple[int, ...]
    port_masses: tuple  # exact (source, target, sum(weight*count))


def packet_germ_classes(packet: ControlPacket, prime: int, precision: int):
    """Retain original atom references; quotient ONLY their declared germ observer."""
    p, m = _prime(prime), _nat(precision, True)
    atoms = _atoms(packet)  # validates integer effects and original stochastic rows
    groups = []
    for index, atom in enumerate(atoms):
        action = atom[3]
        for representative, indices in groups:
            if threshold_action_equivalent(action, representative, p, m+1):
                indices.append(index)
                break
        else:
            groups.append((action, [index]))
    result = []
    for representative, indices in groups:
        totals = {}
        for i in indices:
            source, target, weight, _action, count = atoms[i]
            totals[source, target] = totals.get((source,target), F(0)) + weight*count
        result.append(GermMassClass(representative, tuple(indices),
            tuple((s,t,w) for (s,t),w in sorted(totals.items()))))
    return tuple(result)


@dataclass(frozen=True)
class WeightedLiftSeed:
    packet_digest: str
    prime: int
    precision: int
    guard: int
    frame: tuple
    pivot: int


def weighted_lift_seed(packet, frame, prime, precision):
    p, m = _prime(prime), _nat(precision, True)
    atoms = _atoms(packet)
    guard = max(linear_carry_spread(a,p) for _s,_t,_w,a,_n in atoms)
    s, pivot = _normalize_frame(frame, p, m+guard)
    if len(s) != N:
        raise ValueError('exactly six native spatial coordinates required')
    verify_lifted_peak_frame(packet, s, p, m+1)
    return WeightedLiftSeed(_digest(packet), p, m, guard, s, pivot)


def _validate_seed(packet, seed):
    if not isinstance(seed, WeightedLiftSeed):
        raise TypeError('WeightedLiftSeed required')
    if weighted_lift_seed(packet, seed.frame, seed.prime, seed.precision) != seed:
        raise ValueError('foreign or modified BRC seed')


def _primitive(action, p):
    return sm(F(p)**(-_minimum(action,p)),action)


def _scalar_at_seed(a,b,seed):
    """Unique low-layer projective unit, or None. Exact inherited congruence."""
    p,m,c=seed.prime,seed.precision,seed.guard
    s=matrix(seed.frame); a,b=_primitive(a,p),_primitive(b,p)
    r,j=divmod(seed.pivot,N)
    candidate=mm(mm(inv(b),s),a)[r][j]/s[r][j]
    try:
        u=_mod(candidate,p**m)
        if not u%p: return None
        problem=GermLiftProblem(p,(a,),(b,),c,N)
        problem.seed(seed.frame,(u,),m)
        return u
    except (ValueError,ZeroDivisionError):
        return None


def _matchings(adjacency):
    """All compatible bijections; no mathematical group or frame enumeration."""
    count=len(adjacency)
    order=sorted(range(count),key=lambda i:len(adjacency[i]))
    chosen=[-1]*count
    def visit(depth, used):
        if depth==count:
            yield tuple(chosen)
            return
        i=order[depth]
        for j in adjacency[i]:
            if j not in used:
                chosen[i]=j
                yield from visit(depth+1,used|{j})
    yield from visit(0,set())


def _affine_hull(spaces,p):
    """Project away uniquely determined scalars; reuse inherited RREF twice."""
    successful=[space for space in spaces if space.particular is not None]
    if not successful: return None
    base=successful[0].particular[:N*N]
    directions=[]
    for space in successful:
        directions.append(tuple((x-y)%p for x,y in zip(space.particular[:N*N],base)))
        directions.extend(v[:N*N] for v in space.basis)
    if not directions: directions=[(0,)*(N*N)]
    annihilator=solve_modular_linear(directions,(0,)*len(directions),p).basis
    equations=annihilator or ((0,)*(N*N),)
    rhs=tuple(sum(a*b for a,b in zip(row,base))%p for row in equations)
    return solve_modular_linear(equations,rhs,p)


@dataclass(frozen=True)
class WeightedLiftComponent:
    matching: tuple[int,...]
    certificate: GermLiftCertificate


@dataclass(frozen=True)
class WeightedLiftCertificate:
    packet: ControlPacket
    seed: WeightedLiftSeed
    classes: tuple[GermMassClass,...]
    adjacency: tuple[tuple[int,...],...]
    components: tuple[WeightedLiftComponent,...]
    complete: bool
    space: LinearLiftSpace | None
    matching_budget: int

    @property
    def status(self):
        if not self.complete: return 'MATCHING_LIMIT'
        return 'COMPLETE' if self.space is not None else 'NO_LIFTS'

    @property
    def certified_count(self):
        """Sound family size; exact full fiber size ONLY if complete."""
        return 0 if self.space is None else self.space.count

    def instantiate(self,parameters=()):
        if self.space is None: raise ValueError('NO_KNOWN_LIFT')
        x=self.space.point(parameters)
        scale=self.seed.prime**(self.seed.precision+self.seed.guard)
        frame=tuple(tuple(self.seed.frame[i][j]+scale*x[N*i+j]
                          for j in range(N)) for i in range(N))
        return weighted_lift_seed(self.packet,frame,self.seed.prime,self.seed.precision+1)

    def all_lifts(self,*,limit=4096):
        _nat(limit)
        if self.certified_count>limit:
            raise ValueError('FRAME_LIMIT: symbolic certified family retained')
        if self.space is None: return ()
        return tuple(self.instantiate(x) for x in
                     product(range(self.seed.prime),repeat=len(self.space.basis)))

    def verify(self):
        """Rebuild bindings, all matched constraints, hull and completeness status."""
        rebuilt=lift_weighted_seed(self.packet,self.seed,max_matchings=self.matching_budget)
        if rebuilt!=self: raise ValueError('modified or incomplete weighted lift certificate')
        for component in self.components: component.certificate.verify()
        if self.space is not None:
            self.space.verify()
            # A base point and affine generators suffice by the proved kernel-torsor law.
            dimension=len(self.space.basis)
            self.instantiate((0,)*dimension)
            for j in range(dimension):
                self.instantiate(tuple(int(i==j) for i in range(dimension)))
        return True


def lift_weighted_seed(packet, seed, *, max_matchings=4096):
    """All weighted-kernel lifts above ONE guarded seed, not atom permutations.

    Completeness: fixed controls, supplied seed, prime and next precision, exact
    universal-safe-lattice germ equality. No global GL6 discovery claim.
    MATCHING_LIMIT retains a SOUND affine subset and never claims no lifts.
    """
    _validate_seed(packet,seed);budget=_nat(max_matchings)
    p,m,c=seed.prime,seed.precision,seed.guard
    classes=packet_germ_classes(packet,p,m+1)  # MUST refine before choosing matches
    allowed=[]; scalars={}
    for i,a in enumerate(classes):
        row=[]
        for j,b in enumerate(classes):
            if a.port_masses!=b.port_masses: continue
            u=_scalar_at_seed(a.representative,b.representative,seed)
            if u is not None:
                row.append(j);scalars[i,j]=u
        allowed.append(tuple(row))
    adjacency=tuple(allowed);parts=[];complete=True
    sources=tuple(_primitive(x.representative,p) for x in classes)
    for matching in _matchings(adjacency):
        if len(parts)>=budget:
            complete=False
            break
        targets=tuple(sources[j] for j in matching)
        problem=GermLiftProblem(p,sources,targets,c,N)
        fixed=problem.seed(seed.frame,tuple(scalars[i,j] for i,j in enumerate(matching)),m)
        certificate=lift_germ_seed(problem,fixed)
        parts.append(WeightedLiftComponent(matching,certificate))
    hull=_affine_hull([x.certificate.space for x in parts],p)
    if complete and hull is not None:
        total=sum(x.certificate.space.count for x in parts)
        if hull.count!=total:
            raise ArithmeticError('weighted torsor law or disjoint class-matching invariant failed')
        fibers=[x.certificate.space.count for x in parts if x.certificate.space.count]
        if len(set(fibers))!=1:
            raise ArithmeticError('class-permutation fibers must have equal size')
        number=len(fibers)
        while number>1 and number%p==0: number//=p
        if number!=1:
            raise ArithmeticError('viable class matchings must form a prime-power coset')
    return WeightedLiftCertificate(packet,seed,classes,adjacency,tuple(parts),
                                   complete,hull,budget)


def lift_weighted_family(packet,seeds,target_precision,*,max_frames=4096,max_matchings=4096):
    """Multi-layer continuation, rebuilding colliding/splitting germ classes.

    An oversized layer is returned as complete affine certificates, not
    enumerated and not discarded. This is NOT a universal small-memory
    symbolic solver across arbitrary many precision layers.
    """
    seeds=tuple(dict.fromkeys(seeds));_nat(target_precision,True);_nat(max_frames,True)
    for s in seeds: _validate_seed(packet,s)
    if not seeds: return {'status':'NO_LIFTS','seeds':(),'layers':()}
    if len({s.precision for s in seeds})!=1 or seeds[0].precision>target_precision:
        raise ValueError('equal seed precision not exceeding target required')
    if len({s.prime for s in seeds})!=1:
        raise ValueError('one prime per continuation')
    layers=[];current=seeds
    if len(current)>max_frames:
        return {'status':'FRAME_LIMIT','seeds':current,'layers':()}
    while current and current[0].precision<target_precision:
        certs=tuple(lift_weighted_seed(packet,s,max_matchings=max_matchings) for s in current)
        layers.append((current[0].precision,len(current),sum(c.certified_count for c in certs)))
        if not all(c.complete for c in certs):
            return {'status':'MATCHING_LIMIT','seeds':current,'layers':tuple(layers),'frontier':certs}
        if sum(c.certified_count for c in certs)>max_frames:
            return {'status':'FRAME_LIMIT','seeds':current,'layers':tuple(layers),'frontier':certs}
        current=tuple(s for c in certs for s in c.all_lifts(limit=max_frames))
    return {'status':'COMPLETE' if current else 'NO_LIFTS','seeds':current,'layers':tuple(layers)}
