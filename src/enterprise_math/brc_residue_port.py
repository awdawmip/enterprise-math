"""Exact residue-port BRC transport (research candidate, not Foundation).

Ports are six-coordinate congruence fibers, not spatial dimensions or an
external semantic index. Each block reuses EffectHistogram. Integer affine
maps must preserve the period sublattice and the declared source/target fiber.
Fixed fiber-conditioned weights and degree<=2 observers then close under any
finite number of these updates. This does not preserve occupancy, all labeled
paths, arbitrary nonlinear maps, or constant bit-memory.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import prod
from typing import Iterable, Mapping
from .brc_transport import Affine, EffectHistogram, MomentState, eye, ma, sm, point_moment
from .brc_histogram import WeightHistogram, histogram_recoalesce

Port = tuple[int, ...]
ZERO = (0,) * 6


def natural(x: int) -> int:
    if type(x) is not int or x < 0:
        raise ValueError('nonnegative integer required')
    return x


def vector(x) -> Port:
    x = tuple(x)
    if len(x) != 6 or any(type(v) is not int for v in x):
        raise ValueError('six signed integer raw coordinates required')
    return x


@dataclass(frozen=True)
class ResidueLayout:
    moduli: Port

    def __post_init__(self):
        m = vector(self.moduli)
        if any(v < 1 for v in m):
            raise ValueError('positive moduli required')
        object.__setattr__(self, 'moduli', m)

    @property
    def size(self):
        return prod(self.moduli)

    def ports(self, limit=65536):
        if self.size > natural(limit):
            raise ValueError('explicit port enumeration exceeds limit')
        return tuple(product(*(range(m) for m in self.moduli)))

    def residue(self, x):
        return tuple(v % m for v, m in zip(vector(x), self.moduli))

    def validate(self, port):
        if type(port) is not tuple or self.residue(port) != port:
            raise ValueError('noncanonical residue port')

    def certify(self, source, target, action):
        self.validate(source); self.validate(target)
        if not isinstance(action, Affine) or action.dim != 6:
            raise ValueError('six-axis affine action required')
        if any(x.denominator != 1 for row in action.a for x in row) or any(x.denominator != 1 for x in action.b):
            raise ValueError('integer-preserving affine coefficients required')
        for i, mi in enumerate(self.moduli):
            for j, mj in enumerate(self.moduli):
                if (int(action.a[i][j]) * mj) % mi:
                    raise ValueError('action does not preserve the period sublattice')
        y = tuple(int(v) for v in action.apply(source))
        if self.residue(y) != target:
            raise ValueError('action does not land in its declared residue fiber')


@dataclass(frozen=True)
class ResiduePacket:
    layout: ResidueLayout
    start: int
    duration: int
    blocks: tuple[tuple[Port, Port, EffectHistogram], ...]

    def __post_init__(self):
        natural(self.start); natural(self.duration)
        if not isinstance(self.layout, ResidueLayout) or type(self.blocks) is not tuple:
            raise TypeError('explicit residue layout and immutable blocks required')
        keys = []
        for r, s, h in self.blocks:
            if not isinstance(h, EffectHistogram) or h.dim != 6:
                raise ValueError('six-axis effect histogram required')
            self.layout.validate(r); self.layout.validate(s)
            keys.append((r, s))
            for _w, action, _n in h.entries:
                self.layout.certify(r, s, action)
        if keys != sorted(set(keys)):
            raise ValueError('unique canonical residue blocks required')

    @classmethod
    def from_edges(cls, layout, start, duration, edges: Iterable):
        groups = {}
        for r, s, weight, action, count in edges:
            layout.certify(r, s, action)
            groups.setdefault((r, s), []).append((weight, action, count))
        blocks = tuple((r, s, EffectHistogram.from_terms(6, terms))
                       for (r, s), terms in sorted(groups.items()))
        return cls(layout, start, duration, blocks)

    @property
    def end(self):
        return self.start + self.duration

    def at(self, start):
        """Explicit reuse of THIS frozen spatial rule at a new time port."""
        return ResiduePacket(self.layout, start, self.duration, self.blocks)

    @classmethod
    def identity(cls, layout, start=0):
        return cls(layout, start, 0, tuple((r, r, EffectHistogram.unit(6)) for r in layout.ports()))

    def alternatives(self, other):
        if (self.layout, self.start, self.duration) != (other.layout, other.start, other.duration):
            raise ValueError('parallel layouts/time ports must match')
        blocks = {(r, s): h for r, s, h in self.blocks}
        for r, s, h in other.blocks:
            blocks[r, s] = blocks.get((r, s), EffectHistogram.zero(6)).alternatives(h)
        return ResiduePacket(self.layout, self.start, self.duration,
                             tuple((r, s, h) for (r, s), h in sorted(blocks.items())))

    def then(self, later):
        if self.layout != later.layout or self.end != later.start:
            raise ValueError('serial residue/time ports must match')
        outgoing = {}
        for s, t, h in later.blocks:
            outgoing.setdefault(s, []).append((t, h))
        blocks = {}
        for r, s, h in self.blocks:
            for t, g in outgoing.get(s, ()):
                key = r, t
                hg = h.then(g)
                blocks[key] = blocks.get(key, EffectHistogram.zero(6)).alternatives(hg)
        return ResiduePacket(self.layout, self.start, self.duration + later.duration,
                             tuple((r, t, h) for (r, t), h in sorted(blocks.items())))

    def repeat(self, count):
        """Repeated frozen rule; boundary effects only. Support may grow."""
        n = natural(count)
        out = self.identity(self.layout, self.start)
        power = self
        while n:
            if n & 1:
                out = out.then(power.at(out.end))
            n //= 2
            if n:
                power = power.then(power.at(power.end))
        return out

    def evaluate(self, x) -> dict[Port, WeightHistogram]:
        x = vector(x); source = self.layout.residue(x); result = {}
        for r, _s, h in self.blocks:
            if r != source:
                continue
            for y, weights in h.evaluate(x).items():
                y = tuple(int(v) for v in y)
                result[y] = histogram_recoalesce(result[y], weights) if y in result else weights
        return result

    def stochastic(self):
        totals = {r: Fraction(0) for r in self.layout.ports()}
        for r, _s, h in self.blocks:
            totals[r] += h.forget_effects().total_mass
        return all(w == 1 for w in totals.values())

    def moment_action(self, fibers: Mapping[Port, MomentState]):
        for r, state in fibers.items():
            self.layout.validate(r)
            if not isinstance(state, MomentState) or state.dimension != 6:
                raise ValueError('six-axis fiber moment state required')
        out = {}
        for r, s, h in self.blocks:
            if r not in fibers:
                continue
            term = h.moment_action(fibers[r].to_matrix())
            out[s] = ma(out[s], term) if s in out else term
        return {s: MomentState.from_matrix(m) for s, m in out.items()}


def fiber_moments(layout, measure):
    out = {}
    for x, weight in measure.items():
        x = vector(x)
        if isinstance(weight, bool) or not isinstance(weight, (int, Fraction)) or weight <= 0:
            raise ValueError('positive exact measure required')
        r = layout.residue(x); term = sm(weight, point_moment(x))
        out[r] = ma(out[r], term) if r in out else term
    return {r: MomentState.from_matrix(m) for r, m in out.items()}


def total_moment(fibers):
    out = sm(0, eye(7))
    for state in fibers.values():
        out = ma(out, state.to_matrix())
    return out


def block_swap(layout, axis, scale=1, origin=0, start=0):
    """Swap neighboring coarse blocks, keeping each point's within-block digit.

    Duration=scale counts fine native steps, not a free coarse jump. Direction
    is decided once at the operation's entrance. Origin is a real interaction
    partition offset, not a changed coordinate naming convention.
    """
    if type(axis) is not int or not 0 <= axis < 6 or type(origin) is not int:
        raise ValueError('invalid axis/origin')
    if natural(scale) == 0 or layout.moduli[axis] % (2*scale):
        raise ValueError('tracked modulus must include the block-swap period')
    edges = []
    for r in layout.ports():
        delta = scale if ((r[axis]-origin)//scale) % 2 == 0 else -scale
        v = tuple(delta if i == axis else 0 for i in range(6))
        action = Affine(eye(6), v)
        target = layout.residue(tuple(r[i]+v[i] for i in range(6)))
        edges.append((r, target, 1, action, 1))
    return ResiduePacket.from_edges(layout, start, scale, edges)


def swap_microtrace(x, axis, scale=1, origin=0, start=0):
    """Realize one block swap as primitive steps with a locked direction.

    Tuples are (time, raw_coordinate, remaining_steps, direction). Direction
    remains part of the transit state until arrival; an intermediate position
    alone is not sufficient. This is not a many-particle collision model.
    """
    x = vector(x); natural(start)
    if type(axis) is not int or not 0 <= axis < 6 or type(origin) is not int or natural(scale) == 0:
        raise ValueError('invalid primitive swap parameters')
    direction = 1 if ((x[axis]-origin)//scale) % 2 == 0 else -1
    out = [(start, x, scale, direction)]
    for tick in range(1, scale+1):
        x = tuple(v+direction if i==axis else v for i,v in enumerate(x))
        left = scale-tick
        out.append((start+tick, x, left, direction if left else 0))
    return tuple(out)
