#!/usr/bin/env python3
"""Reproduce EC49FKZ original signed-X6 exact prefix optima using EC49FKY trie DP.
Usage: python3 REPLAY_EXACT_SELECTED_AND_FIRST400.py [selected|first400]
Actual experiment reported by author: 15 selected cases and first 400 coverable cases.
"""
import collections
import itertools
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT/"EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref
assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
EXPECTED_SELECTED=[102,100,114,124,114,116,121,110,112,112,141,108,137,104,90]

def prepare():
    cat=list(all_words())
    labs=sorted({lab for lab,w in cat})
    assert len(cat)==178850 and len(labs)==24
    ids={lab:i for i,lab in enumerate(labs)}
    byk=collections.defaultdict(list)
    covers=collections.defaultdict(int)
    for label,word in cat:
        key=raw_key(word)
        covers[key] |= 1 << ids[label]
        byk[key].append((ids[label], pref(word)[-1].hex()))
    outside=sorted(set(covers)-BASE)
    assert len(covers)==94 and len(outside)==87
    full=(1<<24)-1
    feasible=[]
    selected=[]
    for old in itertools.combinations(sorted(BASE),2):
        keep=BASE-set(old)
        mask=0
        for k in keep:mask|=covers[k]
        seen=0
        for add in itertools.combinations(outside,2):
            if mask | covers[add[0]] | covers[add[1]] == full:
                row=(old,add,tuple(sorted(keep|set(add))))
                feasible.append(row)
                if seen<2:selected.append(row)
                seen+=1
    assert len(feasible)==6315 and len(selected)==14
    combined=tuple(sorted(BASE-{(5,4,1),(6,4,1)}|{(6,3,1),(5,5,1)}))
    selected.append(("two locally optimal singles",None,combined))
    assert len(selected)==15
    return feasible,selected,byk

def solve(records, byk, compiler_output):
    strings=[str(len(records))]
    for _,_,keys in records:
        rows=[row for key in keys for row in byk[key]]
        strings.append(str(len(rows)))
        strings.extend(str(label)+" "+wordhex for label,wordhex in rows)
    proc=subprocess.run([str(compiler_output)],input="\n".join(strings)+"\n",
        text=True,capture_output=True,check=True)
    lines=proc.stdout.strip().splitlines()
    assert len(lines)==len(records)
    for i,line in enumerate(lines):
        assert int(line.split()[0])==i
    return [int(line.split()[1]) for line in lines],lines

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else "selected"
    assert mode in ("selected","first400")
    feasible,selected,byk=prepare()
    cases=selected if mode=="selected" else feasible[:400]
    solver=ROOT/"EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112"/"SCAN_7KEY_GENERAL.cpp"
    with tempfile.TemporaryDirectory(prefix="ec49fkz_") as d:
        exe=Path(d)/"exact"
        subprocess.run(["g++","-O3","-std=c++17",str(solver),"-o",str(exe)],check=True)
        costs,lines=solve(cases,byk,exe)
    if mode=="selected":
        assert costs==EXPECTED_SELECTED
        print("EC49FKZ_SELECTED_15_EXACT_PASS",min(costs),costs)
    else:
        assert len(costs)==400 and min(costs)==100
        histogram=dict(sorted(collections.Counter(costs).items()))
        expected=json.loads((HERE/"EXACT_RADIUS2_FIRST400_SUMMARY_EC49FKZ.json").read_text())
        assert histogram=={int(k):v for k,v in expected["histogram"].items()}
        print("EC49FKZ_FIRST400_EXACT_PASS",min(costs),max(costs),histogram)

if __name__=="__main__":
    main()
