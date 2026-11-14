#!/usr/bin/env python3
"""Independent boundary-layer enumerator for EC49FOD.
Enumerates legal assignments directly, without subset min-plus convolution.
Supply the original 94-key master and VERIFY_EC49FNY_INDEPENDENT.py.
"""
import hashlib,itertools
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as native

CASES=(32264,32274,32279,32315,32318)
ROOTS=(3,5,6,7)
FIXED=(0,5,138,8192)
B=155
MASTER_SHA='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'

def main():
    src=Path('master_and_radius3_cases.txt')
    assert hashlib.sha256(src.read_bytes()).hexdigest()==MASTER_SHA
    U=tuple(i for i in range(24) if not any(x>>i&1 for x in FIXED))
    assert len(U)==18
    for case in CASES:
        words,keys=native.frozen(src,case=case)
        profiles={r:native.table(words,keys,r) for r in ROOTS}
        choices={i:tuple(r for r in ROOTS if i in profiles[r][1]) for i in U}
        base={r:0 for r in ROOTS}
        for j,r in enumerate(ROOTS):
            for i in range(24):
                if FIXED[j]>>i&1: base[r]|=1<<profiles[r][1][i]
        def f(T):
            forced=base.copy();flex=[]
            for i in T:
                if len(choices[i])==1:
                    r=choices[i][0]; forced[r]|=1<<profiles[r][1][i]
                else: flex.append(i)
            best=10**9
            for allocation in itertools.product(*(choices[i] for i in flex)):
                masks=forced.copy()
                for i,r in zip(flex,allocation):
                    masks[r]|=1<<profiles[r][1][i]
                best=min(best,sum(profiles[r][2][masks[r]] for r in ROOTS))
            return best
        high={};strict={}
        for h in (16,17,18):
            vals=[f(T) for T in itertools.combinations(U,h)]
            high[h]=max(vals);strict[h]=sum(v>B for v in vals)
        expect=({16:0,17:0,18:1} if case==32279 else
                {16:0,17:5,18:1})
        assert strict==expect
        assert (high[16],high[17],high[18])==(
            (153,155,156) if case==32279 else (155,157,158))
        if case!=32279:
            assert [i for i in U if f(tuple(j for j in U if j!=i))>B]==[4,5,6,8,9]
        print('EC49FOD_BOUNDARY_PASS',case,strict,high,flush=True)
    print('EC49FOD_BOUNDARY_SUCCESS subset_checks=860')
if __name__=='__main__':main()
