"""Strict half-scale child atlas after fixed-total Walsh conductor collapse.

For every nontrivial odd squarefree conductor m<=k transverse to M=k(k+1), put

    r = k mod m.

Transversality excludes r=0 and r=m-1.  More importantly r<k/2.  Indeed if
m>k/2 then k=m+r and r=k-m<k/2; if m<=k/2 then r<m<=k/2.

The congruence k=r (mod m) is equivalent to

    m | k-r.

Also

    k(k+1)=r(r+1) (mod m),

so parent transversality is exactly gcd(m,r(r+1))=1.  Conversely, if

    0<r<k/2,
    m|k-r,
    m>r,
    m odd squarefree,
    gcd(m,r(r+1))=1,

then k mod m=r and m is transverse to the parent center.

Thus nontrivial parent conductors are in bijection with a strict half-scale child
atlas whose conductor family at child r is the large squarefree divisor family
of the single integer k-r.

Combining this bijection with the exact selected-modulus Euclidean descent

    B_m(k)=(r/k)B_m(r)

gives

    sum_(m<=k,m>1,transverse sf) B_m(k)
      = 1/k * sum_(0<r<k/2) r
          sum_(m|k-r,m>r,sf odd,gcd(m,r(r+1))=1) B_m(r).

This is a second exact BRC after the bi-primitive plane first recoalesces to total
conductor.  The child modulus family is no longer arbitrary: it is a large-
divisor family of k-r, and every child scale is strictly less than half the
parent scale.  No estimate of the child sums or Legendre theorem is asserted.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_walsh_remainder_descent import selected_modulus_tent_contribution


def _mobius_squarefree(value: int) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    omega = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            omega += 1
            if remaining % p == 0:
                return 0
        p += 1
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def child_conductor_family(k: int, child: int) -> tuple[int, ...]:
    """Return all nontrivial parent conductors whose Euclidean remainder child is r."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(child, bool) or not isinstance(child, int) or not (0 < 2 * child < k):
        raise ValueError("child must satisfy 0<child<k/2")
    gap = k - child
    rows: list[int] = []
    for m in range(3, gap + 1, 2):
        if gap % m:
            continue
        if m <= child or _mobius_squarefree(m) == 0:
            continue
        if gcd(m, child * (child + 1)) != 1:
            continue
        if k % m != child:
            raise AssertionError("child conductor conditions failed to reconstruct k mod m")
        if gcd(m, k * (k + 1)) != 1:
            raise AssertionError("child transversality failed to reconstruct parent transversality")
        rows.append(m)
    return tuple(rows)


def conductor_child_bijection(k: int, conductor: int) -> dict[str, object]:
    """Verify one parent conductor lands in the strict half-scale divisor atlas."""
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor <= 1 or conductor > k or conductor % 2 == 0:
        raise ValueError("conductor must be odd with 1<m<=k")
    if _mobius_squarefree(conductor) == 0:
        raise ValueError("conductor must be squarefree")
    if gcd(conductor, k * (k + 1)) != 1:
        raise ValueError("conductor must be transverse to k(k+1)")
    r = k % conductor
    if r == 0:
        raise AssertionError("transverse conductor divided k")
    if not 0 < 2 * r < k:
        raise AssertionError("nontrivial conductor child failed strict half-scale contraction")
    gap = k - r
    if gap % conductor or conductor <= r:
        raise AssertionError("parent conductor did not become a large divisor of k-r")
    if gcd(conductor, r * (r + 1)) != 1:
        raise AssertionError("parent transversality did not descend to child center")
    family = child_conductor_family(k, r)
    if conductor not in family:
        raise AssertionError("parent conductor missing from reconstructed child family")
    return {
        "k": k,
        "parent_conductor_m": conductor,
        "child_scale_r": r,
        "gap_k_minus_r": gap,
        "conductor_divides_gap": True,
        "conductor_exceeds_child": True,
        "child_strictly_below_half_parent": True,
        "child_conductor_family": family,
        "bijection_membership": True,
    }


def total_conductor_child_atlas_sum(k: int, conductors: tuple[int, ...]) -> dict[str, object]:
    """Verify the selected-conductor sum equals the strict half-scale child atlas sum.

    The supplied conductors must be the complete declared transverse squarefree
    family for the comparison; this routine is intended for bounded regressions
    and exact subfamilies closed under the child grouping.
    """
    normalized = tuple(sorted(set(int(m) for m in conductors)))
    if len(normalized) != len(conductors):
        raise ValueError("conductors must be distinct")
    for m in normalized:
        conductor_child_bijection(k, m)

    parent = sum((selected_modulus_tent_contribution(k, m) for m in normalized), start=Fraction(0, 1))
    grouped: dict[int, list[int]] = {}
    for m in normalized:
        grouped.setdefault(k % m, []).append(m)

    child_sum = Fraction(0, 1)
    rows: list[dict[str, object]] = []
    for r, moduli in sorted(grouped.items()):
        inner = sum((selected_modulus_tent_contribution(r, m) for m in moduli), start=Fraction(0, 1))
        term = Fraction(r, k) * inner
        child_sum += term
        rows.append(
            {
                "child_scale_r": r,
                "parent_conductors": tuple(sorted(moduli)),
                "child_selected_sum": inner,
                "weighted_parent_term": term,
            }
        )
    if parent != child_sum:
        raise AssertionError("total-conductor Euclidean child atlas failed exact reconstruction")
    return {
        "k": k,
        "parent_conductors": normalized,
        "parent_selected_sum": parent,
        "child_atlas_sum": child_sum,
        "strict_half_scale_child_atlas": True,
        "rows": tuple(rows),
    }
