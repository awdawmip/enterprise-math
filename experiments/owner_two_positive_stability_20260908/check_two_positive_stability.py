"""Exact raw X6 stability for at most two Jordan-positive sites."""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

__all__ = ["audit_two_positive_stability"]
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OLD_CONSUMER = "experiments/owner_one_positive_stability_20260908/check_one_positive_stability.py"
EXTRA_SOURCE_SHA256 = {
    OLD_CONSUMER: "283c0b64e995077d01e5b42114ffd5791bafadeb5f175b4df17118ee1a9d5878",
    "research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md":
        "1bb732a50cccbbec6c8c11950104c62eed9afc15f326fcc39d9142bd13b24a35",
    "research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_INDEPENDENT_AUDIT_20260908.md":
        "f610e3d642b53279efa91dec15ad3b392270768f73ad0a31edf38212b60be61c",
    "research_notes/OWNER_TWO_POSITIVE_EQUALITY_CLASSIFICATION_REVIEW_20260908.md":
        "1a50237cb4a92a3ec2ef7168b7bd8e90598f69aba394217221f24c83fa810ec7",
}


def _require(condition, message):
    if not condition:
        raise AssertionError(message)


def _verify_sources(pins):
    actual = {path: hashlib.sha256(ROOT.joinpath(path).read_bytes()).hexdigest() for path in pins}
    _require(actual == pins, "reviewed source SHA256 drifted")
    return actual


_verify_sources(EXTRA_SOURCE_SHA256)
sys.path.insert(0, str(ROOT.joinpath(OLD_CONSUMER).parent))
import check_one_positive_stability as one_positive

_require(Path(one_positive.__file__).resolve() == ROOT.joinpath(OLD_CONSUMER).resolve(),
         "unexpected one-positive consumer module")
SOURCE_SHA256 = {**one_positive.SOURCE_SHA256, **EXTRA_SOURCE_SHA256}
_require(len(SOURCE_SHA256) == 16, "expected twelve original pins, old consumer, and three papers")
_verify_sources(SOURCE_SHA256)
x6 = one_positive.x6
exact = one_positive.exact
SLICES = one_positive.SLICES


def _rows(masses):
    return [{"coords": list(coords), "numerator": mass} for coords, mass in sorted(masses.items())]


def _address(coords, axes):
    return tuple(coords[axis] for axis in axes)


def _raw_rows(masses):
    return [{"raw_address": list(address), "joint_can3_address": list(x6.canonical(address)),
             "common_offset": min(address), "numerator": mass} for address, mass in sorted(masses.items())]


def _verify_raw_tables(difference, tables):
    _require([tuple(table["axes"]) for table in tables] == list(SLICES),
             "raw table set or order differs from all twenty slices")
    for table, axes in zip(tables, SLICES):
        actual = one_positive.raw_projection(difference, axes)
        one_positive.verify_joint_projection(difference, axes, actual)
        _require(table["rows"] == _raw_rows(actual), "raw table rows disagree with the actual Jordan projection")
        _require(table["l1_numerator"] == sum(abs(mass) for mass in actual.values()),
                 "raw table L1 disagrees with the actual Jordan projection")


def _rectangle(positive, negative):
    if len(positive) != 2 or len(negative) != 2:
        return None
    u, v = sorted(positive)
    axes = [axis for axis in range(6) if u[axis] != v[axis]]
    if len(axes) != 2:
        return None
    r, s = list(u), list(v)
    r[axes[1]], s[axes[1]] = v[axes[1]], u[axes[1]]
    r, s = tuple(r), tuple(s)
    if set(negative) != {r, s}:
        return None
    weight = positive[u]
    if not (positive[v] == negative[r] == negative[s] == weight):
        return None
    return {"kind": "EQUAL_WEIGHT_COORDINATE_RECTANGLE", "different_axes": axes,
            "positive_diagonal": [list(u), list(v)], "negative_cross_corners": [list(r), list(s)],
            "common_corner_numerator": weight, "original_Jordan_coordinates_checked": True}


def _dual_coefficient(address, axes, positive, different_axes):
    at_positive = address in {_address(coords, axes) for coords in positive}
    if set(different_axes).issubset(axes):
        return 1 if at_positive else -1
    return 0 if at_positive else -1


