"""Compile only the 13 frozen D/U affine predicates into modular masks.

The experiment consumes pinned prior observations, compiles finite modular
tables, verifies their serialization, and measures the same fixed inputs.
"""
from __future__ import annotations

import argparse
from array import array
from base64 import b64decode, b64encode, b85decode, b85encode
from hashlib import sha1, sha256
from math import gcd, isqrt
from pathlib import Path
from statistics import median
from time import perf_counter_ns
import json
import platform
import sys
import zlib


AFFINE_CODE_BLOB = "89d832ed4242e5d0fddae957435b41cdd5efb2c4"
AFFINE_RESULT_BLOB = "a54bf67a0966d7789da6534062cd36b2bdb06824"
ROUNDS = 9
REPEATS = 8


def checked_text(path, blob):
    raw = path.read_bytes().replace(b"\r\n",b"\n").rstrip(b"\n")+b"\n"
    assert sha1(f"blob {len(raw)}\0".encode("ascii")+raw).hexdigest() == blob
    return raw.decode("utf-8")


def audit_payload_encoding(result):
    """Compare serialization only on the already compiled exact table bytes."""
    legacy = result["precompiled_payloads"]
    compact = {key:value for key,value in legacy.items() if key != "payloads"}
    compact["payloads"] = []
    expected = []
    for payload in legacy["payloads"]:
        compressed = b85decode(payload["zlib_base85"])
        raw = zlib.decompress(compressed)
        assert len(raw) == payload["raw_bytes"] and sha256(raw).hexdigest() == payload["sha256"]
        expected.append(raw)
        compact["payloads"].append({key:value for key,value in payload.items() if key != "zlib_base85"}
            | {"zlib_base64": b64encode(compressed).decode("ascii")})
    expected = tuple(expected)
    envelopes = {
        "base85": json.dumps(legacy,separators=(",",":")),
        "base64": json.dumps(compact,separators=(",",":")),
    }

    def load_payload(kind):
        data = json.loads(envelopes[kind])
        assert data["pairs"] == legacy["pairs"]
        assert data["D_bit_indices"] == list(range(13))
        assert data["U_bit_indices"] == list(range(13,26))
        loaded = []
        for payload in data["payloads"]:
            compressed = (b85decode(payload["zlib_base85"]) if kind == "base85"
                          else b64decode(payload["zlib_base64"],validate=True))
            raw = zlib.decompress(compressed)
            assert len(raw) == payload["raw_bytes"] and sha256(raw).hexdigest() == payload["sha256"]
            values = array("I")
            values.frombytes(raw)
            assert len(values) == payload["modulus"]
            loaded.append(values.tobytes())
        return tuple(loaded)

    assert load_payload("base85") == load_payload("base64") == expected
    raw_rounds = {"base85":[],"base64":[]}
    for round_index in range(9):
        order = ("base85","base64") if round_index % 2 == 0 else ("base64","base85")
        for kind in order:
            started = perf_counter_ns()
            for _ in range(3):
                assert load_payload(kind) == expected
            elapsed = perf_counter_ns()-started
            raw_rounds[kind].append({"round": round_index,"order_slot": order.index(kind)+1,
                "repeats": 3,"total_ns": elapsed,"ns_per_load": elapsed/3})
    medians = {kind:median(row["ns_per_load"] for row in rows) for kind,rows in raw_rounds.items()}
    return {"status": "VERIFIED_SAME_PAYLOAD_WITH_BASE64",
        "base64_payload": compact, "envelope_chars": {k:len(v) for k,v in envelopes.items()},
        "median_ns_per_checked_load": medians, "raw_rounds": raw_rounds,
        "paired_base64_faster_rounds": sum(b["total_ns"] < a["total_ns"]
            for a,b in zip(raw_rounds["base85"],raw_rounds["base64"],strict=True)),
        "checked_load_speedup": medians["base85"]/medians["base64"],
        "exact_all_payload_bytes_equal": True,
        "timed": "JSON parsing, decoding, decompression, SHA256 checks, uint32 construction and byte equality; filesystem I/O excluded.",
        "new_public_queries": 0,"new_public_state_observations": 0,
        "extension_scope": "Encoding and loading of saved masks only; earlier predicate timings are retained unchanged."}


