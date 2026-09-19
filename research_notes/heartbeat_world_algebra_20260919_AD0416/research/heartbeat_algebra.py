"""Research-only arithmetic adapter for a declared X6 radix heartbeat.

The world's name/dimensions are binding user definitions; this particular ring
is an optional construction after choosing a chart anchor, axis order and b.
No final-Cell codec, physical clock inverse or new top-level BRC family.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm
from typing import Sequence
from enterprise_math.brc_transport import Affine, EffectHistogram, inv, matrix, mv, euclidean_digits

Vec = tuple[int, ...]
ZERO: Vec = (0,) * 6
ONE: Vec = (1, 0, 0, 0, 0, 0)
LAM: Vec = (0, 1, 0, 0, 0, 0)

def integer(x: int) -> int:
    if type(x) is not int:
        raise TypeError('integer required (not bool or float)')
    return x

def vector(x: Sequence[int]) -> Vec:
    result = tuple(integer(v) for v in x)
    if len(result) != 6:
        raise ValueError('exactly six raw native displacement components required')
    return result

def radix(b: int) -> int:
    if integer(b) < 2:
        raise ValueError('radix must be >=2')
    return b

def add(x: Vec, y: Vec) -> Vec:
    return tuple(a+b for a,b in zip(vector(x), vector(y)))

def neg(x: Vec) -> Vec:
    return tuple(-a for a in vector(x))

def scale(n: int, x: Vec) -> Vec:
    return tuple(integer(n)*a for a in vector(x))

def beat(x: Vec, b: int = 2) -> Vec:
    x, b = vector(x), radix(b)
    return (b*x[-1],) + x[:-1]

def beats(x: Vec, k: int, b: int = 2) -> Vec:
    x, b = vector(x), radix(b)
    if integer(k) < 0:
        raise ValueError('negative time is not a forward heartbeat')
    cycles, phase = divmod(k, 6)
    x = scale(b**cycles, x)
    for _ in range(phase):
        x = beat(x, b)
    return x

def multiply(x: Vec, y: Vec, b: int = 2) -> Vec:
    """Z[L]/(L^6-b), an integer coordinate ring, not intrinsic Cell multiplication."""
    x, y, b = vector(x), vector(y), radix(b)
    out = [0]*6
    for i, a in enumerate(x):
        for j, c in enumerate(y):
            turns, slot = divmod(i+j, 6)
            out[slot] += a*c*(b if turns else 1)
    return tuple(out)

def multiplication_matrix(x: Vec, b: int = 2):
    columns = [multiply(x, tuple(int(i == j) for i in range(6)), b) for j in range(6)]
    return matrix(tuple(zip(*columns)))

def norm(x: Vec, b: int = 2) -> int:
    """Determinant of multiplication. This is not the spatial metric norm."""
    a = [list(row) for row in multiplication_matrix(x, b)]
    det = Fraction(1)
    for i in range(6):
        p = next((j for j in range(i, 6) if a[j][i]), None)
        if p is None:
            return 0
        if p != i:
            a[i], a[p] = a[p], a[i]
            det = -det
        pivot = a[i][i]
        det *= pivot
        for j in range(i+1, 6):
            ratio = a[j][i]/pivot
            for k in range(i+1, 6):
                a[j][k] -= ratio*a[i][k]
    if det.denominator != 1:
        raise AssertionError('integer multiplication matrix has noninteger determinant')
    return det.numerator

def divide_readout(x: Vec, y: Vec, b: int = 2) -> tuple[Vec, int]:
    """Exact rational readout numerator/denominator. Singular divisors reject.

Even for b=2, output denominator>1 is NOT a valid fractional native Cell.
"""
    x, y = vector(x), vector(y)
    if y == ZERO:
        raise ZeroDivisionError('zero divisor argument')
    q = mv(inv(multiplication_matrix(y, b)), tuple(Fraction(v) for v in x))
    d = lcm(*(v.denominator for v in q))
    n = tuple(int(v*d) for v in q)
    g = gcd(d, *n)
    return tuple(v//g for v in n), d//g

def analyze(x: Vec, b: int = 2) -> tuple[Vec, int]:
    x, b = vector(x), radix(b)
    q, digits = euclidean_digits(x[0], (b,))
    return x[1:] + (q,), digits[0]

def synthesize(q: Vec, r: int, b: int = 2) -> Vec:
    b = radix(b)
    if not 0 <= integer(r) < b:
        raise ValueError('residue out of radix')
    return add(beat(q, b), scale(r, ONE))

def lift_add(q: Vec, r: int, p: Vec, s: int, b: int = 2) -> tuple[Vec, int]:
    synthesize(q, r, b); synthesize(p, s, b)
    c, digit = divmod(r+s, b)
    return add(add(q, p), (0,0,0,0,0,c)), digit

def lift_subtract(q: Vec, r: int, p: Vec, s: int, b: int = 2) -> tuple[Vec, int]:
    synthesize(q, r, b); synthesize(p, s, b)
    c, digit = divmod(r-s, b)
    return add(add(q, neg(p)), (0,0,0,0,0,c)), digit

def lift_multiply(q: Vec, r: int, p: Vec, s: int, b: int = 2) -> tuple[Vec, int]:
    synthesize(q, r, b); synthesize(p, s, b)
    c, digit = divmod(r*s, b)
    coarse = add(beat(multiply(q,p,b), b), add(scale(s,q), scale(r,p)))
    return add(coarse, (0,0,0,0,0,c)), digit

@dataclass(frozen=True)
class TimedAffine:
    """Typed forward arrow t->t+duration; spatial effect alone is a quotient."""
    start: int
    duration: int
    effect: Affine

    def __post_init__(self):
        if integer(self.start) < 0 or integer(self.duration) < 0:
            raise ValueError('nonnegative event tick and duration required')
        if not isinstance(self.effect, Affine) or self.effect.dim != 6:
            raise ValueError('six-dimensional affine effect required')

    @property
    def end(self):
        return self.start + self.duration

    def then(self, later: 'TimedAffine') -> 'TimedAffine':
        if self.end != later.start:
            raise ValueError('time ports do not match')
        return TimedAffine(self.start, self.duration+later.duration, self.effect.then(later.effect))

    def apply(self, event):
        t, z = event
        integer(t)
        if t != self.start:
            raise ValueError('event time does not match arrow source')
        return self.end, self.effect.apply(vector(z))

@dataclass(frozen=True)
class TimedPacket:
    """Existing positive BRC effects, with explicit temporal ports."""
    start: int
    duration: int
    effects: EffectHistogram

    def __post_init__(self):
        if integer(self.start) < 0 or integer(self.duration) < 0:
            raise ValueError('nonnegative time required')
        if not isinstance(self.effects, EffectHistogram) or self.effects.dim != 6:
            raise ValueError('six-axis BRC effect histogram required')

    def then(self, later: 'TimedPacket') -> 'TimedPacket':
        if self.start+self.duration != later.start:
            raise ValueError('time ports do not match')
        return TimedPacket(self.start,self.duration+later.duration,self.effects.then(later.effects))

    def alternatives(self, other: 'TimedPacket') -> 'TimedPacket':
        if (self.start,self.duration) != (other.start,other.duration):
            raise ValueError('parallel alternatives must have common time ports')
        return TimedPacket(self.start,self.duration,self.effects.alternatives(other.effects))
