#!/usr/bin/env python3
"""Independent exact-integer verification of sharp sector-quadratic branch theorem."""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb

def signature(n,q,ks):
    by_sector=defaultdict(lambda:[0,0,0,0])
    for k in ks:
        x=n-2*k
        t=by_sector[k%q]
        for j in range(4): t[j]+=x**j
    return tuple(tuple(by_sector[r][:3]) for r in range(q))

def cubic_sector(n,q,ks):
    by_sector=defaultdict(int)
    for k in ks: by_sector[k%q]+=(n-2*k)**3
    return tuple(by_sector[r] for r in range(q))

def legal(n,ks):
    return all(ks.count(k)<=comb(n,k) for k in set(ks))

def sharp(q,n):
    if n<3*q: return None
    if n<4*q: return 4
    return 3

def witnesses(q,n):
    if n<3*q: return None
    if n<4*q:
        return (0,2*q,2*q,2*q),(q,q,q,3*q),48*q**3
    return (0,3*q,3*q),(q,q,4*q),96*q**3

def first_collision(n,q,m):
    seen={}
    for ks in combinations_with_replacement(range(n+1),m):
        if not legal(n,ks):continue
        key=signature(n,q,ks)
        other=seen.get(key)
        if other is not None and other!=ks:
            return other,ks
        if other is None:seen[key]=ks
    return None

def main():
    checked=0; witness=0; exhaustive=0
    for q in range(1,9):
        for n in range(0,5*q+5):
            expected=sharp(q,n)
            w=witnesses(q,n)
            if w is not None:
                A,B,gap=w
                assert legal(n,A) and legal(n,B),(q,n,A,B)
                assert signature(n,q,A)==signature(n,q,B),(q,n)
                assert sum(cubic_sector(n,q,A))-sum(cubic_sector(n,q,B))==gap,(q,n)
                assert len(A)==len(B)==expected
                witness+=1
            sizes=[len(range(r,n+1,q)) if r<=n else 0 for r in range(q)]
            rank=sum(min(3,a) for a in sizes)
            assert rank==min(n+1,3*q)
            assert (rank<n+1)==(expected is not None)
            checked+=1
    for q in range(1,4):
        for n in range(0,4*q+3):
            threshold=sharp(q,n)
            for m in range(1,5):
                collision=first_collision(n,q,m)
                assert (collision is not None)==(threshold is not None and m>=threshold),(q,n,m,collision,threshold)
                exhaustive+=1
    print('PASS')
    print(f'rank_cases={checked} legal_witnesses={witness} exhaustive_branch_probes={exhaustive}')
    print('sharp q=1: n<3 none; n=3 four; n>=4 three')
    print('sharp q=2: n<6 none; n=6,7 four; n>=8 three')

if __name__=='__main__':main()
