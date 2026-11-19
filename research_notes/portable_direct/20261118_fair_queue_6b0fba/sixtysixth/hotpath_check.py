#!/usr/bin/env python3
"""Run four address organizations inside the pinned X1 wave, using its saved frames only as an oracle."""
import argparse
import ast
from collections import Counter, OrderedDict
import csv
import gzip
import hashlib
import importlib.util
from itertools import groupby
from math import prod
import json
import os
from pathlib import Path
import random
import resource
import subprocess
import sys
from tempfile import TemporaryDirectory
from time import perf_counter_ns
from zipfile import ZipFile


ARCHIVE_HASH = "6995c9e842ed391d1363d5ec8ca0ac8d58f1c5abbc78f94c7908f54fc1e46f6c"
PREFIX = "mod7_complex_X1/"
MODES = ("table", "replace", "cancel", "memo")
OUTPUTS = ("FULL_STATES", "RAW_STORE", "EVENTS", "BRC_LEDGER", "STATS", "COUNTS")
VENDOR = ("brc_weighted_recurrent.py", "brc_division_excerpt.py", "division.py")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(archive, root):
    if digest(archive.read_bytes()) != ARCHIVE_HASH:
        raise ValueError("canonical X1 archive required")
    with ZipFile(archive) as z:
        assert z.testzip() is None
        index = json.loads(z.read(PREFIX + "MANIFEST.json"))
        for name, metadata in index.items():
            raw = z.read(PREFIX + name)
            assert len(raw) == metadata["bytes"] and digest(raw) == metadata["sha256"]
        sources = ["test_complex.py", "parent/test_mod7_only.py", "parent/parent_M5/wave_compare.py"]
        sources.extend("parent/parent_M5/vendor/" + name for name in VENDOR)
        for rel in sources:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(z.read(PREFIX + rel))
        receipts = {}
        for name in OUTPUTS:
            gz = name not in ("STATS", "COUNTS")
            raw = z.read(PREFIX + "run1/wave/mod7/" + name + ".json" + (".gz" if gz else ""))
            receipts[name] = digest(gzip.decompress(raw) if gz else raw)
        return {"zip_members": len(z.namelist()), "manifest_members": len(index), "original_outputs": receipts}


