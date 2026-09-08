"""Bounded independent consumer review; no mathematical theorem promotion."""

from __future__ import annotations

import argparse
from collections import Counter
import copy
from datetime import datetime, timezone
import hashlib
import importlib
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
import time


PREFIX = "experiments/owner_positive_support_compression_20260908/"
FROZEN = {
    PREFIX + "check_positive_support_compression.py":
        "f7e31ef40a2af4da1eaf0726068b212bb5efd66e82056ef91c8ee29581853660",
    PREFIX + "certificate.json":
        "e1d6e819678d3472acc95aa9b1655f001161dcb93a02c7e0cb47219a542e1cf5",
    PREFIX + "README.md":
        "5b6394b07d916c8bdf33b7577314938d0bb15337ceec395dac471f2a4ea1af14",
}
SLICES = tuple(combinations(range(6), 3))


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical_hex(value):
    """Make evidence hashes independent of decimal integer rendering limits."""
    if type(value) is int:
        return {"exact_integer_hex": hex(value)}
    if isinstance(value, (list, tuple)):
        return [canonical_hex(item) for item in value]
    if isinstance(value, dict):
        return {key: canonical_hex(item) for key, item in value.items()}
    return value


def value_digest(value):
    data = json.dumps(canonical_hex(value), sort_keys=True, separators=(",", ":")).encode()
    return digest(data)


def snapshot(root, pins):
    records = {}
    for path, pin in sorted(pins.items()):
        file = root.joinpath(path)
        data, stat = file.read_bytes(), file.stat()
        need(digest(data) == pin, "frozen bytes drifted: " + path)
        records[path] = {"sha256": pin, "bytes": len(data), "mtime_ns": stat.st_mtime_ns}
    return records


def aggregate(atoms, axes=None):
    result = Counter()
    for cell, weight in atoms:
        key = cell.coords if axes is None else tuple(cell.coords[a] for a in axes)
        result[key] += weight
    return dict(result)


def difference(left, right):
    return {key: value for key in left.keys() | right.keys()
            if (value := left.get(key, 0) - right.get(key, 0)) != 0}


def decode(rows, dimension):
    result = {}
    for row in rows:
        coords, mass = tuple(row["coords"]), row["numerator"]
        need(len(coords) == dimension and all(type(x) is int for x in coords), "bad coordinate row")
        need(type(mass) is int and coords not in result, "bad mass or duplicate row")
        result[coords] = mass
    return result


def nonzero(histogram):
    return {key: value for key, value in histogram.items() if value != 0}


def independent_case(module, name, mu, nu, denominator=1):
    """Compare each raw table to positive/negative populations projected separately."""
    result = module.audit_compression(name, mu, nu, denominator)
    before = difference(aggregate(mu), aggregate(nu))
    positive = {c: m for c, m in before.items() if m > 0}
    negative = {c: -m for c, m in before.items() if m < 0}
    need(decode(result["aggregated_signed_difference"], 6) == before, name + ": input ledger")
    classes = [set(c[a] for c in positive) for a in range(6)]
    sentinels = [max(values) + 1 if values else 0 for values in classes]
    expected_after = Counter()
    for coords, mass in before.items():
        target = tuple(x if x in classes[a] else sentinels[a] for a, x in enumerate(coords))
        expected_after[target] += mass
    expected_after = nonzero(dict(expected_after))
    after = decode(result["compressed_signed_difference"], 6)
    need(after == expected_after, name + ": pushforward address or mass")
    need({c: m for c, m in after.items() if m > 0} == positive, name + ": positive sites")
    P, N = sum(positive.values()), sum(negative.values())
    need((result["p"], result["P_numerator"], result["N_numerator"], result["l1_numerator"])
         == (len(positive), P, N, P + N), name + ": Jordan summary")
    carrier = 1
    for axis, values in enumerate(classes):
        carrier *= len(values) + 1
        row = result["compression"]["axes"][axis]
        need(row["positive_values"] == sorted(values) and row["external_class"] == sentinels[axis],
             name + ": axis classes")
    need(result["compression"]["carrier_cardinality"] == carrier, name + ": symbolic carrier")
    need(len(after) <= carrier <= (len(positive) + 1) ** 6, name + ": carrier bound")
    need((result["support_before"], result["support_after"], result["q_before"], result["q_after"])
         == (len(before), len(after), len(negative), sum(m < 0 for m in after.values())),
         name + ": occupied support accounting")
    need(tuple(tuple(t["axes"]) for t in result["raw_tables"]) == SLICES, name + ": twenty slices")
    norms = []
    for axes, table in zip(SLICES, result["raw_tables"]):
        # Unlike the reused helper, project the two positive populations first.
        raw_before = difference(aggregate(mu, axes), aggregate(nu, axes))
        raw_after = Counter()
        for coords, mass in expected_after.items():
            raw_after[tuple(coords[a] for a in axes)] += mass
        raw_after = nonzero(dict(raw_after))
        need(nonzero(decode(table["before"], 3)) == raw_before, name + ": raw input table")
        need(nonzero(decode(table["after"], 3)) == raw_after, name + ": raw output table")
        norm = sum(abs(m) for m in raw_before.values())
        need(table["l1_numerator"] == norm == sum(abs(m) for m in raw_after.values()),
             name + ": raw L1")
        norms.append(norm)
    need(result["D_numerator"] == sum(norms), name + ": D is the sum of twenty norms")
    for field, numerator in (("common_mass_unit", 1), ("l1_mass", P + N), ("D_mass", sum(norms))):
        need(result[field] == {"node": "DIV", "numerator": numerator,
                              "denominator": denominator, "state": "UNEVALUATED"},
             name + ": symbolic DIV identity")
    summary = {"case_id": name, "status": "PASS", "p": len(positive),
               "q_before": len(negative), "q_after": sum(m < 0 for m in after.values()),
               "support_before": len(before), "support_after": len(after), "carrier_cardinality": carrier,
               "P_numerator_hex": hex(P), "N_numerator_hex": hex(N), "D_numerator_hex": hex(sum(norms)),
               "denominator_bits": denominator.bit_length(), "twenty_raw_tables_matched": True,
               "input_populations_sha256_canonical_hex": value_digest(result["input_populations"]),
               "complete_result_sha256_canonical_hex": value_digest(result)}
    return result, norms, summary


