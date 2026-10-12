"""Independent post-run verifier for the exact p17 order-one ledger.

Preparation/default entry performs no p17 computation. Verification must be
explicitly invoked only after the parent authorizes the genuine run's ledger.
This module imports no producer or author checker. Mathematical numbers use
integers/Fraction; decimal execution-time metadata is not used in arithmetic.
"""
from fractions import Fraction as Rat
from decimal import Decimal
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json

PRIME = 17
DIM = 16
MASS = 2331
TASK = "RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET"
PUBLICATION = "TP2-26869C0B4D63A6BB761D"
RESEARCHER = "EM-T6-B4F89F"
CERT_PIN = "fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6"
BOUNDS_PIN = "b2175e24af7ab3c3a582c28262503f69241ca00f3024ca9c77e75db615beb647"
PRODUCER_PIN = "22a86082fd4096c44759e7c145b390dc9aefe96e10b7658efd90614ec7c8505b"
OUTSIDE = (2, 6, 12, 14)


class VerificationFailure(RuntimeError):
    pass


def need(condition, location):
    if not condition:
        raise VerificationFailure(location)


def integer(value, location="integer"):
    need(type(value) is int, location + ": non-integer arithmetic value")
    return value


def rational(value, location="rational"):
    need(type(value) is list and len(value) == 2, location + ": malformed pair")
    a, b = (integer(x, location) for x in value)
    need(b > 0, location + ": denominator must be positive")
    return Rat(a, b)


def encode(value):
    value = Rat(value)
    return [value.numerator, value.denominator]


def compare(actual, expected, location):
    """Strictly compare the scientific subtrees, including integer/bool types."""
    need(type(actual) is type(expected), location + ": type mismatch")
    if type(expected) is dict:
        need(set(actual) == set(expected), location + ": missing/extra fields")
        for key in expected:
            compare(actual[key], expected[key], location + "." + key)
    elif type(expected) is list:
        need(len(actual) == len(expected), location + ": length mismatch")
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, location + "[" + str(i) + "]")
    else:
        need(actual == expected, location + ": value mismatch")


def duplicate_safe_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def forbidden_constant(value):
    raise VerificationFailure("nonfinite JSON constant: " + value)


def read_document(path, wanted_hash=None):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    need(wanted_hash is None or digest == wanted_hash, str(path) + ": SHA256 mismatch")
    data = json.loads(raw, parse_float=Decimal, parse_constant=forbidden_constant,
                      object_pairs_hook=duplicate_safe_object)
    return data, digest


