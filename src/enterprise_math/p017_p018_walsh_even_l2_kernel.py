"""Exact even-conductor L2 pair kernel for the P017/P018 orientation-Walsh boundary.

Fix k>=3, M=k(k+1), a prime cutoff z and a conductor cutoff C.  For an
anchor-surviving radius r let

    sigma_p(r)=+1  if p | M-r,
               -1  if p | M+r,
                0  otherwise

for odd transverse primes p<=z.  For squarefree q supported on those primes put

    chi_q(r)=prod_(p|q) sigma_p(r).

The reusable symmetric Walsh core only needs nontrivial even conductors, so the
basic column is

    A_q = sum_r chi_q(r),      q<=C, omega(q) even, q>1.

Its L2 energy has the exact pair expansion

    sum_q A_q^2 = sum_(r,s) K_C(r,s).

For one pair define two disjoint collision prime sets:

    U(r,s): primes active on r and s in the SAME orientation,
    V(r,s): primes active on r and s in OPPOSITE orientations.

Then every q contributing to chi_q(r)chi_q(s) factors uniquely q=a*b with

    a | rad(U),  b | rad(V),  (a,b)=1,

and the sign is mu(b).  Projecting to even total support gives the exact
hyperbolic kernel

    K_C(r,s)
      = 1/2 * sum_(a|U,b|V,ab<=C) [mu(a)+mu(b)] - 1,

where the final -1 removes the trivial conductor q=1.

The pair geometry itself collapses under the 45-degree change of variables

    x=(r+s)/2,
    y=(r-s)/2.

Because surviving radii are odd, x,y are integers.  For every transverse odd p,

    p in U  iff  p|y and x=+/-M (mod p),
    p in V  iff  p|x and y=+/-M (mod p).

Thus the second moment does not create an arbitrary k^2-scale congruence
problem.  It recoalesces to the same root-channel language on the smaller
triangle

    0<x<k,  |y|<min(x,k-x),

with the difference coordinate satisfying |y|<k/2.  This is an exact
second-order BRC/self-similar descent.  It is a representation theorem only: no
sublinear energy estimate or Legendre theorem is claimed here.
"""

from __future__ import annotations

from itertools import combinations
from math import prod

from .legendre import primes_up_to
from .p017_mirror import anchor_surviving_radius, mirror_transverse_supports


def _mu_squarefree_from_size(size: int) -> int:
    return -1 if size % 2 else 1


