#!/usr/bin/env python3
"""R686 exact S3 V17 cocycle and R685 parity-obstruction reproducer; stdlib only."""
from itertools import combinations,permutations
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import json

TRIADS=tuple(combinations(range(6),3))
ADJ={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
ID=(0,1,2); BASE=ID

def move(F,S,T):
    a=next(iter(set(S)-set(T)));b=next(iter(set(T)-set(S)))
    return tuple(b if x==a else x for x in F)
def rho(S,T):
    return tuple(T.index(x) for x in move(S,S,T))
def mul(q,p):
    return tuple(q[j] for j in p)
def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1

def dfs(k):
    out=Counter()
    def walk(S,p,n):
        if n==k:
            if S==BASE:out[p]+=1
            return
        for T in ADJ[S]:walk(T,mul(rho(S,T),p),n+1)
    walk(BASE,ID,0)
    return out
def dp(k):
    a={(BASE,ID):1}
    for _ in range(k):
        b=defaultdict(int)
        for (S,p),mass in a.items():
            for T in ADJ[S]:b[(T,mul(rho(S,T),p))]+=mass
        a=dict(b)
    return Counter({p:n for (S,p),n in a.items() if S==BASE})

MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),
       ((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
PASS=((0,1),(1,2),(2,0))
W=(-1,1,-2,-1)
def enc(S,m):
    if any((a in S)+(b in S)!=1 for a,b in m):return 0
    return 1 if sum(b in S for a,b in m)%2==0 else -1
C={S:tuple(enc(S,m) for m in MATCH) for S in TRIADS}

@lru_cache(maxsize=None)
def choose(u,cnt,S):
    options=[]
    for e,(a,b) in enumerate(PASS):
        v=list(u);v[a]+=1;v[b]-=1
        h=list(cnt);h[e]+=1
        omega=((0,h[0],-h[2],0),(-h[0],0,h[1],0),(h[2],-h[1],0,0),(0,0,0,0))
        scores=[]
        for T in ADJ[S]:
            phi=sum(v[i]*C[T][i] for i in range(4))
            phi+=sum(C[S][i]*omega[i][j]*C[T][j] for i in range(4) for j in range(4))
            scores.append(7*phi+sum(W[i]*C[T][i] for i in range(4)))
        z=max(scores)
        options.append((z,W[a]-W[b],e,tuple(T for T,q in zip(ADJ[S],scores) if q==z)))
    return max(options)

def step(states):
    out=defaultdict(Fraction)
    for (u,m,S,p),mass in states.items():
        _,_,e,options=choose(u,m,S)
        a,b=PASS[e]
        v=list(u);v[a]+=1;v[b]-=1
        h=list(m);h[e]+=1
        for T in options:
            out[(tuple(v),tuple(h),T,mul(rho(S,T),p))]+=mass/len(options)
    assert sum(out.values(),Fraction(0))==1
    return dict(out)

def verify():
    assert len(TRIADS)==20 and all(len(ADJ[S])==9 for S in TRIADS)
    for S in TRIADS:
        for T in ADJ[S]:
            assert mul(rho(T,S),rho(S,T))==ID
            for p in permutations(ID):
                F=tuple(S[i] for i in p)
                G=move(F,S,T)
                assert tuple(T.index(x) for x in G)==mul(rho(S,T),p)
    counts={}
    for k in (1,2,3,4):
        d=dfs(k)
        assert d==dp(k)
        counts[k]={''.join(map(str,p)):d.get(p,0) for p in permutations(ID)}
    assert [sum(counts[k].values()) for k in (1,2,3,4)]==[0,9,36,369]
    assert counts[3]=={'012':18,'021':6,'102':6,'120':0,'201':0,'210':6}
    assert counts[4]=={'012':207,'021':48,'102':48,'120':9,'201':9,'210':48}
    assert mul(rho((0,2,3),(0,1,2)),
               mul(rho((0,1,3),(0,2,3)),rho((0,1,2),(0,1,3))))==(0,2,1)
    bias=(-2,-4,-3,10);S0=(0,3,5)
    a={(bias,(0,0,0),S0,ID):Fraction(1)}
    for t in range(227):a=step(a)
    key=((4,4,-17,10),(75,83,69),(0,2,5))
    fibre={p:mass for (u,c,S,p),mass in a.items() if (u,c,S)==key}
    assert fibre=={ID:Fraction(1,2),(1,2,0):Fraction(1,4)}
    assert len(a)==3 and all(parity(p)==1 for p in fibre)
    assert sum(fibre.values())==Fraction(3,4)
    for (u,c,S,p),mass in a.items():
        assert sum(c)==227 and sum(u)==sum(bias) and mass>0
    data={'schema':'R686_S3_COCYCLE_PARITY_V1',
          'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
          'predecessor':'R685@8505a08128e307c5ffbba1dd0522f66f515a401e',
          'graph_vertices':20,'directed_edges':180,'frame_edge_checks':1080,
          'closed_walks_at_012_by_length':counts,
          'holonomy_generated_group':'S3',
          'first_nontrivial_loop_length':3,'first_nonidentity_even_loop_length':4,
          'witness_time':227,'witness_field':{'u':[4,4,-17,10],
             'M01_M12_M20':[75,83,69],'S':'025'},
          'witness_unconditional_group_masses':{'012':'1/2','120':'1/4'},
          'witness_conditional_group_masses':{'012':'2/3','120':'1/3'},
          'both_frame_classes_even':True,'arithmetic':'int and fractions.Fraction',
          'scope':'All legal finite triad paths for cocycle; all based closed walks length <=4 for counts; R685 single t227 witness.'}
    Path(__file__).with_name('R686_EVIDENCE.json').write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print('R686_S3_COCYCLE_PARITY_EXACT_PASS')
if __name__=='__main__':verify()
