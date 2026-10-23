#!/usr/bin/env python3
"""Exact five-round sign-reversal checker in the 4-label 3-action BRC model."""
from fractions import Fraction
import json
W = {"0": (1,665,1,333), "2": (333,333,1,333), "3": (1,1,1,997)}
E = ((0,1),(1,2),(1,3),(2,3))
d = tuple(sum(i in e for e in E) for i in range(4))
def delta(c):
    n=sum(c.values())
    if n==0:return Fraction(0)
    A=[1]*4; B=[1]*4
    for a,k in c.items():
        for i in range(4):A[i]*=W[a][i]**k
        for j,(i,h) in enumerate(E):B[j]*=(W[a][i]+W[a][h])**k
    return Fraction(sum(B)-sum(d[i]*A[i] for i in range(4)),1000**n)
def mask_probability(word):
    state={0:Fraction(1)}
    for a in word:
        nxt={}
        for mask,p in state.items():
            for i,w in enumerate(W[a]):
                j=mask|(1<<i)
                nxt[j]=nxt.get(j,Fraction(0))+p*Fraction(w,1000)
        state=nxt
    return sum(p for mask,p in state.items()
               if mask.bit_count()==2 and tuple(i for i in range(4) if mask&(1<<i)) in E)
def verify():
    c={"0":0,"2":3,"3":0};base=delta(c)
    change={}
    for a in W:
        v=dict(c);v[a]+=1
        change[a]=delta(v)-base
        assert change[a]<0
    assert change["0"]==Fraction(-414305561,31250000000)
    assert change["2"]==Fraction(-12398083173,125000000000)
    assert change["3"]==Fraction(-23111249741,125000000000)
    v={"0":0,"2":3,"3":1};after=dict(v);after["0"]+=1
    rise=delta(after)-delta(v)
    assert rise==Fraction(2951045627123,125000000000000)>0
    c={"0":0,"2":0,"3":0};prev=peak=variation=Fraction(0);hist=[]
    for t,a in enumerate("22230",1):
        c[a]+=1;cur=delta(c)
        assert cur==mask_probability("22230"[:t])
        variation+=max(cur-prev,Fraction(0))
        peak=max(peak,cur)
        hist.append((str(cur),str(variation-peak)))
        prev=cur
    assert hist[3][1]=="0" and Fraction(hist[4][1])==rise
    assert Fraction(hist[1][0])>Fraction(hist[4][0])
    return {"schema":"EM_BRC_FIXED_MODEL_LOCAL_NEGATIVITY_REENTRY_V1","word":"22230",
            "base_count":{"0":0,"2":3,"3":0},"base_delta":str(base),
            "all_three_immediate_increments":{a:str(x) for a,x in change.items()},
            "after_3_next_0_positive_increment":str(rise),
            "historical_delta_residual_pairs":hist,"first_residual_growth_at_t":5,
            "arithmetic":"exact Fraction 16-state independent mask",
            "admission":"author_side_unreviewed"}
if __name__=="__main__":
    print(json.dumps(verify(),sort_keys=True,indent=2,ensure_ascii=False))
