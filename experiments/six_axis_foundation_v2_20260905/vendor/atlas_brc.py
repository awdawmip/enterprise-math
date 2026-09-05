"""Exact six-label BRC trace/atlas research prototype (not a native metric).

Axis order is (AB, AC, AD, BC, BD, CD) = (L1,L3,L6,L5,L4,L2).
Four slice stars are lossless factorization charts, NOT relations setting
native positive-axis triads equal to the identity. Chart choices are gauges,
not additional physical path occurrences. Standard-library core; frame_lift
imports SymPy only when ordinary commutative matrix algebra is requested.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from typing import Iterable, Mapping

EDGES = tuple(combinations(range(4), 2))
EDGE_INDEX = {e: j for j, e in enumerate(EDGES)}
LINE_ORDER = ("L1", "L3", "L6", "L5", "L4", "L2")
STARS = tuple(tuple(j for j, e in enumerate(EDGES) if v in e) for v in range(4))
GROUP = tuple(permutations(range(4)))
IDENTITY = (0, 1, 2, 3)
ZERO = (0,) * 6


def naturals(values: Iterable[int], size: int) -> tuple[int, ...]:
    values = tuple(values)
    if len(values) != size or any(type(v) is not int or v < 0 for v in values):
        raise ValueError(f"expected {size} nonnegative integers, not bools/floats")
    return values


def permutation(g: Iterable[int]) -> tuple[int, ...]:
    g = tuple(g)
    if len(g) != 4 or any(type(v) is not int for v in g) or set(g) != set(range(4)):
        raise ValueError("expected a permutation of 0,1,2,3")
    return g


def compose(g, h):
    g, h = permutation(g), permutation(h)
    return tuple(g[h[v]] for v in range(4))


def inverse(g):
    g = permutation(g)
    return tuple(g.index(v) for v in range(4))


def edge_action(g):
    g = permutation(g)
    return tuple(EDGE_INDEX[tuple(sorted((g[u], g[v])))] for u, v in EDGES)


def rotate_axes(n, g):
    n = naturals(n, 6)
    out = [0] * 6
    for old, new in enumerate(edge_action(g)):
        out[new] = n[old]
    return tuple(out)


def rotate_slices(k, g):
    k, g = naturals(k, 4), permutation(g)
    out = [0] * 4
    for v in range(4):
        out[g[v]] = k[v]
    return tuple(out)


def decode(residual, extracted):
    r, k = naturals(residual, 6), naturals(extracted, 4)
    return tuple(r[j] + k[u] + k[v] for j, (u, v) in enumerate(EDGES))


def residual(n, k):
    n, k = naturals(n, 6), naturals(k, 4)
    r = tuple(n[j] - k[u] - k[v] for j, (u, v) in enumerate(EDGES))
    if min(r) < 0:
        raise ValueError("infeasible chart factorization")
    return r


def seven_bounds(n):
    n = naturals(n, 6)
    return (n[0]+n[5], n[1]+n[4], n[2]+n[3],
            *(sum(n[e] for e in star) for star in STARS))


def exceptional_base(n):
    """Return b iff n_uv=b_u+b_v+1 with b in N^4; otherwise None."""
    n = naturals(n, 6)
    num = n[0] + n[1] - n[3] - 1
    if num % 2:
        return None
    a = num // 2
    b = (a, n[0]-a-1, n[1]-a-1, n[2]-a-1)
    if min(b) < 0 or any(n[j] != b[u]+b[v]+1 for j,(u,v) in enumerate(EDGES)):
        return None
    return b


@dataclass(frozen=True)
class AtlasFibre:
    """Succinct ALL-optimal integer chart fibre; does not pick a gauge.

    It represents k>=0, k_u+k_v<=n_uv, sum(k)=optimum. The stored
    native trace grade is n, not its smaller residual nor a carrier endpoint.
    """
    axes: tuple[int, ...]
    optimum: int
    bounds: tuple[int, ...]
    exceptional: tuple[int, ...] | None

    def contains(self, k) -> bool:
        k = naturals(k, 4)
        return sum(k) == self.optimum and all(
            k[u]+k[v] <= self.axes[j] for j,(u,v) in enumerate(EDGES))

    def enumerate(self, *, max_box: int = 1_000_000):
        """Optional bounded audit only; normal compilation does not enumerate."""
        upper = [min(self.axes[e] for e in STARS[v]) for v in range(4)]
        size = 1
        for v in upper:
            size *= v+1
        if type(max_box) is not int or max_box < 1 or size > max_box:
            raise ValueError("audit box exceeds explicit enumeration budget")
        return tuple(k for k in product(*(range(v+1) for v in upper)) if self.contains(k))


def compile_fibre(n) -> AtlasFibre:
    """Seven-bound/parity formula: constant count of exact integer operations."""
    n = naturals(n, 6)
    bounds = seven_bounds(n)
    b = exceptional_base(n)
    return AtlasFibre(n, min(bounds)-int(b is not None), bounds, b)


@dataclass(frozen=True)
class BranchKey:
    """A typed compressed path key, not a complete ordered path witness.

    Retains exact positive weight, all six step-count labels, resulting
    relative frame, and original operation count. Lossless for this declared
    observer and future concatenation, not for arbitrary history observers.
    """
    weight: Fraction = Fraction(1)
    axes: tuple[int, ...] = ZERO
    frame: tuple[int, ...] = IDENTITY
    length: int = 0

    def __post_init__(self):
        if isinstance(self.weight, bool) or not isinstance(self.weight, (int,Fraction)):
            raise TypeError("weight must be an exact int/Fraction")
        if self.weight <= 0:
            raise ValueError("positive-branch carrier requires strictly positive weight")
        object.__setattr__(self, 'weight', Fraction(self.weight))
        object.__setattr__(self, 'axes', naturals(self.axes, 6))
        object.__setattr__(self, 'frame', permutation(self.frame))
        if type(self.length) is not int or self.length < 0:
            raise ValueError("operation count must be a nonnegative integer")

    def then(self, other: 'BranchKey') -> 'BranchKey':
        if not isinstance(other, BranchKey):
            raise TypeError("composition requires another BranchKey")
        shifted = rotate_axes(other.axes, self.frame)
        return BranchKey(self.weight*other.weight,
                         tuple(a+b for a,b in zip(self.axes,shifted)),
                         compose(self.frame,other.frame), self.length+other.length)

    def relabel(self, g) -> 'BranchKey':
        return BranchKey(self.weight, rotate_axes(self.axes,g),
                         compose(compose(g,self.frame),inverse(g)), self.length)


def compression_carry(first: BranchKey, second: BranchKey) -> int:
    """Canonical scalar carry for framed concatenation, not a full state.

    Chart certificates must still retain six grades and frame. This
    nonnegative carry satisfies the monoid 2-cocycle identity exactly.
    """
    if not isinstance(first, BranchKey) or not isinstance(second, BranchKey):
        raise TypeError("carry requires two typed BranchKey states")
    return (compile_fibre(first.then(second).axes).optimum
            - compile_fibre(first.axes).optimum
            - compile_fibre(second.axes).optimum)


Histogram = dict[BranchKey, int]


def validate_histogram(h: Mapping[BranchKey,int]) -> None:
    if any(not isinstance(k, BranchKey) or type(c) is not int or c <= 0 for k,c in h.items()):
        raise ValueError("histogram requires BranchKey keys and positive integer multiplicities")


def add(a: Mapping[BranchKey,int], b: Mapping[BranchKey,int]) -> Histogram:
    validate_histogram(a); validate_histogram(b)
    out = dict(a)
    for k,c in b.items():
        out[k] = out.get(k,0)+c
    return out


def multiply(a: Mapping[BranchKey,int], b: Mapping[BranchKey,int]) -> Histogram:
    validate_histogram(a); validate_histogram(b)
    out: Histogram = {}
    for x,c in a.items():
        for y,d in b.items():
            k = x.then(y)
            out[k] = out.get(k,0)+c*d
    return out


def relabel(h: Mapping[BranchKey,int], g) -> Histogram:
    validate_histogram(h); permutation(g)
    return {k.relabel(g): c for k,c in h.items()}


def weight_histogram(h: Mapping[BranchKey,int]) -> dict[Fraction,int]:
    validate_histogram(h)
    out: dict[Fraction,int] = {}
    for k,c in h.items():
        out[k.weight] = out.get(k.weight,0)+c
    return out


def moment(h: Mapping[BranchKey,int], m: int) -> Fraction:
    validate_histogram(h)
    if type(m) is not int or m < 0:
        raise ValueError("moment order must be a nonnegative integer")
    return sum((c*k.weight**m for k,c in h.items()),Fraction(0))


def sector_norm_squared(axes, vertex: int) -> int:
    """Only the established two-active-axis sector readout; NOT a 6D metric."""
    n = naturals(axes,6)
    if type(vertex) is not int or not 0 <= vertex < 4:
        raise ValueError("invalid declared slice")
    if any(n[e] for e in range(6) if e not in STARS[vertex]):
        raise ValueError("trace is not confined to the declared slice")
    if sum(n[e] > 0 for e in STARS[vertex]) > 2:
        raise ValueError("not a primitive two-active-axis sector")
    return sum(n[e]**2 for e in STARS[vertex])


def frame_lift(state_count: int, edges, x, z, *, frames=GROUP, moment_order: int = 1):
    """Fixed-moment commutative matrix for finite framed transitions.

    Each edge is (source,target,BranchKey,multiplicity). Genuine transitions
    must have positive original length. Signed determinants are algebraic
    certificates, not signed branch masses. The finite frame set must be a
    subgroup containing every edge frame. Full atlas has 24 frames.
    """
    import sympy as s
    if type(state_count) is not int or state_count < 1 or len(x) != 6:
        raise ValueError("positive state count and six symbols required")
    if type(moment_order) is not int or moment_order < 0:
        raise ValueError("moment order must be a nonnegative integer")
    frames = tuple(permutation(g) for g in frames)
    if len(set(frames)) != len(frames) or IDENTITY not in frames:
        raise ValueError("frame list must contain distinct frames and identity")
    fs = set(frames)
    if any(compose(g,h) not in fs for g in frames for h in frames):
        raise ValueError("frames must be a group")
    edges = tuple(edges)
    index = {(i,g): i*len(frames)+j for i in range(state_count) for j,g in enumerate(frames)}
    mat = s.zeros(len(index))
    for i,j,key,c in edges:
        if type(i) is not int or type(j) is not int or not 0<=i<state_count or not 0<=j<state_count:
            raise ValueError("state outside declared range")
        validate_histogram({key:c})
        if key.length < 1 or key.frame not in fs:
            raise ValueError("proper original length and a frame in the subgroup required")
        w = s.Rational(key.weight.numerator,key.weight.denominator)**moment_order
        for g in frames:
            grade = rotate_axes(key.axes,g)
            value = c*w*z**key.length*s.prod(a**b for a,b in zip(x,grade))
            mat[index[i,g],index[j,compose(g,key.frame)]] += value
    return mat,index
