"""Fixed-input cost audit for a D strip and the A=1 U boundary.

Only pinned public-puzzle records and the saved paired constructive fixtures
are accepted. This audits state membership, with no factor search or fallback.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha1, sha256
from math import isqrt
from pathlib import Path
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys


INPUT_BLOBS = {
    "brc_public_rsa_fixed_predicates_20260908.json": "e56cfc8457e2398b5de3c90182c2b37824580ef3",
    "brc_kernel13_state_pairs_20260908.json": "6f66b17507bce5fd98909c263724c8da7b86a641",
}
SOURCE_BLOBS = {
    "core.py": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
    "brc_opportunistic_shortcuts.py": "1214aa09770893fb3de7f85b994d1994ff56bffe",
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
    "brc_square_gap_tables.py": "c25d73f9fda5dc78e407d52987c84016e421a96b",
}
ROUNDS = 9
REPEATS = 8


def checked_text(path, blob):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n"
    assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == blob
    return raw.decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    for name, blob in SOURCE_BLOBS.items():
        checked_text(args.enterprise_root/"src"/"enterprise_math"/name, blob)
    sys.path.insert(0, str(args.enterprise_root/"src"))
    from enterprise_math import core
    from enterprise_math import brc_opportunistic_shortcuts as catalog
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_cost, square_residue_table
    assert core.integer_nth_root(1000003, 2) == isqrt(1000003)
    documents = [json.loads(checked_text(Path(__file__).resolve().parent/name, blob))
                 for name,blob in INPUT_BLOBS.items()]
    inputs, paired = documents
    assert [r["label"] for r in inputs["records"]] == ["RSA-270", "RSA-896", "RSA-2048"]
    kernels = tuple(catalog.SQUAREFREE_KERNEL13)
    assert kernels == (1,13,14,3,15,2,5,6,30,22,105,33,7)
    pairs = tuple((d,d) if d % 2 else (4*d,2*d) for d in kernels)
    assert len(pairs) == 13 and all(m in paired["frozen_prefix"] for m,c in pairs)
    low_moduli = tuple(catalog.LOW12_COMPACT_MODULI)
    assert low_moduli == (4096,3465,221,12673)

    # Load existing tables, charging first construction separately.
    square_residue_table.cache_clear()
    started = perf_counter_ns()
    static_tables = (square_residue_table(4032),)
    static_setup_ns = perf_counter_ns()-started
    catalog._square_residue_bitset.cache_clear()
    started = perf_counter_ns()
    low_tables = tuple(catalog._square_residue_bitset(m) for m in low_moduli)
    low_setup_ns = perf_counter_ns()-started
    table_has = catalog._table_has
    assert sum(len(t) for t in low_tables) == 2559
    # The existing two generators agree on the finite modular payloads.
    for modulus, table in zip(low_moduli,low_tables,strict=True):
        assert table == square_residue_table(modulus)

    def floor_membership(n, selected_pairs):
        flags = []
        for m,c in selected_pairs:
            a,gap = ceiling_completion_cost(n,m)
            j = a-1
            remainder = 2*a-1-gap
            d_member = gap > 0 and remainder == j-c and m*n > c*c
            flags.append(int(d_member) | (2 if gap == 1 else 0))
        return tuple(flags)

    def affine_membership(n, selected_pairs, moduli, tables, counts=None):
        # All per-N phase reduction is inside the measured call.
        phases = tuple(n % modulus for modulus in moduli)
        flags = []
        for m,c in selected_pairs:
            d_possible = True
            u_possible = True
            for modulus,table,phase in zip(moduli,tables,phases,strict=True):
                # For these basis pairs and odd N, H=1 mod 8. Hence H is
                # automatically a square residue modulo 4096.
                if d_possible and modulus != 4096:
                    d_possible = table_has(table,(4*m*phase+4*c+1) % modulus)
                    if not d_possible and counts is not None:
                        counts[f"D_first_exit_mod_{modulus}"] += 1
                if u_possible:
                    u_possible = table_has(table,(m*phase+1) % modulus)
                    if not u_possible and counts is not None:
                        counts[f"U_first_exit_mod_{modulus}"] += 1
                if not d_possible and not u_possible:
                    break
            d_member = False
            u_member = False
            if d_possible:
                value = 4*m*n+4*c+1
                root = isqrt(value)
                d_member = root*root == value and root > 2*c+1
                if counts is not None:
                    counts["D_exact_root_calls"] += 1
                    counts["D_members"] += int(d_member)
            if u_possible:
                value = m*n+1
                root = isqrt(value)
                u_member = root*root == value
                if counts is not None:
                    counts["U_exact_root_calls"] += 1
                    counts["U_members"] += int(u_member)
            flags.append(int(d_member) | (2 if u_member else 0))
        return tuple(flags)

    variants = {
        "floor_source": floor_membership,
        "affine_static4032": lambda n,p: affine_membership(n,p,(4032,),static_tables),
        "affine_low12": lambda n,p: affine_membership(n,p,low_moduli,low_tables),
    }
    groups = []
    observations = []
    for original,saved in zip(inputs["records"],paired["records"],strict=True):
        n = int(original["N"])
        assert n % 2 and sha256(original["N"].encode("ascii")).hexdigest() == original["decimal_sha256"]
        by_m = {r["multiplier"]:r for r in saved["evaluations"]}
        expected = []
        states = []
        for m,c in pairs:
            gap = int(by_m[m]["gap"])
            target = m*n
            a = isqrt(target+gap)
            assert a*a == target+gap and (a-1)**2 < target < a*a
            j = a-1
            remainder = target-j*j
            assert target > c*c and remainder == 2*a-1-gap
            assert (4*target+4*c+1) % 8 == 1
            flag = int(remainder == j-c) | (2 if gap == 1 else 0)
            expected.append(flag)
            states.append({"kernel": kernels[len(states)], "m": m, "c": c,
                "saved_direction": by_m[m]["multiplied_direction"],
                "D_strip_member": bool(flag & 1), "U_boundary_member": bool(flag & 2)})
        expected = tuple(expected)
        assert all(method(n,pairs) == expected for method in variants.values())
        counters = {}
        for name,moduli,tables in (("affine_static4032",(4032,),static_tables),
                                  ("affine_low12",low_moduli,low_tables)):
            counts = Counter()
            assert affine_membership(n,pairs,moduli,tables,counts) == expected
            counters[name] = dict(counts)
        observations.append({"label": original["label"], "bits": n.bit_length(),
            "decimal_sha256": original["decimal_sha256"], "source_pdf": original["source_pdf"],
            "existing_positions": len(pairs), "new_positions": 0,
            "D_members": sum(bool(x & 1) for x in expected),
            "U_members": sum(bool(x & 2) for x in expected),
            "predicate_counters": counters, "states": states})
        groups.append({"name": original["label"], "kind": "public_existing_packet",
            "unit": "one N with 13 assigned (m,c) pairs",
            "cases": [(n,pairs,expected)]})

    positive_checks = []
    for size in ("small","large"):
        for direction,flag in (("D",1),("U",2)):
            cases = []
            for row in paired["positive_controls"]:
                if row["size_class"] != size or row["assigned_multiplied_direction"] != direction:
                    continue
                t,q = map(int,row["factor_pair"])
                n = t*q
                m,c = row["multiplier"],row["c"]
                selected = ((m,c),)
                assert n % 2 and m*n > c*c
                assert all(method(n,selected) == (flag,) for method in variants.values())
                a,b = map(int,row["witness"])
                # Consume the known positive identity, without a new factor query.
                assert a*a-b*b == m*n and (a-1)**2 < m*n < a*a
                cases.append((n,selected,(flag,)))
                positive_checks.append({"kernel": row["kernel"], "m": m, "c": c,
                    "size_class": size, "N_bits": n.bit_length(), "assigned_state": direction,
                    "state_gate_flag": flag, "saved_positive_witness_retained": True,
                    "known_small_prime_pair": row["known_small_prime_pair"]})
            assert len(cases) == 13
            groups.append({"name": f"{size}_{direction}", "kind": "assigned_positive_cohort",
                "unit": "13 distinct N, each with its one assigned (m,c) pair",
                "cases": cases})
    assert len(positive_checks) == 52

    def evaluate_group(method, cases):
        return tuple(method(n,p) for n,p,expected in cases)

    measurements = []
    for group_index,group in enumerate(groups):
        cases = group["cases"]
        expected = tuple(expected for n,p,expected in cases)
        for method in variants.values():
            assert evaluate_group(method,cases) == expected
        raw = {name: [] for name in variants}
        names = tuple(variants)
        for round_index in range(ROUNDS):
            offset = (group_index+round_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    actual = evaluate_group(variants[name],cases)
                    assert actual == expected
                elapsed = perf_counter_ns()-started
                raw[name].append({"round": round_index, "order_slot": order.index(name)+1,
                    "repeats": REPEATS, "total_ns": elapsed,
                    "ns_per_group": elapsed/REPEATS})
        medians = {name: median(r["ns_per_group"] for r in rows) for name,rows in raw.items()}
        measurements.append({"name": group["name"], "kind": group["kind"], "unit": group["unit"],
            "median_ns_per_group": medians, "raw_rounds": raw,
            "speedup_vs_same_membership_floor": {name: medians["floor_source"]/ns for name,ns in medians.items()},
            "paired_faster_rounds": {name: sum(row["total_ns"] < raw["floor_source"][i]["total_ns"]
                for i,row in enumerate(rows)) for name,rows in raw.items() if name != "floor_source"}})

    result = {
        "status": "VERIFIED_FIXED_AFFINE_STATE_MEMBERSHIP_AND_COST",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "91cd38de772d892c0707ba356d7bbcecb44996bb",
        "project_parent": "9fb93e7ef1988f2feaabdc76133af08490400ddd",
        "source_blobs": SOURCE_BLOBS, "input_blobs": INPUT_BLOBS,
        "python": sys.version, "platform": platform.platform(),
        "membership_contract": {
            "D": "For mN>c^2 and c>=0, R=J-c iff 4mN+4c+1 is square.",
            "U": "For mN>0, A=1 iff mN+1 is square.",
            "scope": "These two state subsets only. D membership does not guarantee a square completion gap.",
            "flag": "bit 1: D strip membership; bit 2: U boundary membership",
            "basis_pairs": pairs,
            "power_of_two_omission": "For these pairs and odd N, H=1 mod 8, so the D-only 4096 filter is redundant. The U filter retains it.",
            "large_phase_reduction": "N is reduced once per modulus inside each candidate call; all 13 pairs reuse those phases.",
        },
        "table_setup": {"static4032_first_lookup_ns": static_setup_ns,
            "low12_cold_build_ns": low_setup_ns, "static_bytes": sum(map(len,static_tables)),
            "low12_bytes": sum(map(len,low_tables)), "equal_source_generators": True},
        "public_observations": observations, "positive_checks": positive_checks,
        "measurements": measurements,
        "cost_contract": {
            "rounds": ROUNDS, "repeats_per_round": REPEATS,
            "timed": "Complete state-membership calls including each N's modular reductions, candidate construction, roots when admitted, flag comparison and group result creation.",
            "excluded": "Imports, source/input checks, expected-state restoration, table lookup/build, initial warmup, instrumentation and serialization.",
            "positive_unit": "A 13-member cohort of distinct constructed N with one prescribed pair each; not directly comparable to the public one-N packet.",
            "repetition_scope": "Same-process paired warm timing replays, not independent success observations or fresh-process benchmarks.",
            "comparison_scope": "Same two state-membership predicates. No claimed factoring speedup or replacement of the full witness API.",
        },
        "coverage": {"public_inputs": 3, "public_existing_positions": 39,
            "new_public_positions": 0, "new_state_predicates": 78,
            "new_public_square_completion_witness_calls": 0,
            "positive_state_checks": 52, "retained_small_prime_pairs": 12,
            "public_unique_positions_remain": 312,
            "warm_public_position_visits_per_variant": 39*ROUNDS*REPEATS,
            "warm_constructive_position_visits_per_variant": 52*ROUNDS*REPEATS,
            "warmups_and_validation_are_additional_replays": True},
        "reuse_resolution": "COMPOSE_APPLIED: existing source floor completion and residue tables with the derived affine state criteria.",
        "goal_status": "ACTIVE",
    }
    args.output_dir.mkdir(parents=True,exist_ok=True)
    destination = args.output_dir/"brc_affine_state_gate_audit_20260908.json"
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output": str(destination), "tables": result["table_setup"],
        "observations": [{k:v for k,v in r.items() if k not in ("states","decimal_sha256","source_pdf")}
                         for r in observations],
        "measurements": [{k:v for k,v in r.items() if k != "raw_rounds"} for r in measurements],
        "coverage": result["coverage"]},ensure_ascii=True))


if __name__ == "__main__":
    main()
