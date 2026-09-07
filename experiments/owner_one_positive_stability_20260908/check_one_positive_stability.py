#!/usr/bin/env python3
"""Fixed X6 one-positive-support examples, with integer mass numerators.

The paper proves the theorem. This consumer checks only the declared finite
examples and retains symbolic DIV states; it performs no division evaluation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE_SHA256 = {
    "research_notes/OWNER_ONE_POSITIVE_STABILITY_20260907.md":
        "b49eac9291c7b6a6ec458a133700ee17a4573972e58787a976871512746dd4e7",
    "research_notes/OWNER_ONE_POSITIVE_STABILITY_INDEPENDENT_AUDIT_20260908.md":
        "f6fe6713fb46bc0fd9c6626333cb44afd14c88b13b7f7d99fe8f928859434038",
    "research_notes/OWNER_X6_STABILITY_20260907.md":
        "2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127",
    "definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md":
        "519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e",
    "exact_arithmetic_runtime_policy.json":
        "0fdb8eddc09d9e734ddd91b52d6c3c18c9d6036837dfe9fee0bbdbdb7d44b2aa",
    "src/enterprise_math/__init__.py":
        "bf974df0ef0f57991947d061cb300e835e53bc79ff5667e4229fcc7a6cadbdcc",
    "src/enterprise_math/exact_arithmetic.py":
        "f4f8feead82dc53a35e5fec495b31e46e64820f7b115c9efd6034063e68f8ad6",
    "src/enterprise_math/core.py":
        "d2814d1d31eb195905f05136f250fcac2232b8cfc7dc6c9797000733ddebe636",
    "src/enterprise_math/division.py":
        "4421c6dc9acfaa61492137951e543973c010c6a127655126152cc18763cc35e9",
    "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py":
        "e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e",
    "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py":
        "6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4",
    "tools/check_exact_arithmetic_policy.py":
        "d5629502352e8207a4616368858e68dec1c259e8a0c635769163784dc8bd01fa",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def verify_sources():
    actual = {
        relative: hashlib.sha256(ROOT.joinpath(relative).read_bytes()).hexdigest()
        for relative in SOURCE_SHA256
    }
    require(actual == SOURCE_SHA256, "reviewed source SHA256 drifted")
    return actual


verify_sources()
sys.path.insert(0, str(ROOT.joinpath("src")))
sys.path.insert(0, str(ROOT.joinpath("experiments/x6_signed_native_spatial_v16_20260905")))
from enterprise_math import exact_arithmetic as exact
import signed_brc
import x6_signed as x6

for module, relative in (
    (exact, "src/enterprise_math/exact_arithmetic.py"),
    (signed_brc, "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"),
    (x6, "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py"),
):
    require(Path(module.__file__).resolve() == ROOT.joinpath(relative).resolve(),
            "canonical module origin differs from the pinned source")

SLICES = x6.ALL_SLICES
require(len(SLICES) == 20 and len(set(SLICES)) == 20, "twenty unique slices required")
require(all(len(s) == 3 and tuple(sorted(set(s))) == s
            and all(a in range(6) for a in s) for s in SLICES),
        "slice labels must be the complete three-of-six coordinate selections")


def encode_div(expr):
    """Encode an existing canonical expression, without reduction/evaluation."""
    require(type(expr) is exact.DivisionExpr, "canonical DivisionExpr identity required")
    return {"node": "DIV", "numerator": expr.numerator,
            "denominator": expr.denominator, "state": "UNEVALUATED"}


def population(atoms):
    total = {}
    original = []
    for index, (cell, numerator) in enumerate(atoms):
        if type(cell) is not x6.Spatial6:
            raise ValueError("canonical Spatial6 input required")
        if type(numerator) is not int or numerator <= 0:
            raise ValueError("each population numerator must be a strictly positive integer")
        total[cell.coords] = total.get(cell.coords, 0) + numerator
        original.append({"input_index": index, "coords": list(cell.coords),
                         "positive_weight_numerator": numerator})
    return total, original


def raw_projection(masses, axes):
    result = {}
    for coords, mass in masses.items():
        address = tuple(coords[a] for a in axes)
        result[address] = result.get(address, 0) + mass
    return result


def verify_joint_projection(masses, axes, raw):
    """Actually exercise the retained-offset path on the current inputs."""
    joint = {}
    for coords, mass in masses.items():
        cell = x6.Spatial6(coords)
        visible, common, hidden = x6.hidden_slice_coordinates(cell, axes)
        restored = x6.from_hidden_slice_coordinates(axes, visible, common, hidden)
        require(restored == cell, "full joint slice roundtrip failed")
        key = (visible, common)
        joint[key] = joint.get(key, 0) + mass
    recovered = {}
    for (visible, common), mass in joint.items():
        address = tuple(value + common for value in visible)
        recovered[address] = recovered.get(address, 0) + mass
    require(recovered == raw, "joint can3 and common offset lost the raw marginal")


def audit_case(case_id, mu, nu, denominator=1):
    """Audit finite positive inputs already expressed in one common chart."""
    if type(denominator) is not int or denominator <= 0:
        raise ValueError("common denominator must be a strictly positive integer")
    unit = exact.division(1, denominator)
    mu, original_mu = population(mu)
    nu, original_nu = population(nu)
    cells = sorted(set(mu) | set(nu))
    difference = {c: mu.get(c, 0) - nu.get(c, 0) for c in cells}
    difference = {c: value for c, value in difference.items() if value != 0}
    positive = {c: value for c, value in difference.items() if value > 0}
    negative = {c: -value for c, value in difference.items() if value < 0}
    if len(positive) > 1:
        raise ValueError("aggregated difference is outside p(f)<=1")
    q = next(iter(positive), None)
    P, N = sum(positive.values()), sum(negative.values())
    norm = sum(abs(value) for value in difference.values())
    require(norm == P + N, "Jordan norm reconstruction failed")
    equal_mass = sum(mu.values()) == sum(nu.values())
    axis_masses = [0] * 6
    negative_sites = []
    if q is not None:
        for coords, mass in sorted(negative.items()):
            displacement = x6.Spatial6(q).displacement_to(x6.Spatial6(coords))
            r = signed_brc.support_size(displacement)
            distinguished = sum(tuple(coords[a] for a in axes)
                                != tuple(q[a] for a in axes) for axes in SLICES)
            require(distinguished >= 10, "raw distinguishing-count lower bound failed")
            require((distinguished == 10) == (r == 1), "count equality condition failed")
            if r == 1:
                axis = next(a for a, value in enumerate(displacement) if value != 0)
                axis_masses[axis] += mass
            negative_sites.append({"coords": list(coords), "mass_numerator": mass,
                                   "different_axes": r, "distinguishing_tables": distinguished})
    all_single_axis = all(site["different_axes"] == 1 for site in negative_sites)
    tables = []
    for axes in SLICES:
        raw_mu, raw_nu = raw_projection(mu, axes), raw_projection(nu, axes)
        verify_joint_projection(mu, axes, raw_mu)
        verify_joint_projection(nu, axes, raw_nu)
        addresses = sorted(set(raw_mu) | set(raw_nu))
        delta = {a: raw_mu.get(a, 0) - raw_nu.get(a, 0) for a in addresses}
        table_norm = sum(abs(value) for value in delta.values())
        rows = []
        for address in addresses:
            common = min(address)
            rows.append({"raw_address": list(address),
                         "joint_can3_address": [value - common for value in address],
                         "common_offset": common,
                         "mu_numerator": raw_mu.get(address, 0),
                         "nu_numerator": raw_nu.get(address, 0),
                         "signed_difference_numerator": delta[address]})
        table = {"axes": list(axes), "rows": rows, "l1_numerator": table_norm,
                 "missing_addresses_are_zero": True, "joint_roundtrip_verified": True}
        if q is not None:
            q_address = tuple(q[a] for a in axes)
            a_i = sum(mass for coords, mass in negative.items()
                      if tuple(coords[a] for a in axes) != q_address)
            require(delta.get(q_address, 0) == P - N + a_i, "q fibre identity failed")
            require(table_norm == abs(P - N + a_i) + a_i, "single-table identity failed")
            table.update({"negative_mass_away_from_q": a_i,
                          "q_fibre_signed_numerator": P - N + a_i,
                          "single_table_identity_verified": True})
        else:
            require(table_norm == norm, "nonpositive projection changed total mass norm")
        tables.append(table)
    D = sum(table["l1_numerator"] for table in tables)
    A = sum(table["negative_mass_away_from_q"] for table in tables) if q is not None else None
    if q is not None:
        require(A == sum(site["mass_numerator"] * site["distinguishing_tables"]
                         for site in negative_sites), "finite counting identity failed")
        require(A >= 10 * N and D >= 20 * max(P, N - P), "paper lower bounds failed")
    else:
        require(D == 20 * norm, "nonpositive/zero formula failed")
    require(20 * norm <= 3 * D, "general stability inequality failed")
    balanced = all(6 * mass == N for mass in axis_masses)
    general_condition = q is not None and N == 2 * P and all_single_axis and balanced
    general_sharp = norm > 0 and 20 * norm == 3 * D
    require(general_sharp == general_condition, "general sharp iff condition failed")
    equal_sharp = norm > 0 and equal_mass and 10 * norm == D
    equal_condition = q is not None and equal_mass and all_single_axis
    require(equal_sharp == equal_condition, "equal-mass sharp iff condition failed")
    if equal_mass:
        require(10 * norm <= D, "equal-mass stability inequality failed")
    ratio = None
    if norm > 0:
        require(D > 0, "nonzero difference must have positive raw discrepancy")
        ratio = exact.division(norm, D)
        require(exact.compare_divisions(ratio, exact.division(3, 20)) <= 0,
                "symbolic ratio disagrees with the integer general comparison")
        if equal_mass:
            require(exact.compare_divisions(ratio, exact.division(1, 10)) <= 0,
                    "symbolic ratio disagrees with the equal-mass comparison")
    return {
        "case_id": case_id, "common_mass_unit": encode_div(unit),
        "positive_populations": {"mu": original_mu, "nu": original_nu},
        "cell_cancellations": [{"coords": list(c),
                                "cancelled_numerator": min(mu.get(c, 0), nu.get(c, 0))}
                               for c in cells if c in mu and c in nu],
        "aggregated_signed_difference": [{"coords": list(c), "numerator": value}
                                         for c, value in sorted(difference.items())],
        "p": len(positive), "q": list(q) if q is not None else None,
        "P_numerator": P, "N_numerator": N, "A_numerator": A,
        "l1_numerator": norm, "D_numerator": D,
        "l1_mass": encode_div(exact.division(norm, denominator)),
        "D_mass": encode_div(exact.division(D, denominator)),
        "ratio": encode_div(ratio) if ratio is not None else None,
        "difference_kind": "ONE_POSITIVE_SITE" if q is not None else
            ("NONPOSITIVE_NONZERO" if norm else "ZERO_DIFFERENCE"),
        "negative_sites": negative_sites, "axis_negative_masses": axis_masses,
        "raw_tables": tables,
        "general_bound": {"constant": encode_div(exact.division(3, 20)),
                          "lhs": 20 * norm, "rhs": 3 * D, "holds": True,
                          "comparison_equal": 20 * norm == 3 * D,
                          "nonzero_sharp_equality": general_sharp,
                          "equality_conditions_hold": general_condition},
        "equal_mass_bound": {"constant": encode_div(exact.division(1, 10)),
                             "applicable": equal_mass, "lhs": 10 * norm, "rhs": D,
                             "holds": True if equal_mass else None,
                             "comparison_equal": 10 * norm == D if equal_mass else None,
                             "nonzero_sharp_equality": equal_sharp,
                             "equality_conditions_hold": equal_condition},
        "zero_equality_status": "TRIVIAL_ZERO" if norm == 0 else None,
    }


def unit_neighbours(q, signs):
    neighbours, checks = [], []
    for axis, direction in enumerate(signs):
        neighbour = q.step(axis, direction)
        displacement = q.displacement_to(neighbour)
        support = signed_brc.support_size(displacement)
        shortest = signed_brc.shortest_event_count(displacement)
        squared = signed_brc.spatial_norm_squared(displacement)
        require((support, shortest, squared) == (1, 1, 1), "native signed unit witness failed")
        neighbours.append(neighbour)
        checks.append({"from": list(q.coords), "to": list(neighbour.coords),
                       "axis": axis, "direction": direction,
                       "support_size": support, "shortest_event_count": shortest,
                       "spatial_norm_squared": squared})
    return neighbours, checks


def rejection_checks(q, neighbour):
    rejected = []
    probes = (
        ("more_than_one_positive_site", lambda: audit_case("bad", [(q, 1), (neighbour, 1)], [])),
        ("zero_population_weight", lambda: audit_case("bad", [(q, 0)], [])),
        ("negative_population_weight", lambda: audit_case("bad", [(q, -1)], [])),
        ("boolean_population_weight", lambda: audit_case("bad", [(q, True)], [])),
        ("noninteger_coordinate", lambda: x6.Spatial6((0, 0, 0, 0, 0, "1"))),
        ("zero_common_denominator", lambda: audit_case("bad", [(q, 1)], [], 0)),
        ("boolean_common_denominator", lambda: audit_case("bad", [(q, 1)], [], True)),
    )
    for name, probe in probes:
        try:
            probe()
        except ValueError as exc:
            rejected.append({"probe": name, "status": "REJECTED", "exception": str(exc)})
        else:
            raise AssertionError(f"invalid input was accepted: {name}")
    return rejected


def build_certificate():
    source_hashes = verify_sources()
    q = x6.Spatial6()
    neighbours, native_checks = unit_neighbours(q, (1, 1, 1, 1, 1, 1))
    translated = x6.Spatial6((5, -3, 2, 0, -8, 4))
    signed_neighbours, signed_checks = unit_neighbours(translated, (-1, 1, -1, 1, -1, 1))
    e0, twice_e0 = neighbours[0], neighbours[0].step(0)
    diagonal = q
    for axis in range(6):
        diagonal = diagonal.step(axis)
    # Expected values are the independent finite counts in the paper contract.
    # Tuples contain p, L1, D, equal-total-mass, general sharp, equal-mass sharp.
    specs = [
        ("sharp_3_20", [(q, 3)], [(z, 1) for z in neighbours], 1, (1, 9, 60, False, True, False)),
        ("sharp_equal_1_10", [(q, 1)], [(e0, 1)], 4, (1, 2, 20, True, False, True)),
        ("signed_translated_sharp", [(translated, 3)], [(z, 1) for z in signed_neighbours],
         7, (1, 9, 60, False, True, False)),
        ("N_zero", [(q, 4)], [], 3, (1, 4, 80, False, False, False)),
        ("q_partial_cancellation", [(q, 2), (q, 3), (neighbours[1], 4)],
         [(q, 2), (e0, 1), (twice_e0, 2), (neighbours[1], 4)],
         11, (1, 6, 60, True, False, True)),
        ("q_complete_nonpositive", [(q, 2)], [(q, 2), (e0, 3)],
         1, (0, 3, 60, False, False, False)),
        ("q_overcancel_nonpositive", [(q, 2)], [(q, 5), (e0, 1)],
         1, (0, 4, 80, False, False, False)),
        ("zero_difference", [(q, 2)], [(q, 2)], 5, (0, 0, 0, True, False, False)),
        ("negative_projection_collision", [(q, 1)], [(e0, 1), (e0.step(3), 2)],
         1, (1, 4, 60, False, False, False)),
        ("can3_diagonal_loss", [(q, 1)], [(diagonal, 1)],
         1, (1, 2, 40, True, False, False)),
        ("unbalanced_axes_not_general_sharp", [(q, 3)], [(e0, 6)],
         1, (1, 9, 120, False, False, False)),
        ("axis_line_split_still_sharp", [(q, 6)],
         [(e0, 1), (twice_e0, 1)] + [(z, 2) for z in neighbours[1:]],
         13, (1, 18, 120, False, True, False)),
    ]
    cases = []
    for name, mu, nu, scale, expected in specs:
        result = audit_case(name, mu, nu, scale)
        actual = (result["p"], result["l1_numerator"], result["D_numerator"],
                  result["equal_mass_bound"]["applicable"],
                  result["general_bound"]["nonzero_sharp_equality"],
                  result["equal_mass_bound"]["nonzero_sharp_equality"])
        require(actual == expected, f"finite example disagrees with expected counts: {name}")
        result["expected_summary_verified"] = True
        if name == "sharp_equal_1_10":
            require(result["ratio"]["numerator"] == 2 and result["ratio"]["denominator"] == 20,
                    "symbolic ratio was silently reduced")
        if name == "negative_projection_collision":
            table = next(t for t in result["raw_tables"] if t["axes"] == [0, 1, 2])
            row = next(r for r in table["rows"] if r["raw_address"] == [1, 0, 0])
            require(row["nu_numerator"] == 3 and row["signed_difference_numerator"] == -3,
                    "same-sign negative collision was not retained")
            result["collision_verified_on_axes"] = [0, 1, 2]
        if name == "can3_diagonal_loss":
            coarse_D = 0
            for axes in SLICES:
                coarse = {}
                for cell, mass in ((q, 1), (diagonal, -1)):
                    address = cell.observe(axes)
                    coarse[address] = coarse.get(address, 0) + mass
                coarse_D += sum(abs(value) for value in coarse.values())
            require(coarse_D == 0 and result["D_numerator"] == 40,
                    "can3-only diagonal counterexample failed")
            result["can3_only_counterexample"] = {
                "coarse_D_numerator": coarse_D, "raw_D_numerator": 40,
                "l1_numerator": 2, "status": "CAN3_ONLY_CONTRACT_REJECTED"}
        cases.append(result)
    verify_sources()
    return {
        "schema": "OWNER_ONE_POSITIVE_RAW_X6_INTEGER_DIV_V1",
        "status": "FINITE_CONSUMER_PASS_NOT_GENERAL_PROOF",
        "scope": "ANCHOR_EXPOSED_OWNER_AUXILIARY_NO_FORMAL_TASK_CLAIM",
        "input_chart": {"anchor": "one_shared_external_Cell_anchor",
                        "labelled_axes": [0, 1, 2, 3, 4, 5],
                        "coordinates": "signed integers relative to that anchor"},
        "arithmetic": {"carrier": "integer positive mass numerators",
                       "mass_unit": "canonical unevaluated DIV(1,s)",
                       "division_root_evaluation": "NO_EVALUATION_REQUESTED",
                       "evaluation_traces": [],
                       "legacy_integer_compatibility_checks": "NOT_CALLED",
                       "historical_module_initializers": "NOT_MIGRATED_NOT_MAIN_LEDGER_EVIDENCE"},
        "source_sha256": source_hashes,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "native_unit_step_checks": native_checks + signed_checks,
        "cases": cases, "rejected_inputs": rejection_checks(q, e0),
        "general_p_le_7": "OUTSIDE_SCOPE",
    }


def run_with_call_audit():
    """Audit only this fixed main ledger after canonical imports complete."""
    counts = {}
    allowed_exact = {"division", "compare_divisions", "__init__", "__post_init__",
                     "_require_natural", "_require_positive"}
    allowed_signed = {"support_size", "shortest_event_count", "spatial_norm_squared",
                      "_z6", "<genexpr>"}

    def observe(frame, event, arg):
        if event == "call":
            module_name = frame.f_globals.get("__name__", "")
            name = frame.f_code.co_name
            require(module_name != "fractions", "main ledger entered historical Fraction arithmetic")
            if module_name.startswith("enterprise_math."):
                require(module_name == exact.__name__ and name in allowed_exact,
                        f"main ledger entered an unrequested arithmetic path: {module_name}.{name}")
            if module_name == signed_brc.__name__:
                require(name in allowed_signed, f"main ledger entered legacy signed BRC arithmetic: {name}")
            if module_name == x6.__name__:
                require(name not in {"positive_path_multiplicity", "relative_endpoint_multiplicity"},
                        "main ledger entered unrequested legacy X6 multiplicity")
            if module_name in {exact.__name__, signed_brc.__name__, x6.__name__}:
                key = f"{module_name}.{name}"
                counts[key] = counts.get(key, 0) + 1
        elif event == "c_call":
            module_name = getattr(arg, "__module__", "")
            name = getattr(arg, "__name__", "")
            require((module_name, name) not in {("builtins", "divmod"),
                                                ("math", "sqrt"), ("math", "isqrt")},
                    "main ledger requested a direct quotient/root helper")

    previous = sys.getprofile()
    require(previous is None, "run the bounded audit without replacing another profiler")
    sys.setprofile(observe)
    try:
        result = build_certificate()
    finally:
        sys.setprofile(previous)
    require(counts.get("enterprise_math.exact_arithmetic.division", 0) > 0,
            "canonical DIV construction was not executed")
    result["main_ledger_call_audit"] = {
        "status": "PASS", "scope": "after canonical imports; fixed certificate build only",
        "selected_call_counts": dict(sorted(counts.items())),
        "fraction_weight_multiplicity_or_quotient_root_calls": 0,
        "limitation": "runtime call boundary plus reviewed selected source, not a transitive static certificate",
    }
    verify_sources()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write only this directory's certificate.json")
    args = parser.parse_args()
    result = run_with_call_audit()
    content = (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    output = HERE.joinpath("certificate.json")
    if args.write:
        output.write_bytes(content)
    else:
        require(output.read_bytes() == content, "saved certificate bytes differ from the current exact replay")
    print(json.dumps({"status": "PASS", "cases": len(result["cases"]),
                      "rejected_inputs": len(result["rejected_inputs"]),
                      "source_pins": len(SOURCE_SHA256), "mode": "WRITE" if args.write else "EXACT_REPLAY",
                      "certificate_sha256": hashlib.sha256(content).hexdigest()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
