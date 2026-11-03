#!/usr/bin/env python3
"""Stage396-B full exact signed-X6 terminal pair-cancellation verifier."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import factorial

AXES = tuple((i, s) for i in range(6) for s in (1, -1))
P = {d: Fraction((i + 1) if s == 1 else (i + 7), 78) for i, s in AXES for d in [(i, s)]}
assert sum(P.values()) == 1
OMEGA = {(i,s): Fraction(i+2) if s==1 else -Fraction(1,i+2) for (i,s) in AXES}
D = {(0,1)}

def delta(d):
    v=[0]*6; v[d[0]]=d[1]; return tuple(v)

def endpoint(w):
    z=[0]*6
    for i,s in w: z[i]+=s
    return tuple(z)

def partitions(n, k):
    if n==1:
        yield (k,)
    else:
        for j in range(k+1):
            for tail in partitions(n-1,k-j): yield (j,)+tail

@lru_cache(None)
def brc(m,z):
    min_length=sum(abs(a) for a in z)
    if m<min_length or ((m-min_length)&1): return (0, Fraction(0))
    k=(m-min_length)//2
    a=[max(t,0) for t in z]; b=[max(-t,0) for t in z]
    count=0; weight=Fraction(0)
    for ks in partitions(6,k):
        denom=1; pterm=Fraction(1)
        for i,ki in enumerate(ks):
            plus=a[i]+ki; minus=b[i]+ki
            denom *= factorial(plus)*factorial(minus)
            pterm *= P[(i,1)]**plus*P[(i,-1)]**minus
        multi=factorial(m)//denom
        count += multi
        weight += multi*pterm
    return count,weight

@lru_cache(None)
def observe(w):
    z=endpoint(w); h=min(z)
    triples=tuple(tuple(z[i]-min(z[j] for j in S) for i in S) for S in combinations(range(6),3))
    turns=sum(w[j]!=w[j-1] for j in range(1,len(w)))
    signed=Fraction(1)
    for d in w: signed*=OMEGA[d]
    return ('P',z,triples,h,len(w),*brc(len(w),z),turns,signed)

def sig(w,k): return w[-k:] if k else ()

def act(w,kind,d=None):
    if kind=='APPEND': return w+(d,)
    if kind=='POP':
        if w and w[-1] in D: return w[:-1]
        return None
    if kind=='CANCEL':
        if len(w)>=2 and w[-2][0]==w[-1][0] and w[-2][1]==-w[-1][1]: return w[:-2]
        return None
    raise ValueError(kind)

def prove_witness(H,C):
    u=((0,-1),(1,1),(1,-1))
    v=((0,-1),(2,1),(2,-1))
    tail=((3,1),(3,-1))*C+((0,1),)*H
    w=u+tail; x=v+tail
    k=H+2*C+1
    assert observe(w)==observe(x)
    assert sig(w,k-1)==sig(x,k-1) and sig(w,k)!=sig(x,k)
    for _ in range(H):
        w1,x1=act(w,'POP'),act(x,'POP')
        assert w1 is not None and x1 is not None
        w,x=w1,x1
        assert observe(w)==observe(x)
    for _ in range(C):
        w1,x1=act(w,'CANCEL'),act(x,'CANCEL')
        assert w1 is not None and x1 is not None
        w,x=w1,x1
        assert observe(w)==observe(x)
    assert w==u and x==v
    w=act(w,'APPEND',(1,-1)); x=act(x,'APPEND',(1,-1))
    assert observe(w)!=observe(x)
    assert observe(w)[-2]+1==observe(x)[-2], (H,C,observe(w)[-2:],observe(x)[-2:])
    return k

def recurrence_test():
    counts={((0,)*6):(1,Fraction(1))}
    checked=0
    for m in range(4):
        for z,mass in counts.items():
            assert brc(m,z)==mass
            checked+=1
        next_counts=defaultdict(lambda:(0,Fraction(0)))
        for z,(num,mass) in counts.items():
            for d in AXES:
                nz=tuple(z[i]+delta(d)[i] for i in range(6))
                oldnum,oldmass=next_counts[nz]
                next_counts[nz]=(oldnum+num,oldmass+mass*P[d])
        counts=next_counts
    for z,mass in counts.items():
        assert brc(4,z)==mass
        checked+=1
    return checked

def finite_crosscheck():
    small=AXES[:4]; words=[()]
    for m in range(1,5): words.extend(product(small,repeat=m))
    pairs=[]
    for H in (0,1):
        for C in (0,1):
            groups=defaultdict(list)
            for w in words: groups[(observe(w),sig(w,H+2*C+1))].append(w)
            for grp in groups.values():
                for i in range(len(grp)):
                    for j in range(i+1,len(grp)): pairs.append((grp[i],grp[j],H,C))
    examined=0; edges=0
    for w,v,H,C in pairs:
        seen=set(); stack=[(w,v,H,C,0)]
        while stack:
            x,y,h,c,depth=stack.pop()
            key=(x,y,h,c,depth)
            if key in seen: continue
            seen.add(key); examined+=1
            assert observe(x)==observe(y)
            if depth>=4: continue
            options=[('APPEND',d) for d in small]
            if h: options.append(('POP',None))
            if c: options.append(('CANCEL',None))
            for kind,d in options:
                nx=act(x,kind,d); ny=act(y,kind,d)
                assert (nx is None)==(ny is None)
                edges+=1
                if nx is not None:
                    stack.append((nx,ny,h-(kind=='POP'),c-(kind=='CANCEL'),depth+1))
    return len(pairs),examined,edges

def histogram(w):
    hist=defaultdict(int)
    for d,e in zip(w,w[1:]): hist[d,e]+=1
    return dict(hist)

if __name__=='__main__':
    brc_compared=recurrence_test()
    sharp=[prove_witness(H,C) for H in range(4) for C in range(4)]
    pairs,states,edges=finite_crosscheck()
    prev_u=((0,-1),(1,1),(1,-1),(3,1),(3,-1),(0,1))
    prev_v=((0,-1),(2,1),(2,-1),(3,1),(3,-1),(0,1))
    assert observe(prev_u)==observe(prev_v)
    assert histogram(prev_u)!=histogram(prev_v)
    print('STAGE396B_BOUNDED_PAIR_CANCEL_PASS')
    print('full_12_direction_BRC_recurrence_endpoints=',brc_compared)
    print('sharp_suffix_witnesses=',len(sharp),'maximum_required_lookback=',max(sharp))
    print('finite_word_alphabet=4 words_length<=4 H,C<=1 sequence_length<=4')
    print('same_observer_and_signature_pairs=',pairs,'visited_paired_states=',states,'operation_edges=',edges)
    print('joint_adjacent_pair_histogram_distinguishes_stage395_witness=True')
