"""Research BRC extension: exact affine packets behind finite residue guards.

Time ports and source/target control ports must match. This is not complete
path provenance, occupancy recovery, physical time calibration, or Foundation.
The old EffectHistogram and MomentState remain the branch and moment carriers.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from typing import Iterable, Mapping, Sequence

from enterprise_math.brc_transport import (
    Affine, EffectHistogram, MomentState, eye, ma, sm, point_moment,
)
from enterprise_math.brc_histogram import (
    WeightHistogram, histogram_serial, histogram_recoalesce,
)

DIM = 6
Key = tuple[int, ...]
ZERO = (0,) * DIM
ONE = (1,) * DIM


def native(x: Sequence[int]) -> Key:
    out = tuple(x)
    if len(out) != DIM or any(type(a) is not int for a in out):
        raise TypeError('six signed native integers required; not final Cell addresses')
    return out


def nonnegative(x: int) -> int:
    if type(x) is not int or x < 0:
        raise ValueError('nonnegative integer required')
    return x


@dataclass(frozen=True)
class ResidueControl:
    """A finite control quotient, not a quotient of the whole spatial state.

    parity: all six low bits (64 classes).
    neighbor_xor: six adjacent XORs with even sum (32 classes).
    At width>1, guards read floor(x/width) and only translations by multiples
    of width are accepted. General integer affine maps are supported at width1.
    """
    kind: str = 'neighbor_xor'
    width: int = 1

    def __post_init__(self) -> None:
        if self.kind not in ('parity', 'neighbor_xor'):
            raise ValueError('unsupported control quotient')
        if type(self.width) is not int or self.width < 1:
            raise ValueError('positive integer width required')

    @property
    def states(self) -> tuple[Key, ...]:
        return tuple(r for r in product((0, 1), repeat=DIM)
                     if self.kind == 'parity' or sum(r) % 2 == 0)

    def validate(self, c: Key) -> None:
        if type(c) is not tuple or len(c) != DIM or any(type(v) is not int or v not in (0, 1) for v in c):
            raise ValueError('control must be a six-bit tuple')
        if self.kind == 'neighbor_xor' and sum(c) % 2:
            raise ValueError('neighbor XOR bits must have even total parity')

    def observe(self, x: Sequence[int]) -> Key:
        r = tuple((a // self.width) % 2 for a in native(x))
        if self.kind == 'parity':
            return r
        return tuple(r[i] ^ r[(i+1) % DIM] for i in range(DIM))

    def representative(self, c: Key) -> Key:
        self.validate(c)
        if self.kind == 'parity':
            r = c
        else:
            r = [0]
            for i in range(DIM-1):
                r.append(r[-1] ^ c[i])
        return tuple(self.width*a for a in r)

    def target(self, c: Key, action: Affine) -> Key:
        """Prove descent for this integral affine action; never infer it by samples."""
        self.validate(c)
        if not isinstance(action, Affine) or action.dim != DIM:
            raise ValueError('six-axis Affine required')
        if any(x.denominator != 1 for row in action.a for x in row) or any(x.denominator != 1 for x in action.b):
            raise ValueError('integral affine map required by the residue contract')
        if self.width != 1:
            if action.a != eye(DIM) or any(int(x) % self.width for x in action.b):
                raise ValueError('higher-width guard permits only width-multiple translations')
        elif self.kind == 'neighbor_xor':
            # Kernel of adjacent differences over F2 is span{(1,...,1)}.
            # Thus A preserves the quotient iff A*1 is constant modulo2.
            sums = tuple(int(sum(row)) % 2 for row in action.a)
            if len(set(sums)) != 1:
                raise ValueError('affine action does not descend through neighbor-XOR control')
        out = action.apply(self.representative(c))
        return self.observe(tuple(int(a) for a in out))


@dataclass(frozen=True)
class GuardedKernel:
    start: int
    duration: int
    control: ResidueControl
    # Each block is (source control, target control, original BRC packet).
    blocks: tuple[tuple[Key, Key, EffectHistogram], ...]

    def __post_init__(self) -> None:
        nonnegative(self.start); nonnegative(self.duration)
        if not isinstance(self.control, ResidueControl):
            raise TypeError('ResidueControl required')
        if type(self.blocks) is not tuple:
            raise TypeError('immutable block tuple required')
        seen = []
        for c, d, packet in self.blocks:
            self.control.validate(c); self.control.validate(d)
            if not isinstance(packet, EffectHistogram) or packet.dim != DIM or not packet.entries:
                raise ValueError('nonempty original six-axis BRC packet required')
            for _, action, _ in packet.entries:
                if self.control.target(c, action) != d:
                    raise ValueError('incorrect target control port')
            seen.append((c, d))
        if seen != sorted(set(seen)):
            raise ValueError('blocks must be uniquely ordered by source/target')

    @property
    def end(self) -> int:
        return self.start + self.duration

    @classmethod
    def from_rows(cls, start: int, duration: int, control: ResidueControl,
                  rows: Mapping[Key, Iterable[tuple[int | Q, Affine, int]]]) -> 'GuardedKernel':
        grouped: dict[tuple[Key, Key], list] = {}
        for c, terms in rows.items():
            control.validate(c)
            packet = EffectHistogram.from_terms(DIM, terms)
            for w, action, count in packet.entries:
                d = control.target(c, action)
                grouped.setdefault((c, d), []).append((w, action, count))
        return cls(start, duration, control, tuple(
            (c, d, EffectHistogram.from_terms(DIM, terms))
            for (c, d), terms in sorted(grouped.items())))

    @classmethod
    def identity(cls, tick: int, control: ResidueControl) -> 'GuardedKernel':
        return cls.from_rows(tick, 0, control,
                             {r: [(1, Affine.identity(DIM), 1)] for r in control.states})

    @classmethod
    def zero(cls, start: int, duration: int, control: ResidueControl) -> 'GuardedKernel':
        return cls(start, duration, control, ())

    def then(self, later: 'GuardedKernel') -> 'GuardedKernel':
        if not isinstance(later, GuardedKernel) or self.end != later.start or self.control != later.control:
            raise ValueError('time/control ports do not match')
        rhs: dict[Key, list] = {}
        for c, d, packet in later.blocks:
            rhs.setdefault(c, []).append((d, packet))
        grouped: dict[tuple[Key, Key], EffectHistogram] = {}
        for c, middle, first in self.blocks:
            for d, second in rhs.get(middle, ()):
                p = first.then(second)  # actual reuse of original BRC serial law
                k = (c, d)
                grouped[k] = grouped[k].alternatives(p) if k in grouped else p
        return GuardedKernel(self.start, self.duration + later.duration, self.control,
                             tuple((c, d, p) for (c, d), p in sorted(grouped.items())))

    def alternatives(self, other: 'GuardedKernel') -> 'GuardedKernel':
        if not isinstance(other, GuardedKernel) or (self.start, self.duration, self.control) != (other.start, other.duration, other.control):
            raise ValueError('parallel alternatives require the same time/control ports')
        grouped = {(c, d): p for c, d, p in self.blocks}
        for c, d, p in other.blocks:
            grouped[c, d] = grouped[c, d].alternatives(p) if (c, d) in grouped else p
        return GuardedKernel(self.start, self.duration, self.control,
                             tuple((c, d, p) for (c, d), p in sorted(grouped.items())))

    def at(self, start: int) -> 'GuardedKernel':
        """Explicitly schedule this same declared rule at another source tick."""
        return GuardedKernel(start, self.duration, self.control, self.blocks)

    def apply_points(self, points: Mapping[Key, WeightHistogram], tick: int) -> dict[Key, WeightHistogram]:
        if type(tick) is not int or tick != self.start:
            raise ValueError('point-measure time port mismatch')
        rows: dict[Key, list] = {}
        for c, d, packet in self.blocks:
            rows.setdefault(c, []).append((d, packet))
        output: dict[Key, WeightHistogram] = {}
        for x, incoming in points.items():
            x = native(x)
            if not isinstance(incoming, WeightHistogram):
                raise TypeError('original WeightHistogram required')
            c = self.control.observe(x)
            for d, packet in rows.get(c, ()):
                for yq, local in packet.evaluate(x).items():
                    y = tuple(int(a) for a in yq)
                    if self.control.observe(y) != d:
                        raise AssertionError('certified control descent failed')
                    combined = histogram_serial(incoming, local)
                    output[y] = histogram_recoalesce(output[y], combined) if y in output else combined
        return output


@lru_cache(maxsize=4096)
def _translation_summary(packet: EffectHistogram):
    """Finite sum of branch mass, displacement first and second moments."""
    if any(a.a != eye(DIM) for _, a, _ in packet.entries):
        return None
    total = Q(0); first = [Q(0)] * DIM
    second = [[Q(0) for _ in range(DIM)] for _ in range(DIM)]
    for w, a, c in packet.entries:
        w *= c; total += w
        for i in range(DIM):
            first[i] += w*a.b[i]
            for j in range(DIM):
                second[i][j] += w*a.b[i]*a.b[j]
    return total, tuple(first), tuple(tuple(r) for r in second)


def packet_moment(packet: EffectHistogram, state: MomentState) -> MomentState:
    """Exact specialization of original moment_action; falls back for general A."""
    m = state.to_matrix()
    summary = _translation_summary(packet)
    if summary is None:
        return MomentState.from_matrix(packet.moment_action(m))
    total, first, second = summary
    out = [[Q(0) for _ in range(DIM+1)] for _ in range(DIM+1)]
    for i in range(DIM):
        for j in range(DIM):
            out[i][j] = total*m[i][j] + first[i]*m[j][DIM] + first[j]*m[i][DIM] + second[i][j]*m[DIM][DIM]
        out[i][DIM] = out[DIM][i] = total*m[i][DIM] + first[i]*m[DIM][DIM]
    out[DIM][DIM] = total*m[DIM][DIM]
    return MomentState.from_matrix(tuple(tuple(row) for row in out))


@dataclass(frozen=True)
class GuardedMoments:
    tick: int
    control: ResidueControl
    blocks: tuple[tuple[Key, MomentState], ...]

    def __post_init__(self) -> None:
        nonnegative(self.tick)
        if not isinstance(self.control, ResidueControl) or type(self.blocks) is not tuple:
            raise TypeError('control and immutable moment blocks required')
        keys = []
        for c, m in self.blocks:
            self.control.validate(c)
            if not isinstance(m, MomentState) or m.dimension != DIM:
                raise ValueError('six-axis original MomentState required')
            keys.append(c)
        if keys != sorted(set(keys)):
            raise ValueError('moment blocks must be uniquely ordered')

    @classmethod
    def from_points(cls, points: Mapping[Key, WeightHistogram], tick: int,
                    control: ResidueControl) -> 'GuardedMoments':
        grouped = {}
        for x, h in points.items():
            x = native(x)
            if not isinstance(h, WeightHistogram):
                raise TypeError('WeightHistogram required')
            c = control.observe(x)
            m = sm(h.total_mass, point_moment(x))
            grouped[c] = ma(grouped[c], m) if c in grouped else m
        return cls(tick, control, tuple((c, MomentState.from_matrix(m)) for c, m in sorted(grouped.items())))

    def then(self, kernel: GuardedKernel) -> 'GuardedMoments':
        if self.tick != kernel.start or self.control != kernel.control:
            raise ValueError('moment/kernel time or control port mismatch')
        inputs = dict(self.blocks)
        out = {}
        for c, d, packet in kernel.blocks:
            if c not in inputs:
                continue
            m = packet_moment(packet, inputs[c]).to_matrix()
            out[d] = ma(out[d], m) if d in out else m
        return GuardedMoments(kernel.end, self.control,
                              tuple((d, MomentState.from_matrix(m)) for d, m in sorted(out.items())))

    def total(self) -> MomentState:
        m = sm(0, eye(DIM+1))
        for _, block in self.blocks:
            m = ma(m, block.to_matrix())
        return MomentState.from_matrix(m)
