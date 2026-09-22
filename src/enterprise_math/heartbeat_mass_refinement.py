"""Mass-class, rather than atom-bijective, guarded Heartbeat frame lifting.

Fixed control ports, p, positive rational row law and arrow-boundary carry
observer. Finite class matchings give DISJOINT affine one-digit lift families.
Original atom weights/counts are never resampled or replaced by repair counts.
Low seeds are supplied; this is not a search of all GL6, an infinite-lift
termination test, or a probability-preserving quotient for raw atom words.
Dimensions 1,2,3 are algebraic repeated-block diagnostics, not smaller worlds.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import factorial

from .brc_transport import matrix, mm, inv, sm, eye
from .heartbeat_switching_carry import _prime, _minimum, linear_carry_spread
from .heartbeat_peak_orbits import threshold_action_equivalent
from .heartbeat_carry_peak import _atoms
from .heartbeat_congruence_lift import (
    GermLiftProblem, GermLiftCertificate, lift_germ_seed,
    _shape, _normalize_frame, _mod, _nat,
)


def _six(a):
    n = len(a)
    return matrix([[a[i % n][j % n] if i // n == j // n else 0
                    for j in range(6)] for i in range(6)])


@lru_cache(maxsize=16384)
def _same(a, b, p, m):
    return threshold_action_equivalent(_six(a), _six(b), p, m + 1)


def _digest(x):
    return sha256(repr(x).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class KernelTerm:
    source: int
    target: int
    weight: F
    action: tuple
    multiplicity: int = 1

    @property
    def mass(self):
        return self.weight * self.multiplicity


@dataclass(frozen=True)
class GermMassClass:
    representative: int
    members: tuple[int, ...]
    mass_profile: tuple[F, ...]


@dataclass(frozen=True)
class MassKernel:
    prime: int
    dimension: int
    controls: int
    guard: int
    terms: tuple[KernelTerm, ...]

    @classmethod
    def build(cls, terms, prime, *, controls=1):
        p = _prime(prime)
        _nat(controls, True)
        out = []
        for term in terms:
            if not isinstance(term, KernelTerm):
                raise TypeError('KernelTerm required')
            if (type(term.source) is not int or type(term.target) is not int
                or not 0 <= term.source < controls or not 0 <= term.target < controls):
                raise ValueError('control port outside declared layout')
            if type(term.weight) not in (int, F) or term.weight <= 0:
                raise ValueError('positive exact rational atom weight required')
            _nat(term.multiplicity, True)
            a = _shape(term.action)
            inv(a)
            if any(x.denominator != 1 for row in a for x in row):
                raise ValueError('integer linear macro-actions required')
            out.append(KernelTerm(term.source, term.target, F(term.weight), a, term.multiplicity))
        if not out or len(out[0].action) not in (1, 2, 3, 6):
            raise ValueError('nonempty X6 or repeated-block diagnostic terms required')
        n = len(out[0].action)
        if any(len(t.action) != n for t in out):
            raise ValueError('common dimension required')
        if any(sum((t.mass for t in out if t.source == s), F(0)) != 1 for s in range(controls)):
            raise ValueError('row-stochastic mass required; never normalize silently')
        c = max(linear_carry_spread(t.action, p) for t in out)
        return cls(p, n, controls, c, tuple(out))

    @classmethod
    def from_packet(cls, packet, prime):
        return cls.build((KernelTerm(s, t, w, a, k) for s, t, w, a, k in _atoms(packet)),
                         prime, controls=packet.state_count)

    @property
    def digest(self):
        return _digest(self)

    def classes(self, precision):
        return germ_mass_classes(self, precision)

    def seed(self, frame, precision):
        m = _nat(precision, True)
        s, pivot = _normalize_frame(_shape(frame, self.dimension), self.prime, m + self.guard)
        _frame_mapping(self, matrix(s), m)
        return MassLiftSeed(self.digest, m, s, pivot)


@lru_cache(maxsize=512)
def germ_mass_classes(kernel: MassKernel, precision: int) -> tuple[GermMassClass, ...]:
    """Group equal whole-safe-domain action germs; retain every atom's provenance."""
    m = _nat(precision, True)
    groups = []
    for i, term in enumerate(kernel.terms):
        for members in groups:
            if _same(term.action, kernel.terms[members[0]].action, kernel.prime, m):
                members.append(i)
                break
        else:
            groups.append([i])
    result = []
    for members in groups:
        weights = [F(0)] * (kernel.controls ** 2)
        for i in members:
            t = kernel.terms[i]
            weights[t.source * kernel.controls + t.target] += t.mass
        result.append(GermMassClass(members[0], tuple(members), tuple(weights)))
    return tuple(result)


