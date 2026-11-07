#!/usr/bin/env python3
"""Pure-stdlib exact checker for R5 pair A10+B10 convex-hull equality.
No optimization library, floating point, or pretrusted facets at verification time.
"""
from fractions import Fraction as F
from math import gcd
from itertools import permutations
from pathlib import Path
import json

N = ('A','B','A0','A1','B0','B1','A00','A01','A10','A11','B00','B01','B10','B11')
S = ((1,120,240,-1),(1,240,120,-1),
     (2,60,180,0),(2,60,60,0),(2,180,60,1),(2,60,60,1),
     (3,30,108,2),(3,30,72,2),(3,30,45,3),(3,30,15,3),
     (3,90,36,4),(3,90,24,4),(3,20,40,5),(3,40,20,5))
keys=[]; idx=[]
for t,p,q,_ in S:
    g=gcd(p,q); key=(t,p//g,q//g)
    if key not in keys: keys.append(key)
    idx.append(keys.index(key))
assert len(keys)==12 and idx[3]==idx[5] and idx[9]==idx[13]
assert sum(S[i][1] for i in (0,1))==sum(S[i][2] for i in (0,1))==360
for i in range(6):
    children=[row for row in S if row[3]==i]
    assert len(children)==2
    assert sum(c[1] for c in children)==S[i][1]
    assert sum(c[2] for c in children)==S[i][2]

def observe(mask,lr=False):
    live=[False]*14
    r=x=y=s=0
    for i,(t,p,q,parent) in enumerate(S):
        reach=parent<0 or live[parent]
        stop=reach and bool(mask&(1<<(idx[i] if lr else i)))
        live[i]=reach and not stop
        if stop:
            if i in (9,13):r+=q
            x+=(4-t)*p
            y+=(4-t)*q
            if i in (8,12):s+=p
    return (r,x,y,s)

for i,(t,p,q,_) in enumerate(S):
    L=F(p,q)
    qerr=F(2,5)-F(t,30)+F(t+2,200)*L+(F(1,1000) if i in (9,13) else F(0))
    pbase=F(1,5)+F(t,20)+F(t+1,100)/L
    assert 0<qerr<1
    for delta in (F(1,1000),-F(1,1000)):
        perr=pbase+(delta if i in (8,12) else 0)
        assert 0<perr<1
    if t==3:
        p4=F(1,5)+F(4,20)+F(5,100)/L
        q4=F(2,5)-F(4,30)+F(6,200)*L
        assert 0<p4<1 and 0<q4<1

full=[observe(k) for k in range(1<<14)]
lr=[observe(k,True) for k in range(1<<12)]
full_set=set(full);lr_set=set(lr)
assert len(full_set)==647 and len(lr_set)==272
assert lr_set.issubset(full_set)

path=Path(__file__).with_name('R5_PAIR_A10_B10_CERT.jsonl')
cert={}
with path.open(encoding='utf-8') as f:
    for lineno,line in enumerate(f,1):
        v=json.loads(line)
        key=tuple(v['full'])
        assert len(key)==4 and all(type(n) is int for n in key)
        assert key not in cert
        mask=v['full_mask_example']
        assert 0<=mask<(1<<14) and full[mask]==key
        mixture=v['lr_mixtures']
        assert 1<=len(mixture)<=5
        weights=[]
        support=set()
        for m,num,den in mixture:
            assert type(m) is type(num) is type(den) is int
            assert 0<=m<(1<<12) and den>0 and num>0
            assert m not in support
            support.add(m)
            weights.append(F(num,den))
        assert sum(weights)==1
        for k in range(4):
            assert sum(w*lr[entry[0]][k] for w,entry in zip(weights,mixture))==key[k],(lineno,k)
        cert[key]=True
assert set(cert)==full_set,('coverage',len(cert),len(full_set))

def determinant4(rows):
    s=0
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        v=(-1 if inv%2 else 1)
        for i in range(4):v*=rows[i][p[i]]
        s+=v
    return s
witness_masks=[0,1,2,128,256]
pts=[lr[m] for m in witness_masks]
D=determinant4([[pts[i][k]-pts[0][k] for k in range(4)] for i in range(1,5)])
assert D==408240000

# Original fixed (eP,eQ,TP,TQ) observer from the exact stopping model:
# TP=4-x/360, TQ=4-y/360,
# eP=21/100+TP/20+TQ/100+delta*s/360,
# eQ=41/100+TP/200-TQ/30+eta*r/360.
# For eta=1/1000 and every real admissible delta != 0, this is
# an invertible affine transformation of (r,x,y,s), since its Jacobian
# has nonzero product of the time x/y conversion, eta and delta.
# Every behavioral strategy's observer is multiaffine: each key is
# visited at most once. Product interpolation over binary keys
# places its observer in the convex hull of deterministic masks.
print('TREE nodes=14 LR_keys=12 exact collisions A1/B1,A11/B11')
print('PROBABILITIES eta=1/1000 delta=+/-1/1000 strict=True')
print('EXACT_FULL_MASKS 16384 DISTINCT_FULL_VECTORS',len(full_set))
print('EXACT_LR_MASKS 4096 DISTINCT_LR_VECTORS',len(lr_set))
print('EXACT_CARATHEODORY_CERTIFICATES',len(cert),'each_support_at_most_5=True')
print('LR_AFFINE_RANK_4_DET',D,'masks',','.join(map(str,witness_masks)))
print('HULL_IDENTITY conv(FULL)=conv(LR) in (r,x,y,s) exact=True')
print('ORIGINAL_FOUR_OBSERVER_HULL_IDENTITY all admissible real delta != 0, eta=1/1000 exact=True')
print('ACTUAL_REAL_BEHAVIORAL_IMAGE_EQUALITY not_established')
print('PASS_EXACT_R5_PAIR_A10_B10_RANK4_HULL_EQUALITY')
