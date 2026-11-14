#!/usr/bin/env python3
"""EC49FLA: independent compact certificate check and optional full exact solver replay.

Default: verify all 6,315 encoded costs and pinned summary invariants.
--full: regenerate every feasible seven-key set from the frozen nine-state BRC
catalogue, compile the previously published exact native signed-prefix trie DP,
and verify all 6,315 entries in deterministic batches of 50.
"""
import argparse
import base64
import collections
import hashlib
import itertools
import lzma
from pathlib import Path
import subprocess
import sys

P = Path(__file__).resolve().parent
R = P.parent
PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
SHA = "7a94b5b408a73e4be11405c238273e0313b829c0d0ddd4793028609b1851f248"
XZ_SHA = "f5a83e6fb6877f57e33aded9c4c864dcfc66450f184eb15488b063825bc59868"
BASE = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
FJD = R / "EC49FJD_RELEASE_B11_COMPLETE_20261111"
FKY = R / "EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112"

def load_costs():
    data = base64.b64decode((P / "EC49FLA_COST_VECTOR_6315.xz.b64").read_text().strip(), validate=True)
    assert len(data) == 1300
    assert hashlib.sha256(data).hexdigest() == XZ_SHA
    plain = lzma.decompress(data)
    assert len(plain) == 6315
    assert hashlib.sha256(plain).hexdigest() == SHA
    cost = list(plain)
    assert min(cost) == 84 and max(cost) == 204
    assert [i for i, x in enumerate(cost) if x == 84] == [5883]
    assert not [x for x in cost if x <= 83]
    assert [i for i, x in enumerate(cost) if x == 86] == [2473, 4515]
    print("EC49FLA_VECTOR_6315_INTEGRITY_PASS", len(cost), min(cost), max(cost))
    return cost

def feasible_sets():
    sys.path.insert(0, str(FJD))
    from EC49FGW_RADIUS5_SCREEN import PIN as source_pin, all_words, raw_key, pref
    assert source_pin == PIN
    cat = list(all_words())
    assert len(cat) == 178850
    labs = sorted({lab for lab, w in cat})
    assert len(labs) == 24
    lid = {lab:i for i,lab in enumerate(labs)}
    by_key = collections.defaultdict(list)
    support = collections.defaultdict(int)
    for lab,w in cat:
        k = raw_key(w)
        support[k] |= 1 << lid[lab]
        by_key[k].append((lid[lab],pref(w)[-1].hex()))
    assert len(support) == 94 and len(BASE) == 7
    others = sorted(set(support)-BASE)
    full = (1<<24)-1
    result = []
    counts = []
    for dropped in itertools.combinations(sorted(BASE),2):
        kept = BASE-set(dropped)
        have = 0
        for k in kept:
            have |= support[k]
        n=0
        for inserted in itertools.combinations(others,2):
            if have | support[inserted[0]] | support[inserted[1]] == full:
                result.append((dropped, inserted, tuple(sorted(kept | set(inserted)))))
                n+=1
        counts.append(n)
    assert len(result) == 6315 and sum(counts) == 6315
    assert 21*3741 - len(result) == 72246
    assert result[5883][:2] == (((5,4,1),(6,4,1)), ((6,3,1),(7,3,1)))
    print("EC49FLA_NATIVE_BRC_KEY_SCREEN_PASS",len(cat),len(support),len(labs),len(result))
    return result, by_key

def full_replay(cost, sets, by_key, batch=50):
    import tempfile
    with tempfile.TemporaryDirectory(prefix="ec49fla_") as temp:
        exe = str(Path(temp)/"solver")
        source=str(FKY/"SCAN_7KEY_GENERAL.cpp")
        subprocess.run(["g++","-O3","-std=c++17",source,"-o",exe],check=True)
        for start in range(0,len(sets),batch):
            ks = [entry[2] for entry in sets[start:start+batch]]
            lines=[str(len(ks))]
            for keyset in ks:
                rows=[pair for key in keyset for pair in by_key[key]]
                lines.append(str(len(rows)))
                lines.extend(f"{lab} {hexsteps}" for lab,hexsteps in rows)
            p = subprocess.run([exe],input="\n".join(lines)+"\n",
                               capture_output=True,text=True,check=True)
            got=[int(row.split()[1]) for row in p.stdout.splitlines()]
            assert len(got)==len(ks)
            expect=cost[start:start+len(got)]
            if got!=expect:
                first=next(j for j,(a,b) in enumerate(zip(got,expect)) if a!=b)
                raise AssertionError((start+first,got[first],expect[first]))
            print("EC49FLA_FULL_BATCH_PASS",start,start+len(got),flush=True)
    print("EC49FLA_EXHAUSTIVE_6315_EXACT_PASS")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--full",action="store_true")
    args=ap.parse_args()
    costs=load_costs()
    if args.full:
        sets,by_key=feasible_sets()
        full_replay(costs,sets,by_key)
if __name__=="__main__":
    main()
