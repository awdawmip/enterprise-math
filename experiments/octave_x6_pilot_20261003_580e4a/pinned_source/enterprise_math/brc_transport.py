"""BRC affine-effect transport subtool: exact positive branch weights with affine actions.

Extracted from the 2026-09-19 research prototype. This module is a reusable
T0_BRC subtool; it does not promote the associated research claims to Foundation.
Each atom jointly retains (positive rational weight, affine action, multiplicity).
This effect histogram is not complete labeled-path provenance. Its safe interface
is fixed-weight, total affine effects with no hidden/path-label-sensitive access.
Use state-indexed kernels for conditional weights, partial actions or typed ports.

Arithmetic uses integers/Fractions only. Moment compression is exact only for
observations of degree <= 2 and the declared affine future family.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence
from .brc_histogram import WeightHistogram

Q = Fraction
Vector = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def rational(x: int | Fraction) -> Fraction:
    if isinstance(x, bool) or not isinstance(x, (int, Fraction)):
        raise TypeError("exact int or Fraction required; no float or bool")
    return Fraction(x)


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    result = tuple(tuple(rational(x) for x in row) for row in rows)
    if not result or not result[0] or any(len(r) != len(result[0]) for r in result):
        raise ValueError("nonempty rectangular matrix required")
    return result


def eye(n: int) -> Matrix:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("positive integer dimension required")
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def transpose(a: Matrix) -> Matrix:
    return tuple(zip(*a))


def mm(a: Matrix, b: Matrix) -> Matrix:
    if len(a[0]) != len(b):
        raise ValueError("matrix dimension mismatch")
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q())
                       for j in range(len(b[0]))) for i in range(len(a)))


def mv(a: Matrix, v: Vector) -> Vector:
    if len(a[0]) != len(v):
        raise ValueError("vector dimension mismatch")
    return tuple(sum((x*y for x,y in zip(row,v)), Q()) for row in a)


def ma(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix dimension mismatch")
    return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))


def sm(c: int | Fraction, a: Matrix) -> Matrix:
    c = rational(c)
    return tuple(tuple(c*x for x in r) for r in a)


def inv(a: Matrix) -> Matrix:
    """Exact Gauss-Jordan inverse. Rational readout, not an integer-lattice license."""
    n = len(a)
    if len(a[0]) != n:
        raise ValueError("square matrix required")
    work = [list(r) + list(s) for r,s in zip(a, eye(n))]
    for col in range(n):
        pivot = next((r for r in range(col,n) if work[r][col]), None)
        if pivot is None:
            raise ValueError("singular affine linear part")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [x/scale for x in work[col]]
        for r in range(n):
            if r != col:
                scale = work[r][col]
                work[r] = [x-scale*y for x,y in zip(work[r], work[col])]
    return tuple(tuple(r[n:]) for r in work)


def mpow(a: Matrix, n: int) -> Matrix:
    if isinstance(n,bool) or not isinstance(n,int) or n < 0:
        raise ValueError("nonnegative integer exponent required")
    out = eye(len(a))
    while n:
        if n & 1:
            out = mm(out,a)
        a = mm(a,a)
        n //= 2
    return out


@dataclass(frozen=True, order=True)
class Affine:
    a: Matrix
    b: Vector

    def __post_init__(self) -> None:
        normalized = matrix(self.a)
        offset = tuple(rational(x) for x in self.b)
        if len(normalized) != len(normalized[0]) or len(normalized) != len(offset):
            raise ValueError("square linear part and matching offset required")
        object.__setattr__(self, 'a', normalized)
        object.__setattr__(self, 'b', offset)

    @property
    def dim(self) -> int:
        return len(self.b)

    @classmethod
    def identity(cls, dim: int) -> 'Affine':
        return cls(eye(dim), (Q(),)*dim)

    def apply(self, x: Sequence[int | Fraction]) -> Vector:
        v = mv(self.a, tuple(rational(t) for t in x))
        return tuple(y+z for y,z in zip(v,self.b))

    def then(self, later: 'Affine') -> 'Affine':
        """First self, then later: (B,c) o (A,b) = (BA, Bb+c)."""
        if self.dim != later.dim:
            raise ValueError("action dimensions differ")
        return Affine(mm(later.a,self.a), later.apply(self.b))

    def inverse(self) -> 'Affine':
        ai = inv(self.a)
        return Affine(ai, tuple(-x for x in mv(ai,self.b)))

    def homogeneous(self) -> Matrix:
        return tuple(tuple(r)+(b,) for r,b in zip(self.a,self.b)) + ((Q(),)*self.dim+(Q(1),),)


@dataclass(frozen=True)
class EffectHistogram:
    dim: int
    entries: tuple[tuple[Fraction, Affine, int], ...]

    def __post_init__(self) -> None:
        eye(self.dim)
        seen = set()
        for weight, action, count in self.entries:
            if not isinstance(weight,Fraction) or weight <= 0:
                raise ValueError("weights must be positive Fractions")
            if action.dim != self.dim:
                raise ValueError("action dimension mismatch")
            if isinstance(count,bool) or not isinstance(count,int) or count < 1:
                raise ValueError("multiplicity must be a positive integer")
            if (weight,action) in seen:
                raise ValueError("joint (weight,action) duplicates must be coalesced")
            seen.add((weight,action))
        if self.entries != tuple(sorted(self.entries, key=lambda t:(t[0],t[1]))):
            raise ValueError("entries must use canonical joint ordering")

    @classmethod
    def from_terms(cls, dim: int, terms: Iterable[tuple[int | Fraction, Affine, int]]) -> 'EffectHistogram':
        counts = {}
        for w,a,c in terms:
            w = rational(w)
            if w <= 0 or a.dim != dim:
                raise ValueError("positive weight and matching dimension required")
            if isinstance(c,bool) or not isinstance(c,int) or c < 0:
                raise ValueError("nonnegative integer multiplicity required")
            if c:
                counts[w,a] = counts.get((w,a),0)+c
        return cls(dim, tuple((w,a,c) for (w,a),c in sorted(counts.items())))

    @classmethod
    def unit(cls, dim: int) -> 'EffectHistogram':
        return cls.from_terms(dim, [(1,Affine.identity(dim),1)])

    @classmethod
    def zero(cls, dim: int) -> 'EffectHistogram':
        return cls(dim,())

    def alternatives(self, other: 'EffectHistogram') -> 'EffectHistogram':
        if self.dim != other.dim:
            raise ValueError("packet dimensions differ")
        return self.from_terms(self.dim, self.entries+other.entries)

    def then(self, later: 'EffectHistogram') -> 'EffectHistogram':
        if self.dim != later.dim:
            raise ValueError("packet dimensions differ")
        return self.from_terms(self.dim, ((u*v, a.then(b), c*d)
            for u,a,c in self.entries for v,b,d in later.entries))

    def forget_effects(self) -> WeightHistogram:
        counts = {}
        for w,_a,c in self.entries:
            counts[w] = counts.get(w,0)+c
        return WeightHistogram.from_counts(counts)

    def evaluate(self, x: Sequence[int | Fraction]) -> dict[Vector, WeightHistogram]:
        counts = {}
        for w,a,c in self.entries:
            y = a.apply(x)
            cell = counts.setdefault(y,{})
            cell[w] = cell.get(w,0)+c
        return {y:WeightHistogram.from_counts(h) for y,h in counts.items()}

    def moment_action(self, moment: Matrix) -> Matrix:
        n = self.dim+1
        if len(moment) != n or len(moment[0]) != n:
            raise ValueError("homogeneous moment dimension mismatch")
        out = sm(0,eye(n))
        for w,a,c in self.entries:
            h = a.homogeneous()
            out = ma(out, sm(w*c,mm(mm(h,moment),transpose(h))))
        return out


def point_moment(x: Sequence[int | Fraction]) -> Matrix:
    v = tuple(rational(t) for t in x)+(Q(1),)
    return tuple(tuple(a*b for b in v) for a in v)


def explicit_moment(output: dict[Vector, WeightHistogram]) -> Matrix:
    if not output:
        raise ValueError("nonempty output required; zero moment dimension is ambiguous")
    dim = len(next(iter(output)))
    out = sm(0,eye(dim+1))
    for x,h in output.items():
        out = ma(out,sm(h.total_mass,point_moment(x)))
    return out


def factor_defect(a_m: Matrix, a_n: Matrix, a_mn: Matrix) -> Matrix:
    return mm(mm(a_m,a_n),inv(a_mn))


def euclidean_digits(x: int, bases: Sequence[int]) -> tuple[int, tuple[int,...]]:
    if isinstance(x,bool) or not isinstance(x,int):
        raise TypeError("integer x required")
    residues = []
    for b in bases:
        if isinstance(b,bool) or not isinstance(b,int) or b < 2:
            raise ValueError("bases must be integers >=2")
        x,r = divmod(x,b)
        residues.append(r)
    return x,tuple(residues)


def recompose(q: int, residues: Sequence[int], bases: Sequence[int]) -> int:
    if isinstance(q,bool) or not isinstance(q,int) or len(residues) != len(bases):
        raise ValueError("integer quotient and matching digit lengths required")
    for r,b in reversed(tuple(zip(residues,bases))):
        if isinstance(b,bool) or not isinstance(b,int) or b < 2:
            raise ValueError("bases must be integers >=2")
        if isinstance(r,bool) or not isinstance(r,int) or not 0 <= r < b:
            raise ValueError("digit outside its radix")
        q = b*q+r
    return q


@dataclass(frozen=True)
class MomentState:
    dimension: int
    upper: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        eye(self.dimension)
        n = self.dimension+1
        values = tuple(rational(x) for x in self.upper)
        if len(values) != n*(n+1)//2:
            raise ValueError("incorrect packed symmetric moment length")
        object.__setattr__(self, "upper", values)

    @classmethod
    def from_matrix(cls, moment: Matrix) -> "MomentState":
        n = len(moment)
        if n < 2 or any(len(r) != n for r in moment) or moment != transpose(moment):
            raise ValueError("symmetric homogeneous matrix of size >=2 required")
        return cls(n-1,tuple(moment[i][j] for i in range(n) for j in range(i,n)))

    @classmethod
    def from_point(cls, x: Sequence[int | Fraction]) -> "MomentState":
        return cls.from_matrix(point_moment(x))

    def to_matrix(self) -> Matrix:
        n = self.dimension+1
        out = [[Q() for _ in range(n)] for _ in range(n)]
        k = 0
        for i in range(n):
            for j in range(i,n):
                out[i][j] = out[j][i] = self.upper[k]
                k += 1
        return tuple(tuple(r) for r in out)

    def then(self, packet: EffectHistogram) -> "MomentState":
        if packet.dim != self.dimension:
            raise ValueError("moment/action dimensions differ")
        return self.from_matrix(packet.moment_action(self.to_matrix()))
