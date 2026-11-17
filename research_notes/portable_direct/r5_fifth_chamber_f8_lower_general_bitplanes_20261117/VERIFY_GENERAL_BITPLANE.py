#!/usr/bin/env python3
"""Exact finite randomized sanity check for general saturated lie-count bitplanes.
Universal statement is proved algebraically in RESEARCH.md, not by these trials.
"""
import random,json
N=256
ALL=(1<<N)-1

def width(f):return (f+1).bit_length()

def bits_from_counts(counts,f):
    planes=[0]*width(f)
    for h,c in enumerate(counts):
        assert 0<=c<=f+1
        for b in range(len(planes)):
            if c & (1<<b):planes[b]|=1<<h
    return planes

def encoded_eliminated(p,f):
    e=ALL
    for b,v in enumerate(p):
        e &= v if ((f+1)>>b)&1 else ALL^v
    return e

def step(p,normal_support,f):
    active=ALL^encoded_eliminated(p,f)
    carry=(ALL^normal_support)&active
    out=[]
    for bit in p:
        out.append(bit^carry)
        carry &= bit
    assert carry==0
    return out

r=random.Random(20261117)
stats={}
for f in range(21):
    checks=0
    for trial in range(500):
        counts=[r.randrange(f+2) for _ in range(N)]
        sup=r.getrandbits(N)
        p=bits_from_counts(counts,f)
        q=step(p,sup,f)
        expected=[c if c==f+1 or (sup>>h)&1 else c+1 for h,c in enumerate(counts)]
        assert q==bits_from_counts(expected,f)
        assert encoded_eliminated(q,f)==sum((1<<h) for h,c in enumerate(expected) if c==f+1)
        checks+=1
    stats[str(f)]={"checks":checks,"bits":width(f)}
output={"status":"PASS_GENERAL_SATURATED_BITPLANES_F0_F20","seed":20261117,"hypotheses":N,"tested_f":[0,20],"total_transitions":sum(v["checks"] for v in stats.values()),"per_f":stats}
print(json.dumps(output,sort_keys=True))