def load_source(root, mode):
    import importlib
    parent = root / "parent/parent_M5"
    sys.path[:0] = list(map(str, (root, root/"parent", parent)))
    path = parent/"wave_compare.py"
    tree = ast.parse(path.read_text())
    # Only remove construction of the 8748-entry static NEXT dictionary.
    # Never edit the propagation or state-store methods.
    eager = [node for node in tree.body if isinstance(node, ast.For)
             and isinstance(node.target, ast.Tuple)
             and [x.id for x in node.target.elts] == ["x", "coord"]]
    assert len(eager) == 1
    assert "NEXT[x, d]" in ast.unparse(eager[0])
    if mode != "table":
        tree.body.remove(eager[0])
    spec = importlib.util.spec_from_file_location("wave_compare", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    exec(compile(tree, str(path), "exec"), module.__dict__)
    x1 = importlib.import_module("test_complex")
    assert len(module.NEXT) == (8748 if mode == "table" else 0)
    return module, x1


class FactorRoute:
    def __init__(self, mode, source, codec, ar):
        self.mode = mode
        self.ar = ar
        self.cells = source.CELLS
        self.codec = codec
        self.rows = {}
        self.cache = {}
        self.epoch = 0
        self.counts = Counter()
        self.max_code = 1
        self.ar.stage = "factor_setup"
        self.powers = []
        for axis in range(6):
            p = codec.atlas.classes[axis][0]
            self.powers.append((1, p, self.ar.mul(p, p)))

    def invalidate(self):
        self.counts["invalidations"] += 1
        self.counts["discarded_rows"] += len(self.rows)
        self.counts["discarded_edges"] += len(self.cache)
        self.rows.clear()
        self.cache.clear()
        self.epoch += 1

    def __getitem__(self, key):
        return self.resolve(self.epoch, *key)[0]

    def resolve(self, epoch, cell, direction):
        if epoch != self.epoch:
            raise ValueError("stale registration")
        if not (type(cell) is int and 0 <= cell < len(self.cells)
                and type(direction) is int and 0 <= direction < 12):
            raise ValueError("unregistered Cell or signed port")
        self.counts["requests"] += 1
        key = (cell, direction)
        if self.mode == "memo" and key in self.cache:
            self.counts["edge_hits"] += 1
            return self.cache[key]
        self.counts["computed_edges"] += 1
        if cell in self.rows:
            coords, factors, code = self.rows[cell]
            self.counts["row_hits"] += 1
        else:
            coords = self.cells[cell]
            factors = tuple(self.powers[i][v] for i, v in enumerate(coords))
            code = self.codec.id_to_code[cell]
            self.rows[cell] = coords, factors, code
            self.counts["row_builds"] += 1
            self.counts["factor_fields_assembled"] += 6
            self.counts["code_lookup"] += 1
        axis = direction % 6
        old = coords[axis]     # this chart has 0,+1,-1 encoded by exponents 0,1,2
        new = (old + (1 if direction < 6 else -1)) % 3
        self.ar.stage = "online_factor"
        if self.mode == "replace":
            q, rem = self.ar.div(code, factors[axis])
            if rem:
                raise ValueError("source factor mismatch")
            next_code = self.ar.mul(q, self.powers[axis][new])
        elif new > old:
            next_code = self.ar.mul(code, self.powers[axis][new-old])
        else:
            next_code, rem = self.ar.div(code, self.powers[axis][old-new])
            if rem:
                raise ValueError("source exponent mismatch")
        target = self.codec.code_to_id[next_code]
        self.counts["final_id_lookup"] += 1
        self.max_code = max(self.max_code, code, next_code)
        result = (target, next_code)
        if self.mode == "memo":
            self.cache[key] = result
        return result


def cache_limits(events):
    trace = [(e["cell"], d) for e in events if e["kind"] == "triadic_dispatch"
             for _, d, _ in e["targets"]]
    recency = []
    histogram = Counter()
    first = {}
    last = {}
    for i, key in enumerate(trace):
        if key in first:
            distance = recency.index(key)
            histogram[distance] += 1
            del recency[distance]
        else:
            first[key] = i
        recency.insert(0, key)
        last[key] = i
    keys = set(trace)
    force = max(1 + sum(q != key and first[q] < i < last[q] for q in keys)
                for i, key in enumerate(trace))
    bypass = max(sum(first[q] <= i < last[q] for q in keys) for i in range(len(trace)))
    capacities = (32, 128, 168, 169, 192, 257, 258)
    misses = {}
    for capacity in capacities:
        cache = OrderedDict()
        count = 0
        for key in trace:
            if key not in cache:
                count += 1
                if len(cache) == capacity:
                    cache.popitem(last=False)
            else:
                cache.pop(key)
            cache[key] = None
        assert count == len(keys) + sum(n for d,n in histogram.items() if d >= capacity)
        misses[capacity] = count
    return {"requests": len(trace), "distinct_edges": len(keys), "source_cells": len({x for x,d in keys}),
            "stack_distance_multiplicity": sorted(histogram.items()), "LRU_misses": misses,
            "minimum_LRU_slots_no_recomputation": max(histogram)+1,
            "minimum_offline_slots_mandatory_insert": force,
            "minimum_offline_slots_bypass_permitted": bypass}


def verify_semantics(source, codec, snapshots, events, arithmetic):
    """Independent integer commit reconstruction; never supplies a target to the tested wave."""
    initial = snapshots[0]
    rows = initial["cells"]
    residual = [row["residual"][:] for row in rows]
    absorbed = [row["internal"] for row in rows]
    phase = [row["contact"] for row in rows]
    feedback = [row["feedback"] for row in rows]
    banks = {r["id"]:r["bank"] for r in initial["reservoirs"]}
    primes = [codec.atlas.classes[i][0] for i in range(6)]
    counts = Counter()
    for frame in snapshots[1:]:
        outgoing = Counter()
        tick = frame["heartbeat"]
        for micro, group in groupby((v for v in events if v["heartbeat"] == tick), key=lambda e:e["micro"]):
            deltas = Counter()
            if micro:
                counts["synchronous_dispatch_commits"] += 1
            for event in group:
                cell = event["cell"]
                if not micro:
                    direction, units, bank = event["direction"], event["units"], event["reservoir"]
                    assert event["kind"] == "reservoir_release" and banks[bank] >= units
                    banks[bank] -= units
                    deltas[cell, direction] += units
                    continue
                direction = event["incoming_channel"]
                k = event["multiplicity"]
                assert event["kind"] == "triadic_dispatch" and k == residual[cell][direction]//4
                assert event["contact_used"] == phase[cell] and event["feedback_used"] == feedback[cell]
                assert k == event["deposited"] and len(event["targets"]) == 3
                deltas[cell, direction] -= 4*k
                absorbed[cell] += k
                outgoing[cell] += k
                for off, (target, port, amount) in zip((0,1,3), event["targets"]):
                    axis = (direction%6 + phase[cell] + off)%6
                    sign = (direction//6)^feedback[cell]
                    assert amount == k and port == axis+6*sign
                    expected = list(source.CELLS[cell])
                    expected[axis] = (expected[axis]+(1 if sign == 0 else -1))%3
                    assert tuple(expected) == source.CELLS[target]
                    assert prod(p**v for p,v in zip(primes,expected)) == codec.id_to_code[target]
                    counts["individual_signed_target_fields"] += 6
                    counts["unit_transfers"] += k
                    counts["target_batches"] += 1
                    deltas[target,port] += k
            for (cell, port), change in deltas.items():
                residual[cell][port] += change
                assert residual[cell][port] >= 0
        for row in frame["cells"]:
            cell = row["id"]
            phase[cell] = (phase[cell]+1)%3
            feedback[cell] ^= outgoing[cell]%2
            assert (list(source.CELLS[cell]),phase[cell],feedback[cell],residual[cell],absorbed[cell]) == (
                list(row["raw_chart"]),row["contact"],row["feedback"],row["residual"],row["internal"])
        assert banks == {r["id"]:r["bank"] for r in frame["reservoirs"]}
        assert sum(banks.values())+sum(map(sum,residual))+sum(absorbed) == 768
    # Separately exercise original finite registration and budget guards.
    for f in (lambda:codec.atlas.decode(7), lambda:codec.atlas.decode(primes[0]**3),
              lambda:arithmetic.gap(3,4), lambda:source.World(codec,arithmetic,budget=min(codec.primes))):
        try:
            f()
        except (ValueError, AssertionError):
            counts["original_negative_controls"] += 1
        else:
            raise AssertionError("invalid source input accepted")
    return dict(counts)


def worker(root, mode, outdir):
    t0 = perf_counter_ns()
    mod, x1 = load_source(root, mode)
    t1 = perf_counter_ns()
    ap = mod.Arithmetic()
    ap.stage = "prime_generation"
    atlas = x1.Atlas(ap, 1024)
    t2 = perf_counter_ns()
    a = mod.Arithmetic()
    a.stage = "codec_setup"
    codec = x1.Mod7Store(a, x1.bind_atlas(atlas, a), x1.Checks())
    ar = mod.Arithmetic()
    route = None
    if mode != "table":
        route = FactorRoute(mode, mod, codec, ar)
        mod.NEXT = route
        sys.modules["test_mod7_only"].NEXT = route
    w = x1.MultiSourceWorld(codec, a)
    t3 = perf_counter_ns()
    frames = [w.frame()]
    raw = [codec.raw()]
    frame_ns = perf_counter_ns()-t3
    advance_ns = 0
    for _ in range(24):
        start = perf_counter_ns()
        w.advance()
        split = perf_counter_ns()
        frames.append(w.frame())
        raw.append(codec.raw())
        end = perf_counter_ns()
        advance_ns += split - start
        frame_ns += end - split
    start = perf_counter_ns()
    original = {"FULL_STATES": frames, "RAW_STORE": raw, "EVENTS": w.events,
                "BRC_LEDGER": a.entries, "STATS": w.stats, "COUNTS": x1.counts(a)}
    all_outputs = dict(original, ATLAS_LEDGER=ap.entries, ADDRESS_LEDGER=ar.entries,
                       ATLAS={"limit": 1024, "primes": atlas.primes, "classes": atlas.classes,
                              "certificates": atlas.certificates})
    hashes = {}
    sizes = {}
    for name, data in all_outputs.items():
        b = mod.canonical(data)
        packed = b if name in ("STATS","COUNTS","ATLAS") else gzip.compress(b, mtime=0)
        with (outdir/name).open("wb") as fp:
            fp.write(packed)
        hashes[name] = digest(b)
        sizes[name] = [len(b), len(packed)]
    end = perf_counter_ns()
    times = {"source_import_and_routing_rows_ns": t1-t0, "prime_proof_ns": t2-t1,
             "codec_route_world_setup_ns": t3-t2, "full_advance_including_audit_ns": advance_ns,
             "frames_and_raw_ns": frame_ns, "serialize_hash_write_ns": end-start, "end_to_end_ns": end-t0,
             "process_peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    counters = dict(route.counts) if route else {"requests": sum(z["transfer_batches"] for z in w.stats),
                                                 "precomputed_destination_rows": len(mod.NEXT)}
    report = {"semantic_output_sha256": {name: hashes[name] for name in OUTPUTS},
              "all_output_bytes_raw_and_written": sizes, "cold_atlas_arithmetic": x1.counts(ap),
              "route_arithmetic": x1.counts(ar), "route_counts": counters,
              "wave_arithmetic": x1.counts(a),
              "store_reads": codec.read_calls, "store_writes": codec.write_calls,
              "stored_cell_code_bits_max": max(codec.code_to_id).bit_length(),
              "largest_queried_address_bits": route.max_code.bit_length() if route else None,
              "final_stats": w.stats[-1], "event_kind_counts": dict(Counter(v["kind"] for v in w.events)),
              "cache_theory": cache_limits(w.events)}
    report["independent_commit_checks"] = verify_semantics(mod, codec, frames, w.events, a)
    # Outside the paid wave: an old handle must fail, then the same registered
    # address re-enters through a real cold route and recovers the target.
    if route:
        old_epoch = route.epoch
        first = route.resolve(old_epoch, 0, 0)
        route.invalidate()
        try:
            route.resolve(old_epoch, 0, 0)
        except ValueError:
            pass
        else:
            raise AssertionError("stale epoch accepted")
        assert route.resolve(route.epoch, 0, 0) == first
        rejected = 0
        for key in ((-1,0),(0,12)):
            try:
                route[key]
            except ValueError:
                rejected += 1
        assert rejected == 2
    return report,times


def run(args):
    root = Path(args.root) if args.root else None
    if root:
        data,times = worker(root, args.mode, args.output)
        print(json.dumps({"data":data,"timing":times}, separators=(",",":")))
        return
    if not args.archive:
        raise SystemExit("Pass --archive with the original X1 package matching " + ARCHIVE_HASH)
    final = {}
    timings = []
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        pin = prepare(args.archive, root)
        rng = random.Random(6610252)
        repeats = args.repeats if args.timing_csv else 1
        if repeats < 1:
            raise ValueError("positive number of repetitions required")
        for r in range(repeats):
            modes = list(MODES)
            rng.shuffle(modes)
            for order, mode in enumerate(modes):
                with TemporaryDirectory(dir=root) as out:
                    cmd = [sys.executable, str(Path(__file__).resolve()), "--root", str(root),
                           "--mode", mode, "--output", out]
                    measured = subprocess.check_output(cmd, env={**os.environ, "PYTHONDONTWRITEBYTECODE":"1"})
                d = json.loads(measured)
                assert d["data"]["semantic_output_sha256"] == pin["original_outputs"]
                assert final.setdefault(mode, d["data"]) == d["data"]
                timings.append({"round":r,"order":order,"mode":mode,**d["timing"]})
    if args.timing_csv:
        with args.timing_csv.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=timings[0].keys())
            writer.writeheader()
            writer.writerows(timings)
    shared = final["table"]
    metrics = {}
    invariants = ("semantic_output_sha256", "cold_atlas_arithmetic", "wave_arithmetic", "store_reads",
                  "store_writes", "stored_cell_code_bits_max", "final_stats","event_kind_counts","cache_theory","independent_commit_checks")
    for name,data in final.items():
        assert all(data[k] == shared[k] for k in invariants)
        metrics[name] = {k:v for k,v in data.items() if k not in invariants}
    print(json.dumps({"archive_sha256":ARCHIVE_HASH,"source":pin,"common":{k:shared[k] for k in invariants},
                      "modes":metrics,"negative_out_of_wave_tests_per_factor_mode":
                      ["stale epoch rejected","same endpoint recomputed after invalidation",
                       "negative Cell and invalid port rejected"]},indent=2,sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive",type=Path)
    parser.add_argument("--timing-csv",type=Path)
    parser.add_argument("--repeats",type=int,default=5)
    parser.add_argument("--root",help=argparse.SUPPRESS)
    parser.add_argument("--mode",choices=MODES,help=argparse.SUPPRESS)
    parser.add_argument("--output",type=Path,help=argparse.SUPPRESS)
    run(parser.parse_args())
