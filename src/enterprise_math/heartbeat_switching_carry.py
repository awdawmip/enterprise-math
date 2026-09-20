"""Observer-scoped switching-carry diagnostics and BRC lattice-port certificates.

Research candidate on raw signed native X6, not a new world axiom. Reuses
ControlPacket, affine exact matrix arithmetic and WeightHistogram unchanged.
A certificate concerns p-primary LINEAR Smith-depth spread on every allowed
path; it does not bound affine drift, mass, metric distortion or occupancy.
Rational bases below encode algebraic lattices, never fractional Cell moves.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from typing import Mapping
from .brc_transport import Affine, Matrix, matrix, eye, inv, mm, sm
from .brc_control_port import ControlPacket
from .brc_histogram import WeightHistogram, histogram_serial, histogram_recoalesce


def _nat(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError('nonnegative integer required')
    return value


def _prime(p: int) -> int:
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError('prime integer required')
    return p


def _valuation(q, p: int) -> int:
    if isinstance(q, bool) or not isinstance(q, (int, F)) or not q:
        raise ValueError('nonzero exact rational required')
    q = F(q)
    a, b = abs(q.numerator), q.denominator
    value = 0
    while a % p == 0:
        a //= p
        value += 1
    while b % p == 0:
        b //= p
        value -= 1
    return value


def _minimum(a: Matrix, p: int) -> int:
    return min(_valuation(v, p) for row in a for v in row if v)


def linear_carry_spread(a, prime: int) -> int:
    """Exact largest-minus-smallest p-Smith depth, including rational bases.

    min_entry_v(A)=s_min and min_entry_v(A^-1)=-s_max. No SNF enumeration.
    """
    p = _prime(prime)
    a = matrix(a)
    if len(a) != len(a[0]):
        raise ValueError('square matrix required')
    return -_minimum(a, p)-_minimum(inv(a), p)


@dataclass(frozen=True)
class LatticePortCertificate:
    prime: int
    source_digest: str
    bases: tuple[Matrix, ...]
    scales: tuple[tuple[int, int, int], ...]
    basis_spreads: tuple[int, ...]
    normalized_maps: tuple[tuple[int, int, Matrix], ...]

    def endpoint_bound(self, source: int, target: int) -> int:
        if any(type(i) is not int or not 0 <= i < len(self.bases) for i in (source, target)):
            raise ValueError('control port outside layout')
        return self.basis_spreads[source]+self.basis_spreads[target]

    def recheck(self, packet: ControlPacket) -> bool:
        expected = certify_lattice_ports(packet, self.bases, self.prime,
                                          {(s, t): k for s, t, k in self.scales})
        if self != expected:
            raise ValueError('certificate/source mismatch')
        return True


def certify_lattice_ports(packet: ControlPacket, bases, prime: int,
                          scales: Mapping[tuple[int, int], int]) -> LatticePortCertificate:
    """Check p^-k S_target^-1 A S_source and its inverse are p-integral.

    The declared scalar k is common to all affine atoms in a (source,target)
    block. Passing implies a uniform endpoint-dependent Smith-spread bound
    under every finite allowed path, including state-dependent choices.
    Failure rejects this supplied certificate, not the research object.
    Weights, multiplicities and affine offsets retain existing BRC semantics;
    they are not erased from execution or certified by this linear observer.
    """
    p = _prime(prime)
    if not isinstance(packet, ControlPacket):
        raise TypeError('ControlPacket required')
    bases = tuple(matrix(s) for s in bases)
    if len(bases) != packet.state_count or any(len(s) != 6 or len(s[0]) != 6 for s in bases):
        raise ValueError('one invertible rational six-axis basis per control port required')
    inverses = tuple(inv(s) for s in bases)
    keys = {(s, t) for s, t, h in packet.blocks if h.entries}
    if set(scales) != keys or any(type(k) is not int for k in scales.values()):
        raise ValueError('exactly one integer scale per nonempty control block required')
    normalized = []
    for source, target, histogram in packet.blocks:
        if not histogram.entries:
            continue
        k = scales[source, target]
        for _weight, action, _count in histogram.entries:
            if any(v.denominator != 1 for row in action.a for v in row) or any(v.denominator != 1 for v in action.b):
                raise ValueError('native affine effects require integer coefficients')
            b = sm(F(p)**(-k), mm(mm(inverses[target], action.a), bases[source]))
            bi = inv(b)
            if _minimum(b, p) < 0 or _minimum(bi, p) < 0:
                raise ValueError(f'no p-integral lattice automorphism on block {source}->{target}')
            normalized.append((source, target, b))
    widths = tuple(-_minimum(s, p)-_minimum(si, p) for s, si in zip(bases, inverses))
    return LatticePortCertificate(p, sha256(repr(packet).encode()).hexdigest(), bases,
                                  tuple((s, t, scales[s, t]) for s, t in sorted(keys)),
                                  widths, tuple(normalized))


@dataclass(frozen=True, order=True)
class SplitCarryState:
    """Exact signed allocation for diag(p,p,p,1,1,1) / its complement.

    Time n and signed debt d reconstruct u=(n+d)/2 and v=(n-d)/2.
    This preserves the full composed linear action for this commuting family,
    but not labeled path history, arbitrary affine offsets or other matrices.
    """
    steps: int
    debt: int

    def __post_init__(self):
        _nat(self.steps)
        if type(self.debt) is not int or abs(self.debt) > self.steps or (self.steps+self.debt) % 2:
            raise ValueError('debt must have the same parity as time and magnitude <= time')

    def advance(self, sign: int) -> 'SplitCarryState':
        if type(sign) is not int or sign not in (-1, 1):
            raise ValueError('signed choice must be +1 or -1')
        return SplitCarryState(self.steps+1, self.debt+sign)

    @property
    def axis_depths(self) -> tuple[int, ...]:
        return ((self.steps+self.debt)//2,)*3+((self.steps-self.debt)//2,)*3

    @property
    def smith_depths(self) -> tuple[int, ...]:
        return tuple(sorted(self.axis_depths))

    def action(self, prime: int) -> Affine:
        p = _prime(prime)
        diag = tuple(p**a for a in self.axis_depths)
        return Affine(tuple(tuple(diag[i] if i == j else 0 for j in range(6)) for i in range(6)), (0,)*6)


def growing_block_state(steps: int) -> SplitCarryState:
    """Exact prefix of U V U^2 V^2 U^3 V^3 ...; no floating-point clock."""
    t = _nat(steps)
    k = (1+isqrt(1+4*t))//2
    j = t-k*(k-1)
    debt = j if j <= k else 2*k-j
    return SplitCarryState(t, debt)


def split_carry_push(states: Mapping[SplitCarryState, WeightHistogram], choices):
    """Advance the declared split family using existing exact BRC histograms.

    choices contains (sign, positive exact weight, nonnegative multiplicity).
    Same time port is required. No stochastic normalization is implicit.
    """
    if any(not isinstance(s, SplitCarryState) or not isinstance(h, WeightHistogram)
           for s, h in states.items()):
        raise TypeError('SplitCarryState -> WeightHistogram mapping required')
    if len({s.steps for s in states}) > 1:
        raise ValueError('time ports must match')
    edges = []
    for sign, weight, count in choices:
        if type(sign) is not int or sign not in (-1, 1):
            raise ValueError('signed choice must be +1 or -1')
        histogram = WeightHistogram.from_counts({weight: count})
        if not histogram.is_zero:
            edges.append((sign, histogram))
    out = {}
    for state, histogram in states.items():
        if histogram.is_zero:
            continue
        for sign, edge in edges:
            target = state.advance(sign)
            value = histogram_serial(histogram, edge)
            out[target] = histogram_recoalesce(out[target], value) if target in out else value
    return out


def split_feedback_packet(prime: int = 2, *, start: int = 0):
    """Three debt ports {-1,0,+1}; choose at zero, pay back at the next beat.

    It is an actually restricted update policy, not a proof-only relabeling.
    Return (ControlPacket, bases, block_scales). Choices at zero weigh 1/2;
    repayment is deterministic with weight 1. Every full pair acts by p I.
    """
    p = _prime(prime)
    debts = (-1, 0, 1)
    plus = SplitCarryState(1, 1).action(p)
    minus = SplitCarryState(1, -1).action(p)
    packet = ControlPacket.from_edges(3, start, 1,
        ((1, 2, F(1, 2), plus, 1), (1, 0, F(1, 2), minus, 1),
         (0, 1, 1, plus, 1), (2, 1, 1, minus, 1)))
    bases = tuple(tuple(tuple(F(p)**d if i == j and i < 3 else int(i == j)
                               for j in range(6)) for i in range(6)) for d in debts)
    scales = {(1, 2): 0, (1, 0): 1, (0, 1): 0, (2, 1): 1}
    return packet, bases, scales
