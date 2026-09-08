#!/usr/bin/env python3
"""PFSSV gen2 Stage 1: exact substrate, not a scientific residual verdict.

Reuses the historical task sieve algorithm through the existing BRC facade.
The only command runs the newly frozen bounded resource probe. Full-scale
statistics, new blind tests and terminal research labels are not implemented.
"""
from __future__ import annotations

import argparse
from array import array
from bisect import bisect_left, bisect_right
from collections import Counter
from dataclasses import asdict, is_dataclass
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time
import tracemalloc

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO.joinpath("src")))
from enterprise_math import exact_arithmetic as native
from enterprise_math import brc_logarithm as native_log

BINS = 24
MAX_Q = 50_500_000
MAX_UPPER = 101_000_000
SCALES = (10**6, 10**10, 10**14)
MEMORY_CAP = 2 * 1024**3
TRACE_CAP = 512 * 1024**2
ARTIFACT = "research_artifacts/PFSSV_REVISION_20260908"


class ResourceBoundary(RuntimeError):
    """An engineering bound; never a mathematical negative conclusion."""


class PrecisionUnresolved(RuntimeError):
    """The allowed precision did not separate the requested bin."""


def _natural(value: int, name: str, minimum: int = 0) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def _encoded(value):
    if is_dataclass(value):
        return _encoded(asdict(value))
    if isinstance(value, int) and value.bit_length() > 4096:
        return {"integer_hex": hex(value)}
    if isinstance(value, dict):
        return {str(k): _encoded(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_encoded(x) for x in value]
    return value


def _json_bytes(value) -> bytes:
    return (json.dumps(_encoded(value), sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def peak_memory_bytes() -> int:
    """Process peak working set on Windows, tracemalloc fallback elsewhere."""
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes

        class Counters(ctypes.Structure):
            _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
                (name, ctypes.c_size_t) for name in (
                    "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
                    "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage",
                    "QuotaNonPagedPoolUsage", "PagefileUsage", "PeakPagefileUsage")]

        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
        data = Counters()
        data.cb = ctypes.sizeof(data)
        if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(data), data.cb):
            raise OSError(ctypes.get_last_error(), "GetProcessMemoryInfo")
        return data.PeakWorkingSetSize
    return tracemalloc.get_traced_memory()[1]


class NativeTraceCapture:
    """Capture actual original native code-object returns, including nested calls."""
    def __init__(self, path: Path, *, deadline_ns: int | None = None, byte_limit: int = TRACE_CAP):
        self.path = path
        self.deadline_ns = deadline_ns
        self.byte_limit = byte_limit
        self.calls = Counter()
        self.returns = Counter()
        self.seen = Counter()
        self.bytes = 0
        self.codes = {
            native.brc_evaluate_division.__code__: "brc_evaluate_division",
            native.brc_evaluate_root.__code__: "brc_evaluate_root",
            native_log.brc_evaluate_ln.__code__: "brc_evaluate_ln",
            native_log.brc_evaluate_log.__code__: "brc_evaluate_log",
        }

    def __enter__(self):
        self.stream = self.path.open("xb")
        self.previous_profile = sys.getprofile()
        if self.previous_profile is not None:
            self.stream.close()
            raise RuntimeError("refuse to replace an existing profiler")
        sys.setprofile(self._profile)
        return self

    def _profile(self, frame, event, value):
        name = self.codes.get(frame.f_code)
        if name is None:
            return
        if self.deadline_ns is not None and time.monotonic_ns() >= self.deadline_ns:
            raise ResourceBoundary("probe deadline reached")
        if event == "call":
            self.calls[name] += 1
        elif event == "return" and is_dataclass(value):
            self.returns[name] += 1
            body = {"function": name, "trace": _encoded(value)}
            digest = hashlib.sha256(_json_bytes(body)).hexdigest()
            record = {"trace_ref": digest} if digest in self.seen else {"trace_id": digest, **body}
            payload = _json_bytes(record)
            if self.bytes + len(payload) > self.byte_limit:
                raise ResourceBoundary("trace byte cap reached")
            self.stream.write(payload)
            self.bytes += len(payload)
            self.seen[digest] += 1

    def __exit__(self, *exc):
        sys.setprofile(self.previous_profile)
        self.stream.close()

    def receipt(self):
        return {
            "native_code_object_calls": dict(self.calls),
            "native_code_object_trace_returns": dict(self.returns),
            "distinct_traces": len(self.seen), "all_trace_events": sum(self.seen.values()),
            "trace_bytes": self.bytes,
            "trace_sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
            "function_identity": [
                {"name": name, "file": str(Path(code.co_filename).resolve()),
                 "line": code.co_firstlineno,
                 "file_sha256": hashlib.sha256(Path(code.co_filename).read_bytes()).hexdigest()}
                for code, name in self.codes.items()],
            "deduplication": "Every actual returned trace has one definition or an exact trace_ref event; repeated calls are counted. Large integers use reversible integer_hex encoding.",
        }


def _divide(numerator: int, denominator: int):
    return native.brc_evaluate_division(native.division(numerator, denominator))


def _root(radicand: int):
    return native.brc_evaluate_root(native.root(radicand, 2))


class PrimePrefix:
    """Complete bounded prime prefix, using the original additive sieve design."""
    def __init__(self, limit: int):
        _natural(limit, "limit")
        if limit > MAX_Q:
            raise ResourceBoundary("prime prefix exceeds frozen max_q")
        self.limit = limit
        self.flags = bytearray(b"\x01") * (limit + 1)
        self.flags[0] = 0
        if limit >= 1:
            self.flags[1] = 0
        for p in range(2, _root(limit).root_index + 1):
            if self.flags[p]:
                count = _divide(limit - p * p, p).quotient + 1
                self.flags[p * p::p] = bytes(count)
        self.primes = array("I", (i for i, marked in enumerate(self.flags) if marked))
        if self.primes.itemsize != 4 or limit >= 2**32:
            raise ResourceBoundary("uint32 address bound not satisfied")
        self._residues = {}

    def rank(self, value: int) -> int:
        _natural(value, "rank input")
        if value > self.limit:
            raise ValueError("rank input outside complete prime prefix")
        return bisect_right(self.primes, value)

    def rank_interval(self, lo: int, hi: int) -> tuple[int, int]:
        _natural(lo, "lo")
        _natural(hi, "hi")
        if lo > hi or hi > self.limit:
            raise ValueError("invalid prime interval")
        return bisect_left(self.primes, lo) + 1, bisect_right(self.primes, hi)

    def residue_count(self, lo: int, hi: int, residue: int) -> int:
        if residue not in range(30):
            raise ValueError("invalid mod-30 residue")
        if residue not in self._residues:
            # Additive arithmetic progressions label residues without materializing q % 30.
            self._residues[residue] = array("I", (
                q for q in range(residue, self.limit + 1, 30) if self.flags[q]))
        seq = self._residues[residue]
        return bisect_right(seq, hi) - bisect_left(seq, lo)


def bounded_trial_prime(n: int) -> bool:
    """Independent exact small-sample path; no claim of generic 64-bit MR."""
    _natural(n, "primality input")
    if n > MAX_Q:
        raise ResourceBoundary("independent primality exceeds frozen input domain")
    if n < 2:
        return False
    for divisor in range(2, _root(n).root_index + 1):
        if _divide(n, divisor).remainder == 0:
            return False
    return True


def _ceil(n: int, d: int) -> int:
    trace = _divide(n, d)
    return trace.quotient + (1 if trace.remainder else 0)


def rank_edges(cap: int) -> list[int]:
    _natural(cap, "rank cap")
    return [_ceil(b * cap, BINS) for b in range(BINS + 1)]


def _rank_bin(index: int, cap: int) -> int:
    if not 1 <= index <= cap:
        raise ValueError("prime rank is outside its geometric cap")
    return _divide((index - 1) * BINS, cap).quotient


def _scaled_log(argument_n: int, argument_d: int, base: int, scale: int) -> tuple[int, int]:
    trace = native_log.brc_evaluate_log(
        native_log.logarithm(native.division(argument_n, argument_d), native.division(base, 1)), scale)
    if trace.sign < 0:
        raise ValueError("unexpected negative log interval on this declared coordinate")
    lower = trace.magnitude_index
    return lower, lower if trace.exact_boundary else lower + 1


class CoordinateBins:
    """Task-local certified log bins; ambiguity stops instead of choosing a float."""
    def __init__(self):
        self.cache = {}
        self.log_cache = {}

    def _log(self, p: int, X: int, scale: int):
        key = (p, X, scale)
        if key not in self.log_cache:
            self.log_cache[key] = _scaled_log(p, 1, X, scale)
        return self.log_cache[key]

    def bins(self, p: int, X: int) -> dict:
        key = (p, X)
        if key in self.cache:
            return self.cache[key]
        result = {"raw": None, "small_trim": None, "scale_trim": None, "density_flat": None,
                  "coarse_band": None, "overflow_u_gt_half": p * p > X}
        if p * p > X:
            self.cache[key] = result
            return result
        if p * p == X:
            result["raw"] = BINS - 1
            if p > 31:
                result["small_trim"] = BINS - 1
            if p**4 > X:
                result["scale_trim"] = BINS - 1
                result["density_flat"] = BINS - 1
                result["coarse_band"] = 7
            result["boundary"] = "EXACT_RIGHT_ENDPOINT"
            self.cache[key] = result
            return result
        for scale in SCALES:
            lo, hi = self._log(p, X, scale)
            candidates = dict(result)
            separated = True
            for name, anchor in (("raw", 2), ("small_trim", 31)):
                if p < anchor or (name == "small_trim" and p == anchor):
                    continue
                if p == anchor:
                    candidates[name] = 0
                    continue
                a_lo, a_hi = self._log(anchor, X, scale)
                if 2 * a_hi >= scale:
                    separated = False
                    continue
                low = _divide(2 * BINS * max(0, lo - a_hi), scale - 2 * a_lo).quotient
                high = _divide(2 * BINS * (hi - a_lo), scale - 2 * a_hi).quotient
                if low == high and low < BINS:
                    candidates[name] = low
                else:
                    separated = False
            if p**4 > X:
                band_lo = _divide(8 * max(0, 4 * lo - scale), scale).quotient
                band_hi = _divide(8 * (4 * hi - scale), scale).quotient
                if band_lo == band_hi and band_lo < 8:
                    candidates["coarse_band"] = band_lo
                else:
                    separated = False
                low = _divide(BINS * max(0, 4 * lo - scale), scale).quotient
                high = _divide(BINS * (4 * hi - scale), scale).quotient
                if low == high and low < BINS:
                    candidates["scale_trim"] = low
                else:
                    separated = False
                # Known task domain u>1/4 makes the exact lower endpoint 1 valid.
                arg_lo_n = max(3 * lo, scale - lo)
                lz, _ = _scaled_log(arg_lo_n, scale - lo, 3, scale)
                _, uz = _scaled_log(3 * hi, scale - hi, 3, scale)
                low = _divide(BINS * lz, scale).quotient
                high = _divide(BINS * uz, scale).quotient
                if low == high and low < BINS:
                    candidates["density_flat"] = low
                else:
                    separated = False
            if separated:
                candidates["certified_scale"] = scale
                self.cache[key] = candidates
                return candidates
        raise PrecisionUnresolved(f"bin interval unresolved for p={p}, X={X}")


def shell_cell(prefix: PrimePrefix, X: int, num: int, den: int,
               coordinates: CoordinateBins | None = None) -> dict:
    _natural(X, "X", 16)
    _natural(num, "width numerator", 1)
    _natural(den, "width denominator", 1)
    U = _divide(X * (den + num), den).quotient
    if U > MAX_UPPER:
        raise ResourceBoundary("shell upper exceeds frozen workload")
    if prefix.limit < _divide(U, 2).quotient:
        raise ValueError("prime prefix does not cover all possible q")
    stop = _root(U).root_index
    pcap = prefix.rank(stop)
    qcap = prefix.rank(_divide(U, 2).quotient)
    edges = rank_edges(qcap)
    grid = [[0] * BINS for _ in range(BINS)]
    profiles = {name: [0] * BINS for name in ("raw", "small_trim", "scale_trim", "density_flat")}
    coordinate_engine = coordinates if coordinates is not None else CoordinateBins()
    rows, excluded = [], []
    totals = {name: 0 for name in ("raw", "small_trim", "scale_trim", "diagonal", "overflow")}
    for position in range(pcap):
        p = int(prefix.primes[position])
        lo = max(p, _divide(X, p).quotient + 1)
        hi = _divide(U, p).quotient
        if lo > hi:
            excluded.append({"p": p, "qlo": lo, "qhi": hi, "reason": "EMPTY_INTEGER_WINDOW"})
            continue
        first, last = prefix.rank_interval(lo, hi)
        count = last - first + 1
        pi_p = position + 1
        residue = _divide(p, 30).remainder
        channels = [prefix.residue_count(lo, hi, r) for r in range(30)]
        if sum(channels) != count:
            raise AssertionError("residue channels do not reconstruct exact count")
        bins = coordinate_engine.bins(p, X)
        pb = _rank_bin(pi_p, pcap)
        for qb in range(BINS):
            overlap = max(0, min(last, edges[qb + 1]) - max(first, edges[qb] + 1) + 1)
            grid[pb][qb] += overlap
        for name, vector in profiles.items():
            if bins[name] is not None:
                vector[bins[name]] += count
        totals["raw"] += count
        totals["small_trim"] += count if p > 31 else 0
        totals["scale_trim"] += count if p**4 > X else 0
        totals["diagonal"] += 1 if X < p * p <= U else 0
        totals["overflow"] += count if p * p > X else 0
        rows.append({"p": p, "pi_p": pi_p, "qlo": lo, "qhi": hi, "count": count,
                     "q_prime_rank_first": first, "q_prime_rank_last": last,
                     "p_mod_30": residue, "q_mod_30_counts": channels, "bins": bins,
                     "small_trim": p > 31, "scale_trim": p**4 > X})
    if sum(map(sum, grid)) != totals["raw"]:
        raise AssertionError("joint prime-rank view lost mass")
    if sum(profiles["raw"]) + totals["overflow"] != totals["raw"]:
        raise AssertionError("raw domain/overflow accounting failed")
    return {"schema": "PFSSV_NATIVE_CELL_V2", "X": X, "num": num, "den": den, "upper": U,
            "totals": totals, "rows": rows, "geometrically_empty_rows": excluded,
            "zero_prime_count_rows": sum(row["count"] == 0 for row in rows),
            "profiles": {**profiles, "prime_rank_joint": grid},
            "prime_rank_caps": {"p": pcap, "q": qcap},
            "prime_rank_q_edges_zero_based": edges,
            "joint_rank_null": {"status": "NOT_DEFINED_BY_ORIGINAL_NULL_FAMILIES", "required_for_stage_1": False},
            "corrected_profiles": None, "signed_residual_profiles": None, "null_profiles": None,
            "scientific_status": "NOT_COMPUTED_STAGE_1",
            "orbit_representation": "Distinct S3 permutations of each (p,q,0), diagnostic, unweighted in primary counts"}


def iter_pairs(prefix: PrimePrefix, cell: dict):
    for row in cell["rows"]:
        start = row["q_prime_rank_first"] - 1
        stop = row["q_prime_rank_last"]
        for index in range(start, stop):
            yield row["p"], int(prefix.primes[index])


def orbit_diagnostic(p: int, q: int) -> tuple:
    return tuple(sorted(set(itertools.permutations((p, q, 0)))))


def null_a_capacity_witness(cell: dict) -> dict:
    """Deterministic reachability audit of the original count-permutation family.

    This does not run or repair a null ensemble. Within a nontrivial stratum,
    every source row may be sent to every target by a permitted permutation.
    A count exceeding the target's integer residue slots cannot be an occupancy
    realization on that target window. No clipping or rejection sampling occurs.
    """
    groups = {}
    for row in cell["rows"]:
        if row["bins"]["coarse_band"] is not None:
            key = (row["bins"]["coarse_band"], row["p_mod_30"])
            groups.setdefault(key, []).append(row)
    for key, rows in sorted(groups.items()):
        if len(rows) < 2:
            continue
        for residue in (1, 7, 11, 13, 17, 19, 23, 29):
            source = max(rows, key=lambda row: row["q_mod_30_counts"][residue])
            assigned = source["q_mod_30_counts"][residue]
            for target in rows:
                rem = _divide(target["qlo"], 30).remainder
                offset = _divide(residue + 30 - rem, 30).remainder
                first = target["qlo"] + offset
                capacity = 0 if first > target["qhi"] else _divide(target["qhi"] - first, 30).quotient + 1
                if assigned > capacity:
                    return {"status": "REACHABLE_INTEGER_RESIDUE_CAPACITY_VIOLATION",
                            "stratum": {"coarse_band": key[0], "p_mod_30": key[1], "q_mod_30": residue},
                            "source_p": source["p"], "source_count": assigned,
                            "target_p": target["p"], "target_qlo": target["qlo"], "target_qhi": target["qhi"],
                            "target_observed_count": target["q_mod_30_counts"][residue],
                            "target_integer_residue_capacity": capacity, "stratum_size": len(rows),
                            "assignment_probability": {"numerator": 1, "denominator": len(rows)},
                            "random_draws": 0, "null_repaired": False,
                            "scope": "Original scalar count surrogate can still be studied as such; this witness prevents calling every draw an exact factor-window occupancy model."}
    return {"status": "NO_WITNESS_IN_THIS_PROBE_CELL", "random_draws": 0,
            "scope": "No validity proof for other cells, finer coupling, or a joint null."}


def serial_cell(cell: dict) -> bytes:
    required = {"totals", "rows", "profiles", "corrected_profiles", "signed_residual_profiles", "null_profiles"}
    if required - cell.keys():
        raise ValueError("required cell payload missing")
    for name in ("raw", "small_trim", "scale_trim", "density_flat"):
        if len(cell["profiles"][name]) != BINS:
            raise ValueError("full one-dimensional profile missing")
    grid = cell["profiles"]["prime_rank_joint"]
    if len(grid) != BINS or any(len(row) != BINS for row in grid):
        raise ValueError("full two-dimensional prime-rank profile missing")
    return _json_bytes(cell)


def verify_sources(artifact_dir: Path) -> dict:
    binding = json.loads(artifact_dir.joinpath("source_binding.json").read_text(encoding="utf-8"))
    for row in binding["preserve_bytes"]:
        actual = hashlib.sha256(REPO.joinpath(row["path"]).read_bytes()).hexdigest()
        if actual != row["sha256"]:
            raise ValueError(f"source pin drift: {row['path']}")
    return binding


def resource_probe() -> int:
    artifact_dir = REPO.joinpath(ARTIFACT)
    binding = verify_sources(artifact_dir)
    manifest = json.loads(artifact_dir.joinpath("correction_manifest.json").read_text(encoding="utf-8"))
    probe = manifest["resource_probe"]
    if probe["full_run_authorized"] or probe["deadline_seconds"] > 60:
        raise ValueError("this entry only executes the bounded Stage 1 probe")
    start = time.monotonic_ns()
    deadline = start + 55 * 10**9
    trace = NativeTraceCapture(artifact_dir.joinpath("native_trace.jsonl"), deadline_ns=deadline)
    receipt = {"schema": "PFSSV_STAGE1_RESOURCE_PROBE_V1", "argv": sys.argv,
               "publication_id": binding["publication_id"], "claim_id": binding["claim_id"],
               "input": probe, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "full_21_cells_run": False, "scientific_verdict": "NOT_COMPUTED", "failures": []}
    phases = {}
    tracemalloc.start()
    try:
        with trace:
            X, num, den = probe["X"], probe["width_numerator"], probe["width_denominator"]
            upper = _divide(X * (den + num), den).quotient
            prefix = PrimePrefix(_divide(upper, 2).quotient)
            phases["sieve_finished_ns_from_start"] = time.monotonic_ns() - start
            if peak_memory_bytes() > MEMORY_CAP:
                raise ResourceBoundary("process memory cap reached after sieve")
            cell = shell_cell(prefix, X, num, den)
            phases["cell_finished_ns_from_start"] = time.monotonic_ns() - start
            if peak_memory_bytes() > MEMORY_CAP:
                raise ResourceBoundary("process memory cap reached after cell")
            # New deterministic boundary sample; no original discovery audit cell.
            sample_values = sorted({2, 3, 4, 49, prefix.limit, prefix.limit - 1})
            independent = [{"n": n, "trial_prime": bounded_trial_prime(n),
                            "sieve_prime": bool(prefix.flags[n])} for n in sample_values]
            if not all(row["trial_prime"] == row["sieve_prime"] for row in independent):
                raise AssertionError("independent bounded primality mismatch")
            capacity_witness = null_a_capacity_witness(cell)
            artifact_dir.joinpath("cell_profiles.jsonl").write_bytes(serial_cell(cell))
        receipt.update(status="PASS_STAGE1_BOUNDED_PROBE", prime_prefix_limit=prefix.limit,
                       prime_prefix_count=len(prefix.primes), rows=len(cell["rows"]),
                       zero_prime_count_rows=cell["zero_prime_count_rows"], totals=cell["totals"],
                       independent_sample=independent, null_A_capacity_audit=capacity_witness)
        generator = {"schema": "PFSSV_GENERATOR_STAGE1_RECEIPT_V1", "status": "PASS_ONE_NEW_PROBE_CELL",
                     "cell_input": {k: cell[k] for k in ("X", "num", "den", "upper")},
                     "complete_geometric_support": True, "actual_prime_ranks": True,
                     "full_cell_serialization": True, "independent_sample": independent,
                     "full_21_cells_run": False, "old_two_audit_cells_repeated": False,
                     "cell_file_sha256": hashlib.sha256(artifact_dir.joinpath("cell_profiles.jsonl").read_bytes()).hexdigest()}
        artifact_dir.joinpath("generator_receipt.json").write_bytes(_json_bytes(generator))
    except (ResourceBoundary, PrecisionUnresolved, AssertionError, ValueError) as exc:
        receipt["status"] = "PARTIAL_STAGE1_BOUNDARY"
        receipt["failures"].append({"type": type(exc).__name__, "message": str(exc)})
    finally:
        receipt["elapsed_ns"] = time.monotonic_ns() - start
        receipt["phase_times_ns"] = phases
        receipt["peak_process_memory_bytes"] = peak_memory_bytes()
        receipt["peak_python_traced_bytes"] = tracemalloc.get_traced_memory()[1]
        receipt["source_preservation_after"] = verify_sources(artifact_dir) == binding
        receipt["native_trace"] = trace.receipt()
        artifact_dir.joinpath("resource_probe.json").write_bytes(_json_bytes(receipt))
        artifact_dir.joinpath("native_runtime_receipt.json").write_bytes(_json_bytes({
            "schema": "PFSSV_STAGE1_NATIVE_RUNTIME_RECEIPT_V1", "status": receipt["status"],
            "scope": "Only this Stage 1 resource probe, not full scientific statistics or legacy transitive certification",
            "reuse_resolution_actual": "REUSE_EXECUTED: original DIV/ROOT/LOG code objects below; COMPOSE_APPLIED: T0 BRC + T1 complete-prefix window-count/rank-interval readout. No new global family or primality theorem.",
            "preparation_text_boundary": "native_substrate_plan reused the historical preparation text saying claim/ER execution pending. That text describes the earlier preparation checkpoint. The actual winning claim and ER authorization already existed before this run; the current receipt records actual execution. No blind PRE_MATH stamp is asserted.",
            "joint_view_boundary": "True two-dimensional observed prime ranks do not imply a joint null. Original family-wise primary remains one-dimensional; lack of a new joint null is not an added task acceptance gate.",
            "null_A_capacity_audit": receipt.get("null_A_capacity_audit", {"status": "NOT_REACHED"}),
            **receipt["native_trace"]}))
        tracemalloc.stop()
    print(json.dumps({"status": receipt["status"], "elapsed_ns": receipt["elapsed_ns"],
                      "peak_process_memory_bytes": receipt["peak_process_memory_bytes"], "failures": receipt["failures"]}))
    return 0 if receipt["status"] == "PASS_STAGE1_BOUNDED_PROBE" else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resource-probe", action="store_true", required=True)
    parser.parse_args()
    return resource_probe()


if __name__ == "__main__":
    raise SystemExit(main())
