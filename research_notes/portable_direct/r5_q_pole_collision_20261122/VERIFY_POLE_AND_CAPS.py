#!/usr/bin/env python3
"""Pure-integer certificate of R5 Q=2L pole collision and sharp exception bounds.
Optional --packed path checks the immutable archive's original 1092 jets.
"""
import argparse, base64, hashlib
from collections import Counter
from itertools import product
from math import lcm
from pathlib import Path

W = (7,9,11,13,16,17,19,23,25,27,31,37)
NEEDED = tuple(d for d in W if d != 9)
MU_EXPECTED = {7:3,9:3,11:3,13:3,16:2,17:2,19:2,23:1,25:2,27:3,31:3,37:2}
R0_MASKS = {
    7:'00000000000000000000000', 9:'00000000000000000000000',
    11:'73d863fc663fc61bce09ef9', 13:'427fde8e0f3fdc6539ffff0',
    16:'7ffffffffffffffffffffff', 17:'7d9ffd9fe8ff47be71f70ff',
    19:'7ffffffffffffffffffffff', 23:'0fdfff7fffffffe7feffeff',
    25:'7fffffffff3eb7fffffffff', 27:'00000000000000000000000',
    31:'00000000000000000000000', 37:'7ffffffffffffffffffffff'
}
S = [s for s in range(1,79809)
     if s%58 in (0,54,55,56,57)
     and s%64 in (0,60,61,62,63)
     and s%43 in (0,37,38,39,40,41,42)]
L=229746052653717600
K=L//(29*2*43)
Q=2*L
assert len(S)==91 and lcm(*NEEDED)==K and all(Q%(2*d)==0 for d in W)
assert lcm(*(2*d for d in W),79808)==Q

# Disjoint sorted cones, with ties resolved by original index.
for x,y,j in product(range(10),repeat=3):
    a=(x,y,j)
    order=sorted(range(3),key=lambda i:(-a[i],i))
    top,mid,low=[a[i] for i in order]
    assert top>=mid>=low
    assert top-mid>0 or order[0]<order[1]
    assert mid-low>0 or order[1]<order[2]
    assert x+y+j-max(x,y,j)==mid+low
    assert x+y+j == (top-mid)+2*(mid-low)+3*low

MU={}
for d in W:
    best=0
    for r in (219,220,221):
        sum3=214+215+r
        for a,b in ((214,215),(214,r),(215,r)):
            lin=(0,216,217,218,a+b)
            for j in range(2*d):
                mult=sum((2*n+j)%(2*d)==0 for n in lin)
                mult+=int((sum3+j)%d==0)
                best=max(best,mult)
    MU[d]=best
assert MU == MU_EXPECTED, MU

# Archived finite-field R0 nonzero bitmasks: bit i corresponds to S[i].
# Use --packed to revalidate every mask and the original 1092 base witnesses.
parser=argparse.ArgumentParser()
parser.add_argument('--packed',type=Path)
args=parser.parse_args()
if args.packed:
    blob=base64.b64decode(args.packed.read_text())
    assert len(blob)==4368
    assert hashlib.sha256(blob).hexdigest()=='2a728abf89c6d6756b738458ac0e47499f2e0b6ef64d44aa217354ca4ff5175a'
    for ix,d in enumerate(W):
        bitmask=0
        for si in range(91):
            start=4*(91*ix+si)
            r0=int.from_bytes(blob[start:start+2],'little')
            r1=int.from_bytes(blob[start+2:start+4],'little')
            assert r0 or r1,(d,S[si])
            if d==37: assert r0,(d,S[si])
            if r0: bitmask|=1<<si
        assert bitmask==int(R0_MASKS[d],16),(d,'R0 mask mismatch')
    print('ARCHIVED 1092 BASELINE JETS SHA256 / MASKS VERIFIED')
else:
    print('ARCHIVED R0 MASK MODE; --packed validates the original immutable bytes')

bounds=[]
for i,s in enumerate(S):
    caps={}
    for d in NEEDED:
        zero_nonzero=(int(R0_MASKS[d],16)>>i)&1
        if zero_nonzero or d in (7,27,31,37):
            caps[d]=MU[d]-1
        else:
            caps[d]=MU[d]
    bounds.append((s,sum(caps.values()),caps))
distribution=Counter(c for _,c,_ in bounds)
assert distribution=={15:16,16:47,17:21,18:7},distribution
assert sum(c for _,c,_ in bounds)==1475
assert max(c for _,c,_ in bounds)==18
assert int(R0_MASKS[23],16).bit_count()==82
print('MAX POLE ORDERS',MU)
print('CAP FREQUENCIES',dict(sorted(distribution.items())))
print('TOTAL POSSIBLE EXCEPTIONS <= 1475 ; PER PROGRESSION <=18')
print('23rd-order constant nonzero R0 on 82 of 91 progressions')
print('ALL CHECKS PASS')