def _check_equality_claim(positive, negative, M, D, sharp, rectangle):
    _require(type(sharp) is bool and sharp == (M > 0 and D == 4 * M),
             "reported sharp flag disagrees with the nonzero raw gap")
    actual_rectangle = _rectangle(positive, negative)
    _require(rectangle == actual_rectangle, "reported rectangle disagrees with original Jordan coordinates and masses")
    _require(sharp == (actual_rectangle is not None),
             "nonzero equality disagrees with original-coordinate rectangle classification")


def audit_two_positive_stability(case_id, mu_atoms, nu_atoms, denominator=1):
    """Audit finite positive populations in one common labelled raw X6 chart."""
    if type(denominator) is not int or denominator <= 0:
        raise ValueError("common denominator must be a strictly positive integer")
    mu, original_mu = one_positive.population(mu_atoms)
    nu, original_nu = one_positive.population(nu_atoms)
    difference = {coords: mass for coords in sorted(mu.keys() | nu.keys())
                  if (mass := mu.get(coords, 0) - nu.get(coords, 0)) != 0}
    positive = {coords: mass for coords, mass in difference.items() if mass > 0}
    negative = {coords: -mass for coords, mass in difference.items() if mass < 0}
    if len(positive) > 2:
        raise ValueError("aggregated difference is outside p(f)<=2")
    P, N = sum(positive.values()), sum(negative.values())
    M = P + N
    tables = []
    for axes in SLICES:
        raw = one_positive.raw_projection(difference, axes)
        one_positive.verify_joint_projection(difference, axes, raw)
        tables.append({"axes": list(axes), "rows": _raw_rows(raw),
                       "l1_numerator": sum(abs(mass) for mass in raw.values()),
                       "joint_roundtrip_verified": True})
    _verify_raw_tables(difference, tables)
    D = sum(table["l1_numerator"] for table in tables)
    branch = {}
    if len(positive) <= 1:
        # Reconstructed canonical positive populations avoid consuming an input iterator twice.
        old = one_positive.audit_case(case_id + "_one_positive_boundary",
                [(x6.Spatial6(coords), mass) for coords, mass in sorted(mu.items())],
                [(x6.Spatial6(coords), mass) for coords, mass in sorted(nu.items())], denominator)
        for name, value in (("P_numerator", P), ("N_numerator", N), ("l1_numerator", M), ("D_numerator", D)):
            _require(old[name] == value, "independent raw reconstruction disagrees with old boundary: " + name)
        _require([row["l1_numerator"] for row in old["raw_tables"]] ==
                 [row["l1_numerator"] for row in tables], "old boundary twenty-table mismatch")
        branch = {"kind": "REUSED_P_LE_1_BOUNDARY", "p": len(positive),
                  "general_bound": old["general_bound"], "equal_mass_bound": old["equal_mass_bound"],
                  "zero_equality_status": old["zero_equality_status"]}
    else:
        u, v = sorted(positive)
        different_axes = [axis for axis in range(6) if u[axis] != v[axis]]
        d = len(different_axes)
        if d != 2:
            k = 10 if d == 1 else 7
            negative_sites = []
            for coords, mass in sorted(negative.items()):
                avoided = [list(axes) for axes in SLICES
                           if _address(coords, axes) not in {_address(u, axes), _address(v, axes)}]
                _require(len(avoided) >= k, "negative point violates the proved avoiding-table count")
                negative_sites.append({"coords": list(coords), "numerator": mass,
                                       "avoided_tables": avoided, "avoided_count": len(avoided)})
            A = sum(row["numerator"] * row["avoided_count"] for row in negative_sites)
            for table in tables:
                axes = tuple(table["axes"])
                away = sum(mass for coords, mass in negative.items()
                           if _address(coords, axes) not in {_address(u, axes), _address(v, axes)})
                _require(table["l1_numerator"] >= P - N + 2 * away, "per-table finite mass lower bound failed")
                table["negative_mass_away_from_all_positive_projections"] = away
            _require(A >= k * N, "weighted avoiding count failed")
            _require(A == sum(table["negative_mass_away_from_all_positive_projections"] for table in tables),
                     "finite weighted point/table counting identity failed")
            first, second = 20 * P + (2 * k - 20) * N, 20 * (N - P)
            first_gap, second_gap = D - first, D - second
            combined_gap = (40 - k) * D - 20 * k * M
            _require(first_gap >= 0 and second_gap >= 0 and combined_gap >= 0,
                     "stronger two-point counting bound failed")
            _require(combined_gap == 20 * first_gap + (20 - k) * second_gap,
                     "integer weighted-gap combination failed")
            _require(20 * k > 4 * (40 - k) and D > 4 * M, "counting branch must be strictly below one-quarter")
            branch = {"kind": "AVOIDING_TABLE_COUNT", "different_axes": different_axes, "d": d, "k": k,
                      "negative_sites": negative_sites, "weighted_avoiding_mass": A,
                      "lower_bound_one": first, "lower_bound_two": second,
                      "first_gap": first_gap, "second_gap": second_gap,
                      "combined_lhs": (40 - k) * D, "combined_rhs": 20 * k * M,
                      "combined_gap": combined_gap}
        else:
            positive_F = {coords: sum(_dual_coefficient(_address(coords, axes), axes, positive, different_axes)
                                      for axes in SLICES) for coords in positive}
            _require(set(positive_F.values()) == {4}, "dual must equal four at both positive sites")
            table_gap = 0
            pairing = 0
            for table in tables:
                axes = tuple(table["axes"])
                table["dual_class"] = "H" if set(different_axes).issubset(axes) else "L"
                terms = []
                for row in table["rows"]:
                    b = _dual_coefficient(tuple(row["raw_address"]), axes, positive, different_axes)
                    h = row["numerator"]
                    term = abs(h) - b * h
                    _require(term >= 0, "negative table duality gap")
                    terms.append({"raw_address": row["raw_address"], "h": h, "b": b, "gap": term})
                    pairing += b * h
                table["dual_terms"] = terms
                table["dual_gap"] = sum(term["gap"] for term in terms)
                table_gap += table["dual_gap"]
            negative_sites = []
            for coords, mass in sorted(negative.items()):
                values = [_dual_coefficient(_address(coords, axes), axes, positive, different_axes) for axes in SLICES]
                F = sum(values)
                _require(F <= -4, "negative-site dual coefficient exceeds minus four")
                H_sum = sum(value for value, axes in zip(values, SLICES) if set(different_axes).issubset(axes))
                L_sum = F - H_sum
                changed_common = [axis for axis in range(6) if axis not in different_axes and coords[axis] != u[axis]]
                positive_tuple = _address(coords, different_axes) in {
                    _address(u, different_axes), _address(v, different_axes)}
                if positive_tuple:
                    _require(changed_common and H_sum == 4 - 2 * len(changed_common)
                             and L_sum <= -9 and F <= -7, "positive-diagonal common-axis penalty failed")
                else:
                    _require(H_sum == -4 and L_sum <= 0, "different-tuple four-H penalty failed")
                negative_sites.append({"coords": list(coords), "numerator": mass, "b_by_slice": values,
                                       "F": F, "H_sum": H_sum, "L_sum": L_sum,
                                       "positive_diagonal_tuple": positive_tuple, "changed_common_axes": changed_common,
                                       "gap_coefficient": -F - 4, "gap": (-F - 4) * mass})
            negative_gap = sum(row["gap"] for row in negative_sites)
            _require(pairing == 4 * P - sum(row["F"] * row["numerator"] for row in negative_sites),
                     "finite dual pairing identity failed")
            _require(D - 4 * M == table_gap + negative_gap, "complete nonnegative gap identity failed")
            _require(sum(table["dual_class"] == "H" for table in tables) == 4, "expected four H tables")
            branch = {"kind": "FOUR_H_SIXTEEN_L_DUAL", "different_axes": different_axes, "d": d,
                      "positive_F": _rows(positive_F), "negative_sites": negative_sites,
                      "table_gap_sum": table_gap, "negative_gap_sum": negative_gap,
                      "pairing": pairing, "gap_identity_lhs": D - 4 * M,
                      "gap_identity_rhs": table_gap + negative_gap}
    _require(D >= 4 * M, "two-positive stability inequality failed")
    rectangle = _rectangle(positive, negative)
    sharp = M > 0 and D == 4 * M
    _check_equality_claim(positive, negative, M, D, sharp, rectangle)
    if N == 0:
        _require(D == 20 * M, "no-negative-mass raw boundary failed")
    return {"case_id": case_id, "common_mass_unit": one_positive.encode_div(exact.division(1, denominator)),
            "input_populations": {"mu": original_mu, "nu": original_nu},
            "aggregated_signed_difference": _rows(difference),
            "cell_cancellations": [{"coords": list(coords), "cancelled_numerator": min(mu[coords], nu[coords])}
                                   for coords in sorted(mu.keys() & nu.keys())],
            "p": len(positive), "q": len(negative), "P_numerator": P, "N_numerator": N,
            "l1_numerator": M, "D_numerator": D, "bound_gap": D - 4 * M,
            "l1_mass": one_positive.encode_div(exact.division(M, denominator)),
            "D_mass": one_positive.encode_div(exact.division(D, denominator)),
            "ratio": one_positive.encode_div(exact.division(M, D)) if M else None,
            "bound_constant": one_positive.encode_div(exact.division(1, 4)),
            "sharp_nonzero": sharp, "rectangle": rectangle, "zero_difference": M == 0,
            "equal_total_mass": P == N,
            "shared_chart_provenance": "caller premise: common external anchor and labelled raw X6 axes",
            "raw_tables": tables, "proof_branch": branch}


