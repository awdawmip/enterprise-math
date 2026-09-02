"""Exact research checker for the CWM Weighted-BRC safe quotient candidate.

The carrier is the direct product

    count x total-mass x max-path-mass

with addition ``(+,+,max)`` and multiplication ``(*,*,*)``.

This checker uses integer/rational cross multiplication only. It validates
finite semiring laws, coherent-subcarrier closure, exact DAG path evaluation,
future-signature class aggregation, Boolean-only quotient counterexamples, and
coordinate-minimality witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError("Ratio must be non-negative with positive denominator")


RZERO = Ratio(0, 1)
RONE = Ratio(1, 1)


def radd(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.denominator
        + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def rmul(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def req(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator == right.numerator * left.denominator


def rle(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator <= right.numerator * left.denominator


def rmax(left: Ratio, right: Ratio) -> Ratio:
    if rle(left, right):
        return right
    return left


def rscale(value: Ratio, factor: int) -> Ratio:
    return Ratio(value.numerator * factor, value.denominator)


@dataclass(frozen=True)
class CWM:
    count: int
    total: Ratio
    maximum: Ratio

    def __post_init__(self) -> None:
        if isinstance(self.count, bool) or not isinstance(self.count, int) or self.count < 0:
            raise ValueError("count must be a non-negative integer")


CWM_ZERO = CWM(0, RZERO, RZERO)
CWM_ONE = CWM(1, RONE, RONE)


def cwm_add(left: CWM, right: CWM) -> CWM:
    return CWM(
        left.count + right.count,
        radd(left.total, right.total),
        rmax(left.maximum, right.maximum),
    )


def cwm_multiply(left: CWM, right: CWM) -> CWM:
    return CWM(
        left.count * right.count,
        rmul(left.total, right.total),
        rmul(left.maximum, right.maximum),
    )


def cwm_equal(left: CWM, right: CWM) -> bool:
    return (
        left.count == right.count
        and req(left.total, right.total)
        and req(left.maximum, right.maximum)
    )


def coherent(value: CWM) -> bool:
    if value.count == 0:
        return value.total.numerator == 0 and value.maximum.numerator == 0
    if value.total.numerator == 0 or value.maximum.numerator == 0:
        return False
    return (
        rle(value.maximum, value.total)
        and rle(value.total, rscale(value.maximum, value.count))
    )


def edge_lift(weight: Ratio) -> CWM:
    if weight.numerator == 0:
        return CWM_ZERO
    return CWM(1, weight, weight)


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    weight: Ratio


FORWARD_EDGES = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)
PATHS_0_TO_3 = (
    ((0, 3),),
    ((0, 1), (1, 3)),
    ((0, 2), (2, 3)),
    ((0, 1), (1, 2), (2, 3)),
)


def check_semiring_laws() -> int:
    # Coherent samples generated from explicit positive path-mass multisets.
    samples = (
        CWM_ZERO,
        CWM_ONE,
        CWM(1, Ratio(1, 2), Ratio(1, 2)),
        CWM(1, Ratio(2, 1), Ratio(2, 1)),
        CWM(2, Ratio(3, 2), Ratio(1, 1)),
        CWM(2, Ratio(2, 1), Ratio(1, 1)),
        CWM(3, Ratio(7, 2), Ratio(2, 1)),
    )
    if not all(coherent(value) for value in samples):
        raise AssertionError("semiring sample must be coherent")
    checks = 0
    for a, b, c in product(samples, repeat=3):
        if not cwm_equal(cwm_add(cwm_add(a, b), c), cwm_add(a, cwm_add(b, c))):
            raise AssertionError("CWM addition associativity failed")
        if not cwm_equal(cwm_add(a, b), cwm_add(b, a)):
            raise AssertionError("CWM addition commutativity failed")
        if not cwm_equal(cwm_multiply(cwm_multiply(a, b), c), cwm_multiply(a, cwm_multiply(b, c))):
            raise AssertionError("CWM multiplication associativity failed")
        if not cwm_equal(
            cwm_multiply(a, cwm_add(b, c)),
            cwm_add(cwm_multiply(a, b), cwm_multiply(a, c)),
        ):
            raise AssertionError("left distributivity failed")
        if not cwm_equal(
            cwm_multiply(cwm_add(a, b), c),
            cwm_add(cwm_multiply(a, c), cwm_multiply(b, c)),
        ):
            raise AssertionError("right distributivity failed")
        checks += 1
    for value in samples:
        if not cwm_equal(cwm_add(value, CWM_ZERO), value):
            raise AssertionError("additive identity failed")
        if not cwm_equal(cwm_multiply(value, CWM_ONE), value):
            raise AssertionError("multiplicative identity failed")
        if not cwm_equal(cwm_multiply(value, CWM_ZERO), CWM_ZERO):
            raise AssertionError("multiplicative zero failed")
    # Every checked operation result stays in the coherent subcarrier.
    for a, b in product(samples, repeat=2):
        if not coherent(cwm_add(a, b)):
            raise AssertionError("coherent subcarrier not closed under addition")
        if not coherent(cwm_multiply(a, b)):
            raise AssertionError("coherent subcarrier not closed under multiplication")
    return checks


def local_target_value(weights: tuple[Ratio, ...]) -> CWM:
    state = [CWM_ZERO, CWM_ZERO, CWM_ZERO, CWM_ZERO]
    state[0] = CWM_ONE
    for vertex in (1, 2, 3):
        value = CWM_ZERO
        for index, (source, target) in enumerate(FORWARD_EDGES):
            if target != vertex:
                continue
            value = cwm_add(
                value,
                cwm_multiply(state[source], edge_lift(weights[index])),
            )
        state[vertex] = value
    return state[3]


def explicit_target_value(weights: tuple[Ratio, ...]) -> CWM:
    edge_index = {edge: index for index, edge in enumerate(FORWARD_EDGES)}
    result = CWM_ZERO
    for path in PATHS_0_TO_3:
        path_value = CWM_ONE
        for edge in path:
            path_value = cwm_multiply(path_value, edge_lift(weights[edge_index[edge]]))
        result = cwm_add(result, path_value)
    return result


def check_exhaustive_dag_path_sum() -> int:
    palette = (
        Ratio(0, 1),
        Ratio(1, 2),
        Ratio(1, 1),
        Ratio(2, 1),
    )
    cases = 0
    for weights in product(palette, repeat=len(FORWARD_EDGES)):
        local = local_target_value(weights)
        explicit = explicit_target_value(weights)
        if not cwm_equal(local, explicit):
            raise AssertionError("CWM local recurrence differs from explicit path sum")
        if not coherent(local):
            raise AssertionError("path evaluation escaped coherent CWM subcarrier")
        if (local.count > 0) != (local.total.numerator > 0):
            raise AssertionError("count and mass Boolean support disagree")
        if (local.count > 0) != (local.maximum.numerator > 0):
            raise AssertionError("count and maximum Boolean support disagree")
        cases += 1
    return cases


def future_to_sink(node_count: int, edges: tuple[Edge, ...], sink: int) -> tuple[CWM, ...]:
    result = [CWM_ZERO for _ in range(node_count)]
    result[sink] = CWM_ONE
    for vertex in range(node_count - 1, -1, -1):
        if vertex == sink:
            continue
        value = CWM_ZERO
        for edge in edges:
            if edge.source != vertex:
                continue
            if edge.target <= edge.source:
                raise ValueError("checker requires topological source<target edges")
            value = cwm_add(
                value,
                cwm_multiply(edge_lift(edge.weight), result[edge.target]),
            )
        result[vertex] = value
    return tuple(result)


def future_signature(
    node_count: int,
    edges: tuple[Edge, ...],
    sinks: tuple[int, ...],
) -> tuple[tuple[CWM, ...], ...]:
    by_sink = tuple(future_to_sink(node_count, edges, sink) for sink in sinks)
    return tuple(
        tuple(by_sink[sink_index][vertex] for sink_index in range(len(sinks)))
        for vertex in range(node_count)
    )


def cwm_signature_equal(left: tuple[CWM, ...], right: tuple[CWM, ...]) -> bool:
    return len(left) == len(right) and all(
        cwm_equal(a, b) for a, b in zip(left, right)
    )


def check_future_safe_quotient() -> None:
    # 4 and 5 are declared sinks. States 1 and 2 have identical CWM futures;
    # state 3 has the same Boolean reachability but a different mass to sink 5.
    edges = (
        Edge(1, 4, Ratio(1, 1)),
        Edge(1, 5, Ratio(2, 1)),
        Edge(2, 4, Ratio(1, 1)),
        Edge(2, 5, Ratio(2, 1)),
        Edge(3, 4, Ratio(1, 1)),
        Edge(3, 5, Ratio(3, 1)),
    )
    signatures = future_signature(6, edges, (4, 5))
    if not cwm_signature_equal(signatures[1], signatures[2]):
        raise AssertionError("states 1 and 2 should be CWM future-equivalent")
    if cwm_signature_equal(signatures[1], signatures[3]):
        raise AssertionError("state 3 should have a distinct CWM future signature")

    boolean_1 = tuple(item.count > 0 for item in signatures[1])
    boolean_3 = tuple(item.count > 0 for item in signatures[3])
    if boolean_1 != boolean_3:
        raise AssertionError("strict-refinement witness requires equal Boolean future support")

    # Two arbitrary coherent prefix families enter states 1 and 2.
    prefix_1 = CWM(2, Ratio(3, 2), Ratio(1, 1))  # masses 1, 1/2
    prefix_2 = CWM(1, Ratio(2, 1), Ratio(2, 1))  # one mass 2
    merged_prefix = cwm_add(prefix_1, prefix_2)
    if not coherent(prefix_1) or not coherent(prefix_2) or not coherent(merged_prefix):
        raise AssertionError("prefix probes must be coherent")

    for target_index in range(2):
        original = cwm_add(
            cwm_multiply(prefix_1, signatures[1][target_index]),
            cwm_multiply(prefix_2, signatures[2][target_index]),
        )
        quotient = cwm_multiply(merged_prefix, signatures[1][target_index])
        if not cwm_equal(original, quotient):
            raise AssertionError("future-equivalent class aggregation was not safe")

    # Necessity witness: one unit prefix entering state 1 versus state 3 yields
    # distinct target semantics, so one entry-independent class future cannot serve both.
    if cwm_equal(
        cwm_multiply(CWM_ONE, signatures[1][1]),
        cwm_multiply(CWM_ONE, signatures[3][1]),
    ):
        raise AssertionError("different future signatures must be distinguishable by unit prefix")


def check_coordinate_minimality_witnesses() -> None:
    # Same W,M but different C.
    a = CWM(2, Ratio(2, 1), Ratio(1, 1))
    b = CWM(3, Ratio(2, 1), Ratio(1, 1))
    if not req(a.total, b.total) or not req(a.maximum, b.maximum) or a.count == b.count:
        raise AssertionError("C independence witness failed")

    # Same C,M but different W.
    c = CWM(2, Ratio(2, 1), Ratio(1, 1))
    d = CWM(2, Ratio(3, 2), Ratio(1, 1))
    if c.count != d.count or not req(c.maximum, d.maximum) or req(c.total, d.total):
        raise AssertionError("W independence witness failed")

    # Same C,W but different M.
    e = CWM(2, Ratio(2, 1), Ratio(1, 1))
    f = CWM(2, Ratio(2, 1), Ratio(3, 2))
    if e.count != f.count or not req(e.total, f.total) or req(e.maximum, f.maximum):
        raise AssertionError("M independence witness failed")

    if not all(coherent(value) for value in (a, b, c, d, e, f)):
        raise AssertionError("minimality witnesses must be coherent")


def main() -> None:
    law_checks = check_semiring_laws()
    dag_cases = check_exhaustive_dag_path_sum()
    check_future_safe_quotient()
    check_coordinate_minimality_witnesses()
    print(
        "BRC CWM safe quotient research check PASS: "
        f"{law_checks} sampled semiring-law triples; "
        f"{dag_cases} exact weighted DAG assignments; "
        "future quotient and minimality witnesses confirmed"
    )


if __name__ == "__main__":
    main()
