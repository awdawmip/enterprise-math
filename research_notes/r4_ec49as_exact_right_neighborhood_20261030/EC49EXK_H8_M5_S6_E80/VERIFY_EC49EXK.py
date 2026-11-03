#!/usr/bin/env python3
"""EC49EXK exact native-X6 paired-symbolic-BRC H8/M5 witness and bounded-template certificate.
Uses only integer operations and finite enumeration, Python 3.10+.
Frozen scientific pins: GK 773d538180bfb49e24cffeb35c3ee75eb0628e2e,
EM fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import Counter,defaultdict
from itertools import permutations,product
import json
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
HIST=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
T4=(1836687,1867942,1872656,1873981)
T2=(1836425,1866380)
K=(4,2,1)
WITNESS={2:('ce','de','ec','ed'),3:('feg','gef'),
 4:('edfg','defg','gefc','fegc'),5:('fegfg','geffg'),
 **{h:('feg'+'f'*(h-3),'gef'+'f'*(h-3)) for h in (6,7,8)}}
BASE={h:WITNESS[h] for h in (2,3,6,7,8)}

def native(w):return tuple(s for op in w for s in OPS[op])
def primkey(st):return tuple(st.count(i) for i in range(1,7))
def displacement(st):return tuple(st.count(i)-st.count(-i) for i in range(1,7))
def sig(st):
    value=0;factor=1
    for ev,prior in HIST:
        for x in st:
            if prior==1 and x==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            if prior==2 and x==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            prior=x
        value+=BUCKETS.index(ev)*factor
        factor*=5
    return value

def matrix_rank(words):
    # Nine rows, five columns per operation word; exact Fraction-free integer Gaussian elimination.
    cols=[]
    for w in words:
        num=sig(native(w));cols.append([(num//(5**i))%5 for i in range(9)])
    A=[[int(col[row]==bucket) for col in cols for bucket in range(5)] for row in range(9)]
    from fractions import Fraction
    A=[[Fraction(v) for v in row] for row in A]
    rank=0
    for c in range(len(A[0])):
        pivot=next((j for j in range(rank,9) if A[j][c]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        d=A[rank][c]
        A[rank]=[x/d for x in A[rank]]
        for j in range(9):
            if j!=rank and A[j][c]:
                d=A[j][c];A[j]=[u-d*v for u,v in zip(A[j],A[rank])]
        rank+=1
        if rank==9:break
    return rank

def prefixes(w):
    st=native(w)
    return {st[:j] for j in range(1,len(st)+1)}

def fiber(h,key):
    u,v,w=key;r=u+v-h-1;na=w-1;nf=u-r-2*w;ng=v-r
    assert min(r,na,nf,ng)>=0
    out=set()
    for nc in range(r+1):
        charset='a'*na+'c'*nc+'d'*(r-nc)+'e'*w+'f'*nf+'g'*ng
        for p in permutations(charset):out.add(''.join(p))
    return sorted(out)

def run():
    fullpre=set();per=[];allkey=set();allsig=set()
    for h in range(2,9):
        ws=WITNESS[h];assert all(len(w)==h for w in ws)
        signatures={sig(native(w)) for w in ws}
        assert signatures==set(T4 if h in (2,4) else T2),(h,signatures)
        assert matrix_rank(ws)==9,h
        keyset={primkey(native(w)) for w in ws};assert len(keyset)==1
        for w in ws:
            assert displacement(native(w))==(2,0,0,0,0,0)
            fullpre|=prefixes(w)
        allkey|=keyset;allsig|=signatures
        per.append({'h':h,'words':list(ws),'key':list(next(iter(keyset))),'rank':9,'E_cumulative':len(fullpre)})
    assert (len(fullpre),len(allkey),len(allsig))==(80,5,6)
    baseline=set().union(*(prefixes(w) for ws in BASE.values() for w in ws))
    assert len(baseline)==62
    groups=[]
    for h,sigs in [(4,T4),(5,T2)]:
        bysig=defaultdict(list)
        for w in fiber(h,K):
            s=sig(native(w))
            if s in sigs:bysig[s].append(w)
        groups.extend([bysig[s] for s in sigs])
    assert [len(g) for g in groups]==[12]*6
    extras=set().union(*(prefixes(w)-baseline for g in groups for w in g))
    numbers={p:i for i,p in enumerate(sorted(extras))}
    def mask(w):return sum(1<<numbers[e] for e in prefixes(w)-baseline)
    groupmask=[[(mask(w),w) for w in g] for g in groups]
    pairs=[(p[0][0]|p[1][0],(p[0][1],p[1][1])) for p in product(*groupmask[4:])]
    best=10**9;bestwords=()
    h4_combinations=0;tested_pairs=0;pruned=0
    for tup in product(*groupmask[:4]):
        h4_combinations+=1
        current=0
        for code,_ in tup:current|=code
        if current.bit_count()>=best:
            pruned+=1
            continue # Exact monotone lower bound: adding the h5 masks cannot decrease cost.
        for code,ws in pairs:
            tested_pairs+=1
            cost=(current|code).bit_count()
            if cost<best:
                best=cost
                bestwords=tuple(w for _,w in tup)+ws
    assert h4_combinations==12**4
    assert len(pairs)==12**2
    assert best==18,(best,bestwords)
    assert len(set().union(*(prefixes(w) for w in bestwords),baseline))==80
    out={
      'status':'PASS','scope':'fixed h2,h3,h6,h7,h8 equal-key ladder, h4+h5 key=(4,2,1), mandatory T4/T2 signed-native words',
      'H':8,'resources':{'E':len(fullpre),'M':len(allkey),'S':len(allsig)},
      'per_horizon':per,'baseline_E':len(baseline),'h4_candidate_counts':[len(g) for g in groups[:4]],
      'h5_candidate_counts':[len(g) for g in groups[4:]],
      'potential_combinations':12**6,'h4_combinations_exhausted':h4_combinations,
      'h4_combinations_pruned_by_monotonicity':pruned,'h4_h5_pair_combinations_examined':tested_pairs,
      'fixed_template_min_extra':best,'fixed_template_min_E':62+best,
      'attaining_words_for_template':list(bestwords),
      'scientific_inputs':{'global':'773d538180bfb49e24cffeb35c3ee75eb0628e2e','enterprise_math':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'}
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))
    return out
if __name__=='__main__':
    run()
