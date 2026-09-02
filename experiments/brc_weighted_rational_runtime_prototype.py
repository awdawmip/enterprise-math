"""Research-only exact rational Weighted-BRC prototype.

The prototype keeps all branch weights as unreduced ``DivisionExpr`` carriers.
It computes, on a finite topologically indexed DAG:

* Boolean support;
* supported path count C;
* total non-negative path mass W (sum-product);
* strongest single-path mass M (max-product);
* exact effective multiplicity W/M;
* symbolic surplus LN(W/M), materializable by the existing BRC LN runtime.

No logarithm or exponential is evaluated during propagation/recoalescence.
This file is a research prototype, not a canonical R023 mutation or promoted
Enterprise tool interface.
"""

from __future__ import annotations

from dataclasses import dataclass

from enterprise_math.brc_logarithm import LnExpr, brc_ln_decimal_readout, ln
from enterprise_math.exact_arithmetic import DivisionExpr, division


@dataclass(frozen=True)
class WeightedEdge:
    source: int
    target: int
    weight: DivisionExpr


@dataclass(frozen=True)
class WeightedBRCTargetTrace:
    target: int
    boolean_support: bool
    supported_path_count: int
    total_mass: DivisionExpr
    max_path_mass: DivisionExpr
    effective_multiplicity: DivisionExpr | None
    log_surplus: LnExpr | None
    evaluation_kind: str = "WEIGHTED_BRC_RATIONAL_RESEARCH_TRACE"


def _mass_zero() -> DivisionExpr:
    return division(0, 1)


def _mass_one() -> DivisionExpr:
    return division(1, 1)


def _mass_supported(value: DivisionExpr) -> bool:
    return value.numerator != 0