def _transverse_primes(k: int, cutoff: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 1:
        raise ValueError("cutoff must be a positive integer")
    M = k * (k + 1)
    return tuple(
        p for p in primes_up_to(min(k, cutoff))
        if p % 2 == 1 and M % p != 0
    )


def orientation_sigma(k: int, radius: int, prime: int) -> int:
    """Return +1/-1/0 according to the transverse mirror orientation at p."""
    M = k * (k + 1)
    if M % prime == 0:
        raise ValueError("prime must be transverse to M")
    lower = (M - radius) % prime == 0
    upper = (M + radius) % prime == 0
    if lower and upper:
        raise AssertionError("transverse prime hit both mirror orientations")
    return 1 if lower else -1 if upper else 0


def pair_collision_partition(
    k: int,
    radius_r: int,
    radius_s: int,
    prime_cutoff: int,
) -> dict[str, object]:
    """Return SAME/OPPOSITE collision prime sets and verify midpoint-difference form."""
    for radius in (radius_r, radius_s):
        if not anchor_surviving_radius(k, radius):
            raise ValueError("both radii must survive the anchor sieve")
    if (radius_r - radius_s) % 2:
        raise AssertionError("surviving radii must have the same odd parity")

    M = k * (k + 1)
    x = (radius_r + radius_s) // 2
    y = (radius_r - radius_s) // 2
    primes = _transverse_primes(k, prime_cutoff)
    same: list[int] = []
    opposite: list[int] = []

    for p in primes:
        sig_r = orientation_sigma(k, radius_r, p)
        sig_s = orientation_sigma(k, radius_s, p)
        product_sign = sig_r * sig_s
        if product_sign == 1:
            same.append(p)
        elif product_sign == -1:
            opposite.append(p)

        same_coordinate = (y % p == 0) and (
            (x - M) % p == 0 or (x + M) % p == 0
        )
        opposite_coordinate = (x % p == 0) and (
            (y - M) % p == 0 or (y + M) % p == 0
        )
        if same_coordinate != (product_sign == 1):
            raise AssertionError("same-orientation collision lost midpoint/difference characterization")
        if opposite_coordinate != (product_sign == -1):
            raise AssertionError("opposite-orientation collision lost midpoint/difference characterization")
        if same_coordinate and opposite_coordinate:
            raise AssertionError("same/opposite collision sets are not disjoint")

    if not (0 < x < k):
        raise AssertionError("midpoint escaped the physical triangle")
    if abs(y) >= min(x, k - x):
        # Equality is possible only if one original radius is zero or k, both excluded.
        raise AssertionError("difference coordinate escaped the physical triangle")

    return {
        "k": k,
        "radius_r": radius_r,
        "radius_s": radius_s,
        "prime_cutoff": prime_cutoff,
        "midpoint_x": x,
        "difference_y": y,
        "same_orientation_collision_primes": tuple(same),
        "opposite_orientation_collision_primes": tuple(opposite),
        "same_collision_radical": prod(same, start=1),
        "opposite_collision_radical": prod(opposite, start=1),
        "collision_sets_disjoint": True,
        "self_similar_midpoint_difference_geometry": True,
    }


def _squarefree_divisors(primes: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    rows: list[tuple[int, int]] = []
    for size in range(len(primes) + 1):
        mu = _mu_squarefree_from_size(size)
        for subset in combinations(primes, size):
            rows.append((prod(subset, start=1), mu))
    return tuple(rows)


def even_pair_kernel(
    k: int,
    radius_r: int,
    radius_s: int,
    prime_cutoff: int,
    conductor_cutoff: int,
) -> dict[str, object]:
    """Return K_C(r,s) both by direct even-conductor enumeration and hyperbola sum."""
    if conductor_cutoff < 1:
        raise ValueError("conductor_cutoff must be positive")
    part = pair_collision_partition(k, radius_r, radius_s, prime_cutoff)
    same = tuple(int(p) for p in part["same_orientation_collision_primes"])
    opposite = tuple(int(p) for p in part["opposite_orientation_collision_primes"])

    # Direct q enumeration over the collision prime union.
    union = same + opposite
    direct = 0
    q_rows: list[dict[str, object]] = []
    for size in range(2, len(union) + 1, 2):
        for subset in combinations(union, size):
            q = prod(subset)
            if q > conductor_cutoff:
                continue
            sign = _mu_squarefree_from_size(sum(1 for p in subset if p in opposite))
            direct += sign
            q_rows.append({"conductor": q, "primes": subset, "pair_sign": sign})

    hyperbola_twice = 0
    split_rows: list[dict[str, int]] = []
    for a, mu_a in _squarefree_divisors(same):
        for b, mu_b in _squarefree_divisors(opposite):
            if a * b > conductor_cutoff:
                continue
            term = mu_a + mu_b
            hyperbola_twice += term
            split_rows.append({"same_divisor": a, "opposite_divisor": b, "twice_term": term})
    if hyperbola_twice % 2:
        raise AssertionError("even-conductor parity projection produced a half-integer")
    hyperbola = hyperbola_twice // 2 - 1  # remove q=1
    if direct != hyperbola:
        raise AssertionError("direct even-conductor pair kernel disagreed with hyperbolic formula")

    return {
        **part,
        "conductor_cutoff": conductor_cutoff,
        "direct_even_nontrivial_pair_kernel": direct,
        "hyperbolic_even_nontrivial_pair_kernel": hyperbola,
        "kernel_identity": True,
        "direct_conductor_rows": tuple(q_rows),
        "hyperbola_split_rows": tuple(split_rows),
    }


def even_conductor_l2_energy(k: int, prime_cutoff: int, conductor_cutoff: int) -> dict[str, object]:
    """Verify sum_q A_q^2 = sum_(r,s) K_C(r,s) on a bounded physical basin."""
    primes = _transverse_primes(k, prime_cutoff)
    radii = tuple(r for r in range(1, k) if anchor_surviving_radius(k, r))

    conductors: list[tuple[int, tuple[int, ...]]] = []
    for size in range(2, len(primes) + 1, 2):
        for subset in combinations(primes, size):
            q = prod(subset)
            if q <= conductor_cutoff:
                conductors.append((q, subset))

    column_rows: list[dict[str, object]] = []
    direct_energy = 0
    for q, subset in conductors:
        column = 0
        for radius in radii:
            value = 1
            for p in subset:
                sigma = orientation_sigma(k, radius, p)
                if sigma == 0:
                    value = 0
                    break
                value *= sigma
            column += value
        direct_energy += column * column
        column_rows.append({"conductor": q, "primes": subset, "column_sum": column})

    pair_energy = 0
    for r in radii:
        for s in radii:
            pair_energy += int(
                even_pair_kernel(k, r, s, prime_cutoff, conductor_cutoff)[
                    "direct_even_nontrivial_pair_kernel"
                ]
            )
    if direct_energy != pair_energy:
        raise AssertionError("even-conductor L2 column energy disagreed with radius-pair kernel")

    return {
        "k": k,
        "prime_cutoff": prime_cutoff,
        "conductor_cutoff": conductor_cutoff,
        "surviving_radius_count": len(radii),
        "even_conductor_count": len(conductors),
        "direct_column_l2_energy": direct_energy,
        "radius_pair_kernel_energy": pair_energy,
        "l2_pair_collapse": True,
        "column_rows": tuple(column_rows),
    }
