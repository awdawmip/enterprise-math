#!/usr/bin/env python3
"""R670: exact V17 S3 reflection-block no-repeat transport and online minimality.
Pure Python standard library, integer arithmetic only. Run: python R670_VERIFY.py
"""
import itertools
import json
from collections import defaultdict, deque
from pathlib import Path

E=(0,1,2)
G=((0,2,1),(2,1,0),(1,0,2))  # R667 A,B,C, V17 right factors
R=(2,0,1)
def mul(p,q): return tuple(p[q[i]] for i in range(3))
def frame(word):
    h=E
    for j in word: h=mul(h,G[j])
    return h

def dp_counts(n):
    """Each path state is (counts, last label, full S3 holonomy)."""
    a,b,c=n
    table={(0,0,0,-1,E):1}
    for _ in range(a+b+c):
        nxt=defaultdict(int)
        for (i,j,k,last,h),ways in table.items():
            used=(i,j,k)
            for x in range(3):
                if used[x]==n[x] or x==last: continue
                new=tuple(used[t]+int(x==t) for t in range(3))
                nxt[(*new,x,mul(h,G[x]))]+=ways
        table=nxt
    counts=defaultdict(int)
    for (i,j,k,last,h),ways in table.items():
        assert (i,j,k)==n
        counts[h]+=ways
    return dict(counts)

def brute_all(max_len):
    """Independent word enumerator, all no-repeat words up to max_len."""
    result=defaultdict(lambda: defaultdict(int))
    result[(0,0,0)][E]=1
    for length in range(1,max_len+1):
        for start in range(3):
            for tail in itertools.product(range(2),repeat=length-1):
                w=[start]
                for bit in tail:
                    w.append((w[-1]+1+bit)%3)
                n=tuple(w.count(j) for j in range(3))
                result[n][frame(w)]+=1
    return {n:dict(v) for n,v in result.items()}

def minimal_moore_two():
    a,b=G[:2]
    init=(E,-1)
    q=deque([init]); shortest={init:""}
    while q:
        h,last=q.popleft()
        for letter,g in enumerate((a,b)):
            if letter==last: continue
            target=(mul(h,g),letter)
            if target not in shortest:
                shortest[target]=shortest[(h,last)]+"AB"[letter]
                q.append(target)
    assert len(shortest)==13,len(shortest)
    assert {h for h,last in shortest if last==0}==set(itertools.permutations(E))
    assert {h for h,last in shortest if last==1}==set(itertools.permutations(E))
    def obs(state):
        h,last=state
        return (h,tuple(i for i in (0,1) if i!=last))
    assert len({obs(s) for s in shortest})==len(shortest)
    return len(shortest),max(map(len,shortest.values()))

def main():
    brute=brute_all(10)
    n_checked=0
    for a in range(7):
      for b in range(7):
       for c in range(7):
        if a+b+c>10: continue
        n=(a,b,c)
        assert dp_counts(n)==brute.get(n,{}),(n,dp_counts(n),brute.get(n,{}))
        n_checked+=1
    balanced=[]
    for m in range(1,13):
        d=dp_counts((m,m,m));T=sum(d.values())
        if m%2:
            assert len(d)==3 and all(d[g]==T//3 for g in G), (m,d)
            balanced.append({"m":m,"total":T,"reflections_each":T//3})
        else:
            rotations=(R,mul(R,R))
            assert d[rotations[0]]==d[rotations[1]] and len(d)==3,(m,d)
            balanced.append({"m":m,"total":T,"identity":d[E],"each_nonidentity_rotation":d[R],"identity_minus_each_rotation":d[E]-d[R]})
    assert dp_counts((2,2,2))=={E:6,R:12,mul(R,R):12}
    assert dp_counts((3,3,3))=={g:58 for g in G}
    nstates,max_witness=minimal_moore_two()
    evidence={
        "marker":"R670_NO_REPEAT_S3_SYMMETRY_AND_MINIMAL_13_STATE_PASS",
        "source":"R667/R668/R669 immutable 2026-11-09 V17 factors; R462 scientific freeze",
        "exact_frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
        "bruteforce_max_length":10,
        "bruteforce_legal_words":1+3*(2**10-1),
        "crosschecked_count_vectors":n_checked,
        "balanced_m":balanced,
        "two_letter_moore_reachable_states":nstates,
        "two_letter_max_shortest_witness_length":max_witness,
        "two_letter_minimality_observer":"full terminal S3 frame plus legal-next-symbol set",
        "review":"AUTHOR_SIDE_UNREVIEWED",
        "native_H_or_V27_V30_scheduler_verified":False
    }
    Path(__file__).with_name('R670_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(evidence,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
