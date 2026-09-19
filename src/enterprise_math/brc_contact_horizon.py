"""Exact finite-horizon contact observer for two tagged native-X6 positions.

Research T0/T6 domain adapter. Uses relative displacement d=y-x, and one
signed native unit move per action. A radius-h near/far abstraction is exact
with a decreasing remaining horizon; no fixed finite quotient covers all
horizons on unbounded space. FAR is NOT zero, an absent axis or a vanished
path. Past contacts, simultaneous two-particle steps, hidden velocity and
state-dependent motion require their own explicitly declared state.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import comb
from typing import Mapping
from .brc_residue_port import vector, natural
from .brc_histogram import WeightHistogram, histogram_serial, histogram_recoalesce

ZERO = (0,)*6
DIRECTIONS = tuple(tuple(sign if i == axis else 0 for i in range(6))
                   for axis in range(6) for sign in (-1, 1))


def l1(x) -> int:
    return sum(abs(v) for v in vector(x))


def contact_class_count(h: int) -> int:
    """Exact coarsest h-future contact classes on Z^6: the L1 ball plus FAR."""
    natural(h)
    return 2 + sum(2**s * comb(6, s) * comb(h, s) for s in range(1, min(6, h)+1))


def native_l1_ball(h: int, *, limit=1_000_000):
    natural(h)
    if contact_class_count(h)-1 > natural(limit):
        raise ValueError('explicit native ball exceeds enumeration limit')
    def fill(left, slots):
        if slots == 0:
            yield ()
        else:
            for v in range(-left, left+1):
                for rest in fill(left-abs(v), slots-1):
                    yield (v,)+rest
    return tuple(fill(h, 6))


@dataclass(frozen=True)
class ContactState:
    remaining: int
    displacement: tuple[int, ...] | None

    def __post_init__(self):
        natural(self.remaining)
        if self.displacement is not None:
            displacement = vector(self.displacement)
            if l1(displacement) > self.remaining:
                raise ValueError('store outside-ball displacements as FAR, not concrete states')
            object.__setattr__(self, 'displacement', displacement)

    @classmethod
    def encode(cls, displacement, remaining: int):
        displacement = vector(displacement)
        natural(remaining)
        return cls(remaining, displacement if l1(displacement) <= remaining else None)

    @classmethod
    def from_pair(cls, x, y, remaining: int):
        x, y = vector(x), vector(y)
        return cls.encode(tuple(b-a for a, b in zip(x, y)), remaining)

    @property
    def contact(self) -> bool:
        return self.displacement == ZERO

    def advance(self, delta):
        delta = vector(delta)
        if l1(delta) != 1:
            raise ValueError('one signed native primitive step required')
        if not self.remaining:
            raise ValueError('contact horizon exhausted')
        h = self.remaining-1
        if self.displacement is None:
            return ContactState(h, None)
        return ContactState.encode(tuple(a+b for a, b in zip(self.displacement, delta)), h)


def distinguishing_contact_word(left: ContactState, right: ContactState, *, limit=1_000_000):
    """Construct a permitted suffix separating distinct same-horizon classes."""
    if left.remaining != right.remaining or left == right:
        raise ValueError('distinct equal-horizon states required')
    d = left.displacement if left.displacement is not None else right.displacement
    if l1(d) > natural(limit):
        raise ValueError('explicit distinguishing word exceeds limit')
    word = []
    for axis, value in enumerate(d):
        step = tuple((-1 if value > 0 else 1) if j == axis else 0 for j in range(6))
        word.extend([step]*abs(value))
    return tuple(word)


def contact_push(states: Mapping[ContactState, WeightHistogram], moves):
    """Exact BRC weighted edges; same finite remaining-time port required.

    moves contains (relative_unit_step, weight, multiplicity), reused at each
    state in this call. This does not preserve the earlier contact HISTORY.
    Empty mass stays empty. A nonempty input at exhausted time is rejected.
    """
    if any(not isinstance(s, ContactState) or not isinstance(w, WeightHistogram)
           for s, w in states.items()):
        raise TypeError('ContactState -> WeightHistogram mapping required')
    if len({s.remaining for s in states}) > 1:
        raise ValueError('mixed remaining-time ports')
    if states and next(iter(states)).remaining == 0:
        raise ValueError('contact horizon exhausted')
    edges = []
    for delta, weight, count in moves:
        delta = vector(delta)
        if l1(delta) != 1:
            raise ValueError('one signed native primitive step required')
        # Existing histogram interface validates exact positive weights/counts.
        edge = WeightHistogram.from_counts({weight: count})
        if not edge.is_zero:
            edges.append((delta, edge))
    out = {}
    for state, histogram in states.items():
        if histogram.is_zero:
            continue
        for delta, edge in edges:
            target = state.advance(delta)
            result = histogram_serial(histogram, edge)
            out[target] = histogram_recoalesce(out[target], result) if target in out else result
    return out
