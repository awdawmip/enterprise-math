"""Rooted-circuit premise explosion in a balanced binary Horn AND tree.

For one internal node, a rooted-circuit premise is an inclusion-minimal seed set
not containing the node that derives it under the local Horn closure.

Let A_h(z) count minimal ways to make a node of height h available, allowing the
node itself as a one-atom seed. Then

    A_0(z)=z,
    A_h(z)=z+A_(h-1)(z)^2.

The rooted-circuit premise polynomial for the height-h root excludes the direct
root seed:

    P_h(z)=A_(h-1)(z)^2=A_h(z)-z.

Coefficient [z^m]P_h counts inclusion-minimal root premises of width m. At z=1,
with M_h=P_h(1):

    M_1=1,
    M_h=(1+M_(h-1))^2.

The circuit count is exponential in the number of leaves while the local Horn
basis has only 2^h-1 rules.  The polynomial derivative at z=1 gives total premise
literal storage.

This v2 replay corrects an earlier WIP's hand-copied P_3 histogram and consequent
premise-literal totals; the recurrence and circuit-count theorem were unchanged.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

from .stage131_horn_hyperedge_presentation import AndTree, balanced_binary_and_tree, horn_closure

Polynomial = dict[int, int]


def polynomial_add(left: Mapping[int, int], right: Mapping[int, int]) -> Polynomial:
    result: Polynomial = dict(left)
    for degree, coefficient in right.items():
        result[degree] = result.get(degree, 0) + coefficient
        if result[degree] == 0:
            del result[degree]
    return result


def polynomial_multiply(left: Mapping[int, int], right: Mapping[int, int]) -> Polynomial:
    result: Polynomial = {}
    for ld, lc in left.items():
        for rd, rc in right.items():
            result[ld + rd] = result.get(ld + rd, 0) + lc * rc
    return result


def availability_premise_polynomial(height: int) -> Polynomial:
    if isinstance(height, bool) or not isinstance(height, int) or height < 0:
        raise ValueError("height must be a nonnegative integer")
    current: Polynomial = {1: 1}
    for _ in range(height):
        current = polynomial_add({1: 1}, polynomial_multiply(current, current))
    return current


def rooted_circuit_width_polynomial(height: int) -> Polynomial:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    child = availability_premise_polynomial(height - 1)
    return polynomial_multiply(child, child)


def rooted_circuit_count(height: int) -> int:
    return sum(rooted_circuit_width_polynomial(height).values())


def rooted_circuit_count_recurrence(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    count = 1
    for _ in range(2, height + 1):
        count = (1 + count) ** 2
    return count


def rooted_circuit_total_premise_literals(height: int) -> int:
    return sum(width * count for width, count in rooted_circuit_width_polynomial(height).items())


def rooted_circuit_average_premise_width(height: int) -> Fraction:
    return Fraction(rooted_circuit_total_premise_literals(height), rooted_circuit_count(height))


def rooted_circuit_min_width(height: int) -> int:
    return min(rooted_circuit_width_polynomial(height))


def rooted_circuit_max_width(height: int) -> int:
    return max(rooted_circuit_width_polynomial(height))


def rooted_circuit_count_lower_bound(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height < 2:
        raise ValueError("lower-bound formula is stated for height>=2")
    return 1 << (1 << (height - 1))


def rooted_circuit_count_upper_bound(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be positive")
    return 1 << ((1 << height) - 1)


def total_internal_rooted_circuit_rule_count(tree_height: int) -> int:
    if isinstance(tree_height, bool) or not isinstance(tree_height, int) or tree_height <= 0:
        raise ValueError("tree_height must be positive")
    return sum(
        (1 << (tree_height - node_height)) * rooted_circuit_count(node_height)
        for node_height in range(1, tree_height + 1)
    )


def local_horn_basis_rule_count(tree_height: int) -> int:
    if isinstance(tree_height, bool) or not isinstance(tree_height, int) or tree_height <= 0:
        raise ValueError("tree_height must be positive")
    return (1 << tree_height) - 1


def circuit_to_basis_rule_ratio(tree_height: int) -> Fraction:
    return Fraction(total_internal_rooted_circuit_rule_count(tree_height), local_horn_basis_rule_count(tree_height))


def _children_by_node(tree: AndTree) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for rule in tree.local_rules:
        children = tuple(sorted(rule.premises, key=repr))
        if len(children) != 2:
            raise AssertionError("balanced AND tree lost binary premise width")
        result[rule.conclusion] = (children[0], children[1])
    return result


def enumerate_minimal_availability_sets(tree: AndTree, node: str) -> tuple[frozenset[str], ...]:
    children = _children_by_node(tree)
    if node not in children:
        return (frozenset({node}),)
    left, right = children[node]
    left_sets = enumerate_minimal_availability_sets(tree, left)
    right_sets = enumerate_minimal_availability_sets(tree, right)
    derived = tuple(left_set | right_set for left_set in left_sets for right_set in right_sets)
    return (frozenset({node}), *derived)


def enumerate_rooted_circuit_premises(tree: AndTree, node: str) -> tuple[frozenset[str], ...]:
    if tree.height > 4:
        raise ValueError("explicit rooted-circuit enumeration is limited to tree height<=4")
    return tuple(seed_set for seed_set in enumerate_minimal_availability_sets(tree, node) if seed_set != frozenset({node}))


def verify_enumerated_rooted_circuits(tree: AndTree, node: str) -> bool:
    for premises in enumerate_rooted_circuit_premises(tree, node):
        if node not in horn_closure(tree.local_rules, premises):
            raise AssertionError("enumerated premise failed to derive root")
        for removed in premises:
            if node in horn_closure(tree.local_rules, premises - {removed}):
                raise AssertionError("enumerated premise was not inclusion-minimal")
    return True


def enumerated_width_histogram(tree: AndTree, node: str) -> Polynomial:
    histogram: Polynomial = {}
    for premises in enumerate_rooted_circuit_premises(tree, node):
        histogram[len(premises)] = histogram.get(len(premises), 0) + 1
    return histogram


@dataclass(frozen=True)
class RootedCircuitExplosionReport:
    height: int
    leaf_count: int
    local_basis_rules: int
    root_circuit_count: int
    all_internal_circuit_rules: int
    root_min_premise_width: int
    root_max_premise_width: int
    root_total_premise_literals: int
    root_average_premise_width: Fraction


def rooted_circuit_explosion_report(height: int) -> RootedCircuitExplosionReport:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be positive")
    return RootedCircuitExplosionReport(
        height=height,
        leaf_count=1 << height,
        local_basis_rules=local_horn_basis_rule_count(height),
        root_circuit_count=rooted_circuit_count(height),
        all_internal_circuit_rules=total_internal_rooted_circuit_rule_count(height),
        root_min_premise_width=rooted_circuit_min_width(height),
        root_max_premise_width=rooted_circuit_max_width(height),
        root_total_premise_literals=rooted_circuit_total_premise_literals(height),
        root_average_premise_width=rooted_circuit_average_premise_width(height),
    )
