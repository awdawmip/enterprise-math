#!/usr/bin/env python3
"""Independent direct ordered-word enumeration for n<=8; compares DP supports/ranks."""
from collections import defaultdict
from itertools import permutations
from math import factorial
import json, sys
from pathlib import Path
from signed_brc import endpoint_weight, endpoint_multiplicity
from VERIFY_EC49BV import SIX, WP, WM, ID, SWAP, PATTERNS, compositions, attainable_atoms, orbit, rank_of_columns


def brute(n):
    from_dp={}
    from_brute=defaultdict(set)
    word_total=0; weight_total=0
    for k in compositions(n//2,6):
        dp,_=attainable_atoms(k)
        from_dp[k]=dp
        items=[]
        for i,a in enumerate(k):
            items += [i]*a + [i+6]*a
        for word in set(permutations(items)):
            word_total+=1
            if sum(1 if ch==0 else 0 for ch in word)<0:
                raise AssertionError
            mask=0
            for j in range(n-1):
                if word[j:j+2]==(0,1): mask|=1|8  # id A, swap B
                if word[j:j+2]==(1,0): mask|=2|4  # id B, swap A
            from_brute[k].add((word[0],word[-1],mask))
            weight_total+=orbit(k,(ID,),WP,WM)[0]
    assert from_brute==from_dp,[(k,len(from_brute[k]),len(from_dp[k])) for k in from_dp if from_brute[k]!=from_dp[k]]
    by_atom=defaultdict(list)
    for k, atoms in from_brute.items():
        for a in atoms:by_atom[a].append(k)
    fixed_rank=sum(rank_of_columns([orbit(k,(ID,SWAP),WP,WM) for k in ks]) for ks in by_atom.values())
    assert word_total==endpoint_multiplicity(n,SIX)
    assert weight_total==endpoint_weight(n,SIX,WP,WM)
    return {"n":n,"words_directly_enumerated":word_total,"classes":len(by_atom),
      "fixed_rank":fixed_rank,"weight":str(weight_total),"all_dp_signature_sets_identical":True}

if __name__=='__main__':
    lengths=[int(x) for x in sys.argv[1:]] or [4,6,8]
    out={"schema":"EC49BV_BRUTE_CROSSCHECK_V1","models":[brute(n) for n in lengths]}
    dst=Path(__file__).with_name('CROSSCHECK_REPORT_EC49BV.json')
    dst.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))
