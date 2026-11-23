#!/usr/bin/env python3
"""R762KR: exact, reproducible provenance enumerative coding for unsigned M3.
Uses Python standard-library integer arithmetic; no third-party packages.
"""
from functools import lru_cache
from itertools import combinations, product
from collections import defaultdict
from math import comb

INACTIVE = {(0, 1), (2, 3), (4, 5)}
PORTS = [p for p in combinations(range(6), 2) if p not in INACTIVE]
BITS = {p: 1 << i for i, p in enumerate(PORTS)}
EDGES = []
for i, j, k in product(range(2), repeat=3):
    a, b, c = (i, 2 + j), (i, 4 + k), (2 + j, 4 + k)
    EDGES.append((BITS[a] ^ BITS[b], BITS[a] ^ BITS[c], BITS[b] ^ BITS[c]))
F = {0}
for tri in combinations(range(6), 3):
    present = [p for p in combinations(tri, 2) if p in BITS]
    if len(present) == 2:
        e = BITS[present[0]] ^ BITS[present[1]]
        F |= {v ^ e for v in tuple(F)}
assert len(PORTS) == 12 and len(F) == 512 and len(EDGES) == 8


def triples(m):
    for x in range(m+1):
        for y in range(m-x+1):
            yield (x, y, m-x-y)


def local_key(s, c):
    mask = 0
    boundary = 0
    for a, n in enumerate(c):
        if n:
            mask |= (1 << a)
        if n % 2:
            boundary ^= EDGES[s][a]
    return boundary, color_state(mask)


def color_state(mask):
    assert 1 <= mask <= 7
    return mask.bit_length() if mask.bit_count()==1 else 4


def advance(state, contribution):
    if state==4 or contribution==4:
        return 4
    if state==0 or state==contribution:
        return contribution
    return 4


def compact_local(m, s):
    # Each positive even count starts at 2; each positive odd count starts at 1.
    # The remaining count is distributed among active types in increments of 2.
    d = defaultdict(int)
    for mask in range(1,8):
        h = mask.bit_count()
        for p in range(8):
            if p & ~mask:
                continue
            minimum = sum(1 if (p >> a)&1 else 2 for a in range(3) if (mask >> a)&1)
            if minimum>m or (m-minimum)%2:
                continue
            t=(m-minimum)//2
            ways=comb(t+h-1,h-1)
            b=0
            for a in range(3):
                if (p >> a)&1:
                    b ^= EDGES[s][a]
            d[(b,color_state(mask))] += ways
    assert sum(d.values()) == comb(m+2,2)
    return tuple((b,mask,ways) for (b,mask), ways in sorted(d.items()))


def coder(ms):
    assert len(ms)==8 and all(isinstance(m,int) and m>=1 for m in ms)
    local=[compact_local(m,s) for s,m in enumerate(ms)]
    @lru_cache(None)
    def D(i, remainder, seen):
        if i==8:
            return int(remainder==0 and seen==4)
        return sum(ways*D(i+1,remainder^b,advance(seen,mask))
                   for b,mask,ways in local[i])
    def count(b):
        return D(0,b,0)
    def rank(b,choices):
        assert len(choices)==8
        assert count(b)>0
        remainder, seen, pos=b,0,0
        for i,c in enumerate(choices):
            assert len(c)==3 and sum(c)==ms[i] and min(c)>=0
            matched=False
            for x in triples(ms[i]):
                lb,lmask=local_key(i,x)
                ways=D(i+1,remainder^lb,advance(seen,lmask))
                if x==tuple(c):
                    assert ways>0, 'choice not completable'
                    remainder ^= lb; seen = advance(seen,lmask)
                    matched=True; break
                pos+=ways
            assert matched
        assert remainder==0 and seen==4
        assert pos<count(b)
        return pos
    def unrank(b,position):
        assert 0<=position<count(b)
        remainder, seen=b,0
        out=[]
        for i in range(8):
            for c in triples(ms[i]):
                lb,lmask=local_key(i,c)
                ways=D(i+1,remainder^lb,advance(seen,lmask))
                if position>=ways:
                    position-=ways
                else:
                    out.append(c)
                    remainder ^= lb; seen = advance(seen,lmask)
                    break
            else:
                raise AssertionError('unrank exhaustion')
        assert position==0 and remainder==0 and seen==4
        return tuple(out)
    return count, rank, unrank, D


def independent_polynomial(ms):
    # Independent KN.1 group-algebra recurrence and exact v_j subtraction.
    d={0:1}
    for s,m in enumerate(ms):
        r=m//2
        A,B=(((r+1)*(r+2)//2,r*(r+1)//2) if m%2==0
             else (r*(r+1)//2,(r+1)*(r+2)//2))
        nd=defaultdict(int)
        for v,n in d.items():
            nd[v] += n*A
            for e in EDGES[s]:
                nd[v^e] += n*B
        d=nd
    for j in range(3):
        v=0
        for s,m in enumerate(ms):
            if m%2:
                v ^= EDGES[s][j]
        d[v]-=1
    return d


def test(ms, complete=False):
    count,rank,unrank,D=coder(ms)
    ref=independent_polynomial(ms)
    check=sorted(F) if complete else sorted({0,3,18,51,204,3840,4095}&F)
    for b in check:
        n=count(b)
        assert n==ref.get(b,0),(ms,b,n,ref.get(b,0))
        if n:
            indices={0,n//2,n-1} | (set(range(n)) if n<=12 else set())
            for k in indices:
                c=unrank(b,k)
                assert rank(b,c)==k,(ms,b,k)
    if complete:
        assert sum(count(b) for b in F)==sum(ref.get(b,0) for b in F)
    return {'ms':ms,'checked_boundaries':len(check),
            'Q0':count(0),'total_over_F':sum(ref.get(b,0) for b in F),
            'local_count':[comb(m+2,2) for m in ms],
            'memoized_states':D.cache_info().currsize}


if __name__=='__main__':
    reports=[]
    for m in (1,2,3,4):
        reports.append(test((m,)*8, complete=True))
    reports.append(test((1,2,3,4,1,2,3,4), complete=True))
    for item in reports:
        print('PASS',item)
    assert reports[0]['total_over_F']==1638
    assert reports[1]['Q0']==7197
    assert reports[1]['total_over_F']==420093
    assert reports[2]['Q0']==71197
    print('ALL_EXACT_CHECKS_PASS')
