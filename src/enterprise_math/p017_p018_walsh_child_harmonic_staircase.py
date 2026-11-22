"""Harmonic quotient-depth staircase on the total-conductor Euclidean child atlas.

After total-conductor collapse, a parent conductor m<=k with child remainder r
satisfies

    k=a*m+r,       a=floor(k/m),
    0<r<k/2,
    m|k-r,
    m>r.

Put N=k-r.  Then the quotient is exactly the complementary divisor

    a=N/m,

and the large-conductor condition m>r is equivalent to

    a < N/r = k/r - 1.

Therefore child scale itself bounds the number of quotient worlds.  For every
integer j>=1,

    k/(j+2) < r <= k/(j+1)

implies

    a <= j.

In particular:

* k/3 < r < k/2: only quotient a=1 can occur;
* k/4 < r <= k/3: only a=1,2 can occur;
* deeper child worlds expose quotient precision gradually.

The Euclidean parent reconstruction also carries the multiplicative weight
r/k.  On the j-th shell it obeys

    r/k <= 1/(j+1).

Thus quotient-language width grows only when the BRC child weight shrinks.  The
number of candidate parent conductors in one child is at most j, because each
integer quotient a=1,...,j determines at most one conductor m=(k-r)/a.

This is an exact complexity/precision staircase.  It does not bound the signed
value of any selected conductor column and does not prove a prime-gap theorem.
"""

from __future__ import annotations

from fractions import Fraction

from .p017_p018_walsh_total_conductor_child_atlas import child_conductor_family


def child_quotient_rows(k: int, child: int) -> tuple[dict[str, int], ...]:
    """Return the exact quotient a=(k-r)/m attached to each child conductor."""
    family = child_conductor_family(k, child)
    gap = k - child
    rows: list[dict[str, int]] = []
    for m in family:
        if gap % m:
            raise AssertionError("child conductor does not divide k-r")
        a = gap // m
        if k // m != a or k % m != child:
            raise AssertionError("co-divisor failed to equal Euclidean quotient")
        if not a * child < gap:
            raise AssertionError("large-conductor condition failed a*r<k-r")
        rows.append({"conductor_m": m, "quotient_a": a})
    return tuple(sorted(rows, key=lambda row: row["quotient_a"]))


def child_harmonic_shell(k: int, child: int) -> dict[str, object]:
    """Return the least j with r>k/(j+2), and certify every quotient a<=j."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(child, bool) or not isinstance(child, int) or not (0 < 2 * child < k):
        raise ValueError("child must satisfy 0<child<k/2")

    # Unique j>=1 with k/(j+2)<r<=k/(j+1), except exact reciprocal boundaries;
    # use the safe ceiling j=floor((k-r-1)/r), which is exactly the largest
    # integer quotient allowed by a*r<k-r.
    max_quotient = (k - child - 1) // child
    if max_quotient < 1:
        raise AssertionError("strict half-scale child should allow at least quotient one")
    rows = child_quotient_rows(k, child)
    if any(int(row["quotient_a"]) > max_quotient for row in rows):
        raise AssertionError("child quotient escaped harmonic staircase ceiling")
    if len(rows) > max_quotient:
        raise AssertionError("one child retained more conductors than quotient worlds")

    weight = Fraction(child, k)
    # max_quotient=j implies child >? The exact strict relation is
    # j*r < k-r <= (j+1)r, hence (j+1)r<k <=(j+2)r after rearrangement.
    j = max_quotient
    if not (Fraction(k, j + 2) <= child and child < Fraction(k, j + 1)):
        # Exact equality at the lower endpoint may occur because of the -1 in
        # the integer quotient ceiling; retain a direct safe bound instead.
        if not weight <= Fraction(1, j + 1):
            raise AssertionError("child weight escaped quotient-depth reciprocal ceiling")

    return {
        "k": k,
        "child_scale_r": child,
        "gap_N": k - child,
        "maximum_quotient_world": max_quotient,
        "candidate_conductor_count": len(rows),
        "parent_weight_r_over_k": weight,
        "reciprocal_weight_ceiling": Fraction(1, max_quotient + 1),
        "quotient_rows": rows,
        "quotient_precision_opens_with_depth": True,
    }


def declared_shell_ceiling(k: int, child: int, j: int) -> dict[str, object]:
    """Verify k/(j+2)<r<=k/(j+1) forces all actual quotient rows to a<=j."""
    if isinstance(j, bool) or not isinstance(j, int) or j < 1:
        raise ValueError("j must be a positive integer")
    if not (Fraction(k, j + 2) < child <= Fraction(k, j + 1)):
        raise ValueError("child does not lie in the declared harmonic shell")
    rows = child_quotient_rows(k, child)
    if any(int(row["quotient_a"]) > j for row in rows):
        raise AssertionError("declared harmonic shell retained quotient a>j")
    if len(rows) > j:
        raise AssertionError("declared harmonic shell retained more than j conductor worlds")
    return {
        "k": k,
        "child_scale_r": child,
        "shell_index_j": j,
        "parent_weight_r_over_k": Fraction(child, k),
        "shell_weight_upper": Fraction(1, j + 1),
        "quotient_rows": rows,
        "all_quotients_at_most_j": True,
        "conductor_world_count_at_most_j": True,
    }
