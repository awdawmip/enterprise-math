"""BRC one-digit lifts of complete weighted action-germ kernels.

Input is an unchanged ControlPacket: fixed ports, positive weight*count, X6
integer affine arrows. Observer: p-primary linear carry at fixed arrow
boundaries; translations, original atom words and phases/amplitudes are NOT
identified by this mass observer. Source atoms/provenance remain in packet.

Class aggregation is a proved BRC observer, not an independent resampling.
Each class matching reuses the guarded BRC lift solver; complete matching
families are consolidated only with an exhaustive cardinality certificate.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
from math import factorial

from .brc_transport import matrix, mm, inv, sm
from .brc_control_port import ControlPacket
from .heartbeat_carry_peak import _atoms
from .heartbeat_switching_carry import _prime, _minimum, linear_carry_spread
from .heartbeat_peak_orbits import threshold_action_equivalent
from .heartbeat_congruence_lift import (
    GermLiftProblem, lift_germ_seed, solve_modular_linear,
    verify_lifted_peak_frame, _normalize_frame, _mod, LinearLiftSpace)


def _positive(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive integer required')
    return n


def _digest(packet):
    return sha256(repr(packet).encode()).hexdigest()


@dataclass(frozen=True)
class WeightedGermClass:
    source: int
    target: int
    action: tuple
    mass: F
    atom_ids: tuple[int, ...]


def packet_germ_classes(packet: ControlPacket, prime: int, depth: int):
    """Push original BRC masses to universal safe-input action classes.

    depth=m corresponds to carry threshold R=m+1. This is not a quotient of
    arbitrary future operator labels or an equality of individual weights.
    """
    p = _prime(prime); m = _positive(depth)
    classes = []
    for i, (source, target, weight, a, count) in enumerate(_atoms(packet)):
        for j, c in enumerate(classes):
            if (source, target) == (c.source, c.target) and threshold_action_equivalent(a, c.action, p, m+1):
                classes[j] = WeightedGermClass(source, target, c.action,
                                                c.mass+weight*count, c.atom_ids+(i,))
                break
        else:
            classes.append(WeightedGermClass(source, target, a, weight*count, (i,)))
    return tuple(classes)


def _rank(rows, width, p):
    if not rows:
        return 0
    return solve_modular_linear(rows, (0,)*len(rows), p).rank


def _span_basis(rows, width, p):
    kept = []
    for row in rows:
        row = tuple(_mod(v, p) for v in row)
        if len(row) != width:
            raise ValueError('wrong coefficient width')
        if _rank(kept+[row], width, p) > len(kept):
            kept.append(row)
    return tuple(kept)


def repeated_pair_chart(prime: int, pivot: int):
    """Three equal 2x2 correction blocks embedded in X6; explicitly narrower than full X6."""
    p = _prime(prime)
    if type(pivot) is not int or not 0 <= pivot < 36:
        raise ValueError('frame pivot outside X6')
    directions = []
    for a, b in product(range(2), repeat=2):
        d = tuple(tuple(int(i//2==j//2 and i%2==a and j%2==b) for j in range(6)) for i in range(6))
        if not d[pivot//6][pivot%6]:
            directions.append(d)
    return tuple(directions)


def _chart(prime, pivot, supplied):
    raw = tuple(supplied) if supplied is not None else tuple(
        tuple(tuple(int(6*i+j==k) for j in range(6)) for i in range(6))
        for k in range(36) if k != pivot)
    if not raw:
        raise ValueError('nonempty independent correction chart required')
    directions = []
    for a in raw:
        a = matrix(a)
        if len(a) != 6 or any(len(row)!=6 for row in a):
            raise ValueError('six-axis correction matrices required')
        d = tuple(tuple(_mod(v, prime) for v in row) for row in a)
        if d[pivot//6][pivot%6]:
            raise ValueError('chart must preserve the projective gauge pivot')
        directions.append(d)
    flat = tuple(tuple(x for row in a for x in row) for a in directions)
    if _rank(flat, 36, prime) != len(flat):
        raise ValueError('correction directions must be independent')
    return tuple(directions)


@dataclass(frozen=True)
class MatchingFamily:
    matching: tuple[int, ...]
    full_certificate: object
    system: LinearLiftSpace


@dataclass(frozen=True)
class WeightedKernelLift:
    packet_digest: str
    prime: int
    depth: int
    guard: int
    frame: tuple
    pivot: int
    chart: tuple
    coarse_classes: tuple[WeightedGermClass, ...]
    fine_classes: tuple[WeightedGermClass, ...]
    coarse_matching: tuple[int, ...]
    candidate_groups: tuple
    candidate_matchings: int
    status: str
    families: tuple[MatchingFamily, ...]
    affine_space: LinearLiftSpace | None
    obstruction: tuple | None

    @property
    def count(self):
        """None means unresolved enumeration budget, never zero."""
        if self.status == 'MATCHING_LIMIT':
            return None
        return self.affine_space.count if self.affine_space is not None else 0

    def instantiate(self, parameters=None):
        if self.affine_space is None:
            raise ValueError('no complete nonempty repair space')
        if parameters is None:
            parameters = (0,)*len(self.affine_space.basis)
        theta = self.affine_space.point(parameters)
        p, n = self.prime, self.depth+self.guard
        correction = tuple(tuple(sum(c*d[i][j] for c,d in zip(theta,self.chart))%p for j in range(6)) for i in range(6))
        out = tuple(tuple(self.frame[i][j]+p**n*correction[i][j] for j in range(6)) for i in range(6))
        return _normalize_frame(out, p, n+1)[0]

    def all_frames(self, *, limit=4096):
        _positive(limit)
        if self.count is None:
            raise ValueError('MATCHING_LIMIT: unexpanded class matchings retained')
        if self.count == 0:
            return ()
        if self.count > limit:
            raise ValueError('FRAME_LIMIT: symbolic affine family retained')
        return tuple(self.instantiate(x) for x in product(range(self.prime),repeat=len(self.affine_space.basis)))

    def verify(self, packet):
        if self.packet_digest != _digest(packet):
            raise ValueError('packet binding changed')
        # Reconstruct partitions, class matching coverage and all solver systems.
        bound = max(1, self.candidate_matchings) if self.status != 'MATCHING_LIMIT' else max(1, self.candidate_matchings-1)
        expected = lift_weighted_kernel(packet, self.frame, self.prime, self.depth,
                                        correction_chart=self.chart, max_matchings=bound)
        if expected != self:
            raise ValueError('incomplete or altered weighted-kernel certificate')
        if self.affine_space is not None:
            self.affine_space.verify()
        for family in self.families:
            family.full_certificate.verify(); family.system.verify()
        return True


def _affine_hull(families, width, p):
    valid = [f for f in families if f.system.count]
    if not valid:
        return None
    anchor = valid[0].system.particular[:width]
    generators = []
    for f in valid:
        point = f.system.particular[:width]
        generators.append(tuple((x-y)%p for x,y in zip(point, anchor)))
        projected = tuple(z[:width] for z in f.system.basis)
        # Projective scalars are uniquely determined by the frame: projection
        # must be injective, otherwise p^d would overcount physical frames.
        if _rank(projected, width, p) != len(f.system.basis):
            raise ArithmeticError('scalar freedom was incorrectly counted as a frame')
        generators.extend(projected)
    basis = _span_basis(generators, width, p)
    if basis:
        annihilators = solve_modular_linear(basis, (0,)*len(basis), p).basis
    else:
        annihilators = tuple(tuple(int(i==j) for j in range(width)) for i in range(width))
    if not annihilators:
        annihilators = ((0,)*width,)
    rhs = tuple(sum(v*x for v,x in zip(row,anchor))%p for row in annihilators)
    result = solve_modular_linear(annihilators, rhs, p)
    # Matchings are disjoint because conjugation permutes distinct fine classes.
    if result.count != sum(f.system.count for f in valid):
        raise ArithmeticError('union is incomplete, duplicated, or not affine')
    return result


def lift_weighted_kernel(packet: ControlPacket, frame, prime: int, depth: int, *,
                         correction_chart=None, max_matchings=4096):
    """All next-digit mass-kernel symmetries over ONE guarded seed.

    Unlike atom-bijective matching, uses original weight*count summed within
    actual action-germ classes. Complete within the supplied correction chart.
    Full X6 chart is default. MATCHING_LIMIT performs no unsafe affine filling.
    """
    p = _prime(prime); m = _positive(depth); cap = _positive(max_matchings)
    atoms = _atoms(packet)
    guard = max(linear_carry_spread(a,p) for _s,_t,_w,a,_n in atoms)
    s, pivot = _normalize_frame(frame,p,m+guard)
    if len(s) != 6:
        raise ValueError('six-axis reference frame required')
    chart = _chart(p,pivot,correction_chart); width = len(chart)
    verify_lifted_peak_frame(packet,s,p,m+1)
    coarse = packet_germ_classes(packet,p,m)
    fine = packet_germ_classes(packet,p,m+1)
    sinv = inv(matrix(s))
    coarse_matching = []
    for cls in coarse:
        moved = mm(mm(matrix(s),cls.action),sinv)
        candidates = [i for i,c in enumerate(coarse) if
            (cls.source,cls.target,cls.mass)==(c.source,c.target,c.mass) and
            threshold_action_equivalent(moved,c.action,p,m+1)]
        if len(candidates)!=1:
            raise ArithmeticError('coarse kernel did not induce a unique class permutation')
        coarse_matching.append(candidates[0])
    if len(set(coarse_matching))!=len(coarse):
        raise ArithmeticError('nonbijective conjugation class map')
    parent = {i:k for k,c in enumerate(coarse) for i in c.atom_ids}
    left, right = {}, {}
    for i,c in enumerate(fine):
        coarse_parent = parent[c.atom_ids[0]]
        if any(parent[a]!=coarse_parent for a in c.atom_ids):
            raise ArithmeticError('finer classes must refine coarse classes')
        left.setdefault((coarse_matching[coarse_parent],c.mass),[]).append(i)
        right.setdefault((coarse_parent,c.mass),[]).append(i)
    groups = tuple((key,tuple(left.get(key,())),tuple(right.get(key,()))) for key in sorted(set(left)|set(right)))
    common = dict(packet_digest=_digest(packet),prime=p,depth=m,guard=guard,frame=s,pivot=pivot,
                  chart=chart,coarse_classes=coarse,fine_classes=fine,
                  coarse_matching=tuple(coarse_matching),candidate_groups=groups)
    mismatch = tuple(g for g in groups if len(g[1])!=len(g[2]))
    if mismatch:
        return WeightedKernelLift(**common,candidate_matchings=0,status='MASS_SPLIT_OBSTRUCTION',
                                  families=(),affine_space=None,obstruction=mismatch)
    number = 1
    for _key,src,_dst in groups:
        number *= factorial(len(src))
    if number>cap:
        return WeightedKernelLift(**common,candidate_matchings=number,status='MATCHING_LIMIT',
                                  families=(),affine_space=None,obstruction=None)
    permutations_by_group = [tuple(permutations(dst)) for _key,_src,dst in groups]
    families = []
    for assignment in product(*permutations_by_group):
        matching = [-1]*len(fine)
        for (_key,src,_dst),dest in zip(groups,assignment):
            for i,j in zip(src,dest): matching[i]=j
        prob = GermLiftProblem.build([c.action for c in fine],[fine[j].action for j in matching],p)
        if prob.guard!=guard:
            raise ArithmeticError('class projection changed the guard')
        units = []
        for a,b in zip(prob.sources,prob.targets):
            relative = mm(mm(mm(inv(b),matrix(s)),a),sinv)
            units.append(_mod(relative[0][0],p**m))
        seed = prob.seed(s,units,m)
        full = lift_germ_seed(prob,seed)
        flat = tuple(tuple(x for row in d for x in row) for d in chart)
        reduced = tuple(tuple(sum(row[k]*v[k] for k in range(36))%p for v in flat)+tuple(row[36:])
                        for row in full.space.coefficients)
        system = solve_modular_linear(reduced,full.space.rhs,p)
        families.append(MatchingFamily(tuple(matching),full,system))
    space = _affine_hull(families,width,p)
    return WeightedKernelLift(**common,candidate_matchings=number,
                              status='COMPLETE' if space is not None else 'JOINT_OBSTRUCTION',
                              families=tuple(families),affine_space=space,
                              obstruction=None if space is not None else tuple(f.system.obstruction for f in families))


def certify_repaired_frame(packet, certificate: WeightedKernelLift, parameters=None):
    """Actual inherited BRC weighted-row recheck before probability compilation."""
    if _digest(packet)!=certificate.packet_digest:
        raise ValueError('packet binding changed')
    frame = certificate.instantiate(parameters)
    verify_lifted_peak_frame(packet,frame,certificate.prime,certificate.depth+2)
    return frame


def lift_weighted_tower(packet, frames, prime, initial_depth, target_depth, *,
                        correction_chart=None, max_frames=4096, max_matchings=4096):
    """Finite-depth full-kernel continuation, recomputing classes at every level.

    Keeps entire affine frontier on budget failure. It does not collapse
    multi-digit correlations into a single affine space or claim infinite lift.
    """
    p = _prime(prime); m = _positive(initial_depth); end = _positive(target_depth)
    cap = _positive(max_frames); _positive(max_matchings)
    if end < m:
        raise ValueError('target depth cannot precede the seed')
    atoms = _atoms(packet)
    c = max(linear_carry_spread(a,p) for _s,_t,_w,a,_n in atoms)
    current = tuple(dict.fromkeys(_normalize_frame(f,p,m+c)[0] for f in frames))
    for f in current:
        verify_lifted_peak_frame(packet,f,p,m+1)
    layers = []
    if not current:
        return {'status':'NO_LIFTS','frames':(), 'depth':m,'layers':()}
    if len(current)>cap:
        return {'status':'FRAME_LIMIT','frames':current,'depth':m,'layers':()}
    while m < end:
        certs = tuple(lift_weighted_kernel(packet,f,p,m,correction_chart=correction_chart,
                                         max_matchings=max_matchings) for f in current)
        if any(x.count is None for x in certs):
            return {'status':'MATCHING_LIMIT','frames':current,'depth':m,'layers':tuple(layers),
                    'frontier':certs}
        count = sum(x.count for x in certs)
        layers.append((m,len(current),count))
        if count>cap:
            return {'status':'FRAME_LIMIT','frames':current,'depth':m,'layers':tuple(layers),
                    'frontier':certs}
        current = tuple(f for cert in certs for f in cert.all_frames(limit=cap))
        if len(set(current))!=len(current):
            raise ArithmeticError('different seed fibers overlapped')
        m+=1
        if not current:
            return {'status':'NO_LIFTS','frames':(),'depth':m,'layers':tuple(layers),'frontier':certs}
    return {'status':'COMPLETE','frames':current,'depth':m,'layers':tuple(layers)}


def mass_split_defect_bound(packet, certificate: WeightedKernelLift):
    """Per-source lower bound on total variation of the *fine germ* mass law.

    A true frame permutes germs. Sorted child masses minimize L1 distance
    even over arbitrary child permutations; frame restrictions can only
    increase it. This is NOT a lower bound for a particular peak probability:
    pushing to a coarser observable can erase the defect entirely.
    """
    certificate.verify(packet)
    by_parent = [[] for _ in certificate.coarse_classes]
    atom_parent = {a:i for i,c in enumerate(certificate.coarse_classes)
                   for a in c.atom_ids}
    for c in certificate.fine_classes:
        by_parent[atom_parent[c.atom_ids[0]]].append(c.mass)
    out = {i:F(0) for i in range(packet.state_count)}
    for i, c in enumerate(certificate.coarse_classes):
        a = sorted(by_parent[i], reverse=True)
        b = sorted(by_parent[certificate.coarse_matching[i]], reverse=True)
        size = max(len(a), len(b))
        a += [F(0)]*(size-len(a)); b += [F(0)]*(size-len(b))
        out[c.source] += sum((abs(x-y) for x,y in zip(a,b)),F(0))/2
    return out