def _atoms(rows):
    return [(x6.Spatial6(tuple(coords)), mass) for coords, mass in rows]


def _jordan_from_case(case):
    difference = {tuple(row["coords"]): row["numerator"] for row in case["aggregated_signed_difference"]}
    return difference, {coords: mass for coords, mass in difference.items() if mass > 0}, {
        coords: -mass for coords, mass in difference.items() if mass < 0}


def _reject(case_id, action, expected_type, expected_message):
    try:
        action()
    except expected_type as error:
        _require(str(error) == expected_message, case_id + ": unexpected refusal signature: " + str(error))
        return {"case_id": case_id, "status": "EXPECTED_REJECTION", "exception": expected_type.__name__,
                "message": str(error)}
    raise AssertionError(case_id + ": expected refusal did not occur")


def _rejections(rectangle_case, unequal_case):
    origin = x6.Spatial6()

    class IntegerSubclass(int):
        pass

    class CellSubclass(x6.Spatial6):
        pass

    rejected = []
    for label, weight in (("zero_weight", 0), ("negative_weight", -1), ("boolean_weight", True),
                          ("subclass_weight", IntegerSubclass(1)), ("noninteger_weight", "1")):
        rejected.append(_reject(label, lambda weight=weight: audit_two_positive_stability(label, [(origin, weight)], []),
                                ValueError, "each population numerator must be a strictly positive integer"))
    for label, denominator in (("zero_denominator", 0), ("negative_denominator", -1),
                               ("boolean_denominator", True), ("subclass_denominator", IntegerSubclass(1)),
                               ("noninteger_denominator", "1")):
        rejected.append(_reject(label, lambda denominator=denominator: audit_two_positive_stability(
            label, [(origin, 1)], [], denominator), ValueError, "common denominator must be a strictly positive integer"))
    for label, bad_cell in (("noncanonical_cell", (0,) * 6), ("subclass_cell", CellSubclass())):
        rejected.append(_reject(label, lambda bad_cell=bad_cell: audit_two_positive_stability(label, [(bad_cell, 1)], []),
                                ValueError, "canonical Spatial6 input required"))
    rejected.append(_reject("p3_outside_contract", lambda: audit_two_positive_stability("p3",
                             [(origin, 1), (origin.step(0), 1), (origin.step(1), 1)], []),
                             ValueError, "aggregated difference is outside p(f)<=2"))
    difference, positive, negative = _jordan_from_case(rectangle_case)
    tampered = deepcopy(rectangle_case["raw_tables"])
    tampered[0]["rows"][0]["numerator"] += 1
    rejected.append(_reject("raw_row_tampering", lambda: _verify_raw_tables(difference, tampered),
                             AssertionError, "raw table rows disagree with the actual Jordan projection"))
    wrong_norm = deepcopy(rectangle_case["raw_tables"])
    wrong_norm[0]["l1_numerator"] += 1
    rejected.append(_reject("raw_norm_tampering", lambda: _verify_raw_tables(difference, wrong_norm),
                             AssertionError, "raw table L1 disagrees with the actual Jordan projection"))
    wrong_corner = deepcopy(rectangle_case["rectangle"])
    wrong_corner["negative_cross_corners"][0][2] += 1
    rejected.append(_reject("original_coordinate_equality_tampering", lambda: _check_equality_claim(
        positive, negative, 4, 16, True, wrong_corner), AssertionError,
        "reported rectangle disagrees with original Jordan coordinates and masses"))
    rejected.append(_reject("sharp_false_negative", lambda: _check_equality_claim(
        positive, negative, 4, 16, False, None), AssertionError,
        "reported sharp flag disagrees with the nonzero raw gap"))
    _, unequal_positive, unequal_negative = _jordan_from_case(unequal_case)
    rejected.append(_reject("support_only_equality_false_positive", lambda: _check_equality_claim(
        unequal_positive, unequal_negative, unequal_case["l1_numerator"], unequal_case["D_numerator"],
        True, rectangle_case["rectangle"]), AssertionError,
        "reported sharp flag disagrees with the nonzero raw gap"))
    return rejected


