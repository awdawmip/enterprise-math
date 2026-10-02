"""A fixed seven-position prepared-state ordering experiment.

Inputs are pinned public mathematical certificates and prescribed constructive
controls. No target-input port, adaptive range expansion or factor-search
fallback is provided. Only the existing catalog ordering/filter APIs are used.
"""
from __future__ import annotations

import argparse
from hashlib import sha1, sha256
from math import gcd, isqrt
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    source_hashes = {
        "brc_opportunistic_shortcuts.py": "7e186c6b17b4b04c37af875c939a92907e929e8a19b2c0c818d3e3bc5f8b94e7",
        "brc_multiplier_priority_jump.py": "ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d",
        "brc_square_gap_prefilter.py": "f8e178771a25221eaab16002b9ffacd188dc5f39be4948ec2b40ee3e22c9f716",
    }
    for name, expected in source_hashes.items():
        assert sha256((args.enterprise_root / "src" / "enterprise_math" / name).read_bytes()).hexdigest() == expected
    sys.path.insert(0, str(args.enterprise_root / "src"))
    from enterprise_math.brc_opportunistic_shortcuts import (
        SHORTCUT_SPECS, structural_order, learned_cover_order,
        gap_sorted_order_from_materialized_states, passes_low12_compact_square_filter,
    )
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    parent_dir = Path(__file__).resolve().parent
    documents = []
    inputs = {
        "brc_public_rsa_fixed_predicates_20260908.json": "e56cfc8457e2398b5de3c90182c2b37824580ef3",
        "brc_public_frozen_prefix_20260908.json": "c4b201e608167cfff96c5a141bd9e26b575dad69",
    }
    for name, expected in inputs.items():
        raw = (parent_dir/name).read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
        assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == expected
        documents.append(json.loads(raw))
    parents, prefix = documents
    assert [r["label"] for r in parents["records"]] == ["RSA-270", "RSA-896", "RSA-2048"]
    assert [r["label"] for r in prefix["records"]] == [r["label"] for r in parents["records"]]

    # The complete source-defined representative set up to 12 is fixed before
    # any new observation. Five members exist in the archive; 5 and 11 are
    # obtained by exact floor-root projection from saved positions 80 and 99.
    fixed_orders = {"structural": structural_order(12), "learned": learned_cover_order(12)}
    assert fixed_orders == {"structural": (1,9,3,5,7,8,11), "learned": (1,8,3,7,9,5,11)}
    representatives = (1,3,5,7,8,9,11)
    order_names = ("structural", "learned", "gap_sorted")
    backend_names = ("native", "low12")

    def evaluate_prepared(gaps, order_name, backend):
        # This is a seven-scalar square-predicate comparison on prepared data.
        order = (gap_sorted_order_from_materialized_states(gaps, max_multiplier=12)
            if order_name == "gap_sorted" else fixed_orders[order_name])
        count = 0
        for m in order:
            count += 1
            value = gaps[m]
            if backend == "low12" and not passes_low12_compact_square_filter(value):
                continue
            root = isqrt(value)
            if root*root == value:
                return m, root, count
        return None, None, count

    public_records = []
    public_gaps = []
    for parent, archived in zip(parents["records"], prefix["records"], strict=True):
        n = int(parent["N"])
        assert sha256(parent["N"].encode("ascii")).hexdigest() == parent["decimal_sha256"]
        lookup = {e["multiplier"]: e for e in archived["evaluations"]}
        gaps = {m: int(lookup[m]["gap"]) for m in representatives if m in lookup}
        assert set(gaps) == {1,3,7,8,9}
        projections = []
        for target_m, source_m, divisor in ((5,80,4),(11,99,3)):
            source_gap = int(lookup[source_m]["gap"])
            started = perf_counter_ns()
            source_a = isqrt(source_m*n+source_gap)
            restoration_ns = perf_counter_ns()-started
            assert source_gap > 0 and source_a*source_a == source_m*n+source_gap
            assert (source_a-1)**2 < source_m*n <= source_a*source_a
            source_j = source_a-1
            started = perf_counter_ns()
            j = source_j//divisor
            target = target_m*n
            r = target-j*j
            a = j if r == 0 else j+1
            gap = a*a-target
            projection_ns = perf_counter_ns()-started
            assert source_m == divisor*divisor*target_m
            assert j*j <= target < (j+1)**2 and 0 <= r <= 2*j
            # Independent audit of the same derived position, not a new one.
            audit_j = isqrt(target)
            assert audit_j == j
            b = isqrt(gap)
            square = b*b == gap
            gaps[target_m] = gap
            projections.append({"source_multiplier": source_m, "target_multiplier": target_m,
                "root_divisor": divisor, "restoration_ns": restoration_ns,
                "projection_ns": projection_ns, "J": str(j), "R": str(r), "A": str(gap),
                "direction": "Z" if r == 0 else "D" if r <= j else "U",
                "square_witness": [str(a),str(b)] if square else None,
                "independent_native_root_agrees": True})
        assert tuple(sorted(gaps)) == representatives
        started = perf_counter_ns()
        sorted_order = gap_sorted_order_from_materialized_states(gaps, max_multiplier=12)
        sort_ns = perf_counter_ns()-started
        assert set(sorted_order) == set(representatives)
        assert [gaps[m] for m in sorted_order] == sorted(gaps.values())
        results = {}
        for order_name in order_names:
            for backend in backend_names:
                outcome = evaluate_prepared(gaps, order_name, backend)
                results[order_name+"/"+backend] = outcome
                if outcome[0] is not None:
                    m, b, _ = outcome
                    assert b*b == gaps[m]
        public_records.append({"label": parent["label"], "bits": n.bit_length(),
            "source_pdf": parent["source_pdf"], "decimal_sha256": parent["decimal_sha256"],
            "reused_positions": [1,3,7,8,9], "new_derived_positions": projections,
            "prepared_gaps": {str(m): str(gaps[m]) for m in representatives},
            "gap_sorted_order": sorted_order, "single_order_creation_ns": sort_ns,
            "prepared_outcomes": results})
        public_gaps.append(gaps)

    controls = []
    control_gaps = []
    prescribed = [("saved_small", item["t"]) for item in prefix["positive_family"]["controls"]]
    prescribed += [("constructed_large", (1 << ((bits-2)//2))+1) for bits in (896,2048,8192)]
    for kind, t in prescribed:
        n = t*(2*t+1)
        started = perf_counter_ns()
        gaps = {}
        ceilings = {}
        for m in representatives:
            target = m*n
            j = isqrt(target)
            a = j if j*j == target else j+1
            gaps[m] = a*a-target
            ceilings[m] = a
        materialization_ns = perf_counter_ns()-started
        assert gaps[8] == 1 and ceilings[8] == 4*t+1
        results = {}
        for order_name in order_names:
            for backend in backend_names:
                m, b, count = evaluate_prepared(gaps, order_name, backend)
                assert m is not None and b*b == gaps[m]
                factor = gcd(n, ceilings[m]-b)
                assert 1 < factor < n and n % factor == 0
                if order_name == "gap_sorted":
                    assert count == 1
                results[order_name+"/"+backend] = {"multiplier": m, "gap_root": str(b),
                    "predicate_positions": count, "proper_constructive_factor": str(factor)}
        controls.append({"kind": kind, "N_bits": n.bit_length(), "t": str(t),
            "materialization_ns": materialization_ns, "outcomes": results,
            "prime_pair_claimed": False})
        control_gaps.append(gaps)

    # Timings use the three prescribed large positive controls only. Static
    # orders are N-independent and prepared once; input-dependent source gap
    # sorting remains inside its timer. Source LOW12 tables are warm in all
    # trials. Replays are timing samples, not additional mathematical hits.
    passes_low12_compact_square_filter(0)
    rounds, repeats = 7, 256
    rng = Random(20260908)
    timings = []
    for index in range(len(controls)-3, len(controls)):
        gaps = control_gaps[index]
        cases = [(name, backend) for name in order_names for backend in backend_names]
        raw = {name+"/"+backend: [] for name, backend in cases}
        for round_number in range(rounds):
            shuffled = cases[:]
            rng.shuffle(shuffled)
            for name, backend in shuffled:
                started = perf_counter_ns()
                for _ in range(repeats):
                    evaluate_prepared(gaps, name, backend)
                elapsed = perf_counter_ns()-started
                raw[name+"/"+backend].append(elapsed/repeats)
        medians = {name: median(values) for name, values in raw.items()}
        timings.append({"control_index": index, "N_bits": controls[index]["N_bits"],
            "raw_ns_per_evaluation": raw, "median_ns": medians,
            "structural_over_sorted": {backend: medians["structural/"+backend]/medians["gap_sorted/"+backend]
                for backend in backend_names},
            "learned_over_sorted": {backend: medians["learned/"+backend]/medians["gap_sorted/"+backend]
                for backend in backend_names}})

    assert len(controls) == 18 and len(public_records) == 3
    assert len(SHORTCUT_SPECS) == 13

    # Separate complete-cost observations on the three prescribed constructive
    # inputs. Use the unchanged witness API (its default 4032 backend), include
    # every root computation and final gcd/product verification, and stop at
    # the first proper witness within the same seven fixed positions.
    # Five single-run paired rounds; no public input enters this block.
    complete_cost = []
    for index in range(len(controls)-3, len(controls)):
        t = int(controls[index]["t"])
        n = t*(2*t+1)
        raw = {"structural": [], "learned": []}
        calls = {"structural": [], "learned": []}
        for round_number in range(5):
            names = ["structural", "learned"]
            rng.shuffle(names)
            for name in names:
                started = perf_counter_ns()
                observed = None
                for count, m in enumerate(fixed_orders[name], 1):
                    witness = ceiling_completion_square_witness(n, m)
                    if witness is None:
                        continue
                    a, b = witness
                    factor = gcd(n, a-b)
                    if 1 < factor < n and n % factor == 0:
                        assert a*a-b*b == m*n and factor*(n//factor) == n
                        observed = (m, factor, count)
                        break
                elapsed = perf_counter_ns()-started
                assert observed is not None and observed[0] == 8 and observed[1] == t
                assert observed[2] == (6 if name == "structural" else 2)
                raw[name].append(elapsed)
                calls[name].append(observed[2])
        medians = {name: median(values) for name, values in raw.items()}
        complete_cost.append({"control_index": index, "N_bits": controls[index]["N_bits"],
            "raw_ns": raw, "api_calls_per_round": calls, "median_ns": medians,
            "structural_over_learned": medians["structural"]/medians["learned"],
            "learned_faster_rounds": sum(a>b for a,b in zip(raw["structural"],raw["learned"])),
            "verified_constructive_factor": str(t), "witness_multiplier": 8,
            "backend": "unchanged default witness API with modulus 4032"})
    result = {"status": "COMPLETED_FIXED_PREPARED_STATE_ORDERING_EXPERIMENT",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "b2d9ceff961c70ecb356721aafcb03d31396daeb",
        "project_parent": "79c0ed559d177082ea20ed2c3e21fc5342821da4",
        "source_sha256": source_hashes, "input_certificates": inputs,
        "python": sys.version, "platform": platform.platform(),
        "frozen_max_multiplier": 12, "representative_set": representatives,
        "fixed_orders": fixed_orders, "public_records": public_records, "positive_controls": controls,
        "timing_rounds": rounds, "timing_repeats_per_case_per_round": repeats, "timings": timings,
        "complete_cost_constructive_observations": complete_cost,
        "catalog_ids_inspected": [s.shortcut_id for s in SHORTCUT_SPECS],
        "reuse_resolution": "REUSE_EXECUTED for the unchanged complete prepared-gap sorter and existing static orders/LOW12 backend. Exact floor-root projection supplies the two explicitly named missing positions.",
        "coverage": {"public_integers": 3, "new_derived_positions": 6, "reused_positions_in_this_set": 15,
            "new_source_witness_api_calls": 0, "ceiling_advances": 0,
            "appended_fallback_candidates": 0, "positive_cases": 18,
            "new_positive_cases_at_large_sizes": 3, "timing_replays_are_new_hits": False},
        "cost_contract": {"restoration": "The archive stores A, not the source J; isqrt(source_m*N+A) restoration is paid and reported separately.",
            "projection": "Root division, target multiplication, remainder and gap formation; source J is already restored for this timer.",
            "ordering": "Complete unchanged sorter for the fixed source representative set <=12; no partial map is treated as complete for <=100.",
            "prepared_timing": "Square predicates on supplied gaps; dynamic gap-order creation included, static N-independent order creation amortized outside.",
            "outside_prepared_timing": "State acquisition, imports, source verification, initial table setup, constructive factor verification, reporting and serialization.",
            "controls": "Constructed integer factors; no large prime-pair or public challenge hit is inferred.",
            "complete_cost_control_timing": "Three fixed positive integers, five paired single-run rounds; original API root/preparation work and gcd/product verification included. Static order construction, imports, table setup and input generation excluded.",
            "complete_cost_control_api_calls": 120,
            "not_claimed": "Public-RSA factorization speedup, independent coverage from reordering, universal preferred order, or a complete-cost gap-sort speedup."},
        "goal_status": "ACTIVE; fixed branch validation completed, public factoring effectiveness and broader library work remain unfinished"}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir/"brc_materialized_gap_order_20260908.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "public": [{"label": r["label"],
        "new_witnesses": sum(p["square_witness"] is not None for p in r["new_derived_positions"]),
        "sort_order": r["gap_sorted_order"], "sort_ns": r["single_order_creation_ns"],
        "restore_ns": sum(p["restoration_ns"] for p in r["new_derived_positions"]),
        "projection_ns": sum(p["projection_ns"] for p in r["new_derived_positions"])} for r in public_records],
        "positive_controls": len(controls), "timings": [{k:v for k,v in row.items() if k != "raw_ns_per_evaluation"} for row in timings],
        "complete_cost": [{k:v for k,v in row.items() if k not in ("raw_ns","verified_constructive_factor")}
            for row in complete_cost]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
