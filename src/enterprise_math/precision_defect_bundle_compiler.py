"""Finite defect-bundle / A4 escalation reference compiler.

For an arbitrary target under a coarse quotient, the canonical nonlinear defect object is
its coarse-to-target support correspondence.  Group-defect compression is admitted only
when a stronger translation-derivative homogeneity gate passes.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable, Dict, FrozenSet, Hashable, Iterable, Mapping, Optional, Sequence, Tuple


def fiber_supports(states: Iterable[int], coarse_fn: Callable[[int], Hashable],
                   target_fn: Callable[[int], Hashable]) -> Dict[Hashable, FrozenSet[Hashable]]:
    out = defaultdict(set)
    for x in states:
        out[coarse_fn(x)].add(target_fn(x))
    return {a: frozenset(values) for a, values in out.items()}


def target_descends(states: Iterable[int], coarse_fn: Callable[[int], Hashable],
                    target_fn: Callable[[int], Hashable]) -> bool:
    return all(len(values) == 1 for values in fiber_supports(states, coarse_fn, target_fn).values())


def support_relation(states: Iterable[int], coarse_fn: Callable[[int], Hashable],
                     target_fn: Callable[[int], Hashable]) -> FrozenSet[Tuple[Hashable, Hashable]]:
    return frozenset((coarse_fn(x), target_fn(x)) for x in states)


def compose_relations(left: Iterable[Tuple[Hashable, Hashable]],
                      right: Iterable[Tuple[Hashable, Hashable]]) -> FrozenSet[Tuple[Hashable, Hashable]]:
    right_by_source = defaultdict(set)
    for y, z in right:
        right_by_source[y].add(z)
    out = set()
    for x, y in left:
        for z in right_by_source.get(y, ()):
            out.add((x, z))
    return frozenset(out)


def additive_subgroups_mod(n: int) -> Tuple[FrozenSet[int], ...]:
    if n <= 0:
        raise ValueError("modulus must be positive")
    groups = set()
    for step in range(1, n + 1):
        if n % step == 0:
            groups.add(frozenset((k * step) % n for k in range(n // step)))
    return tuple(sorted(groups, key=lambda H: (len(H), tuple(sorted(H)))))


def common_coset_subgroup_mod(supports: Mapping[Hashable, FrozenSet[int]], n: int) -> Optional[FrozenSet[int]]:
    """Return a common additive subgroup H if every support fiber is one H-coset."""
    if not supports:
        return frozenset({0})
    values = tuple(supports.values())
    for H in additive_subgroups_mod(n):
        if all(S and frozenset((base + h) % n for h in H) == S
               for S in values for base in (next(iter(S)),)):
            return H
    return None


def translation_defect_hom_mod(domain_modulus: int, kernel: Sequence[int],
                               target_fn: Callable[[int], int], target_modulus: int):
    """Return phi(k)=t(x+k)-t(x) when every kernel derivative is basepoint-independent."""
    if domain_modulus <= 0 or target_modulus <= 0:
        raise ValueError("moduli must be positive")
    K = tuple(sorted({k % domain_modulus for k in kernel}))
    if 0 not in K:
        raise ValueError("kernel must contain zero")
    # Require additive subgroup closure.
    if any((a + b) % domain_modulus not in K for a in K for b in K):
        raise ValueError("kernel must be an additive subgroup")
    phi = {}
    for k in K:
        values = {(target_fn((x + k) % domain_modulus) - target_fn(x)) % target_modulus
                  for x in range(domain_modulus)}
        if len(values) != 1:
            return None
        phi[k] = next(iter(values))
    # Mechanical homomorphism check.
    if any(phi[(a + b) % domain_modulus] != (phi[a] + phi[b]) % target_modulus
           for a in K for b in K):
        raise AssertionError("basepoint-independent derivatives must form a homomorphism")
    return phi
