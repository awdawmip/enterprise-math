"""R004 binary k-local primitive-ISA Pareto family."""
from __future__ import annotations
from math import comb, ceil

def storage_count(rank: int, locality: int) -> int:
    if not 1 <= locality <= rank:
        raise ValueError("need 1 <= locality <= rank")
    return sum(comb(rank,j) for j in range(1,locality+1))

def streaming_update_incidences(rank: int, locality: int) -> int:
    if not 1 <= locality <= rank:
        raise ValueError("need 1 <= locality <= rank")
    return sum(j*comb(rank,j) for j in range(1,locality+1))

def readout_depth(weight: int, locality: int) -> int:
    if weight < 0 or locality < 1:
        raise ValueError("invalid arguments")
    return ceil(weight/locality) if weight else 0

def max_readout_depth(rank: int, locality: int) -> int:
    return readout_depth(rank,locality)

def total_semantic_readout_length(rank: int, locality: int) -> int:
    if not 1 <= locality <= rank:
        raise ValueError("need 1 <= locality <= rank")
    return sum(comb(rank,w)*readout_depth(w,locality) for w in range(1,rank+1))
