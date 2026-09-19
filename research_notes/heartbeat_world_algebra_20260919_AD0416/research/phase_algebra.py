"""Phase-aware research interface; not a physical clock or final-Cell codec.

Reuses the pinned heartbeat_algebra ring. A Frame is a coordinate readout
F=P*A_b**depth with codomain F(Z^6), not a fractional extension of native Cells.
Every raw inverse is guarded by its exact image test. The world contract does
not fix this frame program or the induced multiplication.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
import heartbeat_algebra as h


def _unbeat_image(y: h.Vec, count: int, b: int) -> h.Vec:
    """Inverse on A_b**count Z^6 only; never discard a nonzero residue."""
    for _ in range(count):
        y, residue = h.analyze(y, b)
        if residue:
            raise ValueError('coordinate is outside the declared frame image')
    return y


@dataclass(frozen=True)
class Frame:
    depth: int
    b: int = 2
    permutation: tuple[int, ...] = (0, 1, 2, 3, 4, 5)

    def __post_init__(self) -> None:
        if h.integer(self.depth) < 0:
            raise ValueError('frame depth must be nonnegative')
        h.radix(self.b)
        if type(self.permutation) is not tuple or len(self.permutation) != 6:
            raise ValueError('six-axis permutation required')
        if any(type(i) is not int for i in self.permutation) or set(self.permutation) != set(range(6)):
            raise ValueError('permutation must contain each native axis exactly once')

    def _permute(self, z: h.Vec) -> h.Vec:
        return tuple(z[i] for i in self.permutation)

    def _unpermute(self, z: h.Vec) -> h.Vec:
        out = [0] * 6
        for i, source in enumerate(self.permutation):
            out[source] = z[i]
        return tuple(out)

    def encode(self, material: Sequence[int]) -> h.Vec:
        return self._permute(h.beats(h.vector(material), self.depth, self.b))

    def decode(self, observed: Sequence[int]) -> h.Vec:
        z = self._unpermute(h.vector(observed))
        return _unbeat_image(z, self.depth, self.b)

    @property
    def unit(self) -> h.Vec:
        return self.encode(h.ONE)

    def product(self, left: Sequence[int], right: Sequence[int]) -> h.Vec:
        """F(m(F^-1 left,F^-1 right)); ring structure transported, not fixed."""
        a, b = self.decode(left), self.decode(right)
        return self.encode(h.multiply(a, b, self.b))

    def folded_product(self, left: Sequence[int], right: Sequence[int]) -> h.Vec:
        """Independent route: unpermute, multiply, divide only ONE frame factor."""
        self.decode(left); self.decode(right)  # product divisibility alone is not enough
        raw = h.multiply(self._unpermute(h.vector(left)), self._unpermute(h.vector(right)), self.b)
        return self._permute(_unbeat_image(raw, self.depth, self.b))


@dataclass(frozen=True)
class FrameProgram:
    depths: tuple[int, ...]
    b: int = 2
    permutation: tuple[int, ...] = (0, 1, 2, 3, 4, 5)

    def __post_init__(self) -> None:
        if type(self.depths) is not tuple or not self.depths:
            raise ValueError('explicit nonempty frame program required')
        for j in self.depths:
            Frame(j, self.b, self.permutation)

    def at(self, tick: int) -> Frame:
        if h.integer(tick) < 0:
            raise ValueError('event tick must be nonnegative')
        return Frame(self.depths[tick % len(self.depths)], self.b, self.permutation)


@dataclass(frozen=True)
class FramedEvent:
    tick: int
    program: FrameProgram
    coordinates: h.Vec

    def __post_init__(self) -> None:
        if type(self.coordinates) is not tuple:
            raise TypeError('coordinates must be an immutable six-tuple')
        if not isinstance(self.program, FrameProgram):
            raise TypeError('FrameProgram required')
        self.program.at(self.tick).decode(self.coordinates)

    @classmethod
    def from_material(cls, material: Sequence[int], tick: int, program: FrameProgram) -> 'FramedEvent':
        return cls(tick, program, program.at(tick).encode(material))

    def material(self) -> h.Vec:
        return self.program.at(self.tick).decode(self.coordinates)

    def product(self, other: 'FramedEvent') -> 'FramedEvent':
        """Same-time arithmetic, NOT a positive-duration evolution arrow."""
        if not isinstance(other, FramedEvent) or (self.tick, self.program) != (other.tick, other.program):
            raise ValueError('binary arithmetic requires identical time and frame-program ports')
        frame = self.program.at(self.tick)
        return FramedEvent(self.tick, self.program, frame.product(self.coordinates, other.coordinates))

    def advance(self, material_translation: Sequence[int] = h.ZERO, *, square: bool = False) -> 'FramedEvent':
        """One forward tick with declared material U(x)=x+c or x*x+c.

        square=False,c=0 is an identity MATERIAL evolution with a changed
        readout/time. It is not an identity event or a free physical transport.
        """
        if type(square) is not bool:
            raise TypeError('square flag must be boolean')
        x, c = self.material(), h.vector(material_translation)
        if square:
            x = h.multiply(x, x, self.program.b)
        return self.from_material(h.add(x, c), self.tick + 1, self.program)


def analyze_fiber(material: Sequence[int], depth: int, b: int = 2) -> tuple[h.Vec, tuple[int, ...]]:
    Frame(depth, b)
    q, digits = h.vector(material), []
    for _ in range(depth):
        q, r = h.analyze(q, b)
        digits.append(r)
    return q, tuple(digits)


def synthesize_fiber(q: Sequence[int], digits: tuple[int, ...], b: int = 2) -> h.Vec:
    h.radix(b)
    if type(digits) is not tuple:
        raise TypeError('immutable chronological residue tuple required')
    z = h.vector(q)
    for r in reversed(digits):
        z = h.synthesize(z, r, b)
    return z


def fiber_product(left, right, b: int = 2):
    """Lossless coarse-chart adapter, not a fixed-size moment contraction."""
    q, r = left; p, s = right
    if len(r) != len(s):
        raise ValueError('coarse depth ports differ')
    a, c = synthesize_fiber(q, r, b), synthesize_fiber(p, s, b)
    return analyze_fiber(h.multiply(a, c, b), len(r), b)
