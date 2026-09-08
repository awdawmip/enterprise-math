#!/usr/bin/env python3
"""PFSSV gen2 exact substrate and capacity audit, not a residual verdict.

Reuses the historical task sieve algorithm through the existing BRC facade.
Commands run the frozen bounded probe or the separately published original-cell
observation/capacity contract. Scientific screens, new blind tests and terminal
research labels are not implemented.
"""
from __future__ import annotations

import argparse
import base64
from array import array
from bisect import bisect_left, bisect_right
from collections import Counter
from dataclasses import asdict, is_dataclass
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time
import tracemalloc
import zlib

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
TRANSPORT_CAP = 50 * 1024**2
TRACE_CHUNK_BYTES = 256 * 1024
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


class TraceTransport:
    """Lossless byte envelope; the mathematical trace records are unchanged."""
    def __init__(self, stream, *, encoded: bool, byte_limit: int = TRANSPORT_CAP):
        self.stream, self.encoded, self.byte_limit = stream, encoded, byte_limit
        self.buffer = bytearray()
        self.raw_hash = hashlib.sha256()
        self.raw_bytes = self.container_bytes = self.sequence = 0
        self.complete = self.failed = False
        if encoded:
            self._emit({"kind": "header", "schema": "PFSSV_TRACE_GZIP_BASE64_JSONL_V1",
                        "raw_format": "PFSSV_NATIVE_TRACE_JSONL_V1", "chunk_raw_bytes": TRACE_CHUNK_BYTES,
                        "compression": "gzip_mtime_0_level_6"})

    def _emit(self, record):
        payload = _json_bytes(record)
        if self.container_bytes + len(payload) > self.byte_limit:
            self.failed = True
            raise ResourceBoundary("trace transport byte cap reached")
        self.stream.write(payload)
        self.container_bytes += len(payload)

    def _chunk(self, raw: bytes):
        self._emit({"kind": "chunk", "sequence": self.sequence, "raw_bytes": len(raw),
                    "raw_sha256": hashlib.sha256(raw).hexdigest(),
                    "gzip_base64": base64.b64encode(gzip.compress(raw, compresslevel=6, mtime=0)).decode("ascii")})
        self.sequence += 1

    def write(self, payload: bytes):
        if self.complete or self.failed:
            raise RuntimeError("trace transport is closed or failed")
        self.raw_hash.update(payload)
        self.raw_bytes += len(payload)
        if not self.encoded:
            self.stream.write(payload)
            self.container_bytes += len(payload)
            return
        self.buffer.extend(payload)
        while len(self.buffer) >= TRACE_CHUNK_BYTES:
            self._chunk(bytes(self.buffer[:TRACE_CHUNK_BYTES]))
            del self.buffer[:TRACE_CHUNK_BYTES]

    def finish(self):
        if self.complete or self.failed:
            return
        if self.encoded:
            if self.buffer:
                self._chunk(bytes(self.buffer))
                self.buffer.clear()
            self._emit({"kind": "footer", "chunk_count": self.sequence, "raw_bytes": self.raw_bytes,
                        "raw_sha256": self.raw_hash.hexdigest()})
        self.complete = True


