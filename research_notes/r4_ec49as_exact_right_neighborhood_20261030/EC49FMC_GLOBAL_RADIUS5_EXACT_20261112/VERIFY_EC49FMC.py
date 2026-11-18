#!/usr/bin/env python3
"""Recompute 1137 radius-five fixed-seven-key signed-X6 prefix minima.
Reuses frozen catalogue and the pre-existing C++ exact trie/subset-DP solver.
"""
from pathlib import Path
from collections import defaultdict, Counter
from itertools import combinations
import sys, subprocess, tempfile, zlib, base64, hashlib, argparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key
assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
SEED = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
FORCED = ((2,1,1),(3,0,1))
# Costs minus 100, exact 1137-byte uint8 vector, compressed/base64 for durable transfer.
# Its hash verifies integrity; its entries are recomputed, not presumed proved.
ENCODED = (
'eNqVUmtP4kAU/QeGT8RUc+OSakqtUG7pg04L7XSYgu3Y8gpgUFFC1Jjdb/7/LRIUdbObPZ00PXfuSc/cM0C4BbzbRyCcABcCS2VV0ZwgKwoSXBgtNyDd/gBIFyxaPtjulUoVSQLjRFY8lq4UUGsVRbf9qG7a7U5cKDcL2kAQTikc6VrAhpvSIezw8fVfMC98ygkXk8Ittzih5mHTYPNz45j7o7PjaudMxaCX/5S1UxPrhkjHT00aJkaL0CghvOlELT8MWG+00RPeoAq7I4TqBR9nnaqdam7oBMNXx8g7Fruil89FG2mQFnlHg+yzL4RzjzP+Do/vs89keN0Xg3w8Ww0m89li+aLYDQbUpnchYzhh+TYNJyLeVe4J4MFMDOLbaSzw9pEATRL9FGg9QCM8ZNBUzbnqURReTyPVwAV7WDdCl6avhHkhZswLpnH2QInDTzp9JxifIPDWIBYibuN0EmcMBU6X23/u3mgBJToQPxwVJdIoTqoYkrOdh6ITSSNASHM3AZv8A4yOWQqcLYC/Pd3gQCurmQ/HtfORXIK0LCk/qsbKAuPSbLGA588iYJlcB+5PNopZJxr0xXC11Ze1kpqBphwNgUdJp9CXJEWqGCs4HSuyYVyYT0Xb55v212vHnV14bboXXvcP4fWWejNs+dEoTuaDyfVLUEdXdtUY28Xk0lj0E+o6yEUxYMFcGqLooUjFDvxSfCAR3xDV5rGZ4OxeFLF0MdE9FUOvp7qVWG1biIljuSLsL2SULVRrsennRYKep3LMZoUBvJlmo9vZYr3RCwzRZnnhTm5TzDydYEa8IGLZA8o+yrW4ZuUC8c3su78Pkn73h6jhHj6RL1isN1bmN+vlbPF4v/71G6ghBe0='
)
COST_BYTES = zlib.decompress(base64.b64decode(ENCODED))
assert len(COST_BYTES)==1137
assert hashlib.sha256(COST_BYTES).hexdigest()=='e9ad477f4aa5c7e7ca02aa1b113d55b0e523122e01c8a396933df14486fe7471'
EXPECTED = [100+b for b in COST_BYTES]

def prepare():
    cat = list(all_words())
    assert len(cat)==178850
    labels = sorted({lab for lab,_ in cat})
    assert len(labels)==24
    lab_id = {lab:i for i,lab in enumerate(labels)}
    masks, rows = defaultdict(int), defaultdict(list)
    for lab,w in cat:
        k=raw_key(w)
        masks[k] |= 1 << lab_id[lab]
        rows[k].append((lab_id[lab],pref(w)[-1].hex()))
    assert len(masks)==94 and SEED.issubset(masks)
    assert all(sum(bool(mask & (1<<i)) for mask in masks.values())==1 for i in (0,1))
    assert {k for k in masks if masks[k]&3}==set(FORCED)
    full=(1<<24)-1
    outside=sorted(set(masks)-SEED)
    assert len(outside)==87
    selected=[]
    fixed=masks[FORCED[0]]|masks[FORCED[1]]
    for five in combinations(outside,5):
        mask=fixed
        for k in five: mask |= masks[k]
        if mask==full: selected.append((*FORCED,*five))
    assert len(selected)==1137
    return selected,rows

def run_solver(selected,rows,limit):
    cpp=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp'
    assert cpp.is_file()
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'scan'
        subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(exe)],check=True)
        result=[]
        for start in range(0,limit,100):
            part=selected[start:min(limit,start+100)]
            lines=[str(len(part))]
            for keys in part:
                words=[item for k in keys for item in rows[k]]
                lines.append(str(len(words)))
                lines.extend(f'{lab} {word}' for lab,word in words)
            process=subprocess.run([str(exe)],input='\n'.join(lines)+'\n',
                                   capture_output=True,text=True,check=True)
            output=process.stdout.splitlines()
            assert len(output)==len(part)
            for i,line in enumerate(output):
                fields=line.split()
                assert int(fields[0])==i and len(fields)==5
                cost=int(fields[1]); roots=int(fields[3])
                assert roots in (3,4)
                assert cost==EXPECTED[start+i],(start+i,cost,EXPECTED[start+i])
                result.append((cost,roots))
        return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=1137)
    args=ap.parse_args()
    assert 1<=args.limit<=1137
    selected,rows=prepare()
    result=run_solver(selected,rows,args.limit)
    if args.limit==1137:
        costs=[v for v,_ in result]
        assert min(costs)==114 and max(costs)==217
        assert [i for i,c in enumerate(costs) if c==114]==[47,638]
        assert Counter(r for _,r in result)=={3:260,4:877}
        print('EC49FMC_R5_ALL_1137_EXACT_PASS',min(costs),max(costs),len(result))
    else:
        print('EC49FMC_PREFIX_SAMPLE_PASS',len(result))

if __name__=='__main__':
    main()
