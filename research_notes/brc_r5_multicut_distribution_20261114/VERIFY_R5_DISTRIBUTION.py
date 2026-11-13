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


from itertools import product

def count_polynomial(cost,B):
    """F[i][s][k]: count of interval partitions on first i blocks with s runs, k centers."""
    F=[[Counter() for _ in range(B+1)] for _ in range(B+1)]
    F[0][0][0]=1
    for i in range(1,B+1):
        for s in range(1,i+1):
            for j in range(s-1,i):
                for v,n in F[j][s-1].items():
                    F[i][s][v+cost[j,i-1]]+=n
    return [{k:n for k,n in sorted(F[B][B-q].items())} for q in range(B)]

def independent_small():
    cases=0
    for B in range(2,6):
        for sizes in product((1,2,3),repeat=B):
            blocks=[]; p=0
            for size in sizes:
                blocks.append(tuple(range(p,p+size)))
                p+=size+2
            x=[v for b in blocks for v in b]
            cuts=[];n=0
            for b in blocks[:-1]:
                n+=len(b); cuts.append(n-1)
            calc=count_polynomial(interval_table(blocks),B)
            brute=[Counter() for q in range(B)]
            for mask in range(1<<(B-1)):
                closed=[c for c in range(B-1) if mask>>c&1]
                brute[len(closed)][cover(translate(x,cuts,closed))[0]]+=1
            assert calc==[{k:n for k,n in sorted(row.items())} for row in brute]
            cases+=1
    return cases

def distribution_main():
    x,cuts,blocks=frozen()
    assert len(x)==954 and len(cuts)==28 and len(blocks)==29
    table=interval_table(blocks)
    F=count_polynomial(table,29)
    total=Counter()
    rows=[]
    enumerated=0
    for q,distribution in enumerate(F):
        assert sum(distribution.values())==comb(28,q)
        assert min(distribution)>=207 and max(distribution)<=213
        for v,n in distribution.items():total[v]+=n
        if q<=4:
            direct=Counter(cover(translate(x,cuts,cs))[0]
                           for cs in combinations(range(28),q))
            assert dict(sorted(direct.items()))==distribution
            enumerated+=sum(direct.values())
        rows.append(dict(closed_cut_count=q,
                         center_count_distribution={str(k):v for k,v in distribution.items()},
                         min_centers=min(distribution),max_centers=max(distribution),
                         patterns=sum(distribution.values())))
    assert enumerated==24158 and sum(total.values())==2**28
    assert F[0]=={213:1} and F[28]=={207:1}
    assert F[11][207]==2 and F[11][213]==782145
    expected=Fraction(sum(k*v for k,v in total.items()),2**28)
    variance=Fraction(sum(k*k*v for k,v in total.items()),2**28)-expected**2
    assert expected==Fraction(13471,64)
    assert variance==Fraction(4115,4096)
    return dict(
        status="PASS_EXACT_R5_ALL_PATTERN_DISTRIBUTION",
        science_pin=PIN,boundary_count=954,activation_events=1065,
        original_blocks=29,candidate_gap_closures=28,pattern_count=2**28,
        exact_interval_costs=len(table),
        distribution={str(k):total[k] for k in sorted(total)},
        expected_centers=dict(numerator=expected.numerator,denominator=expected.denominator),
        variance_centers=dict(numerator=variance.numerator,denominator=variance.denominator),
        direct_enumerated_weight_le_4=enumerated,
        independent_small_block_instances=independent_small(),
        by_closure_count=rows)

if __name__=="__main__":
    print(json.dumps(distribution_main(),ensure_ascii=False,indent=2))