def _build_certificate():
    _verify_sources(SOURCE_SHA256)
    cell = x6.Spatial6
    rectangle = audit_two_positive_stability("unit_rectangle",
        [(cell((0, 0, 0, 0, 0, 0)), 1), (cell((1, 1, 0, 0, 0, 0)), 1)],
        [(cell((1, 0, 0, 0, 0, 0)), 1), (cell((0, 1, 0, 0, 0, 0)), 1)])
    _require((rectangle["P_numerator"], rectangle["N_numerator"], rectangle["l1_numerator"], rectangle["D_numerator"])
             == (2, 2, 4, 16) and rectangle["sharp_nonzero"], "unit rectangle did not attain the sharp bound")
    u, v, r, s = (0, 0, 0, 0, 0, 0), (1, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0)
    cases = [rectangle]

    def add(name, mu, nu, denominator=1):
        case = audit_two_positive_stability(name, _atoms(mu), _atoms(nu), denominator)
        cases.append(case)
        return case

    unequal = add("unequal_total_mass_rectangle", [(u, 2), (v, 5)], [(r, 1), (s, 4)])
    equal_unbalanced = add("equal_mass_unequal_corners", [(u, 1), (v, 3)], [(r, 2), (s, 2)])
    for case in (unequal, equal_unbalanced):
        _require(not case["sharp_nonzero"] and case["proof_branch"]["negative_gap_sum"] == 0
                 and case["proof_branch"]["table_gap_sum"] > 0,
                 "F=-4 alone must not certify four equal corner masses")

    moved_u, moved_v = (-6, 4, 9, -3, 7, 20), (-6, -5, 9, -3, 12, 20)
    moved_r, moved_s = (-6, 4, 9, -3, 12, 20), (-6, -5, 9, -3, 7, 20)
    moved = add("translated_nonunit_axes_1_4_rectangle", [(moved_u, 3), (moved_v, 3)],
                [(moved_r, 3), (moved_s, 3)], 11)
    _require(moved["sharp_nonzero"] and moved["rectangle"]["different_axes"] == [1, 4],
             "nonunit signed-coordinate rectangle classification failed")
    common_shift = add("negative_positive_tuple_common_axis_shift", [(u, 2), (v, 5)], [((0, 0, 1, 0, 0, 0), 3)])
    _require(common_shift["proof_branch"]["negative_sites"][0]["positive_diagonal_tuple"]
             and common_shift["proof_branch"]["negative_sites"][0]["F"] == -7,
             "common-axis shift did not execute the strict F=-7 boundary")
    outside = add("negative_value_outside_difference_axis_endpoints", [(u, 4), (v, 1)], [((3, 0, 0, 0, 0, 0), 2)])
    _require(outside["proof_branch"]["negative_gap_sum"] > 0 and not outside["sharp_nonzero"],
             "difference-axis outside value was incorrectly treated as a cross corner")

    count_cases = [
        add("d1_counting", [(u, 2), ((2, 0, 0, 0, 0, 0), 5)], [((0, 0, 9, 0, 0, 0), 3), ((2, 3, 0, 0, 0, 0), 4)]),
        add("d3_counting_attains_seven_avoided_tables", [(u, 4), ((2, 2, 2, 0, 0, 0), 2)],
            [((0, 2, 0, 0, 0, 0), 5), ((0, 0, 0, 5, 0, 0), 1)]),
        add("d6_counting", [(u, 1), ((1, 1, 1, 1, 1, 1), 2)], [((1, 0, 0, 0, 0, 0), 4)]),
    ]
    _require([case["proof_branch"]["d"] for case in count_cases] == [1, 3, 6], "wrong positive-axis count branch")
    _require(min(row["avoided_count"] for row in count_cases[1]["proof_branch"]["negative_sites"]) == 7,
             "d3 case did not reach the actual seven-table point boundary")
    cancelled = add("mu_many_sites_cancel_to_p2", [(u, 3), (v, 1), ((8,) * 6, 9), (r, 13)],
                    [(u, 2), ((8,) * 6, 9), (r, 14), (s, 1)])
    for key in ("aggregated_signed_difference", "p", "q", "P_numerator", "N_numerator", "l1_numerator", "D_numerator",
                "raw_tables", "proof_branch", "rectangle", "sharp_nonzero"):
        _require(cancelled[key] == rectangle[key], "pre-Jordan common population changed " + key)

    huge_denominator = (1 << 2052) + 1
    huge = add("2053bit_unevaluated_DIV_rectangle", [(u, 7), (v, 7)], [(r, 7), (s, 7)], huge_denominator)
    _require(huge_denominator.bit_length() == 2053 and huge["sharp_nonzero"], "large DIV rectangle failed")
    for key, numerator in (("common_mass_unit", 1), ("l1_mass", 28), ("D_mass", 112)):
        _require(huge[key] == {"node": "DIV", "numerator": numerator, "denominator": huge_denominator,
                               "state": "UNEVALUATED"}, "literal large DIV was reduced or evaluated")
    _require(huge["ratio"] == {"node": "DIV", "numerator": 28, "denominator": 112,
                               "state": "UNEVALUATED"}, "unreduced sharp ratio carrier changed")
    huge["denominator_bit_length"] = huge_denominator.bit_length()
    no_negative = add("p2_no_negative_mass", [(u, 1), (v, 2)], [])
    _require(no_negative["N_numerator"] == 0 and no_negative["D_numerator"] == 60,
             "N=0 boundary was not directly evaluated")
    add("p0_negative_only", [], [((9,) * 6, 3), ((-7,) * 6, 1)])
    p1 = audit_two_positive_stability("p1_reused_general_sharp_boundary", [(cell(u), 3)],
                                       [(cell(u).step(axis), 1) for axis in range(6)])
    _require(not p1["sharp_nonzero"] and p1["l1_numerator"] == 9 and p1["D_numerator"] == 60,
             "stronger p1 boundary was lost")
    cases.append(p1)
    add("zero_empty", [], [])
    add("zero_after_population_cancellation", [(u, 2), (u, 3)], [(u, 5)])
    swapped = add("rectangle_opposite_positive_diagonal", [(r, 1), (s, 1)], [(u, 1), (v, 1)])
    _require(swapped["sharp_nonzero"] and swapped["D_numerator"] == 16, "opposite rectangle diagonal failed")
    for case in cases:
        _require((case["ratio"] is None) == case["zero_difference"], "zero/nonzero ratio boundary changed")
    return {"schema": "OWNER_TWO_POSITIVE_RAW_STABILITY_V1", "status": "PASS", "python": sys.version.split()[0],
            "source_sha256": SOURCE_SHA256, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "public_api": __all__, "cases": cases, "rejected_inputs_or_certificates": _rejections(rectangle, unequal),
            "reuse_decision": {"decision": "EXTEND_EXISTING_TOOL", "nineteen_item_lookup_is_history_only": True,
                               "catalog_is_runtime_pin": False, "compression_consumer_invoked": False},
            "scope": {"post_Jordan_positive_support_at_most": 2, "raw_three_axis_tables": 20,
                      "p3_extended": False, "Gamma_enumerated": False, "formal_authority_granted": False}}


