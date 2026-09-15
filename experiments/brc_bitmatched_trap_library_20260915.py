"""Fixed prime libraries for two explicitly published integer challenges.

Generation precedes challenge observations. No arbitrary modulus, expanding
multiplier range, adaptive library growth, or general factor-search CLI exists.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import perf_counter_ns

HERE = Path(__file__).resolve().parent
ROOT = HERE / "native-root-checkout"
RUN = HERE / "bitmatched-trap-library-20260915"
OLD_RUN = HERE / "semiprime-20260909"
CANONICAL = "73282863250128a33c0473202f90b2b801e93fc1"
PARENT = "130e01f00da1d55dc707957801b2a6c7a877e6a6"
CAP, BLOCK = 200000, 65536
CONFIG = {
    "RSA-270": {"bits": 448, "close_numerator": 640,
        "ratio_numerators": [513, 583, 653, 723, 793, 863, 933, 1003],
        "N_sha256": "83b66aee65c8ffa8bbae104ad3c3e4f0723f854c105f6f29a831d11898e71432"},
    "RSA-2048": {"bits": 1024, "close_numerator": 896,
        "ratio_numerators": [725, 767, 809, 851, 893, 935, 977, 1019],
        "N_sha256": "b3c2468add10e2a0c4a251d9d2bac4ba04d4b3527156ceead43a1305e03f1fc0"},
}
SOURCE_BLOBS = {
    "core.py": "2b7ab070868ef4a2b6d8b33f5e3bc69dbac62c07",
    "brc_multiplier_basin.py": "4d03ded19b38f5aa13d3e873e911205d35be5c5f",
    "brc_square_gap_prefilter.py": "42d4e9a397b56d9d371f034780ffc736d43e6d96",
}
HELPER_BLOB = "5c8c5f757d4768ad21983035b1caaf7836cc4dea"
WHEEL_SHA = "87d1493dc592b67451ffad48a2cbc85f3cdf3ddcd8ba2abf447c21ee5ef74030"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(path):
    b = path.read_bytes().replace(b"\r\n", b"\n").rstrip(b"\n") + b"\n"
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix+".partial")
    temporary.write_bytes((json.dumps(data, indent=2, ensure_ascii=True)+"\n").encode())
    os.replace(temporary, path)


def paths(label):
    stem = label.lower().replace("-", "")
    return (RUN / f"{stem}_prime_progress.json", RUN / f"{stem}_library.json",
            RUN / f"{stem}_challenge.json")


def source_interfaces():
    for name, expected in SOURCE_BLOBS.items():
        if git_blob(ROOT / "src/enterprise_math" / name) != expected:
            raise ValueError("source mismatch: "+name)
    sys.path.insert(0, str(ROOT / "src"))
    from enterprise_math.brc_multiplier_basin import point_cost_state
    from enterprise_math.brc_square_gap_prefilter import ceiling_completion_square_witness
    return point_cost_state, ceiling_completion_square_witness


def prime_runtime():
    helper = HERE / "brc_proved_semiprime2048_benchmark_20260909.py"
    if git_blob(helper) != HELPER_BLOB:
        raise ValueError("prime sieve helper changed")
    spec = importlib.util.spec_from_file_location("frozen_prime_helper", helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.path.insert(0, str(OLD_RUN / "flint_runtime"))
    import flint
    if flint.__version__ != "0.8.0" or flint.__FLINT_VERSION__ != "3.3.1":
        raise ValueError("unrecorded prime-proof runtime")
    installer = json.loads((OLD_RUN / "pip_install_report.json").read_bytes())
    if installer["install"][0]["download_info"]["archive_info"]["hashes"]["sha256"] != WHEEL_SHA:
        raise ValueError("wheel receipt mismatch")
    return flint.fmpz, module.small_sieve_primes()


def fill(label, group, index, numerator, wanted, cache, save, fmpz, primes):
    bits = CONFIG[label]["bits"]
    tag = f"BRC-BITMATCHED-20260915:{label}:{group}:{index}".encode()
    # Offset size is independent of the published challenge integer.
    offset = int.from_bytes(hashlib.sha256(tag).digest()[:12], "big")
    anchor = (numerator*(1 << bits)//1024 + 2*offset) | 1
    key = f"{group}_{index}"
    rows = cache["seeds"].setdefault(key, [])
    start_index = rows[-1]["odd_index"]+1 if rows else 0
    if len(rows) == wanted:
        return rows
    for first in range(start_index, CAP, BLOCK):
        count = min(BLOCK, CAP-first)
        p0 = anchor+2*first
        live = bytearray(b"\1")*count
        for ell in primes:
            at = (-p0*pow(2, -1, ell)) % ell
            if at < count:
                live[at::ell] = b"\0"*((count-1-at)//ell+1)
        for i, good in enumerate(live):
            if not good:
                continue
            p = p0+2*i
            if math.gcd(p-1, 65537) != 1 or not fmpz(p).is_probable_prime():
                continue
            ident = f"{group}_{len(rows) if group == 'close' else index:02d}"
            print(json.dumps({"event": "prove", "target_model": label,
                "id": ident, "bits": bits}), flush=True)
            begun = perf_counter_ns()
            proved = int(fmpz(p).is_prime())
            elapsed = perf_counter_ns()-begun
            if proved != 1:
                continue
            assert p.bit_length() == bits
            rows.append(dict(id=ident, pool=group, value=str(p), bits=bits,
                seed_numerator=numerator, seed_denominator=1024,
                anchor=str(anchor), odd_index=first+i, is_prime=proved,
                prime_proof_ns=elapsed, exponent_65537_compatible=True))
            save()
            print(json.dumps({"event": "proved", "target_model": label,
                "id": ident, "proof_seconds": elapsed/1e9,
                "proved_total": sum(len(v) for v in cache["seeds"].values())}), flush=True)
            if len(rows) == wanted:
                return rows
    raise RuntimeError("fixed prime-construction budget exhausted: "+key)


def generate(label):
    progress, output, _ = paths(label)
    script_blob = git_blob(Path(__file__))
    if output.exists():
        data = json.loads(output.read_bytes())
        assert data["script_blob"] == script_blob
        print(json.dumps({"cached_library": str(output), "members": len(data["members"])}))
        return
    started = perf_counter_ns()
    fmpz, primes = prime_runtime()
    point, witness = source_interfaces()
    if progress.exists():
        cache = json.loads(progress.read_bytes())
        assert cache["script_blob"] == script_blob and cache["target_model"] == label
    else:
        cache = dict(schema="BRC_TRAPLIB_PRIME_PROGRESS_V1", script_blob=script_blob,
            target_model=label, seeds={})
    save = lambda: write(progress, cache)
    cfg = CONFIG[label]
    close = fill(label, "close", 0, cfg["close_numerator"], 8, cache, save, fmpz, primes)
    ratio = []
    for i, numerator in enumerate(cfg["ratio_numerators"]):
        ratio.extend(fill(label, "ratio", i, numerator, 1, cache, save, fmpz, primes))
    pools = {"close": close, "ratio": ratio}
    all_primes = close+ratio
    assert len(all_primes) == 16 and len({r["value"] for r in all_primes}) == 16
    members = []
    validation_started = perf_counter_ns()
    for pool, rows in pools.items():
        for i, (left, right) in enumerate(combinations(rows, 2)):
            p, q = sorted((int(left["value"]), int(right["value"])))
            m = p*q
            state = point(m, 1)
            found = witness(m, 1)
            expected_close = pool == "close"
            assert (found is not None) == expected_close
            if found:
                assert found == ((p+q)//2, (q-p)//2)
            assert p.bit_length() == q.bit_length() == cfg["bits"]
            if label == "RSA-2048":
                assert m.bit_length() == 2048 and 2*p*p >= (1 << 2048)
            else:
                assert len(str(m)) == 270 and m.bit_length() in (895, 896)
            members.append(dict(id=("C" if pool == "close" else "R")+f"{i:02d}",
                pool=pool, prime_ids=[left["id"], right["id"]], M=str(m),
                factor_bits=[cfg["bits"], cfg["bits"]], M_bits=m.bit_length(),
                M_decimal_digits=len(str(m)), self_square_closure=found is not None,
                self_direction="D" if state.subtraction_cost < state.addition_cost else "U",
                self_gap_bits=state.addition_cost.bit_length(),
                self_gap_sha256=sha(str(state.addition_cost).encode()),
                self_witness=[str(v) for v in found] if found else None,
                relative_factor_gap=str(q-p),
                exceeds_RSA_style_min_separation=(q-p) > (1 << max(0, cfg["bits"]-100))))
    validation_ns = perf_counter_ns()-validation_started
    assert len(members) == 56 and len({r["M"] for r in members}) == 56
    result = dict(schema="BRC_BITMATCHED_TRAP_LIBRARY_V1", target_model=label,
        canonical_sha=CANONICAL, project_parent=PARENT, script_blob=script_blob,
        activity_id="RA-EM-HME-0CE4FD-SEMIPRIME-20260909", config=cfg,
        source_blobs=SOURCE_BLOBS, helper_blob=HELPER_BLOB,
        proof_runtime={"python": platform.python_version(), "python_flint": "0.8.0",
            "FLINT": "3.3.1", "wheel_sha256": WHEEL_SHA,
            "method": "fmpz.is_prime -> fmpz_is_prime(proved=1)",
            "standalone_certificate_exported": False},
        construction={"max_odd_candidates_per_seed": CAP, "block": BLOCK,
            "prime_pool_sizes": [8, 8], "target_N_used_for_construction": False,
            "generation_wall_ns": perf_counter_ns()-started,
            "accepted_prime_proof_ns": sum(r["prime_proof_ns"] for r in all_primes),
            "self_validation_ns": validation_ns},
        interpretation={"close_pool": "28 intrinsic first-completion traps, all clustered factors",
            "ratio_pool": "28 known-factor products with spread factor ratios; not self-closing traps",
            "actual_target_factor_bit_lengths_verified": False,
            "library_entries_are_independent_factor_guesses": False},
        primes=all_primes, members=members)
    write(output, result)
    print(json.dumps({"generation_complete": label, "library": str(output),
        "proved_primes": 16, "members": 56,
        "member_bits": dict(Counter(r["M_bits"] for r in members)),
        "self_closures": sum(r["self_square_closure"] for r in members),
        "generation_seconds": result["construction"]["generation_wall_ns"]/1e9,
        "proof_seconds": result["construction"]["accepted_prime_proof_ns"]/1e9}), flush=True)


def challenge(label):
    _, library_path, output = paths(label)
    if output.exists():
        raise RuntimeError("challenge observations already recorded; no replay")
    library_bytes = library_path.read_bytes()
    lib = json.loads(library_bytes)
    assert lib["script_blob"] == git_blob(Path(__file__)) and lib["target_model"] == label
    assert len(lib["primes"]) == 16 and len(lib["members"]) == 56
    public = json.loads((HERE / "brc_public_rsa_fixed_predicates_20260908.json").read_bytes())
    source = next(r for r in public["records"] if r["label"] == label)
    assert sha(source["N"].encode()) == CONFIG[label]["N_sha256"]
    assert "".join(source["decimal_blocks"]) == source["N"]
    n = int(source["N"])
    point, witness = source_interfaces()
    by_id = {r["id"]: r for r in lib["primes"]}
    pool_results, rows, factors = {}, [], set()
    def admit(g):
        if 1 < g < n:
            q, rem = divmod(n, g)
            assert rem == 0 and g*q == n
            factors.add(g)
            factors.add(q)
    started = perf_counter_ns()
    for pool in ("close", "ratio"):
        begun = perf_counter_ns()
        basis = math.prod(int(r["value"]) for r in lib["primes"] if r["pool"] == pool)
        g = math.gcd(n, basis)
        elapsed = perf_counter_ns()-begun
        pool_results[pool] = dict(gcd=str(g), basis_bits=basis.bit_length(),
            basis_sha256=sha(str(basis).encode()), product_and_gcd_ns=elapsed)
        if g != 1:
            for prime in lib["primes"]:
                if prime["pool"] == pool:
                    admit(math.gcd(n, int(prime["value"])))
    for member in lib["members"]:
        m = int(member["M"])
        began = perf_counter_ns()
        w = witness(n, m)
        call_ns = perf_counter_ns()-began
        audit_started = perf_counter_ns()
        s = point(n, m)
        h = s.target_root + (s.subtraction_cost != 0)
        gap = h*h-m*n
        b = math.isqrt(gap)
        assert (w is not None) == (b*b == gap)
        if w is not None:
            assert w == (h, b)
        gcds = []
        if w is not None:
            gcds = [math.gcd(h-b, n), math.gcd(h+b, n)]
            for g in gcds:
                admit(g)
        direct_g = 1
        if pool_results[member["pool"]]["gcd"] != "1":
            direct_g = math.gcd(n, m)
            admit(direct_g)
            if m == n:
                for ident in member["prime_ids"]:
                    admit(int(by_id[ident]["value"]))
        rows.append(dict(id=member["id"], pool=member["pool"], multiplier_bits=m.bit_length(),
            multiplied_bits=(m*n).bit_length(), H=str(h), A=str(gap),
            direction="Z" if gap == 0 else ("D" if s.subtraction_cost < s.addition_cost else "U"),
            square_closure=w is not None, witness=[str(v) for v in w] if w else None,
            original_gcds=[str(g) for g in gcds], direct_library_gcd=str(direct_g),
            direct_gcd_ruled_out_by_pool=pool_results[member["pool"]]["gcd"] == "1",
            witness_call_ns=call_ns, annotation_and_audit_ns=perf_counter_ns()-audit_started))
    result = dict(schema="BRC_BITMATCHED_PUBLIC_CHALLENGE_V1", target=label,
        canonical_sha=CANONICAL, project_parent=PARENT,
        activity_id="RA-EM-HME-0CE4FD-SEMIPRIME-20260909",
        script_blob=git_blob(Path(__file__)), library_sha256=sha(library_bytes),
        source_blobs=SOURCE_BLOBS,
        target_source={"N": source["N"], "decimal_sha256": CONFIG[label]["N_sha256"],
            "bits": n.bit_length(), "decimal_digits": len(source["N"]),
            "source_pdf": source["source_pdf"], "source_page": 3,
            "source_compared_with_saved_decimal_on": "2026-09-15"},
        budget={"library_members": 56, "unique_library_primes": 16,
            "direct_pool_gcd_calls": 2, "witness_calls": len(rows),
            "multiplier_35_calls": 0, "adaptive_extension": False, "target_factor_search": False},
        pool_gcds=pool_results, rows=rows,
        nontrivial_target_factor_candidates=[str(g) for g in sorted(factors)],
        costs={"check_loop_wall_ns": perf_counter_ns()-started,
            "witness_calls_ns": sum(r["witness_call_ns"] for r in rows),
            "annotation_and_audit_ns": sum(r["annotation_and_audit_ns"] for r in rows),
            "pool_product_and_gcd_ns": sum(r["product_and_gcd_ns"] for r in pool_results.values()),
            "scope": "one fixed pass; generation, imports, parsing and final JSON output excluded; no timing replays"},
        all_exact_checks_pass=True)
    write(output, result)
    print(json.dumps({"challenge_complete": label, "pool_gcds": pool_results,
        "self_closing_multiplier_count": sum(r["self_square_closure"] for r in lib["members"]),
        "target_square_closures": sum(r["square_closure"] for r in rows),
        "target_factors": result["nontrivial_target_factor_candidates"],
        "directions": {pool: dict(Counter(r["direction"] for r in rows if r["pool"] == pool))
                       for pool in ("close", "ratio")},
        "costs": result["costs"], "output": str(output)}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=tuple(CONFIG), required=True)
    parser.add_argument("--stage", choices=("generate", "challenge"), required=True)
    args = parser.parse_args()
    (generate if args.stage == "generate" else challenge)(args.target)
