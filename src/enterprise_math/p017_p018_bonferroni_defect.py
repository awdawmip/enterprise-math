"""Exact defect of odd Bonferroni proof precision.

For a single support of cardinality c and a positive odd truncation order m,

    b_m(c)=sum_{j=1}^m (-1)^(j+1) binom(c,j)

satisfies the exact identity

    b_m(0)=0,
    b_m(c)=1+binom(c-1,m)  for c>=1.

Hence for any finite family of signed states with transverse-support sizes c_x,

    B_m = U + E_m,

where U is the number of nonempty supports and

    E_m = sum_{c_x>=m+1} binom(c_x-1,m).

Thus the complete error of an odd-order Bonferroni primality certificate is an
integer high-support defect.  Raising precision from m to m+2 does not vaguely
"improve an approximation": it removes a precisely identified layer of support
multiplicity.

This is the classical alternating-binomial identity repackaged as a finite
proof-precision defect coordinate.  It is intended to interface with P017 CG11,
which constrains the orthogonal column/prime-power collision multiplicities.
"""

from __future__ import annotations

from math import comb


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def odd_bonferroni_point_value(support_size: int, order: int) -> int:
    _require_nonnegative("support_size", support_size)
    if isinstance(order, bool) or not isinstance(order, int) or order < 1 or order % 2 == 0:
        raise ValueError("order must be a positive odd integer")
    c = support_size
    return sum(
        comb(c, degree) if degree % 2 == 1 else -comb(c, degree)
        for degree in range(1, min(order, c) + 1)
    )


def odd_bonferroni_point_defect(support_size: int, order: int) -> dict[str, int]:
    """Return b_m(c)-1_{c>0}=binom(c-1,m) exactly."""
    value = odd_bonferroni_point_value(support_size, order)
    c = support_size
    indicator = 1 if c > 0 else 0
    defect = value - indicator
    expected = comb(c - 1, order) if c > 0 and c - 1 >= order else 0
    if defect != expected:
        raise AssertionError("odd Bonferroni point defect identity failed")
    return {
        "support_size": c,
        "order": order,
        "bonferroni_value": value,
        "nonempty_indicator": indicator,
        "defect": defect,
    }


def family_bonferroni_defect(support_sizes: tuple[int, ...], order: int) -> dict[str, int]:
    """Certify B_m=U+E_m for a finite support-size family."""
    if not support_sizes:
        raise ValueError("support_sizes must be nonempty")
    for value in support_sizes:
        _require_nonnegative("support size", value)
    rows = tuple(odd_bonferroni_point_defect(value, order) for value in support_sizes)
    bonferroni = sum(row["bonferroni_value"] for row in rows)
    union = sum(row["nonempty_indicator"] for row in rows)
    defect = sum(row["defect"] for row in rows)
    if bonferroni != union + defect:
        raise AssertionError("family Bonferroni defect failed to telescope")
    return {
        "state_count": len(support_sizes),
        "order": order,
        "bonferroni_upper": bonferroni,
        "nonempty_union": union,
        "high_support_defect": defect,
    }
