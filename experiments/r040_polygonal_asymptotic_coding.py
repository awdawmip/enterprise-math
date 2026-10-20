from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, gcd, isqrt, log, sqrt
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple
import argparse
import json

def _ceil_fraction(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)

def _ceil_div(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError('positive denominator required')
    return -(-n // d)

def _strict_positive_linear_threshold(L: int, C: int) -> int:
    if L <= 0:
        raise ValueError
    return -C // L + 1

def _strict_negative_linear_threshold(L: int, C: int) -> int:
    if L >= 0:
        raise ValueError
    return C // -L + 1

@dataclass(frozen=True)
class Params:
    s: int
    r: int

    def __post_init__(self) -> None:
        if self.s < 3:
            raise ValueError('s must be >= 3')
        if self.r < 1:
            raise ValueError('r must be >= 1')

    @property
    def a(self) -> int:
        return self.s - 2

    @property
    def c(self) -> int:
        return self.s - 4

    @property
    def B(self) -> int:
        return (self.r - 1) * self.c * self.c

    @property
    def square_q(self) -> int | None:
        q = isqrt(self.r)
        return q if q * q == self.r else None

def polygonal(s: int, k: int) -> int:
    if s < 3 or k < 0:
        raise ValueError
    a, c = (s - 2, s - 4)
    return (a * k * k - c * k) // 2

def discriminant_z(s: int, k: int) -> int:
    if s < 3 or k < 0:
        raise ValueError
    a, c = (s - 2, s - 4)
    return 2 * a * k - c

def lower_index(s: int, x: int) -> int:
    if s < 3 or x < 0:
        raise ValueError
    a, c = (s - 2, s - 4)
    D = c * c + 8 * a * x
    return (c + isqrt(D)) // (2 * a)

def lower_index_holdout(s: int, x: int) -> int:
    if s < 3 or x < 0:
        raise ValueError
    lo, hi = (0, 1)
    while polygonal(s, hi) <= x:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if polygonal(s, mid) <= x:
            lo = mid
        else:
            hi = mid
    return lo

def endpoint_children_value(s: int, x: int) -> Tuple[int, ...]:
    m = lower_index(s, x)
    if polygonal(s, m) == x:
        return (m,)
    return (m, m + 1)

def endpoint_children_holdout(s: int, x: int) -> Tuple[int, ...]:
    m = lower_index_holdout(s, x)
    if polygonal(s, m) == x:
        return (m,)
    return (m, m + 1)

def endpoint_children(s: int, r: int, k: int) -> Tuple[int, ...]:
    return endpoint_children_value(s, r * polygonal(s, k))

def exact_lower_map(s: int, r: int, k: int) -> int:
    return endpoint_children(s, r, k)[0]

def baseline_linear_floor(s: int, r: int, k: int) -> int:
    p = Params(s, r)
    z = discriminant_z(s, k)
    return (p.c + isqrt(r * z * z)) // (2 * p.a)

def curvature_drop(s: int, r: int, k: int) -> int:
    return baseline_linear_floor(s, r, k) - exact_lower_map(s, r, k)

def baseline_lattice_y(s: int, r: int, k: int) -> int:
    p = Params(s, r)
    n = baseline_linear_floor(s, r, k)
    return 2 * p.a * n - p.c

def baseline_pell_norm(s: int, r: int, k: int) -> int:
    z = discriminant_z(s, k)
    y = baseline_lattice_y(s, r, k)
    return r * z * z - y * y

def exact_hit(s: int, r: int, k: int) -> bool:
    return len(endpoint_children(s, r, k)) == 1

def square_affine_offset(s: int, q: int) -> int:
    if s == 4:
        raise ValueError('s=4 is the exact-dilation degeneracy')
    if q < 2:
        raise ValueError
    a, c = (s - 2, s - 4)
    beta = Fraction(c * (1 - q), 2 * a)
    return _ceil_fraction(beta) - 1

def square_stable_threshold(s: int, q: int) -> int:
    if s == 4:
        raise ValueError('s=4 has singleton exact dilation')
    if q < 2:
        raise ValueError
    a, c = (s - 2, s - 4)
    d = square_affine_offset(s, q)

    def LC(j: int) -> Tuple[int, int]:
        return (q * (c * (1 - q) - 2 * a * j), j * (c - a * j))
    L0, C0 = LC(d)
    L1, C1 = LC(d + 1)
    if L0 <= 0 or L1 > 0:
        raise AssertionError((s, q, d, L0, L1))
    K = max(1, _ceil_div(-d, q), _strict_positive_linear_threshold(L0, C0))
    if L1 < 0:
        K = max(K, _strict_negative_linear_threshold(L1, C1))
    elif C1 >= 0:
        raise AssertionError('zero upper slope must have a strictly negative constant for s!=4')
    return K

def curvature_drop_sufficient_threshold(s: int, r: int) -> int:
    p = Params(s, r)
    if r == 1 or p.B == 0:
        return 1
    k = 1
    lhs_const = (p.B + 4 * p.a * p.a) ** 2
    while True:
        z = discriminant_z(s, k)
        if r * z * z > 4 * p.a * p.a and lhs_const < 16 * p.a * p.a * r * z * z:
            return k
        k += 1

def square_forward_invariant_threshold(s: int, q: int) -> int:
    K = square_stable_threshold(s, q)
    d = square_affine_offset(s, q)
    return max(K, _ceil_div(-d, q - 1))

def square_digit_support(q: int, t: int) -> Tuple[int, ...]:
    vals = {0}
    place = 1
    for _ in range(t):
        vals = vals | {v + place for v in vals}
        place *= q
    return tuple(sorted(vals))

def square_support_formula(s: int, q: int, k0: int, t: int) -> Tuple[int, ...]:
    if s == 4:
        return (pow(q, t) * k0,)
    d = square_affine_offset(s, q)
    affine = pow(q, t) * k0 + d * (pow(q, t) - 1) // (q - 1)
    return tuple((affine + x for x in square_digit_support(q, t)))

def lower_jump(s: int, r: int, k: int) -> int:
    return exact_lower_map(s, r, k + 1) - exact_lower_map(s, r, k)

def baseline_jump(s: int, r: int, k: int) -> int:
    return baseline_linear_floor(s, r, k + 1) - baseline_linear_floor(s, r, k)

def support_step(s: int, r: int, support: Iterable[int]) -> Tuple[int, ...]:
    out = set()
    for k in support:
        out.update(endpoint_children(s, r, k))
    return tuple(sorted(out))

def iterate_support(s: int, r: int, start: Iterable[int], steps: int) -> List[Tuple[int, ...]]:
    layers = [tuple(sorted(set(start)))]
    for _ in range(steps):
        layers.append(support_step(s, r, layers[-1]))
    return layers

def cardinality_loss(s: int, r: int, support: Iterable[int]) -> Dict[str, int]:
    support = tuple(sorted(set(support)))
    raw = 0
    incidence: Dict[int, int] = {}
    hits = 0
    for k in support:
        ch = endpoint_children(s, r, k)
        if len(ch) == 1:
            hits += 1
        raw += len(ch)
        for x in ch:
            incidence[x] = incidence.get(x, 0) + 1
    union_size = len(incidence)
    collisions = raw - union_size
    return {'parents': len(support), 'exact_hits': hits, 'raw_children': raw, 'cross_parent_collision_loss': collisions, 'next_support': union_size, 'identity_rhs': 2 * len(support) - hits - collisions}

def sqrt_continued_fraction(r: int) -> Dict[str, object]:
    a0 = isqrt(r)
    if a0 * a0 == r:
        return {'a0': a0, 'period': []}
    m, d, a = (0, 1, a0)
    period: List[int] = []
    while True:
        m = d * a - m
        d = (r - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break
    return {'a0': a0, 'period': period}

def convergents_sqrt(r: int, count: int) -> List[Tuple[int, int]]:
    cf = sqrt_continued_fraction(r)
    a0 = int(cf['a0'])
    period = list(cf['period'])
    if not period:
        return [(a0, 1)]
    coeffs = [a0] + [period[(i - 1) % len(period)] for i in range(1, count)]
    p_nm2, p_nm1 = (0, 1)
    q_nm2, q_nm1 = (1, 0)
    out = []
    for a in coeffs:
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        out.append((p, q))
        p_nm2, p_nm1 = (p_nm1, p)
        q_nm2, q_nm1 = (q_nm1, q)
    return out

def defect_rational_sample(s: int, r: int, k: int, conv_count: int=64) -> Dict[str, object]:
    y = baseline_lattice_y(s, r, k)
    z = discriminant_z(s, k)
    g = gcd(abs(y), abs(z))
    reduced = (y // g, z // g)
    conv = set(convergents_sqrt(r, conv_count))
    return {'k': k, 'N': baseline_pell_norm(s, r, k), 'y': y, 'z': z, 'reduced_y_over_z': list(reduced), 'principal_convergent_within_checked_prefix': reduced in conv}

def sturmian_balance_witness(s: int, r: int, start: int=1, length: int=10000, max_factor_len: int=512) -> Dict[str, object] | None:
    p = Params(s, r)
    if p.square_q is not None:
        return None
    n = isqrt(r)
    vals = [lower_jump(s, r, k) for k in range(start, start + length)]
    if any((v not in (n, n + 1) for v in vals)):
        return {'kind': 'alphabet_not_two_adjacent', 'start': start}
    bits = ''.join(('1' if v == n + 1 else '0' for v in vals))
    for L in range(1, min(max_factor_len, len(bits)) + 1):
        by_count: Dict[int, Tuple[int, str]] = {}
        for i in range(len(bits) - L + 1):
            f = bits[i:i + L]
            by_count.setdefault(f.count('1'), (start + i, f))
        lo, hi = (min(by_count), max(by_count))
        if hi - lo > 1:
            ilo, flo = by_count[lo]
            ihi, fhi = by_count[hi]
            return {'kind': 'sturmian_balance_violation', 'factor_length': L, 'low_ones': lo, 'high_ones': hi, 'low_start_k': ilo, 'high_start_k': ihi, 'low_factor': flo, 'high_factor': fhi}
    return None
