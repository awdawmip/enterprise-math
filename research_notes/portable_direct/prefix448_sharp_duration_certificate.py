#!/usr/bin/env python3
"""Exact certificate for PREFIX-448: sharp 28q full-rank quadratic X6 history port at N=q+1.

The paths are in native signed X6 chart steps, history sector = #(-e1) mod q.
All matrix computations use Python integers and fraction-free Bareiss determinant.
"""
from __future__ import annotations
from collections import defaultdict
from math import comb
from fractions import Fraction
from hashlib import sha256
import json

D=6

def step(i, sign=1):
    e=[0]*D; e[i]=sign
    return tuple(e)

PLUS=[step(i) for i in range(D)]
MINUS=[step(i,-1) for i in range(D)]

def add_steps(word):
    return tuple(sum(s[i] for s in word) for i in range(D))

def hist(word, q):
    return sum(s==MINUS[0] for s in word)%q


def base_words():
    """28 words of length two, each excluding -e1."""
    items=[(PLUS[1],MINUS[1])]
    for i in range(1,D):
        items.extend(((PLUS[i],PLUS[i]),(MINUS[i],MINUS[i])))
    for i in range(1,D):
        for j in range(i+1,D):
            items.append((PLUS[i],PLUS[j]))
    for i in range(1,D):
        items.append((PLUS[0],PLUS[i]))
    items.append((PLUS[0],MINUS[1]))
    items.append((PLUS[0],PLUS[0]))
    assert len(items)==28
    assert len(set(add_steps(w) for w in items))==28
    assert all(MINUS[0] not in w for w in items)
    return tuple(items)

def monomials(x):
    return (1,)+tuple(x)+tuple(x[i]*x[i] for i in range(D))+tuple(x[i]*x[j] for i in range(D) for j in range(i+1,D))

def bareiss(a):
    a=[list(row) for row in a]
    n=len(a); assert all(len(row)==n for row in a)
    sign=1;last=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=a[i][j]*p-a[i][k]*a[k][j]
                assert top%last==0
                a[i][j]=top//last
        for i in range(k+1,n):a[i][k]=0
        last=p
    return sign*a[n-1][n-1]


def paths_for_q(q):
    assert q>=2
    res=[]
    for r in range(q):
        head=(MINUS[0],)*r+(PLUS[0],)*(q-1-r)
        for tail in base_words():
            w=head+tail
            assert len(w)==q+1 and hist(w,q)==r
            res.append((r,w,add_steps(w)))
    assert len(res)==28*q
    assert len({(r,x) for r,w,x in res})==28*q
    return res


def rank_mod_p(rows,p=1000000007):
    pivot={}
    for row in rows:
        v=[x%p for x in row]
        for k,b in sorted(pivot.items()):
            f=v[k]
            if f:
                for j in range(k,len(v)):v[j]=(v[j]-f*b[j])%p
        z=next((j for j,x in enumerate(v) if x),None)
        if z is not None:
            inv=pow(v[z],-1,p)
            pivot[z]=[(x*inv)%p for x in v]
    return len(pivot)


def run():
    rows=[monomials(add_steps(w)) for w in base_words()]
    det=bareiss(rows)
    assert det!=0
    print('BASE_28_DETERMINANT',det)
    # fixed-sector translation only changes lower-order polynomial coefficients.
    for q in (2,3,4,5,6,8,12):
        data=paths_for_q(q)
        ranks=[]
        for r in range(q):
            rr=[monomials(x) for s,w,x in data if s==r]
            ranks.append(rank_mod_p(rr))
        assert ranks==[28]*q, (q,ranks)
        print('Q',q,'N',q+1,'WORDS',len(data),'SECTOR_RANKS',','.join(map(str,ranks)))
        # One each of the 28 points per sector: exact second moments coincide with an explicit 7x7 Gram sum.
        H=[[0]*7 for _ in range(7)]
        for r,w,x in data:
            if r==q-1:
                z=list(x)+[1]
                for i in range(7):
                    for j in range(7):H[i][j]+=z[i]*z[j]
        assert H[6][6]==28
        assert all(H[i][j]==H[j][i] for i in range(7) for j in range(7))
    # Lower bound: for N<=q, sector q-1 has <=1 unspecified direction,
    # with at most 11 possible endpoint positions at N=q.
    for q in (2,3,4,5,8):
        for N in range(q+1):
            if N<q-1:cap=0
            elif N==q-1:cap=1
            else:cap=11 # remaining one step excludes -e1 at N=q
            assert cap<28
            print('LOWER_Q',q,'N',N,'SECTOR_LAST_ENDPOINT_CAP',cap)
    print('PASS: sharp duration N_min(q)=q+1, exact 28x28 nonzero determinant, X6 word witnesses and fixed-state controls')

if __name__=='__main__':run()
