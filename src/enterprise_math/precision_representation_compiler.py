"""Closed-form operation-conditioned representation compiler for R004.

This module is an R004 specialization of the canonical P023/P024 principle:
a representation is legal only when the declared future observation/action
language descends through it.  The state space here is finite arithmetic.

For one p-power component Z/p^K Z, the observable is the capped valuation
q_K(x)=min(v_p(x),K).  The allowed future translations are the subgroup
H_s=p^s Z/p^K Z, 0<=s<=K.

The coarsest safe representation is explicit:
- if v_p(x)<s, retain only that valuation level;
- if v_p(x)>=s, retain the exact tail x/p^s modulo p^(K-s).

Hence the exact class count is s+p^(K-s).  Writing t=K-s (translation depth)
turns this into K-t+p^t, with repair excess p^t-t-1 over the valuation-only
baseline K+1.

For a composite modulus with prime-power CRT factors, component languages and
representations factor as a Cartesian product.  The corresponding class count
is the product of the one-prime counts.

The generic quotient theorem, p-adic valuation, finite cyclic groups and CRT are
prior mathematics.  R004 contributes only this bounded closed-form compiler
specialization and its use as an operation/state-complexity pressure test.
"""
from __future__ import annotations

from collections.abc import Sequence
from math import prod

from enterprise_math.precision_valuation_repair import capped_p_valuation

PrimeComponent = tuple[int, int]  # (prime, cap)
CompiledAtom = tuple[str, int]
CompiledWord = tuple[CompiledAtom, ...]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be a prime integer")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be a prime integer")
        divisor += 1


def _cap(cap: int) -> None:
    if isinstance(cap, bool) or not isinstance(cap, int) or cap <= 0:
        raise ValueError("cap must be a positive integer")


def _subgroup_level(subgroup_level: int, cap: int) -> None:
    if (
        isinstance(subgroup_level, bool)
        or not isinstance(subgroup_level, int)
        or not 0 <= subgroup_level <= cap
    ):
        raise ValueError("subgroup_level must lie in 0..cap")


def translation_depth(cap: int, subgroup_level: int) -> int:
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    return cap - subgroup_level


def prime_translation_group_size(prime: int, cap: int, subgroup_level: int) -> int:
    """Number of allowed translations in H_s=p^s Z/p^K Z."""
    _prime(prime)
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    return prime ** translation_depth(cap, subgroup_level)


