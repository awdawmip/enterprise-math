#!/usr/bin/env python3
"""EC49FRQ independent verifier: raw BRC master + CSV -> ALL 228 actions.

Does NOT import the primary solver or its preconstructed observation arrays,
and does NOT coalesce action indices or response partitions. Must run in
EC49FRQ's complete self-contained archive (source/ contains two frozen files).
Exact integer dynamic programming with original named-state response fibers.
"""
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
import csv
import hashlib
import itertools
import json
import time

BASE = Path(__file__).resolve().parent.parent
master = BASE / "source/frozen_original_master.txt"
costs = BASE / "source/EC49FPG_PROFILE.csv"
assert hashlib.sha256(master.read_bytes()).hexdigest() == (
    "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
)
assert hashlib.sha256(costs.read_bytes()).hexdigest() == (
    "a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
)
roots = (3, 5, 6, 7)
with master.open() as fd:
    head = list(map(int, fd.readline().split()))
    assert head == [94, 178850, 38169]
    families = []
    for _ in range(94):
        masks = [0] * 4
        for __ in range(int(fd.readline())):
            loc, word = fd.readline().split()
            masks[roots.index(bytes.fromhex(word)[0])] |= 1 << int(loc)
        families.append(masks)
    configurations = [
        tuple(map(int, fd.readline().split())) for _ in range(38169)
    ]


def descriptor(cfg):
    out = [0] * 24
    for fam in cfg:
        for j, m in enumerate(families[fam]):
            while m:
                bit = m & -m
                m ^= bit
                out[bit.bit_length() - 1] |= 1 << j
    return tuple(out)


target = descriptor(configurations[16943])
chosen = [
    cid for cid, cfg in enumerate(configurations) if descriptor(cfg) == target
]
assert len(chosen) == 310
active = [l for l in range(24) if target[l].bit_count() > 1]
allocations = list(itertools.product(*(
    tuple(r for j, r in enumerate(roots) if target[l] & (1 << j))
    for l in active
)))
assert len(allocations) == 144
query_keys = []
for j, r in enumerate(roots):
    loci = [l for l in active if target[l] & (1 << j)]
    query_keys += [
        (r, sum(1 << l for l, flag in zip(loci, flags) if flag))
        for flags in itertools.product((0, 1), repeat=len(loci))
    ]
assert len(query_keys) == 84
rows = defaultdict(dict)
chosen_set = set(chosen)
with costs.open() as fd:
    for rec in csv.DictReader(fd):
        cid = int(rec["config"])
        if cid in chosen_set:
            rows[cid][(int(rec["root"]), int(rec["subset"]))] = int(rec["cost"])
assert len(rows) == 310 and all(len(d) == 84 for d in rows.values())
seen = {}
representatives = []
multiplicity = []
for cid in chosen:
    profile = tuple(rows[cid][q] for q in query_keys)
    if profile not in seen:
        seen[profile] = len(representatives)
        representatives.append(cid)
        multiplicity.append(0)
    multiplicity[seen[profile]] += 1
assert len(representatives) == 141 and sum(multiplicity) == 310
terminal = []
for alloc in allocations:
    bits = {r: 0 for r in roots}
    for loc, r in zip(active, alloc):
        bits[r] |= 1 << loc
    terminal.append(tuple(
        sum(rows[c][(r, bits[r])] for r in roots)
        for c in representatives
    ))
root_obs = [
    tuple(rows[c][q] for c in representatives) for q in query_keys
]
observations = terminal + root_obs
assert len(observations) == 228
partitions = []
for v in observations:
    d = defaultdict(int)
    for i, label in enumerate(v):
        d[label] |= 1 << i
    partitions.append(tuple(d.values()))
ALL = (1 << 141) - 1
INF = 10**70


def solve(x, alpha, beta):
    weight = [alpha + beta * m for m in multiplicity]

    @lru_cache(None)
    def mass(s):
        result = 0
        while s:
            b = s & -s
            s -= b
            result += weight[b.bit_length() - 1]
        return result

    @lru_cache(None)
    def dp(s):
        if s.bit_count() == 1:
            return (0, INF)
        best = [INF, INF]
        for q, fibers in enumerate(partitions):  # All 228 original actions
            children = [s & t for t in fibers if s & t]
            if len(children) < 2:
                continue
            price = x if q >= 144 else 1
            totals = {0: 0}
            for child in children:
                if child.bit_count() == 1:
                    continue
                e, o = dp(child)
                nxt = {}
                for p, val in totals.items():
                    for k, add in ((0, e), (1, o)):
                        if add == INF:
                            continue
                        target = p ^ k
                        nxt[target] = min(nxt.get(target, INF), val + add)
                totals = nxt
            offset = price * mass(s)
            for p, val in totals.items():
                total_parity = p ^ ((price * s.bit_count()) & 1)
                best[total_parity] = min(best[total_parity], offset + val)
        return tuple(best)

    t = time.monotonic()
    ans = dp(ALL)
    return {
        "integer_x": x, "alpha": alpha, "beta": beta,
        "parity_minima": ans,
        "reachable_subsets": dp.cache_info().currsize,
        "duration_sec": round(time.monotonic() - t, 3)
    }


if __name__ == "__main__":
    expected = {
        (1, 24, 1): (7861, 7886),
        (1, 19, 2): (7080, 7099),
    }
    result = []
    for args, target in expected.items():
        got = solve(*args)
        assert got["parity_minima"] == target, (args, got)
        assert got["reachable_subsets"] == 12922
        result.append(got)
        print("PASS original 228 actions", args, target, flush=True)
    f = BASE / "evidence/EC49FRQ_INDEPENDENT_ALL228_CERTIFICATE.json"
    f.write_text(json.dumps({
        "schema": "EC49FRQ_INDEPENDENT_ALL228_V1",
        "scientific_pin": "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
        "num_original_configurations": 310,
        "num_named_profiles": 141,
        "num_named_physical_actions": 228,
        "tests": result,
        "status": "AUTHOR_INDEPENDENT_IMPLEMENTATION_NOT_MATHEMATICAL_REVIEW"
    }, indent=2) + "\n")
    print("INDEPENDENT CERTIFICATE", f, flush=True)
