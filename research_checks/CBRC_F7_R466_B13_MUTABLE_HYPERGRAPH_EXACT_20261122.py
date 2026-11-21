#!/usr/bin/env python3
"""Exact 62-packing/62-cover certificate for B13 repair of the frozen F7 B12 witness.

Input: the immutable r464 witness JSON. Standard-library integer enumeration only.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

M = 30_000_000_000_000
TABLE_SHA256 = '340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5'
PACK = [
 [-13,-13,4,-10],[-13,-12,9,-10],[-13,-6,5,-5],[-13,-4,-13,0],
 [-13,-3,-11,9],[-13,-1,-11,12],[-13,0,-12,8],[-13,0,-3,-7],
 [-13,0,1,-12],[-13,0,5,-12],[-13,0,8,0],[-13,0,12,0],
 [-13,2,-9,-2],[-13,3,-8,-7],[-13,4,11,-12],[-13,5,-4,2],
 [-13,6,4,9],[-13,7,-8,8],[-13,8,-9,4],[-13,9,12,-5],
 [-13,10,-12,-3],[-13,11,-4,10],[-12,-13,9,-12],[-12,-1,5,-13],
 [-12,0,0,13],[-12,9,13,0],[-12,11,7,-13],[-11,-13,12,-7],
 [-11,11,13,0],[-10,-3,13,-2],[-10,6,8,-13],[-10,11,11,13],
 [-10,12,-1,13],[-10,13,-5,-3],[-9,-4,13,-10],[-9,13,4,-5],
 [-8,13,8,-3],[-7,7,13,1],[-7,13,3,-6],[-6,13,6,2],
 [-5,13,4,-1],[-4,13,4,3],[-2,-7,-1,-13],[-2,13,4,4],
 [0,-13,11,3],[0,-11,13,12],[1,-2,13,-7],[1,12,3,-13],
 [2,-13,5,5],[3,-12,13,0],[3,2,4,-13],[3,6,13,-9],
 [3,13,7,-3],[4,-9,13,-8],[5,-9,9,-13],[5,-1,13,-5],
 [6,-13,6,6],[6,3,13,13],[6,10,10,-13],[7,9,13,-11],
 [10,-12,13,0],[10,-11,12,13]
]
COVER = ({(13, y) for y in range(-13,14) if y} |
         {(x, y) for x in range(13) for y in (-13, 13)} |
         {(1,-12),(10,-12),(11,11),(17,2),(21,17),
          (27,-7),(34,-21),(38,-25),(47,30),(55,-34)})

def key(x,y):
    return abs(x),y

def mutable(v):
    return v[1]!=0 and v not in ((2,1),(1,-1))

def points(z):
    a,b,c,d=z
    k=a-2*b-c+2*d
    return ((a+k,b+k),(c-k,d-k),(a,b),(c,d))

def verify(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==TABLE_SHA256
    increments={(a,b):n for a,b,n in json.loads(raw)}
    assert len(increments)==2813
    def q(x,y):
        if x==0 and y==0: return 0
        if y==0: return M
        return M//2+increments.get(key(x,y),0)
    def test(z):
        p=points(z)
        support={key(*v) for v in p}
        residual=q(*p[0])+q(*p[1])-q(*p[2])-q(*p[3])
        return support,residual
    old=set()
    for z in itertools.product(range(-12,13),repeat=4):
        support,residual=test(z)
        assert abs(residual)<=M//2
        old.update(support)
    assert len(old)==3073 and len(COVER)==62
    assert COVER<=old and all(mutable(k) for k in COVER)
    old_only_violations=0
    for z in itertools.product(range(-13,14),repeat=4):
        support,residual=test(z)
        if support<=old and abs(residual)>M//2:
            old_only_violations+=1
            assert not support.isdisjoint(COVER), z
    assert old_only_violations==7916
    occupied=set()
    assert len(PACK)==62
    for z in PACK:
        assert all(-13<=c<=13 for c in z)
        support,residual=test(z)
        changeable={k for k in support if mutable(k)}
        assert support<=old and abs(residual)>M//2
        assert changeable and changeable.isdisjoint(occupied), z
        occupied.update(changeable)
    print('CERTIFIED: B13-old-only violation hypergraph on mutable F12 keys')
    print('violations=',old_only_violations,'disjoint_packing=',len(PACK),
          'hitting_cover=',len(COVER),'union_packing_mutable_keys=',len(occupied))
    print('minimum hitting number = maximum disjoint packing number = 62')
    print('Any B13 half-feasible admissible repair of the frozen B12 q must alter >=62 old mutable keys.')

if __name__=='__main__':
    verify(sys.argv[1])
