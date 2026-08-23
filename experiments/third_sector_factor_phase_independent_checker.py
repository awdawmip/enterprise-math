#!/usr/bin/env python3
"""Independent exact checker for the blind third-sector factor-phase task.

The three mathematical modules are deliberately separate:

1. ``direct_cells`` enumerates square cells without factoring ``n``.
2. ``factor_driven_records`` factors ``n`` and constructs Gaussian products
   without consulting direct enumeration.
3. ``reverse_recovery`` uses only two supplied primitive cells, their norm,
   integer arithmetic, and gcd.  Factorization is used only by the outer
   validator, never inside the recovery algorithm.

Running this file writes the normalized CSV corpus and JSONL evidence stream
next to the research report and exits nonzero on any retained-claim mismatch.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


Cell = Tuple[int, int]  # canonical convention: a >= b >= 0
Gaussian = Tuple[int, int]

DEFAULT_FORWARD_MAX = 4096
DEFAULT_REVERSE_MAX = 20000


def factorint(n: int) -> Dict[int, int]:
    """Deterministic trial-division factorization for the declared finite run."""
    if n < 1:
        raise ValueError("factorint requires n >= 1")
    out: Dict[int, int] = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors_count_from_factorization(factors: Dict[int, int]) -> int:
    value = 1
    for exponent in factors.values():
        value *= exponent + 1
    return value


def direct_cells(n: int) -> Tuple[Cell, ...]:
    """Module 1: direct, factorization-free enumeration of a >= b >= 0."""
    if n < 0:
        return ()
    cells: List[Cell] = []
    for b in range(math.isqrt(n // 2) + 1):
        a2 = n - b * b
        a = math.isqrt(a2)
        if a >= b and a * a == a2:
            cells.append((a, b))
    # The module freezes its own normalized output before comparison.
    return tuple(sorted(cells))


def gaussian_mul(z: Gaussian, w: Gaussian) -> Gaussian:
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gaussian_pow(z: Gaussian, exponent: int) -> Gaussian:
    result = (1, 0)
    base = z
    e = exponent
    while e:
        if e & 1:
            result = gaussian_mul(result, base)
        base = gaussian_mul(base, base)
        e >>= 1
    return result


def normalize_cell(z: Gaussian) -> Cell:
    x, y = abs(z[0]), abs(z[1])
    return (x, y) if x >= y else (y, x)


def canonical_split_prime(p: int) -> Gaussian:
    """Return the unique u+iv with u>v>0 and u^2+v^2=p."""
    if p <= 2 or p % 4 != 1:
        raise ValueError(f"not an odd split prime: {p}")
    for v in range(1, math.isqrt(p // 2) + 1):
        u2 = p - v * v
        u = math.isqrt(u2)
        if u > v and u * u == u2:
            return (u, v)
    raise ArithmeticError(f"no canonical two-square decomposition found for {p}")


def split_core_data(n: int) -> Dict[str, object]:
    """Return the canonical arithmetic data used by the forward theorem."""
    if n < 1:
        raise ValueError("split_core_data requires n >= 1")
    factors = factorint(n)
    alpha = factors.get(2, 0)
    split: List[Tuple[int, int]] = []
    inert: List[Tuple[int, int]] = []
    for p, exponent in sorted(factors.items()):
        if p == 2:
            continue
        if p % 4 == 1:
            split.append((p, exponent))
        else:
            inert.append((p, exponent))
    admissible = all(exponent % 2 == 0 for _, exponent in inert)
    core = math.prod(p**exponent for p, exponent in split)
    base_scale = 2 ** (alpha // 2) * math.prod(
        p ** (exponent // 2) for p, exponent in inert
    )
    return {
        "factors": factors,
        "alpha": alpha,
        "split": tuple(split),
        "inert": tuple(inert),
        "admissible": admissible,
        "core": core,
        "base_scale": base_scale,
    }


def factor_driven_records(
    n: int, *, admit_odd_inert: bool = False
) -> Tuple[Dict[str, object], ...]:
    """Module 2: generate quotient representatives from factor choices.

    A record is retained exactly when d <= C/d, thereby choosing one element
    from each complement orbit d <-> C/d.  ``admit_odd_inert`` is a deliberate
    negative control and is never used for a retained claim.
    """
    if n == 0:
        return (
            {
                "n": 0,
                "d": None,
                "complement": None,
                "cell": (0, 0),
                "base_scale": 0,
                "gcd_formula": 0,
                "fixed": True,
                "negative_control": False,
            },
        )
    if n < 0:
        return ()
    data = split_core_data(n)
    if not data["admissible"] and not admit_odd_inert:
        return ()

    alpha = int(data["alpha"])
    split = list(data["split"])
    core = int(data["core"])
    base_scale = int(data["base_scale"])
    # For the negative inert control, floor(exponent/2) silently discards the
    # forbidden residual inert prime.  The resulting norm error is intentional.
    base: Gaussian = (base_scale, 0)
    if alpha % 2:
        base = gaussian_mul(base, (1, 1))

    records: List[Dict[str, object]] = []

    def visit(index: int, d: int, z: Gaussian) -> None:
        if index == len(split):
            complement = core // d
            if d <= complement:
                cell = normalize_cell(z)
                records.append(
                    {
                        "n": n,
                        "d": d,
                        "complement": complement,
                        "cell": cell,
                        "base_scale": base_scale,
                        "gcd_formula": base_scale * math.gcd(d, complement),
                        "fixed": d == complement,
                        "negative_control": bool(admit_odd_inert and not data["admissible"]),
                    }
                )
            return

        p, exponent = split[index]
        pi = canonical_split_prime(p)
        pi_bar = (pi[0], -pi[1])
        for k in range(exponent + 1):
            local = gaussian_mul(
                gaussian_pow(pi, k), gaussian_pow(pi_bar, exponent - k)
            )
            visit(index + 1, d * (p**k), gaussian_mul(z, local))

    visit(0, 1, base)
    records.sort(key=lambda row: (row["cell"], row["d"]))
    return tuple(records)


def factor_driven_cells(n: int) -> Tuple[Cell, ...]:
    return tuple(sorted(row["cell"] for row in factor_driven_records(n)))


def expected_unordered_count(n: int) -> int:
    if n == 0:
        return 1
    data = split_core_data(n)
    if not data["admissible"]:
        return 0
    split_factors = {p: e for p, e in data["split"]}
    choice_count = divisors_count_from_factorization(split_factors)
    fixed = int(all(e % 2 == 0 for e in split_factors.values()))
    return (choice_count + fixed) // 2


def is_primitive(cell: Cell) -> bool:
    return math.gcd(cell[0], cell[1]) == 1


def reverse_recovery(
    n: int, first: Cell, second: Cell, *, omit_two_adic_normalization: bool = False
) -> Dict[str, object]:
    """Module 3: recover a complementary factor pair using gcds only.

    This function intentionally contains no call to ``factorint``.
    """
    a, b = first
    c, d = second
    if first == second:
        raise ValueError("reverse recovery requires two distinct quotient cells")
    if a * a + b * b != n or c * c + d * d != n:
        raise ValueError("input cells do not have the declared common norm")
    if not is_primitive(first) or not is_primitive(second):
        raise ValueError("retained reverse theorem requires primitive cells")

    tau = 2 if n % 2 == 0 else 1
    denominator = 1 if omit_two_adic_normalization else tau
    core = n if omit_two_adic_normalization else n // tau
    raw = {
        "ac_plus_bd": a * c + b * d,
        "ac_minus_bd": a * c - b * d,
        "ad_plus_bc": a * d + b * c,
        "ad_minus_bc": a * d - b * c,
    }
    if any(value % denominator for value in raw.values()):
        raise ArithmeticError("bilinear term is not divisible by parity denominator")
    normalized = {name: value // denominator for name, value in raw.items()}
    gcds = {name: math.gcd(core, abs(value)) for name, value in normalized.items()}

    same = gcds["ac_plus_bd"]
    different = gcds["ac_minus_bd"]
    pair_consistent = (
        same == gcds["ad_minus_bc"]
        and different == gcds["ad_plus_bc"]
    )
    return {
        "n": n,
        "first": first,
        "second": second,
        "tau": tau,
        "denominator": denominator,
        "core": core,
        "raw": raw,
        "normalized": normalized,
        "gcds": gcds,
        "factor_a": same,
        "factor_b": different,
        "pair_consistent": pair_consistent,
        "product_ok": same * different == core,
        "coprime_ok": math.gcd(same, different) == 1,
        "nontrivial": 1 < same < core and 1 < different < core,
    }


def canonical_cell_map_hash(cell_map: Dict[int, Sequence[Cell]]) -> str:
    digest = hashlib.sha256()
    for n in sorted(cell_map):
        payload = {"n": n, "cells": [list(cell) for cell in cell_map[n]]}
        digest.update(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def canonical_json_hash(rows: Iterable[Dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_validation(forward_max: int, reverse_max: int) -> Dict[str, object]:
    direct_map: Dict[int, Tuple[Cell, ...]] = {}
    factor_map: Dict[int, Tuple[Cell, ...]] = {}
    forward_mismatches: List[Dict[str, object]] = []
    count_mismatches: List[Dict[str, object]] = []
    scale_mismatches: List[Dict[str, object]] = []
    injectivity_mismatches: List[Dict[str, object]] = []
    fixed_point_mismatches: List[Dict[str, object]] = []
    forward_rows: List[Dict[str, object]] = []

    for n in range(forward_max + 1):
        direct = direct_cells(n)
        records = factor_driven_records(n)
        generated = tuple(sorted(row["cell"] for row in records))
        direct_map[n] = direct
        factor_map[n] = generated
        if direct != generated:
            forward_mismatches.append(
                {"n": n, "direct": list(direct), "factor": list(generated)}
            )
        expected_count = expected_unordered_count(n)
        if len(direct) != expected_count:
            count_mismatches.append(
                {"n": n, "actual": len(direct), "expected": expected_count}
            )
        if len(set(generated)) != len(generated):
            injectivity_mismatches.append({"n": n, "records": list(records)})

        for record in records:
            cell = record["cell"]
            gcd_actual = math.gcd(cell[0], cell[1])
            if gcd_actual != record["gcd_formula"]:
                scale_mismatches.append(
                    {
                        "n": n,
                        "d": record["d"],
                        "cell": cell,
                        "actual": gcd_actual,
                        "formula": record["gcd_formula"],
                    }
                )
            if n > 0 and record["fixed"]:
                alpha = int(split_core_data(n)["alpha"])
                expected_kind = "axis" if alpha % 2 == 0 else "diagonal"
                actual_kind = "axis" if cell[1] == 0 else "diagonal" if cell[0] == cell[1] else "generic"
                if actual_kind != expected_kind:
                    fixed_point_mismatches.append(
                        {"n": n, "cell": cell, "expected": expected_kind, "actual": actual_kind}
                    )
            forward_rows.append(
                {
                    "record_type": "forward_cell",
                    "n": n,
                    "a": cell[0],
                    "b": cell[1],
                    "c": "",
                    "d_coord": "",
                    "factor_d": "" if record["d"] is None else record["d"],
                    "factor_complement": "" if record["complement"] is None else record["complement"],
                    "base_scale": record["base_scale"],
                    "gcd_actual": gcd_actual,
                    "gcd_formula": record["gcd_formula"],
                    "primitive": int(is_primitive(cell)),
                    "recovered_a": "",
                    "recovered_b": "",
                    "recovery_core": "",
                    "status": "MATCH" if cell in direct else "MISMATCH",
                }
            )
        if not records:
            forward_rows.append(
                {
                    "record_type": "forward_empty",
                    "n": n,
                    "a": "",
                    "b": "",
                    "c": "",
                    "d_coord": "",
                    "factor_d": "",
                    "factor_complement": "",
                    "base_scale": "",
                    "gcd_actual": "",
                    "gcd_formula": "",
                    "primitive": "",
                    "recovered_a": "",
                    "recovered_b": "",
                    "recovery_core": "",
                    "status": "MATCH" if not direct else "MISMATCH",
                }
            )

    reverse_rows_raw: List[Dict[str, object]] = []
    reverse_corpus_rows: List[Dict[str, object]] = []
    reverse_failures: List[Dict[str, object]] = []
    reverse_pair_count = 0
    two_adic_control: Dict[str, object] | None = None

    for n in range(1, reverse_max + 1):
        primitive = tuple(cell for cell in direct_cells(n) if is_primitive(cell))
        for first, second in itertools.combinations(primitive, 2):
            reverse_pair_count += 1
            recovered = reverse_recovery(n, first, second)
            compact = {
                "n": n,
                "first": list(first),
                "second": list(second),
                "core": recovered["core"],
                "factor_a": recovered["factor_a"],
                "factor_b": recovered["factor_b"],
                "pair_consistent": recovered["pair_consistent"],
                "product_ok": recovered["product_ok"],
                "coprime_ok": recovered["coprime_ok"],
                "nontrivial": recovered["nontrivial"],
            }
            reverse_rows_raw.append(compact)
            if not all(
                compact[key]
                for key in ("pair_consistent", "product_ok", "coprime_ok", "nontrivial")
            ):
                reverse_failures.append(compact)
            reverse_corpus_rows.append(
                {
                    "record_type": "reverse_pair",
                    "n": n,
                    "a": first[0],
                    "b": first[1],
                    "c": second[0],
                    "d_coord": second[1],
                    "factor_d": "",
                    "factor_complement": "",
                    "base_scale": "",
                    "gcd_actual": "",
                    "gcd_formula": "",
                    "primitive": 1,
                    "recovered_a": recovered["factor_a"],
                    "recovered_b": recovered["factor_b"],
                    "recovery_core": recovered["core"],
                    "status": "PASS" if compact not in reverse_failures else "FAIL",
                }
            )
            if n % 2 == 0 and two_adic_control is None:
                flawed = reverse_recovery(
                    n, first, second, omit_two_adic_normalization=True
                )
                flawed_pass = bool(
                    flawed["pair_consistent"]
                    and flawed["product_ok"]
                    and flawed["coprime_ok"]
                    and flawed["nontrivial"]
                )
                two_adic_control = {
                    "n": n,
                    "first": list(first),
                    "second": list(second),
                    "correct_core": recovered["core"],
                    "correct_factors": [recovered["factor_a"], recovered["factor_b"]],
                    "flawed_core": flawed["core"],
                    "flawed_factors": [flawed["factor_a"], flawed["factor_b"]],
                    "flawed_pass": flawed_pass,
                }

    inert_control: Dict[str, object] | None = None
    for n in range(1, forward_max + 1):
        data = split_core_data(n)
        if data["admissible"]:
            continue
        flawed = tuple(
            sorted(row["cell"] for row in factor_driven_records(n, admit_odd_inert=True))
        )
        actual = direct_cells(n)
        if flawed != actual:
            inert_control = {
                "n": n,
                "direct": [list(cell) for cell in actual],
                "flawed_admit_odd_inert": [list(cell) for cell in flawed],
                "mismatch": True,
            }
            break

    if two_adic_control is None:
        two_adic_control = {"error": "range contained no even primitive pair"}
    if inert_control is None:
        inert_control = {"error": "range contained no odd-inert negative control"}

    positive_failure_count = sum(
        len(items)
        for items in (
            forward_mismatches,
            count_mismatches,
            scale_mismatches,
            injectivity_mismatches,
            fixed_point_mismatches,
            reverse_failures,
        )
    )
    negative_controls_pass = (
        two_adic_control.get("flawed_pass") is False
        and inert_control.get("mismatch") is True
    )

    return {
        "config": {
            "forward_range": [0, forward_max],
            "reverse_range": [1, reverse_max],
            "cell_convention": "a>=b>=0",
            "source_commit": "12725505c636449df7dd913ac06e581bf418b89c",
            "locked_packet_ref": "87f32a3df7625b76a85944769be82f44e122bc7e",
            "locked_packet_blob": "f755dffbf56af9bf179349105c7107bb998c30b4",
        },
        "forward": {
            "direct_hash": canonical_cell_map_hash(direct_map),
            "factor_hash": canonical_cell_map_hash(factor_map),
            "mismatches": forward_mismatches,
            "count_mismatches": count_mismatches,
            "scale_mismatches": scale_mismatches,
            "injectivity_mismatches": injectivity_mismatches,
            "fixed_point_mismatches": fixed_point_mismatches,
        },
        "reverse": {
            "pair_count": reverse_pair_count,
            "hash": canonical_json_hash(reverse_rows_raw),
            "failures": reverse_failures,
        },
        "negative_controls": {
            "remove_two_adic_normalization": two_adic_control,
            "admit_odd_inert_exponent": inert_control,
            "pass": negative_controls_pass,
        },
        "positive_failure_count": positive_failure_count,
        "pass": positive_failure_count == 0 and negative_controls_pass,
        "corpus_rows": forward_rows + reverse_corpus_rows,
    }


def write_artifacts(root: Path, result: Dict[str, object]) -> None:
    corpus_path = root / "research_output" / "THIRD_SECTOR_FACTOR_PHASE_TEST_CORPUS_20260823.csv"
    evidence_path = (
        root
        / "research_output"
        / "evidence"
        / "THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.jsonl"
    )
    corpus_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.parent.mkdir(parents=True, exist_ok=True)

    rows = result["corpus_rows"]
    fieldnames = [
        "record_type",
        "n",
        "a",
        "b",
        "c",
        "d_coord",
        "factor_d",
        "factor_complement",
        "base_scale",
        "gcd_actual",
        "gcd_formula",
        "primitive",
        "recovered_a",
        "recovered_b",
        "recovery_core",
        "status",
    ]
    with corpus_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    evidence_events = [
        {"event": "run_config", **result["config"]},
        {
            "event": "forward_validation",
            **result["forward"],
            "mismatch_count": len(result["forward"]["mismatches"]),
        },
        {"event": "reverse_validation", **result["reverse"]},
        {"event": "negative_controls", **result["negative_controls"]},
        {
            "event": "terminal_verdict",
            "pass": result["pass"],
            "positive_failure_count": result["positive_failure_count"],
            "classification_if_proofs_frozen": "FULL_BIDIRECTIONAL_BRIDGE_INDEPENDENTLY_RECONSTRUCTED",
        },
    ]
    freeze_artifacts = {
        "report": root / "research_output" / "THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_20260823.md",
        "reducer": root / "research_output" / "reducer_results" / "THIRD_SECTOR_FACTOR_PHASE_INDEPENDENT_RECONSTRUCTION_REDUCER_20260823.md",
        "checker": root / "experiments" / "third_sector_factor_phase_independent_checker.py",
        "corpus": corpus_path,
        "quotient_dictionary": root / "research_output" / "THIRD_SECTOR_FACTOR_PHASE_QUOTIENT_DICTIONARY_20260823.md",
    }
    if all(path.is_file() for path in freeze_artifacts.values()):
        evidence_events.append(
            {
                "event": "independent_package_freeze",
                "source_commit": result["config"]["source_commit"],
                "locked_packet_ref": result["config"]["locked_packet_ref"],
                "locked_packet_blob": result["config"]["locked_packet_blob"],
                "source_comparison_performed": False,
                "artifact_sha256": {
                    name: file_sha256(path) for name, path in freeze_artifacts.items()
                },
            }
        )
    with evidence_path.open("w", encoding="utf-8", newline="\n") as handle:
        for event in evidence_events:
            handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")))
            handle.write("\n")


def public_summary(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "config": result["config"],
        "direct_hash": result["forward"]["direct_hash"],
        "factor_hash": result["forward"]["factor_hash"],
        "forward_mismatch_count": len(result["forward"]["mismatches"]),
        "count_mismatch_count": len(result["forward"]["count_mismatches"]),
        "scale_mismatch_count": len(result["forward"]["scale_mismatches"]),
        "injectivity_mismatch_count": len(result["forward"]["injectivity_mismatches"]),
        "fixed_point_mismatch_count": len(result["forward"]["fixed_point_mismatches"]),
        "reverse_pair_count": result["reverse"]["pair_count"],
        "reverse_hash": result["reverse"]["hash"],
        "reverse_failure_count": len(result["reverse"]["failures"]),
        "negative_controls": result["negative_controls"],
        "pass": result["pass"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forward-max", type=int, default=DEFAULT_FORWARD_MAX)
    parser.add_argument("--reverse-max", type=int, default=DEFAULT_REVERSE_MAX)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="artifact root (defaults to the lane checkout root)",
    )
    args = parser.parse_args()
    result = run_validation(args.forward_max, args.reverse_max)
    write_artifacts(args.root.resolve(), result)
    print(json.dumps(public_summary(result), indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
