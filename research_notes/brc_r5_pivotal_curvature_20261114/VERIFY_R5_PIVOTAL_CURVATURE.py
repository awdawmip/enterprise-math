#!/usr/bin/env python3
"""Exact 28-cut pivotality and interaction census for frozen R5 1D radius-2 observer.
Runs with Python standard library only. Does not assert native X6 or formal Task admission.
"""
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb

SCIENCE_PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def frozen():
    pools={3:set(),12:set(),15:set()}
    n=k=mask=0
    for t in range(1,1<<15):
        bit=t & -t; i=bit.bit_length()-1; mask^=bit
        n+=(1 if mask & bit else -1)*W[i]
        k+=(1 if mask & bit else -1)*K0[i]
        assert mask==(t^(t>>1))
        if n>=3 and k%36==0 and k//36 in pools:pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,v in pools.items() for p in v)
    x=[0]
    for r in sorted(events):x.append(x[-1]+events[r])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]>2]
    blocks=[];a=0
    for j in cuts:blocks.append(tuple(x[a:j+1]));a=j+1
    blocks.append(tuple(x[a:]))
    assert (len(x),len(cuts),len(blocks),x[-1])==(954,28,29,1065)
    assert all(x[i+1]-x[i]==3 for i in cuts)
    return x,cuts,blocks

def min_centers(x,r=2):
    i=j=0;n=len(x);centers=0
    while i<n:
        while j+1<n and x[j+1]<=x[i]+r:j+=1
        e=x[j]+r;centers+=1
        while i<n and x[i]<=e:i+=1
    return centers

def translate(x,cuts,closed):
    closed_at={cuts[c] for c in closed};shift=0;out=[]
    for i,v in enumerate(x):
        out.append(v-shift)
        if i in closed_at:shift+=1
    return out

def interval_cost(blocks):
    d={};B=len(blocks)
    for a in range(B):
        coordinates=[]
        for b in range(a,B):
            coordinates.extend(t-(b-a) for t in blocks[b])
            d[a,b]=min_centers(coordinates)
    return d

def interval_moment(d,B):
    """S[a,b] = sum of minimum centers over all 2^(b-a) internal closure subsets."""
    S={}
    for a in range(B-1,-1,-1):
        for b in range(a,B):
            total=0
            for j in range(a,b+1):
                total+=d[a,j]*(1 if j==b else 2**(b-j-1))
                if j<b:total+=S[j+1,b]
            S[a,b]=total
    return S

def fixed_open_sum(S,segments):
    freedom=sum(b-a for a,b in segments)
    return sum(S[a,b]*2**(freedom-b+a) for a,b in segments)

def by_closure_polynomial(d,B):
    """Exact coefficient count by number of intervals and minimum center count."""
    H=[[Counter() for _ in range(B+1)] for _ in range(B+1)]
    H[0][0][0]=1
    for i in range(1,B+1):
        for s in range(1,i+1):
            for j in range(s-1,i):
                for k,multiplicity in H[j][s-1].items():
                    H[i][s][k+d[j,i-1]]+=multiplicity
    return [H[B][B-q] for q in range(B)]

def brute_min_centers(x,r=2):
    """Independent exhaustive candidate-center solver (small test inputs only)."""
    N=len(x)
    for sz in range(1,N+1):
        for c in combinations(range(N),sz):
            if all(any(abs(x[j]-x[i])<=r for j in c) for i in range(N)):
                return sz
    raise AssertionError('uncovered instance')

def small_exhaustive():
    cases=0;patterns=0;pairs=0
    for B in range(2,5):
        for sizes in product((1,2,3),repeat=B):
            blocks=[];a=0
            for size in sizes:
                blocks.append(tuple(range(a,a+size)));a+=size+2
            x=[y for b in blocks for y in b]
            cuts=[];t=0
            for b in blocks[:-1]:
                t+=len(b);cuts.append(t-1)
            d=interval_cost(blocks);S=interval_moment(d,B)
            all_values={}
            for mask in range(1<<(B-1)):
                closed=tuple(i for i in range(B-1) if mask>>i&1)
                y=translate(x,cuts,closed)
                exact=brute_min_centers(y)
                assert exact==min_centers(y)
                all_values[mask]=exact;patterns+=1
            assert sum(all_values.values())==S[0,B-1]
            for i in range(B-1):
                v=2*fixed_open_sum(S,[(0,i),(i+1,B-1)])-S[0,B-1]
                w=sum(all_values[m]-all_values[m|(1<<i)]
                      for m in all_values if not(m>>i&1))
                assert v==w
                assert all(all_values[m]-all_values[m|(1<<i)] in (0,1)
                           for m in all_values if not(m>>i&1))
            for i,j in combinations(range(B-1),2):
                ai=fixed_open_sum(S,[(0,i),(i+1,B-1)])
                aj=fixed_open_sum(S,[(0,j),(j+1,B-1)])
                aij=fixed_open_sum(S,[(0,i),(i+1,j),(j+1,B-1)])
                v=S[0,B-1]+4*aij-2*ai-2*aj
                w=sum(all_values[m]-all_values[m|(1<<i)]-all_values[m|(1<<j)]+all_values[m|(1<<i)|(1<<j)]
                      for m in all_values if not(m>>i&1 or m>>j&1))
                assert v==w;pairs+=1
            cases+=1
    return cases,patterns,pairs

