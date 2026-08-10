"""Rooted-circuit premise explosion in a balanced binary Horn AND tree.

For one internal node, a rooted-circuit premise is an inclusion-minimal seed set
not containing the node that derives it under the local Horn closure.

Let A_h(z) count minimal ways to make a node of height h available, **allowing**
the node itself as a one-atom seed.  For a leaf,

    A_0(z)=z.

For h>=1, a node is available either by seeding the node itself (z) or by making
both children available independently:

    A_h(z) = z + A_(h-1)(z)^2.

The rooted-circuit premise generating polynomial excludes the direct root seed:

    P_h(z)=A_(h-1)(z)^2=A_h(z)-z.

Thus coefficient [z^m] P_h is the number of inclusion-minimal root premises of
width m.

At z=1, with M_h=P_h(1),

    M_1=1,
    M_h=(1+M_(h-1))^2.

This grows doubly exponentially in tree height and exponentially in the number
of leaves.  The local Horn basis still has only 2^h-1 rules.

The polynomial recurrence also records total premise-literal storage and average
premise width.  Exact set enumeration is included only for small trees as an
independent oracle for the recurrence.

Closure systems, Horn circuits and antichain/minimal-generator enumeration are
standard prior mathematics/CS.  The project value is the Stage131 storage
interpretation: the one-round rooted-circuit table can be exponentially larger
than a compositional local basis even for a tree-shaped closure law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

from .stage131_horn_hyperedge_presentation import (
    AndTree,
    balanced_binary_and_tree,
    horn_closure,
)


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
    for left_degree, left_coefficient in left.items():
        for right_degree, right_coefficient in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, 0) + left_coefficient * right_coefficient
    return result


def availability_premise_polynomial(height: int) -> Polynomial:
    """Return A_h(z): minimal availability seeds, including direct node seed."""
    if isinstance(height, bool) or not isinstance(height, int) or height < 0:
        raise ValueError("height must be a nonnegative integer")
    current: Polynomial = {1: 1}
    for _ in range(height):
        current = polynomial_add({1: 1}, polynomial_multiply(current, current))
    return current


def rooted_circuit_width_polynomial(height: int) -> Polynomial:
    """Return P_h(z) for h>=1, excluding the direct root seed."""
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    child_availability = availability_premise_polynomial(height - 1)
    return polynomial_multiply(child_availability, child_availability)


def rooted_circuit_count(height: int) -> int:
    polynomial = rooted_circuit_width_polynomial(height)
    return sum(polynomial.values())


def rooted_circuit_count_recurrence(height: int) -> int:
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be a positive integer")
    count = 1
    if height == 1:
        return count
    for _ in range(2, height + 1):
        count = (1 + count) ** 2
    return count


def rooted_circuit_total_premise_literals(height: int) -> int:
    polynomial = rooted_circuit_width_polynomial(height)
    return sum(width * count for width, count in polynomial.items())


def rooted_circuit_average_premise_width(height: int) -> Fraction:
    count = rooted_circuit_count(height)
    return Fraction(rooted_circuit_total_premise_literals(height), count)


def rooted_circuit_min_width(height: int) -> int:
    return min(rooted_circuit_width_polynomial(height))


def rooted_circuit_max_width(height: int) -> int:
    return max(rooted_circuit_width_polynomial(height))


def rooted_circuit_count_lower_bound(height: int) -> int:
    """Simple explicit lower bound 2^(2^(h-1)) for h>=2; exact at h=2."""
    if isinstance(height, bool) or not isinstance(height, int) or height < 2:
        raise ValueError("lower-bound formula is stated for height>=2")
    return 1 << (1 << (height - 1))


def rooted_circuit_count_upper_bound(height: int) -> int:
    """Simple explicit upper bound M_h < 2^(2^h-1)."""
    if isinstance(height, bool) or not isinstance(height, int) or height <= 0:
        raise ValueError("height must be positive")
    return 1 << ((1 << height) - 1)


def total_internal_rooted_circuit_rule_count(tree_height: int) -> int:
    """Count all rooted-circuit rules over every internal node of the full tree."""
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
    return Fraction(
        total_internal_rooted_circuit_rule_count(tree_height),
        local_horn_basis_rule_count(tree_height),
    )


def _children_by_node(tree: AndTree) -> dict[str, tuple[str, str]]:
    result = {}
    for rule in tree.local_rules:
        children = tuple(sorted(rule.premises, key=repr))
        if len(children) != 2:
            raise AssertionError("balanced AND tree local rule lost binary premise width")
        result[rule.conclusion] = (children[0], children[1])
    return result


def enumerate_minimal_availability_sets(
    tree: AndTree,
    node: str,
) -> tuple[frozenset[str], ...]:
    """Minimal seed sets making node available, including {node}; small-tree oracle."""
    children = _children_by_node(tree)
    if node not in children:
        return (frozenset({node}),)
    left, right = children[node]
    left_sets = enumerate_minimal_availability_sets(tree, left)
    right_sets = enumerate_minimal_availability_sets(tree, right)
    derived = tuple(
        left_set | right_set
        for left_set in left_sets
        for right_set in right_sets
    )
    return (frozenset({node}), *derived)


def enumerate_rooted_circuit_premises(tree: AndTree, node: str) -> tuple[frozenset[str], ...]:
    """Enumerate all rooted-circuit premises for one internal node; small-tree oracle."""
    if tree.height > 4:
        raise ValueError("explicit rooted-circuit enumeration is limited to tree height<=4")
    availability = enumerate_minimal_availability_sets(tree, node)
    circuits = tuple(seed_set for seed_set in availability if seed_set != frozenset({node}))
    return circuits


def verify_enumerated_rooted_circuits(tree: AndTree, node: str) -> bool:
    circuits = enumerate_rooted_circuit_premises(tree, node)
    for premises in circuits:
        if node not in horn_closure(tree.local_rules, premises):
            raise AssertionError("enumerated rooted premise failed to derive root")
        for removed in premises:
            if node in horn_closure(tree.local_rules, premises - {removed}):
                raise AssertionError("enumerated rooted premise was not inclusion-minimal")
    return True


def enumerated_width_histogram(tree: AndTree, node: str) -> Polynomial:
    circuits = enumerate_rooted_circuit_premises(tree, node)
    histogram: Polynomial = {}
    for premises in circuits:
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
