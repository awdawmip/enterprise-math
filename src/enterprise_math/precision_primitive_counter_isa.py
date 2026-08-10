"""R004 primitive counter ISA gap.

Finite exact reference helpers for comparing cell-addressable and aggregate
counter instruction surfaces over Z/p^K.
"""
from __future__ import annotations
from itertools import product
from typing import Sequence, Tuple

def _vp(x: int, p: int, cap: int) -> int:
    if x == 0:
        return cap
    x=abs(x); v=0
    while v < cap and x % p == 0:
        x//=p; v+=1
    return v

def coordinate_depths(rows: Sequence[Sequence[int]], p: int, cap: int) -> Tuple[int, ...]:
    if p <= 1 or cap < 1 or not rows:
        raise ValueError("invalid arguments")
    d=len(rows[0])
    if any(len(r)!=d for r in rows):
        raise ValueError("ragged matrix")
    return tuple(max(0, cap-min(_vp(r[j],p,cap) for r in rows)) for j in range(d))

def row_module(rows: Sequence[Sequence[int]], modulus: int) -> frozenset[Tuple[int,...]]:
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    rows=tuple(tuple(x % modulus for x in r) for r in rows)
    if not rows:
        return frozenset({()})
    d=len(rows[0])
    if any(len(r)!=d for r in rows):
        raise ValueError("ragged matrix")
    out=set()
    for coeffs in product(range(modulus), repeat=len(rows)):
        out.add(tuple(sum(a*r[j] for a,r in zip(coeffs,rows))%modulus for j in range(d)))
    return frozenset(out)

def exponent_mass_from_size(size: int, p: int) -> int:
    if size < 1 or p <= 1:
        raise ValueError("invalid arguments")
    m=0
    while size>1:
        if size%p:
            raise ValueError("size is not a p-power")
        size//=p; m+=1
    return m

def aggregate_mass(rows: Sequence[Sequence[int]], p: int, cap: int) -> int:
    return exponent_mass_from_size(len(row_module(rows,p**cap)),p)

def cell_mass(rows: Sequence[Sequence[int]], p: int, cap: int) -> int:
    return sum(coordinate_depths(rows,p,cap))

def isa_gap_mass(rows: Sequence[Sequence[int]], p: int, cap: int) -> int:
    return cell_mass(rows,p,cap)-aggregate_mass(rows,p,cap)
