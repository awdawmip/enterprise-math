#!/usr/bin/env python3
"""R5 primitive-16/17 exact cyclotomic certificates, standard library only."""
import json
from fractions import Fraction as Q
from math import gcd, lcm

def ring(p):
    d = 8 if p == 16 else p-1
    zero=(Q(0),)*d
    one=(Q(1),)+(Q(0),)*(d-1)
    def add(x,y):return tuple(a+b for a,b in zip(x,y))
    def scale(x,c):return tuple(c*a for a in x)
    def mul(x,y):
        v=[Q(0)]*p
        for i,a in enumerate(x):
            if a:
                for j,b in enumerate(y):
                    if b:v[(i+j)%p]+=a*b
        if p==16:return tuple(v[i]-v[i+8] for i in range(8))
        return tuple(v[i]-v[-1] for i in range(p-1))
    def mon(k):
        k%=p
        if p==16:return tuple((Q(1) if k==j else -Q(1) if k==j+8 else Q(0)) for j in range(8))
        return tuple(Q(int(j==k)-int(k==p-1)) for j in range(p-1))
    def inv(r):
        n=p//gcd(p,r)
        x=zero
        for j in range(1,n):x=add(x,scale(mon(r*j),-Q(j,n)))
        assert mul(add(one,scale(mon(r),-1)),x)==one
        return x
    return zero,one,add,scale,mul,mon,inv

sets=[set(range(214,219)),{214,216,217,218,219,220,221},set(range(215,222)),set(range(223,291)),set(range(296,313))]
Z,I,add,scale,mul,mon,inv=ring(16)
a16=add(add(mul(mul(inv(219),inv(220)),inv(221)),inv(215)),inv(214))
a16=add(a16,scale(I,-2))
expected16=(Q(-1),Q(1,2),Q(0),Q(1,2),Q(-1),Q(0),Q(0),Q(1))
assert a16==expected16
multiples16=[p for p in range(214,315) if p%16==0]
assert multiples16==[224,240,256,272,288,304]
independent=Z; order6_masks=[]
for mask in range(1,32):
    union=set().union(*(sets[j] for j in range(5) if mask>>j&1))
    if all(p not in union for p in multiples16):
        order6_masks.append(mask)
        val=I
        for p in range(214,222):
            if p not in union:val=mul(val,inv(p%16))
        independent=add(independent,scale(val,(-1)**(mask.bit_count()+1)))
assert independent==a16
assert set(order6_masks)=={1,2,3,4,5,6,7}

Z17,I17,add17,scale17,mul17,mon17,inv17=ring(17)
complement=[r for r in range(1,17) if r not in range(10,15)]
assert complement==[1,2,3,4,5,6,7,8,9,15,16]
coeff=[I17]
for r in complement:
    nxt=[Z17]*(len(coeff)+1)
    for j,v in enumerate(coeff):
        nxt[j]=add17(nxt[j],v)
        nxt[j+1]=add17(nxt[j+1],scale17(mul17(v,mon17(r)),-1))
    coeff=nxt
assert len(coeff)==12 and all(any(c) for c in coeff)
witness=[]
for v in coeff:
    idx=next(i for i,a in enumerate(v) if a)
    witness.append((idx,int(v[idx])))
assert witness==[(0,1),(0,1),(0,1),(0,2),(1,-1),(0,-1),(0,1),(3,-1),(0,-1),(1,-1),(8,-1),(8,-1)]
max_m=34
h=[Z17]*max_m;h[0]=I17
for r in range(10,15):
    zz=mon17(r)
    for j in range(1,max_m):h[j]=add17(h[j],mul17(zz,h[j-1]))
b=Z17
for m in range(1,max_m+1):
    b=add17(b,h[m-1])
    j=(m-1)%17
    assert b==(coeff[j] if j<12 else Z17),m
multiples17=[p for p in range(214,315) if p%17==0]
assert multiples17==[221,238,255,272,289,306]
assert all(p not in sets[0] for p in multiples17)
for mask in range(2,32):
    union=set().union(*(sets[j] for j in range(5) if mask>>j&1))
    assert len(set(multiples17)-union)<=5
for d in range(19,315):
    assert sum(p%d==0 for p in range(214,315))<=5
assert all(sum(p%d==0 for p in range(214,315))<=6 for d in (15,16,17,18))
assert lcm(*range(1,19))==12252240
assert lcm(360360,16,17)==12252240
out={'schema':'R5_PRIMITIVE16_17_V1','status':'PASS',
'primitive16':{'m':1,'pole_order':6,'A16_phi16_basis':[str(x) for x in a16],'order6_inclusion_exclusion_masks':order6_masks,'free_multiples':multiples16},
'primitive17':{'free_multiples':multiples17,'pole_order':6,'S0_only_at_order6':True,'numerator_complement_residues':complement,'nonzero_threshold_m_mod17':list(range(1,13)),'zero_threshold_m_mod17':[0,13,14,15,16],'coefficient_witnesses':witness,'independent_DP_threshold_range':[1,max_m]},
'min_cost_period_for_m1_at_remainder_O_N4':12252240,'independent_review':'NOT_REVIEWED'}
print(json.dumps(out,indent=2,sort_keys=True))
