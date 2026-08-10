"""Relation-coordinate compiler for a structured class of coupled futures.

State space: (Z/p^K Z)^d with componentwise translations.
Relation coordinate:

    R_c(x) = sum_i c_i x_i mod p^K.

If the declared observable is the capped valuation of R_c, every joint action a
induces the one-dimensional translation R_c(a), because

    R_c(x+a) = R_c(x) + R_c(a).

Hence the complete coupled future signature factors exactly through the relation
coordinate and the induced one-axis translation language.  The p-adic trie
compiler may then compile the relation state directly.

When at least one coefficient is a p-adic unit, R_c is surjective onto Z/p^K Z,
so the minimum number of safe classes on the original product state is exactly
the one-axis relation-trie class count.

This is a consumer/specialization of P023 factorization, P024 action-language
precision and A3 relation-state ideas.  It is not a new generic relation theorem.
"""
from __future__ import annotations

from collections.abc import Sequence

from enterprise_math.precision_translation_trie_compiler import (
    TrieToken,
    compile_translation_trie_state,
    translation_trie_class_count,
)
from enterprise_math.precision_valuation_repair import capped_p_valuation

State = tuple[int, ...]
Action = tuple[int, ...]


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


def _coefficients(coefficients: Sequence[int]) -> tuple[int, ...]:
    row = tuple(coefficients)
    if not row:
        raise ValueError("at least one relation coefficient is required")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in row):
        raise ValueError("relation coefficients must be integers")
    return row


def _vector(values: Sequence[int], width: int, name: str) -> tuple[int, ...]:
    row = tuple(values)
    if len(row) != width:
        raise ValueError(f"{name} must match relation arity")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in row):
        raise ValueError(f"{name} entries must be integers")
    return row


def relation_value(
    state: Sequence[int], coefficients: Sequence[int], prime: int, cap: int
) -> int:
    _prime(prime)
    _cap(cap)
    coeffs = _coefficients(coefficients)
    point = _vector(state, len(coeffs), "state")
    modulus = prime**cap
    return sum(coefficient * value for coefficient, value in zip(coeffs, point)) % modulus


def relation_is_surjective(coefficients: Sequence[int], prime: int) -> bool:
    """For a p-power modulus, one p-unit coefficient makes the linear form onto."""
    _prime(prime)
    coeffs = _coefficients(coefficients)
    return any(coefficient % prime != 0 for coefficient in coeffs)


def induced_relation_translations(
    actions: Sequence[Sequence[int]],
    coefficients: Sequence[int],
    prime: int,
    cap: int,
) -> tuple[int, ...]:
    _prime(prime)
    _cap(cap)
    coeffs = _coefficients(coefficients)
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    induced = {
        relation_value(action, coeffs, prime, cap)
        for action in language
    }
    return tuple(sorted(induced))


def relation_future_signature(
    state: Sequence[int],
    actions: Sequence[Sequence[int]],
    coefficients: Sequence[int],
    prime: int,
    cap: int,
) -> tuple[int, ...]:
    """Literal coupled future signature on the original product state."""
    _prime(prime)
    _cap(cap)
    coeffs = _coefficients(coefficients)
    point = _vector(state, len(coeffs), "state")
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    modulus = prime**cap
    output = []
    for action in language:
        move = _vector(action, len(coeffs), "action")
        shifted = tuple((x + a) % modulus for x, a in zip(point, move))
        output.append(capped_p_valuation(relation_value(shifted, coeffs, prime, cap), prime, cap))
    return tuple(output)


def compile_relation_future_state(
    state: Sequence[int],
    actions: Sequence[Sequence[int]],
    coefficients: Sequence[int],
    prime: int,
    cap: int,
) -> TrieToken:
    """Compile a coupled product state through its sufficient relation coordinate."""
    coeffs = _coefficients(coefficients)
    point = _vector(state, len(coeffs), "state")
    relation = relation_value(point, coeffs, prime, cap)
    induced = induced_relation_translations(actions, coeffs, prime, cap)
    return compile_translation_trie_state(relation, induced, prime, cap)


def relation_compiled_class_count(
    actions: Sequence[Sequence[int]],
    coefficients: Sequence[int],
    prime: int,
    cap: int,
) -> int:
    """Exact product-state class count when the relation map is surjective."""
    if not relation_is_surjective(coefficients, prime):
        raise ValueError("exact class-count formula requires a p-unit coefficient")
    induced = induced_relation_translations(actions, coefficients, prime, cap)
    return translation_trie_class_count(induced, prime, cap)


def relation_compiler_partition_is_exact(
    actions: Sequence[Sequence[int]],
    coefficients: Sequence[int],
    prime: int,
    cap: int,
) -> bool:
    """Bounded oracle: relation token equality iff literal future signature equality."""
    _prime(prime)
    _cap(cap)
    coeffs = _coefficients(coefficients)
    if not relation_is_surjective(coeffs, prime):
        raise ValueError("oracle currently requires a surjective relation coordinate")
    modulus = prime**cap
    width = len(coeffs)
    token_groups: dict[TrieToken, set[State]] = {}
    signature_groups: dict[tuple[int, ...], set[State]] = {}

    def visit(prefix: tuple[int, ...]) -> None:
        if len(prefix) == width:
            token_groups.setdefault(
                compile_relation_future_state(prefix, actions, coeffs, prime, cap), set()
            ).add(prefix)
            signature_groups.setdefault(
                relation_future_signature(prefix, actions, coeffs, prime, cap), set()
            ).add(prefix)
            return
        for value in range(modulus):
            visit((*prefix, value))

    visit(())
    return {frozenset(group) for group in token_groups.values()} == {
        frozenset(group) for group in signature_groups.values()
    }