def _run_with_call_audit():
    required = {
        "one_positive.population": (one_positive.population, OLD_CONSUMER),
        "one_positive.raw_projection": (one_positive.raw_projection, OLD_CONSUMER),
        "one_positive.verify_joint_projection": (one_positive.verify_joint_projection, OLD_CONSUMER),
        "one_positive.audit_case_p_le_1_only": (one_positive.audit_case, OLD_CONSUMER),
        "canonical.Spatial6.__post_init__": (x6.Spatial6.__post_init__,
            "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py"),
        "canonical.hidden_slice_coordinates": (x6.hidden_slice_coordinates,
            "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py"),
        "canonical.from_hidden_slice_coordinates": (x6.from_hidden_slice_coordinates,
            "experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py"),
        "canonical.division": (exact.division, "src/enterprise_math/exact_arithmetic.py"),
    }
    counts = {}
    code_counts = {label: 0 for label in required}
    for label, (function, path) in required.items():
        _require(Path(function.__code__.co_filename).resolve() == ROOT.joinpath(path).resolve(),
                 "canonical function code source differs: " + label)
    allowed_exact = {"division", "compare_divisions", "__init__", "__post_init__", "_require_natural", "_require_positive"}
    allowed_signed = {"support_size", "_z6", "<genexpr>"}
    modules = {one_positive.__name__, x6.__name__, exact.__name__, one_positive.signed_brc.__name__}

    def observe(frame, event, arg):
        if event == "call":
            module, name = frame.f_globals.get("__name__", ""), frame.f_code.co_name
            _require(module != "fractions", "sharp ledger entered historical Fraction arithmetic")
            if module.startswith("enterprise_math."):
                _require(module == exact.__name__ and name in allowed_exact,
                         "sharp ledger entered unrequested arithmetic: " + module + "." + name)
            if module == one_positive.signed_brc.__name__:
                _require(name in allowed_signed, "sharp ledger entered unrequested legacy BRC arithmetic")
            if module == x6.__name__:
                _require(name not in {"positive_path_multiplicity", "relative_endpoint_multiplicity"},
                         "sharp ledger entered legacy multiplicity")
            if module in modules:
                key = module + "." + name
                counts[key] = counts.get(key, 0) + 1
            for label, (function, _) in required.items():
                if frame.f_code is function.__code__:
                    code_counts[label] += 1
        elif event == "c_call":
            pair = (getattr(arg, "__module__", ""), getattr(arg, "__name__", ""))
            _require(pair not in {("builtins", "divmod"), ("math", "sqrt"), ("math", "isqrt"), ("math", "factorial")},
                     "sharp ledger entered quotient/root/multiplicity materialization")

    previous = sys.getprofile()
    _require(previous is None, "run the fixed sharp ledger without replacing another profiler")
    sys.setprofile(observe)
    try:
        result = _build_certificate()
    finally:
        sys.setprofile(previous)
    _require(all(count > 0 for count in code_counts.values()), "a declared canonical code object was not executed")
    _verify_sources(SOURCE_SHA256)
    result["main_ledger_call_audit"] = {
        "status": "PASS", "window": "fixed certificate build after canonical imports",
        "selected_call_counts": dict(sorted(counts.items())),
        "observed_required_code_objects": {
            label: {"source_path": path, "source_sha256": SOURCE_SHA256[path],
                    "function_name": function.__qualname__, "runtime_module": function.__module__,
                    "observed_exact_code_object_calls": code_counts[label],
                    "co_code_sha256": hashlib.sha256(function.__code__.co_code).hexdigest()}
            for label, (function, path) in required.items()},
        "forbidden_observed_calls": 0,
        "limitation": "actual frame code-object identity and selected call boundaries; import-time, unexecuted transitive paths and all native C internals are not certified",
    }
    return result


def _main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="update only this directory's certificate.json")
    args = parser.parse_args()
    result = _run_with_call_audit()
    content = (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    target = HERE.joinpath("certificate.json")
    if args.write:
        target.write_bytes(content)
    else:
        _require(target.read_bytes() == content, "saved certificate bytes differ from exact replay")
    print(json.dumps({"status": "PASS", "cases": len(result["cases"]), "source_pins": len(SOURCE_SHA256),
                      "raw_tables": sum(len(case["raw_tables"]) for case in result["cases"]),
                      "expected_rejections": len(result["rejected_inputs_or_certificates"]),
                      "mode": "WRITE" if args.write else "EXACT_REPLAY",
                      "certificate_sha256": hashlib.sha256(content).hexdigest()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
