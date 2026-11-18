#!/usr/bin/env python3
"""EC49FMF: audit 450 exact BRC native-prefix optima, witness words and demand coverage.
Default: verify stored integer vector and constructively check the two 92-prefix witnesses.
--independent: execute separate Python trie-DP on both 92 cases.
--run-all: use the prior unmodified C++17 solver on all 450 cases (heavy).
"""
import collections
import hashlib
import itertools
import json
import subprocess
import sys
import tempfile
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parent
sys.path.insert(0, str(ROOT / "EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key, OPS, T, SIG, STEPS, REQ

E = json.loads((P / "EXACT_VECTOR_EC49FMF.json").read_text())
assert E["scientific_pin"] == PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert E["global_slice"] == [970, 1420] and len(E["costs"]) == 450
costs = E["costs"]
assert all(isinstance(c, int) and c > 0 for c in costs)
assert hashlib.sha256(bytes(costs)).hexdigest() == E["cost_bytes_sha256"]
assert dict(collections.Counter(str(c) for c in costs)) == E["histogram"]
assert min(costs) == 92 and [i + 970 for i, c in enumerate(costs) if c == 92] == [1376, 1393]

cat = list(all_words())
labels = sorted({label for label, _ in cat})
assert len(cat) == 178850 and len(labels) == 24
labid = {label: i for i, label in enumerate(labels)}
bykey = collections.defaultdict(list)
supports = collections.defaultdict(int)
catalogue = set(cat)
for label, w in cat:
    k = raw_key(w)
    supports[k] |= 1 << labid[label]
    bykey[k].append((labid[label], pref(w)[-1].hex()))
assert len(supports) == 94
BASE = set(map(tuple, E["baseline_keys"]))
outside = sorted(set(supports) - BASE)
full = (1 << 24) - 1
sets = []
for removed in itertools.combinations(sorted(BASE), 2):
    for added in itertools.combinations(outside, 2):
        K = sorted(BASE - set(removed) | set(added))
        mask = 0
        for k in K:
            mask |= supports[k]
        if mask == full:
            sets.append(K)
assert len(sets) == 6315

for cert in E["witnesses"]:
    idx = cert["index"]
    keys = set(map(tuple, cert["keys"]))
    assert sorted(keys) == sets[idx] and costs[idx - 970] == 92
    words = cert["words"]
    assert len(words) == 24 and len(E["witness_label_order"]) == 24
    prefixes = set()
    for label, w in zip(E["witness_label_order"], words):
        label = tuple(label)
        assert (label, w) in catalogue and raw_key(w) in keys
        assert len(w) == label[0]
        state, xyz = 0, [0] * 6
        for op in w:
            state = T[state][OPS.index(op)]
            assert state != 8
            for ax in STEPS[op]:
                xyz[abs(ax) - 1] += 1 if ax > 0 else -1
        assert SIG[state] == label[1] and xyz == [2, 0, 0, 0, 0, 0]
        prefixes.update(pref(w))
    assert set(map(tuple, E["witness_label_order"])) == set(labels)
    assert len(prefixes) == 92
    print("EC49FMF_EXPLICIT_SIGNED_X6_92_WITNESS_PASS", idx, len(prefixes), flush=True)

print("EC49FMF_FROZEN_CATALOG_AND_450_COST_VECTOR_PASS", len(cat), len(sets), len(costs), flush=True)

def independent_optimum(keyset):
    """Separate integer-only Python trie and root-demand subset DP."""
    byroot = collections.defaultdict(list)
    for label, w in cat:
        if raw_key(w) in keyset:
            byroot[pref(w)[0]].append((label, w))
    rootcost, options = {}, collections.defaultdict(list)
    for rt, rows in byroot.items():
        local = sorted({label for label, _ in rows})
        lab_index = {label: i for i, label in enumerate(local)}
        children = [{}]
        terminal = [0]
        for label, w in rows:
            u = 0
            for p in pref(w):
                v = children[u].get(p)
                if v is None:
                    v = len(children)
                    children[u][p] = v
                    children.append({})
                    terminal.append(0)
                u = v
            terminal[u] |= 1 << lab_index[label]
        def walk(u):
            dp = {0: 0}
            if terminal[u]:
                dp[terminal[u]] = 0
            for v in children[u].values():
                q = walk(v)
                nxt = {}
                for a, x in dp.items():
                    for b, y in q.items():
                        m = a | b
                        nxt[m] = min(nxt.get(m, 10**9), x + y)
                dp = nxt
            return {m: d + int(u != 0 and m != 0) for m, d in dp.items()}
        d = walk(0)
        f = [10**9] * (1 << len(local))
        for mask, val in d.items():
            f[mask] = val
        for i in range(len(local)):
            for mask in range(len(f)):
                if not (mask >> i & 1):
                    f[mask] = min(f[mask], f[mask | (1 << i)])
        rootcost[rt] = f
        for label, bit in lab_index.items():
            options[label].append((rt, bit))
    assert len(options) == 24
    acc = {rt: 0 for rt in rootcost}
    order = sorted(options, key=lambda label: len(options[label]))
    best = 10**9
    def dfs(i):
        nonlocal best
        if i == 24:
            best = min(best, sum(rootcost[rt][mask] for rt, mask in acc.items()))
            return
        for rt, bit in options[order[i]]:
            acc[rt] |= 1 << bit
            dfs(i + 1)
            acc[rt] &= ~(1 << bit)
    dfs(0)
    return best

if "--independent" in sys.argv:
    for idx in (1376, 1393):
        v = independent_optimum(set(sets[idx]))
        assert v == costs[idx - 970] == 92
        print("EC49FMF_INDEPENDENT_PYTHON_EXACT_OPTIMUM_PASS", idx, v, flush=True)

if "--run-all" in sys.argv:
    with tempfile.TemporaryDirectory() as directory:
        d = Path(directory)
        with (d / "input.txt").open("w") as o:
            o.write("450\n")
            for keyset in sets[970:1420]:
                rows = [r for key in keyset for r in bykey[key]]
                o.write(str(len(rows)) + "\n")
                for i, p in rows:
                    o.write(str(i) + " " + p + "\n")
        cpp = ROOT / "EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112" / "SCAN_7KEY_GENERAL.cpp"
        subprocess.run(["g++", "-std=c++17", "-O3", str(cpp), "-o", str(d / "scan")], check=True)
        with (d / "input.txt").open("rb") as inp, (d / "output.txt").open("wb") as out:
            subprocess.run([str(d / "scan")], stdin=inp, stdout=out, check=True)
        lines = (d / "output.txt").read_text().splitlines()
        assert len(lines) == 450
        assert [int(s.split()[1]) for s in lines] == costs
        assert [int(s.split()[0]) for s in lines] == list(range(450))
        print("EC49FMF_ALL_450_EXACT_CPP_REPLAY_PASS", flush=True)
