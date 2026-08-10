"""Finite projective checks for the R004 counterfactual-master no-go.

The infinite-horizon object itself is intentionally not simulated here.  This
module verifies the finite consistency hypotheses used by the standard inverse-
limit / Kolmogorov extension argument:

* deterministic support-master families truncate onto shallower families;
* rational master measures push forward exactly under tree truncation.

That separation matters.  Executable finite checks establish the projective
system; standard measure theory supplies the infinite-tree measure.  Neither is
a physical hidden-variable proposal.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Mapping
from fractions import Fraction

from .r004_causal_identifiability_completion import (
    Action,
    CounterfactualMaster,
    Relation,
    State,
    compile_rational_master_measure,
    compile_support_masters,
)


def truncate_master(master: CounterfactualMaster, depth: int) -> CounterfactualMaster:
    """Restrict a finite counterfactual master to its first ``depth`` levels."""
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    if depth > master.depth:
        raise ValueError("cannot extend a master by truncation")
    if depth == 0:
        return CounterfactualMaster(state=master.state, depth=0, branches=())

    branches: list[tuple[Action, CounterfactualMaster | None]] = []
    for action, child in master.branches:
        branches.append(
            (
                action,
                None if child is None else truncate_master(child, depth - 1),
            )
        )
    return CounterfactualMaster(
        state=master.state,
        depth=depth,
        branches=tuple(branches),
    )


def truncate_master_family(
    masters: Iterable[CounterfactualMaster], depth: int
) -> frozenset[CounterfactualMaster]:
    """Set-valued pushforward of a deterministic master family by truncation."""
    family = tuple(masters)
    if not family:
        raise ValueError("master family must be nonempty")
    return frozenset(truncate_master(master, depth) for master in family)


def truncate_master_measure(
    master_measure: Mapping[CounterfactualMaster, Fraction],
    depth: int,
) -> dict[CounterfactualMaster, Fraction]:
    """Exact pushforward of a rational finite master measure by truncation."""
    if not master_measure:
        raise ValueError("master measure must be nonempty")
    result: defaultdict[CounterfactualMaster, Fraction] = defaultdict(Fraction)
    for master, raw_weight in master_measure.items():
        weight = Fraction(raw_weight)
        if weight < 0:
            raise ValueError("master weights must be nonnegative")
        result[truncate_master(master, depth)] += weight
    if sum(result.values(), Fraction(0)) != sum(
        (Fraction(weight) for weight in master_measure.values()),
        start=Fraction(0),
    ):
        raise AssertionError("truncation pushforward must preserve total mass")
    return {master: weight for master, weight in result.items() if weight}


def support_master_projective_holds(
    states: Iterable[State],
    relations: Mapping[Action, Relation],
    source: State,
    shallow_horizon: int,
    deep_horizon: int,
) -> bool:
    """Check that deep support masters truncate onto exactly the shallow family."""
    if shallow_horizon < 0 or deep_horizon < shallow_horizon:
        raise ValueError("require 0 <= shallow_horizon <= deep_horizon")
    shallow = frozenset(
        compile_support_masters(states, relations, source, shallow_horizon)
    )
    deep = compile_support_masters(states, relations, source, deep_horizon)
    return truncate_master_family(deep, shallow_horizon) == shallow


def rational_master_measure_projective_holds(
    states: Iterable[State],
    kernels: Mapping[Action, Mapping[State, Mapping[State, Fraction]]],
    source: State,
    shallow_horizon: int,
    deep_horizon: int,
) -> bool:
    """Check exact projectivity of the finite rational master measures."""
    if shallow_horizon < 0 or deep_horizon < shallow_horizon:
        raise ValueError("require 0 <= shallow_horizon <= deep_horizon")
    shallow = compile_rational_master_measure(
        states, kernels, source, shallow_horizon
    )
    deep = compile_rational_master_measure(states, kernels, source, deep_horizon)
    return truncate_master_measure(deep, shallow_horizon) == shallow
