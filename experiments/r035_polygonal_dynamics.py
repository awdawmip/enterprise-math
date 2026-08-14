"""Exact laboratory for R035 polygonal refinement endpoint dynamics.

The theorem-critical core uses integer arithmetic only.

For s >= 3, put a = s-2 and c = a-2 = s-4.  Then
    P_s(k) = k + a*k*(k-1)//2,
and the consecutive gap is
    P_s(k+1)-P_s(k) = a*k + 1.

The discriminant coordinate
    z_s(k) = 2*a*k - c
satisfies
    c^2 + 8*a*P_s(k) = z_s(k)^2.
For n = r*P_s(k),
    D = c^2 + 8*a*n = r*z_s(k)^2 + (1-r)*c^2.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


IndexSupport = Tuple[int, ...]


def _check_s(s: int) -> None:
    if not isinstance(s, int) or s < 3:
        raise ValueError("s must be an integer >= 3")


def _check_nonnegative(name: str, x: int) -> None:
    if not isinstance(x, int) or x < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def polygonal(s: int, k: int) -> int:
    """Return P_s(k) exactly."""
    _check_s(s)
    _check_nonnegative("k", k)
    a = s - 2
    return k + a * k * (k - 1) // 2


def polygonal_gap(s: int, k: int) -> int:
    """Return P_s(k+1)-P_s(k) = (s-2)k+1 exactly."""
    _check_s(s)
    _check_nonnegative("k", k)
    return (s - 2) * k + 1


def discriminant(s: int, n: int) -> int:
    """Quadratic inversion discriminant (s-4)^2 + 8(s-2)n."""
    _check_s(s)
    _check_nonnegative("n", n)
    a = s - 2
    c = s - 4
    return c * c + 8 * a * n


def z_coordinate(s: int, k: int) -> int:
    """Signed lattice discriminant coordinate z=2(s-2)k-(s-4)."""
    _check_s(s)
    _check_nonnegative("k", k)
    a = s - 2
    c = s - 4
    return 2 * a * k - c


def lower_index(s: int, n: int) -> int:
    """Exact L_s(n), using only integer square root and integer division."""
    _check_s(s)
    _check_nonnegative("n", n)
    a = s - 2
    c = s - 4
    q = isqrt(discriminant(s, n))
    m = (c + q) // (2 * a)

    # Defensive exact corrections make the oracle robust to any algebraic mistake
    # in the closed form while remaining integer-only.  They should execute zero
    # iterations for correct inputs/formula.
    while m > 0 and polygonal(s, m) > n:
        m -= 1
    while polygonal(s, m + 1) <= n:
        m += 1
    return m


def endpoint_support(s: int, n: int) -> IndexSupport:
    """Exact E_s(n) as a sorted tuple."""
    m = lower_index(s, n)
    if polygonal(s, m) == n:
        return (m,)
    return (m, m + 1)


def is_exact_parent_hit(s: int, r: int, k: int) -> bool:
    _check_s(s)
    if not isinstance(r, int) or r < 1:
        raise ValueError("r must be an integer >= 1")
    _check_nonnegative("k", k)
    n = r * polygonal(s, k)
    m = lower_index(s, n)
    return polygonal(s, m) == n


def lower_map(s: int, r: int, k: int) -> int:
    _check_s(s)
    if not isinstance(r, int) or r < 1:
        raise ValueError("r must be an integer >= 1")
    _check_nonnegative("k", k)
    return lower_index(s, r * polygonal(s, k))


def parent_children(s: int, r: int, k: int) -> IndexSupport:
    _check_s(s)
    if not isinstance(r, int) or r < 1:
        raise ValueError("r must be an integer >= 1")
    _check_nonnegative("k", k)
    return endpoint_support(s, r * polygonal(s, k))


@dataclass(frozen=True)
class StepResult:
    source: IndexSupport
    target: IndexSupport
    incidence: Mapping[int, Tuple[int, ...]]
    raw_edges: int
    duplicate_edge_excess: int
    recoalescing_children: Tuple[int, ...]


def one_step(s: int, r: int, support: Iterable[int]) -> StepResult:
    src = tuple(sorted(set(support)))
    for k in src:
        _check_nonnegative("support index", k)

    parents_by_child: Dict[int, List[int]] = {}
    raw_edges = 0
    for k in src:
        for child in parent_children(s, r, k):
            raw_edges += 1
            parents_by_child.setdefault(child, []).append(k)

    target = tuple(sorted(parents_by_child))
    incidence = {j: tuple(parents_by_child[j]) for j in target}
    duplicate_edge_excess = sum(len(ps) - 1 for ps in incidence.values())
    recoalescing = tuple(j for j, ps in incidence.items() if len(ps) > 1)
    return StepResult(
        source=src,
        target=target,
        incidence=incidence,
        raw_edges=raw_edges,
        duplicate_edge_excess=duplicate_edge_excess,
        recoalescing_children=recoalescing,
    )


def iterate_support(s: int, r: int, k0: int, depth: int) -> Tuple[IndexSupport, ...]:
    _check_nonnegative("k0", k0)
    _check_nonnegative("depth", depth)
    levels: List[IndexSupport] = [(k0,)]
    for _ in range(depth):
        levels.append(one_step(s, r, levels[-1]).target)
    return tuple(levels)


def iterate_steps(s: int, r: int, k0: int, depth: int) -> Tuple[StepResult, ...]:
    _check_nonnegative("k0", k0)
    _check_nonnegative("depth", depth)
    out: List[StepResult] = []
    current: IndexSupport = (k0,)
    for _ in range(depth):
        result = one_step(s, r, current)
        out.append(result)
        current = result.target
    return tuple(out)


def actual_value_support(s: int, support: Iterable[int]) -> Tuple[int, ...]:
    return tuple(polygonal(s, k) for k in sorted(set(support)))


def support_has_internal_gap(support: Sequence[int]) -> bool:
    if len(support) < 2:
        return False
    return any(v != u + 1 for u, v in zip(support, support[1:]))


def support_missing_count(support: Sequence[int]) -> int:
    if not support:
        return 0
    return support[-1] - support[0] + 1 - len(support)


def exact_hit_pell_residual(s: int, r: int, k: int, m: int) -> int:
    """Return z_m^2-r*z_k^2-(1-r)(s-4)^2; zero iff the Pell form holds."""
    z_k = z_coordinate(s, k)
    z_m = z_coordinate(s, m)
    c = s - 4
    return z_m * z_m - r * z_k * z_k - (1 - r) * c * c


def exact_hit_via_discriminant(s: int, r: int, k: int) -> Tuple[bool, int]:
    """Return (is_hit, m) and cross-check the exact Pell/discriminant identity."""
    m = lower_map(s, r, k)
    hit = polygonal(s, m) == r * polygonal(s, k)
    if hit and exact_hit_pell_residual(s, r, k, m) != 0:
        raise AssertionError("exact-hit Pell identity failed")
    return hit, m


def upper_map(s: int, r: int, k: int) -> int:
    """Largest endpoint child of a parent."""
    return parent_children(s, r, k)[-1]


def lower_jump(s: int, r: int, k: int) -> int:
    """F(k+1)-F(k), where F(k)=L_s(rP_s(k))."""
    return lower_map(s, r, k + 1) - lower_map(s, r, k)


def has_lower_self_loop(s: int, r: int, k: int) -> bool:
    """Whether k itself is a child (equivalently F(k)=k)."""
    return lower_map(s, r, k) == k


def r4_children_formula(s: int, k: int) -> IndexSupport:
    """Closed-form r=4 child rule for positive k; k=0 stays {0}."""
    _check_s(s)
    _check_nonnegative("k", k)
    if k == 0:
        return (0,)
    if s == 3:
        return (2 * k, 2 * k + 1)
    if s == 4:
        return (2 * k,)
    return (2 * k - 1, 2 * k)


def cardinality_components(s: int, r: int, support: Iterable[int]) -> Tuple[int, int, int, int]:
    """Return (N, exact_hit_parents, duplicate_excess, N_next).

    Because every parent has one child on an exact hit and two otherwise,
    N_next = 2*N - exact_hit_parents - duplicate_excess.
    """
    src = tuple(sorted(set(support)))
    hits = sum(is_exact_parent_hit(s, r, k) for k in src)
    step = one_step(s, r, src)
    expected = 2 * len(src) - hits - step.duplicate_edge_excess
    if expected != len(step.target):
        raise AssertionError("cardinality accounting failed")
    return len(src), hits, step.duplicate_edge_excess, len(step.target)


def is_integer_interval(support: Sequence[int]) -> bool:
    if not support:
        return True
    return support[-1] - support[0] + 1 == len(support)



def adjacent_parent_overlap(s: int, r: int, k: int) -> bool:
    """Whether parent k and k+1 share an endpoint child.

    Since the lower map is strictly increasing and every child block has width
    at most one, this is the only possible elementary recoalescence pattern.
    """
    a = set(parent_children(s, r, k))
    b = set(parent_children(s, r, k + 1))
    return bool(a.intersection(b))


def universal_interval_failure_witness(r: int) -> Tuple[int, int, IndexSupport, IndexSupport]:
    """Return the uniform r>=5 two-step gap witness.

    For s=r+1 and k0=1, S1={1,2}; the image of parent 1 is again
    {1,2}, whereas r*P_s(2)=r(r+1) >= P_s(4)=6r-2, so parent 2's
    children begin at index at least 4.  Hence S2 has a gap at 3.
    """
    if not isinstance(r, int) or r < 5:
        raise ValueError("the uniform interval-failure witness requires r >= 5")
    s = r + 1
    levels = iterate_support(s, r, 1, 2)
    return s, 1, levels[1], levels[2]


def eventual_two_jump_start(s: int, r: int) -> int:
    """A sufficient exact start K for the eventual lower-jump alphabet.

    For positive k, the real inverse coordinate has derivative
        r*z/sqrt(r*z^2-(r-1)c^2),
    decreasing to sqrt(r).  With q=floor(sqrt(r)), the integer inequality

        r*((q+1)^2-r)*z_k^2 > (q+1)^2*(r-1)*c^2

    certifies derivative < q+1 from k onward.  Combined with derivative
    >= sqrt(r), every F(j+1)-F(j), j>=K, lies in {q,q+1}.
    No floating point is used to locate K.
    """
    _check_s(s)
    if not isinstance(r, int) or r <= 1:
        raise ValueError("r must be an integer > 1")
    a = s - 2
    c = s - 4
    if c == 0:
        return 1
    q = isqrt(r)
    left_coeff = r * ((q + 1) * (q + 1) - r)
    right = (q + 1) * (q + 1) * (r - 1) * c * c
    zmin = isqrt(right // left_coeff)
    while left_coeff * zmin * zmin <= right:
        zmin += 1
    # z_k=2*a*k-c >= zmin.
    numerator = zmin + c
    k = max(1, (numerator + 2 * a - 1) // (2 * a))
    while left_coeff * z_coordinate(s, k) ** 2 <= right:
        k += 1
    return k

def square_case_children(r: int, k: int) -> IndexSupport:
    """Control formula for s=4; still exact integer arithmetic.

    P_4(k)=k^2.  If r is square, the child is exactly q*k.
    Otherwise (k>0) the two children bracket sqrt(r)*k and are obtained
    by isqrt(r*k^2) without floating point.
    """
    if not isinstance(r, int) or r < 1:
        raise ValueError("r must be >=1")
    _check_nonnegative("k", k)
    n = r * k * k
    q = isqrt(n)
    if q * q == n:
        return (q,)
    return (q, q + 1)


if __name__ == "__main__":
    # Tiny smoke print, intentionally not a theorem claim.
    for s, r, k in [(3, 2, 2), (4, 5, 1), (5, 4, 3)]:
        print(s, r, k, polygonal(s, k), parent_children(s, r, k))
