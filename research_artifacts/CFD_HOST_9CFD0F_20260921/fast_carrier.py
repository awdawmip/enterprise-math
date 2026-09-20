"""Exact axis-generator certificate; extends the frozen CFD support detector.

No pruning, no amplitude threshold, and no replacement of complex arithmetic.
The fast path is used only when every coordinate gcd-generator occurs in the
signed seed. Otherwise the original iterative detector is called unchanged.
"""
from dataclasses import dataclass
from itertools import product
from math import gcd, prod
from numbers import Integral
from typing import Callable, Iterable

Vec = tuple[int, int, int]

@dataclass(frozen=True)
class AxisCertificate:
    gcds: Vec
    carrier_size: int
    source_size: int
    status: str
    carrier: tuple[Vec, ...] | None


def axis_certificate(seed: Iterable[Vec], cutoff: int, limit: int) -> AxisCertificate | None:
    if not isinstance(cutoff, Integral) or isinstance(cutoff, bool) or cutoff < 0:
        raise ValueError('cutoff must be a nonnegative integer')
    if not isinstance(limit, Integral) or isinstance(limit, bool) or limit < 0:
        raise ValueError('limit must be a nonnegative integer')
    S: set[Vec] = set()
    for v in seed:
        v = tuple(v)
        if len(v) != 3 or any(not isinstance(x, Integral) or isinstance(x, bool) for x in v):
            raise ValueError('seed requires exact integer triples')
        p = tuple(int(x) for x in v)
        if any(abs(x) > cutoff for x in p):
            raise ValueError('seed outside retained cube')
        S.add(p)
        S.add(tuple(-x for x in p))
    if not S:
        return AxisCertificate((0, 0, 0), 0, 0, 'EXACT_EMPTY', ())
    ds = tuple(gcd(*(abs(p[j]) for p in S)) for j in range(3))
    for j, d in enumerate(ds):
        if d:
            g = tuple(d if k == j else 0 for k in range(3))
            if g not in S:
                return None
    size = prod(2 * (cutoff // d) + 1 if d else 1 for d in ds)
    if size > limit:
        return AxisCertificate(ds, size, len(S), 'EXACT_SIZE_DENSE_FALLBACK', None)
    axes = [range(-(cutoff // d) * d, (cutoff // d) * d + 1, d) if d else (0,) for d in ds]
    C = tuple(product(*axes))
    assert len(C) == size
    return AxisCertificate(ds, size, len(S), 'EXACT_AXIS_GENERATOR_CARRIER', C)


def fast_carrier(seed: Iterable[Vec], cutoff: int, limit: int, original: Callable):
    """Return (carrier-or-None, metadata); original return structure is preserved."""
    S = tuple(seed)
    cert = axis_certificate(S, cutoff, limit)
    if cert is not None:
        return cert.carrier, {
            'route': cert.status, 'proof': 'AXIS_GCD_GENERATORS_PRESENT',
            'gcds': cert.gcds, 'carrier_size': cert.carrier_size,
            'lower_bound': cert.carrier_size, 'pair_tests': 0,
        }
    result = original(S, cutoff, limit)
    return result.carrier, {
        'route': result.status, 'proof': 'ORIGINAL_TRUNCATED_ADDITIVE_CLOSURE',
        'carrier_size': result.carrier_size, 'lower_bound': result.lower_bound,
        'pair_tests': result.pair_tests,
    }
