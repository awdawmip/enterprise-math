#!/usr/bin/env python3
"""PREFIX-469 exact certificate. Pure stdlib integers and complete Parikh/DFA enumeration.

n<=8: visits every reachable (Parikh vector, suffix-state) pair; this is
independent of the generating-function proof and does not enumerate 11**n
ordered words. All arithmetic uses Python arbitrary precision integers.
"""
from collections import defaultdict
from math import comb

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
N = 8
# Coordinates: x, +e2,-e2,+e3,-e3,...,+e6,-e6.
# q = 0: suffix neither a nor ab; q=1 suffix a; q=2 suffix ab or empty.

def next_state(q,j,n):
    if j == 0:
        if n and q != 2:
            return None
        return 0
    if j == 1:
        return 1
    if j == 3 and q == 1:
        return 2
    return 0

def key_of(count):
    p=[]; y=[]
    for i in range(5):
        a,b=count[1+2*i], count[2+2*i]
        y.append(a-b); p.append(min(a,b))
    return (count[0],*y,p[1]+2*p[3]+p[4],p[2]+p[4])

def series_coefficients(N):
    # PREFIX-468 G=P/D; denominator D=(1-z)^8(1-z^3).
    P=[1,3,5,6,4,-1,-4,-2]
    D=[1,-8,28,-57,78,-84,84,-78,57,-28,8,-1]
    B=[]
    for n in range(N+1):
        val=(P[n] if n < len(P) else 0)
        for j in range(1, min(n,len(D)-1)+1):
            val -= D[j]*B[n-j]
        B.append(val)
    return B

B=series_coefficients(20)
# Independent direct ordered-word enumeration, testing the literal suffix gate.
WEIGHTS=[1,6,1,12,1,18,1,24,1,36,1]
def brute_words(n):
    found=set()
    nwords=0
    total_mass=0
    counts=[0]*11
    seq=[]
    def walk():
        nonlocal nwords,total_mass
        if len(seq)==n:
            key=key_of(counts)
            q=2 if not seq or len(seq)>=2 and seq[-2:]==[1,3] else (1 if seq[-1]==1 else 0)
            found.add((key,q))
            nwords+=1
            weight=1
            for j in seq: weight*=WEIGHTS[j]
            total_mass+=weight
            return
        for j in range(11):
            if j==0 and seq and (len(seq)<2 or seq[-2:]!=[1,3]): continue
            counts[j]+=1;seq.append(j)
            walk()
            seq.pop();counts[j]-=1
    walk()
    return found,nwords,total_mass

active={(0,)*11:1<<2}
lines=['PREFIX-469 EXACT EXECUTION, Python integer certificate',
       'scientific_pin='+PIN,
       'G(z)=(1+2z^2)(1+z)^2(1+z-z^3)/((1-z)^8(1-z^3))',
       'F(z)=(1+z+z^2)G(z)-z-3z^2/(1-z)',
       'n | Parikh_count | B_n | q0 | q1 | q2 | F_n | bits(H>=2)']
for n in range(N+1):
    base_masks={}
    for cnt,mask in active.items():
        key=key_of(cnt)
        base_masks[key]=base_masks.get(key,0)|mask
    counts=[sum((mask>>q)&1 for mask in base_masks.values()) for q in (0,1,2)]
    predicted = (1 if n==0 else (B[n] if n==1 else B[n]+B[n-1]+B[n-2]-3))
    F=sum(x.bit_count() for x in base_masks.values())
    assert len(base_masks)==B[n], ('B',n,len(base_masks),B[n])
    assert F==predicted, ('F',n,F,predicted)
    if n==0:
        assert counts==[0,0,1]
    elif n==1:
        assert counts==[10,1,0]
    else:
        assert counts==[B[n]-3,B[n-1],B[n-2]], (n,counts)
        missing={f for f,mask in base_masks.items() if not mask&1}
        ex={(0,n,0,0,0,0,0,0),(0,n-1,1,0,0,0,0,0),(1,n-1,0,0,0,0,0,0)}
        assert missing==ex,(n,missing,ex)
    if n<=5:
        raw,rawcount,rawmass=brute_words(n)
        compressed={(f,q) for f,mask in base_masks.items()
                    for q in range(3) if mask & (1<<q)}
        assert raw==compressed,('ordered_brute',n,len(raw),len(compressed))
        # Weight recurrence of PREFIX-466, with the unrestricted initial x.
        def expected_words(n,S,c):
            arr=[]
            for k in range(n+1):
                arr.append((1 if k==0 else 0)+(1 if k==1 else 0)
                           + (S*arr[k-1] if k>=1 else 0)
                           + (c*arr[k-3] if k>=3 else 0))
            return arr[n]
        assert rawcount==expected_words(n,10,1),(n,rawcount)
        assert rawmass==expected_words(n,101,72),(n,rawmass)
    # Compact analytic q0 criterion on entire feasible Parikh population.
    # Enumerate *every* vector of total n (rather than only reachable vectors).
    existing=set(active)
    legal=set()
    acc=[0]*11
    def enumerate_vectors(i,left):
        if i==10:
            acc[i]=left
            if acc[0]<=1+min(acc[1],acc[3]):
                legal.add(tuple(acc))
            return
        for k in range(left+1):
            acc[i]=k;enumerate_vectors(i+1,left-k)
    enumerate_vectors(0,n)
    assert legal==existing,('parikh',n,len(legal),len(existing))
    expected_nq0=0 if n==0 else (B[n]-1 if n==1 else B[n]-3)
    assert counts[0]==expected_nq0
    bits=(F-1).bit_length()
    lines.append(f'{n} | {len(active)} | {B[n]} | {counts[0]} | {counts[1]} | {counts[2]} | {F} | {bits}')
    if n==N: break
    nxt={}
    for cnt,mask in active.items():
        for j in range(11):
            nxtmask=0
            for q in (0,1,2):
                if mask&(1<<q):
                    qn=next_state(q,j,n)
                    if qn is not None:
                        nxtmask |= 1<<qn
            if nxtmask:
                nc=list(cnt);nc[j]+=1
                nc=tuple(nc)
                nxt[nc]=nxt.get(nc,0)|nxtmask
    active=nxt
# Exact large-n prediction via rational series only; no independent enumeration there.
lines.append('n | B_n from rational G | F_n from rational F | bits F')
for n in (9,10,12,16,20):
    f=B[n]+B[n-1]+B[n-2]-3
    lines.append(f'{n} | {B[n]} | {f} | {(f-1).bit_length()}')
lines.append('ordered_word_brute_n_0_to_5=PASS; count_and_positive_mass_recurrences=PASS')
lines.append('ALL_CHECKS_PASS')
print('\n'.join(lines))
