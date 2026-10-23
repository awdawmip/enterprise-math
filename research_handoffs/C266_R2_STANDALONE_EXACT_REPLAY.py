#!/usr/bin/env python3
"""C266 R2 standalone exact 3-root / 1029-leaf author proof replay.

No third-party imports. The five preorder trees are fixed certificate data, not
proof authorities: every leaf's rational inequality is recomputed from 79 nodes.
AUTHOR_EXACT, non-native and not independently Driver-admitted.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
I=(5,50,55,56);J=tuple(i for i in range(79) if i not in I)
U=tuple(F(n,d) for n,d in zip(NUM,DEN));Z=F(141421356237309504880,10**20)
A=F(6912*50000**2,17**2);H=2**166;Q=2**128
assert len(U)==79 and all(U[i]<U[i+1] for i in range(78))
B={}
for j in J:
    v=F(Q)*A/H/((2-U[j]*U[j])*(3-U[j]*U[j]))**3
    for r in range(79):
        if r!=j:v*=(Z-U[r])/abs(U[j]-U[r])
    B[j]=v.numerator//v.denominator
    assert B[j]>0

def moving(k,lo,hi,pair=True):
    d=I.index(k);t=(lo[d]+hi[d])/2
    val=F(Q)*A/H/((2-t*t)*(3-t*t))**3
    slope=6*t/(2-t*t)+6*t/(3-t*t)
    for j in J:
        val*=(Z-U[j])/abs(t-U[j]);slope-=1/(t-U[j])
    if pair:
        for p in I:
            if p==k:continue
            dd=I.index(p);e=lo[dd] if p<k else hi[dd]
            val*=(Z-e)/abs(t-e);slope-=1/(t-e)
    return val,val*slope,t

def lower_base(lo,hi):
    total=F(0)
    for j in J:
        v=F(B[j])
        for d,p in enumerate(I):
            e=lo[d] if j>p else hi[d]
            v*=(Z-e)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-e)
        total+=v
    for d,k in enumerate(I):
        v,der,t=moving(k,lo,hi,pair=False)
        x=max(F(0),v+der*((lo[d] if der>=0 else hi[d])-t))
        for dd,p in enumerate(I):
            if p==k:continue
            if k<p:x*=(Z-hi[dd])/(hi[dd]-lo[d])
            else:x*=(Z-lo[dd])/(hi[d]-lo[dd])
        total+=x
    return total

def lower_shared(k,lo,hi):
    d=I.index(k);s=(lo[d]+hi[d])/2
    value=F(0);slope=F(0)
    for j in J:
        v=F(B[j])
        for dd,p in enumerate(I):
            if p==k:continue
            e=lo[dd] if j>p else hi[dd]
            v*=(Z-e)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-e)
        v*=(Z-s)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-s)
        value+=v;slope+=v*(-1/(Z-s)-1/(s-U[j]))
    v,der,_=moving(k,lo,hi)
    value+=v;slope+=der
    value+=slope*((lo[d] if slope>=0 else hi[d])-s)
    for p in I:
        if p==k:continue
        dd=I.index(p);v,der,t=moving(p,lo,hi)
        value+=v+der*((lo[dd] if der>=0 else hi[dd])-t)
    return value


import json
from pathlib import Path
CERT=json.loads(Path(__file__).with_name("C266_R2_COMPACT_EXACT_CERTIFICATE.json").read_text())
assert CERT['schema']=='EM_C266_R2_AUTHOR_EXACT_CERTIFICATE_V1'
assert CERT['new_positive_pairs']==[[4,16],[4,26],[4,30],[12,29],[27,30]]
LEAF={'B':None,'A':5,'C':50,'D':55,'E':56}
allmins=[];nleaves=0;nsplits=0
for root in CERT['roots']:
    pair=root['pair'];lo=tuple(F(x) for x in root['lo']);hi=tuple(F(x) for x in root['hi'])
    assert all(U[I[d]-1]<lo[d]<=hi[d]<U[I[d]+1] for d in range(4))
    assert hi[2]<lo[3] and hi[3]<Z
    tree=root['tree'];pos=[0];margins=[];leaves=[0];splits=[0]
    def walk(lo,hi):
        i=pos[0];assert i<len(tree);token=tree[i];pos[0]+=1
        if token in '0123':
            d=int(token);assert lo[d]<hi[d];mid=(lo[d]+hi[d])/2
            upper=list(hi);upper[d]=mid
            lower=list(lo);lower[d]=mid
            splits[0]+=1
            walk(lo,tuple(upper));walk(tuple(lower),hi)
        else:
            assert token in LEAF
            k=LEAF[token]
            lb=lower_base(lo,hi) if k is None else lower_shared(k,lo,hi)
            gap=lb.numerator//lb.denominator-Q
            assert gap>0,(pair,i,token,gap)
            margins.append(gap);leaves[0]+=1
    walk(lo,hi)
    assert pos[0]==len(tree)
    assert leaves[0]==root['leaves'] and splits[0]+1==leaves[0]
    assert min(margins)==int(root['margin'])
    print('C266_R2_EXACT_ROOT_PASS',pair,leaves[0],min(margins),flush=True)
    nleaves+=leaves[0];nsplits+=splits[0];allmins.extend(margins)
assert nleaves==1029 and nsplits==1026 and min(allmins)==int(CERT['global_minimum_integer_margin'])
assert CERT['counts']['before']=={'negative':213,'positive':103,'unknown':47}
assert CERT['counts']['after']=={'negative':213,'positive':108,'unknown':42}
print('C266_R2_AUTHOR_EXACT_PASS',nleaves,nsplits,min(allmins))
