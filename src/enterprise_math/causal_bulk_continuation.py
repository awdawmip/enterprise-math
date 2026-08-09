"""Bulk + structural-continuation causal state for repeated LEGO growth.

The runtime state is deliberately split:

    (bulk_value, continuation_type)

`bulk_value` stores already-settled value/grade under a declared causal
composition law.  `continuation_type` stores only the minimum structural detail
needed for future updates.  Adding one local symbol performs

    tau'  = next_type(tau, symbol)
    bulk' = combine_bulk(bulk, increment(tau, symbol))

This one schema covers pure accumulators, residue+carry, finite-range grades,
close-packed relative stacking, and saturating bulk laws.  Traditional weighted
automata/transducers/skew-product terminology may describe special coordinate
forms but is not the ontology.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Hashable, TypeVar

Bulk = TypeVar("Bulk")
Tau = TypeVar("Tau", bound=Hashable)
Symbol = TypeVar("Symbol", bound=Hashable)
Increment = TypeVar("Increment")


@dataclass(frozen=True)
class BulkContinuationState(Generic[Bulk, Tau]):
    bulk: Bulk
    continuation: Tau


@dataclass(frozen=True)
class BulkContinuationLaw(Generic[Bulk, Tau, Symbol, Increment]):
    symbols: tuple[Symbol, ...]
    types: tuple[Tau, ...]
    next_type: dict[tuple[Tau, Symbol], Tau]
    increment: dict[tuple[Tau, Symbol], Increment]
    combine_bulk: Callable[[Bulk, Increment], Bulk]

    def __post_init__(self) -> None:
        if not self.symbols or len(set(self.symbols)) != len(self.symbols):
            raise ValueError("symbols must be a non-empty tuple of unique labels")
        if not self.types or len(set(self.types)) != len(self.types):
            raise ValueError("types must be a non-empty tuple of unique labels")
        expected = {(tau, symbol) for tau in self.types for symbol in self.symbols}
        if set(self.next_type) != expected or set(self.increment) != expected:
            raise ValueError("next_type and increment must define every type-symbol pair")
        if not set(self.next_type.values()) <= set(self.types):
            raise ValueError("next_type outputs must be declared continuation types")


def step(
    state: BulkContinuationState[Bulk, Tau],
    symbol: Symbol,
    law: BulkContinuationLaw[Bulk, Tau, Symbol, Increment],
) -> BulkContinuationState[Bulk, Tau]:
    if symbol not in law.symbols:
        raise ValueError("symbol is not declared by the causal law")
    key = (state.continuation, symbol)
    if key not in law.next_type:
        raise ValueError("state continuation type is not declared by the causal law")
    return BulkContinuationState(
        bulk=law.combine_bulk(state.bulk, law.increment[key]),
        continuation=law.next_type[key],
    )


def run(
    initial: BulkContinuationState[Bulk, Tau],
    word: tuple[Symbol, ...],
    law: BulkContinuationLaw[Bulk, Tau, Symbol, Increment],
) -> BulkContinuationState[Bulk, Tau]:
    if not isinstance(word, tuple):
        raise ValueError("word must be a tuple")
    state = initial
    for symbol in word:
        state = step(state, symbol, law)
    return state


def singleton_accumulator_law(
    symbols: tuple[int, ...],
) -> BulkContinuationLaw[int, str, int, int]:
    """Pure integer sum: one structural type, symbol itself is the bulk increment."""
    tau = "unit"
    return BulkContinuationLaw(
        symbols=symbols,
        types=(tau,),
        next_type={(tau, symbol): tau for symbol in symbols},
        increment={(tau, symbol): symbol for symbol in symbols},
        combine_bulk=lambda bulk, inc: bulk + inc,
    )


def base_carry_continuation_law(
    base: int,
) -> BulkContinuationLaw[int, int, int, int]:
    """Residue structural type + accumulated carry bulk for digit summation."""
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer at least two")
    symbols = tuple(range(base))
    types = tuple(range(base))
    return BulkContinuationLaw(
        symbols=symbols,
        types=types,
        next_type={
            (residue, digit): (residue + digit) % base
            for residue in types
            for digit in symbols
        },
        increment={
            (residue, digit): (residue + digit) // base
            for residue in types
            for digit in symbols
        },
        combine_bulk=lambda carry, increment: carry + increment,
    )


def exact_sum_from_carry_state(
    state: BulkContinuationState[int, int],
    base: int,
) -> int:
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer at least two")
    return state.continuation + base * state.bulk
