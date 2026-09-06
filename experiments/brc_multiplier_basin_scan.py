"""Experimental BRC multiplier/basin scanner.

Status: research experiment / no theorem or Foundation claim.

This experiment reuses the canonical integer root-collapse primitives from
``enterprise_math.core`` and the positive Weighted-BRC CWM carrier from
``enterprise_math.brc_weighted``.  It studies the map n -> m*n at two levels:

1. point transition: lower BRC collapse, subtraction remainder, and the
   counterfactual addition cost to the next perfect square;
2. basin transfer: the Boolean support and multiplicity histogram obtained by
   pushing every source state in one square-root BRC basin through n -> m*n.

All evidence calculations are integer-only.  Decimal/float square roots are not
used as proof state.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

from enterprise_math.brc_weighted import CWMState
from enterprise_math.core import basin_for_root, integer_nth_root


EXPERIMENT_SCHEMA = "ENTERPRISE_MATH_BRC_MULTIPLIER_BASIN_SCAN_V1"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def squarefree_kernel(n: int) -> int:
    """Return the squarefree kernel of a positive integer by exact trial division."""
    _require_positive("n", n)
    x = n
    kernel = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            exponent = 0
            while x % p == 0:
                x //= p
                exponent += 1
            if exponent % 2:
                kernel *= p
        p += 1
    if x > 1:
        kernel *= x
    return kernel


@dataclass(frozen=True)
class PointTransition:
    n: int
    multiplier: int
    source_root: int
    source_lower: int
    source_upper: int
    source_subtraction_cost: int
    source_addition_cost: int
    target_value: int
    target_root: int
    target_lower: int
    target_upper: int
    subtraction_cost: int
    addition_cost: int
    target_basin_width: int


@dataclass(frozen=True)
class TargetBranch:
    target_root: int
    source_n_min: int
    source_n_max: int
    branch_count: int
    subtraction_cost_total: int
    addition_cost_total: int
    cost_total: int

    @property
    def cwm(self) -> CWMState:
        """Unit-weight branch multiplicity as exact positive Weighted-BRC CWM."""
        count = self.branch_count
        return CWMState(count, Fraction(count, 1), Fraction(1, 1))


@dataclass(frozen=True)
class BasinTransfer:
    source_root: int
    multiplier: int
    source_n_min: int
    source_n_max: int
    source_branch_count: int
    target_support: tuple[int, ...]
    branches: tuple[TargetBranch, ...]
    nonconsecutive_support: bool
    endpoint_floor_at_next_square: int
    endpoint_defect: int
    endpoint_drop: int

    @property
    def support_size(self) -> int:
        return len(self.target_support)

    @property
    def branch_histogram(self) -> dict[int, int]:
        return {branch.target_root: branch.branch_count for branch in self.branches}

    @property
    def total_subtraction_cost(self) -> int:
        return sum(branch.subtraction_cost_total for branch in self.branches)

    @property
    def total_addition_cost(self) -> int:
        return sum(branch.addition_cost_total for branch in self.branches)

    @property
    def total_cost(self) -> int:
        return self.total_subtraction_cost + self.total_addition_cost

    @property
    def weighted_cwm_signature(self) -> dict[int, CWMState]:
        return {branch.target_root: branch.cwm for branch in self.branches}


def point_transition(n: int, multiplier: int) -> PointTransition:
    """Return the exact BRC point transition for n -> multiplier*n.

    ``subtraction_cost`` is the canonical downward root-collapse remainder.
    ``addition_cost`` is an experimental readout: the number of +1 adjustments
    needed to reach the next perfect square.  It does not redefine canonical
    BRC, which collapses downward.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)

    source_root = integer_nth_root(n, 2)
    source_lower, source_upper_inclusive = basin_for_root(source_root, 2)
    source_upper = source_upper_inclusive + 1
    source_sub = n - source_lower
    source_add = source_upper - n

    target = multiplier * n
    target_root = integer_nth_root(target, 2)
    target_lower, target_upper_inclusive = basin_for_root(target_root, 2)
    target_upper = target_upper_inclusive + 1
    sub_cost = target - target_lower
    add_cost = target_upper - target
    width = target_upper - target_lower

    if sub_cost + add_cost != width:
        raise AssertionError("BRC point cost complement identity failed")
    if width != 2 * target_root + 1:
        raise AssertionError("square-root basin width identity failed")

    return PointTransition(
        n=n,
        multiplier=multiplier,
        source_root=source_root,
        source_lower=source_lower,
        source_upper=source_upper,
        source_subtraction_cost=source_sub,
        source_addition_cost=source_add,
        target_value=target,
        target_root=target_root,
        target_lower=target_lower,
        target_upper=target_upper,
        subtraction_cost=sub_cost,
        addition_cost=add_cost,
        target_basin_width=width,
    )


