"""Exact positive-support compression; default replay is read-only."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CONSUMER = "experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py"
PAPER = "research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md"
EXTRA_SOURCE_SHA256 = {
    CONSUMER: "283c0b64e995077d01e5b42114ffd5791bafadeb5f175b4df17118ee1a9d5878",
    PAPER: "2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def verify_pins(pins):
    actual = {path: hashlib.sha256(ROOT.joinpath(path).read_bytes()).hexdigest()
              for path in pins}
    require(actual == pins, "reviewed source SHA256 drifted")
    return actual


# Pin the reused executable before importing it by its ordinary module name.
verify_pins(EXTRA_SOURCE_SHA256)
sys.path.insert(0, str(ROOT.joinpath(CONSUMER).parent))
import check_one_positive_stability as one_positive

require(Path(one_positive.__file__).resolve() == ROOT.joinpath(CONSUMER).resolve(),
        "unexpected one-positive consumer module")
SOURCE_SHA256 = {**one_positive.SOURCE_SHA256, **EXTRA_SOURCE_SHA256}
require(len(SOURCE_SHA256) == 14, "expected twelve reused sources and two extension sources")
verify_pins(SOURCE_SHA256)
x6 = one_positive.x6
exact = one_positive.exact
SLICES = one_positive.SLICES


def signed_difference(mu, nu):
    return {coords: mass for coords in sorted(mu.keys() | nu.keys())
            if (mass := mu.get(coords, 0) - nu.get(coords, 0)) != 0}


def signed_rows(masses):
    return [{"coords": list(coords), "numerator": mass}
            for coords, mass in sorted(masses.items())]


def jordan(masses):
    positive = {coords: mass for coords, mass in masses.items() if mass > 0}
    negative = {coords: -mass for coords, mass in masses.items() if mass < 0}
    return positive, negative


def compression_spec(positive):
    if not positive:
        return {"mode": "EMPTY_POSITIVE_CONSTANT", "positive_support": [],
                "axes": [{"positive_values": [], "external_class": 0,
                          "carrier_values": [0]} for _ in range(6)],
                "carrier_cardinality": 1}
    axes = []
    carrier = 1
    for axis in range(6):
        values = sorted({coords[axis] for coords in positive})
        external = max(values) + 1
        axes.append({"positive_values": values, "external_class": external,
                     "carrier_values": sorted(values + [external])})
        carrier *= len(values) + 1
    return {"mode": "JORDAN_POSITIVE_SUPPORT", "positive_support": signed_rows(positive),
            "axes": axes, "carrier_cardinality": carrier}


def compressed_coords(coords, spec):
    return tuple(coords[axis] if coords[axis] in row["positive_values"]
                 else row["external_class"] for axis, row in enumerate(spec["axes"]))


def pushforward(masses, spec):
    result = {}
    for coords, mass in masses.items():
        target = compressed_coords(coords, spec)
        # Exercise the canonical six-axis type, without treating compression as motion.
        require(x6.Spatial6(target).coords == target, "canonical compressed cell mismatch")
        result[target] = result.get(target, 0) + mass
    return {coords: mass for coords, mass in result.items() if mass != 0}


def validated_compression(masses, spec):
    positive, _ = jordan(masses)
    if spec != compression_spec(positive):
        raise ValueError("compression specification is not bound to this true Jordan positive support")
    return pushforward(masses, spec)


def audit_compression(case_id, mu_atoms, nu_atoms, denominator=1):
    if type(denominator) is not int or denominator <= 0:
        raise ValueError("the common denominator must be a strictly positive integer")
    mu, original_mu = one_positive.population(mu_atoms)
    nu, original_nu = one_positive.population(nu_atoms)
    before = signed_difference(mu, nu)
    positive, negative = jordan(before)
    spec = compression_spec(positive)
    after = validated_compression(before, spec)
    after_positive, after_negative = jordan(after)
    require(after_positive == positive, "positive sites or individual positive masses changed")
    P, N = sum(positive.values()), sum(negative.values())
    require(sum(after_positive.values()) == P, "Jordan P changed")
    require(sum(after_negative.values()) == N, "Jordan N changed")
    require(sum(abs(mass) for mass in after.values()) == P + N, "global L1 changed")
    require(pushforward(after, spec) == after, "compression is not idempotent")
    require(compression_spec(after_positive) == spec, "recomputed compression specification changed")
    require(all(all(coords[axis] in row["carrier_values"]
                    for axis, row in enumerate(spec["axes"])) for coords in after),
            "compressed support left the symbolic carrier")
    require(len(after) <= spec["carrier_cardinality"], "actual support exceeds carrier")
    require(spec["carrier_cardinality"] <= (len(positive) + 1) ** 6,
            "axis-class carrier exceeds the positive-support bound")
    require(signed_difference(pushforward(mu, spec), pushforward(nu, spec)) == after,
            "aggregate/cancel does not commute with population pushforward")
    tables = []
    D = 0
    for axes in SLICES:
        raw_before = one_positive.raw_projection(before, axes)
        raw_after = one_positive.raw_projection(after, axes)
        one_positive.verify_joint_projection(before, axes, raw_before)
        one_positive.verify_joint_projection(after, axes, raw_after)
        l1_before = sum(abs(mass) for mass in raw_before.values())
        l1_after = sum(abs(mass) for mass in raw_after.values())
        require(l1_before == l1_after, f"raw marginal L1 changed at {axes}")
        D += l1_before
        tables.append({"axes": list(axes), "before": signed_rows(raw_before),
                       "after": signed_rows(raw_after), "l1_numerator": l1_before,
                       "raw_l1_preserved": True, "joint_roundtrip_verified": True})
    return {
        "case_id": case_id,
        "common_mass_unit": one_positive.encode_div(exact.division(1, denominator)),
        "input_populations": {"mu": original_mu, "nu": original_nu},
        "cell_cancellations": [{"coords": list(coords),
                                "cancelled_numerator": min(mu[coords], nu[coords])}
                               for coords in sorted(mu.keys() & nu.keys())],
        "aggregated_signed_difference": signed_rows(before),
        "compressed_signed_difference": signed_rows(after),
        "compression": spec,
        "p": len(positive), "q_before": len(negative), "q_after": len(after_negative),
        "P_numerator": P, "N_numerator": N, "l1_numerator": P + N, "D_numerator": D,
        "l1_mass": one_positive.encode_div(exact.division(P + N, denominator)),
        "D_mass": one_positive.encode_div(exact.division(D, denominator)),
        "support_before": len(before), "support_after": len(after),
        "positive_sites_and_masses_preserved": True, "jordan_masses_preserved": True,
        "global_l1_preserved": True, "idempotent": True,
        "population_pushforward_commutes_with_cancellation": True,
        "carrier_membership_verified_without_enumeration": True, "raw_tables": tables,
    }


def demo_inputs():
    cell = x6.Spatial6
    return (
        [(cell((0, 0, 0, 0, 0, 0)), 5), (cell((2, 0, 0, 0, 0, 0)), 7)],
        [(cell((9, 9, 9, 9, 9, 9)), 3), (cell((11, 11, 11, 11, 11, 11)), 4)],
    )


def demo_case():
    return audit_compression("p2_initial_negative_merge", *demo_inputs())


def row_masses(rows):
    return {tuple(row["coords"]): row["numerator"] for row in rows}


def norm_signature(case):
    return {key: case[key] for key in
            ("p", "P_numerator", "N_numerator", "l1_numerator", "D_numerator")}


def raw_norms(case):
    return {tuple(row["axes"]): row["l1_numerator"] for row in case["raw_tables"]}


def expect_rejection(case_id, action, exception, message):
    try:
        action()
    except exception as error:
        require(str(error) == message, f"{case_id}: wrong rejection boundary: {error}")
        return {"case_id": case_id, "status": "EXPECTED_REJECTION",
                "exception": exception.__name__, "message": str(error)}
    raise AssertionError(f"{case_id}: expected rejection did not occur")


def compare_one_positive(case, mu, nu, denominator=1):
    require(case["p"] <= 1, "the one-positive theorem consumer cannot audit p>1")
    old_before = one_positive.audit_case(case["case_id"] + "_old_before", mu, nu, denominator)
    after = row_masses(case["compressed_signed_difference"])
    positive, negative = jordan(after)
    old_after = one_positive.audit_case(
        case["case_id"] + "_old_after",
        [(x6.Spatial6(coords), mass) for coords, mass in sorted(positive.items())],
        [(x6.Spatial6(coords), mass) for coords, mass in sorted(negative.items())], denominator,
    )
    fields = ("p", "P_numerator", "N_numerator", "A_numerator", "l1_numerator", "D_numerator",
              "ratio", "difference_kind", "axis_negative_masses", "general_bound", "equal_mass_bound",
              "zero_equality_status", "common_mass_unit")
    for key in fields:
        require(old_before[key] == old_after[key], f"one-positive compatibility changed {key}")
    for key, value in norm_signature(case).items():
        require(old_before[key] == value, f"old one-positive consumer disagrees at {key}")
    require(raw_norms(case) == raw_norms(old_before) == raw_norms(old_after),
            "one-positive raw marginal norm changed")
    old_table_fibres = [{key: table[key] for key in
                        ("axes", "negative_mass_away_from_q", "q_fibre_signed_numerator")}
                       for table in old_before["raw_tables"] if "negative_mass_away_from_q" in table]
    new_table_fibres = [{key: table[key] for key in
                        ("axes", "negative_mass_away_from_q", "q_fibre_signed_numerator")}
                       for table in old_after["raw_tables"] if "negative_mass_away_from_q" in table]
    require(old_table_fibres == new_table_fibres, "one-positive per-table fibre identities changed")
    return {"case_id": case["case_id"], "status": "PASS", "p_scope": case["p"],
            "compared_fields": list(fields), "per_table_raw_norms_preserved": True,
            "per_table_fibre_identities": old_table_fibres,
            "general_bound": old_before["general_bound"],
            "equal_mass_bound": old_before["equal_mass_bound"],
            "zero_equality_status": old_before["zero_equality_status"]}


def rejection_checks():
    cell = x6.Spatial6()
    failures = []
    weight_message = "each population numerator must be a strictly positive integer"
    for name, weight in (("zero_weight", 0), ("negative_weight", -1),
                         ("boolean_weight", True), ("noninteger_weight", "1")):
        failures.append(expect_rejection(
            name, lambda weight=weight: audit_compression(name, [(cell, weight)], []),
            ValueError, weight_message))
    for name, denominator in (("zero_denominator", 0), ("negative_denominator", -1),
                              ("boolean_denominator", True), ("noninteger_denominator", "1")):
        failures.append(expect_rejection(
            name, lambda denominator=denominator: audit_compression(name, [(cell, 1)], [], denominator),
            ValueError, "the common denominator must be a strictly positive integer"))
    failures.append(expect_rejection(
        "noncanonical_cell", lambda: audit_compression("bad_cell", [((0,) * 6, 1)], []),
        ValueError, "canonical Spatial6 input required"))
    failures.append(expect_rejection(
        "incorrect_expected_source_digest", lambda: verify_pins({PAPER: "0" * 64}),
        AssertionError, "reviewed source SHA256 drifted"))
    return failures


def failure_boundaries():
    zero = (0,) * 6
    old_spec = compression_spec({zero: 1})
    changed = {(2, 0, 0, 0, 0, 0): 1, (3, 0, 0, 0, 0, 0): -1}
    incorrectly_compressed = pushforward(changed, old_spec)
    require(sum(abs(m) for m in changed.values()) == 2 and not incorrectly_compressed,
            "old-S counterexample did not exhibit the specified norm loss")
    stale_rejection = expect_rejection(
        "old_positive_support_reuse", lambda: validated_compression(changed, old_spec),
        ValueError, "compression specification is not bound to this true Jordan positive support")
    stale_rejection.update({"raw_unvalidated_pushforward_before": signed_rows(changed),
                            "raw_unvalidated_pushforward_after": signed_rows(incorrectly_compressed),
                            "global_l1_before": 2, "global_l1_after": 0,
                            "reason": "the reused S belongs to another signed difference"})

    can3_input = {zero: 1, (1, 2, 3, 0, 0, 0): -1}
    can3_output = validated_compression(can3_input, old_spec)
    axes = (0, 1, 2)

    def can3_histogram(masses):
        result = {}
        for coords, mass in masses.items():
            address = x6.Spatial6(coords).observe(axes)
            result[address] = result.get(address, 0) + mass
        return result

    before = can3_histogram(can3_input)
    after = can3_histogram(can3_output)
    before_norm, after_norm = sum(abs(m) for m in before.values()), sum(abs(m) for m in after.values())
    require((before_norm, after_norm) == (2, 0), "can3-alone counterexample did not lose the offset")
    for masses in (can3_input, can3_output):
        raw = one_positive.raw_projection(masses, axes)
        require(sum(abs(m) for m in raw.values()) == 2, "raw counterexample norm changed")
        one_positive.verify_joint_projection(masses, axes, raw)
    can3_rejection = expect_rejection(
        "can3_alone_is_not_a_preserved_observer",
        lambda: require(before_norm == after_norm, "can3-alone L1 is not preserved"),
        AssertionError, "can3-alone L1 is not preserved")
    can3_rejection.update({"axes": list(axes), "can3_before": signed_rows(before),
                           "can3_after": signed_rows(after), "can3_l1_before": before_norm,
                           "can3_l1_after": after_norm, "raw_l1_before": 2, "raw_l1_after": 2,
                           "joint_can3_and_offset_roundtrip_verified": True})
    return [stale_rejection, can3_rejection]


def build_certificate():
    verify_pins(SOURCE_SHA256)
    cell = x6.Spatial6
    zero = cell()
    mu, nu = demo_inputs()
    first = demo_case()
    require((first["P_numerator"], first["N_numerator"], first["l1_numerator"], first["D_numerator"],
             first["compression"]["carrier_cardinality"], first["support_before"], first["support_after"])
            == (12, 7, 19, 380, 96, 4, 3), "first negative-merge case disagrees")
    cases = [first]
    cross_checks = []
    for differing_axes in range(1, 7):
        other = cell((2,) * differing_axes + (0,) * (6 - differing_axes))
        partly_overlapping_nu = [(cell((0, 0, 0, 0, 0, 9)), 3), (cell((0, 0, 0, 0, 0, 11)), 4)]
        case = audit_compression(f"p2_differing_axes_{differing_axes}",
                                 [(zero, 5), (other, 7)], partly_overlapping_nu)
        expected_carrier = 3 ** differing_axes * 2 ** (6 - differing_axes)
        require(case["p"] == 2 and case["compression"]["carrier_cardinality"] == expected_carrier,
                "p2 carrier formula disagrees with actual axis classes")
        require(case["support_after"] == 3 < expected_carrier <= 729,
                "carrier size was mistaken for occupied support")
        require(min(raw_norms(case).values()) < case["l1_numerator"] == max(raw_norms(case).values()),
                "p2 axis cases must actually exercise both overlapping and separated raw projections")
        case["p2_carrier_check"] = {"differing_axes": differing_axes, "expected": expected_carrier,
                                    "formula": "3^r * 2^(6-r)", "holds": True}
        cases.append(case)

    positive_other = mu[1][0]
    cancelled_cell = cell((6,) * 6)
    cancelling_mu = [(zero, 2), (zero, 3), (zero, 11), (positive_other, 7), (positive_other, 4),
                     (cancelled_cell, 13), (nu[0][0], 17)]
    cancelling_nu = [(zero, 11), (positive_other, 4), (cancelled_cell, 13),
                     (nu[0][0], 20), (nu[1][0], 4)]
    cancelled = audit_compression("p2_aggregate_then_cancel", cancelling_mu, cancelling_nu)
    for key in ("aggregated_signed_difference", "compressed_signed_difference", "compression", "raw_tables"):
        require(cancelled[key] == first[key], f"duplicate/cancelled input changed {key}")
    require(norm_signature(cancelled) == norm_signature(first), "cancellation changed the signed ledger")
    cases.append(cancelled)
    cross_checks.append({"kind": "AGGREGATE_AND_CANCEL", "status": "PASS",
                         "same_true_signed_difference": True, "positive_support_computed_after_cancellation": True})

    shift = (-8, 3, -5, 0, 2, 11)

    def translated(original):
        moved = cell(tuple(value + delta for value, delta in zip(original.coords, shift)))
        require(original.displacement_to(moved) == shift, "native translation displacement differs")
        return moved

    translated_case = audit_compression("p2_translated", [(translated(c), m) for c, m in mu],
                                        [(translated(c), m) for c, m in nu])
    require(norm_signature(translated_case) == norm_signature(first) and
            raw_norms(translated_case) == raw_norms(first), "translation changed preserved masses")
    expected_translated = {translated(cell(coords)).coords: mass
                           for coords, mass in row_masses(first["compressed_signed_difference"]).items()}
    require(row_masses(translated_case["compressed_signed_difference"]) == expected_translated,
            "positive-support compression did not commute with translation")
    cases.append(translated_case)
    cross_checks.append({"kind": "TRANSLATION", "status": "PASS", "shift": list(shift),
                         "compression_commutes_for_nonempty_S": True, "all_twenty_raw_norms_equal": True})

    permutation = (4, 2, 5, 0, 3, 1)
    rotated_case = audit_compression("p2_axis_permuted", [(c.rotate(permutation), m) for c, m in mu],
                                     [(c.rotate(permutation), m) for c, m in nu])
    expected_rotated = {cell(coords).rotate(permutation).coords: mass
                        for coords, mass in row_masses(first["compressed_signed_difference"]).items()}
    require(row_masses(rotated_case["compressed_signed_difference"]) == expected_rotated,
            "compression did not commute with canonical axis permutation")
    require(norm_signature(rotated_case) == norm_signature(first), "axis permutation changed masses")
    rotated_norms = raw_norms(rotated_case)
    for axes, norm in raw_norms(first).items():
        require(rotated_norms[tuple(sorted(permutation[a] for a in axes))] == norm,
                "axis-permuted raw table does not match its relabelled slice")
    cases.append(rotated_case)
    cross_checks.append({"kind": "AXIS_PERMUTATION", "status": "PASS",
                         "old_axis_to_new_axis": list(permutation), "relabelled_twenty_tables_equal": True})

    compatible = []
    q = cell((-3, 2, 0, 1, 4, 7))
    p1_nu = [(q.step(0).step(0), 2), (q.step(1, -1).step(1, -1), 3)]
    compatibility_inputs = [
        ("p0_negative_only", [], nu),
        ("zero_empty", [], []),
        ("zero_after_cancellation", [(zero, 2), (zero, 3)], [(zero, 5)]),
        ("p1_equal_mass_compatibility", [(q, 5)], p1_nu),
        ("p1_general_sharp_compatibility", [(q, 3)], [(q.step(axis), 1) for axis in range(6)]),
    ]
    for name, case_mu, case_nu in compatibility_inputs:
        case = audit_compression(name, case_mu, case_nu)
        cases.append(case)
        compatible.append(compare_one_positive(case, case_mu, case_nu))

    huge_denominator = (1 << 2052) + 1
    require(huge_denominator.bit_length() == 2053, "large DIV denominator bit width differs")
    huge = audit_compression("p2_2053bit_unit_DIV", mu, nu, huge_denominator)
    require(norm_signature(huge) == norm_signature(first) and raw_norms(huge) == raw_norms(first),
            "literal mass unit changed integer ledger")
    for key, numerator in (("common_mass_unit", 1), ("l1_mass", 19), ("D_mass", 380)):
        require(huge[key] == {"node": "DIV", "numerator": numerator,
                              "denominator": huge_denominator, "state": "UNEVALUATED"},
                "large denominator was evaluated, reduced, or replaced")
    huge["denominator_bit_length"] = huge_denominator.bit_length()
    cases.append(huge)

    rebuilt = audit_compression("changed_S_recomputed",
                                [(cell((2, 0, 0, 0, 0, 0)), 1)], [(cell((3, 0, 0, 0, 0, 0)), 1)])
    require(rebuilt["l1_numerator"] == 2 and rebuilt["support_after"] == 2,
            "recomputed S did not restore the valid compression contract")
    cases.append(rebuilt)
    cases.append(audit_compression("can3_boundary_raw_control", [(zero, 1)],
                                   [(cell((1, 2, 3, 0, 0, 0)), 1)]))
    return {
        "schema": "OWNER_POSITIVE_SUPPORT_COMPRESSION_V1", "status": "PASS",
        "source_sha256": SOURCE_SHA256,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "reuse_decision": {"decision": "EXTEND_EXISTING_TOOL", "reviewed_catalog_entries": 19,
                           "catalog_path": "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json",
                           "catalog_sha256_at_paper_review": "9b9b1851602200bbb207681dbac444a7e745b2915d6f8851bc999fd3a028f115",
                           "catalog_is_runtime_pin": False,
                           "T6": "reuse its stated descent contract; no new search or operational call"},
        "cases": cases, "cross_checks": cross_checks, "one_positive_compatibility": compatible,
        "rejected_inputs": rejection_checks(), "failure_boundaries": failure_boundaries(),
        "scope": {"finite_positive_integer_populations_with_common_positive_DIV_unit": True,
                  "Gamma_enumerated": False, "new_two_positive_sharp_consumer": False,
                  "physical_motion_or_microhistory_preservation_claimed": False,
                  "formal_Task_Result_claim_or_catalog_change": False},
    }


def run_with_call_audit():
    """Observe this fixed certificate build, after the pinned canonical imports."""
    counts = {}
    allowed_exact = {"division", "compare_divisions", "__init__", "__post_init__",
                     "_require_natural", "_require_positive"}
    allowed_signed = {"support_size", "_z6", "<genexpr>"}
    selected_modules = {one_positive.__name__, x6.__name__, exact.__name__, one_positive.signed_brc.__name__}

    def observe(frame, event, arg):
        if event == "call":
            module = frame.f_globals.get("__name__", "")
            name = frame.f_code.co_name
            require(module != "fractions", "compression ledger entered historical Fraction arithmetic")
            if module.startswith("enterprise_math."):
                require(module == exact.__name__ and name in allowed_exact,
                        f"compression ledger entered unrequested arithmetic: {module}.{name}")
            if module == one_positive.signed_brc.__name__:
                require(name in allowed_signed, f"compression ledger entered legacy BRC arithmetic: {name}")
            if module == x6.__name__:
                require(name not in {"positive_path_multiplicity", "relative_endpoint_multiplicity"},
                        "compression ledger entered unrequested legacy X6 multiplicity")
            if module in selected_modules:
                key = f"{module}.{name}"
                counts[key] = counts.get(key, 0) + 1
        elif event == "c_call":
            pair = (getattr(arg, "__module__", ""), getattr(arg, "__name__", ""))
            require(pair not in {("builtins", "divmod"), ("math", "sqrt"),
                                 ("math", "isqrt"), ("math", "factorial")},
                    "compression ledger requested a quotient/root/multiplicity helper")

    previous = sys.getprofile()
    require(previous is None, "run this bounded ledger without replacing another profiler")
    sys.setprofile(observe)
    try:
        result = build_certificate()
    finally:
        sys.setprofile(previous)
    for function in ("check_one_positive_stability.population", "check_one_positive_stability.raw_projection",
                     "check_one_positive_stability.verify_joint_projection",
                     "enterprise_math.exact_arithmetic.division", "x6_signed.hidden_slice_coordinates",
                     "x6_signed.from_hidden_slice_coordinates", "x6_signed.rotate", "x6_signed.step"):
        require(counts.get(function, 0) > 0, f"declared native reuse was not executed: {function}")
    result["main_ledger_call_audit"] = {
        "status": "PASS", "scope": "after pinned canonical imports; fixed certificate build only",
        "selected_call_counts": dict(sorted(counts.items())),
        "forbidden_observed_calls": 0,
        "one_positive_audit_case_scope": "only five explicit p=0 or p=1 compatibility cases, before and after",
        "limitation": "observed Python/C call boundaries plus reviewed selected source; imports and unexecuted transitive paths are outside this audit",
    }
    verify_pins(SOURCE_SHA256)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="update only this directory's certificate.json")
    args = parser.parse_args()
    result = run_with_call_audit()
    content = (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    output = HERE.joinpath("certificate.json")
    if args.write:
        output.write_bytes(content)
    else:
        require(output.read_bytes() == content, "saved certificate bytes differ from exact replay")
    print(json.dumps({"status": "PASS", "cases": len(result["cases"]),
                      "raw_tables": sum(len(case["raw_tables"]) for case in result["cases"]),
                      "rejected_inputs": len(result["rejected_inputs"]),
                      "failure_boundaries": len(result["failure_boundaries"]),
                      "source_pins": len(SOURCE_SHA256), "mode": "WRITE" if args.write else "EXACT_REPLAY",
                      "certificate_sha256": hashlib.sha256(content).hexdigest()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