def compile_prime_translation_state(
    residue: int,
    prime: int,
    cap: int,
    subgroup_level: int,
) -> CompiledAtom:
    """Return the coarsest safe token for the subgroup-translation language.

    Token ``("v",a)`` means only capped valuation level a is retained.
    Token ``("r",u)`` means the state lies in H_s and the exact subgroup tail
    u=x/p^s mod p^(K-s) is retained.
    """
    _prime(prime)
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    modulus = prime**cap
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    level = capped_p_valuation(value, prime, cap)
    if level < subgroup_level:
        return "v", level
    tail_modulus = prime ** (cap - subgroup_level)
    return "r", (value // (prime**subgroup_level)) % tail_modulus


def prime_compiled_class_count(prime: int, cap: int, subgroup_level: int) -> int:
    """Exact minimum class count s+p^(K-s)."""
    _prime(prime)
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    return subgroup_level + prime ** (cap - subgroup_level)


def prime_compiled_class_count_by_depth(prime: int, cap: int, depth: int) -> int:
    _prime(prime)
    _cap(cap)
    if isinstance(depth, bool) or not isinstance(depth, int) or not 0 <= depth <= cap:
        raise ValueError("depth must lie in 0..cap")
    return cap - depth + prime**depth


def prime_repair_excess(prime: int, depth: int) -> int:
    """Extra classes over valuation-only baseline, p^t-t-1."""
    _prime(prime)
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    return prime**depth - depth - 1


def prime_incremental_repair_cost(prime: int, depth: int) -> int:
    """Additional classes when translation depth grows from t to t+1."""
    _prime(prime)
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    return (prime - 1) * prime**depth - 1


def prime_subgroup_translation_signature(
    residue: int,
    prime: int,
    cap: int,
    subgroup_level: int,
) -> tuple[int, ...]:
    """Executable oracle: all capped-valuation outputs under H_s translations."""
    _prime(prime)
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    modulus = prime**cap
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    step = prime**subgroup_level
    count = prime ** (cap - subgroup_level)
    value = residue % modulus
    return tuple(
        capped_p_valuation((value + step * offset) % modulus, prime, cap)
        for offset in range(count)
    )


def prime_compiler_partition_is_exact(prime: int, cap: int, subgroup_level: int) -> bool:
    """Check compiled-token equality iff full future-signature equality."""
    _prime(prime)
    _cap(cap)
    _subgroup_level(subgroup_level, cap)
    modulus = prime**cap
    token_groups: dict[CompiledAtom, set[int]] = {}
    signature_groups: dict[tuple[int, ...], set[int]] = {}
    for residue in range(modulus):
        token_groups.setdefault(
            compile_prime_translation_state(residue, prime, cap, subgroup_level), set()
        ).add(residue)
        signature_groups.setdefault(
            prime_subgroup_translation_signature(residue, prime, cap, subgroup_level), set()
        ).add(residue)
    return {frozenset(group) for group in token_groups.values()} == {
        frozenset(group) for group in signature_groups.values()
    }


def _components(components: Sequence[PrimeComponent]) -> tuple[PrimeComponent, ...]:
    row = tuple(components)
    if not row:
        raise ValueError("at least one prime-power component is required")
    seen: set[int] = set()
    for prime, cap in row:
        _prime(prime)
        _cap(cap)
        if prime in seen:
            raise ValueError("prime components must be distinct")
        seen.add(prime)
    return row


def composite_modulus(components: Sequence[PrimeComponent]) -> int:
    row = _components(components)
    return prod(prime**cap for prime, cap in row)


def compile_crt_translation_state(
    residue: int,
    components: Sequence[PrimeComponent],
    subgroup_levels: Sequence[int],
) -> CompiledWord:
    """Compile independent p-power subgroup-translation languages componentwise."""
    row = _components(components)
    levels = tuple(subgroup_levels)
    if len(levels) != len(row):
        raise ValueError("one subgroup level is required per prime component")
    modulus = composite_modulus(row)
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    value = residue % modulus
    output: list[CompiledAtom] = []
    for (prime, cap), subgroup_level in zip(row, levels):
        _subgroup_level(subgroup_level, cap)
        output.append(
            compile_prime_translation_state(
                value % (prime**cap), prime, cap, subgroup_level
            )
        )
    return tuple(output)


def crt_compiled_class_count(
    components: Sequence[PrimeComponent], subgroup_levels: Sequence[int]
) -> int:
    row = _components(components)
    levels = tuple(subgroup_levels)
    if len(levels) != len(row):
        raise ValueError("one subgroup level is required per prime component")
    counts = []
    for (prime, cap), subgroup_level in zip(row, levels):
        _subgroup_level(subgroup_level, cap)
        counts.append(prime_compiled_class_count(prime, cap, subgroup_level))
    return prod(counts)


def crt_translation_subgroup_step(
    components: Sequence[PrimeComponent], subgroup_levels: Sequence[int]
) -> int:
    """Return d=prod p_i^s_i whose multiples form the declared subgroup."""
    row = _components(components)
    levels = tuple(subgroup_levels)
    if len(levels) != len(row):
        raise ValueError("one subgroup level is required per prime component")
    factors = []
    for (prime, cap), subgroup_level in zip(row, levels):
        _subgroup_level(subgroup_level, cap)
        factors.append(prime**subgroup_level)
    return prod(factors)


def crt_translation_signature(
    residue: int,
    components: Sequence[PrimeComponent],
    subgroup_levels: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    """Full future signature under the composite cyclic translation subgroup."""
    row = _components(components)
    levels = tuple(subgroup_levels)
    modulus = composite_modulus(row)
    step = crt_translation_subgroup_step(row, levels)
    value = residue % modulus
    outputs: list[tuple[int, ...]] = []
    for offset in range(modulus // step):
        shifted = (value + step * offset) % modulus
        outputs.append(
            tuple(
                capped_p_valuation(shifted % (prime**cap), prime, cap)
                for prime, cap in row
            )
        )
    return tuple(outputs)


def crt_compiler_partition_is_exact(
    components: Sequence[PrimeComponent], subgroup_levels: Sequence[int]
) -> bool:
    """Finite oracle for the CRT product compiler theorem."""
    row = _components(components)
    modulus = composite_modulus(row)
    tokens: dict[CompiledWord, set[int]] = {}
    signatures: dict[tuple[tuple[int, ...], ...], set[int]] = {}
    for residue in range(modulus):
        tokens.setdefault(
            compile_crt_translation_state(residue, row, subgroup_levels), set()
        ).add(residue)
        signatures.setdefault(
            crt_translation_signature(residue, row, subgroup_levels), set()
        ).add(residue)
    return {frozenset(group) for group in tokens.values()} == {
        frozenset(group) for group in signatures.values()
    }
