#!/usr/bin/env python3
"""PREFIX-478: exact full-X6 finite checks and two-letter arbitrarily-long suffix witnesses.
All arithmetic integral, Python standard library; no stochastic tests.
"""
from collections import defaultdict
from math import comb
from hashlib import sha256

ALPHABET = 'aAbBcCdDeE'
WORDS = ('aab','aAa','ababa')
EXPECTED = {'aab':(3,(2,0),5), 'aAa':(3,(0,0),3), 'ababa':(4,(0,0,0,0),4)}

def step(w, q, c):
    t = w[:q] + c
    return max(j for j in range(len(w)+1) if t.endswith(w[:j]))

def ob(counts):
    s=counts[0]
    axes=[(counts[1+2*i],counts[2+2*i]) for i in range(5)]
    y=tuple(a-b for a,b in axes)
    p=[min(a,b) for a,b in axes]
    return (s,)+y+(p[1]+2*p[3]+p[4],p[2]+p[4])

def coeff(n,k):
    # P(m) from preceding proved series
    def p(m):
        return sum(c*comb(m-h+7,7) for h,c in enumerate((1,2,3,4,2)) if m>=h)
    return p(n)+sum(p(n-1-j*(k+1)) for j in range((n-1)//(k+1)+1)) if n>0 else p(0)

def finite_11(w,N=8):
    k=len(w); updates={(q,c):step(w,q,c) for q in range(k+1) for c in ALPHABET}
    states={((0,)*11,0)}; prev=[]
    for n in range(N+1):
        byq=[set() for _ in range(k+1)]
        for c,q in states: byq[q].add(ob(c))
        union=set().union(*byq)
        B=len(union); F=sum(map(len,byq))
        assert B==coeff(n,k), ('base',w,n,B,coeff(n,k))
        D=[(B if j==0 else prev[n-j]['B'] if n>=j else 0)-len(byq[j]) for j in range(k)]
        assert all(x>=0 for x in D)
        assert len(byq[k])==(prev[n-k]['B'] if n>=k else 0), ('last',w,n)
        assert F==B+sum(prev[n-j]['B'] if n>=j else 0 for j in range(1,k+1))-sum(D)
        prev.append({'B':B, 'D':D, 'F':F})
        if n>=6:
            print('FULL_X6',w,'n=',n,'B=',B,'F=',F,'delta=',','.join(map(str,D)),'states=',len(states))
        if n==N: break
        next_states=set()
        for c,q in states:
            for i,ch in enumerate(ALPHABET):
                a=list(c);a[i+1]+=1
                next_states.add((tuple(a),updates[q,ch]))
            if n==0 or q==k:
                a=list(c);a[0]+=1
                next_states.add((tuple(a),0))
        states=next_states
    return prev

def two_letter_fibers(w,N):
    # Count vectors (a,b,x) with 0<=x<=1; b='A' for aAa.
    letter_b='A' if w=='aAa' else 'b'; k=len(w)
    upd={(q,c):step(w,q,c) for q in range(k+1) for c in ('a',letter_b)}
    states={(0,0,0,0)}; layers=[]
    for n in range(N+1):
        fibers=defaultdict(set)
        for a,b,s,q in states: fibers[(a,b,s)].add(q)
        layers.append(fibers)
        if n==N: break
        out=set()
        for a,b,s,q in states:
            out.add((a+1,b,s,upd[q,'a']))
            out.add((a,b+1,s,upd[q,letter_b]))
            if s==0 and (n==0 or q==k): out.add((a,b,1,0))
        states=out
    return layers

def holes(w,n):
    # Exact count vectors for the asserted missing zero-state observations.
    raw=[(n,0,0),(n-1,1,0),(n-1,0,1)]
    if w=='ababa': raw.append((n-2,1,1))
    return raw

def reduced_certificate(w,N):
    k=len(w); expected_h,expected_tail,expected_D=EXPECTED[w]
    layers=two_letter_fibers(w,N)
    threshold=3*k+1
    for n in range(threshold,N+1):
        candidates=holes(w,n)
        assert len(candidates)==expected_h
        # All reduced alphabet fibers absent in q=0 are precisely these candidates.
        found={v for v,qs in layers[n].items() if 0 not in qs}
        assert found==set(candidates), (w,n,'holes',found ^ set(candidates))
        dd=[]
        for j in range(1,k):
            pref=w[:j]; added_a=pref.count('a');added_b=pref.count('A' if w=='aAa' else 'b')
            prior=holes(w,n-j)
            missing=[]
            for a,b,s in prior:
                padded=(a+added_a,b+added_b,s)
                if j not in layers[n][padded]:missing.append((a,b,s))
            dd.append(len(missing))
        assert tuple(dd)==expected_tail,(w,n,dd)
        if n in (threshold,threshold+1,20,30,48,70):
            print('REDUCED_EXACT',w,'n=',n,'holes=',expected_h,'deltas=',(expected_h,*dd),'D=',expected_h+sum(dd),'candidate_parikhs=',candidates)
    print('CERTIFIED_REDUCED_EXHAUSTIVE_RANGE',w,threshold,N)

if __name__=='__main__':
    for word in WORDS:
        finite_11(word,8)
    for word in WORDS:
        reduced_certificate(word,75)
    print('ALL_CHECKS_PASS')
