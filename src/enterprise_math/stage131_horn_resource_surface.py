"""Resource surface and rooted-circuit frontiers for the Stage131 AND tree.

A multi-premise Horn presentation needs more storage coordinates than rule count.
This module records total premise incidences and maximum premise width, and checks
that the natural level-frontier premises of a balanced AND tree are genuine
inclusion-minimal premises for the root.

For root at height h and a gap s, the frontier consists of the 2^s descendants
exactly s levels below the root.  Their conjunction derives the root, and
removing any one frontier atom destroys that derivation.  Hence each such
frontier is a rooted-circuit premise for the same root, despite widths ranging
from2 up to2^h.

This sharpens the Stage131 interpretation: one-round minimal-premise tables can
contain many incomparable minimal premises for one root, while storage/fan-in
and continuation depth vary dramatically among the corresponding execution
presentations.
"""

from __future__ import annotations

from dataclasses import dataclass

from .stage131_horn_hyperedge_presentation import (
    AndTree,
    HornRule,
    add_derived_horn_macros,
    and_tree_span_macros,
    and_tree_span_presentation_report,
    balanced_binary_and_tree,
    horn_closure,
    rule_is_semantically_derived,
)


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def root_frontier_premises(tree: AndTree, gap: int) -> frozenset[str]:
    s = _positive_int(gap, name="gap")
    if s > tree.height:
        raise ValueError("gap cannot exceed tree height")
    return tree.descendants_at_gap[(tree.root, s)]


def root_frontier_macro(tree: AndTree, gap: int) -> HornRule:
    premises = root_frontier_premises(tree, gap)
    return HornRule(premises, tree.root, f"root_frontier_gap{gap}")


def root_frontier_is_inclusion_minimal_premise(tree: AndTree, gap: int) -> bool:
    macro = root_frontier_macro(tree, gap)
    if not rule_is_semantically_derived(tree.local_rules, macro):
        raise AssertionError("frontier premise unexpectedly failed to derive root")
    for removed in macro.premises:
        reduced = macro.premises - {removed}
        if tree.root in horn_closure(tree.local_rules, reduced):
            raise AssertionError("root frontier remained sufficient after removing one premise")
    return True


def and_tree_max_premise_width(height: int, span: int) -> int:
    h = _positive_int(height, name="height")
    s = _positive_int(span, name="span")
    if s > h:
        raise ValueError("span cannot exceed height")
    if s == 1:
        return 2
    return 1 << s


@dataclass(frozen=True)
class AndTreeResourcePoint:
    height: int
    span: int
    total_rule_count: int
    total_premise_literals: int
    maximum_premise_width: int
    root_round: int
    full_closure_rounds: int
    extra_macro_rules: int
    extra_macro_premise_literals: int


def and_tree_resource_point(height: int, span: int) -> AndTreeResourcePoint:
    report = and_tree_span_presentation_report(height, span)
    return AndTreeResourcePoint(
        height=height,
        span=span,
        total_rule_count=report.total_rule_count,
        total_premise_literals=report.total_premise_literals,
        maximum_premise_width=and_tree_max_premise_width(height, span),
        root_round=report.root_round,
        full_closure_rounds=report.full_closure_rounds,
        extra_macro_rules=report.macro_rule_count,
        extra_macro_premise_literals=report.macro_premise_literals,
    )


def and_tree_resource_table(height: int) -> tuple[AndTreeResourcePoint, ...]:
    h = _positive_int(height, name="height")
    return tuple(and_tree_resource_point(h, span) for span in range(1, h + 1))


def resource_point_dominates(
    left: AndTreeResourcePoint,
    right: AndTreeResourcePoint,
    *,
    include_fan_in: bool = True,
    include_root_depth: bool = True,
    include_full_depth: bool = True,
) -> bool:
    if left.height != right.height:
        raise ValueError("resource points must belong to the same tree height")
    left_values = [left.total_rule_count, left.total_premise_literals]
    right_values = [right.total_rule_count, right.total_premise_literals]
    if include_fan_in:
        left_values.append(left.maximum_premise_width)
        right_values.append(right.maximum_premise_width)
    if include_root_depth:
        left_values.append(left.root_round)
        right_values.append(right.root_round)
    if include_full_depth:
        left_values.append(left.full_closure_rounds)
        right_values.append(right.full_closure_rounds)
    weak = all(a <= b for a, b in zip(left_values, right_values, strict=True))
    strict = any(a < b for a, b in zip(left_values, right_values, strict=True))
    return weak and strict


def and_tree_resource_frontier(
    height: int,
    *,
    include_fan_in: bool = True,
    include_root_depth: bool = True,
    include_full_depth: bool = True,
) -> tuple[AndTreeResourcePoint, ...]:
    points = and_tree_resource_table(height)
    return tuple(
        point
        for point in points
        if not any(
            resource_point_dominates(
                other,
                point,
                include_fan_in=include_fan_in,
                include_root_depth=include_root_depth,
                include_full_depth=include_full_depth,
            )
            for other in points
            if other != point
        )
    )


def root_frontier_premise_widths(height: int) -> tuple[int, ...]:
    tree = balanced_binary_and_tree(height)
    widths = []
    for gap in range(1, tree.height + 1):
        premise = root_frontier_premises(tree, gap)
        if not root_frontier_is_inclusion_minimal_premise(tree, gap):
            raise AssertionError("root frontier failed minimality")
        widths.append(len(premise))
    return tuple(widths)
