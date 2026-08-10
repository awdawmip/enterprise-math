"""Exact CRT compiler for arbitrary correlated translation languages.

Let X=Z/MZ with M=prod p_i^K_i and observe the full vector of capped p_i-adic
valuations.  Let T be any nonempty finite set of translations modulo M; T need
not be a Cartesian product of its prime-power projections.

Because translation and observation act componentwise under CRT, equality of
the complete future observable vectors for all t in T is equivalent to equality
of each component future signature for every translation appearing in that
component projection.  Therefore action-label correlation does not change the
coarsest safe quotient:

    ker Sigma_T = product_i ker Sigma_(proj_i T).

Each marginal kernel is compiled by the one-axis p-adic translation trie.  The
joint class count is therefore the product of the marginal trie class counts.

This is an elementary product-signature specialization of P023/P024, not a new
generic product theorem.
"""
from __future__ import annotations

from collections.abc import Sequence
from math import prod

from enterprise_math.precision_translation_trie_compiler import (
    TrieToken,
    compile_translation_trie_state,
    translation_trie_class_count,
)
from enterprise_math.precision_valuation_repair import capped_p_valuation

PrimeComponent = tuple[int, int]
CRTToken = tuple[TrieToken, ...]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be prime")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1


def _components(components: Sequence[PrimeComponent]) -> tuple[PrimeComponent, ...]:
    row = tuple(components)
    if not row:
        raise ValueError("at least one prime-power component is required")
    seen: set[int] = set()
    for prime, cap in row:
        _prime(prime)
        if isinstance(cap, bool) or not isinstance(cap, int) or cap <= 0:
            raise ValueError("caps must be positive integers")
        if prime in seen:
            raise ValueError("prime components must be distinct")
        seen.add(prime)
    return row


def crt_modulus(components: Sequence[PrimeComponent]) -> int:
    return prod(prime**cap for prime, cap in _components(components))


def _translations(
    translations: Sequence[int], components: Sequence[PrimeComponent]
) -> tuple[int, ...]:
    row = tuple(translations)
    if not row:
        raise ValueError("translation language must be nonempty")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in row):
        raise ValueError("translations must be integers")
    modulus = crt_modulus(components)
    return tuple(sorted({value % modulus for value in row}))


def projected_translation_language(
    translations: Sequence[int],
    components: Sequence[PrimeComponent],
    component_index: int,
) -> tuple[int, ...]:
    row = _components(components)
    if (
        isinstance(component_index, bool)
        or not isinstance(component_index, int)
        or not 0 <= component_index < len(row)
    ):
        raise ValueError("component_index outside component list")
    language = _translations(translations, row)
    prime, cap = row[component_index]
    modulus = prime**cap
    return tuple(sorted({value % modulus for value in language}))


def compile_correlated_crt_translation_state(
    residue: int,
    translations: Sequence[int],
    components: Sequence[PrimeComponent],
) -> CRTToken:
    row = _components(components)
    language = _translations(translations, row)
    modulus = crt_modulus(row)
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    tokens: list[TrieToken] = []
    for index, (prime, cap) in enumerate(row):
        marginal = projected_translation_language(language, row, index)
        tokens.append(
            compile_translation_trie_state(
                value % (prime**cap), marginal, prime, cap
            )
        )
    return tuple(tokens)


def correlated_crt_class_count(
    translations: Sequence[int], components: Sequence[PrimeComponent]
) -> int:
    row = _components(components)
    language = _translations(translations, row)
    counts = []
    for index, (prime, cap) in enumerate(row):
        marginal = projected_translation_language(language, row, index)
        counts.append(translation_trie_class_count(marginal, prime, cap))
    return prod(counts)


def correlated_crt_future_signature(
    residue: int,
    translations: Sequence[int],
    components: Sequence[PrimeComponent],
) -> tuple[tuple[int, ...], ...]:
    row = _components(components)
    language = _translations(translations, row)
    modulus = crt_modulus(row)
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    return tuple(
        tuple(
            capped_p_valuation(
                (value + translation) % (prime**cap), prime, cap
            )
            for prime, cap in row
        )
        for translation in language
    )


def correlated_crt_partition_is_exact(
    translations: Sequence[int], components: Sequence[PrimeComponent]
) -> bool:
    """Finite oracle for arbitrary correlated T under full vector observation."""
    row = _components(components)
    language = _translations(translations, row)
    modulus = crt_modulus(row)
    token_groups: dict[CRTToken, set[int]] = {}
    signature_groups: dict[tuple[tuple[int, ...], ...], set[int]] = {}
    for residue in range(modulus):
        token_groups.setdefault(
            compile_correlated_crt_translation_state(residue, language, row), set()
        ).add(residue)
        signature_groups.setdefault(
            correlated_crt_future_signature(residue, language, row), set()
        ).add(residue)
    return {frozenset(group) for group in token_groups.values()} == {
        frozenset(group) for group in signature_groups.values()
    }
