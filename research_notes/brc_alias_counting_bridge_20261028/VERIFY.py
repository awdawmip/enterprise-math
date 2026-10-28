#!/usr/bin/env python3
"""Author-side exact finite checks for RGS, color fibers, and parsimonious 3-CNF.

From the repository root after publication:
PYTHONPATH=src python3 research_notes/brc_alias_counting_bridge_20261028/VERIFY.py
The local author run uses the isolated vendor directory when it is present.
The declared domains are fixed below. No allocator execution, history count,
native physical inference, ETH speedup, formal admission, or independence claim.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
LOCAL_VENDOR = HERE / "vendor"
if LOCAL_VENDOR.is_dir():
    sys.path.insert(0, str(LOCAL_VENDOR))
from enterprise_math.brc_histogram import (  # noqa: E402
    WeightHistogram,
    histogram_recoalesce,
    histogram_serial,
)

SOURCE_COMMIT = "2ea525e27882e26a64cf6d3573b5e230da87f708"
SOURCE_BLOBS = {
    "brc_histogram.py": "9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1",
    "brc_rational_holonomy.py": "2591640fe348da9cd7f293a957bea9ae92c82943",
    "brc_weighted_recurrent.py": "4e6b3132580e3cd70a20a0d8bd4d28792b961afb",
}
RGS_MAX = 7
COLOR_MAX = 7
PRIMARY_MAX = 5
ALL_VARIABLES_MAX = 3
ZERO = WeightHistogram(())
ONE = WeightHistogram.from_counts({1: 1})
BRC_CALLS = Counter()


def serial(left: WeightHistogram, right: WeightHistogram) -> WeightHistogram:
    BRC_CALLS["histogram_serial"] += 1
    return histogram_serial(left, right)


def recoalesce(left: WeightHistogram, right: WeightHistogram) -> WeightHistogram:
    BRC_CALLS["histogram_recoalesce"] += 1
    return histogram_recoalesce(left, right)


def rgs_sequences(length: int):
    """All restricted-growth strings, with labels starting at one."""
    def visit(prefix: tuple[int, ...], maximum: int):
        if len(prefix) == length:
            yield prefix
            return
        for label in range(1, maximum + 2):
            yield from visit(prefix + (label,), max(maximum, label))
    yield from visit((), 0)


def canonical_labels(colors: tuple[int, ...]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    result = []
    for color in colors:
        if color not in labels:
            labels[color] = len(labels) + 1
        result.append(labels[color])
    return tuple(result)


def falling_factorial(q: int, k: int) -> int:
    result = 1
    for used in range(k):
        result *= q - used
    return result


def brc_block_count_distribution(length: int) -> dict[int, WeightHistogram]:
    """Count-only projection, not a behavioral quotient preserving same(i,j)."""
    current = {0: ONE}
    for _ in range(length):
        following: dict[int, WeightHistogram] = {}
        for blocks, carrier in current.items():
            if blocks:
                term = serial(carrier, WeightHistogram.from_counts({1: blocks}))
                following[blocks] = recoalesce(following.get(blocks, ZERO), term)
            term = serial(carrier, ONE)
            following[blocks + 1] = recoalesce(following.get(blocks + 1, ZERO), term)
        current = following
    return current


def brc_color_fiber(q: int, blocks: int) -> WeightHistogram:
    carrier = ONE
    for used in range(blocks):
        carrier = serial(carrier, WeightHistogram.from_counts({1: q - used}))
    return carrier


def check_rgs_and_colors() -> list[dict]:
    results = []
    known_bell = [1, 1, 2, 5, 15, 52, 203, 877]
    for length in range(1, RGS_MAX + 1):
        strings = list(rgs_sequences(length))
        by_blocks = Counter(max(s) for s in strings)
        assert len(strings) == len(set(strings)) == known_bell[length]
        brc_counts = brc_block_count_distribution(length)
        assert {k: h.count for k, h in brc_counts.items()} == dict(by_blocks)
        logical = ZERO
        physical = ZERO
        fiber_size_carrier = ZERO
        table = []
        for blocks, class_count in sorted(by_blocks.items()):
            h = brc_counts[blocks]
            logical = recoalesce(logical, h)
            fiber = brc_color_fiber(length, blocks)
            formula = falling_factorial(length, blocks)
            assert fiber.count == formula and fiber.total_mass == formula
            contribution = serial(h, fiber)
            physical = recoalesce(physical, contribution)
            fiber_size_carrier = recoalesce(
                fiber_size_carrier,
                WeightHistogram.from_counts({formula: class_count}),
            )
            table.append({"blocks": blocks, "logical_classes": class_count,
                          "colorings_per_class": formula,
                          "colored_encodings": contribution.count})
        assert logical.count == len(strings)
        assert physical.count == length ** length
        assert fiber_size_carrier.count == logical.count
        assert fiber_size_carrier.total_mass == physical.count
        enumerated_colorings = None
        if length <= COLOR_MAX:
            fibers = Counter(canonical_labels(c) for c in product(range(1, length + 1), repeat=length))
            assert set(fibers) == set(strings)
            for s, count in fibers.items():
                assert count == falling_factorial(length, max(s))
            enumerated_colorings = sum(fibers.values())
            assert enumerated_colorings == physical.count
        results.append({"r": length, "logical_classes": logical.count,
                        "well_formed_colored_encodings": physical.count,
                        "enumerated_colored_encodings": enumerated_colorings,
                        "fibers_by_block_count": table,
                        "fiber_size_histogram": [[int(w), c] for w, c in fiber_size_carrier.entries]})
    return results


@dataclass
class CNF:
    variables: int
    primary: dict[tuple[int, int], int]
    clauses: list[tuple[int, ...]]
    gates: list[tuple[str, int, tuple[int, ...]]]

    def gate(self, operator: str, *inputs: int) -> int:
        self.variables += 1
        output = self.variables
        if operator == "OR":
            a, b = inputs
            self.clauses += [(-a, output), (-b, output), (a, b, -output)]
        elif operator == "AND":
            a, b = inputs
            self.clauses += [(a, -output), (b, -output), (-a, -b, output)]
        elif operator == "NOT":
            (a,) = inputs
            self.clauses += [(a, output), (-a, -output)]
        else:
            raise ValueError(operator)
        self.gates.append((operator, output, inputs))
        return output


def rgs_cnf(r: int) -> CNF:
    x = {(i, j): number for number, (i, j) in enumerate(
        ((i, j) for i in range(1, r + 1) for j in range(1, i + 1)), start=1)}
    cnf = CNF(len(x), x, [], [])
    for i in range(1, r + 1):
        prefix = x[i, 1]
        for j in range(2, i + 1):
            prior = prefix
            prefix = cnf.gate("OR", prior, x[i, j])
            cnf.clauses.append((-prior, -x[i, j]))
        cnf.clauses.append((prefix,))
    seen = {}
    for j in range(1, r + 1):
        seen[j, j] = x[j, j]
        for i in range(j + 1, r + 1):
            seen[i, j] = cnf.gate("OR", seen[i - 1, j], x[i, j])
    for i in range(2, r + 1):
        for j in range(2, i + 1):
            cnf.clauses.append((-x[i, j], seen[i - 1, j - 1]))
    return cnf


def extend_assignment(cnf: CNF, primary_mask: int) -> list[bool]:
    values = [False] * (cnf.variables + 1)
    for variable in cnf.primary.values():
        values[variable] = bool(primary_mask & (1 << (variable - 1)))
    for operator, output, inputs in cnf.gates:
        if operator == "OR":
            values[output] = values[inputs[0]] or values[inputs[1]]
        elif operator == "AND":
            values[output] = values[inputs[0]] and values[inputs[1]]
        else:
            values[output] = not values[inputs[0]]
    return values


def satisfies(cnf: CNF, values: list[bool]) -> bool:
    return all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in cnf.clauses)


def decode_if_rgs(cnf: CNF, values: list[bool], r: int):
    """Semantic test independent of the CNF prefix/growth clauses."""
    sequence = []
    maximum = 0
    for i in range(1, r + 1):
        selected = [j for j in range(1, i + 1) if values[cnf.primary[i, j]]]
        if len(selected) != 1:
            return None
        label = selected[0]
        if label > maximum + 1:
            return None
        sequence.append(label)
        maximum = max(maximum, label)
    return tuple(sequence)


def check_gate_truth_tables() -> dict:
    result = {}
    for operator, arity in [("OR", 2), ("AND", 2), ("NOT", 1)]:
        cnf = CNF(arity, {}, [], [])
        output = cnf.gate(operator, *range(1, arity + 1))
        checked = 0
        for inputs in product((False, True), repeat=arity):
            extensions = []
            for proposed in (False, True):
                values = [False, *inputs, proposed]
                if satisfies(cnf, values):
                    extensions.append(proposed)
                checked += 1
            expected = any(inputs) if operator == "OR" else (all(inputs) if operator == "AND" else not inputs[0])
            assert extensions == [expected]
            assert output == arity + 1
        result[operator] = {"complete_truth_rows": checked, "unique_extension": True}
    return result


def check_cnf() -> list[dict]:
    results = []
    for r in range(1, RGS_MAX + 1):
        cnf = rgs_cnf(r)
        assert cnf.variables == (3 * r * r - r) // 2
        assert len(cnf.clauses) == 4 * r * r - 3 * r
        assert max(map(len, cnf.clauses)) <= 3
        expected = set(rgs_sequences(r))
        checked = None
        if r <= PRIMARY_MAX:
            checked = 1 << len(cnf.primary)
            actual = set()
            for mask in range(checked):
                values = extend_assignment(cnf, mask)
                decoded = decode_if_rgs(cnf, values, r)
                assert satisfies(cnf, values) == (decoded is not None)
                if decoded is not None:
                    actual.add(decoded)
            assert actual == expected
        for s in expected:
            mask = sum(1 << (cnf.primary[i, j] - 1) for i, j in enumerate(s, start=1))
            assert satisfies(cnf, extend_assignment(cnf, mask))
        all_assignments = None
        if r <= ALL_VARIABLES_MAX:
            all_assignments = 1 << cnf.variables
            primary_extensions = Counter()
            for mask in range(all_assignments):
                values = [False] + [bool(mask & (1 << i)) for i in range(cnf.variables)]
                if satisfies(cnf, values):
                    primary_extensions[mask & ((1 << len(cnf.primary)) - 1)] += 1
            assert set(primary_extensions.values()) == {1}
            assert len(primary_extensions) == len(expected)
        results.append({"r": r, "primary_variables": len(cnf.primary),
                        "variables": cnf.variables, "clauses": len(cnf.clauses),
                        "max_width": max(map(len, cnf.clauses)),
                        "all_primary_patterns_checked": checked,
                        "all_boolean_assignments_checked": all_assignments,
                        "rgs_satisfying_assignments_checked": len(expected)})
    return results


def add_same(cnf: CNF, i: int, j: int) -> int:
    terms = [cnf.gate("AND", cnf.primary[i, label], cnf.primary[j, label])
             for label in range(1, min(i, j) + 1)]
    result = terms[0]
    for term in terms[1:]:
        result = cnf.gate("OR", result, term)
    return result


def check_predicate_circuit() -> dict:
    r = 4
    cnf = rgs_cnf(r)
    same12 = add_same(cnf, 1, 2)
    same34 = add_same(cnf, 3, 4)
    same13 = add_same(cnf, 1, 3)
    either = cnf.gate("OR", same12, same34)
    different = cnf.gate("NOT", same13)
    output = cnf.gate("AND", either, different)
    cnf.clauses.append((output,))
    accepted = []
    for mask in range(1 << len(cnf.primary)):
        values = extend_assignment(cnf, mask)
        s = decode_if_rgs(cnf, values, r)
        semantic = s is not None and (s[0] == s[1] or s[2] == s[3]) and s[0] != s[2]
        assert satisfies(cnf, values) == semantic
        if semantic:
            accepted.append(s)
    assert len(accepted) == 5
    return {"r": r, "predicate": "(same(1,2) OR same(3,4)) AND NOT same(1,3)",
            "satisfying_partitions": len(accepted), "accepted_rgs": accepted,
            "variables": cnf.variables, "clauses": len(cnf.clauses),
            "all_primary_patterns_checked": 1 << len(cnf.primary),
            "max_width": max(map(len, cnf.clauses))}


def source_pins() -> list[dict]:
    result = []
    for filename, expected in SOURCE_BLOBS.items():
        module_name = "enterprise_math." + filename.removesuffix(".py")
        raw = Path(sys.modules[module_name].__file__).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert blob == expected, (filename, blob, expected)
        result.append({"repository": "awdawmip/enterprise-math", "commit": SOURCE_COMMIT,
                       "path": "src/enterprise_math/" + filename, "git_blob_sha1": blob})
    return result


def main() -> None:
    start = time.monotonic()
    pins = source_pins()
    gate_checks = check_gate_truth_tables()
    colors = check_rgs_and_colors()
    cnf = check_cnf()
    predicate = check_predicate_circuit()
    report = {
        "status": "PASS",
        "scope": "AUTHOR_SIDE_EXACT_FINITE_VERIFICATION_WITH_HAND_PROOF",
        "source_pins": pins,
        "import_scope": "Unchanged brc_histogram and its two exact import dependencies",
        "execution_import_mode": "ISOLATED_LOCAL_PACKAGE_SHIM" if LOCAL_VENDOR.is_dir() else "REPOSITORY_PUBLIC_PACKAGE",
        "domains": {"rgs_max_r": RGS_MAX, "color_max_r": COLOR_MAX,
                    "all_primary_max_r": PRIMARY_MAX, "all_cnf_variables_max_r": ALL_VARIABLES_MAX},
        "brc_execution": {"entrypoints": dict(BRC_CALLS),
                          "input_carrier": "Positive-rational WeightHistogram; unit-weight counting branches",
                          "count_projection_scope": "Counts only; block-count aggregation is not a same-query behavioral quotient",
                          "fiber_carrier_semantics": "Weight = colorings per logical class; coefficient = number of logical classes",
                          "branch_identity": "RGS canonical partition plus injective distinct noncurrent-color labels",
                          "observer_scope": "Equality partition and same(i,j); no allocator transition reachability",
                          "normalization_performed": False},
        "gate_truth_tables": gate_checks,
        "rgs_color_fibers": colors,
        "cnf_checks": cnf,
        "predicate_circuit": predicate,
        "totals": {"enumerated_well_formed_color_strings": sum(x["enumerated_colored_encodings"] for x in colors),
                   "rgs_sequences": sum(x["logical_classes"] for x in colors),
                   "primary_patterns": sum(x["all_primary_patterns_checked"] or 0 for x in cnf),
                   "all_cnf_boolean_assignments": sum(x["all_boolean_assignments_checked"] or 0 for x in cnf)},
        "boundaries": ["Color strings are well-formed static encodings, not proven reachable allocator states or histories.",
                       "Bell(r) counts partitions; applying it to dynamic behavioral classes consumes the source theorem's premises.",
                       "General unique extension and count preservation use the written induction, not finite testing alone.",
                       "No Lean/formal check, independent review, task acceptance, ETH speedup, or native physics claim."],
        "elapsed_seconds": round(time.monotonic() - start, 6),
    }
    (HERE / "EXACT_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": report["status"], "totals": report["totals"],
                      "r6": colors[5], "brc_calls": dict(BRC_CALLS),
                      "elapsed_seconds": report["elapsed_seconds"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