def _frame_mapping(kernel, frame, precision):
    classes = kernel.classes(precision)
    si = inv(frame)
    mapping = []
    for c in classes:
        a = mm(mm(frame, kernel.terms[c.representative].action), si)
        targets = [j for j, d in enumerate(classes)
                   if _same(a, kernel.terms[d.representative].action, kernel.prime, precision)]
        if len(targets) != 1 or classes[targets[0]].mass_profile != c.mass_profile:
            raise ValueError('frame fails the full fixed-control mass-germ law')
        mapping.append(targets[0])
    if len(set(mapping)) != len(classes):
        raise ArithmeticError('conjugacy must permute distinct germs injectively')
    return tuple(mapping)


@dataclass(frozen=True)
class MassLiftSeed:
    kernel_digest: str
    precision: int
    frame: tuple
    pivot: int


@dataclass(frozen=True)
class SplitMassObstruction:
    coarse_source: int
    coarse_target: int
    source_children: tuple
    target_children: tuple


@dataclass(frozen=True)
class ClassLiftComponent:
    matching: tuple[int, ...]
    certificate: GermLiftCertificate

    @property
    def count(self):
        return self.certificate.space.count

    def instantiate(self, kernel, parameters=()):
        child = self.certificate.instantiate(parameters)
        return kernel.seed(child.frame, child.precision)


@dataclass(frozen=True)
class MassLiftResult:
    kernel: MassKernel
    seed: MassLiftSeed
    status: str
    matching_groups: tuple
    matching_count: int
    processed_matchings: int
    components: tuple[ClassLiftComponent, ...]
    rejected: tuple[ClassLiftComponent, ...]
    obstruction: SplitMassObstruction | None

    @property
    def complete(self):
        return self.status != 'MATCHING_LIMIT'

    @property
    def known_count(self):
        return sum(c.count for c in self.components)

    @property
    def count(self):
        return self.known_count if self.complete else None

    def all_seeds(self, *, limit=4096):
        _nat(limit)
        if not self.complete or self.known_count > limit:
            raise ValueError('LIFT_LIMIT: disjoint affine frontier retained')
        out = []
        for component in self.components:
            out.extend(self.kernel.seed(s.frame, s.precision)
                       for s in component.certificate.all_lifts(limit=limit))
        if len(set(out)) != len(out):
            raise ArithmeticError('distinct class matchings must have disjoint lifts')
        return tuple(out)

    def verify(self):
        cap = self.processed_matchings if not self.complete else max(1, self.matching_count)
        expected = lift_mass_seed(self.kernel, self.seed, max_matchings=cap)
        if self != expected:
            raise ValueError('kernel, split-profile or affine-frontier binding mismatch')
        for c in self.components + self.rejected:
            c.certificate.verify()
        return True


