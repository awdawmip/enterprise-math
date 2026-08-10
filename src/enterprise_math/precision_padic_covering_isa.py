"""R004 p-adic precision-native covering ISA.

Finite exact reference helpers for additive primitive instructions over
R = Z/p^K with Hamming readout cost. General coding over finite chain rings is
prior mathematics; R004 owns only the typed compiler interpretation.
"""
from __future__ import annotations
from itertools import combinations, product
from math import comb, ceil
from typing import Sequence, Tuple

Vector=Tuple[int,...]

def alphabet_size(p:int, cap:int)->int:
    if p<2 or cap<1: raise ValueError("invalid p/cap")
    return p**cap

def hamming_ball_volume(p:int, cap:int, length:int, radius:int)->int:
    q=alphabet_size(p,cap)
    if length<0 or not 0<=radius<=length: raise ValueError("invalid length/radius")
    return sum(comb(length,j)*(q-1)**j for j in range(radius+1))

def volume_lower_bound_length(p:int, cap:int, rank:int, radius:int)->int:
    if rank<1 or radius<1: raise ValueError("invalid rank/radius")
    q=alphabet_size(p,cap)
    s=rank
    while hamming_ball_volume(p,cap,s,min(radius,s)) < q**rank:
        s+=1
    return s

def depth_one_exact_length(p:int, cap:int, rank:int)->int:
    if rank<1: raise ValueError("rank must be positive")
    return p**((cap-1)*(rank-1))*((p**rank-1)//(p-1))

def one_null_radius(p:int, cap:int, rank:int)->int:
    q=alphabet_size(p,cap)
    n=rank+1
    return n-ceil(n/q)

def one_null_depth_gain(p:int, cap:int, rank:int)->int:
    return rank-one_null_radius(p,cap,rank)

def fixed_depth_storage_power_inequality(p:int, cap:int, rank:int, radius:int, storage:int)->bool:
    if not (1<=radius<rank) or storage<1: raise ValueError("invalid arguments")
    return (radius+1)*(storage**radius) >= p**(cap*(rank-radius))

def reachable(columns:Sequence[Vector], modulus:int, radius:int)->frozenset[Vector]:
    if modulus<2 or radius<0 or not columns: raise ValueError("invalid arguments")
    r=len(columns[0])
    if any(len(c)!=r for c in columns): raise ValueError("ragged columns")
    out={(0,)*r}
    n=len(columns)
    for j in range(1,min(radius,n)+1):
        for inds in combinations(range(n),j):
            for coeffs in product(range(1,modulus),repeat=j):
                v=[0]*r
                for idx,a in zip(inds,coeffs):
                    c=columns[idx]
                    for t in range(r):
                        v[t]=(v[t]+a*c[t])%modulus
                out.add(tuple(v))
    return frozenset(out)

def covers(columns:Sequence[Vector], modulus:int, radius:int)->bool:
    r=len(columns[0])
    return len(reachable(columns,modulus,radius))==modulus**r
