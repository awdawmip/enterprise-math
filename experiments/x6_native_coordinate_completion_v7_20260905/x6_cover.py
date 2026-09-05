"""Exact connected Cell-cover models over the X6 coordinate completion.

The parameter ``modulus`` is the diagonal closure order m:
- m=1: coordinate-complete Cell identity;
- m>1: cyclic common-depth fibre C_m;
- m=0: unbounded integer common-depth fibre.

Research tool only.  It classifies a model family; it does not choose P000 m.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import repeat
from typing import Iterable

from x6_coordinate import AXIS_COUNT, AXES, Coord6, canonical


def _modulus(m: int) -> int:
    if type(m) is not int or m<0:
        raise ValueError("modulus must be an integer >=0")
    return m


def _reduce_depth(depth: int, m: int) -> int:
    if type(depth) is not int:
        raise TypeError("depth must be integer")
    return depth if m==0 else depth % m


def depth_carry(a: Coord6, b: Coord6) -> int:
    """Existing V2 common-depth carry in the identity frame."""
    if not isinstance(a,Coord6) or not isinstance(b,Coord6):
        raise TypeError("Coord6 operands required")
    return min(x+y for x,y in zip(a.values,b.values))


@dataclass(frozen=True)
class CoverState:
    coordinate: Coord6
    depth: int = 0
    modulus: int = 1

    def __post_init__(self):
        if not isinstance(self.coordinate,Coord6):
            raise TypeError("coordinate must be Coord6")
        m=_modulus(self.modulus)
        object.__setattr__(self,"depth",_reduce_depth(self.depth,m))

    def compose(self, other: "CoverState") -> "CoverState":
        if not isinstance(other,CoverState) or self.modulus!=other.modulus:
            raise ValueError("same-cover states required")
        raw=tuple(a+b for a,b in zip(self.coordinate.values,other.coordinate.values))
        carry=min(raw)
        return CoverState(
            Coord6(canonical(raw)),
            self.depth+other.depth+carry,
            self.modulus,
        )

    def step(self, axis: int, direction: int=1) -> "CoverState":
        if type(axis) is not int or axis not in AXES or direction not in (-1,1):
            raise ValueError("invalid native axis step")
        # Work with an exact integer lift: coordinate + depth*1.  For a finite
        # fibre any representative of the depth residue gives the same class.
        lift=[x+self.depth for x in self.coordinate.values]
        lift[axis]+=direction
        low=min(lift)
        coord=Coord6(canonical(lift))
        return CoverState(coord,low,self.modulus)

    @property
    def coordinate_observation(self) -> Coord6:
        return self.coordinate


def diagonal_loop(state: CoverState, repeats: int=1) -> CoverState:
    if type(repeats) is not int or repeats<0:
        raise ValueError("repeats must be nonnegative integer")
    out=state
    for _ in range(repeats):
        for i in AXES:
            out=out.step(i,+1)
    return out


def first_positive_diagonal_return(modulus: int):
    """Number of complete six-axis diagonal loops needed for full-state return.

    Returns None for m=0 (no nonzero return).
    """
    m=_modulus(modulus)
    return None if m==0 else m


__all__=["CoverState","depth_carry","diagonal_loop","first_positive_diagonal_return"]
