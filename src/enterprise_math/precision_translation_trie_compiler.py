"""Exact p-adic trie compiler for arbitrary finite translation languages.

Let the finite state space be Z/p^K Z and observe capped p-adic valuation after
translations from a nonempty finite set T.  Write C=-T for the corresponding
centers.  The future signature of x is the vector of capped valuations
v_p(x-c), c in C.

Read residues in p-adic digit order (least significant digit first).  The center
set defines an occupied prefix trie.  The coarsest future-safe representation
has two token types:

* a center token when x itself is one of the centers;
* an exit token for the deepest occupied prefix followed by x before x enters
  an unoccupied child branch.

All residues exiting through the same occupied parent have exactly the same
future signature.  Distinct center/exit tokens are future-distinguishable.
Therefore the exact class count is

    number of centers
    + number of occupied trie nodes (depth < K) having at least one empty child.

The subgroup compiler s+p^(K-s) is the special case where the center set is the
subgroup p^s Z/p^K Z.

p-adic valuations, finite prefix tries and generic future-safe quotient theory
are prior mathematics.  This module is an R004/P024 arithmetic specialization.
"""
from __future__ import annotations

from collections.abc import Sequence

from enterprise_math.precision_valuation_repair import capped_p_valuation

TrieToken = tuple[str, int, int]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be prime")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1


def _cap(cap: int) -> None:
    if isinstance(cap, bool) or not isinstance(cap, int) or cap <= 0:
        raise ValueError("cap must be positive")


def _translations(translations: Sequence[int], prime: int, cap: int) -> tuple[int, ...]:
    _prime(prime)
    _cap(cap)
    row = tuple(translations)
    if not row:
        raise ValueError("translation language must be nonempty")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in row):
        raise ValueError("translations must be integers")
    modulus = prime**cap
    return tuple(sorted({value % modulus for value in row}))


def translation_centers(
    translations: Sequence[int], prime: int, cap: int
) -> tuple[int, ...]:
    """Return sorted centers C=-T modulo p^K."""
    row = _translations(translations, prime, cap)
    modulus = prime**cap
    return tuple(sorted({(-value) % modulus for value in row}))


def occupied_prefixes(
    translations: Sequence[int], prime: int, cap: int, depth: int
) -> frozenset[int]:
    """Occupied low-digit prefixes modulo p^depth; depth zero has root {0}."""
    centers = translation_centers(translations, prime, cap)
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= cap:
        raise ValueError("depth must lie in 0..cap")
    if depth == 0:
        return frozenset({0})
    modulus = prime**depth
    return frozenset(center % modulus for center in centers)


def trie_deficit_node_count(
    translations: Sequence[int], prime: int, cap: int
) -> int:
    """Count occupied prefix nodes with at least one unoccupied child."""
    _prime(prime)
    _cap(cap)
    translation_centers(translations, prime, cap)
    deficit = 0
    for depth in range(cap):
        parents = occupied_prefixes(translations, prime, cap, depth)
        children = occupied_prefixes(translations, prime, cap, depth + 1)
        step = prime**depth
        child_modulus = prime ** (depth + 1)
        for parent in parents:
            occupied_children = sum(
                ((parent + digit * step) % child_modulus) in children
                for digit in range(prime)
            )
            if occupied_children < prime:
                deficit += 1
    return deficit


def translation_trie_class_count(
    translations: Sequence[int], prime: int, cap: int
) -> int:
    centers = translation_centers(translations, prime, cap)
    return len(centers) + trie_deficit_node_count(translations, prime, cap)


def compile_translation_trie_state(
    residue: int,
    translations: Sequence[int],
    prime: int,
    cap: int,
) -> TrieToken:
    """Compile one residue to its minimal center/exit token."""
    _prime(prime)
    _cap(cap)
    centers = set(translation_centers(translations, prime, cap))
    modulus = prime**cap
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    if value in centers:
        return "center", cap, value

    # Find the deepest low-digit prefix still occupied by at least one center.
    # At the next digit the state exits the center trie.
    for depth in range(cap - 1, -1, -1):
        prefix_modulus = prime**depth
        prefix = value % prefix_modulus if depth else 0
        occupied = occupied_prefixes(translations, prime, cap, depth)
        if prefix in occupied:
            return "exit", depth, prefix
    raise AssertionError("the root prefix must always be occupied")


def translation_future_signature(
    residue: int,
    translations: Sequence[int],
    prime: int,
    cap: int,
) -> tuple[int, ...]:
    """Exact capped-valuation outputs for every distinct declared translation."""
    row = _translations(translations, prime, cap)
    modulus = prime**cap
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    return tuple(
        capped_p_valuation((value + translation) % modulus, prime, cap)
        for translation in row
    )


def translation_trie_partition_is_exact(
    translations: Sequence[int], prime: int, cap: int
) -> bool:
    """Finite oracle: token equality iff full translation signature equality."""
    row = _translations(translations, prime, cap)
    modulus = prime**cap
    token_groups: dict[TrieToken, set[int]] = {}
    signature_groups: dict[tuple[int, ...], set[int]] = {}
    for residue in range(modulus):
        token_groups.setdefault(
            compile_translation_trie_state(residue, row, prime, cap), set()
        ).add(residue)
        signature_groups.setdefault(
            translation_future_signature(residue, row, prime, cap), set()
        ).add(residue)
    return {frozenset(group) for group in token_groups.values()} == {
        frozenset(group) for group in signature_groups.values()
    }


def subgroup_translation_language(
    prime: int, cap: int, subgroup_level: int
) -> tuple[int, ...]:
    """Return H_s=p^s Z/p^K Z as an explicit bounded translation language."""
    _prime(prime)
    _cap(cap)
    if (
        isinstance(subgroup_level, bool)
        or not isinstance(subgroup_level, int)
        or not 0 <= subgroup_level <= cap
    ):
        raise ValueError("subgroup_level must lie in 0..cap")
    step = prime**subgroup_level
    return tuple(step * offset for offset in range(prime ** (cap - subgroup_level)))


def subgroup_trie_class_count(prime: int, cap: int, subgroup_level: int) -> int:
    """Trie formula specialized to H_s, returning s+p^(K-s)."""
    language = subgroup_translation_language(prime, cap, subgroup_level)
    count = translation_trie_class_count(language, prime, cap)
    expected = subgroup_level + prime ** (cap - subgroup_level)
    if count != expected:
        raise AssertionError("subgroup trie must recover the closed-form compiler count")
    return count
