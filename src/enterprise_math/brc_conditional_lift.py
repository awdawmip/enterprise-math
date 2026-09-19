"""Conditional-distribution lift certificates for finite control BRC.

Research candidate. This is NOT a pointwise state quotient: admissible input
measures must satisfy mu=alpha*L. A mass certificate proves L*W=Q*L; an
'affine_mass' certificate proves that identity separately for each affine
map. The latter preserves joint endpoint measures at declared boundaries,
not weight-histogram shape, labeled paths or arbitrary initial conditions.
L is a fixed nonnegative fiber-supported reconstruction kernel, L*P=I.
No field/occupancy randomization is performed by the certificate itself.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from typing import Sequence
from .brc_control_port import ControlPacket
from .brc_control_mass import control_mass_matrix
from .brc_transport import Affine


def _q(value):
    if isinstance(value, bool) or not isinstance(value, (int, F)):
        raise TypeError('exact int/Fraction required')
    value = F(value)
    if value < 0:
        raise ValueError('nonnegative mass required')
    return value


def independence_witness(table):
    """Return (row, column, signed defect), or None for a product measure.

    Test T*M_ij = row_i*column_j. A zero table passes algebraically without
    claiming a normalized probability distribution. The signed defect is a
    diagnostic, never a negative BRC branch weight.
    """
    rows = tuple(tuple(_q(x) for x in row) for row in table)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('nonempty rectangular table required')
    rs = tuple(sum(row, F(0)) for row in rows)
    cs = tuple(sum((row[j] for row in rows), F(0)) for j in range(len(rows[0])))
    total = sum(rs, F(0))
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            defect = total*value-rs[i]*cs[j]
            if defect:
                return i, j, defect
    return None


@dataclass(frozen=True)
class ConditionalLift:
    """L[a,i]=probabilities[i] when labels[i]=a, zero otherwise."""
    labels: tuple[int, ...]
    probabilities: tuple[F, ...]

    def __post_init__(self):
        labels = tuple(self.labels)
        if not labels or any(type(a) is not int or a < 0 for a in labels):
            raise ValueError('nonempty nonnegative integer labels required')
        if set(labels) != set(range(max(labels)+1)):
            raise ValueError('labels must cover consecutive classes from zero')
        p = tuple(_q(x) for x in self.probabilities)
        if len(p) != len(labels):
            raise ValueError('one conditional probability per microstate required')
        for a in range(max(labels)+1):
            if sum((p[i] for i in range(len(p)) if labels[i] == a), F(0)) != 1:
                raise ValueError('conditional probabilities in every fiber must sum to one')
        object.__setattr__(self, 'labels', labels)
        object.__setattr__(self, 'probabilities', p)

    @classmethod
    def uniform(cls, labels: Sequence[int]):
        labels = tuple(labels)
        if not labels:
            raise ValueError('nonempty labels required')
        return cls(labels, tuple(F(1, labels.count(a)) for a in labels))

    @property
    def micro_count(self):
        return len(self.labels)

    @property
    def coarse_count(self):
        return 1+max(self.labels)

    @property
    def full_support(self):
        return all(self.probabilities)

    def matrix(self):
        return tuple(tuple(p if self.labels[i] == a else F(0)
                           for i, p in enumerate(self.probabilities))
                     for a in range(self.coarse_count))

    def lift_mass(self, alpha):
        alpha = tuple(_q(x) for x in alpha)
        if len(alpha) != self.coarse_count:
            raise ValueError('coarse distribution dimension mismatch')
        return tuple(alpha[a]*p for a, p in zip(self.labels, self.probabilities))

    def project_mass(self, mu):
        mu = tuple(_q(x) for x in mu)
        if len(mu) != self.micro_count:
            raise ValueError('micro distribution dimension mismatch')
        out = [F(0)]*self.coarse_count
        for a, weight in zip(self.labels, mu):
            out[a] += weight
        return tuple(out)

    def encode_mass(self, mu):
        """Reject rather than silently reset a non-admissible distribution."""
        mu = tuple(_q(x) for x in mu)
        alpha = self.project_mass(mu)
        if self.lift_mass(alpha) != mu:
            raise ValueError('input distribution is outside the declared conditional family')
        return alpha


@dataclass(frozen=True)
class LiftCertificate:
    source_digest: str
    lift: ConditionalLift
    mode: str
    quotient: ControlPacket
    coefficient_checks: int

    def check_input(self, mu):
        return self.lift.encode_mass(mu)

    def recheck(self, packet):
        expected = certify_conditional_lift(packet, self.lift, mode=self.mode)
        if self != expected:
            raise ValueError('certificate/source mismatch')
        return True


def certify_conditional_lift(packet, lift, *, mode='mass'):
    """Verify L*W_a=Q_a*L sparsely, a=None for mass-only checking.

    Every coefficient is checked on complete finite control fibers. The
    synthesized quotient coalesces MASS by affine map, not individual branch
    weight shapes. Coordinate/residue and current-observer typing remain the
    caller's explicit obligations. An affine-mass input needs conditional
    independence of micro-control and spatial position given coarse control.
    """
    if not isinstance(packet, ControlPacket) or not isinstance(lift, ConditionalLift):
        raise TypeError('ControlPacket and ConditionalLift required')
    if packet.state_count != lift.micro_count:
        raise ValueError('packet/lift dimensions disagree')
    if mode not in ('mass', 'affine_mass'):
        raise ValueError('mode must be mass or affine_mass')
    left = {}
    identity = Affine.identity(6)
    for i, j, histogram in packet.blocks:
        p = lift.probabilities[i]
        if not p:
            continue
        a = lift.labels[i]
        for weight, action, count in histogram.entries:
            if mode == 'affine_mass' and (any(v.denominator != 1 for row in action.a for v in row)
                                          or any(v.denominator != 1 for v in action.b)):
                raise ValueError('native endpoint lift requires integer affine coefficients')
            key = a, j, action if mode == 'affine_mass' else identity
            left[key] = left.get(key, F(0))+p*weight*count
    coarse = {}
    for (a, j, action), weight in left.items():
        key = a, lift.labels[j], action
        coarse[key] = coarse.get(key, F(0))+weight
    fibers = tuple(tuple(i for i, a in enumerate(lift.labels) if a == b)
                   for b in range(lift.coarse_count))
    checks = 0
    for (a, b, action), weight in coarse.items():
        for j in fibers[b]:
            expected = weight*lift.probabilities[j]
            if left.get((a, j, action), F(0)) != expected:
                raise ValueError(f'conditional family not closed: coarse={a}, target={j}, mode={mode}')
            checks += 1
    edges = ((a, b, weight, action, 1)
             for (a, b, action), weight in coarse.items() if weight)
    quotient = ControlPacket.from_edges(lift.coarse_count, packet.start, packet.duration, edges)
    digest = sha256(repr(packet).encode('utf-8')).hexdigest()
    return LiftCertificate(digest, lift, mode, quotient, checks)


def conditional_mass_matrix(certificate):
    if not isinstance(certificate, LiftCertificate):
        raise TypeError('LiftCertificate required')
    return control_mass_matrix(certificate.quotient)


def conditional_mass_defect(packet, lift):
    """Return (Q,E), E=L*W-Q*L, without granting an unsafe certificate.

    E is a signed algebraic residual, not a positive BRC carrier. Together
    with exact Q,W it supports telescoping error calculations; it is not
    evidence of preserved independence when E is nonzero.
    """
    if not isinstance(packet, ControlPacket) or not isinstance(lift, ConditionalLift):
        raise TypeError('ControlPacket and ConditionalLift required')
    if packet.state_count != lift.micro_count:
        raise ValueError('packet/lift dimensions disagree')
    n, m = lift.micro_count, lift.coarse_count
    left = [[F(0)]*n for _ in range(m)]
    for i, j, histogram in packet.blocks:
        left[lift.labels[i]][j] += lift.probabilities[i]*histogram.forget_effects().total_mass
    q = [[F(0)]*m for _ in range(m)]
    for a in range(m):
        for j in range(n):
            q[a][lift.labels[j]] += left[a][j]
    defect = tuple(tuple(left[a][j]-q[a][lift.labels[j]]*lift.probabilities[j]
                         for j in range(n)) for a in range(m))
    return tuple(tuple(row) for row in q), defect


def _endpoint(key, count):
    if not isinstance(key, tuple) or len(key) != 2:
        raise ValueError('endpoint key must be (control, six-integer coordinate)')
    control, x = key
    if type(control) is not int or not 0 <= control < count:
        raise ValueError('control outside finite layout')
    if not isinstance(x, tuple) or len(x) != 6 or any(type(v) is not int for v in x):
        raise ValueError('six signed integer raw coordinates required')
    return control, x


def lift_endpoint_measure(lift, coarse):
    """Reconstruct only the stipulated joint endpoint measure, not path IDs."""
    if not isinstance(lift, ConditionalLift):
        raise TypeError('ConditionalLift required')
    out = {}
    for key, raw_weight in coarse.items():
        a, x = _endpoint(key, lift.coarse_count)
        weight = _q(raw_weight)
        if weight:
            for i, b in enumerate(lift.labels):
                p = lift.probabilities[i]
                if a == b and p:
                    out[i, x] = weight*p
    return out


def encode_endpoint_measure(lift, measure):
    """Test micro-control/position conditional independence, then encode."""
    if not isinstance(lift, ConditionalLift):
        raise TypeError('ConditionalLift required')
    coarse, cleaned = {}, {}
    for key, raw_weight in measure.items():
        i, x = _endpoint(key, lift.micro_count)
        weight = _q(raw_weight)
        if weight:
            cleaned[i, x] = weight
            target = lift.labels[i], x
            coarse[target] = coarse.get(target, F(0))+weight
    if lift_endpoint_measure(lift, coarse) != cleaned:
        raise ValueError('joint endpoint measure is outside the conditional family')
    return coarse
