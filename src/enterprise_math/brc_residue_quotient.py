"""Certified observer-scoped quotients of finite residue-port BRC packets.

Research-extracted T0/T6 subtool candidate, not Foundation admission.  A
certificate compares exact affine-effect histograms or exact degree-two
moment operators into EACH retained target class.  It applies only to the
supplied frozen packet family, at arrow boundaries.  It does not preserve
occupancy, unrecorded controls, past labeled histories, or arbitrary future
operators.  Refinement is coarsest only among partitions certified by this
particular coefficient-equality test and refining the initial partition.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from typing import Iterable, Mapping

from .brc_transport import Affine, EffectHistogram, MomentState
from .brc_residue_port import Port, ResidueLayout, ResiduePacket

PAIRS = tuple((i, j) for i in range(7) for j in range(i, 7))
SIZE = len(PAIRS)
Operator = tuple[tuple[Fraction, ...], ...]
ZERO_OPERATOR: Operator = tuple((Fraction(0),) * SIZE for _ in range(SIZE))
Groups = tuple[tuple[Port, ...], ...]


@lru_cache(maxsize=256)
def affine_moment_operator(action: Affine) -> Operator:
    """Return the exact 28-by-28 map on packed symmetric homogeneous moments."""
    if not isinstance(action, Affine) or action.dim != 6:
        raise ValueError('six-axis Affine required')
    h = action.homogeneous()
    return tuple(tuple(h[i][k]*h[j][l] + (h[i][l]*h[j][k] if k != l else 0)
                       for k, l in PAIRS) for i, j in PAIRS)


def _sum_operators(terms: Iterable[tuple[Fraction, Operator]]) -> Operator:
    out = [[Fraction(0) for _ in PAIRS] for _ in PAIRS]
    for weight, operator in terms:
        for i, row in enumerate(operator):
            for j, value in enumerate(row):
                if value:
                    out[i][j] += weight*value
    return tuple(tuple(row) for row in out)


def _hist_operator(histogram: EffectHistogram) -> Operator:
    return _sum_operators((weight*count, affine_moment_operator(action))
                          for weight, action, count in histogram.entries)


def _canonical_groups(layout: ResidueLayout, groups: Iterable[Iterable[Port]]) -> Groups:
    result = tuple(sorted(tuple(sorted(group)) for group in groups))
    if not result or any(not g for g in result):
        raise ValueError('nonempty classes required')
    flat = tuple(port for group in result for port in group)
    if len(set(flat)) != len(flat) or set(flat) != set(layout.ports()):
        raise ValueError('classes must partition every canonical residue port exactly once')
    for port in flat:
        layout.validate(port)
    return result


def _block_map(packet: ResiduePacket, groups: Groups):
    index = {r: i for i, group in enumerate(groups) for r in group}
    by_source = {r: {} for r in packet.layout.ports()}
    for source, target, histogram in packet.blocks:
        g = index[target]
        previous = by_source[source].get(g, EffectHistogram.zero(6))
        by_source[source][g] = previous.alternatives(histogram)
    return by_source


def _signature(row, mode: str):
    if mode == 'effects':
        return tuple((target, hist.entries) for target, hist in sorted(row.items()) if hist.entries)
    if mode == 'moment2':
        return tuple((target, _hist_operator(hist)) for target, hist in sorted(row.items()) if hist.entries)
    raise ValueError("mode must be 'effects' or 'moment2'")


def packet_digest(packet: ResiduePacket) -> str:
    """Local deterministic content binding, not a server signature."""
    return sha256(repr(packet).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class QuotientCertificate:
    packet_digest: str
    groups: Groups
    mode: str
    equality_checks: int


def certify_port_quotient(packet: ResiduePacket, groups, *, mode='moment2') -> QuotientCertificate:
    """Reject a merge unless every source has the same map into every target class."""
    if not isinstance(packet, ResiduePacket):
        raise TypeError('ResiduePacket required')
    groups = _canonical_groups(packet.layout, groups)
    rows = _block_map(packet, groups)
    checks = 0
    for group in groups:
        expected = _signature(rows[group[0]], mode)
        for source in group[1:]:
            if _signature(rows[source], mode) != expected:
                raise ValueError(f'unsafe {mode} merge: source fibers {group[0]} and {source} differ')
            checks += 1
    # Validate the mode even if the partition consists only of singleton classes.
    _signature({}, mode)
    return QuotientCertificate(packet_digest(packet), groups, mode, checks)


def verify_quotient_certificate(packet: ResiduePacket, certificate: QuotientCertificate) -> bool:
    """Recheck content binding and every equality; a local digest is not authority."""
    if not isinstance(certificate, QuotientCertificate):
        raise TypeError('QuotientCertificate required')
    expected = certify_port_quotient(packet, certificate.groups, mode=certificate.mode)
    if expected != certificate:
        raise ValueError('certificate does not match the packet or its equalities')
    return True


def refine_port_partition(packets: Iterable[ResiduePacket], initial=None, *, mode='moment2') -> Groups:
    """Finite exact refinement for a fixed family. No minimal arbitrary-state claim."""
    packets = tuple(packets)
    if not packets or any(not isinstance(p, ResiduePacket) for p in packets):
        raise ValueError('nonempty ResiduePacket family required')
    layout = packets[0].layout
    if any(p.layout != layout for p in packets):
        raise ValueError('all operators must share one residue layout')
    groups = _canonical_groups(layout, initial if initial is not None else (layout.ports(),))
    while True:
        rows = [_block_map(packet, groups) for packet in packets]
        split = []
        for group in groups:
            buckets = {}
            for source in group:
                key = tuple(_signature(row[source], mode) for row in rows)
                buckets.setdefault(key, []).append(source)
            split.extend(tuple(bucket) for bucket in buckets.values())
        refined = _canonical_groups(layout, split)
        if refined == groups:
            for packet in packets:
                certify_port_quotient(packet, groups, mode=mode)
            return groups
        groups = refined


@dataclass(frozen=True)
class QuotientMomentPacket:
    """Linear moment update on a certified partition. No geometric-position codec."""
    start: int
    duration: int
    layout: ResidueLayout
    groups: Groups
    blocks: tuple[tuple[int, int, Operator], ...]
    certificate: QuotientCertificate

    @classmethod
    def compile(cls, packet: ResiduePacket, groups, *, mode='moment2'):
        certificate = certify_port_quotient(packet, groups, mode=mode)
        rows = _block_map(packet, certificate.groups)
        blocks = tuple((source_group, target, _hist_operator(hist))
                       for source_group, members in enumerate(certificate.groups)
                       for target, hist in sorted(rows[members[0]].items()) if hist.entries)
        return cls(packet.start, packet.duration, packet.layout, certificate.groups, blocks, certificate)

    def aggregate(self, fibers: Mapping[Port, MomentState]) -> dict[int, MomentState]:
        index = {r: i for i, group in enumerate(self.groups) for r in group}
        output = {}
        for port, state in fibers.items():
            self.layout.validate(port)
            if not isinstance(state, MomentState) or state.dimension != 6:
                raise ValueError('six-axis moment state required')
            g = index[port]
            previous = output.get(g, (Fraction(0),)*SIZE)
            output[g] = tuple(a+b for a, b in zip(previous, state.upper))
        return {g: MomentState(6, values) for g, values in output.items()}

    def apply(self, state: Mapping[int, MomentState], *, start: int) -> dict[int, MomentState]:
        if type(start) is not int or start != self.start:
            raise ValueError('time port mismatch')
        for key, moment in state.items():
            if type(key) is not int or not 0 <= key < len(self.groups):
                raise ValueError('unknown retained class')
            if not isinstance(moment, MomentState) or moment.dimension != 6:
                raise ValueError('six-axis moment state required')
        out = {}
        for source, target, operator in self.blocks:
            if source not in state:
                continue
            values = state[source].upper
            moved = tuple(sum((v*x for v, x in zip(row, values) if v), Fraction(0))
                          for row in operator)
            previous = out.get(target, (Fraction(0),)*SIZE)
            out[target] = tuple(a+b for a, b in zip(previous, moved))
        return {g: MomentState(6, values) for g, values in out.items()}
