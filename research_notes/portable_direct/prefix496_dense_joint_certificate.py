#!/usr/bin/env python3
"""Exact integer certificate for PREFIX-496 dense joint BRC/KMP/source ranking.
Native X6 restriction: sixth axis unoccupied; five axes (a,A,b,B,c,C,d,D,e,E).
Observer: (n,y[5],V,W,q,t), first-source tag N/B/C.
No floating point; this certificate uses Python integers, tuple/set and integer combinatorics.
"""
from collections import defaultdict, Counter
from math import comb, ceil, log2
import json

LETTERS='aAbBcCdDeE'
COEFF_V=(0,1,0,2,1)
COEFF_W=(0,0,1,0,1)
GATES=('aab','aba')
MAX_N=9

def q_of_word(g,w):
    return max(j for j in range(len(g)+1) if w.endswith(g[:j]))

def t_of_word(w):
    for c in w:
        if c in 'bB':return 'B'
        if c in 'cC':return 'C'
    return 'N'

def direct_obs(w,g):
    signed=[]; p=[]
    for c in 'abcde':
        a=w.count(c); b=w.count(c.upper());signed.append(a-b);p.append(min(a,b))
    return tuple(signed)+(p[1]+2*p[3]+p[4],p[2]+p[4],q_of_word(g,w),t_of_word(w))

def advance(state,ch,g):
    y=state[:5];V,W,q,t=state[5:]
    axis=LETTERS.index(ch)//2;eps=1 if ch.islower() else -1
    delta=int(eps*y[axis]<0)
    ny=list(y);ny[axis]+=eps
    suffix=g[:q]+ch
    nq=max(j for j in range(len(g)+1) if suffix.endswith(g[:j]))
    nt=t if t!='N' else ('B' if ch in 'bB' else 'C' if ch in 'cC' else 'N')
    return tuple(ny)+(V+COEFF_V[axis]*delta,W+COEFF_W[axis]*delta,nq,nt)

def total_base_fibers(n):
    return sum(c*comb(n-j+7,7) for j,c in enumerate([1,2,3,4,2]) if n-j>=0)

def build(g):
    s={(0,0,0,0,0,0,0,0,'N')}
    summary=[];checkpoints={}
    for n in range(MAX_N+1):
        groups=defaultdict(set)
        for x in s:
            groups[x[:7]].add(x[7:])
        base_sorted=sorted(groups)
        assert len(base_sorted)==total_base_fibers(n),(g,n,len(base_sorted),total_base_fibers(n))
        k_hist=dict(sorted(Counter(map(len,groups.values())).items()))
        qonly={(x[:7],x[7]) for x in s}
        rank={};i=0
        for b in base_sorted:
            for c in sorted(groups[b]):
                rank[b+c]=i;i+=1
        assert len(rank)==len(s)==i
        assert sorted(rank.values())==list(range(len(s)))
        # demonstrate exactly invertible per-fiber and global ranking
        inverse=[None]*len(s)
        for x,j in rank.items():
            assert inverse[j] is None
            inverse[j]=x
        assert set(inverse)==s
        raw_bits=(11 if g=='aab' else 10)*len(groups)
        fixed_radix_bits=(raw_bits-1).bit_length() if raw_bits>1 else 0
        dense_bits=(len(s)-1).bit_length() if len(s)>1 else 0
        summary.append({'n':n,'base_fibers':len(groups),'q_only_fibers':len(qonly),'joint_states':len(s),'support_sizes':k_hist,
                        'fixed_radix_capacity':raw_bits,'fixed_radix_bits':fixed_radix_bits,
                        'dense_bits':dense_bits,'bits_saved':fixed_radix_bits-dense_bits,
                        'control_occupancy_ratio':f'{len(s)}/{raw_bits}'})
        if n in (4,8,9):
            checkpoints[n]={'source_masks':dict(sorted(Counter(t for x in s for t in [x[-1]]).items())),
                            'kmp_counts':dict(sorted(Counter(x[-2] for x in s).items()))}
        if n<MAX_N:
            s={advance(x,ch,g) for x in s for ch in LETTERS}
    return summary,checkpoints

def independent_words_test():
    out={}
    for g in GATES:
        dynamic={(0,0,0,0,0,0,0,0,'N')}
        words=['']
        for n in range(5):
            actual={direct_obs(w,g) for w in words}
            assert actual==dynamic,(g,n,len(actual),len(dynamic),list(actual^dynamic)[:2])
            words=[w+c for w in words for c in LETTERS]
            dynamic={advance(x,c,g) for x in dynamic for c in LETTERS}
        out[g]={'ordered_words_through_n4':11111,'checked_each_length':list(range(5))}
    return out

if __name__=='__main__':
    summaries={};checkpoints={}
    for g in GATES:
        summaries[g],checkpoints[g]=build(g)
    assert summaries['aab'][8]['joint_states']==60590
    assert summaries['aba'][8]['joint_states']==60550
    assert summaries['aab'][8]['base_fibers']==22275
    assert summaries['aab'][8]['q_only_fibers']==39886
    assert summaries['aba'][8]['q_only_fibers']==39887
    independent=independent_words_test()
    obj={
      'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
      'model':'X6 signed five-axis occupancy subfamily; sixth native axis held at zero',
      'observer':'(n,y_a,y_b,y_c,y_d,y_e,V,W,q,t)',
      'max_n':MAX_N,
      'gates':summaries,
      'source_state_checkpoints':checkpoints,
      'independent_ordered_path_check':independent,
      'status':'ALL_CHECKS_PASS',
    }
    print(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True))
