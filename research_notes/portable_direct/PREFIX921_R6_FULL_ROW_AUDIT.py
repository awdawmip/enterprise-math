#!/usr/bin/env python3
"""Audit exact named-XOR witnesses and row labels emitted by PREFIX921 C++ at b=524287."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json,sys

N=1<<32; B=524287
EXACT_GAPS={518271,521279,522783,523535,523911,524099,524193}

def check(path):
    counts=Counter();seen_gaps=[];expected=262145;headline=None
    for line in Path(path).read_text(encoding="ascii").splitlines():
        if line.startswith("W "):
            a,b,t,x,y,i,j=map(int,line[2:].split(","))
            assert (a,b)==(expected,B) and 1<=t<=3 and 0<=x<y<N
            assert (i,j)==(-1,-1) if t==1 else (i>=0 and j==-1) if t==2 else (i>=0 and j>=0)
            assert -1<=i<32 and -1<=j<32
            u=x if i==-1 else (x^(1<<i))
            v=y if j==-1 else (y^(1<<j))
            assert (y-x)%a==0 and (v-u)%b==0
            counts[t]+=1
            expected+=2
        elif line.startswith("NO_DISTINCT_START_COLLISION "):
            a,b=map(int,line.split()[1].split(","))
            assert (a,b)==(expected,B)
            seen_gaps.append(a);expected+=2
        elif line.startswith("TOTAL "):
            assert headline is None
            headline=line
        else:raise AssertionError("Unexpected row record: "+line[:100])
    assert expected==524289
    assert set(seen_gaps)==EXACT_GAPS and len(seen_gaps)==7
    assert (counts[1],counts[2],counts[3])==(1,48723,82341)
    return {"schema":"PREFIX921_R6_ROW_AUDIT_V1","b":B,"rows":131072,
      "directly_verified_different_start_witnesses":sum(counts.values()),
      "zero_zero":counts[1],"zero_flip":counts[2],"two_flip":counts[3],
      "gap_free_a":sorted(seen_gaps),"invalid_witnesses":0,
      "output_sha256":sha256(Path(path).read_bytes()).hexdigest(),
      "generator_summary":headline}
if __name__=="__main__":
    print(json.dumps(check(sys.argv[1]),indent=2))
