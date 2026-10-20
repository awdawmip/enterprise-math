from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class ChildResult:
    children: Tuple[int, ...]
    exact_hit: bool


def polygonal(s: int, k: int) -> int:
    if s < 3 or k < 0:
        raise ValueError("require s>=3 and k>=0")
    a = s - 2
    c = s - 4
    return (a * k * k - c * k) // 2


def discriminant_z(s: int, k: int) -> int:
    a = s - 2
    c = s - 4
    return 2 * a * k - c


def exact_children(s: int, r: int, k: int) -> ChildResult:
    """Exact integer endpoint oracle for E_s(r P_s(k))."""
    if s < 3 or r < 1 or k < 1:
        raise ValueError("require s>=3, r>=1, k>=1")
    a = s - 2
    c = s - 4
    z = discriminant_z(s, k)
    B = (r - 1) * c * c
    D = r * z * z - B
    q = isqrt(D)
    den = 2 * a
    if q * q == D and (c + q) % den == 0:
        return ChildResult(((c + q) // den,), True)
    lo = (c + q) // den
    return ChildResult((lo, lo + 1), False)


def is_exact_hit(s: int, r: int, k: int) -> bool:
    return exact_children(s, r, k).exact_hit


def predecessor(s: int, r: int, child: int) -> Optional[int]:
    """Return the unique positive parent when it exists in the r>=5 separated regime.

    The small bounded candidate window is derived from the exact inverse of z_child
    under z -> sqrt(r z^2 - B), then certified by the exact child oracle.
    """
    if child < 1:
        return None
    a = s - 2
    c = s - 4
    zc = discriminant_z(s, child)
    B = (r - 1) * c * c
    # Parent z is near sqrt((zc^2+B)/r).  floor(sqrt(floor(Q))) is exact
    # for floor(sqrt(Q)) when Q>=0.
    q = isqrt((zc * zc + B) // r)
    p0 = (c + q) // (2 * a)
    found = []
    for p in range(max(1, p0 - 3), p0 + 4):
        if child in exact_children(s, r, p).children:
            found.append(p)
    if len(found) > 1:
        raise AssertionError(f"distinct-parent recoalescence: child={child}, parents={found}")
    return found[0] if found else None


def mechanical_baseline(s: int, r: int, k: int) -> int:
    """Exact floor(sqrt(r) k + beta) for nonsquare r.

    Using sqrt(r) k+beta=(sqrt(r) z_k+c)/(2a).  Since sqrt(r) z_k
    is irrational for nonsquare r, floor division by 2a can be performed from
    floor(sqrt(r z_k^2)).
    """
    a = s - 2
    c = s - 4
    z = discriminant_z(s, k)
    q = isqrt(r * z * z)
    return (q + c) // (2 * a)


def pell_strip_norm(s: int, r: int, k: int) -> int:
    a = s - 2
    c = s - 4
    z = discriminant_z(s, k)
    g = mechanical_baseline(s, r, k)
    y = 2 * a * g - c
    return r * z * z - y * y


def pell_strip_class(s: int, r: int, k: int) -> str:
    c = s - 4
    B = (r - 1) * c * c
    N = pell_strip_norm(s, r, k)
    if N == B:
        return "EXACT_HIT_BOUNDARY"
    if 0 < N < B:
        return "INTERIOR_DEFECT"
    if N > B:
        return "MECHANICAL_SIDE"
    return "PRESTABLE_OR_OTHER"


def support_levels(s: int, r: int, roots: Sequence[int], depth: int) -> List[Tuple[int, ...]]:
    cur = tuple(sorted(set(roots)))
    out = [cur]
    for _ in range(depth):
        nxt = []
        for k in cur:
            nxt.extend(exact_children(s, r, k).children)
        if len(nxt) != len(set(nxt)):
            raise AssertionError("support recoalescence detected")
        cur = tuple(sorted(nxt))
        out.append(cur)
    return out


def hit_counts_by_level(s: int, r: int, roots: Sequence[int], depth: int) -> List[int]:
    return [sum(is_exact_hit(s, r, k) for k in lev) for lev in support_levels(s, r, roots, depth)]


def backward_path(s: int, r: int, target: int, ancestor: int, max_depth: int = 10000) -> Optional[List[int]]:
    rev = [target]
    cur = target
    for _ in range(max_depth):
        if cur == ancestor:
            return list(reversed(rev))
        cur = predecessor(s, r, cur)
        if cur is None:
            return None
        rev.append(cur)
    return None


def hit_ancestor_chain(s: int, r: int, target: int, max_depth: int = 10000) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    cur = target
    for depth in range(1, max_depth + 1):
        cur = predecessor(s, r, cur)
        if cur is None:
            break
        if is_exact_hit(s, r, cur):
            out.append((depth, cur))
    return out


def enumerate_hits(s: int, r: int, k_max: int) -> List[int]:
    return [k for k in range(1, k_max + 1) if is_exact_hit(s, r, k)]


def sqrt_rational_bounds(n: int, decimal_digits: int = 40) -> Tuple[Fraction, Fraction]:
    if n <= 0:
        raise ValueError("n must be positive")
    Q = 10 ** decimal_digits
    L = isqrt(n * Q * Q)
    if L * L == n * Q * Q:
        x = Fraction(L, Q)
        return x, x
    return Fraction(L, Q), Fraction(L + 1, Q)


def cylinder_enclosure(s: int, r: int, level: int, k: int, decimal_digits: int = 40) -> Tuple[Fraction, Fraction]:
    """Rigorous rational enclosure for the normalized branch cylinder.

    Normalization is X_t = r^{-t/2}(k-c/(2a)) = z_k/(2a alpha^t), alpha=sqrt(r).
    Every legal child obeys k' = alpha k + beta + e with
    |e| <= C := 1 + D(1), where
    D(k)=alpha k+beta-Phi(k)=B/[2a(alpha z_k + W(z_k))].
    Therefore every continuation from a level-t prefix lies within
    [center - T alpha^-t, center + T alpha^-t], T=C/(alpha-1).
    This function replaces alpha and W(1) by outward rational bounds.
    """
    if level < 0:
        raise ValueError("level must be nonnegative")
    a = s - 2
    c = s - 4
    B = (r - 1) * c * c
    z = discriminant_z(s, k)
    alpha_lo, alpha_hi = sqrt_rational_bounds(r, decimal_digits)
    if alpha_lo <= 1:
        raise ValueError("r>1 required")

    # center = z/(2a alpha^level)
    center_lo = Fraction(z, 2 * a) / (alpha_hi ** level)
    center_hi = Fraction(z, 2 * a) / (alpha_lo ** level)

    # W at k=1, z_1=s.  Lower bounds make the denominator smaller and D upper larger.
    z1 = s
    W2 = r * z1 * z1 - B
    W_lo, _ = sqrt_rational_bounds(W2, decimal_digits)
    D_upper = Fraction(B, 1) / (2 * a * (alpha_lo * z1 + W_lo)) if B else Fraction(0)
    C_upper = Fraction(1) + D_upper
    T_upper = C_upper / (alpha_lo - 1)
    tail_upper = T_upper / (alpha_lo ** level)
    return center_lo - tail_upper, center_hi + tail_upper


def count_interval_overlaps(intervals: Sequence[Tuple[Fraction, Fraction]]) -> int:
    """Count unordered overlapping pairs among rigorous enclosures."""
    ordered = sorted(intervals, key=lambda x: (x[0], x[1]))
    count = 0
    for i, (_, hi) in enumerate(ordered):
        for lo2, _ in ordered[i + 1:]:
            if lo2 > hi:
                break
            count += 1
    return count


def fundamental_pell_unit(r: int, v_limit: int = 2_000_000) -> Tuple[int, int]:
    if isqrt(r) ** 2 == r:
        raise ValueError("r must be nonsquare")
    for v in range(1, v_limit + 1):
        u2 = 1 + r * v * v
        u = isqrt(u2)
        if u * u == u2:
            return u, v
    raise RuntimeError("fundamental Pell unit not found within limit")


def pell_matrix_period_mod(r: int, modulus: int, step_limit: int = 1_000_000) -> int:
    """Least n>0 for which the fundamental Pell-unit matrix is I mod modulus."""
    if modulus <= 1:
        return 1
    u, v = fundamental_pell_unit(r)
    A = ((u % modulus, (r * v) % modulus), (v % modulus, u % modulus))
    M = ((1, 0), (0, 1))
    I = M

    def mul(X, Y):
        return (
            ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % modulus,
             (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % modulus),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % modulus,
             (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % modulus),
        )

    for n in range(1, step_limit + 1):
        M = mul(M, A)
        if M == I:
            return n
    raise RuntimeError("matrix period not found within limit")


def bounded_recurrence_scan(s_values: Iterable[int], r_values: Iterable[int], k_max: int) -> Dict[str, object]:
    cells = []
    max_hit_chain = 0
    for s in s_values:
        if s == 4:
            continue
        for r in r_values:
            if r < 5 or isqrt(r) ** 2 == r:
                continue
            hits = enumerate_hits(s, r, k_max)
            witnesses = []
            local_max = 1 if hits else 0
            for h in hits:
                chain = hit_ancestor_chain(s, r, h)
                if chain:
                    local_max = max(local_max, 1 + len(chain))
                    d, anc = chain[0]
                    if d >= 2:
                        path = backward_path(s, r, h, anc)
                        witnesses.append({"ancestor_hit": anc, "descendant_hit": h, "gap_steps": d, "path": path})
            max_hit_chain = max(max_hit_chain, local_max)
            cells.append({
                "s": s,
                "r": r,
                "k_max": k_max,
                "ambient_hit_count": len(hits),
                "ambient_hits": hits,
                "max_hits_on_one_checked_ancestry": local_max,
                "nonconsecutive_revisit_witnesses": witnesses[:8],
                "pell_unit": fundamental_pell_unit(r),
                "pell_matrix_period_mod_2a": pell_matrix_period_mod(r, 2 * (s - 2)),
            })
    return {
        "classification": "BOUNDED_EXHAUSTIVE",
        "k_max": k_max,
        "max_hits_on_one_checked_ancestry": max_hit_chain,
        "cells": cells,
    }
