"""R004 finite-field covering-code primitive ISA bridge.

Covering codes and length functions are prior coding theory.  This module only
packages the exact parity-check / null-program interpretation used by R004.
"""
from __future__ import annotations
from itertools import combinations
from math import comb, ceil
from typing import Sequence, Tuple

def hamming_ball_volume(q: int, length: int, radius: int) -> int:
    if q < 2 or length < 0 or not 0 <= radius <= length:
        raise ValueError("invalid arguments")
    return sum(comb(length,j)*(q-1)**j for j in range(radius+1))

def volume_lower_bound_length(q: int, rank: int, radius: int) -> int:
    if q < 2 or rank < 0 or radius < 1:
        raise ValueError("invalid arguments")
    s=rank
    while hamming_ball_volume(q,s,min(radius,s)) < q**rank:
        s+=1
    return s

def depth_one_exact_length(q: int, rank: int) -> int:
    if q < 2 or rank < 1:
        raise ValueError("invalid arguments")
    return (q**rank-1)//(q-1)

def one_redundant_radius(q: int, rank: int) -> int:
    if q < 2 or rank < 1:
        raise ValueError("invalid arguments")
    n=rank+1
    return n-ceil(n/q)

def binary_reachable(generators: Sequence[int], radius: int) -> frozenset[int]:
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    out={0}
    for j in range(1,min(radius,len(generators))+1):
        for inds in combinations(range(len(generators)),j):
            x=0
            for i in inds:
                x ^= generators[i]
            out.add(x)
    return frozenset(out)

def binary_covers(generators: Sequence[int], rank: int, radius: int) -> bool:
    if rank < 0 or any(g < 0 or g >= 2**rank for g in generators):
        raise ValueError("invalid generator")
    return len(binary_reachable(generators,radius)) == 2**rank

def binary_covering_radius(generators: Sequence[int], rank: int) -> int:
    for radius in range(len(generators)+1):
        if binary_covers(generators,rank,radius):
            return radius
    raise ValueError("generators do not span the semantic space")

def short_word_excess(q: int, rank: int, length: int, radius: int) -> int:
    return hamming_ball_volume(q,length,radius)-q**rank

def normalized_binary_search(rank: int, radius: int, length: int) -> Tuple[int, Tuple[int,...] | None]:
    """Exact small search up to GL(rank,2) by forcing the standard basis."""
    if length < rank:
        return 0,None
    basis=tuple(1<<i for i in range(rank))
    candidates=tuple(x for x in range(1,2**rank) if x not in basis)
    checked=0
    for extras in combinations(candidates,length-rank):
        checked+=1
        gens=basis+extras
        if binary_covers(gens,rank,radius):
            return checked,gens
    return checked,None
