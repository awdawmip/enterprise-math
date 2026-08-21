from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class HitPair:
    parent_index: int
    child_index: int
    y: int
    z: int


@dataclass(frozen=True)
class ReducedPellLabel:
    reduced_y: int
    reduced_z: int
    unit_exponent: int


def params(s: int, r: int) -> Tuple[int, int, int, int, Fraction]:
    if s < 3 or s == 4 or r < 5 or isqrt(r) ** 2 == r:
        raise ValueError("require s>=3, s!=4, nonsquare r>=5")
    a = s - 2
    c = s - 4
    m = 2 * a
    B = (r - 1) * c * c
    kappa = Fraction(c, m)
    return a, c, m, B, kappa


def discriminant_z(s: int, k: int) -> int:
    a = s - 2
    c = s - 4
    return 2 * a * k - c


def index_from_z(s: int, z: int) -> Optional[int]:
    a = s - 2
    c = s - 4
    m = 2 * a
    if (z + c) % m:
        return None
    return (z + c) // m


def polygonal(s: int, k: int) -> int:
    a = s - 2
    c = s - 4
    return (a * k * k - c * k) // 2


def exact_children(s: int, r: int, k: int) -> Tuple[Tuple[int, ...], bool]:
    a, c, m, B, _ = params(s, r)
    if k < 1:
        raise ValueError("positive endpoint index required")
    z = discriminant_z(s, k)
    D = r * z * z - B
    q = isqrt(D)
    if q * q == D and (q + c) % m == 0:
        return ((q + c) // m,), True
    lo = (q + c) // m
    return (lo, lo + 1), False


def is_exact_hit(s: int, r: int, k: int) -> bool:
    return exact_children(s, r, k)[1]


def hit_pair(s: int, r: int, k: int) -> HitPair:
    children, exact = exact_children(s, r, k)
    if not exact:
        raise ValueError("k is not an exact-hit parent")
    j = children[0]
    return HitPair(k, j, discriminant_z(s, j), discriminant_z(s, k))


def predecessor(s: int, r: int, child: int) -> Optional[int]:
    """Exact unique predecessor in the separated r>=5 regime."""
    _, c, m, B, _ = params(s, r)
    if child < 1:
        return None
    y = discriminant_z(s, child)
    q = isqrt((y * y + B) // r)
    p0 = max(1, (q + c) // m)
    found: List[int] = []
    for p in range(max(1, p0 - 3), p0 + 5):
        if child in exact_children(s, r, p)[0]:
            found.append(p)
    if len(found) > 1:
        raise AssertionError(f"distinct-parent recoalescence: {child=} {found=}")
    return found[0] if found else None


def reverse_path(s: int, r: int, target: int, depth: int) -> Optional[Tuple[int, ...]]:
    cur = target
    rev = [cur]
    for _ in range(depth):
        cur = predecessor(s, r, cur)
        if cur is None:
            return None
        rev.append(cur)
    return tuple(reversed(rev))


def fundamental_pell_unit(r: int) -> Tuple[int, int]:
    """Return minimal (u,v)>0 with u^2-r v^2=1 by continued fractions."""
    if r < 2 or isqrt(r) ** 2 == r:
        raise ValueError("r must be nonsquare >1")
    a0 = isqrt(r)
    m = 0
    d = 1
    a = a0
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    while True:
        p = a * p_m1 + p_m2
        q = a * q_m1 + q_m2
        if p * p - r * q * q == 1:
            return p, q
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q
        m = d * a - m
        d = (r - m * m) // d
        a = (a0 + m) // d


def apply_unit(r: int, pair: Tuple[int, int], unit: Tuple[int, int]) -> Tuple[int, int]:
    y, z = pair
    u, v = unit
    return u * y + r * v * z, v * y + u * z


def inverse_unit(r: int, pair: Tuple[int, int], unit: Tuple[int, int]) -> Tuple[int, int]:
    y, z = pair
    u, v = unit
    return u * y - r * v * z, u * z - v * y


def reduce_positive_pell_pair(r: int, pair: Tuple[int, int]) -> ReducedPellLabel:
    """Reduce a positive fixed-norm Pell pair by inverse fundamental units."""
    unit = fundamental_pell_unit(r)
    y, z = pair
    if y <= 0 or z <= 0:
        raise ValueError("positive pair required")
    n = 0
    while True:
        yy, zz = inverse_unit(r, (y, z), unit)
        if yy > 0 and zz > 0:
            y, z = yy, zz
            n += 1
        else:
            return ReducedPellLabel(y, z, n)


def reduced_bound_holds(s: int, r: int, reduced: Tuple[int, int]) -> bool:
    _, _, _, B, _ = params(s, r)
    u, _ = fundamental_pell_unit(r)
    _, z = reduced
    return r * z * z <= u * u * B


def centered_energy(s: int, k: int) -> Fraction:
    a = s - 2
    c = s - 4
    kappa = Fraction(c, 2 * a)
    x = Fraction(k) - kappa
    return x * x - kappa * kappa


def ideal_reverse_center_square(s: int, r: int, target: int, depth: int) -> Fraction:
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    _, _, _, _, kappa = params(s, r)
    return kappa * kappa + centered_energy(s, target) / (r ** depth)


def certify_shadow_error_lt(s: int, r: int, ancestor: int, target: int, depth: int, eps: Fraction) -> bool:
    if eps <= 0:
        raise ValueError("eps must be positive")
    _, _, _, _, kappa = params(s, r)
    centered_ancestor = Fraction(ancestor) - kappa
    if centered_ancestor <= eps:
        raise ValueError("certificate helper expects positive lower square endpoint")
    S = ideal_reverse_center_square(s, r, target, depth)
    return (centered_ancestor - eps) ** 2 < S < (centered_ancestor + eps) ** 2


def exact_first_reverse_gate_values(s: int, r: int, target_hit: int, d_shifts: Sequence[int] = (-1, 0, 1)) -> Tuple[dict, ...]:
    _, c, m, B, _ = params(s, r)
    pair = hit_pair(s, r, target_hit)
    Y, Z = pair.y, pair.z
    modulus = r * m
    residue = (-Y - r * c) % modulus
    D0 = residue
    if 2 * D0 > modulus:
        D0 -= modulus
    lower = r * (-2 * m * Z + m * m)
    upper = r * (2 * m * Z + m * m)
    rows = []
    for shift in d_shifts:
        D = D0 + shift * modulus
        num = Y + D
        if num % r:
            continue
        z = num // r
        k = index_from_z(s, z)
        gate_poly = D * (2 * Y + D) - (r + 1) * B
        passes = bool(Z > m and z > 0 and k is not None and lower < gate_poly < upper)
        rows.append({"D": D, "z": z, "parent_index": k, "gate_poly": gate_poly, "lower": lower, "upper": upper, "passes": passes})
    return tuple(rows)


def same_reduced_pell_class(s: int, r: int, k1: int, k2: int) -> bool:
    p1 = hit_pair(s, r, k1)
    p2 = hit_pair(s, r, k2)
    a = reduce_positive_pell_pair(r, (p1.y, p1.z))
    b = reduce_positive_pell_pair(r, (p2.y, p2.z))
    return (a.reduced_y, a.reduced_z) == (b.reduced_y, b.reduced_z)


def local_gate_residual(s: int, r: int, parent: int, child: int) -> dict:
    _, _, m, B, _ = params(s, r)
    z0 = discriminant_z(s, parent)
    z1 = discriminant_z(s, child)
    E = r * z0 * z0 - z1 * z1 - B
    lower = -2 * m * z1 + m * m
    upper = 2 * m * z1 + m * m
    gate = bool(z1 > m and lower < E < upper)
    oracle = child in exact_children(s, r, parent)[0]
    return {"parent": parent, "child": child, "z_parent": z0, "z_child": z1, "E": E, "lower": lower, "upper": upper, "gate": gate, "oracle": oracle}


def weighted_path_residual_identity(s: int, r: int, path: Sequence[int]) -> Tuple[Fraction, Fraction]:
    if len(path) < 2:
        raise ValueError("path needs at least one edge")
    _, _, m, _, _ = params(s, r)
    ell = len(path) - 1
    lhs = Fraction(r ** ell) * centered_energy(s, path[0]) - centered_energy(s, path[-1])
    weighted = 0
    for t, (parent, child) in enumerate(zip(path, path[1:]), start=1):
        E = local_gate_residual(s, r, parent, child)["E"]
        weighted += (r ** (ell - t)) * E
    return lhs, Fraction(weighted, m * m)
