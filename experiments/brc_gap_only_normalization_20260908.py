"""Exact representation audit of 60 previously saved mathematical states.

The only public inputs are two pinned local certificates. This checker does
not generate a multiplier position, run a factor-search API or accept a target
integer. Square tests below audit the already recorded arithmetic identities.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha1, sha256
from math import isqrt
from pathlib import Path
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    source_path = args.enterprise_root / "src" / "enterprise_math" / "brc_multiplier_priority_jump.py"
    source_digest = sha256(source_path.read_bytes()).hexdigest()
    assert source_digest == "ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d"
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_multiplier_priority_jump import odd_n_ceiling_state_scan_representative

    parent_dir = Path(__file__).resolve().parent
    input_specs = [
        ("brc_public_rsa_fixed_predicates_20260908.json", "e56cfc8457e2398b5de3c90182c2b37824580ef3"),
        ("brc_public_frozen_prefix_20260908.json", "c4b201e608167cfff96c5a141bd9e26b575dad69"),
    ]
    documents = []
    for name, expected in input_specs:
        raw = (parent_dir / name).read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
        actual = sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
        assert actual == expected
        documents.append(json.loads(raw))
    inputs, prefix = documents
    labels = ["RSA-270", "RSA-896", "RSA-2048"]
    assert [r["label"] for r in inputs["records"]] == labels
    assert [r["label"] for r in prefix["records"]] == labels
    assert prefix["input_certificate_blob"] == input_specs[0][1]

    # Reuse the saved m=8 positive identities. New controls are small inputs
    # prescribed by N=t^2-1, even t, rather than selected by a search.
    control_inputs = []
    for item in prefix["positive_family"]["controls"]:
        a, b = item["witness"]
        control_inputs.append({"kind": "reused_m8_positive", "N": item["N"],
            "multiplier": 8, "a": a, "gap": b*b, "square_root": b,
            "expected_representative": 8, "expected_scale": 1})
    for t in range(4, 35, 2):
        control_inputs.append({"kind": "constructed_fold_positive", "N": t*t-1,
            "multiplier": 16, "a": 4*t, "gap": 16, "square_root": 4,
            "expected_representative": 1, "expected_scale": 4})
    control_inputs.append({"kind": "zero_gap_boundary", "N": 9,
        "multiplier": 16, "a": 12, "gap": 0, "square_root": 0,
        "expected_representative": 1, "expected_scale": 4})

    records = []
    verified_controls = []
    # A single finite worklist; there is no callable public-target solver.
    worklist = []
    for parent, item in zip(inputs["records"], prefix["records"], strict=True):
        n = int(parent["N"])
        assert n % 2 == 1
        assert sha256(parent["N"].encode("ascii")).hexdigest() == parent["decimal_sha256"]
        assert len(item["evaluations"]) == 20
        for e in item["evaluations"]:
            worklist.append((parent["label"], n, e, None))
    for control in control_inputs:
        e = {"multiplier": control["multiplier"], "gap": str(control["gap"])}
        worklist.append((None, control["N"], e, control))

    qrs4096 = {r*r % 4096 for r in range(4096)}
    for label, n, entry, control in worklist:
        m, gap = entry["multiplier"], int(entry["gap"])
        assert m > 0 and gap >= 0 and n % 2 == 1

        # Verification side only: restore a from the saved identity. This
        # restoration is explicitly not a free step in an N-only pipeline.
        a = isqrt(m*n + gap)
        assert a*a == m*n + gap and (a-1)**2 < m*n <= a*a

        # Representation side: after the valid-state contract above, this
        # block reads only m and gap. N and a do not select a reduction.
        representative, reduced_gap, scale, steps = m, gap, 1, 0
        while representative % 4 == 0 and reduced_gap % 4 == 0:
            representative //= 4
            reduced_gap //= 4
            scale *= 2
            steps += 1
        impossible = representative % 4 == 2 or representative % 8 == 4
        source_representative = odd_n_ceiling_state_scan_representative(m, a)
        assert source_representative == (None if impossible else representative)
        assert m == scale*scale*representative and gap == scale*scale*reduced_gap
        assert a % scale == 0
        reduced_a = a // scale
        assert reduced_a*reduced_a-reduced_gap == representative*n
        assert (reduced_a-1)**2 < representative*n <= reduced_a*reduced_a

        old_root, new_root = isqrt(gap), isqrt(reduced_gap)
        old_square, new_square = old_root*old_root == gap, new_root*new_root == reduced_gap
        assert old_square == new_square
        if old_square:
            assert old_root == scale*new_root
        if impossible:
            assert not old_square and reduced_gap % 8 not in (0, 1, 4)

        if control is not None:
            assert old_square and not impossible
            assert a == control["a"] and old_root == control["square_root"]
            assert representative == control["expected_representative"]
            assert scale == control["expected_scale"]
            verified_controls.append({**control, "reduced_gap": str(reduced_gap),
                "reduced_ceiling": reduced_a, "reduced_square_root": new_root,
                "source_equivalence": True, "square_identity_preserved": True})
            continue

        assert entry["status"] in ("REUSED_PINNED_NO_WITNESS", "NO_WITNESS_AT_THIS_POSITION")
        assert not old_square
        row = {"label": label, "prefix_slot": entry["prefix_slot"], "multiplier": m,
            "original_multiplied_direction": entry["multiplied_direction"],
            "gap": str(gap), "reduced_multiplier": representative,
            "reduced_gap": str(reduced_gap), "root_scale": scale, "reduction_steps": steps,
            "source_representative": source_representative,
            "source_equivalence": True, "exact_square_status_preserved": True,
            "already_rejected_by_original_mod4096": gap % 4096 not in qrs4096}
        if impossible:
            row["classification"] = "MODULARLY_IMPOSSIBLE"
            row["reason"] = "reduced multiplier is 2 mod 4" if representative % 4 == 2 else "reduced multiplier is 4 mod 8 with odd ceiling"
        elif representative == m:
            row["classification"] = "UNCHANGED"
        else:
            item = next(r for r in prefix["records"] if r["label"] == label)
            aliases = [e for e in item["evaluations"] if e["multiplier"] == representative]
            if aliases:
                alias = aliases[0]
                assert int(alias["gap"]) == reduced_gap
                row["alias_prefix_slot"] = alias["prefix_slot"]
                row["classification"] = "EARLIER_ALIAS" if alias["prefix_slot"] < entry["prefix_slot"] else "LATER_ALIAS"
            else:
                row["classification"] = "REPRESENTATIVE_OUTSIDE_SAVED_PREFIX"
        records.append(row)

    summaries = []
    for label in labels:
        group = [r for r in records if r["label"] == label]
        counts = Counter(r["classification"] for r in group)
        live = [r for r in group if r["classification"] != "MODULARLY_IMPOSSIBLE"]
        keys = {(r["reduced_multiplier"], r["reduced_gap"]) for r in live}
        assert len({r["reduced_gap"] for r in live}) == len(keys)
        direction_counts = []
        for direction in ("D", "U", "Z"):
            subset = [r for r in group if r["original_multiplied_direction"] == direction]
            direction_counts.append({"direction": direction, "saved_positions": len(subset),
                "classification_counts": dict(Counter(r["classification"] for r in subset))})
        summaries.append({"label": label, "saved_positions": len(group),
            "classification_counts": dict(counts), "remaining_distinct_predicate_inputs": len(keys),
            "eliminated_modular_positions": counts["MODULARLY_IMPOSSIBLE"],
            "duplicate_live_records": len(live)-len(keys),
            "modular_exits_already_rejected_by_mod4096": sum(r["already_rejected_by_original_mod4096"]
                for r in group if r["classification"] == "MODULARLY_IMPOSSIBLE"),
            "direction_counts": direction_counts})
    assert len(records) == 60 and len(verified_controls) == 32
    assert sum(r["remaining_distinct_predicate_inputs"] for r in summaries) == 50
    assert sum(r["eliminated_modular_positions"] for r in summaries) == 7
    assert sum(r["duplicate_live_records"] for r in summaries) == 3
    assert sum(r["modular_exits_already_rejected_by_mod4096"] for r in summaries) == 7

    result = {"status": "COMPLETED_FIXED_ARCHIVE_REPRESENTATION_AUDIT",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "dd32c654bc48def291fcb1383c87ecdaa342493c",
        "project_parent": "2e45c3dace447e8af4be28675a4d2589b45c2744",
        "input_certificates": dict(input_specs), "source_sha256": {source_path.name: source_digest},
        "python": sys.version, "platform": platform.platform(),
        "reuse_resolution": "COMPOSE_APPLIED: source root-based representative is the exact reference; the observed scope difference is the supplied carrier (m,A). No production helper is changed.",
        "observer_contract": {"input": "m,A with a previously validated odd-N immediate-ceiling-state contract",
            "preparation_cost": "N-to-A acquisition is required upstream and is not free",
            "coordinate": "A is the upward completion gap, distinct from the downward remainder R",
            "normalization_reads": ["m", "A"], "audit_only": "N and restored ceiling a",
            "metadata_only": "original multiplied-state D/U/Z label; not assumed invariant under reduction"},
        "budget": {"consumed_public_positions": 60, "new_public_positions": 0,
            "new_public_witness_api_calls": 0, "new_public_factors": 0,
            "source_reference_comparisons": 92, "known_positive_controls_consumed": 15,
            "new_constructed_positive_controls": 16, "zero_gap_boundary_controls": 1},
        "accounting": {"before": 60, "remaining_distinct_square_predicate_inputs": 50,
            "modular_exits": 7, "duplicate_live_records": 3,
            "fewer_predicate_inputs_fraction": "1/6",
            "qualification": "Count after states are already supplied; not a measured time or N-to-gap/root-preparation reduction.",
            "existing_filter_overlap": "All 7 modular exits already fail the existing mod4096 necessary condition; do not add both as independent savings.",
            "alias_qualification": "Two references point to later saved slots. A completed batch can deduplicate them; one-pass reuse cannot treat a future recorded outcome as already known.",
            "unmeasured": "Net speed after normalization, cache overhead and preparation; no factorization speedup is claimed."},
        "summaries": summaries, "positive_controls": verified_controls, "records": records,
        "goal_status": "ACTIVE; this is a residual-carrier equivalence result, not a public factorization"}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir / "brc_gap_only_normalization_20260908.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "public_states": len(records),
        "positive_controls": len(verified_controls), "summaries": summaries}, ensure_ascii=False))


if __name__ == "__main__":
    main()
