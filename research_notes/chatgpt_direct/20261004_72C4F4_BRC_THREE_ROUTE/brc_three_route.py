"""Provisional path-labelled extension of the pinned X6 Weighted-BRC model.

Branching is NOT a native three-force balance law. T/U retain their candidate
status. Positive path weights are never replaced by signed readout amplitudes.
Source and branch identities are separate; no phase or origin is discarded.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable
import brc_x6_extension as e

@dataclass(frozen=True)
class Path:
    state: e.Branch
    choices: tuple[int, ...] = ()

    @property
    def key(self):
        return self.state.source_id, self.choices


def initial(source: str, x, weight=1) -> tuple[Path, ...]:
    return (Path(e.branch(source, x, weight)),)


def disjoint_union(*families: Iterable[Path]) -> tuple[Path, ...]:
    paths = tuple(path for family in families for path in family)
    if len({p.key for p in paths}) != len(paths):
        raise ValueError('path identity collision: preserve root source and choices')
    return paths


def act(paths: Iterable[Path], word: Iterable[str]) -> tuple[Path, ...]:
    word = tuple(word)
    if any(a not in ('T', 'U') for a in word):
        raise ValueError('common action alphabet is exactly T,U')
    out = []
    for path in paths:
        b = path.state
        for a in word:
            b = e.transform(b, a)
        out.append(Path(b, path.choices))
    return tuple(out)


def three_route(paths: Iterable[Path], weights=(Fraction(1,3),)*3,
                *, max_paths: int = 100_000) -> tuple[Path, ...]:
    """Positive alternatives I, T^4, T^8 with exact normalized weights.

    No averaged coordinate is inserted as a native Cell. B0/B1/B2 in history
    label branching events, not primitive spatial steps or physical time.
    """
    paths = tuple(paths)
    weights = tuple(weights)
    if any(isinstance(w, bool) or not isinstance(w, (int, Fraction)) for w in weights):
        raise TypeError('weights must be exact int/Fraction, not floating input')
    if type(max_paths) is not int or max_paths < 1:
        raise ValueError('positive integer path budget required')
    weights = tuple(Fraction(w) for w in weights)
    if len(weights) != 3 or any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError('three nonnegative rational weights summing to one required')
    if len(paths)*sum(w > 0 for w in weights) > max_paths:
        raise ValueError('explicit path budget exceeded; no silent compression')
    out = []
    for path in paths:
        for j, w in enumerate(weights):
            if not w:
                continue
            old = path.state
            b = e.Branch(old.source_id, old.x,
                         e.call('cwm_propagate', old.cwm, e.call('cwm_edge', w)),
                         old.operation_history + (f'B{j}',))
            for _ in range(4*j):
                b = e.transform(b, 'T')
            out.append(Path(b, path.choices+(j,)))
    return disjoint_union(out)


def positive_summary(paths):
    return e.positive_summary(p.state for p in paths)


def c_observer(paths):
    return e.weighted_observer(tuple(p.state for p in paths))


def h_observer(paths):
    paths = tuple(paths)
    return tuple(sum((p.state.cwm.total*e.c4(p.state)[j] for p in paths), Fraction(0))
                 for j in range(2))


def raw_first_moment(paths):
    paths = tuple(paths)
    return tuple(sum((p.state.cwm.total*p.state.x[j] for p in paths), Fraction(0))
                 for j in range(6))


def gluing_defect(c, h):
    values = tuple(c)+tuple(h)
    if len(c) != 4 or len(h) != 2 or any(type(v) is not int for v in values):
        raise TypeError('gluing defect is an INTEGER carrier check, not a weighted mean')
    return ((h[0]-c[0]+c[2]) % 3, (h[1]-c[1]+c[3]) % 3)


def endpoint_distribution(paths):
    out = {}
    for p in paths:
        key = p.state.source_id, p.state.x
        out[key] = out.get(key, Fraction(0)) + p.state.cwm.total
    return out


def unhide_coefficients(h):
    a, b = (Fraction(2,3)*v for v in h)
    return a, b, -a, -b


def reverse_each_recorded_path(paths):
    """Source/path-sensitive control, outside the common-action quotient.

    Ignore branching tags (weights/branch records are retained), invert each
    recorded coordinate action. Actual T inverse is executed as eleven T calls.
    This restores coordinates, NOT source merging or time/history reversal.
    """
    out = []
    for p in paths:
        b = p.state
        original = b.operation_history
        for a in reversed(original):
            if a == 'T':
                for _ in range(11):
                    b = e.transform(b, 'T')
            elif a == 'U':
                b = e.transform(b, 'U')
            elif a not in ('B0','B1','B2'):
                raise ValueError('unrecognized retained history')
        out.append(Path(b, p.choices))
    return tuple(out)


def even_sign_program(bits):
    """Return a T/U word and its diagonal signs for five adjacent-pair flips.

    These 32 masks are compositions of EXISTING T and U, not new native actions.
    The parity partition below belongs only to this chosen signed-cycle model.
    """
    bits = tuple(bits)
    if len(bits) != 5 or any(type(b) is not int or b not in (0,1) for b in bits):
        raise ValueError('five exact bits required')
    word = []
    signs = [1]*6
    for k, bit in enumerate(bits):
        if bit:
            word += ['T']*((12-k)%12)+['U']+['T']*k
            for j in ((4+k)%6, (5+k)%6):
                signs[j] *= -1
    return tuple(word), tuple(signs)
