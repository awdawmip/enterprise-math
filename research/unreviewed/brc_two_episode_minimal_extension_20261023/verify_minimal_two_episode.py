#!/usr/bin/env python3
"""Exact BRC four-label occupancy witness, two independent algorithms.
Author-only result, not a native X6 theorem or a formal Source Result.
Run: python verify_minimal_two_episode.py
"""
from fractions import Fraction as F
from itertools import product
import json

PAIRS = ((0,1),(1,2),(1,3),(2,3))
MASKS = tuple((1<<i)|(1<<j) for i,j in PAIRS)

CASES = (
    ("sparse_interior", F(3,4), (F(0),F(1,4),F(0),F(3,4)),
     "0N20NN", (F(0),F(29,48),F(5,9),F(481,864),F(239,432),F(7657,13824)),
     (F(1,864),F(1,1536)), 4),
    ("full_support_new_action",F(19,20),
     (F(1,1000),F(1,1000),F(1,1000),F(997,1000)),
     "0N2020",
     (F(0),F(13333,20000),F(32987,60000),F(1319063,2160000),
      F(541979,1296000),F(813588041,1944000000)),
     (F(131531,2160000),F(619541,1944000000)),22),
)

def laws(z,n):
    result = {
        "0":(F(0),(1+z)/3,(1-z)/3,F(1,3)),
        "2":(F(1,3),F(1,3),F(0),F(1,3)),
        "N":n,
    }
    assert all(sum(q,F(0))==1 and min(q)>=0 for q in result.values())
    return result

def pair_formula(word,law):
    ans=F(0)
    for i,j in PAIRS:
        a=b=c=F(1)
        for char in word:
            q=law[char]
            a*=q[i]+q[j]
            b*=q[i]
            c*=q[j]
        ans+=a-b-c
    return ans

def mask_dp(word,law):
    m=[F(0)]*16
    m[0]=F(1)
    for char in word:
        nxt=[F(0)]*16
        for mask,mass in enumerate(m):
            if mass:
                for k,p in enumerate(law[char]):
                    if p:nxt[mask|(1<<k)]+=mass*p
        m=nxt
    assert sum(m,F(0))==1
    return sum((m[t] for t in MASKS),F(0))

def trace(word,law,fn):
    dprev=s=m=rprev=F(0)
    vals=[]
    growth=[]
    for t in range(1,len(word)+1):
        d=fn(word[:t],law)
        s+=max(F(0),d-dprev)
        m=max(m,d)
        r=s-m
        assert r>=rprev>=0
        dr=r-rprev
        vals.append((d,d-dprev,m,r,dr))
        if dr>0:growth.append(t)
        dprev,rprev=d,r
    return vals,tuple(growth)

def has_second(growth):
    return any(b>a+1 for a,b in zip(growth,growth[1:]))

def run():
    all_results={}
    for name,z,n,w,expected_ds,expected_drs,expected_count in CASES:
        law=laws(z,n)
        exact,growth=trace(w,law,pair_formula)
        independent,growth2=trace(w,law,mask_dp)
        assert exact==independent and growth==growth2==(4,6)
        assert tuple(row[0] for row in exact)==expected_ds
        assert (exact[3][4],exact[5][4])==expected_drs
        assert exact[4][4]==0
        counts={}
        crosschecks=0
        witnesses=[]
        for length in range(1,7):
            hit=0
            for tup in product("02N",repeat=length):
                word="".join(tup)
                x,g=trace(word,law,pair_formula)
                y,h=trace(word,law,mask_dp)
                assert (x,g)==(y,h)
                crosschecks+=1
                if has_second(g):
                    hit+=1
                    if length==6:witnesses.append(word)
            counts[str(length)]=hit
        assert crosschecks==1092
        assert all(counts[str(k)]==0 for k in range(1,6))
        assert counts["6"]==expected_count and w in witnesses
        all_results[name]={
            "parameter_z":str(z),
            "new_action":[str(x) for x in n],
            "word":w,
            "exact_delta_prefixes":[str(row[0]) for row in exact],
            "exact_delta_increments":[str(row[1]) for row in exact],
            "exact_residual_increments":[str(row[4]) for row in exact],
            "strict_growth_times":list(growth),
            "two_episode_words_by_length":counts,
            "length6_two_episode_words":witnesses,
            "independent_exact_word_crosschecks":crosschecks,
        }
    all_results["scope"]={
        "arithmetic":"Fraction exact rational",
        "algorithms":["good-pair product inclusion/exclusion","16 occupied-mask DP"],
        "total_full_word_crosschecks":2184,
        "claim":"first separated episodes at sharp length six in an extended auxiliary action alphabet",
        "admission":"AUTHOR_UNREVIEWED_NOT_P000_NATIVE_X6",
    }
    print(json.dumps(all_results,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=="__main__":
    run()