def _mass_add(left: DivisionExpr, right: DivisionExpr) -> DivisionExpr:
    return division(
        left.numerator * right.denominator
        + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def _mass_multiply(left: DivisionExpr, right: DivisionExpr) -> DivisionExpr:
    return division(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def _mass_greater(left: DivisionExpr, right: DivisionExpr) -> bool:
    return left.numerator * right.denominator > right.numerator * left.denominator


def _mass_equal(left: DivisionExpr, right: DivisionExpr) -> bool:
    return left.numerator * right.denominator == right.numerator * left.denominator


def _mass_ratio_positive(
    numerator: DivisionExpr,
    denominator: DivisionExpr,
) -> DivisionExpr:
    if not _mass_supported(numerator) or not _mass_supported(denominator):
        raise ValueError("effective multiplicity ratio requires positive masses")
    return division(
        numerator.numerator * denominator.denominator,
        numerator.denominator * denominator.numerator,
    )


def _validate_graph(node_count: int, edges: tuple[WeightedEdge, ...], source: int) -> None:
    if isinstance(node_count, bool) or not isinstance(node_count, int) or node_count <= 0:
        raise ValueError("node_count must be a positive integer")
    if isinstance(source, bool) or not isinstance(source, int) or not 0 <= source < node_count:
        raise ValueError("source must index a node")
    for edge in edges:
        if not 0 <= edge.source < node_count or not 0 <= edge.target < node_count:
            raise ValueError("edge endpoint out of range")
        if edge.source >= edge.target:
            raise ValueError("research prototype requires topological source<target edges")


def weighted_brc_target_trace(
    node_count: int,
    edges: tuple[WeightedEdge, ...],
    target: int,
    *,
    source: int = 0,
) -> WeightedBRCTargetTrace:
    """Evaluate exact weighted, max-path, count, and Boolean states at target."""
    _validate_graph(node_count, edges, source)
    if isinstance(target, bool) or not isinstance(target, int) or not 0 <= target < node_count:
        raise ValueError("target must index a node")

    total = [_mass_zero() for _ in range(node_count)]
    maximum = [_mass_zero() for _ in range(node_count)]
    count = [0 for _ in range(node_count)]
    total[source] = _mass_one()
    maximum[source] = _mass_one()
    count[source] = 1

    for vertex in range(node_count):
        if vertex == source:
            continue
        vertex_total = _mass_zero()
        vertex_max = _mass_zero()
        vertex_count = 0
        for edge in edges:
            if edge.target != vertex:
                continue
            if count[edge.source] == 0 or not _mass_supported(edge.weight):
                continue
            contribution = _mass_multiply(total[edge.source], edge.weight)
            vertex_total = _mass_add(vertex_total, contribution)
            vertex_count += count[edge.source]
            max_candidate = _mass_multiply(maximum[edge.source], edge.weight)
            if not _mass_supported(vertex_max) or _mass_greater(max_candidate, vertex_max):
                vertex_max = max_candidate
        total[vertex] = vertex_total
        maximum[vertex] = vertex_max
        count[vertex] = vertex_count

    supported = count[target] > 0
    if supported != _mass_supported(total[target]):
        raise AssertionError("non-negative weighted support must equal path-count support")
    if not supported:
        return WeightedBRCTargetTrace(
            target=target,
            boolean_support=False,
            supported_path_count=0,
            total_mass=total[target],
            max_path_mass=maximum[target],
            effective_multiplicity=None,
            log_surplus=None,
        )

    effective = _mass_ratio_positive(total[target], maximum[target])
    surplus = ln(effective)
    return WeightedBRCTargetTrace(
        target=target,
        boolean_support=True,
        supported_path_count=count[target],
        total_mass=total[target],
        max_path_mass=maximum[target],
        effective_multiplicity=effective,
        log_surplus=surplus,
    )


def _assert_mass(value: DivisionExpr, numerator: int, denominator: int) -> None:
    if not _mass_equal(value, division(numerator, denominator)):
        raise AssertionError(
            f"mass mismatch: {value.numerator}/{value.denominator} != "
            f"{numerator}/{denominator}"
        )


def equal_three_path_demo() -> WeightedBRCTargetTrace:
    # Three source-to-target paths, each of mass 1/6:
    # 0->3, 0->1->3, 0->2->3.
    edges = (
        WeightedEdge(0, 3, division(1, 6)),
        WeightedEdge(0, 1, division(1, 2)),
        WeightedEdge(1, 3, division(1, 3)),
        WeightedEdge(0, 2, division(1, 4)),
        WeightedEdge(2, 3, division(2, 3)),
    )
    trace = weighted_brc_target_trace(4, edges, 3)
    if trace.supported_path_count != 3 or not trace.boolean_support:
        raise AssertionError("three equal supported paths expected")
    _assert_mass(trace.total_mass, 1, 2)
    _assert_mass(trace.max_path_mass, 1, 6)
    if trace.effective_multiplicity is None or trace.log_surplus is None:
        raise AssertionError("positive target requires effective multiplicity and surplus")
    _assert_mass(trace.effective_multiplicity, 3, 1)
    if brc_ln_decimal_readout(trace.log_surplus, 6).text != "1.098612":
        raise AssertionError("equal three-path surplus must materialize as ln(3)")
    return trace


def unequal_two_path_demo() -> WeightedBRCTargetTrace:
    # Two path masses: 1/2 and 1/4. W/M = (3/4)/(1/2)=3/2.
    edges = (
        WeightedEdge(0, 1, division(1, 2)),
        WeightedEdge(1, 3, division(1, 1)),
        WeightedEdge(0, 2, division(1, 4)),
        WeightedEdge(2, 3, division(1, 1)),
    )
    trace = weighted_brc_target_trace(4, edges, 3)
    if trace.supported_path_count != 2 or not trace.boolean_support:
        raise AssertionError("two supported paths expected")
    _assert_mass(trace.total_mass, 3, 4)
    _assert_mass(trace.max_path_mass, 1, 2)
    if trace.effective_multiplicity is None or trace.log_surplus is None:
        raise AssertionError("positive target requires effective multiplicity and surplus")
    _assert_mass(trace.effective_multiplicity, 3, 2)
    if brc_ln_decimal_readout(trace.log_surplus, 6).text != "0.405465":
        raise AssertionError("unequal two-path surplus must materialize as ln(3/2)")
    return trace


def unreachable_demo() -> WeightedBRCTargetTrace:
    edges = (WeightedEdge(0, 1, division(1, 2)),)
    trace = weighted_brc_target_trace(3, edges, 2)
    if trace.boolean_support or trace.supported_path_count != 0:
        raise AssertionError("target 2 should be unreachable")
    if trace.effective_multiplicity is not None or trace.log_surplus is not None:
        raise AssertionError("unreachable target must not construct LN(0)")
    return trace


def main() -> None:
    equal = equal_three_path_demo()
    unequal = unequal_two_path_demo()
    unreachable_demo()
    print(
        "Weighted BRC rational prototype PASS: "
        f"equal-path C={equal.supported_path_count}, W/M=3, surplus=ln(3); "
        f"unequal-path C={unequal.supported_path_count}, W/M=3/2, surplus=ln(3/2)"
    )


if __name__ == "__main__":
    main()