def decode_trace_transport(path: Path, output: Path | None = None) -> dict:
    """Verify all ordered chunks and decode exact raw bytes, never evaluating math."""
    whole = hashlib.sha256()
    total = sequence = 0
    short_chunk = footer = False
    destination = None
    try:
        with path.open("rb") as source:
            header_line = source.readline()
            if not header_line.endswith(b"\n"):
                raise ValueError("truncated trace transport header line")
            header = json.loads(header_line)
            expected = {"kind": "header", "schema": "PFSSV_TRACE_GZIP_BASE64_JSONL_V1",
                        "raw_format": "PFSSV_NATIVE_TRACE_JSONL_V1", "chunk_raw_bytes": TRACE_CHUNK_BYTES,
                        "compression": "gzip_mtime_0_level_6"}
            if header != expected:
                raise ValueError("invalid trace transport header")
            if path.stat().st_size > TRANSPORT_CAP:
                raise ValueError("trace transport exceeds authorized container budget")
            if output is not None:
                destination = output.open("xb")
            for line in source:
                if not line.endswith(b"\n"):
                    raise ValueError("truncated trace transport record line")
                row = json.loads(line)
                if footer:
                    raise ValueError("trailing trace transport records")
                if row.get("kind") == "footer":
                    if (type(row.get("chunk_count")) is not int or type(row.get("raw_bytes")) is not int
                            or row["chunk_count"] != sequence or row["raw_bytes"] != total
                            or row.get("raw_sha256") != whole.hexdigest()):
                        raise ValueError("trace transport footer mismatch")
                    footer = True
                    continue
                if (row.get("kind") != "chunk" or type(row.get("sequence")) is not int
                        or row["sequence"] != sequence or short_chunk):
                    raise ValueError("invalid trace transport sequence")
                size = row.get("raw_bytes")
                if type(size) is not int or not 1 <= size <= TRACE_CHUNK_BYTES:
                    raise ValueError("invalid trace chunk size")
                try:
                    packed = base64.b64decode(row["gzip_base64"], validate=True)
                    decoder = zlib.decompressobj(31)
                    raw = decoder.decompress(packed, TRACE_CHUNK_BYTES + 1)
                except (ValueError, KeyError, zlib.error) as exc:
                    raise ValueError("invalid compressed trace chunk") from exc
                if (len(raw) != size or not decoder.eof or decoder.unused_data or decoder.unconsumed_tail
                        or hashlib.sha256(raw).hexdigest() != row.get("raw_sha256")):
                    raise ValueError("trace chunk bytes or hash mismatch")
                total += size
                if total > TRACE_CAP:
                    raise ValueError("decoded raw trace exceeds authorized budget")
                whole.update(raw)
                if destination is not None:
                    destination.write(raw)
                sequence += 1
                short_chunk = size < TRACE_CHUNK_BYTES
            if not footer:
                raise ValueError("truncated trace transport: missing footer")
        if destination is not None:
            destination.close()
        return {"status": "PASS_LOSSLESS_TRANSPORT_VERIFICATION", "encoding": expected["schema"],
                "raw_bytes": total, "raw_sha256": whole.hexdigest(), "chunk_count": sequence,
                "transport_bytes": path.stat().st_size,
                "transport_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    except BaseException:
        if destination is not None:
            destination.close()
            output.unlink()
        raise


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
    def __init__(self, path: Path, *, deadline_ns: int | None = None, byte_limit: int = TRACE_CAP,
                 replace_verified: bool = False, encoded_transport: bool = False,
                 transport_limit: int = TRANSPORT_CAP):
        self.path = path
        self.deadline_ns = deadline_ns
        self.byte_limit = byte_limit
        self.replace_verified = replace_verified
        self.encoded_transport = encoded_transport
        self.transport_limit = transport_limit
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
        self.previous_profile = sys.getprofile()
        if self.previous_profile is not None:
            raise RuntimeError("refuse to replace an existing profiler")
        self.stream = self.path.open("wb" if self.replace_verified else "xb")
        try:
            self.transport = TraceTransport(self.stream, encoded=self.encoded_transport, byte_limit=self.transport_limit)
        except BaseException:
            self.stream.close()
            raise
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
            self.transport.write(payload)
            self.bytes += len(payload)
            self.seen[digest] += 1

    def __exit__(self, *exc):
        sys.setprofile(self.previous_profile)
        try:
            self.transport.finish()
        finally:
            self.stream.close()

    def receipt(self):
        return {
            "native_code_object_calls": dict(self.calls),
            "native_code_object_trace_returns": dict(self.returns),
            "distinct_traces": len(self.seen), "all_trace_events": sum(self.seen.values()),
            "trace_bytes": self.path.stat().st_size,
            "trace_sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
            "raw_trace_bytes": self.transport.raw_bytes,
            "raw_trace_sha256": self.transport.raw_hash.hexdigest(),
            "encoding": "PFSSV_TRACE_GZIP_BASE64_JSONL_V1" if self.encoded_transport else "PFSSV_NATIVE_TRACE_JSONL_V1",
            "transport_complete": self.transport.complete,
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
                     "legacy_null_A_band": 7 if bins["overflow_u_gt_half"] and p**4 > X else bins["coarse_band"],
                     "small_trim": p > 31, "scale_trim": p**4 > X})
    if sum(map(sum, grid)) != totals["raw"]:
        raise AssertionError("joint prime-rank view lost mass")
    if sum(profiles["raw"]) + totals["overflow"] != totals["raw"]:
        raise AssertionError("raw domain/overflow accounting failed")
    overflow_by_view = {"raw": totals["overflow"], "small_trim": 0, "scale_trim": 0}
    for row in rows:
        if row["bins"]["overflow_u_gt_half"]:
            for name in ("small_trim", "scale_trim"):
                overflow_by_view[name] += row["count"] if row[name] else 0
    for name in ("small_trim", "scale_trim"):
        if sum(profiles[name]) + overflow_by_view[name] != totals[name]:
            raise AssertionError("trim profile/overflow mass accounting failed")
    return {"schema": "PFSSV_NATIVE_CELL_V2", "X": X, "num": num, "den": den, "upper": U,
            "totals": totals, "rows": rows, "geometrically_empty_rows": excluded,
            "overflow_by_view": overflow_by_view,
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


def null_a_complete_capacity_audit(cell: dict) -> dict:
    """Audit every original band/p-residue/q-residue stratum, without sampling.

    For each target, the maximum source channel count characterizes whether
    any permitted assignment exceeds that target's integer residue capacity.
    Historical overflow rows are explicitly tagged with the old band-7 rule
    for this audit only; their log profiles remain separate overflow strata.
    """
    groups = {}
    for row in cell["rows"]:
        band = row["legacy_null_A_band"]
        if band is not None:
            groups.setdefault((band, row["p_mod_30"]), []).append(row)
    records = []
    failure_count = 0
    for key, rows in sorted(groups.items()):
        for residue in (1, 7, 11, 13, 17, 19, 23, 29):
            source = max(rows, key=lambda row: row["q_mod_30_counts"][residue])
            maximum = source["q_mod_30_counts"][residue]
            targets = []
            for target in rows:
                rem = _divide(target["qlo"], 30).remainder
                offset = _divide(residue + 30 - rem, 30).remainder
                first = target["qlo"] + offset
                capacity = 0 if first > target["qhi"] else _divide(target["qhi"] - first, 30).quotient + 1
                observed = target["q_mod_30_counts"][residue]
                if observed > capacity:
                    raise AssertionError("observed channel exceeds exact integer residue capacity")
                violates = maximum > capacity
                failure_count += violates
                targets.append({"p": target["p"], "qlo": target["qlo"], "qhi": target["qhi"],
                                "observed_count": observed, "integer_residue_capacity": capacity,
                                "positive_probability_violation": violates,
                                "overflow_u_gt_half": target["bins"]["overflow_u_gt_half"]})
            records.append({"coarse_band": key[0], "p_mod_30": key[1], "q_mod_30": residue,
                            "size": len(rows), "source_maximum_p": source["p"],
                            "source_maximum_count": maximum,
                            "specified_source_to_target_probability": {"numerator": 1, "denominator": len(rows)},
                            "targets": targets})
    return {"schema": "PFSSV_NULL_A_EXACT_CAPACITY_AUDIT_V1",
            "status": "MODEL_SUPPORT_FAILURE" if failure_count else "NO_CAPACITY_VIOLATION_IN_THIS_CELL",
            "violating_target_channel_count": failure_count,
            "stratum_channel_count": len(records), "strata": records,
            "random_draws": 0, "counts_clipped": False, "rejection_sampling": False,
            "band_boundary": "Original coarse band rule including explicitly tagged legacy overflow band7. This is not density-flat-bin clipping.",
            "strength": "Exact original scalar-permutation reachability/capacity check. No violation is not a proof of a valid prime process, fine-density control, or joint null."}


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


def _stage2_contract(artifact_dir: Path, published_commit: str, published_sha256: str) -> tuple[dict, str]:
    """Consume the one published precompute contract, without inventing authority."""
    raw = artifact_dir.joinpath("result_summary.json").read_bytes()
    if len(published_commit) != 40 or any(c not in "0123456789abcdef" for c in published_commit):
        raise ValueError("exact published precompute commit required")
    if hashlib.sha256(raw).hexdigest() != published_sha256:
        raise ValueError("published precompute content hash mismatch")
    summary = json.loads(raw)
    contract = summary["stage2_precompute_contract"]
    if contract["mode"] != "EXACT_OBSERVATION_AND_DETERMINISTIC_CAPACITY_AUDIT":
        raise ValueError("unexpected Stage 2 mode")
    if contract["scientific_null_draws"] != 0 or contract["blind_holdout_claim"]:
        raise ValueError("Stage 2 scientific/blindness scope violation")
    if contract["cells"] != [[X, num, den] for X in
            (100000, 300000, 1000000, 3000000, 10000000, 30000000, 100000000)
            for num, den in ((1, 100), (3, 1000), (1, 1000))]:
        raise ValueError("the complete original 21-cell design is required")
    if not contract.get("stage1_published_commit"):
        raise ValueError("published Stage 1 and precompute source bindings required")
    for key, upper in (("time_limit_seconds", 1800), ("memory_limit_bytes", MEMORY_CAP),
                       ("trace_limit_bytes", TRACE_CAP), ("trace_transport_limit_bytes", TRANSPORT_CAP)):
        _natural(contract[key], key, 1)
        if contract[key] > upper:
            raise ValueError("Stage 2 resource limit exceeds authorization")
    if contract["stage2_script_sha256"] != hashlib.sha256(Path(__file__).read_bytes()).hexdigest():
        raise ValueError("Stage 2 script differs from published contract")
    return contract, hashlib.sha256(raw).hexdigest()


def observation_capacity_run(published_commit: str, published_sha256: str) -> int:
    """Full observations only; a model failure cannot become a residual verdict."""
    artifact_dir = REPO.joinpath(ARTIFACT)
    binding = verify_sources(artifact_dir)
    contract, precompute_sha = _stage2_contract(artifact_dir, published_commit, published_sha256)
    for row in contract["stage1_replaceable_outputs"]:
        if hashlib.sha256(artifact_dir.joinpath(row["name"]).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"pre-run Stage 1 output drift: {row['name']}")
    for row in contract["retained_source_files"]:
        if hashlib.sha256(REPO.joinpath(row["path"]).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"retained Stage 1 or Driver source drift: {row['path']}")
    ledger = json.loads(artifact_dir.joinpath("discrepancy_ledger.json").read_bytes())
    start = time.monotonic_ns()
    deadline = start + contract["time_limit_seconds"] * 10**9
    trace = NativeTraceCapture(artifact_dir.joinpath("native_trace.jsonl"), deadline_ns=deadline,
                               byte_limit=contract["trace_limit_bytes"], replace_verified=True,
                               encoded_transport=True, transport_limit=contract["trace_transport_limit_bytes"])
    summary = {"schema": "PFSSV_STAGE2_OBSERVATION_SUMMARY_V1", "stage2_precompute_contract": contract,
               "precompute_source": {"commit": published_commit, "sha256": precompute_sha},
               "argv": sys.argv, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "source_execution_record": binding["execution_record_id"],
               "scientific_screen": "NOT_RUN_DRIVER_CAPACITY_GATE", "scientific_null_draws": 0,
               "residual_hard_target": "OPEN", "blindness": "POST_EXPOSURE_REANALYSIS",
               "cells": [], "failures": []}
    tracemalloc.start()
    try:
        with trace, artifact_dir.joinpath("cell_profiles.jsonl").open("wb") as cells_out:
            prefix = PrimePrefix(MAX_Q)
            summary["prime_prefix"] = {"limit": prefix.limit, "prime_count": len(prefix.primes)}
            coords = CoordinateBins()
            if peak_memory_bytes() > contract["memory_limit_bytes"]:
                raise ResourceBoundary("Stage 2 memory limit after full prime prefix")
            for index, (X, num, den) in enumerate(contract["cells"]):
                cell = shell_cell(prefix, X, num, den, coords)
                audit = null_a_complete_capacity_audit(cell)
                cell["null_A_capacity_audit"] = audit
                cell["scientific_status"] = "OBSERVATION_AND_CAPACITY_AUDIT_ONLY"
                cells_out.write(serial_cell(cell))
                cells_out.flush()
                summary["cells"].append({"X": X, "num": num, "den": den, "upper": cell["upper"],
                    "totals": cell["totals"], "geometric_rows": len(cell["rows"]),
                    "zero_prime_count_rows": cell["zero_prime_count_rows"],
                    "empty_integer_windows": len(cell["geometrically_empty_rows"]),
                    "overflow_by_view": cell["overflow_by_view"],
                    "capacity_audit_status": audit["status"],
                    "violating_target_channel_count": audit["violating_target_channel_count"],
                    "stratum_channel_count": audit["stratum_channel_count"]})
                peak = peak_memory_bytes()
                if peak > contract["memory_limit_bytes"]:
                    raise ResourceBoundary("Stage 2 memory cap reached")
                print(json.dumps({"completed_cells": index + 1, "X": X, "width": [num, den],
                                  "capacity_status": audit["status"], "trace_bytes": trace.bytes,
                                  "elapsed_ns": time.monotonic_ns() - start, "peak_memory_bytes": peak}), flush=True)
        summary["trace_roundtrip"] = decode_trace_transport(artifact_dir.joinpath("native_trace.jsonl"))
        if (summary["trace_roundtrip"]["raw_sha256"] != trace.transport.raw_hash.hexdigest()
                or summary["trace_roundtrip"]["raw_bytes"] != trace.bytes):
            raise ValueError("decoded trace differs from original captured event bytes")
        if time.monotonic_ns() >= deadline:
            raise ResourceBoundary("Stage 2 time cap includes trace verification")
        summary["status"] = "PASS_COMPLETE_21_CELL_OBSERVATION_AND_CAPACITY_AUDIT"
    except (ResourceBoundary, PrecisionUnresolved, AssertionError, ValueError) as exc:
        summary["status"] = "PARTIAL_STAGE2_BOUNDARY"
        summary["failures"].append({"type": type(exc).__name__, "message": str(exc)})
    finally:
        summary["source_preservation_after"] = verify_sources(artifact_dir) == binding
        summary["retained_source_preservation_after"] = all(
            hashlib.sha256(REPO.joinpath(row["path"]).read_bytes()).hexdigest() == row["sha256"]
            for row in contract["retained_source_files"])
        if not summary["retained_source_preservation_after"]:
            summary["status"] = "PARTIAL_STAGE2_BOUNDARY"
            summary["failures"].append({"type": "ValueError", "message": "retained Stage 1 or Driver source drift"})
        summary["cell_file_sha256"] = hashlib.sha256(artifact_dir.joinpath("cell_profiles.jsonl").read_bytes()).hexdigest()
        summary["native_trace"] = trace.receipt()
        summary["model_support_failure_cells"] = sum(c["capacity_audit_status"] == "MODEL_SUPPORT_FAILURE" for c in summary["cells"])
        summary["joint_null"] = "NOT_DEFINED_NOT_AN_ADDED_ACCEPTANCE_GATE"
        summary["elapsed_ns"] = time.monotonic_ns() - start
        summary["peak_process_memory_bytes"] = peak_memory_bytes()
        summary["peak_python_traced_bytes"] = tracemalloc.get_traced_memory()[1]
        if summary["peak_process_memory_bytes"] > contract["memory_limit_bytes"] or time.monotonic_ns() >= deadline:
            summary["status"] = "PARTIAL_STAGE2_BOUNDARY"
            summary["failures"].append({"type": "ResourceBoundary", "message": "resource cap including receipt preparation"})
        for item in ledger["items"]:
            item["status"] = ("COMPLETE_OBSERVATION_REPAIR_RECOMPUTED_NOT_SCIENTIFIC_ACCEPTANCE"
                              if not summary["failures"] and len(summary["cells"]) == 21
                              else "PARTIAL_STAGE2_OBSERVATION_CHECK")
        ledger["stage2_evidence"] = {"status": summary["status"], "completed_cells": len(summary["cells"]),
            "precompute_source": summary["precompute_source"], "stage1_source": contract["stage1_published_commit"],
            "model_support_failure_cells": summary["model_support_failure_cells"], "scientific_null_draws": 0,
            "corrected_signed_null_profiles": "UNAVAILABLE_NOT_ZERO", "hard_target_status": "OPEN"}
        artifact_dir.joinpath("discrepancy_ledger.json").write_bytes(_json_bytes(ledger))
        summary["discrepancy_ledger_sha256"] = hashlib.sha256(artifact_dir.joinpath("discrepancy_ledger.json").read_bytes()).hexdigest()
        artifact_dir.joinpath("result_summary.json").write_bytes(_json_bytes(summary))
        artifact_dir.joinpath("generator_receipt.json").write_bytes(_json_bytes({
            "schema": "PFSSV_STAGE2_GENERATOR_RECEIPT_V1", "status": summary["status"],
            "completed_cells": len(summary["cells"]), "cell_file_sha256": summary["cell_file_sha256"],
            "prime_prefix_limit": MAX_Q, "stage1_source": contract["stage1_published_commit"],
            "actual_prime_prefix": summary.get("prime_prefix"),
            "claim_id": binding["claim_id"], "scientific_null_draws": 0}))
        artifact_dir.joinpath("native_runtime_receipt.json").write_bytes(_json_bytes({
            "schema": "PFSSV_STAGE2_NATIVE_RUNTIME_RECEIPT_V1", "status": summary["status"],
            "scope": "Exact original-cell observation and deterministic capacity audit only; no scientific residual screen",
            "stage1_source": contract["stage1_published_commit"],
            "method_harvest": "T0_BRC + T1_SCALE_ENUMERATION_VALUATION COMPOSE: actual BRC boundaries, complete prime prefix, cumulative-count window difference and lossless rank-bin intersections. No new primality theorem or global tool family.",
            "elapsed_ns_including_trace_transport_and_verification": summary["elapsed_ns"],
            "peak_process_memory_bytes": summary["peak_process_memory_bytes"],
            "lossless_transport_verification": summary.get("trace_roundtrip"),
            **summary["native_trace"]}))
        tracemalloc.stop()
    print(json.dumps({"status": summary["status"], "completed_cells": len(summary["cells"]),
                      "model_support_failure_cells": summary["model_support_failure_cells"],
                      "elapsed_ns": summary["elapsed_ns"], "failures": summary["failures"]}), flush=True)
    return 0 if len(summary["cells"]) == 21 and not summary["failures"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--resource-probe", action="store_true")
    modes.add_argument("--observation-capacity", action="store_true")
    modes.add_argument("--verify-trace", type=Path, metavar="TRANSPORT_JSONL")
    parser.add_argument("--decoded-output", type=Path)
    parser.add_argument("--precompute-commit", default="")
    parser.add_argument("--precompute-sha256", default="")
    args = parser.parse_args()
    if args.verify_trace is not None:
        print(json.dumps(decode_trace_transport(args.verify_trace, args.decoded_output), sort_keys=True))
        return 0
    if args.decoded_output is not None:
        parser.error("--decoded-output requires --verify-trace")
    return resource_probe() if args.resource_probe else observation_capacity_run(args.precompute_commit, args.precompute_sha256)


if __name__ == "__main__":
    raise SystemExit(main())