def expect_value_error(name, action, expected):
    try:
        action()
    except ValueError as error:
        need(str(error) == expected, name + ": wrong rejection message")
        return {"case_id": name, "status": "EXPECTED_REJECTION", "message": str(error)}
    raise AssertionError(name + ": missing rejection")


def run(root):
    before_limit = sys.get_int_max_str_digits()
    frozen_before = snapshot(root, FROZEN)
    saved = json.loads(root.joinpath(PREFIX + "certificate.json").read_bytes())
    pins = saved["source_sha256"]
    need(len(pins) == 14, "fourteen dependency pins required")
    before = snapshot(root, {**pins, **FROZEN})
    argv = [sys.executable, "-B", "-X", "utf8", PREFIX + "check_positive_support_compression.py"]
    start = time.perf_counter_ns()
    replay = subprocess.run(argv, cwd=root, capture_output=True, timeout=30, check=False)
    elapsed = time.perf_counter_ns() - start
    need(replay.returncode == 0, "fresh default replay failed: " + replay.stderr.decode("utf-8", "replace"))
    replay_out = json.loads(replay.stdout)
    need(replay_out["mode"] == "EXACT_REPLAY" and replay_out["cases"] == 18
         and replay_out["raw_tables"] == 360 and replay_out["source_pins"] == 14
         and replay_out["certificate_sha256"] == FROZEN[PREFIX + "certificate.json"], "replay receipt")
    need(snapshot(root, {**pins, **FROZEN}) == before, "default replay changed source bytes or mtimes")

    need("check_positive_support_compression" not in sys.modules, "fresh review import required")
    sys.path.insert(0, str(root.joinpath(PREFIX)))
    module = importlib.import_module("check_positive_support_compression")
    need(Path(module.__file__).resolve() == root.joinpath(PREFIX + "check_positive_support_compression.py").resolve(),
         "wrong extension module")
    need(module.SOURCE_SHA256 == pins, "effective dependency pins differ")
    one, native, exact = module.one_positive, module.x6, module.exact
    need(native is one.x6 and exact is one.exact and module.SLICES is one.SLICES, "reused module identities")
    selected = {
        "one_positive.population": one.population,
        "one_positive.raw_projection": one.raw_projection,
        "one_positive.verify_joint_projection": one.verify_joint_projection,
        "native.Spatial6.__post_init__": native.Spatial6.__post_init__,
        "native.hidden_slice_coordinates": native.hidden_slice_coordinates,
        "native.from_hidden_slice_coordinates": native.from_hidden_slice_coordinates,
        "exact.division": exact.division,
        "exact.compare_divisions": exact.compare_divisions,
        "signed_brc.support_size": one.signed_brc.support_size,
        "one_positive.audit_case": one.audit_case,
    }
    expected_files = {
        "one_positive": "experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py",
        "native": "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py",
        "exact": "src/enterprise_math/exact_arithmetic.py",
        "signed_brc": "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py",
    }
    identities = {}
    for name, function in selected.items():
        expected_file = expected_files[name.split(".", 1)[0]]
        need(Path(function.__code__.co_filename).resolve() == root.joinpath(expected_file).resolve(), name + ": code origin")
        identities[name] = {"source_path": expected_file, "source_sha256": pins[expected_file],
                            "first_line": function.__code__.co_firstlineno, "module": function.__module__}
    code_names = {function.__code__: name for name, function in selected.items()}
    counts = Counter()
    allowed_exact = {"division", "__init__", "__post_init__", "_require_natural", "_require_positive"}

    def profile(frame, event, arg):
        if event == "call":
            origin, name = frame.f_globals.get("__name__", ""), frame.f_code.co_name
            need(origin != "fractions", "independent calls entered Fraction")
            if origin.startswith("enterprise_math."):
                need(origin == exact.__name__ and name in allowed_exact, "unrequested arithmetic call")
            need(origin != one.signed_brc.__name__, "new compression cases called a signed-BRC arithmetic helper")
            need(frame.f_code is not one.audit_case.__code__, "new cases invoked the p<=1 theorem consumer")
            if frame.f_code in code_names:
                counts[code_names[frame.f_code]] += 1
        elif event == "c_call":
            call = (getattr(arg, "__module__", ""), getattr(arg, "__name__", ""))
            need(call not in {("builtins", "divmod"), ("math", "sqrt"), ("math", "isqrt"),
                              ("math", "factorial")}, "unrequested quotient/root/multiplicity helper")

    need(sys.getprofile() is None, "existing profiler would be displaced")
    sys.setprofile(profile)
    try:
        cell = native.Spatial6
        positive = [cell((j - 8, j*j - 70, 2*j - 15, (-1 if j in (1, 3, 5, 7, 9, 11, 13, 15) else 1)
                          * (j + 2), 3*j - 21, 50 - j*j)) for j in range(17)]
        mu = [(q, j + 1) for j, q in enumerate(positive)]
        nu = []
        for j in range(6):
            axis = j + 1 if j < 5 else 0
            external = max(q.coords[axis] for q in positive)
            for increment, weight in ((3, j + 2), (9, j + 5)):
                coords = list(positive[j].coords)
                coords[axis] = external + increment
                nu.append((cell(tuple(coords)), weight))
        nu += [(cell((1000,) * 6), 19), (cell((2000,) * 6), 23)]
        common = [(positive[7], 31), (cell((-1000,) * 6), 13)]
        mu += common
        nu += common
        large, norms, large_summary = independent_case(module, "seventeen_post_jordan_positive_sites", mu, nu, 67)
        need(large["p"] == 17 and large["compression"]["carrier_cardinality"] == 18**6,
             "generic-p fixture did not reach its intended carrier")
        need(large["q_after"] < large["q_before"], "generic-p fixture lacks an actual negative merge")
        swapped, swapped_norms, swapped_summary = independent_case(module, "sign_swapped_populations", nu, mu, 67)
        need(norms == swapped_norms and swapped["P_numerator"] == large["N_numerator"]
             and swapped["N_numerator"] == large["P_numerator"], "sign-swap norm symmetry")
        u, v, w = cell((5, 9, -4, 0, 8, 11)), cell((-2, -3, 6, -8, 2, 14)), cell((5, 9, -4, 7, -1, 0))
        reduced, _, reduced_summary = independent_case(module, "three_mu_sites_reduce_to_one_positive",
            [(u, 2), (u, 3), (v, 5), (w, 7)], [(u, 8), (v, 5), (w, 2)], 13)
        need(reduced["p"] == 1 and reduced["D_numerator"] == 154, "post-Jordan fixture")
        B, W, denominator = 1 << 17000, (1 << 18000) + 3, (1 << 17003) + 1
        huge, _, huge_summary = independent_case(module, "p3_bigint_coordinates_weights_and_DIV",
            [(cell((-B, 5, 0, 2, -3, 7)), W), (cell((-B + 11, -9, 4, -1, 8, 0)), 11),
             (cell((-B + 19, 5, 6, 3, -4, 2)), 17)],
            [(cell((-B, 13, 0, 2, -3, 7)), 5), (cell((-B + 31, 30, 29, 28, 27, 26)), 7)], denominator)
        need(huge["p"] == 3 and huge["common_mass_unit"]["denominator"] == denominator, "large symbolic input")
        huge_summary.update({"coordinate_magnitude_bits": B.bit_length(), "largest_weight_bits": W.bit_length()})
        nonpositive, _, nonpositive_summary = independent_case(module, "all_negative_generic_support", [], nu, 67)
        need(nonpositive["p"] == 0 and nonpositive["support_after"] == 1
             and nonpositive["D_numerator"] == 20 * nonpositive["l1_numerator"], "p0 boundary")
        spec = copy.deepcopy(large["compression"])
        spec["carrier_cardinality"] += 1
        rejections = [expect_value_error("tampered_same_support_carrier_metadata",
            lambda: module.validated_compression(decode(large["aggregated_signed_difference"], 6), spec),
            "compression specification is not bound to this true Jordan positive support")]

        class ForeignSpatial(cell):
            pass

        class IntegerSubclass(int):
            pass

        rejections.append(expect_value_error("noncanonical_spatial_subclass",
            lambda: module.audit_compression("foreign", [(ForeignSpatial(), 1)], []),
            "canonical Spatial6 input required"))
        rejections.append(expect_value_error("positive_integer_subclass_weight",
            lambda: module.audit_compression("subclass_weight", [(cell(), IntegerSubclass(1))], []),
            "each population numerator must be a strictly positive integer"))
    finally:
        sys.setprofile(None)
    for name in ("one_positive.population", "one_positive.raw_projection", "one_positive.verify_joint_projection",
                 "native.hidden_slice_coordinates", "native.from_hidden_slice_coordinates", "exact.division"):
        need(counts[name] > 0, "declared exact native reuse not observed: " + name)
    need(counts["one_positive.audit_case"] == counts["signed_brc.support_size"] == 0, "unrequested theorem consumer")
    need(sys.get_int_max_str_digits() == before_limit, "global decimal rendering limit changed")
    after = snapshot(root, {**pins, **FROZEN})
    need(after == before and snapshot(root, FROZEN) == frozen_before, "protected bytes or mtimes changed")
    return {
        "schema": "OWNER_POSITIVE_SUPPORT_COMPRESSION_INDEPENDENT_REVIEW_V1",
        "status": "PASS_BOUNDED_CONSUMER_REVIEW_NO_FORMAL_ACCEPTANCE",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0],
        "executed_script_sha256": digest(Path(__file__).read_bytes()), "argv": sys.argv,
        "reviewed_freeze_manifest_sha256": "e96471b93542205d1046c1f84dfba8ae613c45d663e9004e33366928a7836833",
        "public_dependency_source_commit": "d11e10126170335cc520fb9ce809682d76aa8bfe",
        "public_compression_paper_commit": "90974735b479a6e99db769eec385b2c51a749f24",
        "reproduction_uses_exact_byte_pins_not_local_only_git_objects": True,
        "candidate_sha256": FROZEN, "dependency_sha256": pins,
        "all_seventeen_protected_file_bytes_and_mtimes_unchanged": True,
        "fresh_default_replay": {"argv": argv, "cwd": str(root), "exit_code": replay.returncode,
            "elapsed_ns": elapsed, "stdout": replay_out, "stdout_sha256": digest(replay.stdout),
            "stderr_sha256": digest(replay.stderr), "certificate_bytes_and_mtime_unchanged": True,
            "actual_recomputed_call_audit": saved["main_ledger_call_audit"]},
        "independent_cases": [large_summary, swapped_summary, reduced_summary, huge_summary, nonpositive_summary],
        "independent_rejections": rejections, "independent_raw_tables": 100,
        "actual_function_code_origins": identities,
        "independent_observed_calls_by_exact_code_object": dict(sorted(counts.items())),
        "observed_forbidden_arithmetic_calls": 0,
        "profile_scope": "Five new cases and three rejection boundaries, after pinned imports; selected code objects and observed Python/C boundaries only.",
        "decimal_integer_rendering_limit_before_and_after": before_limit,
        "limits": {"carrier_enumerated": False, "random_or_exhaustive_search": False,
            "new_mathematical_theorem_proved_by_execution": False, "all_coordinate_subset_tables_executed": False,
            "twenty_raw_three_axis_tables_per_case_checked": True,
            "transitive_or_import_time_arithmetic_compliance_claimed": False,
            "general_bigint_decimal_json_serialization_promised": False,
            "formal_task_result_claim_catalog_or_foundation_change": False},
        "global_knowledge_sync": "main@eb09a0a / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    result = run(args.repo.resolve())
    target = Path(__file__).with_name("review.json")
    target.write_bytes((json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({"status": result["status"], "independent_cases": len(result["independent_cases"]),
                      "independent_raw_tables": result["independent_raw_tables"],
                      "rejections": len(result["independent_rejections"]),
                      "review_json_sha256": digest(target.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