def lift_mass_seed(kernel: MassKernel, seed: MassLiftSeed, *, max_matchings=4096) -> MassLiftResult:
    """Complete one-digit mass-row lifting, or an explicitly retained frontier.

    Refine germs FIRST; match their aggregate source/target mass vectors SECOND;
    solve all shared frame equations THIRD. Different fine-class permutations
    yield disjoint affine families. No individual-weight atom bijection needed.
    """
    _nat(max_matchings, True)
    if kernel.seed(seed.frame, seed.precision) != seed:
        raise ValueError('invalid or foreign low-precision mass seed')
    m, p = seed.precision, kernel.prime
    coarse, fine = kernel.classes(m), kernel.classes(m + 1)
    mapping = _frame_mapping(kernel, matrix(seed.frame), m)
    parent = {a: j for j, c in enumerate(coarse) for a in c.members}
    fine_parent = tuple(parent[c.representative] for c in fine)
    groups = []
    for c, d in enumerate(mapping):
        left = {}
        right = {}
        for j, f in enumerate(fine):
            if fine_parent[j] == c:
                left.setdefault(f.mass_profile, []).append(j)
            if fine_parent[j] == d:
                right.setdefault(f.mass_profile, []).append(j)
        lcount = Counter({k: len(v) for k, v in left.items()})
        rcount = Counter({k: len(v) for k, v in right.items()})
        if lcount != rcount:
            obs = SplitMassObstruction(c, d, tuple(sorted(lcount.items())), tuple(sorted(rcount.items())))
            return MassLiftResult(kernel, seed, 'MASS_SPLIT_OBSTRUCTION', (), 0, 0, (), (), obs)
        groups.extend((tuple(left[k]), tuple(right[k])) for k in sorted(left))
    # Each compatibility block is complete bipartite. Enumerate its bijections
    # lazily: the budget never forces materializing a factorial-size pool.
    choices = {i: targets for sources, targets in groups for i in sources}
    def permutations(i, used, current):
        if i == len(fine):
            yield tuple(current)
            return
        for j in choices[i]:
            if j not in used:
                yield from permutations(i + 1, used | {j}, current + [j])
    total = 1
    for sources, _ in groups:
        total *= factorial(len(sources))
    src = tuple(kernel.terms[c.representative].action for c in fine)
    accepted, rejected = [], []
    processed = 0
    s = matrix(seed.frame)
    for pi in permutations(0, set(), []):
        if processed == max_matchings:
            break
        dst = tuple(src[j] for j in pi)
        problem = GermLiftProblem.build(src, dst, p)
        if problem.guard != kernel.guard:
            raise ArithmeticError('germ grouping unexpectedly changed the guard depth')
        multipliers = tuple(_mod(mm(mm(mm(inv(b), s), a), inv(s))[0][0], p**m)
                            for a, b in zip(problem.sources, problem.targets))
        cert = lift_germ_seed(problem, problem.seed(s, multipliers, m))
        component = ClassLiftComponent(pi, cert)
        (accepted if component.count else rejected).append(component)
        processed += 1
    status = 'MATCHING_LIMIT' if processed < total else ('COMPLETE' if accepted else 'GEOMETRIC_OBSTRUCTION')
    return MassLiftResult(kernel, seed, status, tuple(groups), total, processed,
                          tuple(accepted), tuple(rejected), None)


def lift_mass_family(kernel, seeds, target_precision, *, max_seeds=4096, max_matchings=4096):
    """Recompute split classes at EVERY layer; never freeze an arbitrary old matching.

    Budget stop returns all solved affine components plus current seeds, not a
    false no-lift conclusion. This does not flatten multi-layer obstructions
    into one affine space and does not solve the infinite continuation problem.
    """
    _nat(target_precision, True); _nat(max_seeds, True); _nat(max_matchings, True)
    current = tuple(dict.fromkeys(seeds))
    if not current:
        return {'status': 'NO_LIFTS', 'seeds': (), 'layers': ()}
    if len({s.precision for s in current}) != 1 or current[0].precision > target_precision:
        raise ValueError('one starting precision not exceeding target required')
    for seed in current:
        if kernel.seed(seed.frame, seed.precision) != seed:
            raise ValueError('invalid seed')
    layers = []
    if len(current) > max_seeds:
        return {'status': 'LIFT_LIMIT', 'seeds': current, 'layers': ()}
    while current[0].precision < target_precision:
        reports = tuple(lift_mass_seed(kernel, s, max_matchings=max_matchings) for s in current)
        known = sum(r.known_count for r in reports)
        complete = all(r.complete for r in reports)
        layers.append((current[0].precision, len(current), known, complete))
        if not complete or known > max_seeds:
            return {'status': 'LIFT_LIMIT', 'seeds': current, 'layers': tuple(layers), 'frontier': reports}
        current = tuple(s for r in reports for s in r.all_seeds(limit=max_seeds))
        if not current:
            return {'status': 'NO_LIFTS', 'seeds': (), 'layers': tuple(layers), 'frontier': reports}
    return {'status': 'COMPLETE', 'seeds': current, 'layers': tuple(layers)}


def collision_horizon(kernel: MassKernel):
    """Last finite germ collision, not a bound on geometric symmetry lifetime.

    At and above returned separation_precision, distinct classes differ already
    modulo that precision unless they are EXACT rational scalar multiples.
    """
    last = 0
    pairs = []
    for i, t in enumerate(kernel.terms):
        for j, u in enumerate(kernel.terms[:i]):
            rel = mm(inv(u.action), t.action)
            diag = rel[0][0]
            if diag and rel == sm(diag, eye(kernel.dimension)):
                continue
            depth = 0
            if diag:
                normal = sm(1/diag, rel)
                if _minimum(normal, kernel.prime) >= 0 and _minimum(inv(normal), kernel.prime) >= 0:
                    defect = tuple(tuple(x - int(a == b) for b, x in enumerate(row))
                                   for a, row in enumerate(normal))
                    depth = max(0, _minimum(defect, kernel.prime))
            last = max(last, depth)
            pairs.append((j, i, depth))
    return {'separation_precision': max(1, last + 1), 'finite_pair_lifetimes': tuple(pairs)}


