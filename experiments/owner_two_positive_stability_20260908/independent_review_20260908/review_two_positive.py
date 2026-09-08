"""Bounded independent audit; no author source mutation or theorem promotion."""
from __future__ import annotations

from copy import deepcopy
import argparse
import hashlib
from itertools import combinations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
OUT: Path
INPUT_METADATA = PACKAGE.joinpath("author_input_pins.json")
EXPECTED_INPUT_METADATA = "57a90c8aa99f22d51cbb8bd905cf9700900ecdb4f56b081cacaf8d713841548c"
EXPECTED_MANIFEST = "ccfdfc7365685e5e4270ca7cd9d48802993f7e627f07914abe087f68399a7105"
TARGET = "experiments/owner_two_positive_stability_20260908/check_two_positive_stability.py"
SLICES = tuple(combinations(range(6), 3))


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, data):
    path.write_bytes((json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode())


def protected_snapshot(paths):
    return {p: {"sha256": sha(ROOT.joinpath(p).read_bytes()),
                "mtime_ns": ROOT.joinpath(p).stat().st_mtime_ns} for p in paths}


def oracle(mu, nu):
    """Literal point/address accumulation, without any consumer projection code."""
    signed = {}
    for rows, sign in ((mu, 1), (nu, -1)):
        for point, weight in rows:
            signed[point] = signed.get(point, 0) + sign * weight
    signed = {p: w for p, w in signed.items() if w}
    positive = {p: w for p, w in signed.items() if w > 0}
    negative = {p: -w for p, w in signed.items() if w < 0}
    tables = []
    for axes in SLICES:
        table = {}
        for point, weight in signed.items():
            address = tuple(point[i] for i in axes)
            table[address] = table.get(address, 0) + weight
        tables.append(table)
    P, N = sum(positive.values()), sum(negative.values())
    D = sum(sum(abs(w) for w in table.values()) for table in tables)
    return signed, positive, negative, tables, P, N, P + N, D


class OnePass:
    def __init__(self, rows, cell):
        self.rows, self.cell, self.iterations = rows, cell, 0

    def __iter__(self):
        self.iterations += 1
        require(self.iterations == 1, "input population iterated more than once")
        return ((self.cell(point), weight) for point, weight in self.rows)


def expected_div(numerator, denominator):
    return {"node": "DIV", "numerator": numerator, "denominator": denominator,
            "state": "UNEVALUATED"}


def audit_case(c, name, mu, nu, denominator, expected, expected_sharp, branch, observed):
    raw = oracle(mu, nu)
    difference, positive, negative, tables, P, N, M, D = raw
    require((P, N, M, D) == expected, "independent hand count mismatch: " + name)
    observed["current_p"] = len(positive)
    left, right = OnePass(mu, c.x6.Spatial6), OnePass(nu, c.x6.Spatial6)
    result = c.audit_two_positive_stability(name, left, right, denominator)
    require(left.iterations == right.iterations == 1, "one-pass population boundary")
    require((result["P_numerator"], result["N_numerator"], result["l1_numerator"], result["D_numerator"])
            == expected, "public scalar mismatch: " + name)
    require(result["p"] == len(positive) and result["q"] == len(negative), "Jordan support mismatch")
    require(result["sharp_nonzero"] is expected_sharp, "sharpness mismatch")
    require(result["proof_branch"]["kind"] == branch, "wrong proof branch")
    require(result["bound_gap"] == D - 4 * M and D >= 4 * M, "stability bound mismatch")
    require(result["equal_total_mass"] == (P == N), "equal mass must use Jordan totals")
    require(result["zero_difference"] == (M == 0), "zero flag mismatch")
    require(result["common_mass_unit"] == expected_div(1, denominator), "unit DIV changed")
    require(result["l1_mass"] == expected_div(M, denominator), "mass DIV reduced")
    require(result["D_mass"] == expected_div(D, denominator), "D DIV reduced")
    require(result["ratio"] == (expected_div(M, D) if M else None), "ratio literal or zero boundary")
    require(result["bound_constant"] == expected_div(1, 4), "bound DIV changed")
    require([tuple(t["axes"]) for t in result["raw_tables"]] == list(SLICES), "all twenty ordered raw tables")
    for axes, expected_table, actual in zip(SLICES, tables, result["raw_tables"]):
        actual_table = {tuple(r["raw_address"]): r["numerator"] for r in actual["rows"]}
        require(len(actual_table) == len(actual["rows"]), "duplicate reported raw address")
        require(actual_table == expected_table, "independent raw address or mass mismatch")
        require(actual["l1_numerator"] == sum(abs(w) for w in expected_table.values()), "independent raw norm")
        require(actual["joint_roundtrip_verified"] is True, "joint roundtrip marker")
        for row in actual["rows"]:
            address = row["raw_address"]
            require(row["common_offset"] == min(address), "per-slice common offset")
            require(row["joint_can3_address"] == [v - min(address) for v in address], "can3 component")
        if "dual_terms" in actual:
            for term in actual["dual_terms"]:
                require(term["gap"] == abs(term["h"]) - term["b"] * term["h"] >= 0, "dual term gap")
    if branch == "FOUR_H_SIXTEEN_L_DUAL":
        b = result["proof_branch"]
        require(b["table_gap_sum"] + b["negative_gap_sum"] == D - 4 * M, "complete dual gap")
    observed["cases"].append({"name": name, "p": len(positive), "P": P, "N": N, "M": M, "D": D,
                              "sharp": expected_sharp, "branch": branch, "tables_checked": len(tables),
                              "input_iterations": [left.iterations, right.iterations]})
    return result, raw


def rejection(log, name, action, exception, message_part):
    try:
        action()
    except exception as error:
        require(message_part in str(error), name + ": wrong rejection path: " + str(error))
        log.append({"name": name, "exception": type(error).__name__, "message": str(error)})
    else:
        raise AssertionError(name + ": mutation or invalid input was accepted")


def main():
    metadata_bytes = INPUT_METADATA.read_bytes()
    require(sha(metadata_bytes) == EXPECTED_INPUT_METADATA, "bundled input pin metadata drift")
    manifest = json.loads(metadata_bytes)
    require(manifest["author_manifest_sha256"] == EXPECTED_MANIFEST, "author manifest provenance drift")
    pins = dict(manifest["sources_sha256"])
    for path, row in manifest["files"].items():
        pins[path] = row["sha256"]
        require(ROOT.joinpath(path).stat().st_size == row["bytes"], "frozen file size drift")
    before = protected_snapshot(pins)
    require({p: r["sha256"] for p, r in before.items()} == pins, "protected source drift")
    write_json(OUT.joinpath("before.json"), before)
    sys.path.insert(0, str(ROOT.joinpath(TARGET).parent))
    import check_two_positive_stability as c
    require(Path(c.__file__).resolve() == ROOT.joinpath(TARGET).resolve(), "canonical consumer module")
    require(c.x6 is c.one_positive.x6 and c.exact is c.one_positive.exact, "canonical types diverged")
    require(c.__all__ == ["audit_two_positive_stability"], "public API scope")
    observed = {"cases": [], "rejections": [], "current_p": None, "calls": {}, "forbidden_calls": []}
    functions = {"population": c.one_positive.population, "raw_projection": c.one_positive.raw_projection,
                 "joint_projection": c.one_positive.verify_joint_projection, "old_boundary": c.one_positive.audit_case,
                 "Spatial6_init": c.x6.Spatial6.__post_init__, "native_slice": c.x6.hidden_slice_coordinates,
                 "native_restore": c.x6.from_hidden_slice_coordinates, "DIV": c.exact.division}
    codes = {label: f.__code__ for label, f in functions.items()}
    allowed_exact = {"division", "compare_divisions", "__init__", "__post_init__", "_require_natural", "_require_positive"}

    def profile(frame, event, arg):
        if event == "call":
            module, name = frame.f_globals.get("__name__", ""), frame.f_code.co_name
            forbidden = module == "fractions" or (module.startswith("enterprise_math.") and
                        not (module == c.exact.__name__ and name in allowed_exact))
            if forbidden:
                observed["forbidden_calls"].append(module + "." + name)
                raise AssertionError("unexpected evaluated arithmetic call")
            for label, code in codes.items():
                if frame.f_code is code:
                    observed["calls"][label] = observed["calls"].get(label, 0) + 1
                    if label == "old_boundary":
                        require(observed["current_p"] <= 1, "old p1 auditor entered on p2")
        elif event == "c_call":
            pair = (getattr(arg, "__module__", ""), getattr(arg, "__name__", ""))
            require(pair not in {("builtins", "divmod"), ("math", "sqrt"), ("math", "isqrt"), ("math", "factorial")},
                    "unexpected quotient/root/multiplicity evaluation")

    require(sys.getprofile() is None, "existing profiler must not be displaced")
    results = []
    sys.setprofile(profile)
    try:
        u, v = (-4, 6, -2, 9, 3, -11), (8, 6, -2, 9, 3, 7)
        r, s, shared = (8, 6, -2, 9, 3, -11), (-4, 6, -2, 9, 3, 7), (2, -3, 5, -7, 11, -13)
        W = (1 << 2052) + 3
        cases = [
            ("split_generators_cancel_bigint_rectangle", [(u, W - 1), (u, 1), (v, W), (shared, 13), (r, 2)],
             [(r, W + 2), (s, W), (shared, 13)], 4 * W, (2 * W, 2 * W, 4 * W, 16 * W), True, "FOUR_H_SIXTEEN_L_DUAL"),
            ("balanced_unequal_corners", [(u, 2), (v, 4)], [(r, 3), (s, 3)], 6, (6, 6, 12, 72), False, "FOUR_H_SIXTEEN_L_DUAL"),
            ("d1_third_endpoint_negative_excess", [(u, 2), (r, 1)], [((20, 6, -2, 9, 3, -11), 7)],
             9, (3, 7, 10, 140), False, "AVOIDING_TABLE_COUNT"),
            ("d4_two_endpoint_mix", [((0, 0, 0, 0, 5, -3), 2), ((2, 3, 4, 6, 5, -3), 3)],
             [((2, 0, 4, 0, 5, -3), 5)], 7, (5, 5, 10, 160), False, "AVOIDING_TABLE_COUNT"),
            ("d6_can3_only_collapse", [((-2,) * 6, 3), ((5,) * 6, 4)], [((1,) * 6, 7)],
             14, (7, 7, 14, 280), False, "AVOIDING_TABLE_COUNT"),
            ("p1_cancellation_at_positive_site", [(u, 5)], [(u, 3), ((-4, 6, -2, 9, 3, -12), 2)],
             8, (2, 2, 4, 40), False, "REUSED_P_LE_1_BOUNDARY"),
            ("p0_after_shared_cancellation", [(u, 4)], [(u, 9)], 5, (0, 5, 5, 100), False, "REUSED_P_LE_1_BOUNDARY"),
            ("zero_after_duplicate_cancellation", [(u, 2), (u, 3)], [(u, 5)], 2, (0, 0, 0, 0), False, "REUSED_P_LE_1_BOUNDARY"),
            ("p2_no_negative_population", [(u, 7), (v, 3)], [], 10, (10, 0, 10, 200), False, "FOUR_H_SIXTEEN_L_DUAL"),
        ]
        for args in cases:
            results.append(audit_case(c, *args, observed))
        require(W.bit_length() == 2053, "large positive numerator boundary")
        rectangle, (difference, positive, negative, _, _, _, M, D) = results[0]
        require(rectangle["rectangle"]["different_axes"] == [0, 5], "original axis labels")
        require(rectangle["rectangle"]["common_corner_numerator"] == W, "original corner mass")
        require(len(rectangle["cell_cancellations"]) == 2, "cancellation ledger")
        diagonal = results[4][0]
        for table in diagonal["raw_tables"]:
            collapsed = {}
            for row in table["rows"]:
                key = tuple(row["joint_can3_address"])
                collapsed[key] = collapsed.get(key, 0) + row["numerator"]
            require(sum(abs(w) for w in collapsed.values()) == 0 and table["l1_numerator"] == 14,
                    "can3-alone must lose the actual raw marginal")
        # New mutations target completeness and retained offsets, not only a scalar norm.
        raw_mutations = []
        t = deepcopy(rectangle["raw_tables"]); t.pop(); raw_mutations.append(("missing_twentieth_table", t, "set or order"))
        t = deepcopy(rectangle["raw_tables"]); t[1]["axes"] = t[0]["axes"]; raw_mutations.append(("duplicate_axes", t, "set or order"))
        t = deepcopy(rectangle["raw_tables"]); t[0]["rows"][0]["common_offset"] += 1; raw_mutations.append(("wrong_retained_offset", t, "raw table rows"))
        t = deepcopy(rectangle["raw_tables"]); t[0]["rows"][0]["joint_can3_address"][0] += 1; raw_mutations.append(("wrong_can3_component", t, "raw table rows"))
        t = deepcopy(rectangle["raw_tables"]); t[0]["rows"][0]["raw_address"] = [n + 1 for n in t[0]["rows"][0]["raw_address"]]; raw_mutations.append(("diagonal_shift_preserves_can3_but_changes_raw", t, "raw table rows"))
        t = deepcopy(rectangle["raw_tables"]); t[0]["l1_numerator"] += 1; raw_mutations.append(("changed_raw_norm", t, "raw table L1"))
        t = deepcopy(rectangle["raw_tables"]); zero = next(x for x in t if x["l1_numerator"] == 0); zero["rows"].pop(); raw_mutations.append(("discard_explicit_zero_address", t, "raw table rows"))
        for name, tables, message in raw_mutations:
            rejection(observed["rejections"], name, lambda tables=tables: c._verify_raw_tables(difference, tables), AssertionError, message)
        wrong = deepcopy(rectangle["rectangle"])
        wrong["negative_cross_corners"][0] = [n + 1 for n in wrong["negative_cross_corners"][0]]
        rejection(observed["rejections"], "false_original_corner_from_can3", lambda: c._check_equality_claim(positive, negative, M, D, True, wrong), AssertionError, "original Jordan coordinates")
        wrong = deepcopy(rectangle["rectangle"]); wrong["common_corner_numerator"] = 1
        rejection(observed["rejections"], "false_mass_normalization", lambda: c._check_equality_claim(positive, negative, M, D, True, wrong), AssertionError, "original Jordan coordinates")
        near, (_, pp, nn, _, _, _, mm, dd) = results[1]
        rejection(observed["rejections"], "support_only_false_sharp", lambda: c._check_equality_claim(pp, nn, mm, dd, True, rectangle["rectangle"]), AssertionError, "sharp flag")
        origin = c.x6.Spatial6()

        class IntSubclass(int):
            pass

        class CellSubclass(c.x6.Spatial6):
            pass

        for name, value in (("boolean_denominator", True), ("subclass_denominator", IntSubclass(3)), ("string_denominator", "3")):
            rejection(observed["rejections"], name, lambda value=value: c.audit_two_positive_stability(name, [(origin, 1)], [], value), ValueError, "common denominator")
        for name, value in (("boolean_weight", True), ("subclass_weight", IntSubclass(2)), ("negative_weight", -2)):
            rejection(observed["rejections"], name, lambda value=value: c.audit_two_positive_stability(name, [(origin, value)], []), ValueError, "population numerator")
        rejection(observed["rejections"], "cell_subclass", lambda: c.audit_two_positive_stability("bad", [(CellSubclass(), 1)], []), ValueError, "canonical Spatial6")
        rejection(observed["rejections"], "true_p3_after_aggregation", lambda: c.audit_two_positive_stability("p3", [(origin, 1), (origin.step(1), 1), (origin.step(5), 1)], []), ValueError, "p(f)<=2")
    finally:
        sys.setprofile(None)
    require(set(observed["calls"]) == set(functions), "declared reuse must actually execute")
    require(not observed["forbidden_calls"], "forbidden arithmetic")
    # A real copied proof-byte drift must reject before historical imports or any math build.
    copied_root = OUT.joinpath("pin-drift-fixture")
    for relative in [TARGET, *c.EXTRA_SOURCE_SHA256]:
        destination = copied_root.joinpath(relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT.joinpath(relative), destination)
    damaged = copied_root.joinpath("research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md")
    damaged.write_bytes(damaged.read_bytes() + b"\nINDEPENDENT_PIN_DRIFT_TEST\n")
    argv = [sys.executable, "-B", "-X", "utf8", str(copied_root.joinpath(TARGET))]
    rejected = subprocess.run(argv, cwd=copied_root, capture_output=True, timeout=15)
    OUT.joinpath("pin-drift.stdout.log").write_bytes(rejected.stdout)
    OUT.joinpath("pin-drift.stderr.log").write_bytes(rejected.stderr)
    require(rejected.returncode != 0 and b"reviewed source SHA256 drifted" in rejected.stderr, "copied source drift did not reject")
    observed["source_drift_subprocess"] = {"argv": argv, "cwd": str(copied_root), "exit_code": rejected.returncode,
                                         "stdout_sha256": sha(rejected.stdout), "stderr_sha256": sha(rejected.stderr)}
    after = protected_snapshot(pins)
    require(after == before, "frozen or source bytes/mtime changed")
    write_json(OUT.joinpath("after.json"), after)
    saved = json.loads(ROOT.joinpath("experiments/owner_two_positive_stability_20260908/certificate.json").read_bytes())
    require(saved["source_sha256"] == c.SOURCE_SHA256, "saved certificate source pins")
    observed.update(status="PASS", python=sys.version, source_root=str(ROOT),
                    author_manifest_provenance_sha256=EXPECTED_MANIFEST,
                    input_metadata_sha256=EXPECTED_INPUT_METADATA,
                    author_full_manifest_required_for_replay=False,
                    protected_paths=pins, protected_bytes_and_mtimes_unchanged=True,
                    consumer_sha256=pins[TARGET], script_sha256=sha(Path(__file__).read_bytes()),
                    author_saved_counts={"cases": len(saved["cases"]), "tables": sum(len(x["raw_tables"]) for x in saved["cases"]),
                                         "rejections": len(saved["rejected_inputs_or_certificates"])},
                    independent_tables=sum(x["tables_checked"] for x in observed["cases"]),
                    observed_code_objects={label: {"source": f.__code__.co_filename, "module": f.__module__,
                                                   "co_code_sha256": sha(f.__code__.co_code)} for label, f in functions.items()},
                    observation_boundary="after canonical imports; finite calls, not import initialization, all transitive code or all C internals",
                    authority="internal auxiliary independent execution audit; no formal Result, Driver verdict, Foundation or new theorem",
                    review_script_authoring_global_knowledge_snapshot="main@31d06a1 / GLOBAL_KNOWLEDGE_V1")
    observed.pop("current_p", None)
    write_json(OUT.joinpath("execution-evidence.json"), observed)
    write_json(OUT.joinpath("independent-case-outputs.json"), [x[0] for x in results])
    print(json.dumps({"status": "PASS", "cases": len(results), "tables": observed["independent_tables"],
                      "local_rejections": len(observed["rejections"]), "source_drift_rejection": True,
                      "protected_paths": len(pins), "evidence_sha256": sha(OUT.joinpath("execution-evidence.json").read_bytes())}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="checkout containing all nineteen pinned inputs")
    parser.add_argument("--output", type=Path, required=True, help="directory for independent run artifacts")
    args = parser.parse_args()
    ROOT = args.root.resolve()
    OUT = args.output.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    try:
        main()
    except Exception:
        OUT.joinpath("failure.txt").write_text(traceback.format_exc(), encoding="utf-8", newline="\n")
        raise
