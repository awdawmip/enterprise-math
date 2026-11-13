#!/usr/bin/env python3
"""Frozen R5, radius-2 integer-event centers, all 2**28 gap-closure patterns.
No non-standard dependencies. This is an auxiliary 1D observer, not native X6.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def frozen():
    pools = {3:set(),12:set(),15:set()}
    n = k = mask = 0
    for t in range(1, 1<<15):
        bit = t & -t
        i = bit.bit_length()-1
        mask ^= bit
        n += (1 if mask & bit else -1)*W[i]
        k += (1 if mask & bit else -1)*K0[i]
        assert mask == (t ^ (t>>1))
        if n >= 3 and k % 36 == 0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    events=Counter(Fraction(p,q) for q,vals in pools.items() for p in vals)
    x=[0]
    for r in sorted(events):
        x.append(x[-1]+events[r])
    assert len(events)==953 and len(x)==954 and x[-1]==1065
    boundaries=[i for i in range(len(x)-1) if x[i+1]-x[i]>2]
    assert len(boundaries)==28 and all(x[i+1]-x[i]==3 for i in boundaries)
    blocks=[]; start=0
    for i in boundaries:
        blocks.append(tuple(x[start:i+1]));start=i+1
    blocks.append(tuple(x[start:]))
    return x,boundaries,blocks

def cover(points, R=2):
    """Greedy exact minimum candidate-center count, with index witness."""
    i=j=0; chosen=[];N=len(points)
    while i<N:
        while j+1<N and points[j+1]<=points[i]+R:
            j+=1
        chosen.append(j)
        end=points[j]+R
        while i<N and points[i]<=end:
            i+=1
    return len(chosen),chosen

def translate(x,cuts,closed):
    lowers=set(cuts[c] for c in closed)
    shift=0;ans=[]
    for i,y in enumerate(x):
        ans.append(y-shift)
        if i in lowers: shift+=1
    return ans

def interval_table(blocks):
    d={}
    for left in range(len(blocks)):
        points=[]
        for right in range(left,len(blocks)):
            points.extend(t-(right-left) for t in blocks[right])
            d[left,right]=cover(points)[0]
    return d

def optimize(blocks,mode):
    B=len(blocks);cost=interval_table(blocks)
    scores=[[None]*(B+1) for _ in range(B+1)]
    counts=[[0]*(B+1) for _ in range(B+1)]
    back=[[None]*(B+1) for _ in range(B+1)]
    scores[0][0]=0;counts[0][0]=1
    for end in range(1,B+1):
        for segments in range(1,end+1):
            options=[(scores[start][segments-1]+cost[start,end-1],start)
                for start in range(segments-1,end)
                if scores[start][segments-1] is not None]
            best=(min if mode=='min' else max)(v for v,_ in options)
            tied=[j for v,j in options if v==best]
            scores[end][segments]=best
            counts[end][segments]=sum(counts[j][segments-1] for j in tied)
            back[end][segments]=tied[0]
    def witness(q):
        end=B;segments=B-q;runs=[]
        while segments:
            start=back[end][segments]
            runs.append((start,end-1))
            end=start;segments-=1
        return sorted(c for a,b in runs for c in range(a,b))
    return scores,counts,witness

def main():
    x,cuts,blocks=frozen();B=len(blocks)
    assert B==29 and cover(x)[0]==213
    f,nf,wmin=optimize(blocks,'min')
    g,ng,wmax=optimize(blocks,'max')
    rows=[]
    for q in range(B):
        s=B-q;mn=f[B][s];mx=g[B][s]
        mw=wmin(q);xw=translate(x,cuts,mw)
        assert len(mw)==q and cover(xw)[0]==mn
        assert cover(translate(x,cuts,wmax(q)))[0]==mx
        assert 0<nf[B][s]<=comb(B-1,q) and 0<ng[B][s]<=comb(B-1,q)
        rows.append(dict(closed_cut_count=q,min_centers=mn,
                         number_of_minimizing_patterns=nf[B][s],
                         max_centers=mx,
                         number_of_maximizing_patterns=ng[B][s],
                         minimizing_cuts=mw))
    # Exhaustively compare every bit pattern of weight <= 4 with the transfer DP.
    checked=0
    for q in range(5):
        values=Counter(cover(translate(x,cuts,c))[0]
                       for c in combinations(range(28),q))
        row=rows[q]
        assert len(values)>0 and sum(values.values())==comb(28,q)
        assert min(values)==row['min_centers'] and max(values)==row['max_centers']
        assert values[min(values)]==row['number_of_minimizing_patterns']
        assert values[max(values)]==row['number_of_maximizing_patterns']
        checked+=sum(values.values())
    # Independent subset enumeration on short sequences tests the covering oracle.
    small=0
    for n in range(1,9):
        for tail in combinations(range(1,11),n-1):
            z=(0,)+tail
            brute=min(k for k in range(1,n+1)
                if any(all(min(abs(z[i]-z[j]) for j in cs)<=2
                           for i in range(n))
                       for cs in combinations(range(n),k)))
            assert brute==cover(z)[0]
            small+=1
    singles={c:cover(translate(x,cuts,(c,)))[0] for c in range(28)}
    interaction=[];two=Counter()
    for c,d in combinations(range(28),2):
        actual=cover(translate(x,cuts,(c,d)))[0]
        two[actual]+=1
        predicted=singles[c]+singles[d]-213
        if actual!=predicted:
            interaction.append(dict(cuts=[c,d],predicted_independent=predicted,actual=actual))
        assert d==c+1 or actual==predicted
    assert two=={211:8,212:118,213:252}
    assert interaction==[
        dict(cuts=[5,6],predicted_independent=211,actual=212),
        dict(cuts=[8,9],predicted_independent=211,actual=212),
        dict(cuts=[12,13],predicted_independent=213,actual=212)]
    assert rows[0]['min_centers']==213 and rows[11]['min_centers']==207
    assert rows[11]['number_of_minimizing_patterns']==2
    assert rows[28]['min_centers']==207
    return dict(status='PASS_EXACT_MULTI_CUT_DOMINATION',science_pin=PIN,
        boundary_count=954,activation_events=1065,original_blocks=29,
        candidate_gap_closures=28,all_pattern_count=1<<28,
        exact_transfer_profiles=rows,
        directly_enumerated_patterns=checked,
        brute_force_short_sequences=small,
        two_cut_histogram=dict(sorted(two.items())),
        nonadditive_pairs=interaction)

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
