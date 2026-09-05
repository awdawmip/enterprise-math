"""Exact chart-separated Cell development; conditional model, not Foundation.

Four local endpoint-translation groups are glued only at the pointed packet.
Endpoint normal forms and ordered event histories are different types.
No inference of spatial dimension from the group normal form is made.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable
import sys

_VENDOR = Path(__file__).resolve().parent / "vendor_foundation"
if str(_VENDOR) not in sys.path:
    sys.path.insert(0, str(_VENDOR))
import six_axis as atlas
from vendor import atlas_brc as brc

GROUP, EDGES, STARS = brc.GROUP, brc.EDGES, brc.STARS


def _ints(values: Iterable[int], n: int) -> tuple[int, ...]:
    t = tuple(values)
    if len(t) != n or any(type(x) is not int for x in t):
        raise ValueError(f"expected {n} exact integers (not booleans/floats)")
    return t


def _vertex(v: int) -> int:
    return atlas.vertex(v)


def neighbours(v: int) -> tuple[int, ...]:
    _vertex(v)
    return tuple(w for w in range(4) if w != v)


@dataclass(frozen=True)
class LocalMove:
    """Derived local endpoint displacement, NOT a primitive point address."""
    x: int
    y: int

    def __post_init__(self):
        _ints((self.x, self.y), 2)

    @property
    def zero(self) -> bool:
        return self.x == 0 and self.y == 0

    def positive_decode(self) -> tuple[int, int, int]:
        m = min(self.x, self.y, 0)
        return self.x-m, self.y-m, -m

    @classmethod
    def from_positive(cls, triple: Iterable[int]) -> "LocalMove":
        a,b,c = _ints(triple, 3)
        if min(a,b,c) != 0:
            raise ValueError("local derived section requires nonnegative min-zero data")
        return cls(a-c, b-c)

    def __add__(self, other: "LocalMove") -> "LocalMove":
        if not isinstance(other, LocalMove):
            return NotImplemented
        return LocalMove(self.x+other.x, self.y+other.y)

    def __neg__(self) -> "LocalMove":
        return LocalMove(-self.x, -self.y)

    def gauge_squared(self) -> int:
        return sum(n*n for n in self.positive_decode())

    def rotate(self, chart: int, g: Iterable[int]) -> "LocalMove":
        g = brc.permutation(g)
        src, dst = neighbours(chart), neighbours(g[chart])
        out = [0,0,0]
        for w, n in zip(src, self.positive_decode()):
            out[dst.index(g[w])] = n
        return LocalMove.from_positive(out)


@dataclass(frozen=True)
class Syllable:
    chart: int
    move: LocalMove

    def __post_init__(self):
        _vertex(self.chart)
        if not isinstance(self.move, LocalMove) or self.move.zero:
            raise ValueError("syllables require a nonzero typed local move")


@dataclass(frozen=True)
class Cell:
    """A packet in the universal chart-separated DEVELOPMENT candidate.

    Empty normal form denotes a chosen anchor packet c*, not geometric O_E.
    A tuple of syllables is an endpoint identifier, never a path-count object.
    """
    syllables: tuple[Syllable, ...] = ()

    def __post_init__(self):
        if not isinstance(self.syllables, tuple):
            raise TypeError("immutable syllable tuple required")
        if any(not isinstance(s, Syllable) for s in self.syllables):
            raise TypeError("all endpoint syllables must be typed")
        if any(a.chart == b.chart for a,b in zip(self.syllables,self.syllables[1:])):
            raise ValueError("adjacent equal-chart syllables are not a normal form")

    def push(self, chart: int, move: LocalMove) -> "Cell":
        _vertex(chart)
        if not isinstance(move, LocalMove):
            raise TypeError("typed local endpoint move required")
        if move.zero:
            return self
        work = list(self.syllables)
        if work and work[-1].chart == chart:
            merged = work.pop().move + move
            if not merged.zero:
                work.append(Syllable(chart, merged))
        else:
            work.append(Syllable(chart, move))
        return Cell(tuple(work))

    def multiply(self, other: "Cell") -> "Cell":
        if not isinstance(other, Cell):
            raise TypeError("Cell multiplication is only the declared development law")
        out = self
        for s in other.syllables:
            out = out.push(s.chart, s.move)
        return out

    def inverse(self) -> "Cell":
        return Cell(tuple(Syllable(s.chart, -s.move) for s in reversed(self.syllables)))

    def rotate(self, g: Iterable[int]) -> "Cell":
        g = brc.permutation(g)
        return Cell(tuple(Syllable(g[s.chart],s.move.rotate(s.chart,g)) for s in self.syllables))

    def gauge_terms(self) -> tuple[int, ...]:
        """Length is sum(sqrt(term)); this derived gauge is NOT event count."""
        return tuple(s.move.gauge_squared() for s in self.syllables)

    def carrier_readout(self) -> tuple[int,int,int]:
        """Many-to-one FCC observation; never used to decide Cell equality."""
        out = [0,0,0]
        for s in self.syllables:
            for w,n in zip(neighbours(s.chart),s.move.positive_decode()):
                edge = brc.EDGE_INDEX[tuple(sorted((s.chart,w)))]
                q = atlas.flag_ray(s.chart,edge)
                for i in range(3):
                    out[i] += n*q[i]
        return tuple(out)

    def flat_quotient_address(self) -> tuple[int,int,int]:
        """Only the optional reciprocal-seam quotient, not this Cell's identity."""
        x,y,z = self.carrier_readout()
        numerators = z-x-y, x+z-y, x-y-z
        if any(v % 2 for v in numerators):
            raise AssertionError("FCC parity invariant violated")
        return tuple(v//2 for v in numerators)


def step_move(chart: int, neighbour: int, sign: int = 1) -> LocalMove:
    if type(sign) is not int or sign not in (-1,1):
        raise ValueError("reversal flag must be +1 or -1")
    k = neighbours(chart).index(_vertex(neighbour))
    x,y = ((1,0),(0,1),(-1,-1))[k]
    return LocalMove(sign*x,sign*y)


@dataclass(frozen=True)
class Event:
    chart: int
    neighbour: int
    sign: int = 1
    occurrence: str = "default-channel"
    weight: Fraction = Fraction(1)

    def __post_init__(self):
        step_move(self.chart,self.neighbour,self.sign)
        if not isinstance(self.occurrence,str) or not self.occurrence:
            raise ValueError("an occurrence label is required")
        if isinstance(self.weight,bool) or not isinstance(self.weight,(int,Fraction)) or self.weight <= 0:
            raise ValueError("branch weight must be a positive exact rational")
        object.__setattr__(self,"weight",Fraction(self.weight))

    @property
    def axis(self) -> int:
        return brc.EDGE_INDEX[tuple(sorted((self.chart,self.neighbour)))]

    @property
    def move(self) -> LocalMove:
        return step_move(self.chart,self.neighbour,self.sign)

    def reversed(self) -> "Event":
        # Inverse ENDPOINT operation does not invert/erase occurrence weight.
        return Event(self.chart,self.neighbour,-self.sign,self.occurrence,self.weight)

    def rotate(self,g: Iterable[int]) -> "Event":
        g=brc.permutation(g)
        return Event(g[self.chart],g[self.neighbour],self.sign,self.occurrence,self.weight)


@dataclass(frozen=True)
class PacketPath:
    start: Cell
    events: tuple[Event,...]

    def __post_init__(self):
        if not isinstance(self.start,Cell):
            raise TypeError("path must start at a packet, not an incidence vertex")
        if not isinstance(self.events,tuple) or any(not isinstance(e,Event) for e in self.events):
            raise TypeError("typed immutable ordered events required")

    def trajectory(self) -> tuple[Cell,...]:
        out=[self.start]
        for e in self.events:
            out.append(out[-1].push(e.chart,e.move))
        return tuple(out)

    @property
    def endpoint(self) -> Cell:
        x=self.start
        for e in self.events:
            x=x.push(e.chart,e.move)
        return x

    @property
    def event_count(self) -> int:
        return len(self.events)

    @property
    def occupied_packet_count(self) -> int:
        return len(set(self.trajectory()))

    def rotate(self,g: Iterable[int]) -> "PacketPath":
        return PacketPath(self.start.rotate(g),tuple(e.rotate(g) for e in self.events))

    def then(self,other: "PacketPath") -> "PacketPath":
        if not isinstance(other,PacketPath) or self.endpoint != other.start:
            raise ValueError("source/target mismatch; paths are not composable")
        return PacketPath(self.start,self.events+other.events)

    def summary(self) -> brc.BranchKey:
        """Declared old observer; demonstrably NOT a complete Cell endpoint key."""
        n=[0]*6; w=Fraction(1)
        for e in self.events:
            n[e.axis]+=1
            w*=e.weight
        return brc.BranchKey(w,tuple(n),brc.IDENTITY,len(self.events))


@dataclass(frozen=True)
class IncidenceVertex:
    """Three-packet incidence observation; deliberately not a Cell."""
    packets: frozenset[Cell]

    def __post_init__(self):
        if not isinstance(self.packets,frozenset) or len(self.packets)!=3 or any(not isinstance(p,Cell) for p in self.packets):
            raise ValueError("a three-packet incidence requires three distinct packets")
        # Existence of a common single-chart triangular leaf is part of typing.
        points=tuple(self.packets)
        differences=[points[i].inverse().multiply(points[j]) for i in range(3) for j in range(i+1,3)]
        if any(len(d.syllables)!=1 for d in differences):
            raise ValueError("incidence is not inside one local chart leaf")
        charts={d.syllables[0].chart for d in differences}
        if len(charts)!=1:
            raise ValueError("incidence chart mismatch")
        v=next(iter(charts))
        units={step_move(v,w,sgn) for w in neighbours(v) for sgn in (-1,1)}
        if any(d.syllables[0].move not in units for d in differences):
            raise ValueError("incidence packets are not a local elementary triangle")


def elementary_vertex(anchor: Cell, chart: int, first: int, second: int) -> IncidenceVertex:
    if first==second:
        raise ValueError("two distinct positive chart directions required")
    a=Event(chart,first); b=Event(chart,second)
    p=PacketPath(anchor,(a,b)).trajectory()
    return IncidenceVertex(frozenset(p))


def endpoint_masses(paths: Iterable[PacketPath]) -> dict[Cell,tuple[int,Fraction]]:
    """Explicitly coarse endpoint observer; caller retains original paths."""
    out={}
    for p in paths:
        if not isinstance(p,PacketPath):
            raise TypeError("PacketPath required")
        count,mass=out.get(p.endpoint,(0,Fraction(0)))
        out[p.endpoint]=(count+1,mass+p.summary().weight)
    return out


def local_triangle_certificate(a: LocalMove,b: LocalMove) -> bool:
    """Integer-only equivalent of ||can(a+b)|| <= ||can(a)||+||can(b)||."""
    A,B,C=a.gauge_squared(),b.gauge_squared(),(a+b).gauge_squared()
    return C <= A+B or (C-A-B)**2 <= 4*A*B
