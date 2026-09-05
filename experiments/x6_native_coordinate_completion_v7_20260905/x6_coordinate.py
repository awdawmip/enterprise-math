"""Exact six-axis coordinate-completion research prototype.

This module implements the *derived* coordinate model

    G6_D = Z^6 / Z(1,1,1,1,1,1)

through its unique nonnegative min-zero section.  It is deliberately typed as a
research candidate for native Cell coordinates, not as an already-promoted P000
Cell ontology.

Classical abelian rank is NOT Enterprise spatial dimension.  P000 dimension is
six native spatial axes.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
from typing import Iterable, Sequence

AXIS_COUNT = 6
AXES = tuple(range(AXIS_COUNT))
ALL_SLICES = tuple(combinations(AXES, 3))
S6 = tuple(permutations(AXES))
ZERO = (0,) * AXIS_COUNT

# K4/FCC edge-label order retained for interoperability with the existing
# six-axis derived atlas: AB, AC, AD, BC, BD, CD.
K4_EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
K4_STARS = tuple(tuple(i for i,e in enumerate(K4_EDGES) if v in e) for v in range(4))
K4_FACES = tuple(tuple(i for i,e in enumerate(K4_EDGES) if v not in e) for v in range(4))


def _integers(values: Iterable[int], size: int) -> tuple[int, ...]:
    out = tuple(values)
    if len(out) != size or any(type(x) is not int for x in out):
        raise ValueError(f"expected {size} exact integers")
    return out


def _slice(slice_axes: Sequence[int]) -> tuple[int,int,int]:
    out = tuple(slice_axes)
    if len(out) != 3 or any(type(i) is not int or i not in AXES for i in out) or len(set(out)) != 3:
        raise ValueError("slice must contain three distinct native axis indices")
    return out


def canonical(values: Iterable[int]) -> tuple[int, ...]:
    """Unique min-zero representative of an integer diagonal-shift class."""
    out = tuple(values)
    if not out or any(type(x) is not int for x in out):
        raise ValueError("expected a nonempty exact integer tuple")
    m = min(out)
    return tuple(x - m for x in out)


def is_address(values: Iterable[int]) -> bool:
    out = tuple(values)
    return (
        len(out) == AXIS_COUNT
        and all(type(x) is int and x >= 0 for x in out)
        and min(out) == 0
    )


@dataclass(frozen=True)
class Coord6:
    """Min-zero six-component coordinate class (derived; native candidate)."""

    values: tuple[int,...] = ZERO

    def __post_init__(self):
        values = tuple(self.values)
        if not is_address(values):
            raise ValueError("Coord6 requires six nonnegative integers with global minimum zero")
        object.__setattr__(self,"values",values)

    @classmethod
    def from_integer_lift(cls, values: Iterable[int]) -> "Coord6":
        values = _integers(values,AXIS_COUNT)
        return cls(canonical(values))

    def translated(self, delta: Iterable[int]) -> "Coord6":
        delta = _integers(delta,AXIS_COUNT)
        return Coord6.from_integer_lift(a+b for a,b in zip(self.values,delta))

    def step(self, axis: int, direction: int = 1) -> "Coord6":
        if type(axis) is not int or axis not in AXES:
            raise ValueError("invalid native axis")
        if direction not in (-1,1):
            raise ValueError("direction must be +1 or -1")
        delta=[0]*AXIS_COUNT
        delta[axis]=direction
        return self.translated(delta)

    def inverse_displacement(self) -> "Coord6":
        return Coord6.from_integer_lift(-x for x in self.values)

    def norm_squared(self) -> int:
        """P000 typed six-axis component quadratic readout on this candidate."""
        return sum(x*x for x in self.values)

    def observe(self, slice_axes: Sequence[int]) -> tuple[int,int,int]:
        S=_slice(slice_axes)
        return canonical(self.values[i] for i in S)

    def rotate(self, permutation: Sequence[int]) -> "Coord6":
        p=tuple(permutation)
        if len(p)!=AXIS_COUNT or set(p)!=set(AXES):
            raise ValueError("expected a permutation of six axes")
        out=[0]*AXIS_COUNT
        for old,new in enumerate(p):
            out[new]=self.values[old]
        return Coord6(tuple(out))

    @property
    def grade_c6(self) -> int:
        """Well-defined total-component residue modulo 6."""
        return sum(self.values)%6


ORIGIN_COORD = Coord6()


def axis_step(axis: int, direction: int = 1) -> Coord6:
    return ORIGIN_COORD.step(axis,direction)


def observe_after_step(state: Coord6, slice_axes: Sequence[int], axis: int, direction: int=1):
    return state.step(axis,direction).observe(slice_axes)


def local_step(address: Iterable[int], local_axis_position: int, direction: int=1):
    address=tuple(address)
    if len(address)!=3 or any(type(x) is not int or x<0 for x in address) or min(address)!=0:
        raise ValueError("local address must be a nonnegative min-zero triple")
    if type(local_axis_position) is not int or not 0<=local_axis_position<3 or direction not in (-1,1):
        raise ValueError("invalid local step")
    z=list(address)
    z[local_axis_position]+=direction
    return canonical(z)


def hidden_chart(state: Coord6, slice_axes: Sequence[int]):
    """Lossless set-chart: visible min-zero triple + 3 omitted relative integers.

    Gauge is fixed by subtracting the minimum of the three visible lifted
    coordinates from all six lifted coordinates.
    """
    S=_slice(slice_axes)
    visible_raw=tuple(state.values[i] for i in S)
    m=min(visible_raw)
    visible=tuple(x-m for x in visible_raw)
    omitted=tuple(i for i in AXES if i not in S)
    hidden=tuple(state.values[i]-m for i in omitted)
    return visible,hidden


def from_hidden_chart(slice_axes: Sequence[int], visible: Iterable[int], hidden: Iterable[int]) -> Coord6:
    S=_slice(slice_axes)
    visible=tuple(visible); hidden=tuple(hidden)
    if len(visible)!=3 or any(type(x) is not int or x<0 for x in visible) or min(visible)!=0:
        raise ValueError("visible chart must be a nonnegative min-zero triple")
    if len(hidden)!=3 or any(type(x) is not int for x in hidden):
        raise ValueError("hidden chart requires three exact relative integers")
    omitted=tuple(i for i in AXES if i not in S)
    lift=[0]*AXIS_COUNT
    for i,x in zip(S,visible): lift[i]=x
    for i,x in zip(omitted,hidden): lift[i]=x
    return Coord6.from_integer_lift(lift)


def slice_holonomy(slice_axes: Sequence[int]) -> Coord6:
    """Full displacement of one positive step on each visible slice axis."""
    S=_slice(slice_axes)
    z=[0]*AXIS_COUNT
    for i in S: z[i]=1
    return Coord6.from_integer_lift(z)


def complement_slice(slice_axes: Sequence[int]) -> tuple[int,int,int]:
    S=set(_slice(slice_axes))
    return tuple(i for i in AXES if i not in S)


def group_equal_opposite(x: Coord6, y: Coord6) -> bool:
    return x.values==y.values


def brc_endpoint_multiplicity(length: int, endpoint: Coord6) -> int:
    """Exact equal-weight N-BRC multiplicity for positive six-axis words."""
    if type(length) is not int or length<0 or not isinstance(endpoint,Coord6):
        raise ValueError("nonnegative integer length and Coord6 required")
    total=sum(endpoint.values)
    gap=length-total
    if gap<0 or gap%6:
        return 0
    k=gap//6
    counts=tuple(a+k for a in endpoint.values)
    out=factorial(length)
    for c in counts:
        out//=factorial(c)
    return out


def brc_endpoint_weight(
    length: int,
    endpoint: Coord6,
    weights: Sequence[Fraction|int],
) -> Fraction:
    """Exact positive-rational Weighted-BRC terminal mass."""
    weights=tuple(weights)
    if len(weights)!=6:
        raise ValueError("six axis weights required")
    q=[]
    for w in weights:
        if isinstance(w,bool) or not isinstance(w,(int,Fraction)):
            raise TypeError("weights must be exact int/Fraction")
        w=Fraction(w)
        if w<=0:
            raise ValueError("weights must be strictly positive")
        q.append(w)
    mult=brc_endpoint_multiplicity(length,endpoint)
    if mult==0:
        return Fraction(0)
    k=(length-sum(endpoint.values))//6
    out=Fraction(mult)
    for a,w in zip(endpoint.values,q):
        out*=w**(a+k)
    return out


def positive_return_count(length: int) -> int:
    return brc_endpoint_multiplicity(length,ORIGIN_COORD)


def k4_s4_axis_permutations():
    """24 S6 permutations induced from the current K4/FCC edge action."""
    out=[]
    edge_index={e:i for i,e in enumerate(K4_EDGES)}
    for g in permutations(range(4)):
        p=[]
        for u,v in K4_EDGES:
            p.append(edge_index[tuple(sorted((g[u],g[v])))])
        out.append(tuple(p))
    if len(set(out))!=24:
        raise AssertionError("K4 edge action must be faithful S4")
    return tuple(out)


def k4_slice_type(slice_axes: Sequence[int]) -> str:
    S=frozenset(_slice(slice_axes))
    if S in map(frozenset,K4_STARS): return "STAR"
    if S in map(frozenset,K4_FACES): return "FACE"
    return "PATH"


__all__=[
    "Coord6","ORIGIN_COORD","AXES","ALL_SLICES","S6","K4_STARS","K4_FACES",
    "canonical","axis_step","local_step","hidden_chart","from_hidden_chart",
    "slice_holonomy","complement_slice","brc_endpoint_multiplicity",
    "brc_endpoint_weight","positive_return_count","k4_s4_axis_permutations",
    "k4_slice_type",
]
