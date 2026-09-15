"""Exact arithmetic audit of fixed synthetic BRC residual families.

Only prescribed constructed integers are used. The command line accepts source
and output directories, not moduli, keys, ciphertexts, or search horizons.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import platform
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from time import perf_counter_ns


CANONICAL = "e5a086173024bde6e59782df4c68427bbe24e3ef"
PARENT = "a93a0a74d2aefea45ef27954fdab34895230e076"
CORE_BLOB = "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07"
PRIME_HELPER_BLOB = "65f06c03038b2c95a875436c099f50f008700af3"
PRIOR_NOTE_BLOB = "fcb5c72b75c8340fd3d253fc1279b96c5afa6f3b"
OFFSETS = {"D": (1, 2, 3), "U": (2, 3, 4)}
COEFFICIENTS = (1, 3, 5, 7)
EXPONENTS = (None, 127, 511, 1023, 4095)
ROUNDS, REPEATS = 9, 4
ROOT = None


def checked_bytes(path, expected=None):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if expected is not None:
        assert blob == expected, (str(path), blob, expected)
    return raw, blob


def digest_int(value):
    return hashlib.sha256(str(value).encode("ascii")).hexdigest()


def visible_int(value):
    return {"bits": value.bit_length(), "decimal_sha256": digest_int(value),
            "decimal": str(value) if value.bit_length() < 64 else None}


def encode_packet(document):
    metadata = {k: v for k, v in document.items() if k != "records"}
    text = json.dumps(metadata, indent=2, ensure_ascii=True)
    assert text.endswith("\n}")
    rows = ",\n".join("    "+json.dumps(row, separators=(",", ":"), ensure_ascii=True)
                      for row in document["records"])
    return text[:-2]+",\n  \"records\": [\n"+rows+"\n  ]\n}\n"


def state_of(n):
    j = ROOT(n, 2)
    r = n - j*j
    assert 0 < r <= 2*j
    return j, r, 2*j+1-r, "D" if r <= j else "U"


def _fixed_probe(n, state, residual, endpoint=None, unit_only=False):
    """Private fixed-cohort arithmetic; full division is the certificate gate.

    If endpoint is absent, candidate construction reads just one residual.
    Endpoint mode is a sufficient subcase, not an equivalent composite test.
    Return (factor, cofactor, c, b, big_divisions, short_remainders, small_divisions).
    """
    corrections = []
    for c in OFFSETS[state]:
        t = residual+c*c if state == "D" else residual-c*c
        # b and every factor of odd N are odd. This is exact parity rejection.
        if t > 1 and t & 1:
            corrections.append((c, t))
    big_divisions = short_remainders = small_divisions = 0
    for b in ((1,) if unit_only else COEFFICIENTS):
        for c, t in corrections:
            if b == 1:
                h = t
            else:
                h, rem = divmod(t, b)
                small_divisions += 1
                if rem:
                    continue
            if not 1 < h < n:
                continue
            if endpoint is not None:
                residue, offset = endpoint % h, c % h
                short_remainders += 1
                if residue != offset and residue+offset != h:
                    continue
            big_divisions += 1
            q, rem = divmod(n, h)
            if rem == 0:
                assert h*q == n and 1 < h < n and q > 1
                return h, q, c, b, big_divisions, short_remainders, small_divisions
    return 1, n, None, None, big_divisions, short_remainders, small_divisions


def _complete(n, gated=False, unit_only=False):
    j, r, a, state = state_of(n)
    residual = r if state == "D" else a
    endpoint = (j if state == "D" else j+1) if gated else None
    return _fixed_probe(n, state, residual, endpoint, unit_only)


def prescribed_cases():
    cases = []
    for state in ("D", "U"):
        for b in COEFFICIENTS:
            ratio = b+1
            for c in OFFSETS[state]:
                for exponent in EXPONENTS:
                    p = 127 if exponent is None else (1 << exponent)-19
                    q = ratio*ratio*p + 2*ratio*c + (b if state == "D" else -b)
                    cases.append({"id": f"{state}_b{b}_c{c}_e{exponent}",
                        "state": state, "b": b, "c": c, "ratio": ratio,
                        "exponent": exponent, "p": p, "q": q,
                        "small_prime_pair": False})
    # Four explicitly prescribed educational examples; no prime search.
    for state, b, c, p in (("D", 1, 2, 11), ("U", 1, 2, 13),
                            ("D", 3, 1, 17), ("U", 3, 2, 19)):
        ratio = b+1
        q = ratio*ratio*p + 2*ratio*c + (b if state == "D" else -b)
        cases.append({"id": f"small_prime_{state}_b{b}", "state": state,
            "b": b, "c": c, "ratio": ratio, "exponent": None,
            "p": p, "q": q, "small_prime_pair": True})
    assert len(cases) == 124
    return cases


def summarize_result(result):
    h, q, c, b, big, short, small = result
    return {"factor": visible_int(h), "cofactor": visible_int(q), "c": c, "b": b,
            "hit": h > 1, "N_divisions": big, "endpoint_remainders": short,
            "small_coefficient_divisions": small}


def timed_four(n, j, r, a, state, expected, case_index):
    residual = r if state == "D" else a
    endpoint = j if state == "D" else j+1
    calls = {
        "complete_residual": lambda: _complete(n),
        "complete_root_gate": lambda: _complete(n, gated=True),
        "prepared_residual": lambda: _fixed_probe(n, state, residual),
        "prepared_root_gate": lambda: _fixed_probe(n, state, residual, endpoint),
    }
    names = tuple(calls)
    for name, call in calls.items():
        assert call() == expected[name]
    raw = {name: [] for name in names}
    for round_index in range(ROUNDS):
        start = (case_index+round_index) % len(names)
        order = names[start:] + names[:start]
        for name in order:
            call = calls[name]
            begun = perf_counter_ns()
            for _ in range(REPEATS):
                result = call()
            elapsed = perf_counter_ns()-begun
            assert result == expected[name]
            raw[name].append(elapsed)
    return {"raw_batch_ns": raw,
            "median_ns_per_call": {k: statistics.median(v)/REPEATS for k, v in raw.items()},
            "root_gate_faster_rounds": sum(x < y for x,y in zip(
                raw["complete_root_gate"], raw["complete_residual"]))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enterprise-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    source_dir = Path(__file__).resolve().parent
    checked_bytes(args.enterprise_root/"src/enterprise_math/core.py", CORE_BLOB)
    checked_bytes(source_dir/"brc_kernel13_state_pairs_20260908.py", PRIME_HELPER_BLOB)
    checked_bytes(source_dir/"BRC_ROOT_ENDPOINT_GCD_AUDIT_20260908.md", PRIOR_NOTE_BLOB)
    ast.parse(Path(__file__).read_text(encoding="utf-8"))
    sys.path.insert(0, str(args.enterprise_root/"src"))
    from enterprise_math.core import integer_nth_root
    from math import gcd
    global ROOT
    ROOT = integer_nth_root
    spec = importlib.util.spec_from_file_location("bounded_prime_source",
        source_dir/"brc_kernel13_state_pairs_20260908.py")
    prime_source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prime_source)

    records = []
    counts = Counter()
    begun = perf_counter_ns()
    for case_index, case in enumerate(prescribed_cases()):
        p, q, b, c, ratio = (case[k] for k in ("p", "q", "b", "c", "ratio"))
        n = p*q
        assert p > c*c and p & 1 and q & 1 and q > 1
        j, r, a, state = state_of(n)
        assert state == case["state"]
        if state == "D":
            assert j == ratio*p+c and r == b*p-c*c
            assert n == (j-c)*(j+c)+(r+c*c)
            corrected, endpoint = r+c*c, j
            residual = r
        else:
            assert j+1 == ratio*p+c and a == b*p+c*c
            assert n == (j+1-c)*(j+1+c)-(a-c*c)
            corrected, endpoint = a-c*c, j+1
            residual = a
        assert corrected == b*p and corrected % b == 0
        assert endpoint % p == c % p and 1 < p < n and n//p == q
        if case["small_prime_pair"]:
            assert prime_source.small_prime(p) and prime_source.small_prime(q)
        unit = _complete(n, unit_only=True)
        complete = _complete(n)
        gated = _complete(n, gated=True)
        prepared = _fixed_probe(n, state, residual)
        prepared_gated = _fixed_probe(n, state, residual, endpoint)
        assert complete == prepared and gated == prepared_gated
        assert complete[0] > 1 and gated[0] > 1
        if b == 1:
            assert unit[0] > 1
        for output in (unit, complete, gated):
            if output[0] > 1:
                assert output[0]*output[1] == n
            assert output[4] <= 8 and output[5] <= 8 and output[6] <= 6
        expected = {"complete_residual": complete, "prepared_residual": prepared,
                    "complete_root_gate": gated, "prepared_root_gate": prepared_gated}
        times = timed_four(n, j, r, a, state, expected, case_index)
        prior_center = gcd(n, abs(j-r))
        record = {"id": case["id"], "state": state, "b": b, "c": c,
            "ratio": ratio, "p_recipe": ("explicit small prime" if case["small_prime_pair"]
                else "127" if case["exponent"] is None else f"2**{case['exponent']}-19"),
            "p": visible_int(p), "q": visible_int(q), "N": visible_int(n),
            "J": visible_int(j), "R": visible_int(r), "A": visible_int(a),
            "verified_prime_pair": case["small_prime_pair"],
            "assigned_identity_and_factor_pass": True,
            "unit_probe": summarize_result(unit), "residual_probe": summarize_result(complete),
            "root_gate_probe": summarize_result(gated),
            "prior_center_gcd": visible_int(prior_center), "timing": times}
        records.append(record)
        counts[state] += 1
        counts["unit_hits"] += unit[0] > 1
        counts["quotient_hits"] += complete[0] > 1
        counts["root_gate_hits"] += gated[0] > 1
        counts["same_returned_factor"] += complete[0] == gated[0]
        counts["quotient_added_positive_cases"] += unit[0] == 1 and complete[0] > 1
        counts["positive_cases_beyond_prior_center"] += prior_center == 1
        counts["verified_small_prime_pairs"] += case["small_prime_pair"]
    elapsed = perf_counter_ns()-begun
    groups = defaultdict(list)
    for record in records:
        groups[(record["state"], record["p"]["bits"])].append(record)
    summary = []
    for (state, p_bits), rows in sorted(groups.items()):
        summary.append({"state": state, "p_bits": p_bits, "cases": len(rows),
            "N_bit_range": [min(x["N"]["bits"] for x in rows), max(x["N"]["bits"] for x in rows)],
            "complete_residual_us_range": [min(x["timing"]["median_ns_per_call"]["complete_residual"] for x in rows)/1000,
                                            max(x["timing"]["median_ns_per_call"]["complete_residual"] for x in rows)/1000],
            "complete_root_gate_us_range": [min(x["timing"]["median_ns_per_call"]["complete_root_gate"] for x in rows)/1000,
                                             max(x["timing"]["median_ns_per_call"]["complete_root_gate"] for x in rows)/1000]})
    result = {"schema": "BRC_FIXED_SYNTHETIC_RESIDUAL_CANDIDATE_FAMILIES_V1",
        "canonical_sha": CANONICAL, "project_parent": PARENT,
        "source_blobs": {"core.py": CORE_BLOB, "bounded_prime_helper": PRIME_HELPER_BLOB,
                         "prior_root_note": PRIOR_NOTE_BLOB},
        "scope": {"inputs": "124 prescribed constructed composites; no input search",
            "public_inputs_queried": 0, "public_multiplier_positions_added": 0,
            "baseline_public_positions_unchanged": 312,
            "D_offsets": list(OFFSETS["D"]), "U_offsets": list(OFFSETS["U"]),
            "coefficients": list(COEFFICIENTS), "candidate_pairs_per_state": 12,
            "parity_admissible_candidates_max": 8, "adaptive_extension": False,
            "factor_primality": "only four prescribed small pairs checked; no large prime claim",
            "coverage": "positive-family audit, not a population hit-rate estimate"},
        "cost_contract": {"rounds": ROUNDS, "repeats_per_batch": REPEATS,
            "order": "rotate four variants by (case_index+round_index)%4",
            "complete": "N only; exact native root, both residuals and D/U classification, fixed candidate construction, gates, divmod and product verification",
            "prepared_residual": "N, state and selected R or A already supplied; no root read",
            "prepared_root_gate": "prepared selected residual and selected endpoint supplied",
            "full_domain_and_source_checks": "outside timers",
            "warmups_imports_serialization": "outside timers",
            "in_query_domain_checks": "native root validation, exact 0<R<=2J assertion, candidate bounds and parity",
            "timing_note": "same-process replay costs on prescribed positives; root gate is a sufficient subset of direct divisibility for general composite candidates"},
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "counts": dict(counts), "cohort_check_and_benchmark_ns": elapsed,
        "timing_groups": summary, "records": records}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir/"brc_residual_candidate_families_20260908.json"
    output.write_text(encode_packet(result), encoding="utf-8")
    print(json.dumps({"output": str(output), "counts": dict(counts), "groups": summary,
        "small_examples": [{k: x[k] for k in ("id", "N", "J", "R", "A", "residual_probe", "prior_center_gcd")}
            for x in records if x["verified_prime_pair"]],
        "wall_ns": elapsed}, ensure_ascii=True))


if __name__ == "__main__":
    main()
