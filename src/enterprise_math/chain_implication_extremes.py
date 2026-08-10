"""Exact storage/depth endpoints for finite chain closure laws.

For x_0 => x_1 => ... => x_n under single-head implications:

* the unique minimum-rule complete basis is the adjacent/Hasse basis, with n
  rules and worst-case parallel depth n;
* the unique inclusion-minimal one-round complete basis is the full rooted
  circuit table, with binom(n+1,2) rules and depth one.

The underlying graph/Horn facts are classical; this module packages the exact
resource endpoints for P025 precision accounting.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Hashable, Iterable

from .closure_implication_bases import (
    basis_report,
    chain_adjacent_basis,
    chain_closure_states,
    chain_full_circuit_basis,
)

Label = Hashable


@dataclass(frozen=True)
class ChainBasisExtremes:
    label_count: int
    minimum_rule_count: int
    minimum_rule_depth: int
    one_round_rule_count: int
    one_round_depth: int
    adjacent_complete: bool
    full_complete: bool


def chain_basis_extremes(labels: Iterable[Label]) -> ChainBasisExtremes:
    labels = tuple(labels)
    if not labels:
        raise ValueError("chain must contain at least one label")
    states = chain_closure_states(labels)
    adjacent = chain_adjacent_basis(labels)
    full = chain_full_circuit_basis(labels)
    adjacent_report = basis_report(labels, states, adjacent)
    full_report = basis_report(labels, states, full)
    n = len(labels) - 1
    if adjacent_report.rule_count != n or adjacent_report.worst_case_rounds != n:
        raise AssertionError("adjacent basis must realize the minimum-storage chain endpoint")
    if full_report.rule_count != comb(n + 1, 2) or full_report.worst_case_rounds != (0 if n == 0 else 1):
        raise AssertionError("full circuit table must realize the one-round chain endpoint")
    return ChainBasisExtremes(
        label_count=len(labels),
        minimum_rule_count=n,
        minimum_rule_depth=n,
        one_round_rule_count=comb(n + 1, 2),
        one_round_depth=0 if n == 0 else 1,
        adjacent_complete=adjacent_report.complete,
        full_complete=full_report.complete,
    )
