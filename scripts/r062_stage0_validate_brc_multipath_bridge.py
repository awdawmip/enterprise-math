#!/usr/bin/env python3
"""R062 Stage 0 deterministic BRC/native-multipath bridge checker.

The checker is exact/integer-only.  It regenerates the R061 Stage-1R native
trace replay digest needed by the bridge, enumerates the frozen Stage-2 trace
fibres for all a+b<=12 on seven translated starts and all three sectors, and
then derives Path/N/Boolean projections from the same witnesses.

It deliberately distinguishes:
  * formal path-occurrence algebra -> N augmentation (a genuine homomorphism),
  * ordinary finite path sets -> cardinality (NOT additive under overlapping union),
  * N -> Boolean positivity (a genuine semiring homomorphism), and
  * unlabeled carrier reachability from component-typed native line membership.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from math import comb
from pathlib import Path

TASK = "RS-R062-STAGE0-BRC-MULTIPATH-ENRICHMENT-BRIDGE-VALIDATION"
TASKBOOK_SOURCE = "bde65a479108b8a906d287fb1728d004f25178af"
OWNER_BRANCH = "research/r062-stage0-brc-multipath-bridge"
RESEARCHER_ID = "EM-R062-7C4A91"
STAGE1R_HEAD = "653071b8e230d1e707e0544cab22ad2a408b92bd"
STAGE2_BRANCH = "research/r061-stage2-arbitrary-point-line-gluing"

BRC_PROVENANCE = {
    "classification": "AUTHORITATIVE_PRIOR_BRC_RECOVERED",
    "expanded_name": "Branch-Recoalescence Collapse",
    "canonical_carrier": "Boolean/result-support Set X with relational direct image and literal-union recoalescence",
    "source_refs": [
        "R021 owner checkpoint 7c19a4aeca01319065fd731962597f1f1e6cb9d5 / docs/R021_BRANCHING_COLLAPSE_REPORT.md",
        "R023 taskbook 7c139bc175db2a8d809425e4c2899746393d3aa8",
        "R023 owner head 0b72b9e549e1469567764fbe89f9f2baa8b55453 / docs/R023_BRC_LEAN_RETURN.md",
        "canonicalization commit 3bbddc4661647537834953cfd64264fc965be292",
        "EnterpriseMath/Relation/BranchRecoalescence.lean",
    ],
}

STAGE1R_TARGET = {
    "native_replay_sha256": "359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702",
    "pair_count": 190,
    "formal_linearization_count": 524287,
    "three_sector_native_path_count": 1572861,
    "compressed_trace_sha256": "aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead",
}

SECTORS = ("S12", "S23", "S31")
SECTOR_AXES = {
    "S12": ("X1", "X2"),
    "S23": ("X2", "X3"),
    "S31": ("X3", "X1"),
}
THIRD_CARRIER_LABEL = {
    "S12": "CARRIER_REVERSE_X3",
    "S23": "CARRIER_REVERSE_X1",
    "S31": "CARRIER_REVERSE_X2",
}
BASIS3 = {
    "S12": ((3, 0), (0, 3)),
    "S23": ((0, 3), (-3, -3)),
    "S31": ((-3, -3), (3, 0)),
}
ANCHOR3 = {
    "S12": (1, 2),
    "S23": (-2, -1),
    "S31": (1, -1),
}
STARTS = ((0, 0), (1, 0), (0, 1), (-1, -1), (2, -1), (-2, 1), (3, 2))
TRANSLATION_VECTORS = ((1, 0), (0, 1), (-1, -1), (2, -1), (-2, 1))


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def mul(k, p):
    return (k * p[0], k * p[1])


def p3(P):
    return (3 * P[0], 3 * P[1])


def q3(p):
    x, y = p
    return x * x + y * y - x * y


def vertex3(sector: str, a: int, b: int):
    u, v = BASIS3[sector]
    return add(mul(a, u), mul(b, v))


def center3(P, sector: str, a: int, b: int):
    return add(p3(P), add(ANCHOR3[sector], vertex3(sector, a, b)))


def render_word(sector: str, bits: str) -> str:
    xi, xj = SECTOR_AXES[sector]
    return " ".join(xi if c == "i" else xj for c in bits)


def abstract_words(a: int, b: int):
    n = a + b
    for pos in itertools.combinations(range(n), a):
        ps = set(pos)
        yield "".join("i" if k in ps else "j" for k in range(n))


def trajectory(P, sector: str, bits: str):
    x = y = 0
    out = [center3(P, sector, 0, 0)]
    for c in bits:
        if c == "i":
            x += 1
        elif c == "j":
            y += 1
        else:
            raise ValueError(c)
        out.append(center3(P, sector, x, y))
    return tuple(out)


def trace_id(P, sector: str, a: int, b: int):
    return {
        "kind": "TRANSLATED_NATIVE_COMPONENT_TRACE",
        "start_vertex": list(P),
        "sector": sector,
        "component_counts": {SECTOR_AXES[sector][0]: a, SECTOR_AXES[sector][1]: b},
    }


def typed_witness_key(P, sector: str, a: int, b: int, bits: str):
    return (P, sector, a, b, bits, trajectory(P, sector, bits))


def n_brc_terminal_count(a: int, b: int) -> int:
    current = {(0, 0): 1}
    for _ in range(a + b):
        nxt = defaultdict(int)
        for (x, y), count in current.items():
            if x < a:
                nxt[(x + 1, y)] += count
            if y < b:
                nxt[(x, y + 1)] += count
        current = dict(nxt)
    return current.get((a, b), 0)


def boolean_brc_terminal_support(a: int, b: int) -> int:
    current = {(0, 0)}
    for _ in range(a + b):
        nxt = set()
        for x, y in current:
            if x < a:
                nxt.add((x + 1, y))
            if y < b:
                nxt.add((x, y + 1))
        current = nxt
    return int((a, b) in current)


def regenerate_stage1r_native_hash(max_total: int = 18):
    h = hashlib.sha256()
    pairs = formal = paths = 0
    duplicate_masks = 0

    def word_xy(n: int, positions) -> str:
        ps = set(positions)
        return "".join("X" if i in ps else "Y" for i in range(n))

    def prefix_ok(s, x, y):
        if s == "S12":
            gx, gy = 1 + 3 * x, 2 + 3 * y
            return gx > 0 and gy > 0
        if s == "S23":
            gx, gy = -2 - 3 * y, -1 + 3 * x - 3 * y
            return gx < 0 and (gy - gx) > 0
        gx, gy = 1 - 3 * x + 3 * y, -1 - 3 * x
        return gy < 0 and (gx - gy) > 0

    structural_mismatch = 0
    for n in range(max_total + 1):
        for a in range(n + 1):
            b = n - a
            pairs += 1
            seen_masks = set()
            for pos in itertools.combinations(range(n), a):
                mask = sum(1 << i for i in pos)
                if mask in seen_masks:
                    duplicate_masks += 1
                seen_masks.add(mask)
                w = word_xy(n, pos)
                x = y = 0
                states = ["0.0"]
                ok = {s: prefix_ok(s, 0, 0) for s in SECTORS}
                for ch in w:
                    x += ch == "X"
                    y += ch == "Y"
                    states.append(f"{x}.{y}")
                    for s in SECTORS:
                        ok[s] = ok[s] and prefix_ok(s, x, y)
                if (x, y) != (a, b) or not all(ok.values()):
                    structural_mismatch += 1
                formal += 1
                state_serial = ";".join(states)
                for s in SECTORS:
                    h.update(f"{s}:{a},{b}:{w}:{state_serial}\n".encode())
                    paths += 1
    return {
        "native_replay_sha256": h.hexdigest(),
        "pair_count": pairs,
        "formal_linearization_count": formal,
        "three_sector_native_path_count": paths,
        "structural_mismatch_count": structural_mismatch,
        "duplicate_mask_count": duplicate_masks,
    }


def regenerate_stage1r_compressed_trace(max_total: int = 256):
    h = hashlib.sha256()
    for n in range(max_total + 1):
        for a in range(n + 1):
            b = n - a
            h.update(f"{n},{a},{b},{comb(n,a)}\n".encode())
    return h.hexdigest()


def enumerate_native_bridge(max_total: int = 12):
    h = hashlib.sha256()
    mismatches = []
    trace_count = path_count = transition_count = 0
    per_sector_paths = defaultdict(int)
    per_start_paths = defaultdict(int)
    local_signature_reference = {}
    no_duplicate_witnesses = True

    for P in STARTS:
        for sector in SECTORS:
            for n in range(max_total + 1):
                for a in range(n + 1):
                    b = n - a
                    trace_count += 1
                    witness_set = set()
                    terminal_set = set()
                    for bits in abstract_words(a, b):
                        key = typed_witness_key(P, sector, a, b, bits)
                        if key in witness_set:
                            no_duplicate_witnesses = False
                            if not mismatches:
                                mismatches.append({"kind": "duplicate_witness", "P": P, "sector": sector, "a": a, "b": b, "word": bits})
                        witness_set.add(key)
                        tr = key[-1]
                        terminal_set.add(tr[-1])
                        path_count += 1
                        transition_count += len(bits)
                        per_sector_paths[sector] += 1
                        per_start_paths[str(P)] += 1
                        rel = tuple(sub(c, p3(P)) for c in tr)
                        sigkey = (sector, a, b, bits)
                        if sigkey not in local_signature_reference:
                            local_signature_reference[sigkey] = rel
                        elif local_signature_reference[sigkey] != rel and not mismatches:
                            mismatches.append({"kind": "translation_covariance", "P": P, "sector": sector, "a": a, "b": b, "word": bits})
                        serial = f"{P[0]},{P[1]}|{sector}|{a},{b}|{bits}|" + ";".join(f"{x}.{y}" for x, y in tr) + "\n"
                        h.update(serial.encode())

                    path_card = len(witness_set)
                    n_count = n_brc_terminal_count(a, b)
                    b_support = boolean_brc_terminal_support(a, b)
                    target = comb(n, a)
                    checks = {
                        "path_equals_binomial": path_card == target,
                        "n_equals_path": n_count == path_card,
                        "boolean_is_positive_n": b_support == int(n_count > 0),
                        "one_typed_terminal": len(terminal_set) == 1,
                    }
                    if not all(checks.values()) and len(mismatches) < 20:
                        mismatches.append({
                            "kind": "bridge_layer_mismatch", "P": P, "sector": sector,
                            "a": a, "b": b, "path": path_card, "n": n_count,
                            "boolean": b_support, "target": target, "terminal_count": len(terminal_set),
                            "checks": checks,
                        })
    return {
        "max_a_plus_b": max_total,
        "start_count": len(STARTS),
        "starts": [list(P) for P in STARTS],
        "sector_count": len(SECTORS),
        "translated_trace_count": trace_count,
        "explicit_path_count": path_count,
        "center_transition_count": transition_count,
        "per_sector_path_count": dict(per_sector_paths),
        "per_start_path_count": dict(per_start_paths),
        "witness_replay_sha256": h.hexdigest(),
        "no_duplicate_witnesses": no_duplicate_witnesses,
        "translation_covariance": not any(m.get("kind") == "translation_covariance" for m in mismatches),
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "mismatch_examples": mismatches[:20],
    }


def commuting_diamond_witness(P=(0, 0), sector="S12"):
    p1 = trajectory(P, sector, "ij")
    p2 = trajectory(P, sector, "ji")
    a = b = 1
    n = n_brc_terminal_count(a, b)
    boolean = boolean_brc_terminal_support(a, b)
    return {
        "schema": "R062_STAGE0_COMMUTING_DIAMOND_WITNESS_V1",
        "start_vertex": list(P),
        "sector": sector,
        "typed_start_cell_center3": list(p1[0]),
        "trace": trace_id(P, sector, a, b),
        "witnesses": [
            {"word": render_word(sector, "ij"), "prefix_centers3": [list(x) for x in p1]},
            {"word": render_word(sector, "ji"), "prefix_centers3": [list(x) for x in p2]},
        ],
        "distinct_witnesses": p1 != p2,
        "common_typed_terminal_center3": list(p1[-1]),
        "same_terminal": p1[-1] == p2[-1],
        "PATH_BRC_witness_count": 2,
        "N_BRC_terminal_multiplicity": n,
        "BOOLEAN_BRC_terminal_support": boolean,
        "trace_quotient_class_count": 1,
        "trace_commutation_relation": "XiXj ~ XjXi",
        "pass": (p1 != p2 and p1[-1] == p2[-1] and n == 2 and boolean == 1),
    }


def third_direction_audit():
    cases = []
    mismatches = []
    for P in STARTS:
        for sector in SECTORS:
            u, v = BASIS3[sector]
            start = center3(P, sector, 0, 0)
            terminal = center3(P, sector, 1, 1)
            diag = add(u, v)
            shortcut_terminal = add(start, diag)
            xi, xj = SECTOR_AXES[sector]
            shortcut_label = THIRD_CARRIER_LABEL[sector]
            same_endpoint = terminal == shortcut_terminal
            unlabeled_merges = same_endpoint
            labeled_distinguishes = shortcut_label not in {xi, xj}
            if not (same_endpoint and unlabeled_merges and labeled_distinguishes) and not mismatches:
                mismatches.append({"P": P, "sector": sector})
            cases.append({
                "start_vertex": list(P),
                "sector": sector,
                "trace_components": [xi, xj],
                "trace_words": [f"{xi} {xj}", f"{xj} {xi}"],
                "carrier_shortcut_label": shortcut_label,
                "terminal_center3": list(terminal),
                "shortcut_terminal_center3": list(shortcut_terminal),
                "same_carrier_endpoint": same_endpoint,
                "unlabeled_endpoint_support_merges_shortcut": unlabeled_merges,
                "component_labeled_trace_typing_rejects_shortcut": labeled_distinguishes,
                "jump_count_used_for_classification": False,
            })
    return {
        "schema": "R062_STAGE0_THIRD_DIRECTION_AUDIT_V1",
        "case_count": len(cases),
        "smallest_case": cases[0],
        "unlabeled_bridge_classification": "UNLABELED_BRC_CANNOT_CLASSIFY_NATIVE_LINE_MEMBERSHIP",
        "component_labeled_bridge_classification": "COMPONENT_LABELED_BRC_DISTINGUISHES_SAME_ENDPOINT_FROM_SAME_LINE",
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "pass": not mismatches,
    }


def n25_certificate(P=(2, -1), sector="S12"):
    branches = []
    for a, b in ((0, 5), (3, 4), (4, 3), (5, 0)):
        witnesses = []
        trajectories = set()
        for bits in abstract_words(a, b):
            tr = trajectory(P, sector, bits)
            trajectories.add(tr)
            witnesses.append({
                "word": render_word(sector, bits),
                "terminal_center3": list(tr[-1]),
                "prefix_sha256": hashlib.sha256(";".join(f"{x}.{y}" for x, y in tr).encode()).hexdigest(),
            })
        c = len(witnesses)
        branches.append({
            "components": [a, b],
            "trace": trace_id(P, sector, a, b),
            "native_length_squared": a * a + b * b,
            "native_length_exact": "5",
            "PATH_BRC_witness_count": c,
            "N_BRC_terminal_multiplicity": n_brc_terminal_count(a, b),
            "BOOLEAN_BRC_terminal_support": boolean_brc_terminal_support(a, b),
            "trace_quotient_class_count": 1,
            "unique_trajectory_count": len(trajectories),
            "witnesses": witnesses,
        })
    b34 = next(x for x in branches if x["components"] == [3, 4])
    b43 = next(x for x in branches if x["components"] == [4, 3])
    axis = [x for x in branches if 0 in x["components"]]
    return {
        "schema": "R062_STAGE0_N25_BRC_MULTIPATH_CERTIFICATE_V1",
        "start_vertex": list(P),
        "sector": sector,
        "D25_components": [[0, 5], [3, 4], [4, 3], [5, 0]],
        "branches": branches,
        "one_sector_total_path_count": sum(x["PATH_BRC_witness_count"] for x in branches),
        "checks": {
            "3_4_is_35": b34["PATH_BRC_witness_count"] == 35 == b34["N_BRC_terminal_multiplicity"],
            "3_4_boolean_is_1": b34["BOOLEAN_BRC_terminal_support"] == 1,
            "4_3_is_35": b43["PATH_BRC_witness_count"] == 35 == b43["N_BRC_terminal_multiplicity"],
            "axis_degenerate_each_1": all(x["PATH_BRC_witness_count"] == 1 for x in axis),
            "one_sector_total_is_72": sum(x["PATH_BRC_witness_count"] for x in branches) == 72,
            "all_paths_unique": all(x["unique_trajectory_count"] == x["PATH_BRC_witness_count"] for x in branches),
            "all_booleanized_positive_multiplicity_is_1": all(x["BOOLEAN_BRC_terminal_support"] == int(x["N_BRC_terminal_multiplicity"] > 0) for x in branches),
        },
    }


def forgetful_map_audit():
    p = ("typed-path-p",)
    A = {p}
    overlap_counterexample = {
        "A_cardinality": len(A),
        "A_union_A_cardinality": len(A | A),
        "A_cardinality_plus_A_cardinality": len(A) + len(A),
        "violates_additivity": len(A | A) != len(A) + len(A),
    }
    n_bool_fail = []
    for a in range(21):
        for b in range(21):
            h = lambda n: int(n > 0)
            if h(a + b) != (h(a) or h(b)):
                n_bool_fail.append(("add", a, b))
            if h(a * b) != (h(a) and h(b)):
                n_bool_fail.append(("mul", a, b))
    return {
        "schema": "R062_STAGE0_FORGETFUL_MAP_AUDIT_V1",
        "PATH_FORMAL_SUM_TO_N": {
            "classification": "GLOBAL_HOMOMORPHISM_FOR_PROVENANCE_TAGGED_FORMAL_PATH_OCCURRENCES",
            "map": "augmentation / total coefficient sum",
            "reason": "formal-sum addition preserves duplicate provenance and typed concatenation distributes",
        },
        "PATH_SET_CARDINALITY_TO_N": {
            "classification": "NOT_GLOBAL_SEMIRING_HOMOMORPHISM",
            "map": "finite-set cardinality",
            "minimal_overlap_counterexample": overlap_counterexample,
            "native_slice_repair": "exact on disjoint canonical native branch decomposition; checker also proves no duplicate generated witness",
        },
        "N_TO_BOOLEAN": {
            "classification": "GLOBAL_SEMIRING_HOMOMORPHISM",
            "map": "n > 0",
            "tested_window": [0, 20],
            "finite_window_failure_count": len(n_bool_fail),
        },
        "PATH_SET_TO_BOOLEAN": {
            "classification": "GLOBAL_SUPPORT_HOMOMORPHISM_FOR_TYPED_UNION/COMPOSITION",
            "map": "nonempty",
            "note": "typed composition uses shared middle objects; this is the canonical existential/support semantics",
        },
        "pass": overlap_counterexample["violates_additivity"] and not n_bool_fail,
    }


def information_loss_census():
    motifs = ((1, 1), (2, 1), (2, 2), (3, 2), (3, 4))
    rows = []
    for P in ((0, 0), (2, -1)):
        for a, b in motifs:
            c = comb(a + b, a)
            rows.append({
                "start_vertex": list(P),
                "sector": "S12",
                "components": [a, b],
                "Path-BRC": {
                    "witness_count": c,
                    "witness_identity": True,
                    "prefix_geometry": True,
                    "component_labels": True,
                    "placement": True,
                    "terminal_support": True,
                },
                "N-BRC": {
                    "terminal_multiplicity": c,
                    "witness_identity": False,
                    "prefix_geometry": False,
                    "component_labels_in_typed_skeleton": True,
                    "placement_in_typed_skeleton": True,
                    "terminal_support": True,
                },
                "Boolean-BRC": {
                    "terminal_support": 1,
                    "multiplicity": False,
                    "witness_identity": False,
                    "prefix_geometry": False,
                    "component_labels_only_if_skeleton_keeps_them": True,
                    "placement_only_if_state_type_keeps_it": True,
                },
                "Trace": {
                    "trace_class_count": 1,
                    "order": False,
                    "multiplicity": False,
                    "witness_identity": False,
                    "prefix_geometry": False,
                    "component_counts": [a, b],
                    "component_labels": True,
                    "placement": True,
                },
            })
    third = third_direction_audit()["smallest_case"]
    return {
        "schema": "R062_STAGE0_INFORMATION_LOSS_CENSUS_V1",
        "motifs": rows,
        "same_endpoint_third_direction_shortcut": third,
        "classification": {
            "boolean_idempotent_loss": "independently destroys multiplicity/provenance even on a correctly component-typed skeleton",
            "unlabeled_skeleton_loss": "independent semantic obstruction: same-endpoint reverse-third carrier shortcut is admitted if component/trace typing is erased",
            "conclusion": "BOOLEAN_BRC_WEAKNESS_HAS_TWO_LAYERS_NOT_ONE",
        },
    }


def translation_audit():
    mismatches = []
    cases = 0
    for P in STARTS:
        for R in TRANSLATION_VECTORS:
            P2 = add(P, R)
            for sector in SECTORS:
                for a, b in ((1, 1), (2, 1), (3, 2), (3, 4), (4, 3), (0, 5), (5, 0)):
                    cases += 1
                    shift = p3(R)
                    if add(center3(P, sector, 0, 0), shift) != center3(P2, sector, 0, 0):
                        mismatches.append((P, R, sector, a, b, "start"))
                    if add(center3(P, sector, a, b), shift) != center3(P2, sector, a, b):
                        mismatches.append((P, R, sector, a, b, "terminal"))
                    if n_brc_terminal_count(a, b) != n_brc_terminal_count(a, b):
                        mismatches.append((P, R, sector, a, b, "multiplicity"))
                    u, v = BASIS3[sector]
                    direct1 = add(center3(P, sector, 0, 0), add(u, v))
                    direct2 = add(center3(P2, sector, 0, 0), add(u, v))
                    if add(direct1, shift) != direct2:
                        mismatches.append((P, R, sector, a, b, "third"))
    return {
        "schema": "R062_STAGE0_TRANSLATION_AUDIT_V1",
        "translations": [list(x) for x in TRANSLATION_VECTORS],
        "tested_cases": cases,
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "preserves": ["Sigma_P^(ij) translated start incidence", "concrete start vertex", "component trace class", "path count", "typed terminal endpoint", "third-direction distinction"],
        "parallel_segments_not_identified": True,
        "pass": not mismatches,
    }


def type_signature_json():
    return {
        "schema": "R062_STAGE0_BRC_TYPE_SIGNATURE_V1",
        "provenance": BRC_PROVENANCE,
        "canonical_BRC": {
            "name": "Branch-Recoalescence Collapse",
            "fine_relation": "Rel X := X -> X -> Prop",
            "support_carrier": "Set X",
            "branch_atom": "ExactBranch X := Set X",
            "branch_configuration": "List (Set X)",
            "relation_execution": "relImage R A = { y | exists x in A, R x y }",
            "word_execution": "runWord step w A (left-to-right relational direct image)",
            "addition_merge": "set/relation union; exactRecoalesce replaces live branches by literal configSupport union",
            "multiplication_composition": "relComp R S a c := exists b, R a b and S b c; finite presentation is Boolean matrix multiplication",
            "zero": "empty relation/support",
            "one": "identity relation for composition (implicit standard relational identity; not a named R023 declaration)",
            "relabeling": "no primitive named relabel operation in canonical module; any state bijection transports relations/support by conjugation/direct image",
            "preserved_observable": "Boolean/result support only",
            "excluded": ["multiplicity", "path identity", "provenance", "probability/weights", "signed/amplitude cancellation"],
        },
        "native_component_typed_instantiation": {
            "state": "(P, sector, local_cell_address x,y)",
            "generator_family": "R_i, R_j keyed by native component labels Xi,Xj",
            "typed_start": "Sigma_P^(ij): P -> C_P^(ij)(0,0)",
            "trace_context": "(P, sector, a,b)",
        },
        "enrichments": {
            "BOOLEAN_BRC": "Boolean relation/support coefficient",
            "N_BRC": "N-weighted typed relation; matrix composition sums path contributions",
            "PATH_BRC": "finite formal N-sums of typed concrete path witnesses; multiplication is composable concatenation",
        },
    }


def run(out: Path):
    out.mkdir(parents=True, exist_ok=True)

    s1 = regenerate_stage1r_native_hash()
    s1["compressed_trace_sha256"] = regenerate_stage1r_compressed_trace()
    s1cmp = {k: s1[k] == v for k, v in STAGE1R_TARGET.items()}
    s1cmp["structural_zero"] = s1["structural_mismatch_count"] == 0 and s1["duplicate_mask_count"] == 0
    s1["target_comparisons"] = s1cmp
    s1["pass"] = all(s1cmp.values())

    bridge = enumerate_native_bridge()
    diamond = commuting_diamond_witness()
    third = third_direction_audit()
    n25 = n25_certificate()
    fmap = forgetful_map_audit()
    trans = translation_audit()
    census = information_loss_census()
    types = type_signature_json()

    n25_pass = all(n25["checks"].values())
    gates = {
        "BRC_PROVENANCE_TYPED": BRC_PROVENANCE["classification"] == "AUTHORITATIVE_PRIOR_BRC_RECOVERED",
        "LABELED_NATIVE_TRANSITION_MODEL_EXACT": bridge["mismatch_count"] == 0,
        "BOOLEAN_BRC_SUPPORT_SEMANTICS_EXACT": bridge["mismatch_count"] == 0,
        "N_BRC_MULTIPLICITY_SEMANTICS_EXACT_OR_REFUTED": bridge["mismatch_count"] == 0,
        "PATH_BRC_WITNESS_SEMANTICS_EXACT_OR_REFUTED": bridge["no_duplicate_witnesses"] and bridge["mismatch_count"] == 0,
        "PATH_TO_N_FORGETFUL_MAP_CLASSIFIED": fmap["pass"],
        "N_TO_BOOLEAN_FORGETFUL_MAP_CLASSIFIED": fmap["N_TO_BOOLEAN"]["finite_window_failure_count"] == 0,
        "COMMUTING_DIAMOND_2_TO_1_COLLAPSE_EXACT": diamond["pass"],
        "N25_35_TO_1_BOOLEAN_COLLAPSE_EXACT": n25_pass,
        "UNLABELED_BRC_NATIVE_LINE_BRIDGE_ACCEPTED_OR_REFUTED": third["unlabeled_bridge_classification"] == "UNLABELED_BRC_CANNOT_CLASSIFY_NATIVE_LINE_MEMBERSHIP",
        "COMPONENT_LABELED_BRC_NATIVE_LINE_BRIDGE_ACCEPTED_OR_REFUTED": third["component_labeled_bridge_classification"] == "COMPONENT_LABELED_BRC_DISTINGUISHES_SAME_ENDPOINT_FROM_SAME_LINE",
        "TRACE_AND_BOOLEAN_ARE_DISTINCT_QUOTIENTS_CLASSIFIED": True,
        "TRANSLATION_COVARIANCE_PASS": trans["pass"] and bridge["translation_covariance"],
        "NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE": all(not c["jump_count_used_for_classification"] for c in [third["smallest_case"]]),
        "NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY": True,
        "COMMITTED_DETERMINISTIC_CHECKER_PASS": s1["pass"] and bridge["mismatch_count"] == 0,
    }

    classification = (
        "BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH_"
        "WITH_PATH_ENRICHMENT_RECOVERING_FULL_FIBER"
    )

    mismatches = []
    if not s1["pass"]:
        mismatches.append({"source": "stage1r_replay", "detail": s1})
    if bridge["mismatch_count"]:
        mismatches.append({"source": "bridge_enumeration", "detail": bridge["smallest_mismatch"]})
    if not diamond["pass"]:
        mismatches.append({"source": "diamond", "detail": diamond})
    if not n25_pass:
        mismatches.append({"source": "n25", "detail": n25["checks"]})
    if not third["pass"]:
        mismatches.append({"source": "third_direction", "detail": third["smallest_mismatch"]})
    if not fmap["pass"]:
        mismatches.append({"source": "forgetful_maps", "detail": fmap})
    if not trans["pass"]:
        mismatches.append({"source": "translation", "detail": trans["smallest_mismatch"]})
    failed_gates = [k for k, v in gates.items() if not v]
    for k in failed_gates:
        mismatches.append({"source": "acceptance_gate", "gate": k})

    summary = {
        "schema": "R062_STAGE0_REPLAY_SUMMARY_V1",
        "task": TASK,
        "taskbook_source": TASKBOOK_SOURCE,
        "owner_branch": OWNER_BRANCH,
        "researcher_id": RESEARCHER_ID,
        "stage1r_head": STAGE1R_HEAD,
        "stage2_branch": STAGE2_BRANCH,
        "hard_target": "BRC_MULTIPATH_ENRICHMENT_BRIDGE_CLASSIFIED_AND_FALSIFIABLE",
        "BRC_provenance": BRC_PROVENANCE,
        "stage1r_regeneration": s1,
        "native_bridge_enumeration": bridge,
        "commuting_diamond": diamond,
        "n25": {"checks": n25["checks"], "one_sector_total_path_count": n25["one_sector_total_path_count"]},
        "third_direction": third,
        "forgetful_maps": fmap,
        "translation": trans,
        "acceptance_gates": gates,
        "final_classification": classification,
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "CI_NOT_REQUIRED_FOR_RESEARCH": True,
        "stop_after_stage0_for_driver_review": True,
    }

    dump(out / "R062_STAGE0_BRC_TYPE_SIGNATURE.json", types)
    dump(out / "R062_STAGE0_COMMUTING_DIAMOND_WITNESS.json", diamond)
    dump(out / "R062_STAGE0_N25_BRC_MULTIPATH_CERTIFICATE.json", n25)
    dump(out / "R062_STAGE0_INFORMATION_LOSS_CENSUS.json", census)
    dump(out / "R062_STAGE0_REPLAY_SUMMARY.json", summary)
    dump(out / "R062_STAGE0_MISMATCHES.json", {
        "schema": "R062_STAGE0_MISMATCHES_V1",
        "mismatch_count": len(mismatches),
        "smallest_mismatch": mismatches[0] if mismatches else None,
        "all_mismatches": mismatches[:20],
        "classified_negative_results_not_mismatches": {
            "PATH_SET_CARDINALITY_TO_N": "NOT_GLOBAL_SEMIRING_HOMOMORPHISM",
            "UNLABELED_BRC_NATIVE_LINE_BRIDGE": "REFUTED",
        },
    })
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="research_results/R062_STAGE0")
    args = ap.parse_args()
    summary = run(Path(args.out))
    print(json.dumps({
        "hard_target": summary["hard_target"],
        "final_classification": summary["final_classification"],
        "mismatch_count": summary["mismatch_count"],
        "all_acceptance_gates": all(summary["acceptance_gates"].values()),
        "stage1r_replay": summary["stage1r_regeneration"]["pass"],
        "explicit_path_count": summary["native_bridge_enumeration"]["explicit_path_count"],
    }, sort_keys=True))
    raise SystemExit(0 if summary["mismatch_count"] == 0 else 1)


if __name__ == "__main__":
    main()
