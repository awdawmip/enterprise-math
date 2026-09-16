"""A frozen catalog-prefix audit and paired D/U constructive witnesses.

The three public mathematical inputs and source prefix are pinned. Previously
verified positions are consumed, and each newly declared position is evaluated
once. No range extension, advancing ceiling or appended fallback is used.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha1, sha256
from math import gcd, isqrt
from pathlib import Path
from random import Random
from time import perf_counter_ns
import json
import platform
import sys


FROZEN_PREFIX = (
    1,3,5,7,8,9,13,15,16,24,25,27,32,33,45,48,49,56,63,64,72,75,80,81,88,96,
    105,112,117,120,121,125,128,135,144,147,169,175,192,200,208,216,224,225,
    240,243,245,256,288,289,297,320,325,343,352,361,363,375,384,392,400,405,
    432,441,448,480,504,507,512,528,529,567,576,600,605,625,637,648,675,720,
    729,735,768,784,792,800,825,832,841,845,847,864,867,896,945,960,961,968,
)
INPUT_BLOBS = {
    "brc_public_rsa_fixed_predicates_20260908.json": "e56cfc8457e2398b5de3c90182c2b37824580ef3",
    "brc_public_frozen_prefix_20260908.json": "c4b201e608167cfff96c5a141bd9e26b575dad69",
    "brc_materialized_gap_order_20260908.json": "9a866dd4a923fa046768346c3ce0f1f49f4dc73c",
    "brc_native_square_root_audit_20260908.json": "913084dd4a7934670f9bd42b475ae4b905fbb380",
}
SOURCE_BLOBS = {
    "core.py": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
    "brc_opportunistic_shortcuts.py": "1214aa09770893fb3de7f85b994d1994ff56bffe",
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
}


def checked_text(path, blob):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == blob
    return raw.decode("utf-8")


def audit_lift_windows(controls, prefix, kernels):
    """Check proposed scaled identities and their exact ceiling windows.

    Only previously constructed identities and the fixed small multiplier set
    enter this algebraic audit. It never asks for another public witness.
    """
    rays = {}
    assigned = []
    for d in kernels:
        base_m = d if d % 2 else 4*d
        ray = []
        for m in prefix:
            if m % base_m:
                continue
            scale = isqrt(m//base_m)
            if base_m*scale*scale == m:
                ray.append((m,scale))
                assigned.append(m)
        rays[base_m] = ray
    assert len(assigned) == len(set(assigned)) == 98 and set(assigned) == set(prefix)
    records = []
    total_cases = 0
    transported = Counter()
    outside_window = 0
    for control in controls:
        base_m = control["multiplier"]
        t,q = map(int,control["factor_pair"])
        n = t*q
        a,b = map(int,control["witness"])
        gap = b*b
        assert b > 0 and a*a-gap == base_m*n and (a-1)**2 < base_m*n
        max_scale = (2*a-1)//gap
        counts = Counter()
        outside = 0
        for m,scale in rays[base_m]:
            total_cases += 1
            scaled_a, scaled_b = scale*a, scale*b
            target = m*n
            assert scaled_a*scaled_a-scaled_b*scaled_b == target
            immediate = (scaled_a-1)**2 < target <= scaled_a*scaled_a
            assert immediate == (scale <= max_scale)
            if immediate:
                j = scaled_a-1
                r = target-j*j
                assert 0 < r <= 2*j
                direction = "D" if r <= j else "U"
                assert direction == ("U" if scale*gap < a else "D")
                counts[direction] += 1
                transported[direction] += 1
            else:
                outside += 1
                outside_window += 1
        records.append({"kernel": control["kernel"], "base_multiplier": base_m,
            "size_class": control["size_class"], "base_assigned_direction": control["assigned_multiplied_direction"],
            "ray_entries_in_prefix": len(rays[base_m]), "maximum_preserving_scale": str(max_scale),
            "U_scale_end": str((a-1)//gap), "D_scale_start": str((a+gap-1)//gap),
            "preserved_ceiling_identity_counts": dict(counts), "outside_this_identity_window": outside})
    assert total_cases == 392 and sum(transported.values()) == 207
    assert transported == {"D": 30, "U": 177} and outside_window == 185
    return {"ray_count": 13, "partitioned_source_entries": 98,
        "proposed_identity_checks": total_cases, "preserved_immediate_identities": sum(transported.values()),
        "preserved_direction_counts": dict(transported), "outside_this_identity_window": outside_window,
        "formula": "For a valid immediate-ceiling witness a^2-mN=b^2>0 and integer scale v>=1, its scaled identity stays immediate iff v<=floor((2a-1)/b^2). It is U for v*b^2<a and D otherwise within that window.",
        "scope": "The transported identity's ceiling property only. No absence of different witnesses or preservation of a specific gcd factor is asserted outside or inside the window.",
        "new_public_queries": 0, "new_source_witness_calls": 0, "records": records}


def small_prime(value):
    # Only the explicitly constructed h=2 factors enter this bounded check.
    assert 0 <= value < 50000
    return value >= 2 and all(value % d for d in range(2, isqrt(value)+1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    for name, blob in SOURCE_BLOBS.items():
        checked_text(args.enterprise_root/"src"/"enterprise_math"/name, blob)
    sys.path.insert(0, str(args.enterprise_root/"src"))
    from enterprise_math.brc_opportunistic_shortcuts import SQUAREFREE_KERNEL13, kernel13_prefix
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    documents = [json.loads(checked_text(Path(__file__).resolve().parent/name, blob))
        for name, blob in INPUT_BLOBS.items()]
    parent, prior, projected, native_audit = documents
    labels = ["RSA-270", "RSA-896", "RSA-2048"]
    assert [r["label"] for r in parent["records"]] == labels
    assert [r["label"] for r in prior["records"]] == labels
    assert [r["label"] for r in projected["public_records"]] == labels
    assert native_audit["coverage"]["reused_public_positions"] == 66
    assert native_audit["core_blobs"]["candidate"] == SOURCE_BLOBS["core.py"]
    started = perf_counter_ns()
    prefix = kernel13_prefix(1000)
    setup_ns = perf_counter_ns()-started
    assert prefix == FROZEN_PREFIX and len(prefix) == len(set(prefix)) == 98
    kernels = tuple(SQUAREFREE_KERNEL13)
    assert kernels == (1,13,14,3,15,2,5,6,30,22,105,33,7)
    slots = {m: index+1 for index,m in enumerate(prefix)}

    # Each kernel receives a matched pair at h=2 and one fixed large even h.
    # Pair members have the same first factor and prescribed multiplier.
    prescribed = []
    for d in kernels:
        c, m, coefficient = (d,d,2) if d % 2 else (2*d,4*d,1)
        assert m in slots and c*c == m*d and 2*c == m*coefficient
        for h in (2, (1 << 511)+2):
            b = c*h+1
            t = b*h-1
            assert h % 2 == 0 and t > 1 and t % 2 == 1
            for direction in ("D", "U"):
                gap_root = b if direction == "D" else 1
                q = d*t+coefficient*gap_root
                n = t*q
                prescribed.append({"kernel": d, "c": c, "multiplier": m,
                    "h": h, "t": t, "q": q, "N": n,
                    "expected_gap_root": gap_root, "expected_direction": direction})
    assert len(prescribed) == 52
    assert len({(p["N"],p["multiplier"]) for p in prescribed}) == 52
    Random(20260908).shuffle(prescribed)
    controls = []
    for execution_index, case in enumerate(prescribed):
        d,c,m,h,t,q,n,v,direction = (case[k] for k in
            ("kernel","c","multiplier","h","t","q","N","expected_gap_root","expected_direction"))
        started = perf_counter_ns()
        witness = ceiling_completion_square_witness(n, m)
        assert witness is not None
        a, b = witness
        factor = gcd(n, a-b)
        assert 1 < factor < n and n % factor == 0
        assert factor*(n//factor) == n and a*a-b*b == m*n
        api_and_verification_ns = perf_counter_ns()-started
        assert (a,b) == (c*t+v,v) and factor == t and gcd(t,q) == 1
        assert (a-1)**2 < m*n < a*a
        j = a-1
        remainder = m*n-j*j
        if direction == "D":
            assert a == b*b-c and remainder == j-c and b*b == a+c
            assert 0 < remainder <= j
        else:
            assert b == 1 and remainder == 2*j
        base_j = isqrt(n)
        base_r = n-base_j*base_j
        base_direction = "Z" if base_r == 0 else "D" if base_r <= base_j else "U"
        controls.append({"execution_index": execution_index, "kernel": d,
            "c": c, "multiplier": m, "h": str(h), "size_class": "small" if h == 2 else "large",
            "N_bits": n.bit_length(), "N_sha256": sha256(str(n).encode("ascii")).hexdigest(),
            "factor_pair": [str(t),str(q)], "coprime_factor_pair": True,
            "witness": [str(a),str(b)], "base_direction": base_direction,
            "assigned_multiplied_direction": direction,
            "guaranteed_prefix_slot_at_most": slots[m],
            "exact_state_relation": "R=J-c, A=a+c" if direction == "D" else "R=2J, A=1",
            "api_and_factor_verification_ns": api_and_verification_ns,
            "known_small_prime_pair": small_prime(t) and small_prime(q) if h == 2 else None})
    controls.sort(key=lambda r: (kernels.index(r["kernel"]), r["size_class"] != "small", r["assigned_multiplied_direction"]))
    assert Counter(r["assigned_multiplied_direction"] for r in controls) == {"D": 26, "U": 26}
    assert max(r["guaranteed_prefix_slot_at_most"] for r in controls) == 30

    records = []
    for original, saved, added in zip(parent["records"], prior["records"], projected["public_records"], strict=True):
        n = int(original["N"])
        assert sha256(original["N"].encode("ascii")).hexdigest() == original["decimal_sha256"]
        existing = {}
        for entry in saved["evaluations"]:
            assert entry["status"] in ("REUSED_PINNED_NO_WITNESS", "NO_WITNESS_AT_THIS_POSITION")
            existing[entry["multiplier"]] = (int(entry["gap"]),entry["multiplied_direction"])
        for entry in added["new_derived_positions"]:
            assert entry["square_witness"] is None and entry["target_multiplier"] not in existing
            existing[entry["target_multiplier"]] = (int(entry["A"]),entry["direction"])
        assert len(existing) == 22 and len(set(prefix)&set(existing)) == 16
        evaluations = []
        started_loop = perf_counter_ns()
        for slot,m in enumerate(prefix,1):
            if m in existing:
                gap, direction = existing[m]
                evaluations.append({"prefix_slot": slot, "multiplier": m,
                    "status": "REUSED_PINNED_NO_WITNESS", "new_api_call": False,
                    "api_ns": None, "gap": str(gap), "multiplied_direction": direction})
                continue
            started = perf_counter_ns()
            witness = ceiling_completion_square_witness(n, m)
            api_ns = perf_counter_ns()-started
            target = m*n
            j = isqrt(target)
            remainder = target-j*j
            assert j*j <= target < (j+1)**2
            a = j if remainder == 0 else j+1
            gap = a*a-target
            b = isqrt(gap)
            assert b*b <= gap < (b+1)**2
            expected = (a,b) if b*b == gap else None
            assert witness == expected
            direction = "Z" if remainder == 0 else "D" if remainder <= j else "U"
            item = {"prefix_slot": slot, "multiplier": m,
                "status": "NO_WITNESS_AT_THIS_POSITION" if witness is None else "EXACT_SQUARE_WITNESS",
                "new_api_call": True, "api_ns": api_ns, "gap": str(gap),
                "multiplied_direction": direction, "exact_interval_and_square_checks": True}
            if witness is not None:
                item["witness"] = [str(a),str(b)]
            evaluations.append(item)
        loop_ns = perf_counter_ns()-started_loop
        new = [e for e in evaluations if e["new_api_call"]]
        assert len(evaluations) == 98 and len(new) == 82
        direction_summaries = []
        for direction in ("D", "U", "Z"):
            group = [e for e in new if e["multiplied_direction"] == direction]
            direction_summaries.append({"direction": direction, "new_positions": len(group),
                "new_square_witnesses": sum(e["status"] == "EXACT_SQUARE_WITNESS" for e in group),
                "sum_api_ns": sum(e["api_ns"] for e in group)})
        records.append({"label": original["label"], "bits": n.bit_length(),
            "source_pdf": original["source_pdf"], "decimal_sha256": original["decimal_sha256"],
            "base_direction": original["state_annotation"]["direction"],
            "reused_positions": 16, "new_api_calls": 82,
            "new_square_witnesses": sum(e["status"] == "EXACT_SQUARE_WITNESS" for e in new),
            "sum_new_api_ns": sum(e["api_ns"] for e in new), "evaluation_loop_ns": loop_ns,
            "new_direction_summaries": direction_summaries, "evaluations": evaluations})
    prime_controls = [r for r in controls if r["known_small_prime_pair"]]
    assert len(prime_controls) == 12
    result = {"status": "COMPLETED_FROZEN_KERNEL13_AND_PAIRED_STATE_EXPERIMENT",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "b2d9ceff961c70ecb356721aafcb03d31396daeb",
        "project_parent": "bd5251aae5669bf570180dc8e44128eb1c1e169b",
        "source_blobs": SOURCE_BLOBS, "input_certificates": INPUT_BLOBS,
        "python": sys.version, "platform": platform.platform(),
        "frozen_prefix": prefix, "kernel_ids": kernels, "source_prefix_generation_ns": setup_ns,
        "paired_family": {"odd_kernel": "c=d, m=d, lambda=2",
            "even_kernel": "c=2d, m=4d, lambda=1",
            "parameters": "even h>=2; b=c*h+1; t=b*h-1",
            "U": "N=t(d*t+lambda), a=c*t+1, A=1, R=2J",
            "D": "N=t(d*t+lambda*b), a=b^2-c, A=b^2=a+c, R=J-c",
            "factor_certificate": "gcd(N,a-gap_root)=t; the two constructed factors are coprime",
            "known_small_prime_pairs": len(prime_controls),
            "large_prime_pair_claimed": False, "infinite_prime_pair_claimed": False,
            "guaranteed_prefix_slot_at_most": 30,
            "slot_scope": "Assigned positive witness gives an upper bound; earlier prefix candidates are not run on controls, so first-hit direction/rank is not asserted."},
        "positive_controls": controls, "records": records,
        "lift_window_audit": audit_lift_windows(controls, prefix, kernels),
        "coverage": {"public_integers": 3, "source_prefix_entries": 98,
            "new_public_positions": 246, "reused_public_positions_in_prefix": 48,
            "prior_unique_public_positions": 66, "resulting_unique_public_positions": 312,
            "new_public_api_calls": 246, "new_position_exact_checks": 246,
            "public_timing_repeats": 0, "ceiling_advances": 0, "appended_fallback_candidates": 0,
            "assigned_constructive_checks": 52, "D_constructive_checks": 26, "U_constructive_checks": 26},
        "reuse_resolution": "REUSE_EXECUTED for existing kernel13_prefix(1000) and witness API on the verified native-root core; COMPOSE_APPLIED for state-separated difference-of-squares constructions.",
        "cost_contract": {"api_ns": "Complete unchanged witness API, including the native target-root preparation and existing 4032 filter.",
            "loop_ns": "All prefix records, actual new API calls, exact interval/square checks and result construction.",
            "outside_public_timers": "Source/input verification, parsing, source-prefix setup, 52 constructive controls, imports and serialization.",
            "audit_scope": "The reference reconstruction uses the same math.isqrt primitive; explicit integer bounds and square identities verify wrapper/filter results. No independent root algorithm is claimed.",
            "control_timing": "One prescribed source call plus gcd/product verification; fixture generation, labels and bounded small-factor primality checks are outside.",
            "lift_window_extension": "Separate exact checks on saved constructive identities after public timers; no added public query or source witness call.",
            "not_claimed": "Stable comparative benchmark, independent hit-rate observations from paired controls, exhaustive toolkit coverage, or public factorization effectiveness."},
        "goal_status": "ACTIVE; this source prefix is verified under its fixed budget and positive states are retained"}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir/"brc_kernel13_state_pairs_20260908.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "prefix_entries": len(prefix),
        "prefix_generation_ns": setup_ns, "positive_checks": len(controls),
        "known_small_prime_pairs": len(prime_controls),
        "records": [{k:v for k,v in r.items() if k not in ("evaluations","source_pdf","decimal_sha256")}
            for r in records]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
