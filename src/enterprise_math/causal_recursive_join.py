"""Recursive causal join on continuation types.

The primitive object is a finite nonnegative-integer join kernel

    K(alpha, beta; nu, delta)

meaning that joining one witness of continuation types alpha and beta produces
`multiplicity` joint witnesses of continuation type nu and integer grade shift
delta.  Inventories compose by explicit finite witness counting.  Ordinary
matrix/tensor/convolution notation is only a coordinate shadow of this rule.

A binary causal law is sufficient to generate arbitrary-dimensional joint
inventories without parenthesization dependence exactly when the typed kernel is
associative:

    sum_{mu,d1+d2=d} K(a,b;mu,d1) K(mu,c;nu,d2)
  = sum_{mu,d1+d2=d} K(b,c;mu,d1) K(a,mu;nu,d2)

for every exact typed outcome.  When this fails, the left-only/right-only
positive defects are an irreducible three-body compatibility defect relative to
the declared continuation-type language.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

ContinuationType = Hashable
Inventory = dict[tuple[ContinuationType, int], int]
JoinKernel = dict[tuple[ContinuationType, ContinuationType, ContinuationType, int], int]
Outcome = tuple[ContinuationType, int]


def _validate_inventory(inventory: Inventory) -> None:
    if not isinstance(inventory, dict):
        raise ValueError("inventory must be a dict")
    for (tau, grade), count in inventory.items():
        try:
            hash(tau)
        except TypeError as error:
            raise ValueError("continuation types must be hashable") from error
        if isinstance(grade, bool) or not isinstance(grade, int):
            raise ValueError("grades must be integers")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("inventory counts must be non-negative integers")


def _validate_kernel(kernel: JoinKernel) -> None:
    if not isinstance(kernel, dict):
        raise ValueError("kernel must be a dict")
    for (left, right, out, shift), count in kernel.items():
        for tau in (left, right, out):
            try:
                hash(tau)
            except TypeError as error:
                raise ValueError("continuation types must be hashable") from error
        if isinstance(shift, bool) or not isinstance(shift, int):
            raise ValueError("grade shifts must be integers")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("join multiplicities must be non-negative integers")


def singleton_inventory(tau: ContinuationType, grade: int = 0) -> Inventory:
    if isinstance(grade, bool) or not isinstance(grade, int):
        raise ValueError("grade must be an integer")
    return {(tau, grade): 1}


def compose_inventories(
    left: Inventory,
    right: Inventory,
    kernel: JoinKernel,
) -> Inventory:
    """Exact inventory composition under a typed causal join kernel."""
    _validate_inventory(left)
    _validate_inventory(right)
    _validate_kernel(kernel)
    result: dict[Outcome, int] = defaultdict(int)
    rules_by_inputs: dict[tuple[ContinuationType, ContinuationType], list[tuple[ContinuationType, int, int]]] = defaultdict(list)
    for (left_tau, right_tau, out_tau, shift), multiplicity in kernel.items():
        if multiplicity:
            rules_by_inputs[(left_tau, right_tau)].append((out_tau, shift, multiplicity))

    for (left_tau, left_grade), left_count in left.items():
        if not left_count:
            continue
        for (right_tau, right_grade), right_count in right.items():
            if not right_count:
                continue
            for out_tau, shift, rule_count in rules_by_inputs.get((left_tau, right_tau), ()):
                result[(out_tau, left_grade + right_grade + shift)] += (
                    left_count * right_count * rule_count
                )
    return dict(result)


def three_way_left(
    first: ContinuationType,
    second: ContinuationType,
    third: ContinuationType,
    kernel: JoinKernel,
) -> Inventory:
    return compose_inventories(
        compose_inventories(singleton_inventory(first), singleton_inventory(second), kernel),
        singleton_inventory(third),
        kernel,
    )


def three_way_right(
    first: ContinuationType,
    second: ContinuationType,
    third: ContinuationType,
    kernel: JoinKernel,
) -> Inventory:
    return compose_inventories(
        singleton_inventory(first),
        compose_inventories(singleton_inventory(second), singleton_inventory(third), kernel),
        kernel,
    )


def typed_associativity_defect(
    types: tuple[ContinuationType, ...],
    kernel: JoinKernel,
) -> dict[tuple[ContinuationType, ContinuationType, ContinuationType], tuple[dict[Outcome, int], dict[Outcome, int]]]:
    """Return positive left-only/right-only defects for every input triple.

    Signed differences are intentionally not summed: missing left outcomes and
    missing right outcomes are causally different failures and may numerically
    cancel in a scalar summary.
    """
    if not isinstance(types, tuple) or not types or len(set(types)) != len(types):
        raise ValueError("types must be a non-empty tuple of unique labels")
    _validate_kernel(kernel)
    result = {}
    for first in types:
        for second in types:
            for third in types:
                left = three_way_left(first, second, third, kernel)
                right = three_way_right(first, second, third, kernel)
                outcomes = set(left) | set(right)
                left_only = {
                    outcome: left.get(outcome, 0) - right.get(outcome, 0)
                    for outcome in outcomes
                    if left.get(outcome, 0) > right.get(outcome, 0)
                }
                right_only = {
                    outcome: right.get(outcome, 0) - left.get(outcome, 0)
                    for outcome in outcomes
                    if right.get(outcome, 0) > left.get(outcome, 0)
                }
                if left_only or right_only:
                    result[(first, second, third)] = (left_only, right_only)
    return result


def kernel_is_associative(
    types: tuple[ContinuationType, ...],
    kernel: JoinKernel,
) -> bool:
    return not typed_associativity_defect(types, kernel)


def unit_type_is_exact(
    unit: ContinuationType,
    types: tuple[ContinuationType, ...],
    kernel: JoinKernel,
) -> bool:
    """Whether `unit` joins uniquely with zero grade shift on either side."""
    _validate_kernel(kernel)
    for tau in types:
        left_rules = {
            (out, shift): count
            for (a, b, out, shift), count in kernel.items()
            if a == unit and b == tau and count
        }
        right_rules = {
            (out, shift): count
            for (a, b, out, shift), count in kernel.items()
            if a == tau and b == unit and count
        }
        if left_rules != {(tau, 0): 1} or right_rules != {(tau, 0): 1}:
            return False
    return True


def deterministic_join_kernel(
    types: tuple[ContinuationType, ...],
    operation: dict[tuple[ContinuationType, ContinuationType], ContinuationType],
) -> JoinKernel:
    """Build a zero-grade multiplicity-one kernel from a total binary type law."""
    expected = {(left, right) for left in types for right in types}
    if set(operation) != expected:
        raise ValueError("operation must define every ordered type pair")
    if not set(operation.values()) <= set(types):
        raise ValueError("operation outputs must be declared types")
    return {
        (left, right, operation[(left, right)], 0): 1
        for left in types
        for right in types
    }


def xor_parity_kernel() -> JoinKernel:
    """Two continuation types that retain only accumulated parity."""
    types = (0, 1)
    return deterministic_join_kernel(
        types,
        {(left, right): left ^ right for left in types for right in types},
    )


def fold_inventory(
    factors: tuple[Inventory, ...],
    kernel: JoinKernel,
) -> Inventory:
    """Left fold; parenthesization is irrelevant when the kernel is associative."""
    if not isinstance(factors, tuple) or not factors:
        raise ValueError("factors must be a non-empty tuple")
    current = factors[0]
    for factor in factors[1:]:
        current = compose_inventories(current, factor, kernel)
    return current
