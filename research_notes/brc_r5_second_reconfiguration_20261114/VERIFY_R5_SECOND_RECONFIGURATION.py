#!/usr/bin/env python3
"""Frozen R5: exact 214->215 optimal-center reconfiguration.

Integers/Fraction only. Dynamic programming for optimal center path languages,
then epsilon-product automata for maximum intersection, with independent small
finite exhaustive crosschecks. Requires only Python >=3.10 standard library.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json

PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def make_r5():
    pools={3:set(),12:set(),15:set()}
    mask=n=k=0
    for step in range(1,1<<15):
        bit=step&-step;i=bit.bit_length()-1;mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i];k+=sign*K0[i]
        assert mask==(step^(step>>1))
        if n>=3 and k%36==0 and k//36 in pools:pools[k//36].add(n)
    assert tuple(len(pools[q]) for q in (3,12,15))==(538,298,229)
    walls=Counter(Fraction(p,q) for q,values in pools.items() for p in values)
    assert len(walls)==953 and Counter(walls.values())=={1:869,2:56,3:28}
    x=[0]
    for v in sorted(walls):x.append(x[-1]+walls[v])
    assert len(x)==954 and x[-1]==1065
    blocks=[];start=0
    for i in range(1,len(x)):
        if x[i]-x[i-1]>2:blocks.append(x[start:i]);start=i
    blocks.append(x[start:])
    assert len(blocks)==29
    return x,blocks

def local_dp(xs):
    """Min-plus center DAG; row[t-1][q]=(best prefix cost, tied count)."""
    N=len(xs)
    incoming=[[] for _ in xs]
    for p in range(N):
        for q in range(p+1,min(N,p+6)):
            vals=[min(xs[b]-xs[p],xs[q]-xs[b]) for b in range(p+1,q)]
            if all(v<=2 for v in vals):incoming[q].append((p,sum(vals)))
    row=[None]*N
    for p in range(N):
        if xs[p]-xs[0]<=2:row[p]=(sum(xs[p]-xs[b] for b in range(p)),1)
    rows=[row];answers={}
    for budget in range(1,N+1):
        ends=[(p,v[0]+sum(xs[i]-xs[p] for i in range(p+1,N)),v[1])
              for p,v in enumerate(row) if v is not None and xs[-1]-xs[p]<=2]
        if ends:
            best=min(v for _,v,_ in ends)
            answers[budget]=(best,sum(cnt for _,v,cnt in ends if v==best))
        if budget==N:break
        nxt=[None]*N
        for q,edges in enumerate(incoming):
            choices=[(row[p][0]+w,row[p][1]) for p,w in edges if row[p] is not None]
            if choices:
                best=min(v for v,_ in choices)
                nxt[q]=(best,sum(cnt for v,cnt in choices if v==best))
        row=nxt;rows.append(row)
    return answers,rows,incoming

def optimal_dag(xs,summary,budget):
    """All prefixes in optimal center paths, including exact start and terminal conditions."""
    answers,rows,incoming=summary;N=len(xs)
    best=answers[budget][0]
    good=[set() for _ in range(budget+1)]
    for q,entry in enumerate(rows[budget-1]):
        if entry and xs[-1]-xs[q]<=2 and entry[0]+sum(xs[i]-xs[q] for i in range(q+1,N))==best:
            good[budget].add(q)
    for t in range(budget,1,-1):
        for q in good[t]:
            val=rows[t-1][q][0]
            for p,w in incoming[q]:
                if rows[t-2][p] and rows[t-2][p][0]+w==val:
                    good[t-1].add(p)
    nxt={(0,-1):tuple(sorted(good[1]))}
    for t in range(1,budget):
        for p in good[t]:nxt[(t,p)]=[]
        for q in good[t+1]:
            val=rows[t][q][0]
            for p,w in incoming[q]:
                if p in good[t] and rows[t-1][p][0]+w==val:
                    nxt[t,p].append(q)
    for key,val in nxt.items():nxt[key]=tuple(sorted(val))
    return nxt,good

def find_pair(xs,summary,k,r):
    """Find optimal paths with <=r deletions old-only and <=r+1 new-only.
    Synchronized equal symbols count a common increasing subsequence. Existence
    at minimal r yields the exact cardinality of S\\T.
    """
    old,go=optimal_dag(xs,summary,k);new,gn=optimal_dag(xs,summary,k+1)
    count=[0]
    @lru_cache(None)
    def visit(i,p,j,q,d,a):
        count[0]+=1
        if i==k and j==k+1:return () if d==r and a==r+1 else None
        if d>r or a>r+1:return None
        if i<k and j<k+1:
            for c in sorted(set(old.get((i,p),()))&set(new.get((j,q),()))):
                tail=visit(i+1,c,j+1,c,d,a)
                if tail is not None:return (('shared',c),)+tail
        if d<r and i<k:
            for c in old.get((i,p),()):
                tail=visit(i+1,c,j,q,d+1,a)
                if tail is not None:return (('old',c),)+tail
        if a<r+1 and j<k+1:
            for c in new.get((j,q),()):
                tail=visit(i,p,j+1,c,d,a+1)
                if tail is not None:return (('new',c),)+tail
        return None
    aligned=visit(0,-1,0,-1,0,0)
    if aligned is None:return None,count[0]
    S=tuple(v for tag,v in aligned if tag!='new')
    T=tuple(v for tag,v in aligned if tag!='old')
    assert len(S)==k and len(T)==k+1
    assert tuple(sorted(set(S)))==S and tuple(sorted(set(T)))==T
    def verify(centers,expected):
        distances=[min(abs(y-xs[c]) for c in centers) for y in xs]
        assert max(distances)<=2 and sum(distances)==expected
    verify(S,summary[0][k][0]);verify(T,summary[0][k+1][0])
    assert len(set(S)-set(T))<=r
    return (S,T),count[0]

def exhaustive_compare(xs):
    """Independent direct subset enumeration to validate product-language min edit."""
    opts={}
    for k in range(1,len(xs)+1):
        for selection in combinations(range(len(xs)),k):
            distances=[min(abs(y-xs[c]) for c in selection) for y in xs]
            if max(distances)>2:continue
            v=sum(distances)
            if k not in opts or v<opts[k][0]:opts[k]=(v,[selection])
            elif v==opts[k][0]:opts[k][1].append(selection)
    summary=local_dp(xs)
    assert {k:v[0] for k,v in opts.items()}=={k:v[0] for k,v in summary[0].items()}
    tested=0
    for k in sorted(opts):
        if k+1 not in opts:continue
        truth=min(len(set(a)-set(b)) for a in opts[k][1] for b in opts[k+1][1])
        got=next(r for r in range(k+1) if find_pair(xs,summary,k,r)[0] is not None)
        assert got==truth,(xs,k,truth,got)
        tested+=1
    return tested

def main():
    x,blocks=make_r5();ds=[local_dp(b) for b in blocks]
    kmins=[min(d[0]) for d in ds]
    assert sum(kmins)==213
    J0=sum(d[0][k][0] for d,k in zip(ds,kmins));assert J0==1070
    gains=[d[0][k][0]-d[0][k+1][0] for d,k in zip(ds,kmins)]
    assert gains.count(6)==1 and gains.index(6)==22
    assert gains.count(5)==7
    win5=[i for i,g in enumerate(gains) if g==5]
    # The unique 6-gain block is mandatory at K=214; at K=215, a further 5-gain
    # first increment in precisely one of seven blocks beats all other allocations.
    # Explicitly check every two-unit allocation, including double increments.
    best2=max(max(gains[i]+gains[j] for i in range(29) for j in range(i+1,29)),
              max(gains[i]+(ds[i][0][kmins[i]+1][0]-ds[i][0][kmins[i]+2][0]) for i in range(29)))
    assert best2==11
    assert [i for i in range(29) if i!=22 and gains[i]==5]==win5
    assert J0-6==1064 and J0-best2==1059

    records=[]; witness=None
    for i in win5:
        k=kmins[i]
        zero,n0=find_pair(blocks[i],ds[i],k,0)
        one,n1=find_pair(blocks[i],ds[i],k,1)
        two,n2=find_pair(blocks[i],ds[i],k,2)
        assert zero is None and one is None and two is not None
        S,T=two; assert len(set(S)-set(T))==2
        r={'index_zero_based':i,'size':len(blocks[i]),'k':k,
           'cost_k':ds[i][0][k][0],'cost_k1':ds[i][0][k+1][0],
           'opt_counts':[ds[i][0][k][1],ds[i][0][k+1][1]],
           'min_removed':2,'product_states_attempted':[n0,n1,n2],
           'old_only_relative':[blocks[i][v]-blocks[i][0] for v in S if v not in T],
           'new_only_relative':[blocks[i][v]-blocks[i][0] for v in T if v not in S]}
        records.append(r)
        if i==4:witness={'block':4,'old_centers_relative':[blocks[i][v]-blocks[i][0] for v in S],
                           'new_centers_relative':[blocks[i][v]-blocks[i][0] for v in T]}
    assert witness is not None

    # Exact finite exhaustive independent tests (deliberately small stated domain).
    small_count=0;transition_count=0
    for N in range(2,8):
        for others in combinations(range(1,10),N-1):
            xs=(0,)+others
            transition_count+=exhaustive_compare(xs)
            small_count+=1
    result={
        'status':'PASS_EXACT_LOCAL',
        'scientific_pin':PIN,'event_boundaries':len(x),'events':x[-1],
        'block_count':len(blocks),'global_J_213_214_215':[1070,1064,1059],
        'K214_optimal_extra_allocation':[[22,1]],
        'K215_optimal_extra_allocations':[[[22,1],[i,1]] for i in win5],
        'seven_gain5_block_results':records,
        'global_transition':'214_to_215','rho_214':2,
        'minimum_symmetric_difference':5,
        'global_constructive_witness_block4':witness,
        'independent_exhaustive_small_integer_inputs':small_count,
        'independent_exhaustive_budget_transitions':transition_count,
        'classification':'This result is within frozen R5 integer-event sampling, not native 28-coordinate end-to-end throughput or formal Result/Review',
    }
    outfile=Path(__file__).with_name('EXACT_OUTPUT.json')
    outfile.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
