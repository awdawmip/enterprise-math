#!/usr/bin/env python3
"""R83 exact whole-interval certificate family: source residuals, all-in, all-out."""
from fractions import Fraction as F
from math import floor,ceil
from heapq import heapify,heappop

def out(t,r,q,L,U):
    z=F(1,q)
    assert L<=z<=U and floor(L)==floor(U)==floor(2*L)==floor(2*U)==0
    s0=F(r,q)+min(t*(L-z),t*(U-z))
    s1=F(r,q)+max(t*(L-z),t*(U-z))
    return ceil(s0-max(2*L,2*U))>floor(s1-min(L,U))
def inside_all(t,L,U):
    if floor(t*L)!=floor(t*U):return False
    k=floor(t*L)
    return all(z<=t*z-k<2*z for z in (L,U))
def query_heap(rows,q,L,U):
    heap=[(-t,-r) for t,r in rows];heapify(heap);calls=0
    while heap:
        t,r=heappop(heap);t=-t;r=-r;calls+=1
        if out(t,r,q,L,U):continue
        assert inside_all(t,L,U)
        return ('STABLE',t,calls)
    return ('STABLE_NONE',None,calls)
class N:
    def __init__(self,k,l=None,r=None):
        self.k,self.l,self.r=k,l,r
        self.h=1+max(l.h if l else 0,r.h if r else 0)
def h(n):return n.h if n else 0
def rotl(n):
    r=n.r
    return N(r.k,N(n.k,n.l,r.l),r.r)
def rotr(n):
    l=n.l
    return N(l.k,l.l,N(n.k,l.r,n.r))
def bal(n):
    d=h(n.l)-h(n.r)
    if d>1:
        if h(n.l.l)<h(n.l.r):n=N(n.k,rotl(n.l),n.r)
        return rotr(n)
    if d< -1:
        if h(n.r.r)<h(n.r.l):n=N(n.k,n.l,rotr(n.r))
        return rotl(n)
    return n
def put(n,k):
    if n is None:return N(k)
    if k<n.k:return bal(N(n.k,put(n.l,k),n.r))
    if k>n.k:return bal(N(n.k,n.l,put(n.r,k)))
    return n
def popmax(n):
    if n.r is None:return n.l,n.k
    nr,key=popmax(n.r)
    return bal(N(n.k,n.l,nr)),key
def query_avl(root,q,L,U):
    n=root;calls=0
    while n:
        n,(t,r)=popmax(n);calls+=1
        if out(t,r,q,L,U):continue
        assert inside_all(t,L,U)
        return ('STABLE',t,calls)
    return ('STABLE_NONE',None,calls)

for g in (32,128,512):
    q=g+3;z=F(1,q);L=z;U=z+F(1,1000*q*q)
    for early in (False,True):
        rows=[(q+r,r) for r in range(3,q)]
        if early:rows.append((3*q+1,1))
        tree=None
        for row in sorted(rows):tree=put(tree,row)
        want=('STABLE',3*q+1,1) if early else ('STABLE_NONE',None,g)
        assert query_heap(rows,q,L,U)==query_avl(tree,q,L,U)==want
        for t,r in rows:
            assert inside_all(t,L,U) if early and r==1 else out(t,r,q,L,U)
        for delta in (F(0),F(1,5),F(2,3),F(1)):
            theta=L+delta*(U-L)
            observed=max((t for t,r in rows if theta<=(t*theta)%1<2*theta),default=None)
            assert observed==want[1]
print('R83_MIN_PASS',6)
