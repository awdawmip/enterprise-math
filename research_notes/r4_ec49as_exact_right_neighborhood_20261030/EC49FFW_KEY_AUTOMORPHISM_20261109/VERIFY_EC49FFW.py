#!/usr/bin/env python3
"""Exact BRC nine-state transfer counter; word bijection and signature symmetry.
Original frozen EC49FFV operation order a,c,d,e,f,g. Pure integer arithmetic.
Outputs exact word counts, not native X6 prefix-cost optima.
"""
from math import factorial
from functools import lru_cache
import json, argparse
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
LOW=(1,2,4,8)
PI=(0,1,3,2,5,4,7,6,8)
SIGMA=(0,2,1,3,5,4)
def verify_automorphism():
    assert PI[0]==0
    assert all(T[PI[q]][SIGMA[j]]==PI[T[q][j]]
               for q in range(9) for j in range(6))
    assert all(S[PI[q]]=={1:4,4:1,2:8,8:2,16:32,32:16}.get(S[q],S[q])
               for q in range(9))
def exact_formula(h):
    # coefficient t^1 of (4+t+t^-1)^h-(1+t+t^-1)^h
    return sum(factorial(h)//(factorial(k)*factorial(k+1)*factorial(h-2*k-1))
               * (4**(h-2*k-1)-1) for k in range((h-1)//2+1))
def forward(maxh):
    dp={(0,0,False):1}
    rows=[]
    for h in range(1,maxh+1):
        nd={}
        for (q,d,seen),v in dp.items():
            for j in range(6):
                key=(T[q][j],d+(-1 if j==0 else 1 if j==3 else 0),
                     seen or j in (1,2,5))
                nd[key]=nd.get(key,0)+v
        dp=nd
        counts={str(s):sum(v for (q,d,b),v in dp.items()
                        if d==1 and b and S[q]==s) for s in LOW}
        legal=sum(v for (q,d,b),v in dp.items() if d==1 and b)
        assert legal==exact_formula(h)
        assert counts['1']==counts['4'] and counts['2']==counts['8']
        rows.append(dict(h=h,legal_words=legal,low_candidate_words=sum(counts.values()),
                         low_counts_by_signature=counts))
    return rows
@lru_cache(None)
def suffix(n,q):
    """(reachability bit mask, low signature counts, all/viable prefix visits)."""
    if not any(n):
        s=S[q]
        cnt=tuple(int(s==i) for i in LOW)
        return (s if s in LOW else 0,cnt,1,int(s in LOW))
    mask=0;counts=[0]*4;allvis=1;livevis=0
    for j,c in enumerate(n):
        if not c:continue
        nxt=list(n);nxt[j]-=1
        m,cs,at,lt=suffix(tuple(nxt),T[q][j])
        mask|=m;allvis+=at;livevis+=lt
        for k in range(4):counts[k]+=cs[k]
    return (mask,tuple(counts),allvis,livevis+int(mask!=0))
def split_census(h):
    legal_keys=0;live_keys=0;low=0;all_vis=0;live_vis=0
    counts=[0]*4
    for z in range(1,h//2+2):
      for x in range(1,h+2):
       for y in range(1,h+2):
        a=z-1;e=z;d=x+y-h-1;f=h+1-y-2*z;g=h+1-x
        if min(a,e,d,f,g)<0:continue
        legal_keys+=1;seen=False
        for c in range(d+1):
            mask,cs,at,lt=suffix((a,c,d-c,e,f,g),0)
            all_vis+=at;live_vis+=lt
            low+=sum(cs)
            seen|=bool(mask)
            for k in range(4):counts[k]+=cs[k]
        live_keys+=int(seen)
    return dict(h=h,positive_keys=legal_keys,keys_with_low=live_keys,
                low_candidate_words=low,low_counts_by_signature=dict(zip(map(str,LOW),counts)),
                operation_prefix_visits_all=all_vis,operation_prefix_visits_viable=live_vis,
                operation_prefix_visits_filtered=all_vis-live_vis,
                interpretation="per-key/split virtual operation-prefix visits, not unique signed X6 nodes")
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--maxh',type=int,default=32)
    p.add_argument('--split-h',nargs='*',type=int,default=list(range(3,15)))
    p.add_argument('--output',default='')
    a=p.parse_args()
    verify_automorphism()
    forward_rows=forward(a.maxh)
    splits=[split_census(h) for h in a.split_h]
    for r in splits:
        ref=forward_rows[r['h']-1]
        assert r['low_candidate_words']==ref['low_candidate_words']
        assert r['low_counts_by_signature']==ref['low_counts_by_signature']
    # Reproduce immutable EC49FFV values, and EC49FFW's new finite counts.
    expected={9:625050,10:3091460,11:15233900,12:74884944,13:367524430,
              14:1801977660,20:24952444838400,
              32:4981943563654708671936}
    for h,n in expected.items():
        if h<=a.maxh:assert forward_rows[h-1]['low_candidate_words']==n,(h,n)
    print("BRC_AUTOMORPHISM_PASS; exact transfer H1..H%d PASS; %d split crosschecks PASS"
          %(a.maxh,len(splits)))
    for h in (9,10,11,12,13,14,20,32):
        if h<=a.maxh:
            r=forward_rows[h-1]
            print("H%d legal=%d low=%d"%(h,r['legal_words'],r['low_candidate_words']))
    if a.output:
        with open(a.output,'w') as f:
            json.dump({'schema':'EC49FFW_EXACT_WORD_COUNTS_V1',
                       'frozen_science_input':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
                       'forward':forward_rows,'split':splits},f,indent=2)
if __name__=="__main__":main()
