#!/usr/bin/env python3
"""PREFIX-476: exact finite certificate for uniform mixed-word KMP suffix correction.
Uses only Python stdlib; all arithmetic and sets are exact.
"""
from collections import defaultdict
from math import comb
from time import perf_counter

ORDINARY = 'aAbBcCdDeE'
ALL = 'x' + ORDINARY
WEIGHTS = ((0, 1, 0, 2, 1), (0, 0, 1, 0, 1))

def kmp_next(word, q, letter):
    if letter == 'x':
        return 0
    t = word[:q] + letter
    for j in range(min(len(word), len(t)), 0, -1):
        if t.endswith(word[:j]):
            return j
    return 0

def observer(counts):
    s = counts[0]
    y, p = [], []
    for i in range(5):
        pos, neg = counts[1+2*i], counts[2+2*i]
        y.append(pos-neg)
        p.append(min(pos, neg))
    return (s, *y, sum(WEIGHTS[0][i]*p[i] for i in range(5)),
            sum(WEIGHTS[1][i]*p[i] for i in range(5)))

def pad(base, word):
    s = base[0]
    old_y = base[1:6]
    new_y, d_p = [], []
    for i in range(5):
        plus = word.count(ORDINARY[2*i]); minus = word.count(ORDINARY[2*i+1])
        y2 = old_y[i] + plus-minus
        dp = (plus+minus+abs(old_y[i])-abs(y2))//2
        assert (plus+minus+abs(old_y[i])-abs(y2)) % 2 == 0
        new_y.append(y2); d_p.append(dp)
    return (s, *new_y,
            base[6]+sum(WEIGHTS[0][i]*d_p[i] for i in range(5)),
            base[7]+sum(WEIGHTS[1][i]*d_p[i] for i in range(5)))

def base_formula(k, n):
    def h(t):
        if t < 0: return 0
        return sum(comb(t-(k+1)*i+7, 7) for i in range(t//(k+1)+1))
    pol = {0:1}
    for t in ({0:1,2:2}, {0:1,1:2,2:1}, {0:1,1:1,k+1:-1}):
        nxt=defaultdict(int)
        for a,c in pol.items():
            for b,d in t.items(): nxt[a+b] += c*d
        pol=dict(nxt)
    return sum(c*h(n-i) for i,c in pol.items())

def run(word, max_n):
    k=len(word)
    assert 'x' not in word and word and word[0] in ORDINARY
    letters=('x',)+tuple(ORDINARY)
    index={c:i for i,c in enumerate(letters)}
    transitions={(q,c):kmp_next(word,q,c) for q in range(k+1) for c in ORDINARY}
    empty=(0,)*11
    states={(empty,0)}
    S=[]; Sq=[]
    start=perf_counter()
    print(f'PATTERN {word} K={k} MAX_N={max_n}')
    for n in range(max_n+1):
        byq=[set() for _ in range(k+1)]
        byall=set()
        bycount=defaultdict(set)
        for counts,q in states:
            f=observer(counts)
            byall.add(f); byq[q].add(f)
            bycount[counts].add(q)
        S.append(byall); Sq.append(byq)
        assert len(byall) == base_formula(k,n), ('base formula',word,n,len(byall),base_formula(k,n))
        hole=byall-byq[0]
        witness={}
        for counts,qs in bycount.items():
            if counts[0] <= 1 and all(counts[index[c]]<k for c in ORDINARY if c !=word[0]):
                f=observer(counts)
                witness.setdefault(f,counts)
        assert hole.issubset(witness), ('hole counterexample',word,n,hole-set(witness))
        correction=[]
        for j in range(1,min(k-1,n)+1):
            m=n-j
            u=word[:j]
            s0={pad(f,u) for f in Sq[m][0]}
            full={pad(f,u) for f in S[m]}
            assert len(full)==len(S[m]),('padding injectivity',word,n,j)
            assert s0.issubset(byq[j]), ('lower sandwich',word,n,j, s0-byq[j])
            assert byq[j].issubset(full), ('upper sandwich',word,n,j,byq[j]-full)
            assert len(byq[j]-s0) <= len(S[m]-Sq[m][0])
            correction.append(f'{j}:{len(byq[j]-s0)}')
        if n>=k:
            full={pad(f,word) for f in S[n-k]}
            assert byq[k]==full, ('full match',word,n)
        else:
            assert not byq[k]
        if word == 'a' or (len(word)>=2 and word == 'a' + 'b'*(len(word)-1)):
            expected_hole=min(k,n)+min(k-1,max(0,n-1)) if n>=1 else 0
            assert len(hole)==expected_hole, ('explicit ab^r holes',word,n,len(hole),expected_hole)
            for j in range(1,k+1):
                assert len(byq[j]) == (len(S[n-j]) if n>=j else 0), ('ab^r suffix',word,n,j)
            for H in range(k+2):
                if H==0: actual=len(byall); expected=len(byall)
                elif H>=k:
                    actual=sum(map(len,byq))
                    expected=sum(len(S[n-j]) for j in range(k+1) if n>=j)-expected_hole
                else:
                    r=k-H
                    actual=len(set().union(*byq[:r+1]))+sum(len(byq[j]) for j in range(r+1,k+1))
                    expected=len(byall)+sum(len(S[n-j]) for j in range(r+1,k+1) if n>=j)
                assert actual==expected, ('ab^r H-quotient',word,n,H,actual,expected)
        fn=sum(len(x) for x in byq)
        approx=sum(len(S[n-j]) if n>=j else 0 for j in range(k+1))
        assert 0 <= approx-fn <= k*2*k**9
        print('n=%d B=%d Q=%s holes0=%d deficits=%d proper_extra={%s} states=%d' %
              (n,len(byall),','.join(str(len(q)) for q in byq),len(hole),approx-fn,
              ','.join(correction),len(states)))
        if n==max_n: break
        out=set()
        for counts,q in states:
            for c in ORDINARY:
                v=list(counts);v[index[c]]+=1
                out.add((tuple(v),transitions[(q,c)]))
            if n==0 or q==k:
                v=list(counts);v[0]+=1
                out.add((tuple(v),0))
        states=out
    print(f'PASS pattern={word} elapsed={perf_counter()-start:.3f}s')

if __name__=='__main__':
    for w,cap in [('a',7),('aa',7),('ab',7),('aba',7),('aab',7),('abb',7),('abab',7),('abbb',7),('abbbb',7),('aAa',7),('ababa',7)]:
        run(w,cap)
    print('ALL_CHECKS_PASS')
