"""Static equal-cost raw-three-axis query design for sparse signed-X6 mass.

This is a task-local consumer of observer_certificate/WeightHistogram, not a
new BRC carrier. GUARANTEED always requires the caller's declared target-support
bound; this planner does not infer sparsity from observed marginal tables.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
OBSERVER_PATH = ROOT / "experiments" / "owner_joint_observer_20260907"
if str(OBSERVER_PATH) not in sys.path:
    sys.path.insert(0, str(OBSERVER_PATH))
from observer_certificate import Branch, fiber_histograms, raw_marginal_table


ALL_TRIPLES = tuple(combinations(range(6), 3))
OPTIMAL_PAIR_COVER = ((0, 1, 2), (0, 1, 3), (0, 4, 5),
                      (1, 4, 5), (2, 3, 4), (2, 3, 5))


def _six_ints(values, name):
    values = tuple(values)
    if len(values) != 6 or any(type(v) is not int for v in values):
        raise ValueError(f"{name} must contain six signed integers")
    return values


@dataclass(frozen=True)
class SignedAxisChart:
    """Common signed primitive-axis relabeling and Cell anchor, not general GL6."""
    anchor: tuple[int, ...] = (0, 0, 0, 0, 0, 0)
    permutation: tuple[int, ...] = (0, 1, 2, 3, 4, 5)
    signs: tuple[int, ...] = (1, 1, 1, 1, 1, 1)

    def __post_init__(self):
        anchor = _six_ints(self.anchor, "anchor")
        permutation = _six_ints(self.permutation, "permutation")
        signs = _six_ints(self.signs, "signs")
        if sorted(permutation) != list(range(6)):
            raise ValueError("frame must permute the six primitive axes")
        if any(sign not in (-1, 1) for sign in signs):
            raise ValueError("frame signs must be +1 or -1")
        object.__setattr__(self, "anchor", anchor)
        object.__setattr__(self, "permutation", permutation)
        object.__setattr__(self, "signs", signs)

    def to_world(self, coordinates):
        coordinates = _six_ints(coordinates, "coordinates")
        world = list(self.anchor)
        for axis in range(6):
            world[self.permutation[axis]] += self.signs[axis] * coordinates[axis]
        return tuple(world)

    def to_chart(self, coordinates):
        coordinates = _six_ints(coordinates, "coordinates")
        return tuple(self.signs[axis] * (coordinates[self.permutation[axis]]
                     - self.anchor[self.permutation[axis]]) for axis in range(6))

    def record(self):
        return {"anchor": list(self.anchor), "permutation": list(self.permutation),
                "signs": list(self.signs)}


DEFAULT_CHART = SignedAxisChart()


def _contract(s, queries, chart):
    if type(s) is not int or s < 0:
        raise ValueError("s must be a nonnegative integer; bool/float are invalid")
    if type(chart) is not SignedAxisChart:
        raise TypeError("chart must be an explicit SignedAxisChart")
    canonical = []
    for query in queries:
        query = tuple(query)
        if (len(query) != 3 or any(type(a) is not int or not 0 <= a < 6 for a in query)
                or len(set(query)) != 3):
            raise ValueError("each query must select three distinct integer axes 0..5")
        canonical.append(tuple(sorted(query)))
    if len(set(canonical)) != len(canonical):
        raise ValueError("query collections are sets; duplicate triples are rejected")
    return s, tuple(sorted(canonical)), chart


def _binding(s, queries, chart):
    value = {"support_bound": s, "queries": [list(q) for q in queries], "chart": chart.record()}
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def _chart_population(branches, chart):
    branches = tuple(branches)
    # Reuse the original consumer to validate even an empty query collection.
    raw_marginal_table(branches, tuple(range(6)))
    return tuple(Branch(b.label, chart.to_chart(b.coordinate), b.weight) for b in branches)


def observe(branches, queries, *, chart=DEFAULT_CHART, encoding="raw"):
    """Read full mass tables through existing BRC; retain raw or joint can3/depth."""
    _, queries, chart = _contract(0, queries, chart)
    if encoding not in ("raw", "can3_depth"):
        raise ValueError("the recovery contract accepts raw or joint can3_depth only")
    population = _chart_population(branches, chart)
    output = {}
    for axes in queries:
        table = raw_marginal_table(population, axes)
        if encoding == "raw":
            output[axes] = table
        else:
            output[axes] = {
                (tuple(x - min(address) for x in address), min(address)): mass
                for address, mass in table.items()
            }
    return output


def _branch_records(population):
    return [{"label": b.label, "coordinate": list(b.coordinate),
             "weight": f"{b.weight.numerator}/{b.weight.denominator}"} for b in population]


def _from_records(records):
    if type(records) is not list:
        raise ValueError("population must be a list of positive branch records")
    output = []
    for item in records:
        if type(item) is not dict or set(item) != {"label", "coordinate", "weight"}:
            raise ValueError("wrong branch record fields")
        weight = item["weight"]
        if type(weight) is not str:
            raise ValueError("witness weights must be canonical p/q strings")
        value = Fraction(weight)
        if weight != f"{value.numerator}/{value.denominator}":
            raise ValueError("witness weight is not canonical")
        output.append(Branch(item["label"], tuple(item["coordinate"]), value))
    return tuple(output)


def _parity_populations(varying_axes, chart):
    positive, negative = [], []
    for bits in product((0, 1), repeat=len(varying_axes)):
        coordinate = [0] * 6
        for axis, bit in zip(varying_axes, bits):
            coordinate[axis] = bit
        parity = sum(bits) % 2
        branch = Branch(f"parity{parity}:" + "".join(map(str, bits)),
                        chart.to_world(coordinate), Fraction(1))
        (positive if parity == 0 else negative).append(branch)
    return tuple(positive), tuple(negative)


def verify_counterexample(s, queries, witness, *, chart=DEFAULT_CHART):
    """Recompute raw BRC tables and actual spatial support, ignoring self-reports."""
    try:
        s, queries, chart = _contract(s, queries, chart)
        fields = {"schema", "input_sha256", "varying_axes", "target", "competitor"}
        if type(witness) is not dict or set(witness) != fields:
            raise ValueError("wrong counterexample fields")
        if witness["schema"] != "owner_x6_query_counterexample_v1":
            raise ValueError("unknown witness schema")
        if witness["input_sha256"] != _binding(s, queries, chart):
            raise ValueError("witness is not bound to this query/support/chart contract")
        left, right = _from_records(witness["target"]), _from_records(witness["competitor"])
        spatial_left = raw_marginal_table(left, tuple(range(6)))
        spatial_right = raw_marginal_table(right, tuple(range(6)))
        if len(spatial_left) > s:
            raise ValueError("witness target violates the declared spatial support bound")
        if spatial_left == spatial_right:
            raise ValueError("different branch labels are not different spatial masses")
        chart_left, chart_right = _chart_population(left, chart), _chart_population(right, chart)
        varying = witness["varying_axes"]
        if (type(varying) is not list or any(type(a) is not int or not 0 <= a < 6 for a in varying)
                or varying != sorted(set(varying))):
            raise ValueError("varying_axes must be a sorted set of integer axes")
        actual_varying = [axis for axis in range(6)
                          if len({b.coordinate[axis] for b in chart_left + chart_right}) > 1]
        if varying != actual_varying:
            raise ValueError("varying_axes does not match the supplied populations")
        comparisons = []
        for query in queries:
            lhs, rhs = raw_marginal_table(chart_left, query), raw_marginal_table(chart_right, query)
            if lhs != rhs:
                raise ValueError(f"raw query {query} distinguishes the alleged witness")
            comparisons.append({"axes": list(query), "raw_mass_tables_equal": True,
                                "fiber_histograms_equal": fiber_histograms(chart_left, query)
                                == fiber_histograms(chart_right, query),
                                "raw_fiber_count": len(lhs)})
        difference = sorted(key for key in set(spatial_left) | set(spatial_right)
                            if spatial_left.get(key, 0) != spatial_right.get(key, 0))[0]
        return {"valid": True, "target_support": len(spatial_left),
                "competitor_support": len(spatial_right), "queries_checked": len(queries),
                "comparisons": comparisons,
                "spatial_difference": {"coordinate": list(difference),
                    "target_mass": str(spatial_left.get(difference, 0)),
                    "competitor_mass": str(spatial_right.get(difference, 0))},
                "scope": "FAILURE_OF_UNIVERSAL_QUERY_GUARANTEE; NOT_AMBIGUITY_OF_USER_DATA"}
    except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) as error:
        return {"valid": False, "reason": str(error)}


def classify_query_set(s, queries, *, chart=DEFAULT_CHART):
    """Classify exactly the universal guarantee under a USER-DECLARED support bound."""
    s, queries, chart = _contract(s, queries, chart)
    result = {"schema": "owner_x6_query_plan_v1", "support_bound": s,
              "queries": [list(q) for q in queries], "query_count": len(queries),
              "chart": chart.record(), "input_sha256": _binding(s, queries, chart),
              "sparsity_premise": "USER_DECLARED_NOT_VERIFIED_FROM_OBSERVATIONS",
              "target_and_competitor": "FINITE_NONNEGATIVE_SPATIAL_MASS_IN_THE_SAME_CHART",
              "recovery_scope": "SPATIAL_MASS_ONLY; NO_BRANCH_LABEL_OR_PATH_IDENTITY_RECOVERY",
              "query_contract": "STATIC_UNWEIGHTED_FULL_RAW_THREE_AXIS_TABLES"}
    required_order = 0 if s == 0 else 1 if s == 1 else 2 if s <= 3 else 3 if s <= 7 else 4
    required = list(combinations(range(6), required_order))
    coverage = []
    missing = []
    for axes in required:
        query = next((q for q in queries if set(axes).issubset(q)), None)
        if query is None:
            missing.append(axes)
        else:
            coverage.append({"required_axes": list(axes), "read_query": list(query)})
    minimum = 1 if s == 0 else 2 if s == 1 else 6 if s <= 3 else 20 if s <= 7 else None
    result.update(required_cover_order=required_order, coverage_witness=coverage,
                  missing_required_subsets=[list(a) for a in missing],
                  global_minimum_table_count=minimum,
                  possible_with_three_axis_queries=s < 8)
    if not missing:
        result.update(status="GUARANTEED", counterexample=None)
        return result
    varying = missing[0]
    if s == 0:
        target, competitor = (), (Branch("nonzero_competitor", chart.to_world((0,) * 6), Fraction(1)),)
    else:
        target, competitor = _parity_populations(varying, chart)
    witness = {"schema": "owner_x6_query_counterexample_v1",
               "input_sha256": _binding(s, queries, chart), "varying_axes": list(varying),
               "target": _branch_records(target), "competitor": _branch_records(competitor)}
    verification = verify_counterexample(s, queries, witness, chart=chart)
    if not verification["valid"]:
        raise ArithmeticError("generated BRC counterexample failed: " + verification["reason"])
    result.update(status="COUNTEREXAMPLE", counterexample=witness, verification=verification)
    return result


def minimum_query_plan(s, *, chart=DEFAULT_CHART):
    """Return a proved minimum plan, or an all-20-table impossibility witness."""
    if type(s) is not int or s < 0:
        raise ValueError("s must be a nonnegative integer")
    queries = ((0, 1, 2),) if s == 0 else ((0, 1, 2), (3, 4, 5)) if s == 1 else (
        OPTIMAL_PAIR_COVER if s <= 3 else ALL_TRIPLES)
    result = classify_query_set(s, queries, chart=chart)
    result["minimum_certificate"] = (
        "ONE_TOTAL_MASS_OBSERVER_REQUIRED" if s == 0 else
        "SIX_AXES_REQUIRE_AT_LEAST_TWO_TRIPLES" if s == 1 else
        "EACH_AXIS_NEEDS_THREE_INCIDENCES; 6*3/3=6; EXPLICIT_PAIR_COVER" if s <= 3 else
        "EVERY_ONE_OF_TWENTY_TRIPLES_HAS_ITS_OWN_PARITY_OBSTRUCTION" if s <= 7 else
        "FOUR_AXIS_PARITY_COLLIDES_ON_ALL_TWENTY_QUERIES")
    return result