def mass_germ_defect(kernel: MassKernel, frame, precision):
    """Per-source total variation of the action-germ mass rows under one frame.

    Monotone under precision refinement. Not itself a first-hit probability
    difference, nor a signed BRC measure. Original positive rows are unchanged.
    """
    m = _nat(precision, True)
    s, _ = _normalize_frame(_shape(frame, kernel.dimension), kernel.prime, m + kernel.guard)
    s = matrix(s); si = inv(s)
    entries = []
    for t in kernel.terms:
        entries += [(t.source, t.target, t.mass, t.action),
                    (t.source, t.target, -t.mass, mm(mm(s, t.action), si))]
    buckets = []
    for source, target, signed_mass, a in entries:
        for b in buckets:
            if b[0] == source and b[1] == target and _same(a, b[3], kernel.prime, m):
                b[2] += signed_mass
                break
        else:
            buckets.append([source, target, signed_mass, a])
    return tuple(sum((abs(w) for c, _, w, _a in buckets if c == source), F(0))/2
                 for source in range(kernel.controls))

@dataclass(frozen=True)
class JointMassLiftSpace:
    """One affine FRAME family, including allowed permutations of fine germs.

    Coefficients describe reference-frame repairs, not BRC probabilities.
    Complete disjoint component certificates establish coverage of the hull.
    """
    source: MassLiftResult
    particular: tuple
    basis: tuple

    @property
    def count(self):
        return self.source.kernel.prime ** len(self.basis)

    def instantiate(self, parameters=()):
        p, n = self.source.kernel.prime, self.source.kernel.dimension
        params = tuple(parameters)
        if len(params) != len(self.basis) or any(type(x) is not int or not 0 <= x < p for x in params):
            raise ValueError('one finite-field coefficient per joint free direction required')
        x = tuple((a + sum(c * v[i] for c, v in zip(params, self.basis))) % p
                  for i, a in enumerate(self.particular))
        seed = self.source.seed
        scale = p ** (seed.precision + self.source.kernel.guard)
        frame = tuple(tuple(seed.frame[i][j] + scale * x[i*n+j] for j in range(n)) for i in range(n))
        return self.source.kernel.seed(frame, seed.precision + 1)

    def verify(self):
        self.source.verify()
        if compress_mass_lifts(self.source) != self:
            raise ValueError('joint affine hull certificate mismatch')
        return True


def compress_mass_lifts(result: MassLiftResult) -> JointMassLiftSpace:
    """Compress a COMPLETE nonempty mass-lift union without enumerating frames.

    The fiber of a group stabilizer under one congruence reduction is a coset
    of an elementary abelian p-group. Hence it is an affine frame space even
    when a fixed class matching splits it into multiple components. We also
    certify this computationally: known disjoint component cardinality equals
    the exact affine-hull cardinality. No claim across several digits at once.
    """
    from .heartbeat_congruence_lift import solve_modular_linear
    if not isinstance(result, MassLiftResult) or not result.complete or not result.known_count:
        raise ValueError('complete nonempty lift result required')
    result.verify()  # A claimed component count is not a coverage certificate.
    p, n = result.kernel.prime, result.kernel.dimension
    q = n*n
    origin = result.components[0].certificate.space.particular[:q]
    candidates = []
    for c in result.components:
        space = c.certificate.space
        candidates.extend(v[:q] for v in space.basis)
        candidates.append(tuple((x-y) % p for x, y in zip(space.particular[:q], origin)))
    basis = []
    for v in candidates:
        if not any(v):
            continue
        rows = tuple(basis + [v])
        rank = solve_modular_linear(rows, (0,)*len(rows), p).rank
        if rank > len(basis):
            basis.append(v)
    # All components are contained in this hull; their matching classes are
    # disjoint and projective scalars are unique given a frame. Equal finite
    # cardinalities therefore certify that the hull has no spurious point.
    if p**len(basis) != result.known_count:
        raise ArithmeticError('mass-lift fiber is not the certified affine hull')
    return JointMassLiftSpace(result, origin, tuple(basis))