def result():
    x,cuts,blocks=frozen();B=len(blocks)
    d=interval_cost(blocks);S=interval_moment(d,B)
    overall=S[0,B-1]
    assert overall==13471*2**22
    open1=[fixed_open_sum(S,[(0,i),(i+1,B-1)]) for i in range(B-1)]
    pivots=[2*v-overall for v in open1]
    assert all(0<=v<=2**27 for v in pivots)
    nonzero_interactions=[];signs=Counter()
    interaction_sum=0
    for i,j in combinations(range(B-1),2):
        v=overall+4*fixed_open_sum(S,[(0,i),(i+1,j),(j+1,B-1)])-2*open1[i]-2*open1[j]
        assert abs(v)<=2**26
        signs['zero' if v==0 else 'positive' if v>0 else 'negative']+=1
        interaction_sum+=v
        if v:nonzero_interactions.append({'cuts':[i,j],'effect':str(Fraction(v,2**26))})
    H=by_closure_polynomial(d,B)
    assert all(sum(row.values())==comb(28,q) for q,row in enumerate(H))
    by_q=[sum(k*v for k,v in h.items()) for h in H]
    assert sum(by_q)==overall
    negderivative=sum((28-2*q)*v for q,v in enumerate(by_q))
    assert negderivative==sum(pivots)
    assert Fraction(interaction_sum*2,2**26)==Fraction(-29,8)
    small_cases,small_masks,small_pairs=small_exhaustive()
    direct_pairs=0
    for i in range(28):
        other=[j for j in range(28) if j!=i]
        for q in range(3):
            for closed in combinations(other,q):
                difference=min_centers(translate(x,cuts,closed))-min_centers(translate(x,cuts,closed+(i,)))
                assert difference in (0,1)
                direct_pairs+=1
    assert direct_pairs==10612
    def mean(p):
        return sum(Fraction(v)*p**q*(1-p)**(28-q) for q,v in enumerate(by_q))
    assert mean(Fraction(0))==213 and mean(Fraction(1))==207
    assert mean(Fraction(1,2))==Fraction(13471,64)
    assert Fraction(sum(pivots),2**27)==Fraction(11,2)
    assert by_q[1]-28*by_q[0]==-5
    assert 2*(by_q[2]-27*by_q[1]+comb(28,2)*by_q[0])==2
    assert 28*by_q[28]-by_q[27]==-9
    return {
        'status':'PASS_EXACT_R5_PIVOTAL_AND_CURVATURE',
        'science_pin':SCIENCE_PIN,'scope':'R5 derived integer-event radius-2 observer; not native X6',
        'boundary_count':len(x),'activation_event_count':x[-1],
        'original_blocks':B,'candidate_gap_closures':B-1,
        'unconditional_center_sum':overall,'closure_pattern_count':2**28,
        'one_cut_pivotal_count_by_zero_based_cut':pivots,
        'one_cut_pivotal_denominator':2**27,
        'sum_of_pivotal_probabilities':str(Fraction(sum(pivots),2**27)),
        'second_interaction_denominator_pattern_count':2**26,
        'second_interaction_sign_counts':dict(signs),
        'nonzero_second_interactions':nonzero_interactions,
        'E_D_second_derivative_at_half':str(Fraction(2*interaction_sum,2**26)),
        'E_D_first_derivative_at_zero':str(by_q[1]-28*by_q[0]),
        'E_D_first_derivative_at_one':str(28*by_q[28]-by_q[27]),
        'E_D_second_derivative_at_zero':'2',
        'E_D_first_derivative_at_half':'-11/2',
        'mean_centers_by_p':{str(p):str(mean(p)) for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1))},
        'small_exhaustive_block_cases':small_cases,'small_exhaustive_closure_patterns':small_masks,
        'small_exhaustive_pair_interactions':small_pairs,
        'full_scale_direct_single_cut_pairs_q_other_le_2':direct_pairs,
        'all_q_center_histogram_check':'PASS'
    }

if __name__=='__main__':
    print(json.dumps(result(),ensure_ascii=False,indent=2))
