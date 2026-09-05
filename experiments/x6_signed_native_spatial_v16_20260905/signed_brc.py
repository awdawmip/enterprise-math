"""Exact signed-axis BRC kernels on the P000-V4 X6 spatial candidate."""
from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Iterable, Sequence


def _z6(z:Iterable[int]):
    z=tuple(z)
    if len(z)!=6 or any(type(x) is not int for x in z):
        raise ValueError("six signed integer components required")
    return z


def support_size(z:Iterable[int])->int:
    return sum(x!=0 for x in _z6(z))


def shortest_event_count(z:Iterable[int])->int:
    return sum(abs(x) for x in _z6(z))


def spatial_norm_squared(z:Iterable[int])->int:
    return sum(x*x for x in _z6(z))


def shortest_path_multiplicity(z:Iterable[int])->int:
    z=_z6(z); m=shortest_event_count(z)
    out=factorial(m)
    for x in z: out//=factorial(abs(x))
    return out


def _weak_compositions(total:int,parts:int,prefix=()):
    if parts==1:
        yield prefix+(total,); return
    for k in range(total+1):
        yield from _weak_compositions(total-k,parts-1,prefix+(k,))


def endpoint_multiplicity(length:int,z:Iterable[int])->int:
    z=_z6(z)
    if type(length) is not int or length<0: raise ValueError("nonnegative integer length required")
    a=tuple(max(x,0) for x in z); b=tuple(max(-x,0) for x in z)
    base=sum(a)+sum(b); gap=length-base
    if gap<0 or gap%2: return 0
    K=gap//2; total=0
    for ks in _weak_compositions(K,6):
        denom=1
        for ai,bi,k in zip(a,b,ks): denom*=factorial(ai+k)*factorial(bi+k)
        total+=factorial(length)//denom
    return total


def endpoint_weight(
    length:int,
    z:Iterable[int],
    positive_weights:Sequence[Fraction|int],
    negative_weights:Sequence[Fraction|int],
)->Fraction:
    z=_z6(z); wp=tuple(map(Fraction,positive_weights)); wm=tuple(map(Fraction,negative_weights))
    if len(wp)!=6 or len(wm)!=6 or any(w<=0 for w in wp+wm):
        raise ValueError("six strictly positive exact weights per sign required")
    if type(length) is not int or length<0: raise ValueError("nonnegative integer length required")
    a=tuple(max(x,0) for x in z); b=tuple(max(-x,0) for x in z)
    base=sum(a)+sum(b); gap=length-base
    if gap<0 or gap%2: return Fraction(0)
    K=gap//2; total=Fraction(0)
    for ks in _weak_compositions(K,6):
        term=Fraction(factorial(length))
        for ai,bi,k,p,m in zip(a,b,ks,wp,wm):
            term*=p**(ai+k)*m**(bi+k)
            term/=factorial(ai+k)*factorial(bi+k)
        total+=term
    return total


def return_multiplicity(length:int)->int:
    return endpoint_multiplicity(length,(0,0,0,0,0,0))


def primitive_straight(z:Iterable[int])->bool:
    return support_size(z)==1


__all__=[
    "support_size","shortest_event_count","spatial_norm_squared",
    "shortest_path_multiplicity","endpoint_multiplicity","endpoint_weight",
    "return_multiplicity","primitive_straight",
]
