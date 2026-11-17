#!/usr/bin/env python3
"""Exact two-read predecessor-fiber validation of the offset family."""
import json

def valid(p,c):
    N=1<<p
    assert c%2==1 and c<N//2
    q1,q2=N-1,N-c
    # all q2 collision pairs have terminals (u,N-c+u), 0<=u<c
    for u in range(c):
        w=N-c+u
        A={u%q1}|{(u^(1<<i))%q1 for i in range(p)}
        B={w%q1}|{(w^(1<<i))%q1 for i in range(p)}
        if A&B:return False,(u,w,sorted(A&B))
    return True,None

results=[]
for p in range(6,17):
    cases=0
    for c in range(3,min(128,1<<(p-1)),2):
        L=(c-1).bit_length()
        if p<L+3: continue
        expected=((c-1).bit_count()>=3)
        actual,witness=valid(p,c)
        assert actual==expected,(p,c,witness)
        cases+=1
    results.append({'p':p,'all_checked':cases})
assert valid(6,15)[0]
print(json.dumps({'schema':'PREFIX860_OFFSET_HAMMING_V1','cases':results,'p6_c15_extension':True,'assertions':'ALL_EXACT_ASSERTIONS_PASSED'},separators=(',',':')))
