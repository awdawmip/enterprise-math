"""p-adic exterior/guard specializations for the R004 <-> A3 bridge."""

from __future__ import annotations

from itertools import combinations, product
from math import gcd
from typing import Iterable, Sequence, Tuple

from .precision_structural_target_cut_compiler import row_module_elements


def _vp_residue(a: int, p: int, K: int) -> int:
    modulus = p ** K
    a %= modulus
    if a == 0:
        return K
    v = 0
    while v < K and a % p == 0:
        a //= p
        v += 1
    return v


def content_gcd(vector: Sequence[int]) -> int:
    g = 0
    for value in vector:
        g = gcd(g, abs(int(value)))
    return g


def exterior_integer_smith_profile(capacity: Sequence[int]) -> Tuple[int, ...]:
    """Nonzero Smith invariants of c -> capacity wedge c over Z."""
    if len(capacity) < 2:
        return tuple()
    g = content_gcd(capacity)
    if g == 0:
        return tuple()
    return (g,) * (len(capacity) - 1)


def exterior_padic_profile(capacity: Sequence[int], p: int, K: int) -> Tuple[int, ...]:
    """Invariant-factor exponent depths of im(capacity wedge -) over Z/p^K."""
    if len(capacity) < 2:
        return tuple()
    s = min(_vp_residue(v, p, K) for v in capacity)
    if s >= K:
        return tuple()
    return (K - s,) * (len(capacity) - 1)


def wedge_coordinates(u: Sequence[int], v: Sequence[int], modulus: int) -> Tuple[int, ...]:
    return tuple((int(u[i]) * int(v[j]) - int(u[j]) * int(v[i])) % modulus
                 for i, j in combinations(range(len(u)), 2))


def projective_agreement_depth(u: Sequence[int], v: Sequence[int], p: int, K: int) -> int:
    if len(u) != len(v):
        raise ValueError("dimension mismatch")
    if not any(int(x) % p for x in u) or not any(int(x) % p for x in v):
        raise ValueError("projective directions must be primitive mod p")
    minors = wedge_coordinates(u, v, p ** K)
    if not minors:
        return K
    return min(_vp_residue(value, p, K) for value in minors)


def projective_defect_distance(u: Sequence[int], v: Sequence[int], p: int, K: int) -> int:
    return K - projective_agreement_depth(u, v, p, K)


def _mat_vec(matrix, x, modulus):
    return tuple(sum(int(row[j]) * int(x[j]) for j in range(len(x))) % modulus
                 for row in matrix)


def _kernel_elements(matrix, p: int, K: int, width: int):
    modulus = p ** K
    return tuple(x for x in product(range(modulus), repeat=width)
                 if all(value == 0 for value in _mat_vec(matrix, x, modulus)))


def _profile_from_torsion_counts(counts: Sequence[int], p: int, K: int) -> Tuple[int, ...]:
    alpha = []
    for count in counts:
        n = int(count)
        a = 0
        while n > 1:
            if n % p:
                raise AssertionError("torsion count is not a p-power")
            n //= p
            a += 1
        alpha.append(a)
    beta = [0] * (K + 2)
    for j in range(1, K + 1):
        beta[j] = alpha[j] - alpha[j - 1]
    exponents = []
    for j in range(K, 0, -1):
        exponents.extend([j] * (beta[j] - beta[j + 1]))
    return tuple(exponents)


def subgroup_exponent_profile(elements: Iterable[Tuple[int, ...]], p: int, K: int) -> Tuple[int, ...]:
    elements = frozenset(elements)
    modulus = p ** K
    counts = [1]
    for j in range(1, K + 1):
        scalar = p ** j
        counts.append(sum(1 for x in elements
                          if all((scalar * value) % modulus == 0 for value in x)))
    return _profile_from_torsion_counts(counts, p, K)


def guard_image_exponent_profile(A, W, p: int, K: int) -> Tuple[int, ...]:
    width = len(A[0]) if A else len(W[0])
    modulus = p ** K
    image = {_mat_vec(W, x, modulus) for x in _kernel_elements(A, p, K, width)}
    return subgroup_exponent_profile(image, p, K)


def row_defect_exponent_profile(A, W, p: int, K: int) -> Tuple[int, ...]:
    """Profile of (Row(A)+Row(W))/Row(A) by exact quotient torsion counts."""
    width = len(A[0]) if A else len(W[0])
    modulus = p ** K
    RA = row_module_elements(tuple(tuple(r) for r in A), p, K, width=width)
    RC = row_module_elements(tuple(tuple(r) for r in tuple(A) + tuple(W)), p, K, width=width)
    counts = [1]
    for j in range(1, K + 1):
        scalar = p ** j
        numerator = 0
        for c in RC:
            pc = tuple((scalar * value) % modulus for value in c)
            if pc in RA:
                numerator += 1
        counts.append(numerator // len(RA))
    return _profile_from_torsion_counts(counts, p, K)
