#!/usr/bin/env python3
"""R284FQ: exact lower-bound certificate for q=2,u=1, n<=15.

This checker uses only the Python standard library, with integer arithmetic.
It enumerates every coordinate-permutation equivalence class of four fixed
n-bit words (constant columns removed), applies necessary adjacent distance
and exact R284FM stable-phase flow cuts, and verifies explicit first-prefix
contradictions for all three remaining 15-bit histograms.

The proof for n<15 uses the previously proved universal n>=4q+5u+2
(the exact R284FO hypothesis, model and sources are specified in the note).
"""
from itertools import combinations
from math import comb

N,Q,U=15,2,1
PAT={}
for p in range(1,8):
    bits=(0,p&1,(p>>1)&1,(p>>2)&1)
    changed={e for e in range(4) if bits[e]!=bits[(e-1)%4]}
    last=tuple(next((i-t)%4 for t in range(4)
                    if (i-t)%4 in changed) for i in range(4))
    PAT[p]=(bits,last)

def compositions(n,m):
    for cuts in combinations(range(n+m-1),m-1):
        prev=-1; out=[]
        for t in cuts:
            out.append(t-prev-1);prev=t
        out.append(n+m-2-prev)
        yield tuple(out)

def cuts(i,j):
    edges=[(p,PAT[p][1][i],4+PAT[p][1][j])
           for p in range(1,8)
           if PAT[p][0][i]!=PAT[p][0][j]]
    c={}
    for vm in range(1,256):
        mask=0
        for p,left,right in edges:
            if vm&(1<<left) and vm&(1<<right):
                mask|=1<<(p-1)
        if mask: c[mask]=min(c.get(mask,99),vm.bit_count())
    return [(tuple(k for k in range(7) if mask&(1<<k)),Q*v+2*U+1)
            for mask,v in c.items()]

def classify():
    pairs=((0,1),(1,2),(2,3),(3,0),(0,2),(1,3))
    dist=((2*Q+4*U+1),)*4+((2*(Q+U)+1),)*2
    supports=[tuple(p-1 for p in range(1,8)
                    if PAT[p][0][i]!=PAT[p][0][j])
              for i,j in pairs]
    cutsets=[cuts(i,j) for i,j in pairs]
    allhist=dist_ok=0; survivors=[]
    for x in compositions(N,7):
        allhist+=1
        if any(sum(x[k] for k in ps)<m
               for ps,m in zip(supports,dist)):
            continue
        dist_ok+=1
        if any(not any(sum(x[k] for k in ps)>=limit
                       for ps,limit in cut)
               for cut in cutsets):
            continue
        survivors.append(x)
    expected=[
        (0,0,5,0,4,6,0),
        (0,0,6,0,3,6,0),
        (0,0,6,0,4,5,0),
    ]
    assert allhist==comb(21,6)==54264,allhist
    assert dist_ok==306,dist_ok
    assert survivors==expected,survivors
    return allhist,dist_ok,survivors

def codewords(x):
    words=[0]*4
    bit_groups={p:[] for p in range(1,8)}
    k=0
    for p in range(1,8):
        for _ in range(x[p-1]):
            bit_groups[p].append(k)
            for phase in range(1,4):
                if p>>(phase-1)&1:words[phase]|=1<<k
            k+=1
    return tuple(words),bit_groups

def group_error_counts(words,phase,s):
    groups=[0]*4
    for k in range(N):
        for age in range(1,5):
            e=(phase-age)%4
            if (words[e]^words[(e+1)%4]) & (1<<k):
                if (s^words[phase]) & (1<<k):
                    groups[e]+=1
                break
        else:
            raise AssertionError("a constant column remains")
    return groups

# case, first changed-bit pattern p, stable old source s0,
# write-prefix physical word v, observed forced readout y,
# forced stable witness phase j, corresponding stable word sj.
WITNESSES=[
    (1,3, 198,199,207,1,223),
    (1,5, 387,451,455,1,463),
    (2,3,3078,3079,3087,2,7183),
    (2,5,1152,1216,3264,3,7360),
    (0,3, 102,103,111,1,127),
    (0,5, 195,227,231,1,239),
]

def check_witnesses(survivors):
    for case,p,s0,v,y,j,sj in WITNESSES:
        x=survivors[case]
        words,bits=codewords(x)
        assert words[0]==0
        assert (words[0]^words[1]) & (1<<bits[p][0])
        # Bit-coordinate relabeling makes any first bit of a pattern equivalent.
        k=bits[p][0]; mask=1<<k
        updated=(s0|mask) if words[1]&mask else (s0&~mask)
        assert updated==v,(case,p,"prefix",updated,v)
        assert max(group_error_counts(words,0,s0))<=Q
        assert max(group_error_counts(words,j,sj))<=Q
        assert (v^y).bit_count()<=U
        assert (y^sj).bit_count()<=U
        if j==1:
            # Old phase is forced by a separate legal readout v:
            # |v-s0|=1; reading y then v yields new->old rollback.
            assert (v^s0).bit_count()<=U
        else:
            # A phase other than both the old 0 and next 1 is forced.
            assert j in (2,3)
    return len(WITNESSES)

def main():
    total,passed,survivors=classify()
    six=check_witnesses(survivors)
    print("exact tuples",total,"pass six distances",passed)
    print("six-cut survivors",len(survivors),survivors)
    print("first-prefix witnesses verified",six)
    print("conclusion: no 15-bit protocol for q=2,u=1; with R284FO n>=15, n>=16")

if __name__=="__main__":
    main()
