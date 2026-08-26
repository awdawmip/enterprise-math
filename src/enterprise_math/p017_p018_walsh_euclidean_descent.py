"""Exact Euclidean one-step descent of orientation-Walsh boundary columns.

Let k>=3 and write

    k = 2H + epsilon,       epsilon in {0,1}, H=floor(k/2).

Positive odd radii 1<=r<k are r=2t+1 with 0<=t<H.  Fix a nonempty odd
squarefree conductor q transverse to M=k(k+1).  One q-block in t has exactly
one root for every orientation sign pattern.  Since the Walsh sign cube has
zero constant mode, every complete q-block cancels exactly.

Write

    H = A*q + h,            0<=h<q,

and define the Euclidean child scale

    k' = 2h + epsilon.

Then

    k-k' = 2Aq,

so k=k' (mod q) and therefore

    k(k+1)=k'(k'+1) (mod q).

The incomplete parent block t=0,...,h-1 is exactly the complete positive-odd
radius domain of scale k'.  Hence the raw signed q-column boundary at parent
scale k equals the same raw q-column at child scale k'.

Moreover h<q implies

    q > floor((k'-1)/2).

Thus q lies in the child's half-cutoff/single-use regime.  If the parent is
actually repeatable, A>=1, then q divides

    n=(k-k')/2

and the two inequalities combine to give the strict half-scale contraction

    k' < (k+1)/2.

So every repeatable parent boundary column executes in one child world of at
most half the parent scale, where its conductor is already single-use.  For a
fixed child k', the possible parent conductors form only the large-divisor
family

    q | (k-k')/2,       q > floor((k'-1)/2).

This is an exact P017/P018/BRC transport theorem.  It explains boundary carry
as scale-reduced execution rather than an uncontrolled error.  Anchor survival
may be carried as an external radius filter; the raw conductor/root identity
itself is exact.  No estimate of the signed child sum and no Legendre proof is
claimed.
"""

from __future__ import annotations

from itertools import product
from math import prod


def _require_transverse_conductor(k: int, conductor_primes: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in conductor_primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("conductor_primes must be nonempty and distinct")
    M = k * (k + 1)
    for p in normalized:
        if p < 3 or p % 2 == 0 or M % p == 0:
            raise ValueError("conductor primes must be odd and transverse to M")
    return normalized


def euclidean_child_scale(k: int, conductor: int) -> dict[str, int | bool]:
    """Return H=Aq+h and child k'=2h+epsilon with its exact contraction data."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor < 1 or conductor % 2 == 0:
        raise ValueError("conductor must be a positive odd integer")
    epsilon = k % 2
    H = k // 2
    block_count, h = divmod(H, conductor)
    child = 2 * h + epsilon
    if (k - child) != 2 * block_count * conductor:
        raise AssertionError("Euclidean child reconstruction failed")
    if k % conductor != child % conductor:
        raise AssertionError("parent and child scales lost congruence modulo q")
    if k * (k + 1) % conductor != child * (child + 1) % conductor:
        raise AssertionError("parent and child centers lost congruence modulo q")
    child_half_cutoff = (child - 1) // 2 if child >= 1 else -1
    if not conductor > child_half_cutoff:
        raise AssertionError("descended conductor did not enter child single-use half-cutoff regime")

    repeatable_parent = block_count >= 1
    large_divisor_parent = (k - child) // 2
    if repeatable_parent:
        if large_divisor_parent % conductor:
            raise AssertionError("repeatable parent conductor did not divide child-gap quotient")
        if not child < (k + 1) / 2:
            raise AssertionError("repeatable Euclidean child failed strict half-scale contraction")

    return {
        "k": k,
        "conductor_q": conductor,
        "parity_epsilon": epsilon,
        "positive_odd_radius_count_H": H,
        "complete_q_blocks_A": block_count,
        "boundary_prefix_h": h,
        "child_scale_k_prime": child,
        "child_half_cutoff": child_half_cutoff,
        "repeatable_parent_conductor": repeatable_parent,
        "strict_scale_contraction": child < k,
        "strict_half_scale_contraction_when_repeatable": (not repeatable_parent) or child < (k + 1) / 2,
        "child_gap_half_n": large_divisor_parent,
        "conductor_divides_child_gap_half": (not repeatable_parent) or large_divisor_parent % conductor == 0,
        "child_conductor_single_use": True,
    }


def _orientation_root_sign(k: int, radius: int, primes: tuple[int, ...], signs: tuple[int, ...]) -> int:
    M = k * (k + 1)
    for p, sign in zip(primes, signs):
        if (M - sign * radius) % p:
            return 0
    return prod(signs, start=1)


def raw_orientation_column(k: int, conductor_primes: tuple[int, ...]) -> int:
    """Return the raw positive-radius signed root column on scale k."""
    primes = _require_transverse_conductor(k, conductor_primes)
    total = 0
    for radius in range(1, k, 2):
        value = 0
        for signs in product((1, -1), repeat=len(primes)):
            value += _orientation_root_sign(k, radius, primes, signs)
        total += value
    return total


def euclidean_boundary_column(k: int, conductor_primes: tuple[int, ...]) -> dict[str, object]:
    """Verify parent column equals child column after complete q-block cancellation."""
    primes = _require_transverse_conductor(k, conductor_primes)
    q = prod(primes)
    data = euclidean_child_scale(k, q)
    child = int(data["child_scale_k_prime"])
    H = int(data["positive_odd_radius_count_H"])
    h = int(data["boundary_prefix_h"])

    parent = raw_orientation_column(k, primes)

    block_rows: list[dict[str, int]] = []
    for block in range(int(data["complete_q_blocks_A"])):
        block_sum = 0
        for t in range(block * q, (block + 1) * q):
            radius = 2 * t + 1
            for signs in product((1, -1), repeat=len(primes)):
                block_sum += _orientation_root_sign(k, radius, primes, signs)
        if block_sum != 0:
            raise AssertionError("complete q-block retained a nonzero Walsh constant mode")
        block_rows.append({"block": block, "signed_sum": block_sum})

    boundary = 0
    for t in range(H - h, H):
        radius = 2 * t + 1
        for signs in product((1, -1), repeat=len(primes)):
            boundary += _orientation_root_sign(k, radius, primes, signs)

    local_boundary = 0
    start = H - h
    for local_t in range(h):
        parent_radius = 2 * (start + local_t) + 1
        child_radius = 2 * local_t + 1
        for signs in product((1, -1), repeat=len(primes)):
            parent_value = _orientation_root_sign(k, parent_radius, primes, signs)
            child_value = _orientation_root_sign(child, child_radius, primes, signs)
            if parent_value != child_value:
                raise AssertionError("parent boundary root pattern changed under Euclidean descent")
            local_boundary += parent_value

    child_column = raw_orientation_column(child, primes) if child >= 3 else local_boundary
    if not (parent == boundary == local_boundary == child_column):
        raise AssertionError("Euclidean boundary/child column identity failed")

    return {
        **data,
        "conductor_primes": primes,
        "parent_raw_signed_column": parent,
        "parent_boundary_signed_column": boundary,
        "child_raw_signed_column": child_column,
        "euclidean_boundary_descent_identity": True,
        "complete_block_rows": tuple(block_rows),
    }
