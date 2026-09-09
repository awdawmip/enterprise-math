"""Fixed small-number audit of equal-bit prime-product geometry.

All input factors come from an exhaustive sieve below 4096. This is an observer
and identity audit, not an arbitrary-modulus factorization program. Neither
observer returns factors or searches midpoint candidates. No input CLI exists.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import platform
import statistics
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from time import perf_counter_ns

HERE = Path(__file__).resolve().parent
ROOT = HERE / "native-root-checkout"
OUT = HERE / "brc_equal_bit_product_observers_20260909.json"
BITS = (8, 10, 12)
ROUNDS, REPEATS = 7, 2
CANONICAL = "22993e5ce6f9348c48719079b6461815c9fa198b"
PARENT = "c4139b9b1532b756bfa1b950dcf5bc33965569e1"
QUERY_BLOB = "e8ea67310094c517b5a882d5e2e1709be975c675"
CORE_BLOB = "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07"
STATE = None


def checked_blob(path, expected):
    raw = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    found = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if found != expected:
        raise ValueError((str(path), found, expected))


def load_state():
    checked_blob(ROOT / "src/enterprise_math/core.py", CORE_BLOB)
    source = HERE / "brc_residual_candidate_families_20260908.py"
    checked_blob(source, QUERY_BLOB)
    sys.path.insert(0, str(ROOT / "src"))
    from enterprise_math.core import integer_nth_root
    spec = importlib.util.spec_from_file_location("fixed_brc_state_source", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = integer_nth_root
    return module.state_of


def small_primes():
    mark = bytearray(b"\1") * 4096
    mark[0:2] = b"\0\0"
    for p in range(2, math.isqrt(4095) + 1):
        if mark[p]:
            start = p*p
            mark[start:4096:p] = b"\0" * (((4095-start)//p)+1)
    return tuple(p for p in range(2, 4096) if mark[p])


def toy_observer(n, parity_gate):
    if type(n) is not int or n <= 1 or n >= 1 << 24 or not n & 1:
        raise ValueError("observer is restricted to prescribed small odd products")
    j, r, a, state = STATE(n)
    h = j + 1
    if parity_gate and (h & 1) != (1 if n % 4 == 1 else 0):
        return state, False
    v = math.isqrt(a)
    return state, v*v == a


def audit(bits, primes):
    chosen = [p for p in primes if p.bit_length() == bits]
    rows, digest = [], hashlib.sha256()
    states, zero, parity_pass, product_bits = Counter(), Counter(), Counter(), Counter()
    by_gap = defaultdict(list)
    by_layer = defaultdict(list)
    for p, q in combinations(chosen, 2):
        n, u, v = p*q, (p+q)//2, (q-p)//2
        j, r, a, state = STATE(n)
        h, d = j+1, u-j-1
        row = dict(p=p, q=q, N=n, u=u, v=v, H=h, A=a, d=d, state=state)
        assert n == u*u-v*v and d >= 0 and 3*v < u
        assert v*v == a + 2*h*d + d*d
        assert a == v*v - 2*u*d + d*d
        assert (u & 1) == (1 if n % 4 == 1 else 0)
        assert (d & 1) == ((u & 1) ^ (h & 1))
        assert state == ("D" if a >= h else "U")
        assert (d == 0) == (v*v < 2*u-1)
        assert 2*u*d-d*d < v*v < 2*u*(d+1)-(d+1)*(d+1)
        assert (state, d == 0) == toy_observer(n, False) == toy_observer(n, True)
        rows.append(row)
        by_gap[v].append(row)
        by_layer[(v, d)].append(row)
        states[state] += 1
        zero[state] += d == 0
        parity_pass[state] += (h & 1) == (u & 1)
        product_bits[n.bit_length()] += 1
        digest.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    gap_links = linear_links = down_to_up = 0
    for seq in by_gap.values():
        seq.sort(key=lambda row: row["u"])
        for left, right in zip(seq, seq[1:]):
            assert right["d"] <= left["d"]
            gap_links += 1
    for seq in by_layer.values():
        seq.sort(key=lambda row: row["u"])
        for left, right in zip(seq, seq[1:]):
            du = right["u"]-left["u"]
            assert right["H"] == left["H"]+du
            assert right["A"] == left["A"]-2*left["d"]*du
            assert right["A"]-right["H"] == left["A"]-left["H"]-(2*left["d"]+1)*du
            assert not (left["state"] == "U" and right["state"] == "D")
            linear_links += 1
            down_to_up += left["state"] == "D" and right["state"] == "U"
    report = dict(factor_bits=bits, primes=chosen, pair_count=len(rows),
        product_bit_counts=dict(sorted(product_bits.items())), states=dict(states),
        d_zero_by_state=dict(zero), parity_pass_by_state=dict(parity_pass),
        d_histogram=dict(sorted(Counter(row["d"] for row in rows).items())),
        d_median=statistics.median(row["d"] for row in rows),
        d_max=max(row["d"] for row in rows),
        gap_monotonicity_links=gap_links, fixed_gap_layer_linear_links=linear_links,
        fixed_gap_layer_down_to_up_links=down_to_up,
        all_derived_identities_pass=True, canonical_rows_sha256=digest.hexdigest())
    return rows, report


def time_observers(rows):
    ns = tuple(row["N"] for row in rows)
    expected = tuple((row["state"], row["d"] == 0) for row in rows)
    raw = {"direct_square": [], "parity_then_square": []}
    for round_index in range(ROUNDS):
        order = (("direct_square", False), ("parity_then_square", True))
        if round_index & 1:
            order = order[::-1]
        for name, gate in order:
            started = perf_counter_ns()
            for _ in range(REPEATS):
                output = tuple(toy_observer(n, gate) for n in ns)
            raw[name].append(perf_counter_ns()-started)
            assert output == expected
    return dict(raw_batch_ns=raw, pairs_per_batch=len(ns), repeats=REPEATS,
        median_ns_per_observation={name: statistics.median(values)/(len(ns)*REPEATS)
                                  for name, values in raw.items()},
        second_square_root_calls_per_pass={"direct_square": len(ns),
            "parity_then_square": sum(((row["H"] & 1) == (row["u"] & 1)) for row in rows)},
        parity_faster_rounds=sum(a > b for a, b in zip(raw["direct_square"], raw["parity_then_square"])))


def main():
    global STATE
    if OUT.exists():
        raise RuntimeError("preserve the recorded audit and timing; output already exists")
    STATE = load_state()
    primes = small_primes()
    reports, all_rows = [], []
    for bits in BITS:
        rows, report = audit(bits, primes)
        report["observer_timing"] = time_observers(rows)
        reports.append(report)
        all_rows.extend(rows)
    examples = {(131, 137), (131, 157), (131, 173), (131, 179), (131, 181), (131, 251)}
    result = dict(schema="BRC_EQUAL_BIT_PRODUCT_OBSERVERS_V1", canonical_sha=CANONICAL,
        project_parent=PARENT, activity_id="RA-EM-HME-0CE4FD-SEMIPRIME-20260909",
        source_blobs={"state_source": QUERY_BLOB, "core": CORE_BLOB},
        environment={"python": platform.python_version(), "platform": platform.platform()},
        scope={"factor_bits": list(BITS), "prime_sieve_exclusive_bound": 4096,
            "population": "all unordered distinct equal-bit prime pairs at each prescribed bit size",
            "RSA_key_generation_filters_applied": False,
            "known_factor_labels": "u, v and d are audit labels; observers receive N alone",
            "observer_output": "D/U state and first-completion-gap-is-square Boolean; no factors",
            "general_factor_search": False, "external_inputs": 0},
        cost_contract={"paired_rounds": ROUNDS, "repeats_per_batch": REPEATS,
            "included": ["toy-size guard", "unchanged native root/state preparation", "square-status observer", "output tuple allocation"],
            "excluded": ["prime sieve", "input construction", "factor-label arithmetic", "identity audit", "imports", "source checks", "output serialization"],
            "interpretation": "small-number observer costs; not factorization speed or large-key probability"},
        cohorts=reports, examples=[row for row in all_rows if (row["p"], row["q"]) in examples])
    OUT.write_bytes((json.dumps(result, indent=2, ensure_ascii=True)+"\n").encode())
    print(json.dumps({"output": str(OUT), "cohorts": [{k: v for k, v in r.items()
        if k not in ("primes", "d_histogram")} for r in reports], "examples": result["examples"]}, ensure_ascii=True))


if __name__ == "__main__":
    main()