def determinant_by_rational_elimination(matrix):
    """Independent exact Gaussian determinant, not the producer's Bareiss code."""
    n = len(matrix)
    need(n > 0 and all(len(row) == n for row in matrix), "determinant dimensions")
    work = [[Rat(x) for x in row] for row in matrix]
    determinant = Rat(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            return Rat(0)
        if pivot != col:
            work[pivot], work[col] = work[col], work[pivot]
            determinant = -determinant
        diagonal = work[col][col]
        determinant *= diagonal
        for row in range(col + 1, n):
            multiplier = work[row][col] / diagonal
            for j in range(col + 1, n):
                work[row][j] -= multiplier * work[col][j]
            work[row][col] = Rat(0)
    return determinant


def gram_ldl(rows):
    """Rebuild GS lengths/mu through G=L D L^T, without author GS vectors."""
    n = len(rows)
    need(n > 0 and all(len(row) == n for row in rows), "LDL dimensions")
    gram = [[sum(x * y for x, y in zip(a, b)) for b in rows] for a in rows]
    lower = [[Rat(0) for _ in range(n)] for _ in range(n)]
    diagonal = []
    for i in range(n):
        lower[i][i] = Rat(1)
        d = Rat(gram[i][i]) - sum((lower[i][k] ** 2 * diagonal[k]
                                  for k in range(i)), Rat(0))
        need(d > 0, "LDL nonpositive diagonal at " + str(i))
        diagonal.append(d)
        for j in range(i + 1, n):
            numerator = Rat(gram[j][i]) - sum((lower[j][k] * lower[i][k] * diagonal[k]
                                               for k in range(i)), Rat(0))
            lower[j][i] = numerator / d
    for i in range(n):
        for j in range(n):
            rebuilt = sum((lower[i][k] * diagonal[k] * lower[j][k]
                           for k in range(n)), Rat(0))
            need(rebuilt == gram[i][j], "LDL Gram reconstruction")
    return lower, diagonal


def project_via_ldl(point, weighted_rows, lower, diagonal):
    h = []
    for i, row in enumerate(weighted_rows):
        scalar = Rat(sum(x * y for x, y in zip(point, row)))
        scalar -= sum((lower[i][k] * diagonal[k] * h[k]
                       for k in range(i)), Rat(0))
        h.append(scalar / diagonal[i])
    need(sum((d * x * x for d, x in zip(diagonal, h)), Rat(0))
         == sum(x * x for x in point), "full-rank affine projection norm")
    return h


def congruences_by_rationals(vector, cofactor=None, uniform_modulus=None):
    """Clear exact unit denominators; do not reuse producer inverse-power code."""
    for k in range(1, 7):
        value = sum((Rat(u, s ** k) for s, u in enumerate(vector, 1)), Rat(0))
        if cofactor is not None:
            value += Rat(1, cofactor ** k)
        need(value.denominator % PRIME != 0, "scaled congruence denominator")
        modulus = PRIME ** k if uniform_modulus is None else uniform_modulus
        need(value.numerator % modulus == 0, "mixed congruence k=" + str(k))


def bracketing_choices(center):
    target = -Rat(center)
    whole, remainder = divmod(target.numerator, target.denominator)
    if remainder == 0:
        return whole, None
    if 2 * remainder <= target.denominator:
        return whole, whole + 1
    return whole + 1, whole


def prime_factors(value):
    divisors = []
    for trial in range(2, value + 1):
        if value % trial == 0:
            divisors.append(trial)
            while value % trial == 0:
                value //= trial
        if value == 1:
            break
    return divisors


def certify_inputs(certificate, bounds):
    need(integer(certificate["prime"]) == PRIME, "certificate prime")
    need(integer(certificate["side_budget"]) == MASS, "certificate budget")
    raw = [[integer(x) for x in row] for row in certificate["unweighted_basis"]]
    weighted = [[integer(x) for x in row] for row in certificate["weighted_basis"]]
    need(len(raw) == len(weighted) == DIM, "basis dimensions")
    need(all(len(row) == DIM for row in raw + weighted), "basis row length")
    compare(weighted, [[(PRIME * s - 1) * x for s, x in enumerate(row, 1)]
                       for row in raw], "basis weighting")
    need(abs(determinant_by_rational_elimination(raw)) == PRIME ** 21,
         "kernel determinant/index")
    for row in raw:
        congruences_by_rationals(row)
    unit_minor = [[Rat(1, s ** k) for s in range(1, 7)] for k in range(1, 7)]
    minor_det = determinant_by_rational_elimination(unit_minor)
    need(minor_det.numerator % PRIME != 0 and minor_det.denominator % PRIME != 0,
         "six-column unit determinant")
    lower, diagonal = gram_ldl(weighted)
    need(diagonal == [rational(x) for x in certificate["gram_schmidt_squared"]],
         "independent LDL/certified GS mismatch")
    need(min(diagonal) == rational(certificate["minimum_gram_schmidt_squared"]),
         "minimum norm mismatch")
    max_radius = MASS ** 2 + 2026 ** 2
    need(all(d > max_radius for d in diagonal), "two-integer interval theorem")
    need(3 * min(diagonal) > 4 * max_radius, "two-nonpreferred theorem")
    admissible = [r for r in range(1, 17) if max(prime_factors(PRIME + r)) <= PRIME]
    compare(bounds["actual_maximal_prime17_admissible_residues"], admissible,
            "static admissible domain")
    compare(bounds["outside_maximal_prime17_residues"], list(OUTSIDE),
            "static outside domain")
    need(len(bounds["classes"]) == DIM, "static sixteen-class bounds")
    return raw, weighted, lower, diagonal


def labels_from_norms(diagonal, r):
    cost = PRIME * (PRIME + r) - 1
    radius = (MASS - cost) ** 2 + MASS ** 2
    labels = [()]
    labels += [(i,) for i, d in enumerate(diagonal) if d <= 4 * radius]
    labels += [(i, j) for i, j in combinations(range(DIM), 2)
               if diagonal[i] + diagonal[j] <= 4 * radius]
    return labels, cost, radius


def completion_expected(vector, r, positive, negative):
    atom = PRIME * (PRIME + r)
    plus = MASS - (atom - 1) - positive
    minus = MASS - negative
    need(plus >= 0 and minus >= 0, "completion residual budgets")
    moments = [Rat(1 + sum(vector))]
    moments += [Rat(1, atom ** k)
                + sum((Rat(u, (PRIME * s) ** k)
                       for s, u in enumerate(vector, 1)), Rat(0))
                for k in range(1, 7)]
    need(all(m.denominator % PRIME != 0 for m in moments[1:]), "completion pole")
    cuts = []
    for k, value in enumerate(moments):
        low, high = -Rat(plus, 2 ** k), Rat(minus, 2 ** k)
        cuts.append({"k": k, "M_k": encode(value), "necessary_lower": encode(low),
                     "necessary_upper": encode(high), "passes": low <= value <= high})
    return {"remaining_positive_budget": plus, "remaining_negative_budget": minus,
            "moments": [encode(x) for x in moments], "necessary_completion_cuts": cuts,
            "completion_status": "OPEN_AFTER_NECESSARY_CUTS" if all(c["passes"] for c in cuts)
                                 else "EXCLUDED_BY_NAMED_NECESSARY_CUT",
            "local_survivor_retained": True,
            "unknown_completion_equations":
                "sum_a t_a/a^k = -M_k, k=0..6, with separate residual masses and all17-free composite/integer denominators whose prime factors are at most13",
            "full_collision_or_global_T6_claim": False}


def verify_label_record(record, label, r, point, weighted_point, h,
                        raw_rows, weighted_rows, lower, diagonal, radius):
    """Independently reproduce one fixed label, including every prefix decision."""
    coefficients = [0] * DIM
    energy = Rat(0)
    trace = []
    for i in reversed(range(DIM)):
        center = h[i] + sum((coefficients[j] * lower[j][i]
                             for j in range(i + 1, DIM)), Rat(0))
        preferred, alternate = bracketing_choices(center)
        chosen = alternate if i in label else preferred
        if chosen is None:
            expected = {"nonpreferred_indices": list(label),
                        "status": "NO_DISTINCT_NONPREFERRED_INTEGER", "stopping_index": i,
                        "coordinate_decisions": len(trace) + 1,
                        "partial_norm_squared": encode(energy), "steps": trace}
            compare(record, expected, "r=" + str(r) + " absent branch " + str(label))
            return expected
        coefficients[i] = chosen
        term = diagonal[i] * (center + chosen) ** 2
        need(term >= 0, "negative contribution")
        if i in label:
            need(term >= diagonal[i] / 4, "nonpreferred quarter bound")
        energy += term
        trace.append({"i": i, "center": encode(center), "preferred": preferred,
                      "other": alternate, "chosen": chosen, "nonpreferred": i in label,
                      "contribution": encode(term), "partial_norm_squared": encode(energy)})
        if energy > radius:
            expected = {"nonpreferred_indices": list(label), "status": "EXACT_NORM_PRUNED",
                        "stopping_index": i, "coordinate_decisions": len(trace),
                        "partial_norm_squared": encode(energy), "steps": trace}
            compare(record, expected, "r=" + str(r) + " exact prune " + str(label))
            return expected
    vector = [point[s] + sum(coefficients[i] * raw_rows[i][s] for i in range(DIM))
              for s in range(DIM)]
    weighted = [(PRIME * (s + 1) - 1) * x for s, x in enumerate(vector)]
    from_weighted = [weighted_point[s]
                     + sum(coefficients[i] * weighted_rows[i][s] for i in range(DIM))
                     for s in range(DIM)]
    need(weighted == from_weighted, "independent weighted reconstruction")
    squared = sum(x * x for x in weighted)
    need(Rat(squared) == energy and squared <= radius, "independent full norm")
    congruences_by_rationals(vector, PRIME + r)
    positive = sum(x for x in weighted if x > 0)
    negative = -sum(x for x in weighted if x < 0)
    plus_limit = MASS - (PRIME * (PRIME + r) - 1)
    feasible = positive <= plus_limit and negative <= MASS
    expected = {"nonpreferred_indices": list(label),
                "status": "LOCAL_FEASIBLE" if feasible else "SIGNED_BUDGET_REJECTED",
                "coordinate_decisions": len(trace), "basis_coefficients": coefficients,
                "q0_vector": vector, "weighted_norm_squared": squared,
                "positive_q0_mass": positive, "negative_q0_mass": negative,
                "positive_q0_budget": plus_limit, "negative_q0_budget": MASS,
                "mixed_congruence_residues": [0] * 6, "steps": trace}
    if feasible:
        expected["completion"] = completion_expected(vector, r, positive, negative)
    compare(record, expected, "r=" + str(r) + " full path " + str(label))
    return expected


def verify_context(ledger, context_path):
    source, digest = read_document(context_path)
    need(ledger["control_context_sha256"] == digest, "control context digest")
    expected = {}
    for field in ["task_id", "publication_id", "claim_id", "execution_record_id",
                  "run_id", "researcher_id", "root_verified_current_native_authorization",
                  "execution_authorized"]:
        expected[field] = source[field]
    need(expected["task_id"] == TASK and expected["publication_id"] == PUBLICATION,
         "actual child task/publication")
    need(expected["researcher_id"] == RESEARCHER, "actual parent Researcher provenance")
    for field in ["claim_id", "execution_record_id", "run_id"]:
        need(type(expected[field]) is str and bool(expected[field]), "actual provenance " + field)
    need(expected["root_verified_current_native_authorization"] is True
         and expected["execution_authorized"] is True, "parent recorded authorization")
    descriptors = []
    for item in source["receipt_evidence"]:
        need(item["kind"] in ("TASK_PUBLICATION", "CLAIM", "RUN"), "receipt kind")
        raw = Path(item["path"]).read_bytes()
        need(hashlib.sha256(raw).hexdigest() == item["sha256"], "receipt byte binding")
        descriptors.append({k: item[k] for k in ("kind", "path", "sha256")})
    need({x["kind"] for x in descriptors} == {"TASK_PUBLICATION", "CLAIM", "RUN"},
         "all receipt kinds")
    expected["receipt_evidence"] = descriptors
    compare(ledger["task_execution_context"], expected, "public control provenance")
    return digest


def verify_actual_ledger(ledger_path, certificate_path, bounds_path, producer_path, context_path):
    """Only call after explicit parent authorization following the genuine run."""
    ledger, ledger_hash = read_document(ledger_path)
    certificate, certificate_hash = read_document(certificate_path, CERT_PIN)
    bounds, bounds_hash = read_document(bounds_path, BOUNDS_PIN)
    producer_hash = hashlib.sha256(Path(producer_path).read_bytes()).hexdigest()
    need(producer_hash == PRODUCER_PIN, "reviewed producer snapshot changed")
    need(ledger["executor_sha256"] == producer_hash, "ledger producer binding")
    need(ledger["certificate_sha256"] == certificate_hash
         and ledger["branch_bound_sha256"] == bounds_hash, "ledger input bindings")
    need(ledger["schema"] == "T6_P17_ORDER1_EXACT_SIXTEEN_ROW_CLASSIFICATION_V1"
         and ledger["status"] == "COMPLETE_DOMAIN_AND_AFFINE_CLASSIFICATION", "ledger scope/status")
    context_hash = verify_context(ledger, context_path)
    raw_rows, weighted_rows, lower, diagonal = certify_inputs(certificate, bounds)
    rows = ledger["rows"]
    need(type(rows) is list and len(rows) == DIM, "all sixteen ledger rows")
    all_paths, all_decisions, all_survivors, cut_excluded = 0, 0, 0, 0
    statuses = []
    for r, row in enumerate(rows, 1):
        need(integer(row["r"]) == r, "residue row ordering/uniqueness")
        divisors = prime_factors(PRIME + r)
        if max(divisors) > PRIME:
            compare(row, {"r": r, "cofactor": PRIME + r, "prime_divisors": divisors,
                          "status": "OUTSIDE_MAXIMAL_P17_DOMAIN", "affine_paths_evaluated": 0,
                          "relaxed_class_empty_claim": False}, "outside row " + str(r))
            statuses.append(row["status"])
            continue
        labels, cost, radius = labels_from_norms(diagonal, r)
        bound_row = bounds["classes"][r - 1]
        need(integer(bound_row["r"]) == r and integer(bound_row["R2"]) == radius
             and integer(bound_row["atom_cost"]) == cost, "saved class bound")
        compare(bound_row["weighted_farther_choice_singletons"],
                [x[0] for x in labels if len(x) == 1], "saved singleton coverage")
        compare(bound_row["weighted_farther_choice_pairs"],
                [list(x) for x in labels if len(x) == 2], "saved pair coverage")
        need(integer(bound_row["weighted_leaf_bound"]) == len(labels), "saved class count")
        point = [integer(x, "particular") for x in row["particular_q0"]]
        need(len(point) == DIM, "particular dimension")
        need(point[6:] == [0] * 10 and all(0 <= x < PRIME ** 6 for x in point[:6]),
             "recorded strong-construction representative shape")
        congruences_by_rationals(point, PRIME + r, PRIME ** 6)
        congruences_by_rationals(point, PRIME + r)
        weighted_point = [(PRIME * s - 1) * x for s, x in enumerate(point, 1)]
        h = project_via_ldl(weighted_point, weighted_rows, lower, diagonal)
        records = row["paths"]
        need(type(records) is list and len(records) == len(labels), "all independent labels covered")
        compare(row["allowed_nonpreferred_sets"], [list(x) for x in labels], "row labels")
        verified = [verify_label_record(rec, label, r, point, weighted_point, h,
                                        raw_rows, weighted_rows, lower, diagonal, radius)
                    for rec, label in zip(records, labels)]
        survivors = [x for x in verified if x["status"] == "LOCAL_FEASIBLE"]
        need(len({tuple(x["q0_vector"]) for x in survivors}) == len(survivors),
             "duplicate local survivor")
        decisions = sum(x["coordinate_decisions"] for x in verified)
        expected_row = {"r": r, "cofactor": PRIME + r, "prime_divisors": divisors,
                        "status": "COMPLETE_LOCAL_FEASIBLE_VECTOR_LIST" if survivors
                                  else "EMPTY_BY_COMPLETE_EXACT_SEARCH",
                        "q1_cost": cost, "R2": radius, "particular_q0": point,
                        "particular_mixed_residues": [0] * 6,
                        "affine_h_coordinates": [encode(x) for x in h],
                        "allowed_nonpreferred_sets": [list(x) for x in labels],
                        "affine_paths_evaluated": len(labels), "coordinate_decisions": decisions,
                        "paths": verified, "local_survivor_count": len(survivors),
                        "full_collision_or_global_T6_claim": False}
        compare(row, expected_row, "complete class " + str(r))
        all_paths += len(labels)
        all_decisions += decisions
        all_survivors += len(survivors)
        cut_excluded += sum(x["completion"]["completion_status"] == "EXCLUDED_BY_NAMED_NECESSARY_CUT"
                            for x in survivors)
        statuses.append(row["status"])
    need(all_paths == 299 and all_decisions <= 4784, "complete 299-label bound")
    need(integer(ledger["affine_paths_evaluated"]) == all_paths, "ledger total path count")
    need(integer(ledger["coordinate_decisions"]) == all_decisions, "ledger total decisions")
    need(integer(ledger["local_survivor_count"]) == all_survivors, "ledger survivor total")
    for field in ("p17_higher_orders_claim", "global_T6_completion_claim",
                  "p19_campaign_replayed", "author_checkers_imported_or_executed"):
        need(ledger[field] is False, "forbidden scope flag: " + field)
    return {"schema": "T6_P17_ORDER1_INDEPENDENT_LOCAL_LEDGER_CHECK_V1", "status": "PASS",
            "ledger_sha256": ledger_hash, "certificate_sha256": certificate_hash,
            "branch_bound_sha256": bounds_hash, "producer_sha256": producer_hash,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "control_context_sha256": context_hash, "task_id": TASK, "publication_id": PUBLICATION,
            "rows_verified": DIM, "outside_domain_rows_verified": list(OUTSIDE),
            "fixed_labels_independently_verified": all_paths,
            "coordinate_decisions_verified": all_decisions, "local_survivors_retained": all_survivors,
            "survivors_excluded_only_at_completion_cut": cut_excluded, "row_statuses": statuses,
            "arithmetic": "ARBITRARY_PRECISION_INTEGER_AND_FRACTION",
            "independent_method": "RATIONAL_GAUSSIAN_DETERMINANT_AND_GRAM_LDL_RECONSTRUCTION",
            "nonblind_same_owner_code_exposure": True, "producer_imported_or_called": False,
            "native_reviewer_identity_or_result_created": False,
            "control_authority_authenticated_by_this_checker": False,
            "full_collision_or_global_T6_claim": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-actual-ledger", action="store_true")
    for name in ("ledger", "certificate", "bounds", "producer", "context", "report"):
        parser.add_argument("--" + name, type=Path)
    parser.add_argument("--parent-post-run-authorization-note")
    options = parser.parse_args()
    if not options.verify_actual_ledger:
        print(json.dumps({"status": "CHECKER_READY_NO_ACTUAL_P17_COMPUTATION",
                          "requires_parent_post_run_authorization": True,
                          "task_id": TASK, "publication_id": PUBLICATION}))
        return
    need(type(options.parent_post_run_authorization_note) is str
         and bool(options.parent_post_run_authorization_note.strip()),
         "explicit parent post-run authorization note required")
    need(all(getattr(options, name) is not None for name in
             ("ledger", "certificate", "bounds", "producer", "context", "report")),
         "all explicit verification paths required")
    need(not options.report.exists(), "refuse to overwrite verification evidence")
    result = verify_actual_ledger(options.ledger, options.certificate, options.bounds,
                                  options.producer, options.context)
    result["parent_post_run_authorization_note"] = options.parent_post_run_authorization_note
    options.report.parent.mkdir(parents=True, exist_ok=True)
    with options.report.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "report": str(options.report),
                      "fixed_labels_verified": result["fixed_labels_independently_verified"],
                      "full_collision_or_global_T6_claim": False}))


if __name__ == "__main__":
    try:
        main()
    except (VerificationFailure, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"status": "FAIL_HARD", "error": str(error),
                          "no_pass_or_empty_class_claim": True}))
        raise SystemExit(1)
