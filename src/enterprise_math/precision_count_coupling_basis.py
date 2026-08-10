"""R004 fractionless COUNT coupling residual basis.

Finite exact reference helpers.  Generic contingency-table marginal lattices,
Smith normal form, and integer module theory are prior mathematics.
"""
from __future__ import annotations
from itertools import product
from math import prod
from typing import Sequence, Tuple

Cell = Tuple[int, ...]

def cells(shape: Sequence[int]) -> Tuple[Cell, ...]:
    if any(n <= 0 for n in shape):
        raise ValueError("axis sizes must be positive")
    return tuple(product(*(range(n) for n in shape)))

def coupling_cells(shape: Sequence[int], base: Sequence[int] | None = None) -> Tuple[Cell, ...]:
    shape = tuple(shape)
    base = tuple(0 for _ in shape) if base is None else tuple(base)
    if len(base) != len(shape) or any(not (0 <= b < n) for b, n in zip(base, shape)):
        raise ValueError("invalid base")
    return tuple(c for c in cells(shape) if sum(x != b for x, b in zip(c, base)) >= 2)

def coupling_dimension(shape: Sequence[int]) -> int:
    shape = tuple(shape)
    return prod(shape) - sum(shape) + len(shape) - 1

def residual_coefficients(shape: Sequence[int], coefficients: Sequence[int], base: Sequence[int] | None = None) -> Tuple[int, ...]:
    cs = cells(shape)
    if len(coefficients) != len(cs):
        raise ValueError("coefficient length mismatch")
    base = tuple(0 for _ in shape) if base is None else tuple(base)
    index = {c:i for i,c in enumerate(cs)}
    c0 = coefficients[index[base]]
    out=[]
    for c in cs:
        value = coefficients[index[c]]
        approx = c0
        for axis, val in enumerate(c):
            if val != base[axis]:
                star=list(base); star[axis]=val
                approx += coefficients[index[tuple(star)]] - c0
        out.append(value - approx)
    return tuple(out)

def coupling_residual(shape: Sequence[int], coefficients: Sequence[int], base: Sequence[int] | None = None) -> Tuple[int, ...]:
    residual = residual_coefficients(shape, coefficients, base)
    cs = cells(shape)
    cc = set(coupling_cells(shape, base))
    return tuple(residual[i] for i,c in enumerate(cs) if c in cc)

def reconstruct_joint(shape: Sequence[int], marginals: Sequence[Sequence[int]], coupling_counts: Sequence[int], base: Sequence[int] | None = None) -> Tuple[int, ...]:
    shape=tuple(shape)
    base=tuple(0 for _ in shape) if base is None else tuple(base)
    if len(marginals)!=len(shape) or any(len(m)!=n for m,n in zip(marginals,shape)):
        raise ValueError("invalid marginals")
    cc=coupling_cells(shape,base)
    if len(coupling_counts)!=len(cc):
        raise ValueError("coupling count length mismatch")
    table={c:v for c,v in zip(cc,coupling_counts)}
    for axis,n in enumerate(shape):
        for val in range(n):
            if val==base[axis]: continue
            star=list(base); star[axis]=val; star=tuple(star)
            used=sum(v for c,v in table.items() if c[axis]==val)
            table[star]=marginals[axis][val]-used
    total=sum(marginals[0])
    table[base]=total-sum(table.values())
    return tuple(table[c] for c in cells(shape))

def birth_depth(invariant: int, p: int, cap: int) -> int:
    if invariant == 0 or p <= 1 or cap < 0:
        raise ValueError("invalid arguments")
    x=abs(invariant); v=0
    while x % p == 0:
        x//=p; v+=1
    return max(0, cap-v)