def audit_d_residue_families(result):
    """Construct positives from every allowed small residue class; no N scan."""
    pairs = result["mask_contract"]["pairs"]
    masks = {}
    for payload in result["payload_encoding_audit"]["base64_payload"]["payloads"]:
        raw = zlib.decompress(b64decode(payload["zlib_base64"],validate=True))
        assert sha256(raw).hexdigest() == payload["sha256"]
        values = array("I")
        values.frombytes(raw)
        masks[payload["modulus"]] = values
    classes = []
    records = []
    for index,(m,c) in enumerate(pairs):
        d = m if m % 2 else m//4
        odd_part = d if d % 2 else d//2
        omega = 0
        remaining = odd_part
        for prime in (3,5,7,11,13):
            if remaining % prime == 0:
                omega += 1
                remaining //= prime
                assert remaining % prime
        assert remaining == 1
        residues = [r for r in range(m)
                    if (r*r*(r*r-1)) % m == 0 and (m % 2 or r % 8 in (1,7))]
        expected_count = (1 if m % 2 else 2)*3**omega
        assert len(residues) == expected_count
        classes.append({"kernel":d,"m":m,"c":c,"odd_prime_factors":omega,
            "residues":residues,"CRT_class_count":expected_count})
        for residue in residues:
            for size,offset in (("small",0),("large",1 << 511)):
                b = m*(3+offset)+residue
                a = b*b-c
                target = a*a-b*b
                assert target % m == 0 and a-b > m
                n = target//m
                assert n > 0 and n % 2 and target > c*c
                started = perf_counter_ns()
                bit = 1 << index
                for modulus in (4096,3465,221,12673):
                    assert masks[modulus][n % modulus] & bit
                value = 4*m*n+4*c+1
                y = isqrt(value)
                assert y*y == value and y > 2*c+1
                observed_a = (y+1)//2
                gap = observed_a*observed_a-m*n
                observed_b = isqrt(gap)
                assert observed_b*observed_b == gap
                factor = gcd(n,observed_a-observed_b)
                assert 1 < factor < n and n % factor == 0
                assert factor*(n//factor) == n
                elapsed = perf_counter_ns()-started
                assert (observed_a,observed_b) == (a,b)
                j = a-1
                remainder = target-j*j
                assert 0 < remainder == j-c <= j
                assert gap == j+c+1
                records.append({"kernel":d,"m":m,"c":c,"b_residue":residue,
                    "size_class":size,"N_bits":n.bit_length(),
                    "N_sha256":sha256(str(n).encode("ascii")).hexdigest(),
                    "factor_pair":[str(factor),str(n//factor)],
                    "factors_coprime":gcd(factor,n//factor) == 1,
                    "assigned_positive_verified":True,
                    "mask_roots_and_factor_verification_ns":elapsed})
    assert sum(row["CRT_class_count"] for row in classes) == 96 and len(records) == 192
    return {"status":"VERIFIED_COMPLETE_D_RESIDUE_CLASS_CONSTRUCTIONS",
        "integer_condition":"m divides b^2*(b^2-1), because c^2=0 and 2c=0 modulo m.",
        "odd_N_condition":"Automatic for odd m; for m=8e with odd squarefree e, additionally b=1 or 7 modulo 8.",
        "parameters":"For each allowed residue r modulo m: b=m*(3+offset)+r; offset=0 or 2^511.",
        "formula":"a=b^2-c; N=((a-b)*(a+b))/m; R=J-c; A=J+c+1=b^2.",
        "proper_factor_scope":"a-b>m implies 1<gcd(N,a-b)<N. Prime factors or coprimality are not asserted generally.",
        "classes":classes,"total_residue_classes":96,"positive_certificates":192,
        "records":records,
        "single_pass_median_ns_by_size":{size:median(r["mask_roots_and_factor_verification_ns"]
            for r in records if r["size_class"] == size) for size in ("small","large")},
        "cost_scope":"One assigned (m,c) per constructed N: four mask checks, both exact roots, gcd and product verification. Input construction, table loading and later annotations are excluded; these are single-pass descriptive costs.",
        "new_public_queries":0,"new_public_state_observations":0,
        "general_semiprime_claimed":False,"new_prime_pair_checks":0,
        "extension_scope":"Finite constructive residue classes; no public search, timing replay or candidate-range extension."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root",type=Path,required=True)
    parser.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    checked_text(here/"brc_affine_state_gate_audit_20260908.py",AFFINE_CODE_BLOB)
    import brc_affine_state_gate_audit_20260908 as preceding
    certificate = json.loads(checked_text(here/"brc_affine_state_gate_audit_20260908.json",AFFINE_RESULT_BLOB))
    for name,blob in preceding.SOURCE_BLOBS.items():
        checked_text(args.enterprise_root/"src"/"enterprise_math"/name,blob)
    sys.path.insert(0,str(args.enterprise_root/"src"))
    from enterprise_math import brc_opportunistic_shortcuts as catalog
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_cost, square_residue_table
    inputs,paired = [json.loads(checked_text(here/name,blob)) for name,blob in preceding.INPUT_BLOBS.items()]
    kernels = tuple(catalog.SQUAREFREE_KERNEL13)
    assert kernels == (1,13,14,3,15,2,5,6,30,22,105,33,7)
    pairs = tuple((d,d) if d % 2 else (4*d,2*d) for d in kernels)
    assert list(map(list,pairs)) == certificate["membership_contract"]["basis_pairs"]
    slots = {d:i for i,d in enumerate(kernels)}
    full_mask = (1 << 26)-1
    assert array("I").itemsize == 4 and sys.byteorder == "little"
    moduli = (4032,4096,3465,221,12673)
    table_has = catalog._table_has
    catalog._square_residue_bitset.cache_clear()
    square_residue_table.cache_clear()
    started = perf_counter_ns()
    residue_tables = {m: square_residue_table(m) if m == 4032 else catalog._square_residue_bitset(m)
                      for m in moduli}
    residue_setup_ns = perf_counter_ns()-started
    compiled = {}
    compile_times = {}
    for modulus in moduli:
        table = residue_tables[modulus]
        started = perf_counter_ns()
        masks = array("I",[0])*modulus
        for r in range(modulus):
            value = 0
            for i,(m,c) in enumerate(pairs):
                if table_has(table,(4*m*r+4*c+1) % modulus):
                    value |= 1 << i
                if table_has(table,(m*r+1) % modulus):
                    value |= 1 << (i+13)
            masks[r] = value
        compile_times[str(modulus)] = perf_counter_ns()-started
        assert len(masks) == modulus and all(value <= full_mask for value in masks)
        compiled[modulus] = masks
    # The omitted D-only power-of-two test is now represented explicitly:
    # every reachable odd residue has all 13 D bits set.
    assert all(compiled[4096][r] & ((1 << 13)-1) == (1 << 13)-1 for r in range(1,4096,2))
    payloads = []
    started = perf_counter_ns()
    for modulus in moduli:
        raw = compiled[modulus].tobytes()
        payloads.append({"modulus": modulus, "word_order": "little-endian uint32",
            "raw_bytes": len(raw), "sha256": sha256(raw).hexdigest(),
            "zlib_base85": b85encode(zlib.compress(raw,9)).decode("ascii")})
    serialization_ns = perf_counter_ns()-started
    envelope = json.dumps({"pairs": pairs, "D_bit_indices": list(range(13)),
        "U_bit_indices": list(range(13,26)), "payloads": payloads},separators=(",",":"))

    def load_masks(text):
        data = json.loads(text)
        assert data["pairs"] == list(map(list,pairs))
        assert data["D_bit_indices"] == list(range(13)) and data["U_bit_indices"] == list(range(13,26))
        loaded = {}
        for payload in data["payloads"]:
            raw = zlib.decompress(b85decode(payload["zlib_base85"]))
            assert len(raw) == payload["raw_bytes"] and sha256(raw).hexdigest() == payload["sha256"]
            values = array("I")
            values.frombytes(raw)
            assert len(values) == payload["modulus"]
            loaded[payload["modulus"]] = values
        return loaded

    # Timed loader includes JSON parsing, decoding, decompression and hashing.
    started = perf_counter_ns()
    loaded = load_masks(envelope)
    checked_load_ns = perf_counter_ns()-started
    assert all(loaded[m] == compiled[m] for m in moduli)

    def floor_membership(n,indices,requested_mask):
        result = 0
        for i in indices:
            m,c = pairs[i]
            a,gap = ceiling_completion_cost(n,m)
            j = a-1
            remainder = 2*a-1-gap
            if gap > 0 and remainder == j-c and m*n > c*c:
                result |= 1 << i
            if gap == 1:
                result |= 1 << (i+13)
        return result & requested_mask

    def compiled_membership(n,indices,requested_mask,selected_moduli):
        possible = requested_mask
        for modulus in selected_moduli:
            r = n & 4095 if modulus == 4096 else n % modulus
            possible &= loaded[modulus][r]
            if not possible:
                return 0
        result = 0
        while possible:
            bit = possible & -possible
            index = bit.bit_length()-1
            possible ^= bit
            if index < 13:
                m,c = pairs[index]
                value = 4*m*n+4*c+1
                root = isqrt(value)
                if root*root == value and root > 2*c+1:
                    result |= bit
            else:
                m,c = pairs[index-13]
                value = m*n+1
                root = isqrt(value)
                if root*root == value:
                    result |= bit
        return result

    variants = {
        "floor_source": floor_membership,
        "compiled_static4032": lambda n,i,m: compiled_membership(n,i,m,(4032,)),
        "compiled_low12": lambda n,i,m: compiled_membership(n,i,m,(4096,3465,221,12673)),
    }
    groups = []
    public_records = []
    for original,saved in zip(inputs["records"],certificate["public_observations"],strict=True):
        n = int(original["N"])
        assert n % 2 and original["label"] == saved["label"]
        assert sha256(original["N"].encode("ascii")).hexdigest() == saved["decimal_sha256"]
        expected = 0
        for i,state in enumerate(saved["states"]):
            assert (state["m"],state["c"]) == pairs[i]
            expected |= int(state["D_strip_member"]) << i
            expected |= int(state["U_boundary_member"]) << (i+13)
        indices = tuple(range(13))
        assert all(method(n,indices,full_mask) == expected for method in variants.values())
        phases = []
        possible = full_mask
        for modulus in (4096,3465,221,12673):
            residue = n % modulus
            possible &= loaded[modulus][residue]
            phases.append({"modulus": modulus, "N_residue": residue,
                "admitted_D_bits": (possible & ((1 << 13)-1)).bit_count(),
                "admitted_U_bits": (possible >> 13).bit_count(),
                "combined_mask": possible})
        public_records.append({"label": original["label"], "bits": n.bit_length(),
            "existing_positions": 13, "expected_membership_mask": expected,
            "low12_intersections": phases, "low12_exact_root_calls": possible.bit_count()})
        groups.append({"name": original["label"],"kind": "public_existing_packet",
            "unit": "one N with all 13 assigned pairs", "cases": [(n,indices,full_mask,expected)]})
    for size in ("small","large"):
        for direction in ("D","U"):
            cases = []
            for row in paired["positive_controls"]:
                if row["size_class"] != size or row["assigned_multiplied_direction"] != direction:
                    continue
                n = int(row["factor_pair"][0])*int(row["factor_pair"][1])
                i = slots[row["kernel"]]
                requested = (1 << i) | (1 << (i+13))
                expected = 1 << (i if direction == "D" else i+13)
                assert all(method(n,(i,),requested) == expected for method in variants.values())
                cases.append((n,(i,),requested,expected))
            assert len(cases) == 13
            groups.append({"name": f"{size}_{direction}","kind": "assigned_positive_cohort",
                "unit": "13 distinct positive N with one assigned pair each", "cases": cases})

    def evaluate_group(method,cases):
        return tuple(method(n,i,m) for n,i,m,expected in cases)

    measurements = []
    for group_index,group in enumerate(groups):
        cases = group["cases"]
        expected = tuple(x[3] for x in cases)
        for method in variants.values():
            assert evaluate_group(method,cases) == expected
        raw = {name:[] for name in variants}
        names = tuple(variants)
        for round_index in range(ROUNDS):
            offset = (round_index+group_index) % len(names)
            order = names[offset:]+names[:offset]
            for name in order:
                started = perf_counter_ns()
                for _ in range(REPEATS):
                    assert evaluate_group(variants[name],cases) == expected
                elapsed = perf_counter_ns()-started
                raw[name].append({"round": round_index,"order_slot": order.index(name)+1,
                    "repeats": REPEATS,"total_ns": elapsed,"ns_per_group": elapsed/REPEATS})
        medians = {name:median(x["ns_per_group"] for x in values) for name,values in raw.items()}
        measurements.append({"name": group["name"],"kind": group["kind"],"unit": group["unit"],
            "median_ns_per_group": medians, "raw_rounds": raw,
            "speedup_vs_same_membership_floor": {name:medians["floor_source"]/value for name,value in medians.items()},
            "paired_faster_rounds": {name:sum(x["total_ns"] < raw["floor_source"][i]["total_ns"]
                for i,x in enumerate(values)) for name,values in raw.items() if name != "floor_source"}})

    result = {
        "status": "VERIFIED_COMPILED_FIXED_AFFINE_STATE_MASKS",
        "researcher": "EM-HME-0CE4FD / TASK_RESEARCH",
        "global_snapshot": "91cd38de772d892c0707ba356d7bbcecb44996bb",
        "project_parent": "9fb93e7ef1988f2feaabdc76133af08490400ddd",
        "preceding_artifacts": {"brc_affine_state_gate_audit_20260908.py": AFFINE_CODE_BLOB,
            "brc_affine_state_gate_audit_20260908.json": AFFINE_RESULT_BLOB},
        "source_blobs": preceding.SOURCE_BLOBS,"input_blobs": preceding.INPUT_BLOBS,
        "python": sys.version,"platform": platform.platform(),
        "mask_contract": {"pairs": pairs,"D_bits": list(range(13)),"U_bits": list(range(13,26)),
            "row_definition": "Bit i is set iff 4*m_i*r+4*c_i+1 is square modulo M; bit i+13 iff m_i*r+1 is square modulo M.",
            "scope": "Necessary modular conditions for the same 26 fixed state predicates; exact roots decide survivors.",
            "D_threshold": "Exact D membership also requires mN>c^2, enforced by root>2c+1.",
            "query": "Intersect the requested bits across tables indexed by N mod M, then check only surviving exact affine-square values.",
            "state_membership_only": True},
        "setup": {"source_residue_tables_ns": residue_setup_ns,
            "compile_ns_by_modulus": compile_times,"total_compile_ns": sum(compile_times.values()),
            "serialization_ns": serialization_ns,"checked_all_table_load_ns": checked_load_ns,
            "checked_load_scope": "JSON string parsing, base85 decoding, zlib decompression, SHA256 checks and uint32 construction; filesystem I/O excluded.",
            "raw_static4032_bytes": len(loaded[4032])*4,
            "raw_low12_bytes": sum(len(loaded[m])*4 for m in (4096,3465,221,12673)),
            "all_raw_bytes": sum(len(values)*4 for values in loaded.values()),
            "serialized_envelope_chars": len(envelope),"exact_payload_roundtrip": True,
            "D_4096_odd_residues_all_admitted": True},
        "precompiled_payloads": json.loads(envelope),
        "public_records": public_records, "positive_state_checks_retained": 52,
        "measurements": measurements,
        "cost_contract": {"rounds": ROUNDS,"repeats_per_round": REPEATS,
            "timed": "Per-N modular reduction, mask lookups/intersection, exact roots for survivors, result construction and equality checks.",
            "excluded": "Imports, source/input checks, mask compilation or loading, initial warmups, serialization and instrumentation.",
            "comparisons": "Paired same-process warm replay; compare only each group against its own floor baseline, not directly against a prior run.",
            "positive_scope": "Known state membership and retained saved constructive witnesses; no end-to-end factoring speedup asserted.",
            "cold_scope": "Compilation and checked loading are separate measured costs, not free query setup."},
        "coverage": {"public_inputs": 3,"reused_public_positions": 39,"new_public_positions": 0,
            "new_public_square_completion_witness_calls": 0,"new_state_observations": 0,
            "compiled_table_rows": sum(moduli),"retained_constructive_state_checks": 52,
            "public_unique_positions_remain": 312,
            "warm_public_position_visits_per_variant": 39*ROUNDS*REPEATS,
            "warm_constructive_position_visits_per_variant": 52*ROUNDS*REPEATS,
            "warmups_and_validation_are_additional_replays": True},
        "reuse_resolution": "COMPOSE_APPLIED: compile the existing residue tables for the fixed affine predicate packet.",
        "goal_status": "ACTIVE",
    }
    result["payload_encoding_audit"] = audit_payload_encoding(result)
    result["D_residue_family_audit"] = audit_d_residue_families(result)
    result["coverage"]["new_constructive_D_certificates"] = 192
    result["coverage"]["complete_D_residue_classes"] = 96
    args.output_dir.mkdir(parents=True,exist_ok=True)
    destination = args.output_dir/"brc_compiled_affine_gate_audit_20260908.json"
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"output": str(destination),"setup": result["setup"],"public": public_records,
        "payload_encoding": {k:v for k,v in result["payload_encoding_audit"].items()
            if k not in ("base64_payload","raw_rounds")},
        "D_residue_families": {k:v for k,v in result["D_residue_family_audit"].items()
            if k not in ("classes","records")},
        "measurements": [{k:v for k,v in r.items() if k != "raw_rounds"} for r in measurements],
        "coverage": result["coverage"]},ensure_ascii=True))


if __name__ == "__main__":
    main()
