#!/usr/bin/env python3
"""R708 exact integer/positive-Fraction checks for labeled X6 equal-q Cell triads."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod
import json

AXES=6
TRIPLES=tuple(combinations(range(6),3))

@lru_cache(None)
def D(n):
    if not any(n): return 1
    if sum(n)%3: return 0
    a=next(i for i,v in enumerate(n) if v)
    ans=0
    for b,c in combinations((i for i in range(AXES) if i!=a and n[i]),2):
        z=list(n)
        for i in (a,b,c): z[i]-=1
        ans+=n[b]*n[c]*D(tuple(z))
    return ans

def greedy(n):
    z=list(n)
    out=[]
    while any(z):
        a=sorted(range(AXES),key=lambda i:(-z[i],i))[:3]
        if any(z[i]<=0 for i in a): return None
        out.append(tuple(a))
        for i in a: z[i]-=1
    return out

def coeffs(max_m=4,max_power=3):
    cur={(0,)*AXES:1}
    out=[cur]
    for m in range(1,max_m+1):
        nxt=Counter()
        for mon,weight in cur.items():
            for tr in TRIPLES:
                z=list(mon)
                for i in tr: z[i]+=1
                if max(z)<=max_power: nxt[tuple(z)]+=weight
        cur=dict(nxt)
        out.append(cur)
    return out

@lru_cache(None)
def brute(tokens):
    tokens=tuple(sorted(tokens))
    if not tokens: return frozenset({()})
    a=tokens[0]
    result=set()
    for b,c in combinations(tokens[1:],2):
        if len({a[0],b[0],c[0]})!=3: continue
        tr=tuple(sorted((a,b,c)))
        rest=tuple(x for x in tokens if x not in tr)
        for tail in brute(rest):
            result.add(tuple(sorted((tr,)+tail)))
    return frozenset(result)

def rational_sampler(tokens):
    tokens=tuple(sorted(tokens))
    if not tokens: return {():Fraction(1)}
    n=tuple(sum(t[0]==i for t in tokens) for i in range(AXES))
    total=D(n)
    if total==0: return {}
    a=tokens[0]
    out=Counter()
    for b,c in combinations(tokens[1:],2):
        if len({a[0],b[0],c[0]})!=3: continue
        tr=tuple(sorted((a,b,c)))
        rest=tuple(t for t in tokens if t not in tr)
        nn=tuple(sum(t[0]==i for t in rest) for i in range(AXES))
        mass=Fraction(D(nn),total)
        if not mass: continue
        for tail,w in rational_sampler(rest).items():
            out[tuple(sorted((tr,)+tail))]+=mass*w
    return dict(out)

def profile_count(m):
    dp=[1]+[0]*(3*m)
    for _ in range(6):
        nxt=[0]*(3*m+1)
        for j,c in enumerate(dp):
            if c:
                for k in range(min(m,3*m-j)+1):
                    nxt[j+k]+=c
        dp=nxt
    return dp[3*m]

def run():
    polys=coeffs()
    profiles=ok=no=0
    for n in product(range(4),repeat=6):
        if sum(n)%3 or sum(n)>12:continue
        profiles+=1
        m=sum(n)//3
        x=D(n)
        numer=polys[m].get(n,0)*prod(factorial(v) for v in n)
        assert numer%factorial(m)==0
        assert x==numer//factorial(m)
        possible=(max(n)<=m)
        assert (x>0)==possible
        witness=greedy(n)
        assert (witness is not None)==possible
        if possible:
            assert len(witness)==m
            assert Counter(i for tr in witness for i in tr)==Counter({i:n[i] for i in range(6) if n[i]})
            ok+=1
        else: no+=1
    examples={}
    for n in [(2,2,2,0,0,0),(1,1,1,1,1,1),(2,1,1,1,1,0),(2,2,1,1,0,0)]:
        tokens=tuple((i,j) for i,v in enumerate(n) for j in range(v))
        actual=brute(tokens)
        masses=rational_sampler(tokens)
        assert len(actual)==D(n) and set(actual)==set(masses)
        assert sum(masses.values())==1 and set(masses.values())=={Fraction(1,len(actual))}
        examples[str(n)]=len(actual)
    family={}
    for m in range(1,9):
        n=(m,m-1,m-1,1,1,0)
        expect=factorial(m)*factorial(m-1)*(2*m-1)
        assert D(n)==expect
        family[m]=expect
    f={}
    for m in range(11):
        formula=comb(3*m+5,5)-6*comb(2*m+4,5)+(15*comb(m+3,5) if m>=2 else 0)
        assert profile_count(m)==formula
        f[m]=formula
    assert (profiles,ok,no)==(1309,1077,232)
    print('R708_TRIADIC_FEASIBILITY_UNIFORM_BRC_EXACT_PASS',profiles,ok,no)
    return dict(marker='R708_TRIADIC_FEASIBILITY_UNIFORM_BRC_EXACT_PASS',profiles=profiles,feasible=ok,infeasible=no,example_D=examples,family=family,F6=f,assumptions='6 axes; equal-q labeled tokens; distinct-axis triples')

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True))
