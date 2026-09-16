"""Fixed finite-prefix observations on three pinned public math puzzles.

The historical prefix is frozen before execution. No other inputs, added
multipliers, ceiling advances, automatic strategy changes or search fallbacks
are accepted. Previously checked m=1 observations are consumed from a pinned
certificate. Timings describe one pass, not a repeated performance benchmark.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha1, sha256
from math import gcd, isqrt
from pathlib import Path
from time import perf_counter_ns
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_opportunistic_shortcuts import LEARNED_COVER_PREFIX
    from enterprise_math.brc_multiplier_priority_jump import odd_n_multiplier_is_scan_irredundant
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness

    expected_sources = {
        "brc_opportunistic_shortcuts.py": "7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7",
        "brc_multiplier_priority_jump.py": "ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d",
        "brc_square_gap_prefilter.py": "f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716",
    }
    for name, expected in expected_sources.items():
        assert sha256((args.enterprise_root / "src" / "enterprise_math" / name).read_bytes()).hexdigest() == expected
    prefix = tuple(LEARNED_COVER_PREFIX)
    assert prefix == (1,48,96,8,15,80,21,16,56,45,35,3,72,7,99,88,40,55,9,24)
    assert len(prefix) == len(set(prefix)) == 20
    assert all(odd_n_multiplier_is_scan_irredundant(m) for m in prefix)
    assert prefix.index(8)+1 == 4

    input_path = Path(__file__).resolve().parent / "brc_public_rsa_fixed_predicates_20260908.json"
    raw = input_path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    input_blob = sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest()
    assert input_blob == "e56cfc8457e2398b5de3c90182c2b37824580ef3"
    parent = json.loads(raw)
    assert [r["label"] for r in parent["records"]] == ["RSA-270", "RSA-896", "RSA-2048"]

    def prime_seed(value):
        # Applies only to the prescribed small constructive factors below.
        return value >= 2 and all(value%d for d in range(2, isqrt(value)+1))

    # A positive integer family for an already frozen prefix member:
    # N=t(2t+1), 8N=(4t+1)^2-1. It does not search for t on an unknown input.
    positive_controls = []
    for t in range(3, 32, 2):
        n = t*(2*t+1)
        x, b = ceiling_completion_square_witness(n, 8)
        assert (x, b) == (4*t+1, 1)
        assert x*x-b*b == 8*n and gcd(n, x-b) == t
        assert 1 < t < 2*t+1 and t*(2*t+1) == n
        j = isqrt(n)
        r = n-j*j
        positive_controls.append({"t": t, "N": n, "pair": [t, 2*t+1],
            "known_prime_pair": prime_seed(t) and prime_seed(2*t+1),
            "base_direction": "D" if r <= j else "U",
            "multiplier": 8, "witness": [x,b], "guaranteed_prefix_slot_at_most": 4})

    records = []
    for item in parent["records"]:
        n = int(item["N"])
        assert sha256(item["N"].encode("ascii")).hexdigest() == item["decimal_sha256"]
        assert item["direct_completion"]["status"] == "NO_WITNESS_THIS_OBSERVATION"
        parent_state = item["state_annotation"]
        parent_j, parent_r = int(parent_state["J"]), int(parent_state["R"])
        assert parent_j*parent_j+parent_r == n and 0 < parent_r <= 2*parent_j
        evaluations = [{"prefix_slot": 1, "multiplier": 1,
            "status": "REUSED_PINNED_NO_WITNESS", "new_api_call": False, "api_ns": None,
            "multiplied_direction": parent_state["direction"],
            "gap": parent_state["next_square_gap"], "independent_audit": "verified in pinned parent"}]
        started_batch = perf_counter_ns()
        for slot, multiplier in enumerate(prefix[1:], 2):
            started = perf_counter_ns()
            witness = ceiling_completion_square_witness(n, multiplier)
            api_ns = perf_counter_ns() - started

            # Exact independent audit of the same prescribed position.
            # This does not advance the position or select another multiplier.
            target = multiplier*n
            j = isqrt(target)
            r = target-j*j
            a = j if r == 0 else j+1
            gap = a*a-target
            gap_root = isqrt(gap)
            expected = (a, gap_root) if gap_root*gap_root == gap else None
            assert witness == expected
            mode = "Z" if r == 0 else "D" if r <= j else "U"
            evaluation = {"prefix_slot": slot, "multiplier": multiplier,
                "status": "NO_WITNESS_AT_THIS_POSITION" if witness is None else "EXACT_SQUARE_WITNESS",
                "new_api_call": True, "api_ns": api_ns,
                "multiplied_direction": mode, "gap": str(gap),
                "independent_audit": "exact native root/gap equality verified"}
            if witness is not None:
                # Return the mathematical identity certificate only. There is
                # no general factor-search or key-recovery workflow here.
                x, b = witness
                assert x*x-b*b == target
                evaluation["witness"] = [str(x), str(b)]
            evaluations.append(evaluation)
        batch_ns = perf_counter_ns() - started_batch
        assert len(evaluations) == 20
        calls = [row for row in evaluations if row["new_api_call"]]
        records.append({"label": item["label"], "source_pdf": item["source_pdf"],
            "decimal_sha256": item["decimal_sha256"], "bits": item["bits"],
            "base_direction": parent_state["direction"],
            "evaluations": evaluations,
            "new_api_calls": len(calls), "reused_parent_positions": 1,
            "new_witnesses": sum(row["status"] == "EXACT_SQUARE_WITNESS" for row in calls),
            "sum_new_api_ns": sum(row["api_ns"] for row in calls),
            "new_evaluation_loop_ns": batch_ns,
            "new_multiplied_direction_counts": dict(Counter(row["multiplied_direction"] for row in calls))})

    assert sum(row["new_api_calls"] for row in records) == 57
    assert sum(row["reused_parent_positions"] for row in records) == 3
    result = {
        "status": "COMPLETED_FIXED_HISTORICAL_PREFIX_MATHEMATICAL_OBSERVATIONS",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "fca4ad184d83679f38a66ae99763c32abb829ee5",
        "project_parent": "33bb079035409809399f44bbcbd126e3a6ddaf02",
        "input_certificate_blob": input_blob,
        "source_sha256": expected_sources,
        "python": sys.version, "platform": platform.platform(),
        "frozen_prefix": prefix,
        "budget": {"public_integers": 3, "prefix_slots_per_integer": 20,
            "new_primary_api_calls_per_integer": 19, "reused_positions_per_integer": 1,
            "independent_exact_audits_per_new_position": 1,
            "timing_repeats": 0, "adaptive_parameter_changes": 0,
            "ceiling_advances": 0, "appended_fallback_candidates": 0},
        "observer_contract": {"observation_input": "pinned public N and a predetermined source-catalog multiplier",
            "output": "exact immediate square-witness status at that position",
            "information_retained": "prefix slot, multiplier, exact gap and multiplied-state D/U/Z label",
            "source_factors_or_hidden_S_used": False,
            "positive_control_factors": "known by construction and never supplied to public observations",
            "public_target_input_port": False},
        "cost_contract": {"single_pass": True,
            "api_ns": "unchanged witness API call; its current input validation and generic root implementation included",
            "loop_ns": "new-position API calls, independent audits and evaluation-record construction",
            "outside_timers": "imports, hash/source verification, input parsing, constructive controls and final serialization",
            "not_claimed": "stable benchmark, first-hit production time, complete scan coverage or overall factorization speedup"},
        "positive_family": {"formula": "N=t(2t+1), odd t>=3; 8N=(4t+1)^2-1",
            "gcd_identity": "gcd(N,4t)=t", "prefix_member": 8,
            "integer_success_guaranteed_no_later_than_slot": 4,
            "infinite_prime_pair_claim": False,
            "checked_constructions": len(positive_controls),
            "known_prime_pairs": sum(row["known_prime_pair"] for row in positive_controls),
            "controls": positive_controls},
        "records": records,
        "interpretation": "The finite prefix is one catalog specialist. A non-hit ends this declared budget and does not reject the retained positive family or authorize a wider scan.",
        "goal_status": "ACTIVE; full library verification and public-RSA factoring effectiveness remain unfinished",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir / "brc_public_frozen_prefix_20260908.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "positive_constructions": len(positive_controls),
        "known_prime_pairs": result["positive_family"]["known_prime_pairs"],
        "records": [{k: v for k, v in row.items() if k not in ("evaluations", "source_pdf", "decimal_sha256")}
                    for row in records]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
