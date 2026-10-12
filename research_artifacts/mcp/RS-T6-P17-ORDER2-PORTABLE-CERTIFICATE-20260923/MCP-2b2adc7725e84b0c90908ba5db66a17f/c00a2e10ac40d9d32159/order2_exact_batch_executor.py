#!/usr/bin/env python3
"""Exact producer for the remaining 271 literal relaxed order-two patterns.

Construction reuses our frozen q2-1 implementation; default entry is readiness
only. No native API, old author checker, p19 code or independent consumer is
imported. No case preparation/search is permitted before the actual dynamic
native receipts and full-byte Source scope proof have been checked.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
import time

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "t6-p17-order2-q2-1-own-execution-20261012"
INPUT = OLD / "source-inputs/exact-source/research_artifacts/T6_P17_ORDER1_SUPPORT_20260923"
TASK = "RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923"
PUB = "TP2-33BFE7DD84657DAB803C"
ACTOR = "EM-T6-B4F89F"
SID = "MCP-2b2adc7725e84b0c90908ba5db66a17f"
RA = "RA-B6662BE3C64EEFC2AA156A87"
PORTABLE_SHA = "7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce"
PROBLEM_SHA = "a16356adfd5c1763ed0c0426b381d89f70f0c51736335687578f1b9a5c63db0d"
PRIOR_SOURCE = "c406e50f16d8e1d3ba359f3291299170d7940bad"
PRIOR_LEDGER_SHA = "0cacbc773fc6f4bb995f36ad127aa07fd7cfa5bf6e79195a2b78db3549da016c"
REUSED_OWN_CODE_SHA = "401462459bcbb2c72ba9da858f17918545c08157db60b34dcda2b86eadd203e6"
FORBIDDEN_RUN = "RUN-487a00106ee481b05e05902d"
FORBIDDEN_CLAIM = "MCP-280ddc7735532406ab95a2ba"
SCOPE = "ALL_REMAINING_271_LITERAL_RELAXED_ORDER2_PATTERNS"
P, N, BUDGET = 17, 16, 2331
PER_CASE_NODES, PER_CASE_EDGES, ALL_EDGES = 136, 272, 73712
COMPACT_ENCODING = "COMPACT_INDEXED_TWO_CHOICE_TREE_V1"


class InvariantError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise InvariantError(message)


def nofloat(_value):
    raise InvariantError("Floating or nonfinite JSON is forbidden")


def integer(value):
    require(type(value) is str and bool(value)
            and (value.isdecimal() or (value[0] == "-" and value[1:].isdecimal())),
            "Expected decimal-string scientific integer")
    return int(value)


def rat(value):
    require(type(value) is list and len(value) == 2, "Malformed rational pair")
    numerator, denominator = map(integer, value)
    require(denominator > 0, "Nonpositive rational denominator")
    return Fraction(numerator, denominator)


def pair(value):
    value = Fraction(value)
    return [str(value.numerator), str(value.denominator)]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def read(path, sha=None):
    raw = Path(path).read_bytes()
    require(sha is None or digest(raw) == sha, "Input or evidence SHA256 mismatch: " + str(path))
    return json.loads(raw, parse_float=nofloat, parse_constant=nofloat,
                      object_pairs_hook=unique_object)


def write_new(path, value, compact=False):
    path = Path(path)
    raw = (json.dumps(value, separators=(",", ":")) if compact
           else json.dumps(value, indent=2)) + "\n"
    raw = raw.encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(raw)
    return {"path": str(path.relative_to(HERE)), "bytes": len(raw),
            "sha256": digest(raw), "git_blob_sha1": blob(raw)}


def dot(left, right):
    require(len(left) == len(right), "Vector dimension mismatch")
    return sum((x * y for x, y in zip(left, right)), Fraction(0))


def det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    require(n > 0 and all(len(row) == n for row in a), "Determinant dimensions")
    previous, sign = 1, 1
    for k in range(n - 1):
        pivot = next((j for j in range(k, n) if a[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                q, r = divmod(value * a[i][j] - a[i][k] * a[k][j], previous)
                require(r == 0, "Nonexact Bareiss division")
                a[i][j] = q
            a[i][k] = 0
        previous = value
    return sign * a[-1][-1]


def modular_solve(matrix, rhs, modulus):
    n = len(matrix)
    require(len(rhs) == n and all(len(row) == n for row in matrix), "Modular dimensions")
    a = [[x % modulus for x in row] + [rhs[i] % modulus]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k] % P != 0), None)
        require(pivot is not None, "Missing unit modular pivot")
        a[k], a[pivot] = a[pivot], a[k]
        inverse = pow(a[k][k], -1, modulus)
        a[k] = [(x * inverse) % modulus for x in a[k]]
        for i in range(n):
            if i != k:
                multiplier = a[i][k]
                a[i] = [(x - multiplier * y) % modulus for x, y in zip(a[i], a[k])]
    result = [a[i][-1] for i in range(n)]
    require(all((sum(x * y for x, y in zip(row, result)) - target) % modulus == 0
                for row, target in zip(matrix, rhs)), "Modular solve invariant")
    return result


def factors(value):
    answer, trial = [], 2
    while trial * trial <= value:
        if value % trial == 0:
            answer.append(trial)
            while value % trial == 0:
                value //= trial
        trial += 1
    if value > 1:
        answer.append(value)
    return answer


def native_descriptor(context, name):
    refs = context.get("actual_receipts", {})
    if name in refs:
        descriptor = refs[name]
    else:
        descriptor = {"path": context.get("native_" + name + "_receipt_path"),
                      "sha256": context.get("native_" + name + "_receipt_sha256")}
    require(type(descriptor) is dict and type(descriptor.get("path")) is str
            and type(descriptor.get("sha256")) is str, "Missing dynamic " + name + " receipt descriptor")
    return descriptor


def success_receipt(descriptor):
    value = read(descriptor["path"], descriptor["sha256"])
    bridge = value["bridge_receipt"]
    require(bridge["status"] == "SUCCEEDED" and bridge.get("error") is None,
            "Actual native receipt is not successful")
    return bridge["receipt"]


def check_lease(context):
    value = context["owner_lease_until"]
    require(type(value) is str and bool(value), "Actual owner lease required")
    lease = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(lease.tzinfo is not None and lease > datetime.now(timezone.utc), "Actual owner lease expired")


def check_binding(binding, context):
    require(binding["executor_role"] == "RESEARCHER", "Wrong native executor role")
    for name, expected in (("researcher_id", ACTOR), ("session_id", SID),
                           ("publication_id", PUB), ("claim_id", context["claim_id"]),
                           ("execution_record_id", context["execution_record_id"])):
        require(binding[name] == expected, "Native binding mismatch: " + name)
    require(binding["allowed_outputs"] == context["allowed_outputs"], "Native allowed outputs mismatch")
    if "owner_lease_until" in binding:
        require(binding["owner_lease_until"] == context["owner_lease_until"], "Native lease mismatch")


def authorize(context_path):
    context_raw = Path(context_path).read_bytes()
    context = read(context_path)
    require(context["task_id"] == TASK and context["publication_id"] == PUB, "Wrong task/publication")
    require(context["researcher_id"] == ACTOR and context["session_id"] == SID, "Wrong actual actor/SID")
    require(context["native_authorized"] is True, "Native context is not authorized")
    require(context["run_id"] != FORBIDDEN_RUN and context["claim_id"] != FORBIDDEN_CLAIM,
            "Released q2-1 claim/run is forbidden for new work")
    require(type(context["run_generation"]) is int and context["run_generation"] > 0,
            "Actual run generation required")
    require(context.get("fenced_by_claim_id") is None, "Current context is fenced")
    require(context["scope"] == SCOPE and context["excluded_replay_pattern_ids"] == ["q2-1"],
            "Context must authorize precisely the remaining literal 271")
    require(context["include_outside_domain_patterns"] is True, "Literal outside patterns cannot be skipped")
    require(context["Source_session_RA_ER_publication_book_full_bytes_verified"] is True,
            "Full actual Source scope must be checked before mathematics")
    prepared_receipt = success_receipt(native_descriptor(context, "prepare"))
    prepared = prepared_receipt["result"]
    claimed = success_receipt(native_descriptor(context, "claim"))["result"]
    opened = success_receipt(native_descriptor(context, "open"))
    require(claimed["authorized"] is True and opened["result"]["authorized"] is True, "Claim/open denied")
    for result in (claimed, opened["result"]):
        require(result["authorization_authority"] == "CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM",
                "Wrong native authorization authority")
        require(result["task_id"] == TASK, "Native result task mismatch")
        check_binding(result["execution_binding"], context)
    if prepared.get("schema") == "ENTERPRISE_MATH_CONTINUATION_PREPARE_V1":
        require(prepared["execution_authorized"] is False,
                "Typed preparation must not be represented as execution authorization")
        executor = prepared_receipt["executor_binding"]
        require(executor["researcher_id"] == ACTOR and executor["session_id"] == SID
                and executor["activity_id"] == RA, "Typed continuation executor mismatch")
        # A typed continuation prepares the existing executor but does not
        # allocate the later claim/ER. The actual new claim/open bindings and
        # Source proof below must join those identifiers independently.
    else:
        intent = prepared["intent"]
        require(intent["claim_id"] == context["claim_id"]
                and intent["execution_record_id"] == context["execution_record_id"],
                "Prepare claim/ER chain mismatch")
    run = opened["run"]
    for name, expected in (("run_id", context["run_id"]), ("task_id", TASK),
                           ("publication_id", PUB), ("researcher_id", ACTOR),
                           ("session_id", SID), ("claim_id", context["claim_id"])):
        require(run[name] == expected, "Open run mismatch: " + name)
    require(run["generation"] == context["run_generation"] and run["fenced_by_claim_id"] is None,
            "Run generation/fence mismatch")
    proof_ref = context.get("source_scope_proof") or {
        "path": context.get("Source_scope_proof_path"),
        "sha256": context.get("Source_scope_proof_sha256")}
    require(type(proof_ref.get("path")) is str and type(proof_ref.get("sha256")) is str,
            "Source scope proof descriptor required")
    proof = read(proof_ref["path"], proof_ref["sha256"])
    require(proof["Source_session_RA_ER_publication_book_full_bytes_verified"] is True
            and proof["own_actor"] == ACTOR and proof["own_SID"] == SID
            and proof["native_claim_authorized"] is True, "Source scope identity/authority mismatch")
    check_binding(proof["execution_binding"], context)
    source_files = proof["files"]
    require(type(source_files) is list and len(source_files) >= 5, "Five full Source scope files required")
    kinds = set()
    for entry in source_files:
        raw = Path(entry["local_path"]).read_bytes()
        require(len(raw) == entry["bytes"] and digest(raw) == entry["sha256"]
                and blob(raw) == entry["git_blob_sha1"].split(":")[-1], "Source scope raw byte mismatch")
        source_path = entry["path"]
        if source_path.startswith("research_session_records/"):
            kinds.add("session")
        elif source_path.startswith("research_activity_records/"):
            kinds.add("activity")
        elif source_path.startswith("research_execution_records/"):
            record = json.loads(raw, parse_float=nofloat, parse_constant=nofloat)
            require(record["execution_record_id"] == context["execution_record_id"], "Wrong Source ER")
            kinds.add("execution")
        elif source_path.startswith("research_task_records/"):
            record = json.loads(raw, parse_float=nofloat, parse_constant=nofloat)
            require(record["task_id"] == TASK and record["publication_id"] == PUB, "Wrong Source publication")
            kinds.add("publication")
        elif source_path.startswith("research_tasks/"):
            kinds.add("book")
    require(kinds == {"session", "activity", "execution", "publication", "book"}, "Incomplete Source scope kinds")
    check_lease(context)
    return context, {"context_sha256": digest(context_raw), "Source_scope_proof": proof_ref,
                     "actual_receipts": {name: native_descriptor(context, name)
                                         for name in ("prepare", "claim", "open")},
                     "native_authority_granted_by_local_code": False}


def expected_pattern_definitions():
    patterns = []
    patterns += [("q2-" + str(r), [[2, r]], []) for r in range(1, 17)]
    patterns += [("same-q1-" + str(a) + "-" + str(b), [[1, a], [1, b]], [])
                 for a in range(1, 17) for b in range(a, 17)]
    patterns += [("opposite-q1-" + str(a) + "-" + str(b), [[1, a]], [[1, b]])
                 for a in range(1, 17) for b in range(a + 1, 17)]
    return patterns


def atom_record(q, r):
    require(q in (1, 2) and 1 <= r <= 16, "Wrong order-two atom")
    cofactor = P * q + r
    fs = factors(cofactor)
    return {"q": str(q), "r": str(r), "cofactor": str(cofactor),
            "denominator": str(P * cofactor), "mass": str(P * cofactor - 1),
            "factorization": list(map(str, fs)), "maximal_prime": str(max([P] + fs))}


def derive_case(case, expected):
    pattern_id, plus_atoms, minus_atoms = expected
    require(case["id"] == pattern_id and case["status"] == "INPUT_ONLY_NOT_SOLVED", "Wrong original case state/ID")
    encoded_plus = [[str(q), str(r)] for q, r in plus_atoms]
    encoded_minus = [[str(q), str(r)] for q, r in minus_atoms]
    require(case["positive_atoms"] == encoded_plus and case["negative_atoms"] == encoded_minus, "Pattern atom mismatch")
    require(sum(q for q, r in plus_atoms + minus_atoms) == 2, "Vertical order is not two")
    require(not set(map(tuple, plus_atoms)).intersection(map(tuple, minus_atoms)), "Nonprimitive shared vertical atom")
    plus_records = [atom_record(q, r) for q, r in plus_atoms]
    minus_records = [atom_record(q, r) for q, r in minus_atoms]
    plus_cost = sum(P * (P * q + r) - 1 for q, r in plus_atoms)
    minus_cost = sum(P * (P * q + r) - 1 for q, r in minus_atoms)
    plus_budget, minus_budget = BUDGET - plus_cost, BUDGET - minus_cost
    require(plus_budget >= 0 and minus_budget >= 0, "Negative residual budget")
    radius = plus_budget ** 2 + minus_budget ** 2
    targets = []
    for k in range(1, 7):
        modulus = P ** k
        target = (sum(pow(P * q + r, -k, modulus) for q, r in minus_atoms)
                  - sum(pow(P * q + r, -k, modulus) for q, r in plus_atoms)) % modulus
        targets.append(target)
    require(integer(case["q0_positive_budget"]) == plus_budget
            and integer(case["q0_negative_budget"]) == minus_budget
            and integer(case["radius_squared"]) == radius
            and list(map(integer, case["mixed_targets"])) == targets, "Original per-pattern budget/target mismatch")
    largest = max([P] + [int(x["maximal_prime"]) for x in plus_records + minus_records])
    return {"pattern_id": pattern_id, "positive_atoms": encoded_plus, "negative_atoms": encoded_minus,
            "positive_vertical_atoms": plus_records, "negative_vertical_atoms": minus_records,
            "positive_vertical_mass": str(plus_cost), "negative_vertical_mass": str(minus_cost),
            "q0_positive_budget": str(plus_budget), "q0_negative_budget": str(minus_budget),
            "radius_squared": str(radius), "mixed_targets": list(map(str, targets)),
            "maximal_p17_admissible": largest <= P, "largest_vertical_prime": str(largest),
            "literal_relaxed_classification_required": True}


def validate_prior_input():
    prior_path = OLD / "Q2_1_COMPLETE_NEW_LEDGER.json"
    prior = read(prior_path, PRIOR_LEDGER_SHA)
    evidence_path = OLD / "SOURCE_ALL_BYTES_VERIFIED.json"
    evidence = read(evidence_path)
    require(evidence["status"] == "PASS" and evidence["source_commit"] == PRIOR_SOURCE
            and evidence["all11_source_files_byte_sha256_gitblob_verified"] is True, "Prior actual Source custody not verified")
    pinned = [x for x in evidence["source_files"]
              if x["path"].endswith("/Q2_1_COMPLETE_NEW_LEDGER.json")]
    require(len(pinned) == 1 and pinned[0]["sha256"] == PRIOR_LEDGER_SHA
            and pinned[0]["native_pins_match"] is True, "Prior q2-1 Source ledger binding")
    require(prior["pattern_id"] == "q2-1" and prior["outcome"] == "EMPTY"
            and prior["complete_traversal"] is True, "Prior q2-1 input scope mismatch")
    return {"pattern_id": "q2-1", "source_commit": PRIOR_SOURCE,
            "ledger_sha256": PRIOR_LEDGER_SHA, "immutable_url": pinned[0]["immutable_url"],
            "custody_evidence_sha256": digest(evidence_path.read_bytes()),
            "input_only": True, "replayed": False, "nodes_copied_into_new_payload": False,
            "counts_included_in_new_compute_totals": False}


def validate_common_once(context):
    portable = read(INPUT / "portable_input.json", PORTABLE_SHA)
    problem = read(INPUT / "order2_problem.json", PROBLEM_SHA)
    require(problem["common_basis_sha256"] == PORTABLE_SHA, "Problem/common join mismatch")
    expected = expected_pattern_definitions()
    require(len(expected) == len(problem["cases"]) == 272, "Literal family count mismatch")
    cases = [derive_case(case, declaration) for case, declaration in zip(problem["cases"], expected)]
    cases = [case for case in cases if case["pattern_id"] != "q2-1"]
    require(len(cases) == 271 and len({x["pattern_id"] for x in cases}) == 271, "Remaining pattern ID mismatch")
    if "authorized_remaining_pattern_ids" in context:
        require(context["authorized_remaining_pattern_ids"] == [x["pattern_id"] for x in cases], "Actual context pattern IDs mismatch")
    require(sum(x["maximal_p17_admissible"] for x in cases) == 153, "Actual-domain pattern count mismatch")
    require(sum(not x["maximal_p17_admissible"] for x in cases) == 118, "Outside-domain pattern count mismatch")
    weights = [P * s - 1 for s in range(1, N + 1)]
    require(list(map(integer, portable["weights"])) == weights
            and list(map(integer, problem["weights"])) == weights, "Common weights mismatch")
    moduli = [P ** k for k in range(1, 7)]
    coefficients = [[pow(s, -k, P ** k) for s in range(1, N + 1)] for k in range(1, 7)]
    require(list(map(integer, problem["moduli"])) == moduli
            and [[integer(x) for x in row] for row in problem["coefficients"]] == coefficients, "Mixed input coefficients mismatch")
    U = [[integer(x) for x in row] for row in portable["unweighted_basis"]]
    B = [[integer(x) for x in row] for row in portable["weighted_basis"]]
    require(len(U) == len(B) == N and all(len(row) == N for row in U + B), "Common basis dimensions")
    require(B == [[w * x for w, x in zip(weights, row)] for row in U], "Common weighted basis mismatch")
    determinant = det(U)
    require(abs(determinant) == P ** 21, "Mixed-kernel index mismatch")
    require(all(sum(x * a for x, a in zip(row, coefficients[k])) % moduli[k] == 0
                for row in U for k in range(6)), "Common basis outside mixed kernel")
    unit_minor = det([[coefficients[k][s] % P for s in range(6)] for k in range(6)]) % P
    require(unit_minor != 0, "Mixed kernel saturation not established")
    D = list(map(rat, portable["gram_schmidt_squared"]))
    mu = [[rat(x) for x in row] for row in portable["mu"]]
    require(len(D) == len(mu) == N and all(len(row) == N for row in mu), "Common orthogonal dimensions")
    require(all(D[i] > 0 and mu[i][i] == 1 and all(mu[i][j] == 0 for j in range(i + 1, N))
                for i in range(N)), "Common orthogonal triangular structure")
    require(all(dot(B[i], B[j]) == sum((mu[i][k] * mu[j][k] * D[k]
                                       for k in range(N)), Fraction(0))
                for i in range(N) for j in range(N)), "Common exact Gram identity mismatch")
    maximum_radius = max(integer(x["radius_squared"]) for x in cases)
    require(all(d > 2 * maximum_radius for d in D), "One-nonpreferred/node bound unavailable")
    prior = validate_prior_input()
    common = {"common_input_sha256": PORTABLE_SHA, "order2_problem_sha256": PROBLEM_SHA,
              "kernel_determinant": str(determinant), "unit_minor_mod17": str(unit_minor),
              "max_remaining_radius_squared": str(maximum_radius),
              "all_D_gt_twice_max_radius": True, "common_validation_count": 1,
              "portable_r1_particular_and_centers_used": False,
              "max_internal_nodes_per_pattern": PER_CASE_NODES,
              "max_candidate_checks_per_pattern": PER_CASE_EDGES,
              "max_all_new_candidate_checks": ALL_EDGES,
              "both_choices_always_checked_not_omitted_by_bound": True}
    return common, cases, weights, U, B, D, mu, coefficients, moduli, prior


def check_mixed(vector, coefficients, targets, moduli, label):
    residues = [sum(x * a for x, a in zip(vector, coefficients[k])) % moduli[k]
                for k in range(6)]
    require(residues == targets, label + ": true mixed congruence identity failure")
    return residues


def construct_case_input(case, weights, U, B, D, mu, coefficients, moduli):
    plus = [(integer(q), integer(r)) for q, r in case["positive_atoms"]]
    minus = [(integer(q), integer(r)) for q, r in case["negative_atoms"]]
    modulus = P ** 6
    matrix = [[pow(s, -k, modulus) for s in range(1, 7)] for k in range(1, 7)]
    target = [(sum(pow(P * q + r, -k, modulus) for q, r in minus)
               - sum(pow(P * q + r, -k, modulus) for q, r in plus)) % modulus
              for k in range(1, 7)]
    original = modular_solve(matrix, target, modulus) + [0] * (N - 6)
    targets = list(map(integer, case["mixed_targets"]))
    check_mixed(original, coefficients, targets, moduli, case["pattern_id"] + " original")
    weighted = [w * x for w, x in zip(weights, original)]
    inner = []
    for i in range(N):
        inner.append(dot(weighted, B[i]) - sum((mu[i][j] * inner[j] for j in range(i)), Fraction(0)))
    centers = [inner[i] / D[i] for i in range(N)]
    require(dot(weighted, weighted) == sum((D[i] * centers[i] ** 2 for i in range(N)), Fraction(0)),
            "Original affine norm identity")
    shift, trace = [0] * N, []
    for i in range(N - 1, -1, -1):
        center = centers[i] + sum((mu[j][i] * shift[j] for j in range(i + 1, N)), Fraction(0))
        quotient, remainder = divmod(center.numerator, center.denominator)
        chosen = -quotient - 1 if 2 * remainder >= center.denominator else -quotient
        shift[i] = chosen
        trace.append({"index": i, "center": pair(center), "quotient": str(quotient),
                      "remainder": str(remainder), "denominator": str(center.denominator), "z": str(chosen)})
    particular = [original[s] + sum(shift[i] * U[i][s] for i in range(N)) for s in range(N)]
    translated = [centers[i] + shift[i]
                  + sum((mu[j][i] * shift[j] for j in range(i + 1, N)), Fraction(0)) for i in range(N)]
    require(all(abs(c) <= Fraction(1, 2) for c in translated), "Babai cell identity")
    check_mixed(particular, coefficients, targets, moduli, case["pattern_id"] + " translated")
    weighted = [w * x for w, x in zip(weights, particular)]
    require(dot(weighted, weighted) == sum((D[i] * translated[i] ** 2 for i in range(N)), Fraction(0)),
            "Translated affine norm identity")
    for i in range(N):
        require(dot(weighted, B[i]) == sum((mu[i][j] * D[j] * translated[j] for j in range(N)), Fraction(0)),
                "Translated affine Gram identity")
    return original, particular, centers, translated, shift, trace


def completion_obligations(case, vector, plus_mass, minus_mass):
    plus = case["positive_vertical_atoms"]
    minus = case["negative_vertical_atoms"]
    left_plus = integer(case["q0_positive_budget"]) - plus_mass
    left_minus = integer(case["q0_negative_budget"]) - minus_mass
    require(left_plus >= 0 and left_minus >= 0, "Survivor residual budget")
    moments = [Fraction(len(plus) - len(minus) + sum(vector))]
    for k in range(1, 7):
        value = sum((Fraction(1, integer(a["denominator"]) ** k) for a in plus), Fraction(0))
        value -= sum((Fraction(1, integer(a["denominator"]) ** k) for a in minus), Fraction(0))
        value += sum((Fraction(u, (P * s) ** k) for s, u in enumerate(vector, 1)), Fraction(0))
        require(value.denominator % P != 0, "Uncanceled p17 pole in survivor")
        moments.append(value)
    cuts = [{"k": k, "M_k": pair(value),
             "lower": pair(-Fraction(left_plus, 2 ** k)),
             "upper": pair(Fraction(left_minus, 2 ** k)),
             "passes": -Fraction(left_plus, 2 ** k) <= value <= Fraction(left_minus, 2 ** k)}
            for k, value in enumerate(moments)]
    return {"remaining_positive_budget": str(left_plus), "remaining_negative_budget": str(left_minus),
            "moments_M0_to_M6": list(map(pair, moments)), "necessary_completion_cuts": cuts,
            "status": "OPEN_AFTER_NECESSARY_CUTS" if all(x["passes"] for x in cuts)
                      else "EXCLUDED_BY_NAMED_NECESSARY_CUT",
            "local_survivor_retained": True,
            "completion_equations": "sum_a t_a/a^k=-M_k for k=0..6; a>=2,17-free; separate (a-1)-weighted residual masses",
            "lower_prime_carrier_allowed_only_if_maximal_p17_admissible": case["maximal_p17_admissible"],
            "full_collision_claim": False}


def classify_case(case, common, context, weights, U, B, D, mu, coefficients, moduli):
    started = time.perf_counter_ns()
    original, particular, original_centers, alpha, shift, shift_trace = construct_case_input(
        case, weights, U, B, D, mu, coefficients, moduli)
    radius = integer(case["radius_squared"])
    plus_budget = integer(case["q0_positive_budget"])
    minus_budget = integer(case["q0_negative_budget"])
    targets = list(map(integer, case["mixed_targets"]))
    nodes, survivors = [], []
    counts = {"full_sphere_leaves": 0, "budget_pruned": 0}
    z = [0] * N

    def visit(i, partial, nonpreferred_count):
        node_id = len(nodes)
        require(node_id < PER_CASE_NODES, "Node bound failure; not an EMPTY outcome")
        node = {"id": node_id, "index": i, "suffix": list(map(str, z[i + 1:])),
                "partial_norm": pair(partial), "edges": [],
                "nonpreferred_count_prefix": nonpreferred_count}
        nodes.append(node)
        center = alpha[i] + sum((mu[j][i] * z[j] for j in range(i + 1, N)), Fraction(0))
        q, rem = divmod(center.numerator, center.denominator)
        require(center.numerator == q * center.denominator + rem and 0 <= rem < center.denominator,
                "Euclidean floor identity")
        preferred = -q - 1 if 2 * rem >= center.denominator else -q
        node.update(center=pair(center),
                    floor={"quotient": str(q), "remainder": str(rem), "denominator": str(center.denominator)},
                    preferred_z=str(preferred))
        # Both integers are checked even at integral centers; the extra neighbor
        # then has distance one and is safely rejected by the exact norm.
        for value in (-q - 1, -q):
            z[i] = value
            contribution = D[i] * (value + center) ** 2
            total = partial + contribution
            require(contribution >= 0, "Negative orthogonal contribution")
            nonpreferred = value != preferred
            if nonpreferred:
                require(contribution >= D[i] / 4, "Nonpreferred quarter-cost invariant")
            edge = {"z": str(value), "partial_norm": pair(total),
                    "nonpreferred": nonpreferred, "contribution": pair(contribution)}
            node["edges"].append(edge)
            if total > radius:
                edge["action"] = "NORM_PRUNED"
            else:
                next_count = nonpreferred_count + int(nonpreferred)
                require(next_count <= 1, "One-nonpreferred theorem violated; no branch may be omitted")
                if i > 0:
                    edge["action"] = "CHILD"
                    edge["child"] = visit(i - 1, total, next_count)
                else:
                    counts["full_sphere_leaves"] += 1
                    vector = [particular[s] + sum(z[t] * U[t][s] for t in range(N)) for s in range(N)]
                    weighted = [w * u for w, u in zip(weights, vector)]
                    require(dot(weighted, weighted) == total, "Full leaf integer/GS norm identity")
                    residues = check_mixed(vector, coefficients, targets, moduli, case["pattern_id"] + " leaf")
                    positive = sum(max(x, 0) for x in weighted)
                    negative = sum(max(-x, 0) for x in weighted)
                    edge.update(vector=list(map(str, vector)), positive_mass=str(positive), negative_mass=str(negative),
                                mixed_residues=list(map(str, residues)), weighted_norm=pair(total),
                                positive_budget=str(plus_budget), negative_budget=str(minus_budget))
                    if positive > plus_budget or negative > minus_budget:
                        edge["action"] = "BUDGET_PRUNED"
                        counts["budget_pruned"] += 1
                    else:
                        edge["action"] = "SURVIVOR"
                        survivors.append({"q0": list(map(str, vector)),
                                          "q0_positive_mass": str(positive), "q0_negative_mass": str(negative),
                                          "total_positive_mass_with_atoms": str(positive + integer(case["positive_vertical_mass"])),
                                          "total_negative_mass_with_atoms": str(negative + integer(case["negative_vertical_mass"])),
                                          "mixed_residues": list(map(str, residues)),
                                          "full_H0_lower_prime_completion": "OPEN_NOT_A_FULL_COLLISION",
                                          "completion": completion_obligations(case, vector, positive, negative)})
        return node_id

    root = visit(N - 1, Fraction(0), 0)
    edge_count = sum(len(x["edges"]) for x in nodes)
    require(all(len(x["edges"]) == 2 for x in nodes) and edge_count == 2 * len(nodes)
            and len(nodes) <= PER_CASE_NODES and edge_count <= PER_CASE_EDGES, "Complete two-choice tree bound")
    require(len({tuple(x["q0"]) for x in survivors}) == len(survivors), "Duplicate survivor")
    return {"schema": "T6_P17_ORDER2_EXACT_TWO_CHOICE_CASE_LEDGER_V1",
            "task_id": TASK, "publication_id": PUB, **case,
            "outcome": "LOCAL_KERNEL" if survivors else "EMPTY",
            "scope": "ONE_LITERAL_RELAXED_REMAINING_ORDER2_PATTERN",
            "particular_q0": list(map(str, particular)), "affine_centers": list(map(pair, alpha)),
            "original_particular_q0": list(map(str, original)),
            "original_affine_centers": list(map(pair, original_centers)),
            "lattice_translation": list(map(str, shift)), "translation_divrem_trace": shift_trace,
            "root": root, "nodes": nodes, "survivors": survivors, "node_count": len(nodes),
            "edge_count": edge_count, "pruned_edges": sum(e["action"] == "NORM_PRUNED" for x in nodes for e in x["edges"]),
            **counts, "complete_traversal": True, "resource_exhausted": False,
            "literal_relaxed_outcome_even_if_outside_domain": True,
            "common_input_sha256": PORTABLE_SHA, "order2_problem_sha256": PROBLEM_SHA,
            "weights": list(map(str, weights)), "moduli": list(map(str, moduli)),
            "coefficients": [[str(a) for a in row] for row in coefficients],
            "exact_scientific_arithmetic": "PYTHON_INT_AND_FRACTION_WITH_SAVED_EUCLIDEAN_DIVREM",
            "elapsed_nanoseconds": time.perf_counter_ns() - started,
            "own_actual_control": {"researcher_id": ACTOR, "session_id": SID,
                                  "claim_id": context["claim_id"], "execution_record_id": context["execution_record_id"],
                                  "run_id": context["run_id"], "run_generation": context["run_generation"]},
            "global_T6_complete": False}


def compact_projection(ledger):
    """Project a saved verbose record; never reconstruct or rerun its DFS."""
    case_keys = ("pattern_id", "outcome", "particular_q0", "root", "survivors",
                 "complete_traversal", "resource_exhausted", "maximal_p17_admissible",
                 "largest_vertical_prime", "positive_atoms", "negative_atoms",
                 "positive_vertical_mass", "negative_vertical_mass", "q0_positive_budget",
                 "q0_negative_budget", "radius_squared", "mixed_targets",
                 "literal_relaxed_outcome_even_if_outside_domain")
    result = {key: ledger[key] for key in case_keys}
    result["certificate_encoding"] = COMPACT_ENCODING
    leaf_keys = ("vector", "positive_mass", "negative_mass", "mixed_residues",
                 "weighted_norm", "positive_budget", "negative_budget")
    projected_nodes = []
    for node in ledger["nodes"]:
        edges = []
        require(len(node["edges"]) == 2, "Cannot encode an incomplete two-choice node")
        for edge in node["edges"]:
            action = edge["action"]
            require(action in ("CHILD", "NORM_PRUNED", "BUDGET_PRUNED", "SURVIVOR"),
                    "Unknown saved edge action")
            item = {"z": edge["z"], "action": action}
            if action == "CHILD":
                item["child"] = edge["child"]
            elif action in ("BUDGET_PRUNED", "SURVIVOR"):
                item.update({key: edge[key] for key in leaf_keys})
            edges.append(item)
        projected_nodes.append({"id": node["id"], "index": node["index"], "edges": edges})
    result["nodes"] = projected_nodes
    return result


def write_compact_certificate(batch, proof_entry):
    projected = []
    require(len(batch["case_artifact_manifest"]) == len(batch["case_ledgers"]) == 271,
            "Cannot compact an incomplete batch")
    for ledger, entry in zip(batch["case_ledgers"], batch["case_artifact_manifest"]):
        raw = (HERE / entry["path"]).read_bytes()
        require(len(raw) == entry["bytes"] and digest(raw) == entry["sha256"]
                and blob(raw) == entry["git_blob_sha1"], "Saved verbose original pin mismatch")
        saved = read(HERE / entry["path"], entry["sha256"])
        require(saved == ledger and saved["pattern_id"] == entry["pattern_id"],
                "Saved verbose record differs from batch record")
        # This is an encoding of the saved tree, not a new scientific search.
        projected.append(compact_projection(saved))
    certificate = {key: batch[key] for key in
                   ("task_id", "publication_id", "status", "completed_pattern_ids", "new_pattern_count",
                    "prime17_admissible_count", "outside_domain_count", "outside_patterns_classified_not_skipped",
                    "common_validation", "prior_q2_1", "classification_counts", "total_node_count",
                    "total_edge_count", "survivor_count", "complete_traversal", "resource_exhausted",
                    "own_actual_control", "control_evidence", "producer_sha256", "family_hard_target_complete",
                    "family_integration_and_Driver_review_required", "global_T6_complete", "p19_replayed",
                    "q2_1_replayed", "construction_credit")}
    certificate.update(schema="T6_P17_ORDER2_REMAINING271_COMPACT_CERTIFICATE_V1",
                       certificate_encoding=COMPACT_ENCODING, case_ledgers=projected,
                       verbose_complete_proof_artifact=proof_entry,
                       case_artifact_manifest=batch["case_artifact_manifest"],
                       deterministic_projection_of_saved_verbose_originals=True,
                       scientific_reexecution_for_encoding=False)
    return write_new(HERE / "BATCH_COMPACT_CERTIFICATE.json", certificate, compact=True)


def write_lossless_archive(entries):
    """Archive all declared producer output originals, then verify raw bytes."""
    names = [entry["path"] for entry in entries]
    require(len(names) == len(set(names)), "Duplicate declared archive path")
    archive_path = HERE / "COMPLETE_VERBOSE_ORIGINALS.tar.gz"
    with archive_path.open("xb") as output:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w", format=tarfile.USTAR_FORMAT) as archive:
                for entry in entries:
                    path = Path(entry["path"])
                    require(not path.is_absolute() and ".." not in path.parts, "Unsafe declared archive path")
                    raw = (HERE / path).read_bytes()
                    require(len(raw) == entry["bytes"] and digest(raw) == entry["sha256"]
                            and blob(raw) == entry["git_blob_sha1"], "Archive input pin mismatch")
                    info = tarfile.TarInfo(path.as_posix())
                    info.size, info.mtime, info.mode, info.uid, info.gid = len(raw), 0, 0o644, 0, 0
                    info.uname = info.gname = ""
                    archive.addfile(info, io.BytesIO(raw))
    archive_raw = archive_path.read_bytes()
    with tarfile.open(archive_path, mode="r:gz") as archive:
        members = archive.getmembers()
        require([member.name for member in members] == names and all(member.isfile() for member in members),
                "Lossless archive member inventory mismatch")
        for member, entry in zip(members, entries):
            stream = archive.extractfile(member)
            require(stream is not None, "Missing archived original")
            raw = stream.read()
            require(raw == (HERE / entry["path"]).read_bytes()
                    and len(raw) == entry["bytes"] and digest(raw) == entry["sha256"]
                    and blob(raw) == entry["git_blob_sha1"], "Lossless raw-byte roundtrip failed")
    archive_entry = {"path": str(archive_path.relative_to(HERE)), "bytes": len(archive_raw),
                     "sha256": digest(archive_raw), "git_blob_sha1": blob(archive_raw)}
    write_new(HERE / "LOSSLESS_VERBOSE_ARCHIVE_MANIFEST.json",
              {"schema": "T6_REMAINING271_ALL_DECLARED_PRODUCER_OUTPUT_BYTES_ARCHIVE_V1",
               "scope": "271_VERBOSE_CASE_FILES_PLUS_VERBOSE_BATCH_COMPACT_CERTIFICATE_AND_SUMMARY",
               "declared_originals": entries, "archive": archive_entry,
               "all_declared_originals_preserved": True, "raw_byte_roundtrip_verified": True,
               "scientific_reexecution": False, "additional_owner_logs_not_declared_here": True})
    return archive_entry


def execute(context_path):
    context, control_evidence = authorize(context_path)
    require(not (HERE / "BATCH_COMPLETE_PROOF.json").exists()
            and not (HERE / "BATCH_SUMMARY.json").exists(), "Do not repeat completed batch")
    case_dir = HERE / "cases"
    require(not case_dir.exists() or not any(case_dir.iterdir()), "Existing case evidence: require typed recovery, not replay")
    started = time.perf_counter_ns()
    common, cases, weights, U, B, D, mu, coefficients, moduli, prior = validate_common_once(context)
    case_ledgers, artifacts = [], []
    try:
        for case in cases:
            check_lease(context)
            ledger = classify_case(case, common, context, weights, U, B, D, mu, coefficients, moduli)
            require(ledger["pattern_id"] != "q2-1", "Completed input must never be searched")
            entry = write_new(case_dir / (ledger["pattern_id"] + ".json"), ledger)
            artifacts.append({"pattern_id": ledger["pattern_id"], **entry})
            case_ledgers.append(ledger)
    except Exception as error:
        write_new(HERE / "BATCH_FAILURE_NOT_CLASSIFIED.json",
                  {"schema": "T6_REMAINING271_FAIL_HARD_V1", "status": "FAILED_NOT_CLASSIFIED",
                   "error": str(error), "completed_pattern_ids": [x["pattern_id"] for x in case_ledgers],
                   "remaining_unclassified_pattern_ids": [x["pattern_id"] for x in cases[len(case_ledgers):]],
                   "case_artifact_manifest": artifacts, "resource_or_failure_is_not_EMPTY": True,
                   "global_T6_complete": False})
        raise
    ids = [x["pattern_id"] for x in case_ledgers]
    expected_ids = [x["pattern_id"] for x in cases]
    require(ids == expected_ids and len(ids) == 271 and "q2-1" not in ids, "Full remaining-ID coverage failure")
    total_edges = sum(x["edge_count"] for x in case_ledgers)
    total_nodes = sum(x["node_count"] for x in case_ledgers)
    require(total_edges <= ALL_EDGES and total_nodes <= 271 * PER_CASE_NODES, "New batch resource bound failure")
    counts = {"EMPTY": sum(x["outcome"] == "EMPTY" for x in case_ledgers),
              "LOCAL_KERNEL": sum(x["outcome"] == "LOCAL_KERNEL" for x in case_ledgers)}
    require(sum(counts.values()) == 271, "Incomplete classification outcome")
    batch = {"schema": "T6_P17_ORDER2_REMAINING271_BATCH_PROOF_V1",
             "task_id": TASK, "publication_id": PUB, "status": "COMPLETE_REMAINING271_LITERAL_RELAXED_CLASSIFICATION",
             "completed_pattern_ids": ids, "remaining_new_pattern_count": 0,
             "new_pattern_count": 271, "prime17_admissible_count": 153, "outside_domain_count": 118,
             "outside_patterns_classified_not_skipped": True, "common_validation": common,
             "prior_q2_1": prior, "case_ledgers": case_ledgers, "case_artifact_manifest": artifacts,
             "classification_counts": counts, "total_node_count": total_nodes, "total_edge_count": total_edges,
             "survivor_count": sum(len(x["survivors"]) for x in case_ledgers),
             "complete_traversal": True, "resource_exhausted": False,
             "own_actual_control": {"researcher_id": ACTOR, "session_id": SID,
                                   "claim_id": context["claim_id"], "execution_record_id": context["execution_record_id"],
                                   "run_id": context["run_id"], "run_generation": context["run_generation"]},
             "control_evidence": control_evidence, "producer_sha256": digest(Path(__file__).read_bytes()),
             "elapsed_nanoseconds": time.perf_counter_ns() - started,
             "family_hard_target_complete": False, "family_integration_and_Driver_review_required": True,
             "global_T6_complete": False, "p19_replayed": False, "q2_1_replayed": False,
             "construction_credit": {"reused_own_q2_1_code_sha256": REUSED_OWN_CODE_SHA,
                                     "Root_contribution": "Structural branch bound and compact complete certificate design",
                                     "local_helper_native_identity": None,
                                     "shared_owner_nonblind": True,
                                     "independent_consumer_is_separate_not_imported": True}}
    proof_entry = write_new(HERE / "BATCH_COMPLETE_PROOF.json", batch)
    compact_entry = write_compact_certificate(batch, proof_entry)
    summary = {key: batch[key] for key in
               ("schema", "task_id", "publication_id", "status", "completed_pattern_ids", "new_pattern_count",
                "prime17_admissible_count", "outside_domain_count", "classification_counts",
                "total_node_count", "total_edge_count", "survivor_count", "own_actual_control",
                "control_evidence", "producer_sha256", "family_hard_target_complete", "global_T6_complete",
                "q2_1_replayed", "p19_replayed", "construction_credit")}
    summary["complete_proof_artifact"] = proof_entry
    summary["compact_certificate_artifact"] = compact_entry
    summary["case_artifact_manifest"] = artifacts
    summary["prior_q2_1"] = prior
    summary_entry = write_new(HERE / "BATCH_SUMMARY.json", summary)
    archive_entry = write_lossless_archive(artifacts + [proof_entry, compact_entry, summary_entry])
    print(json.dumps({key: summary[key] for key in
                      ("status", "new_pattern_count", "classification_counts",
                       "total_node_count", "total_edge_count", "survivor_count")}
                     | {"lossless_archive": archive_entry}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--context", type=Path, default=HERE / "CURRENT_NATIVE_EXECUTION_CONTEXT.json")
    args = parser.parse_args()
    if not args.execute:
        print(json.dumps({"status": "CODE_READY_NO_PREPARATION_OR_SEARCH",
                          "requires_actual_dynamic_native_context": True,
                          "prior_q2_1_input_only_not_replayed": True}))
        return
    execute(args.context)


if __name__ == "__main__":
    try:
        main()
    except (InvariantError, OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"status": "FAIL_HARD_NOT_CLASSIFIED", "error": str(error),
                          "failure_or_resource_is_not_EMPTY": True}))
        raise SystemExit(1)
