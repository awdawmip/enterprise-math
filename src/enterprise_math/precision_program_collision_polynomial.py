"""R004/P011 collision polynomial and execution-depth shell decomposition."""
from __future__ import annotations
from math import comb
from typing import Mapping, Sequence, Tuple


def collision_hierarchy(multiplicities: Sequence[int]) -> Tuple[int, ...]:
    if any(n < 0 for n in multiplicities):
        raise ValueError("multiplicities must be nonnegative")
    maximum=max(multiplicities,default=0)
    return tuple(sum(comb(n,k) for n in multiplicities if n>=k) for k in range(maximum+1))


def multiplicity_histogram_from_collisions(collisions: Sequence[int]) -> Tuple[int, ...]:
    if not collisions:
        return ()
    M=len(collisions)-1
    h=[]
    for m in range(M+1):
        value=sum(((-1)**(k-m))*comb(k,m)*collisions[k] for k in range(m,M+1))
        if value < 0:
            raise ValueError("not a valid finite collision hierarchy")
        h.append(value)
    return tuple(h)


def transition_histogram(previous: Sequence[int], shell: Sequence[int]) -> Tuple[Tuple[Tuple[int,int],int], ...]:
    if len(previous)!=len(shell) or any(a<0 for a in previous) or any(b<0 for b in shell):
        raise ValueError("invalid transition data")
    counts={}
    for a,b in zip(previous,shell):
        counts[(a,b)]=counts.get((a,b),0)+1
    return tuple(sorted(counts.items()))


def collision_birth_components(previous: Sequence[int], shell: Sequence[int], order: int) -> Tuple[int, ...]:
    if order < 1 or len(previous)!=len(shell):
        raise ValueError("invalid arguments")
    out=[]
    for j in range(1,order+1):
        total=0
        for a,b in zip(previous,shell):
            if b>=j and a>=order-j:
                total += comb(b,j)*comb(a,order-j)
        out.append(total)
    return tuple(out)


def collision_increment(previous: Sequence[int], shell: Sequence[int], order: int) -> int:
    return sum(collision_birth_components(previous,shell,order))


def endpoint_increment(previous: Sequence[int], shell: Sequence[int], order: int) -> int:
    current=tuple(a+b for a,b in zip(previous,shell))
    return sum(comb(n,order) for n in current if n>=order) - sum(
        comb(n,order) for n in previous if n>=order
    )