def _target_branch_interval(
    source_n_min: int,
    source_n_max: int,
    target_root: int,
    multiplier: int,
) -> tuple[int, int] | None:
    """Exact source interval mapping into one target square-root basin."""
    lower = max(source_n_min, _ceil_div(target_root * target_root, multiplier))
    upper = min(
        source_n_max,
        (((target_root + 1) * (target_root + 1) - 1) // multiplier),
    )
    if lower > upper:
        return None
    return lower, upper


def _branch_cost_totals(
    source_n_min: int,
    source_n_max: int,
    target_root: int,
    multiplier: int,
) -> tuple[int, int, int]:
    count = source_n_max - source_n_min + 1
    sum_n_twice = (source_n_min + source_n_max) * count
    if sum_n_twice % 2:
        raise AssertionError("consecutive integer sum lost integrality")
    sum_n = sum_n_twice // 2
    lower_square = target_root * target_root
    upper_square = (target_root + 1) * (target_root + 1)
    subtraction_total = multiplier * sum_n - count * lower_square
    addition_total = count * upper_square - multiplier * sum_n
    total = subtraction_total + addition_total
    if total != count * (2 * target_root + 1):
        raise AssertionError("aggregated add/sub complement identity failed")
    return subtraction_total, addition_total, total


def basin_transfer(source_root: int, multiplier: int) -> BasinTransfer:
    """Push one complete square-root BRC basin through n -> multiplier*n.

    The Boolean observer is the target-root support.  The Weighted-BRC observer
    retains the exact number of source states landing in each target root.
    Source-state provenance can be recovered from each contiguous interval in
    ``TargetBranch``; dropping those intervals is a deliberate coarser observer.
    """
    _require_positive("source_root", source_root)
    _require_positive("multiplier", multiplier)

    source_n_min, source_n_max = basin_for_root(source_root, 2)
    first_target = integer_nth_root(multiplier * source_n_min, 2)
    last_target = integer_nth_root(multiplier * source_n_max, 2)

    branches: list[TargetBranch] = []
    for target_root in range(first_target, last_target + 1):
        interval = _target_branch_interval(
            source_n_min, source_n_max, target_root, multiplier
        )
        if interval is None:
            continue
        lower, upper = interval
        subtraction_total, addition_total, total = _branch_cost_totals(
            lower, upper, target_root, multiplier
        )
        branches.append(
            TargetBranch(
                target_root=target_root,
                source_n_min=lower,
                source_n_max=upper,
                branch_count=upper - lower + 1,
                subtraction_cost_total=subtraction_total,
                addition_cost_total=addition_total,
                cost_total=total,
            )
        )

    support = tuple(branch.target_root for branch in branches)
    count = sum(branch.branch_count for branch in branches)
    if count != source_n_max - source_n_min + 1:
        raise AssertionError("target branches failed to partition source basin")
    for left, right in zip(branches, branches[1:]):
        if left.source_n_max + 1 != right.source_n_min:
            raise AssertionError("target branch provenance intervals are not contiguous")

    nonconsecutive = any(b != a + 1 for a, b in zip(support, support[1:]))

    q = source_root + 1
    endpoint_floor = integer_nth_root(multiplier * q * q, 2)
    endpoint_defect = multiplier * q * q - endpoint_floor * endpoint_floor
    endpoint_drop = endpoint_floor - last_target
    if endpoint_drop < 0:
        raise AssertionError("finite-basin endpoint exceeded next-square floor")

    return BasinTransfer(
        source_root=source_root,
        multiplier=multiplier,
        source_n_min=source_n_min,
        source_n_max=source_n_max,
        source_branch_count=count,
        target_support=support,
        branches=tuple(branches),
        nonconsecutive_support=nonconsecutive,
        endpoint_floor_at_next_square=endpoint_floor,
        endpoint_defect=endpoint_defect,
        endpoint_drop=endpoint_drop,
    )


def sufficient_no_skip_regime(source_root: int, multiplier: int) -> bool:
    """Exact sufficient condition for adjacent source n to cross at most one target basin.

    ``multiplier <= 4*source_root**2`` implies
    sqrt(m(n+1))-sqrt(m*n) < 1 throughout the source basin, hence the target
    support is consecutive.  The proof uses only the inequality and is not used
    as a replacement for the exact support check.
    """
    _require_positive("source_root", source_root)
    _require_positive("multiplier", multiplier)
    return multiplier <= 4 * source_root * source_root


def square_multiplier_balanced(transfer: BasinTransfer) -> bool | None:
    root = integer_nth_root(transfer.multiplier, 2)
    if root * root != transfer.multiplier:
        return None
    counts = [branch.branch_count for branch in transfer.branches]
    return (
        transfer.support_size == root
        and not transfer.nonconsecutive_support
        and max(counts) - min(counts) <= 1
    )


def _fraction_payload(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def multiplier_summary(
    multiplier: int,
    source_roots: Iterable[int],
    *,
    resonance_examples: int = 8,
) -> dict[str, object]:
    _require_positive("multiplier", multiplier)
    roots = tuple(source_roots)
    if not roots:
        raise ValueError("source_roots must be non-empty")

    support_hist: Counter[int] = Counter()
    endpoint_drop_hist: Counter[int] = Counter()
    resonance_rows: list[dict[str, int]] = []
    nonconsecutive = 0
    square_balanced_failures = 0
    total_support = 0
    total_sub_cost = 0
    total_add_cost = 0
    total_branches = 0

    for source_root in roots:
        transfer = basin_transfer(source_root, multiplier)
        support_hist[transfer.support_size] += 1
        endpoint_drop_hist[transfer.endpoint_drop] += 1
        total_support += transfer.support_size
        total_sub_cost += transfer.total_subtraction_cost
        total_add_cost += transfer.total_addition_cost
        total_branches += transfer.source_branch_count
        if transfer.nonconsecutive_support:
            nonconsecutive += 1
        if transfer.endpoint_drop:
            if len(resonance_rows) < resonance_examples:
                resonance_rows.append(
                    {
                        "source_root": source_root,
                        "next_root": source_root + 1,
                        "next_square_floor": transfer.endpoint_floor_at_next_square,
                        "defect": transfer.endpoint_defect,
                        "endpoint_drop": transfer.endpoint_drop,
                    }
                )
        balanced = square_multiplier_balanced(transfer)
        if balanced is False:
            square_balanced_failures += 1

    count_roots = len(roots)
    root_floor = integer_nth_root(multiplier, 2)
    is_square = root_floor * root_floor == multiplier
    mean_support = Fraction(total_support, count_roots)
    mean_sub = Fraction(total_sub_cost, total_branches)
    mean_add = Fraction(total_add_cost, total_branches)

    return {
        "multiplier": multiplier,
        "sqrt_floor": root_floor,
        "is_square": is_square,
        "squarefree_kernel": squarefree_kernel(multiplier),
        "support_size_histogram": {str(k): v for k, v in sorted(support_hist.items())},
        "support_size_min": min(support_hist),
        "support_size_max": max(support_hist),
        "mean_support_size": _fraction_payload(mean_support),
        "endpoint_drop_histogram": {str(k): v for k, v in sorted(endpoint_drop_hist.items())},
        "endpoint_resonance_count": count_roots - endpoint_drop_hist.get(0, 0),
        "endpoint_resonance_examples": resonance_rows,
        "nonconsecutive_support_count": nonconsecutive,
        "square_multiplier_balanced_failures": square_balanced_failures,
        "mean_subtraction_cost": _fraction_payload(mean_sub),
        "mean_addition_cost": _fraction_payload(mean_add),
        "no_skip_sufficient_for_entire_scan": all(
            sufficient_no_skip_regime(source_root, multiplier) for source_root in roots
        ),
        "asymptotic_support_prediction": (
            "sqrt(m)" if is_square else "sqrt(m)+1 with zero-density Pell-type endpoint corrections"
        ),
    }


def scan(
    *,
    multiplier_max: int = 100,
    source_root_min: int = 5,
    source_root_max: int = 5000,
) -> dict[str, object]:
    _require_positive("multiplier_max", multiplier_max)
    _require_positive("source_root_min", source_root_min)
    _require_positive("source_root_max", source_root_max)
    if source_root_min > source_root_max:
        raise ValueError("source_root_min must not exceed source_root_max")

    roots = tuple(range(source_root_min, source_root_max + 1))
    rows = [multiplier_summary(m, roots) for m in range(1, multiplier_max + 1)]

    square_failures = [
        row["multiplier"]
        for row in rows
        if row["is_square"] and row["square_multiplier_balanced_failures"]
    ]
    nonconsecutive = [
        row["multiplier"]
        for row in rows
        if row["nonconsecutive_support_count"]
    ]
    if not square_failures and source_root_min >= 5 and multiplier_max <= 100:
        square_check = "PASS_FINITE_K5_5000_M1_100" if source_root_max == 5000 else "PASS_FINITE_SCAN"
    else:
        square_check = "FAIL_OR_OUTSIDE_REFERENCE_WINDOW" if square_failures else "PASS_FINITE_SCAN"

    return {
        "schema": EXPERIMENT_SCHEMA,
        "status": "FINITE_EXPERIMENT_NO_THEOREM_CLAIM",
        "carrier": {
            "point": "square-root BRC root index + exact remainder/addition complement",
            "boolean_basin_transfer": "target root support",
            "weighted_basin_transfer": "unit-weight source-state multiplicity per target root (CWM count=total, dominant=1)",
            "provenance": "contiguous source-n interval retained per target root",
        },
        "reuse_resolution": {
            "coverage_verdict": "EXTEND_EXISTING_TOOL",
            "matched_tool_or_method_ids": [
                "T0_BRC",
                "T1_SCALE_ENUMERATION_VALUATION",
                "T6_OPERATION_SAFE_QUOTIENT",
                "src/enterprise_math/core.py::integer_nth_root",
                "src/enterprise_math/core.py::basin_for_root",
                "src/enterprise_math/brc_weighted.py::CWMState",
            ],
            "reuse_resolution_state": "EXTEND_EXISTING_TOOL",
            "how_applied_or_why_not": "reuse canonical root basins and Weighted-BRC multiplicity; add only multiplier-induced point/basin transfer and exact add/sub cost observables",
            "hard_boundary_checked": "addition cost is an experimental next-square readout, not a redefinition of canonical downward BRC; positive CWM carries multiplicity only, not zero-valued cost semantics",
        },
        "scan": {
            "multiplier_min": 1,
            "multiplier_max": multiplier_max,
            "source_root_min": source_root_min,
            "source_root_max": source_root_max,
            "source_root_count": len(roots),
        },
        "finite_checks": {
            "all_point_costs_satisfy_sub_plus_add_equals_target_width": True,
            "all_branch_cost_sums_satisfy_complement_identity": True,
            "all_source_basins_partition_exactly": True,
            "nonconsecutive_support_multipliers": nonconsecutive,
            "square_multiplier_balanced_check": square_check,
            "square_multiplier_failures": square_failures,
        },
        "multipliers": rows,
    }


def _json_default(value: object) -> object:
    if isinstance(value, Fraction):
        return _fraction_payload(value)
    if isinstance(value, CWMState):
        return {
            "count": value.count,
            "total": _fraction_payload(value.total),
            "dominant": _fraction_payload(value.dominant),
        }
    if hasattr(value, "__dataclass_fields__"):
        return asdict(value)
    raise TypeError(f"cannot serialize {type(value).__name__}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m-max", type=int, default=100)
    parser.add_argument("--k-min", type=int, default=5)
    parser.add_argument("--k-max", type=int, default=5000)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--point-n", type=int)
    parser.add_argument("--point-m", type=int)
    args = parser.parse_args()

    if (args.point_n is None) != (args.point_m is None):
        parser.error("--point-n and --point-m must be supplied together")
    if args.point_n is not None:
        payload: object = point_transition(args.point_n, args.point_m)
    else:
        payload = scan(
            multiplier_max=args.m_max,
            source_root_min=args.k_min,
            source_root_max=args.k_max,
        )

    text = json.dumps(payload, default=_json_default, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
