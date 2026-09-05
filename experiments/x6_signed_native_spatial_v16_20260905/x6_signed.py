"""P000 V4-aligned X6 signed spatial coordinate research prototype.

Full spatial coordinates live in Z^6.  The older min-zero six-axis object is
retained as a relative/joint-slice observer, not as the full spatial state.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from math import factorial
from typing import Iterable, Sequence

AXES=tuple(range(6))
ALL_SLICES=tuple(combinations(AXES,3))
S6=tuple(permutations(AXES))
DIAGONAL=(1,1,1,1,1,1)


def _z6(values:Iterable[int])->tuple[int,...]:
    out=tuple(values)
    if len(out)!=6 or any(type(x) is not int for x in out):
        raise ValueError("expected six signed integer coordinates")
    return out


def canonical(values:Iterable[int])->tuple[int,...]:
    out=tuple(values)
    if not out or any(type(x) is not int for x in out):
        raise ValueError("exact integer tuple required")
    m=min(out)
    return tuple(x-m for x in out)


def _slice(S:Sequence[int])->tuple[int,int,int]:
    S=tuple(S)
    if len(S)!=3 or len(set(S))!=3 or any(type(i) is not int or i not in AXES for i in S):
        raise ValueError("expected three distinct native axis indices")
    return S


@dataclass(frozen=True)
class Spatial6:
    coords:tuple[int,...]=(0,0,0,0,0,0)
    def __post_init__(self):
        object.__setattr__(self,"coords",_z6(self.coords))
    def step(self,axis:int,direction:int=1)->"Spatial6":
        if type(axis) is not int or axis not in AXES or direction not in (-1,1):
            raise ValueError("invalid signed native-axis step")
        z=list(self.coords); z[axis]+=direction
        return Spatial6(tuple(z))
    def displacement_to(self,other:"Spatial6")->tuple[int,...]:
        if not isinstance(other,Spatial6): raise TypeError("Spatial6 required")
        return tuple(b-a for a,b in zip(self.coords,other.coords))
    def norm_squared_from_origin(self)->int:
        return sum(x*x for x in self.coords)
    def observe(self,S:Sequence[int])->tuple[int,int,int]:
        S=_slice(S)
        return canonical(self.coords[i] for i in S)
    def rotate(self,p:Sequence[int])->"Spatial6":
        p=tuple(p)
        if len(p)!=6 or set(p)!=set(AXES): raise ValueError("S6 permutation required")
        out=[0]*6
        for old,new in enumerate(p): out[new]=self.coords[old]
        return Spatial6(tuple(out))
    def relative_residual_depth(self):
        h=min(self.coords)
        return canonical(self.coords),h


ORIGIN=Spatial6()


def full_distance_squared(a:Spatial6,b:Spatial6)->int:
    d=a.displacement_to(b)
    return sum(x*x for x in d)


def relative_class(z:Iterable[int])->tuple[int,...]:
    return canonical(_z6(z))


def from_residual_depth(residual:Iterable[int],depth:int)->Spatial6:
    r=tuple(residual)
    if len(r)!=6 or any(type(x) is not int or x<0 for x in r) or min(r)!=0 or type(depth) is not int:
        raise ValueError("min-zero six residual and integer depth required")
    return Spatial6(tuple(x+depth for x in r))


def depth_carry(a:Iterable[int],b:Iterable[int])->int:
    a=tuple(a); b=tuple(b)
    if len(a)!=6 or len(b)!=6 or min(a)!=0 or min(b)!=0 or any(type(x) is not int or x<0 for x in a+b):
        raise ValueError("two nonnegative min-zero six residuals required")
    return min(x+y for x,y in zip(a,b))


def joint_slice_equal(a:Spatial6,b:Spatial6)->bool:
    return all(a.observe(S)==b.observe(S) for S in ALL_SLICES)


def joint_slice_difference_is_diagonal(a:Spatial6,b:Spatial6)->bool:
    d=a.displacement_to(b)
    return len(set(d))==1


def hidden_slice_coordinates(state:Spatial6,S:Sequence[int]):
    """Lossless chart: local min-zero triple + common visible offset + 3 omitted signed coords."""
    S=_slice(S)
    raw=tuple(state.coords[i] for i in S)
    c=min(raw)
    visible=tuple(x-c for x in raw)
    omitted=tuple(i for i in AXES if i not in S)
    hidden=tuple(state.coords[i] for i in omitted)
    return visible,c,hidden


def from_hidden_slice_coordinates(S:Sequence[int],visible:Iterable[int],common:int,hidden:Iterable[int])->Spatial6:
    S=_slice(S); visible=tuple(visible); hidden=tuple(hidden)
    if len(visible)!=3 or any(type(x) is not int or x<0 for x in visible) or min(visible)!=0:
        raise ValueError("local visible address must be min-zero")
    if type(common) is not int or len(hidden)!=3 or any(type(x) is not int for x in hidden):
        raise ValueError("integer common offset and three hidden integers required")
    omitted=tuple(i for i in AXES if i not in S)
    z=[0]*6
    for i,x in zip(S,visible): z[i]=x+common
    for i,x in zip(omitted,hidden): z[i]=x
    return Spatial6(tuple(z))


def diagonal_step(state:Spatial6,repeats:int=1)->Spatial6:
    if type(repeats) is not int: raise TypeError("integer repeats required")
    return Spatial6(tuple(x+repeats for x in state.coords))


def triangle_displacement(S:Sequence[int])->Spatial6:
    S=_slice(S); z=[0]*6
    for i in S: z[i]=1
    return Spatial6(tuple(z))


def positive_path_multiplicity(endpoint:Iterable[int])->int:
    """N-BRC multiplicity for positive-axis words ending at exact full endpoint from origin."""
    n=_z6(endpoint)
    if any(x<0 for x in n): return 0
    m=sum(n)
    out=factorial(m)
    for x in n: out//=factorial(x)
    return out


def relative_endpoint_multiplicity(length:int,residual:Iterable[int])->int:
    """Older quotient formula, explicitly typed as relative endpoint + length observer."""
    r=tuple(residual)
    if type(length) is not int or length<0 or len(r)!=6 or any(type(x) is not int or x<0 for x in r) or min(r)!=0:
        raise ValueError("length and min-zero residual required")
    gap=length-sum(r)
    if gap<0 or gap%6: return 0
    k=gap//6
    return positive_path_multiplicity(tuple(x+k for x in r))


__all__=[
    "Spatial6","ORIGIN","AXES","ALL_SLICES","S6","DIAGONAL","canonical",
    "full_distance_squared","relative_class","from_residual_depth","depth_carry",
    "joint_slice_equal","joint_slice_difference_is_diagonal","hidden_slice_coordinates",
    "from_hidden_slice_coordinates","diagonal_step","triangle_displacement",
    "positive_path_multiplicity","relative_endpoint_multiplicity",
]
