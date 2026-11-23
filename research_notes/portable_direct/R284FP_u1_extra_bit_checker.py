#!/usr/bin/env python3
"""R284FP: q=2,u=1 exact width-15 first-bit obstruction for the four-code cycle."""
from itertools import combinations
from math import comb
import json

Q, U, N = 2, 1, 15
PAIRS = ((0,1),(1,2),(2,3),(3,0),(0,2),(1,3))
PAT = {}
for p in range(1,8):
    bits=(0,p&1,(p>>1)&1,(p>>2)&1)
    changed=tuple(i for i in range(4) if bits[i]!=bits[(i-1)%4])
    last=tuple(next((i-t)%4 for t in range(4) if (i-t)%4 in changed) for i in range(4))
    PAT[p]=(bits,last)

def histograms(n):
    for divs in combinations(range(n+6),6):
        z=(-1,)+divs+(n+6,)
        yield tuple(z[i+1]-z[i]-1 for i in range(7))

def cut_options(i,j):
    edges=[(p-1,PAT[p][1][i],4+PAT[p][1][j]) for p in range(1,8)
           if PAT[p][0][i]!=PAT[p][0][j]]
    options={}
    for mask in range(1,256):
        cols=tuple(p for p,l,r in edges if (mask>>l)&1 and (mask>>r)&1)
        if cols:
            options[cols]=min(options.get(cols,9),mask.bit_count())
    return [(cols,Q*vertices+2*U+1) for cols,vertices in options.items()]

def viable_histogram(hist,cutsets):
    distances=(2*Q+4*U+1,)*4+(2*(Q+U)+1,)*2
    for (i,j),need,opts in zip(PAIRS,distances,cutsets):
        if sum(hist[p-1] for p in range(1,8) if PAT[p][0][i]!=PAT[p][0][j])<need:
            return False
        if not any(sum(hist[p] for p in cols)>=threshold for cols,threshold in opts):
            return False
    return True

def make_words(hist):
    patterns=[p for p,k in enumerate(hist,1) for _ in range(k)]
    return tuple(0 if phase==0 else sum(((p>>(phase-1))&1)<<k
                 for k,p in enumerate(patterns)) for phase in range(4))

def stable_states(words,phase):
    groups=[[] for _ in range(4)]
    for k in range(N):
        for age in range(1,5):
            edge=(phase-age)%4
            if (words[edge]^words[(edge+1)%4])>>k&1:
                groups[edge].append(k)
                break
        else:
            raise AssertionError("constant coordinate")
    masks=[0]
    for group in groups:
        options=[sum(1<<k for k in subset)
                 for r in range(min(Q,len(group))+1)
                 for subset in combinations(group,r)]
        masks=[a|b for a in masks for b in options]
    return {words[phase]^mask for mask in masks}

def mandatory_success_masks(states):
    forced_y=bytearray(1<<N)
    for phase,physical_set in enumerate(states):
        for s in physical_set:
            forced_y[s]|=1<<phase
            for k in range(N):
                forced_y[s^(1<<k)]|=1<<phase
    assert all(mask.bit_count()<=1 for mask in forced_y), "stable collision"
    forced_x=bytearray(forced_y)
    for x in range(1<<N):
        for k in range(N):
            forced_x[x]|=forced_y[x^(1<<k)]
    return forced_y,forced_x

def first_step_witnesses(words,states,forced_x):
    witnesses=[]
    for phase in range(4):
        j=(phase+1)%4
        old,new=1<<phase,1<<j
        allowed=old|new
        change_bits=[k for k in range(N) if (words[phase]^words[j])>>k&1]
        for bit in change_bits:
            mask=1<<bit
            target=words[j]&mask
            witness=None
            for s in sorted(states[phase]):
                x=(s&~mask)|target  # First attempt succeeds; no omissions.
                forced=forced_x[x]
                if forced & ~allowed or forced==allowed:
                    witness=(phase,bit,s,x,forced)
                    break
            assert witness is not None, ("possible first bit",phase,bit)
            witnesses.append(witness)
    return witnesses

def main():
    cuts=[cut_options(*pair) for pair in PAIRS]
    viable=[hist for hist in histograms(N) if viable_histogram(hist,cuts)]
    assert set(viable)=={
      (0,0,5,0,4,6,0),(0,0,6,0,3,6,0),(0,0,6,0,4,5,0)
    } and len(viable)==3
    certificates=[]
    for hist in viable:
        words=make_words(hist)
        states=[stable_states(words,i) for i in range(4)]
        _,forced_x=mandatory_success_masks(states)
        witnesses=first_step_witnesses(words,states,forced_x)
        expected=sum((words[i]^words[(i+1)%4]).bit_count() for i in range(4))
        assert len(witnesses)==expected
        certificates.append({"histogram":hist,"words":words,
          "stable_sizes":[len(x) for x in states],
          "tested_first_bits":len(witnesses),
          "first_step_witnesses":witnesses})
    report={"parameters":{"q":Q,"u":U,"n":N},
      "histograms_exhausted":comb(N+6,6),
      "cut_eligible_histograms":len(viable),
      "first_bit_choices_excluded":sum(x["tested_first_bits"] for x in certificates),
      "result":"all width-15 candidates rejected for q=2,u=1",
      "certificates":certificates}
    assert report["first_bit_choices_excluded"]==112
    print(json.dumps(report,sort_keys=True))

if __name__=="__main__":
    main()
