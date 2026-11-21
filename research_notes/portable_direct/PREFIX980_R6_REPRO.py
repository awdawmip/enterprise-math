#!/usr/bin/env python3
"""PREFIX-980 exact nonzero triple-word exhaustive checker, Python stdlib."""
from collections import defaultdict, Counter, deque
from itertools import product
import json

def names(p):
    d=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (1,-1): d[(1<<i)-s*(1<<j)].append((i,j,s))
    return d

def masks(src):
    out={}
    for a,triples in src.items():
        P=M=0
        for i,j,s in triples:
            if j:
                if s==1: P |= 1<<j
                else: M |= 1<<j
        out[a]=(P,M)
    return out

def graph(word,m):
    U=sorted({j for a in word for pm in m[a] for j in range(1,pm.bit_length()) if pm>>j&1})
    L=len(word); n=1<<len(U)
    adj=[[] for _ in range(L*n)]
    for phase,a in enumerate(word):
        P,M=m[a]
        for bits in range(n):
            v=phase*n+bits
            for k,j in enumerate(U):
                if ((M if bits>>k&1 else P)>>j)&1:
                    adj[v].append(((phase+1)%L*n+(bits^(1<<k)),j))
    return U,adj

def cycle_and_length(adj):
    indeg=[0]*len(adj)
    for row in adj:
        for w,j in row: indeg[w]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0)
    depth=[0]*len(adj); visited=0
    while q:
        v=q.popleft(); visited+=1
        for w,j in adj[v]:
            depth[w]=max(depth[w], depth[v]+1)
            indeg[w]-=1
            if indeg[w]==0:q.append(w)
    return visited<len(adj), max(depth)

def pair_inf(m,a,b):
    P,M=m[a];Q,N=m[b]
    return bool((P&N)|(M&Q)|((P&M) and (Q&N)))

def check_original_named(p,word,src,m):
    U,adj=graph(word,m); n=1<<len(U); checks=0
    for phase,a in enumerate(word):
        for x in range(1,1<<p,2):
            bits=sum(((x>>j)&1)<<k for k,j in enumerate(U))
            expected=sorted(j for i,j,s in src[a] if j and ((x>>j)&1)==(s==-1))
            actual=sorted(j for w,j in adj[phase*n+bits])
            assert expected==actual,(p,word,phase,x,expected,actual)
            checks+=1
    return checks

def main():
    result={};example=None;original_checks=0
    for p in (3,4,5,6):
        src=names(p);m=masks(src);res=sorted(a for a in src if a!=0)
        categories=Counter();maxfinite=0
        for word in product(res, repeat=3):
            U,adj=graph(word,m)
            assert len(U)<=6
            persistent,longest=cycle_and_length(adj)
            pairs=sum(pair_inf(m,word[i],word[(i+1)%3]) for i in range(3))
            categories[(persistent,pairs)]+=1
            if not persistent:maxfinite=max(maxfinite,longest)
            if p==4 and word==(-1,3,6):
                assert not persistent and pairs==3
                example=list(word)
        result[str(p)]={'nonzero_residues':len(res),'triple_words':len(res)**3,
          'persistent':sum(n for (b,k),n in categories.items() if b),
          'finite':sum(n for (b,k),n in categories.items() if not b),
          'maximum_finite_path_observed_any_phase':maxfinite,
          'pairwise_criterion_but_triple_finite':categories[(False,3)]}
        chosen=list(product(res,repeat=3)) if p==3 else [tuple(res[:3]),tuple(res[-3:]),(res[0],res[len(res)//2],res[-1])]
        for word in chosen: original_checks+=check_original_named(p,word,src,m)
    p=8;src=names(p);m=masks(src);word=(6,24,96);U,adj=graph(word,m)
    assert cycle_and_length(adj)[0]
    x=1;steps=[]
    for a,j in zip(word*2,(1,3,5,1,3,5)):
        valid=[(i,jj,s) for i,jj,s in src[a] if jj==j and ((x>>j)&1)==(s==-1)]
        assert len(valid)==1
        steps.append({'residual':a,'port':j,'state_before':x,'named_source':valid[0]})
        x^=1<<j
    assert x==1
    print(json.dumps({'schema':'PREFIX980_R6_EXACT_V1','triple_nonzero_enumeration':result,
      'all_pairwise_but_triple_finite_p4':example,'three_port_six_step_cycle_p8':steps,
      'original_named_transition_state_checks':original_checks,'scientific_review':'NOT_REVIEWED',
      'native_X6_equivalence':'NOT_ESTABLISHED'},ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
