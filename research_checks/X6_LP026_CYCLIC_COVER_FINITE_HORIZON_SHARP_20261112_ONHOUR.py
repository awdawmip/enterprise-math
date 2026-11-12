#!/usr/bin/env python3
"""Exact finite-horizon observer-safety and BRC descent checks for signed X6."""
from collections import defaultdict
from math import factorial

D=6

def cover(z,m):
    h=min(z)
    return (tuple(x-h for x in z),h%m)

def norm(z): return sum(x*x for x in z)
def brc_short(z):
    n=sum(map(abs,z)); out=factorial(n)
    for x in z: out//=factorial(abs(x))
    return out

def witness(m,k):
    z=(-m-k,-m,-m,0,0,0)
    return z,tuple(x+m for x in z)

def boundary_brc_witness(m):
    t=(m,m,0,1,1,m-2)
    z=tuple(-x for x in t)
    return z,tuple(x+m for x in z)

def test_formulas():
    tests=0
    for m in range(1,16):
        x,y=witness(m,0)
        assert cover(x,m)==cover(y,m)
        assert sum(map(abs,x))==sum(map(abs,y))==3*m
        assert norm(x)==norm(y)==3*m*m
        assert brc_short(x)==brc_short(y)
        tests+=1
        for k in range(1,16):
            x,y=witness(m,k)
            n=3*m+k
            assert cover(x,m)==cover(y,m)
            assert sum(map(abs,x))==sum(map(abs,y))==n
            assert norm(x)-norm(y)==2*m*k
            assert brc_short(y)==brc_short(x)*__import__('math').comb(m+k,m)
            tests+=1
        if m>=3:
            x,y=boundary_brc_witness(m)
            assert cover(x,m)==cover(y,m)
            assert sum(map(abs,x))==sum(map(abs,y))==3*m
            assert norm(x)==norm(y)
            assert brc_short(x)!=brc_short(y)
            assert brc_short(x)*m==brc_short(y)*2*(m-1)
            tests+=1
    return tests

def enumerate_shells(max_n=9):
    dist={(0,)*D:1}
    checks=0; worst=0; classifications=[]
    for n in range(max_n+1):
        worst=max(worst,len(dist))
        for m in range(1,5):
            fibers=defaultdict(list)
            for z in dist:
                fibers[cover(z,m)].append(z)
            expect_collision=(n>=3*m)
            expect_norm=(n>=3*m+1)
            expect_brc=(n>=3*m+1 or (m>=3 and n>=3*m))
            has_collision=has_norm=has_brc=False
            for zlist in fibers.values():
                if len(zlist)>1:
                    has_collision=True
                    if len({norm(z) for z in zlist})>1:has_norm=True
                    if len({dist[z] for z in zlist})>1:has_brc=True
                checks+=1
            assert has_collision==expect_collision,(n,m,'collision')
            assert has_norm==expect_norm,(n,m,'norm')
            assert has_brc==expect_brc,(n,m,'brc')
            classifications.append((n,m,len(fibers),has_collision,has_norm,has_brc))
        if n<max_n:
            nxt=defaultdict(int)
            for z,count in dist.items():
                for i in range(D):
                    plus=list(z);plus[i]+=1;nxt[tuple(plus)]+=count
                    minus=list(z);minus[i]-=1;nxt[tuple(minus)]+=count
            dist=dict(nxt)
    return checks,worst,classifications

if __name__=='__main__':
    formulas=test_formulas()
    checked,max_shell,rows=enumerate_shells(9)
    print('PASS_X6_CYCLIC_FINITE_HORIZON_SHARP')
    print('formula_exact_witness_cases=',formulas)
    print('distinct_cover_key_cases=',checked)
    print('max_endpoint_shell_size=',max_shell)
    for r in rows:
        if r[0] in (3,4,6,7,9):print('N,m,classes,collision,norm_unsafe,brc_unsafe=',*r)
    x,y=boundary_brc_witness(3)
    print('m3_N9_endpoint_witness=',x,y,'norms=',norm(x),norm(y),'BRC=',brc_short(x),brc_short(y))
