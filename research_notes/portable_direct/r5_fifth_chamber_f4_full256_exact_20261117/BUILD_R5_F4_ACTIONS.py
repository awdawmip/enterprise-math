#!/usr/bin/env python3
"""Generate the exact five-action full-256 normal-response masks at tau=U-1.
Usage: python BUILD_R5_F4_ACTIONS.py EXACT_R5_ALL_101_BUDGETS.json f4_actions.txt
"""
import hashlib,json,sys
from pathlib import Path
INPUT_SHA256='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
U=58182461585441404127941754880
BUDGETS=(216,223,296,214,215)

def maximal_normal_supports(row,tau):
    groups={}
    for i,center in enumerate(row):groups[center]=groups.get(center,0)|(1<<i)
    candidates=set()
    for low in sorted(groups):
        mask=0
        for center,group in groups.items():
            if low<=center<=low+tau:mask|=group
        candidates.add(mask)
    return tuple(sorted(a for a in candidates if not any(a!=b and a&b==a for b in candidates)))

def main(src,dst):
    raw=Path(src).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_SHA256
    data=json.loads(raw)
    rows={int(k):tuple(map(int,item['counts'])) for k,item in data['counts_and_cohorts'].items()}
    assert set(rows)==set(range(214,315)) and all(len(r)==256 for r in rows.values())
    with open(dst,'w') as f:
        f.write(f'{len(BUDGETS)}\n')
        for k in BUDGETS:
            family=maximal_normal_supports(rows[k],U-1)
            f.write(f'{k} {len(family)}\n')
            for a in family:
                f.write(' '.join(str((a>>(64*i))&((1<<64)-1)) for i in range(4))+'\n')
    print('SHA256',hashlib.sha256(Path(dst).read_bytes()).hexdigest())

if __name__=='__main__':main(*sys.argv[1:])
