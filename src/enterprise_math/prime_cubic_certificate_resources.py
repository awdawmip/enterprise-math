"""Exact resource laws for finite cubic certificate composition.

This module abstracts the two active finite resources in the R005-B cubic
classification:

* an effective relative prime-interval row with integer parameter Delta;
* an exhaustive cofactor-gap database through an integer scale X.

It does not verify either external resource.  It freezes only the exact integer
conversion from resource strength to the largest cubic basin coordinate covered.
"""

from math import isqrt


def vertical_effective_k_max(delta: int) -> int:
    """Return the exact largest k fitting one effective relative interval row.

    The cubic fit condition is

        3*(k+1)*(delta-1) > k^2.

    Writing D=delta-1, the exact last integer satisfying it is k=3D: at k=3D
    the margin is 3D>0, and at k=3D+1 the margin is -1.
    """
    if delta <= 1:
        raise ValueError("delta must exceed 1")
    return 3 * (delta - 1)


def horizontal_database_k_max(coverage_limit: int) -> int:
    """Return the exact largest k whose q>k cofactor points lie below X.

    The worst q>k coordinate is k^2-k.  Requiring k^2-k < X is equivalent to

        k^2-k <= X-1.

    Hence

        K_H(X)=floor((1+sqrt(4X-3))/2).

    The implementation uses integer square root only.
    """
    if coverage_limit <= 0:
        raise ValueError("coverage_limit must be positive")
    return (1 + isqrt(4 * coverage_limit - 3)) // 2


def horizontal_coverage_required_for_k(k: int) -> int:
    """Return the least integer X making k^2-k < X."""
    if k < 1:
        raise ValueError("k must be positive")
    return k * k - k + 1


def effective_delta_required_for_k(k: int) -> int:
    """Return the least integer Delta satisfying the cubic fit inequality."""
    if k < 1:
        raise ValueError("k must be positive")
    denominator = 3 * (k + 1)
    d_min = (k * k) // denominator + 1
    return d_min + 1


def combined_resource_k_max(delta: int, coverage_limit: int) -> int:
    """Return min(vertical effective cap, horizontal database cap).

    This assumes separately that the effective theorem's x0 is reached whenever
    the finite Oppermann certificate no longer applies, and that an early upper
    prefix / gap-cap certificate is already available.  Those are semantic
    preconditions, not encoded by the two scalar resources here.
    """
    return min(
        vertical_effective_k_max(delta),
        horizontal_database_k_max(coverage_limit),
    )


def coverage_required_to_match_delta(delta: int) -> int:
    """Return the least horizontal X needed to exploit a Delta row fully."""
    return horizontal_coverage_required_for_k(vertical_effective_k_max(delta))
