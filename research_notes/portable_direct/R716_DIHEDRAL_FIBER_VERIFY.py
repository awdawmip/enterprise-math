#!/usr/bin/env python3
"""Exact integer validation of phase-pair/dihedral BRC fibres, no external dependencies."""
from itertools import combinations
from collections import Counter
from math import comb
import json

V = tuple(combinations(range(1,6),2))
ADJ = {u: tuple(v for v in V if not set(u)&set(v)) for u in V}
E = {v: v[1]-v[0]-1 for v in V}

def word_profile(word):
    return tuple(sum(a<=t<b for a,b in word) for t in range(1,5))

def formula(m):
    k=(m-5)//2
    profiles=Counter()
    for r in range(k+1):
        for s in range(k-r+1):
            t=k-r-s
            D=(2+r+s,2+t,2+s,2+r+t)
            profiles[D]=8*m*comb(r+s,s)*comb(r+t,t)
    return profiles

def enumerate_opt(m):
    out=[]
    def rec(word,ex):
        if len(word)==m:
            if ex==3 and word[0] in ADJ[word[-1]]:
                out.append(tuple(word))
            return
        for v in ADJ[word[-1]]:
            if ex+E[v]<=3: rec(word+[v],ex+E[v])
    for v in V:
        if E[v]<=3: rec([v],E[v])
    return out

def canonical(w):
    n=len(w)
    return min(tuple(w[i:]+w[:i]) for i in range(n))  # not used

def orbit(w):
    n=len(w)
    return {w[i:]+w[:i] for i in range(n)} | {w[::-1][i:]+w[::-1][:i] for i in range(n)}

def exact_dp(m):
    # Trace of weighted graph transfer, tracking excess and four-boundary D
    totals=Counter()
    for u in V:
        frontier={(u,E[u], tuple(int(a<=t<b) for t in range(1,5) for a,b in [u])):1}
        for i in range(1,m):
            nxt=Counter()
            for (last,ex,d),ct in frontier.items():
                for v in ADJ[last]:
                    ex2=ex+E[v]
                    if ex2>3:continue
                    d2=tuple(d[t]+int(v[0]<=t+1<v[1]) for t in range(4))
                    nxt[(v,ex2,d2)]+=ct
            frontier=nxt
        for (last,ex,d),ct in frontier.items():
            if ex==3 and u in ADJ[last]:totals[d]+=ct
    return totals

def main():
    tests=[]
    for m in (5,7,9,11):
        W=enumerate_opt(m)
        assert Counter(map(word_profile,W))==formula(m)
        classes=set()
        for w in W:
            orb=orbit(w)
            assert len(orb)==2*m, (m,w,len(orb))
            classes.add(min(orb))
        assert len(classes)==len(W)//(2*m)
        peak=(m+6)//4  # ceil((m+3)/4)
        joint=sum(1 for w in W if max(word_profile(w))==peak)
        n=(m-3)//4
        assert joint == (8*m if m%4==1 else 8*m*(2+n*n))
        tests.append({'m':m,'rooted_area':len(W),'bracelets_area':len(classes),'rooted_joint':joint,'bracelets_joint':joint//(2*m),'all_orbits_size':2*m})
    for m in (13,15,17):
        P=exact_dp(m)
        assert P==formula(m), (m,P,formula(m))
        peak=(m+6)//4
        joint=sum(c for d,c in P.items() if max(d)==peak)
        n=(m-3)//4
        assert joint==(8*m if m%4==1 else 8*m*(2+n*n))
        tests.append({'m':m,'rooted_area':sum(P.values()),'bracelets_area':sum(P.values())//(2*m),'rooted_joint':joint,'bracelets_joint':joint//(2*m),'method':'exact_DP'})
    res={'flag':'R716_DIHEDRAL_FIBER_EXACT_PASS','hypotheses':'odd m>=5, area m+3, labelled cyclic phase-pair edge words; dihedral action by edge re-index/reversal','tests':tests,'scope':'finite checks m=5..17 odd; universal theorem requires supplied group-action proof'}
    print(json.dumps(res,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
