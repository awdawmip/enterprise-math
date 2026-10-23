#!/usr/bin/env python3
"""C265 compact, standalone exact 5-root / 308-leaf proof replay.

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

LEAF={'B':None,'A':5,'C':50,'D':55,'E':56}
ROOTS=[((0, 21), ('4/543', '43/62', '53/68', '9/11'), ('9/613', '57/79', '38/47', '121/147'), '231013021BDD21BDDD3202CCCDD103DD3DD03DD3DD0130DDDD13DDD103DBDD30112DB2CB1DD11DD1DDC', 42, 222837823719880734794660194768903177), ((0, 15), ('4/543', '43/62', '4/5', '17/21'), ('9/613', '57/79', '38/47', '121/147'), '320131021E03CC3CC1EE21E32CCC1EE203021CCC21CCC02CC2CC32013CCC1CCC20CCC03CC3CC1021E0CC1BC21BC1BC2003CC3CC3CCC1320301CC1CC01CB1CB312CCC1CC03CC3CC2003CCC3CCC3021BBE21BBE021BBED131021E3CC1BE21B0EE1BE20321CCC2CC0CC0CC1021BC1BC21BCE203CCCC132031CC1CB0CC0CC20CCC3021BBE21BBE0DD013120EEE2CE20CCC132CBC3EB1312EEC2CC13CCE201310DDCC31CBC131DCC31CBB013CB3CB13CB3CB', 176, 7469096285338240545368980763778606), ((1, 2), ('3/407', '5/7', '60/77', '4/5'), ('7/477', '31/43', '87/109', '9/11'), '21032E1EE2E31EBD32EE2E3EDE1302103E2EEEE103D3DDEE21EE10EEE031023DD3DD2DDD1DD310DDDD3ED', 43, 66320106200372350631609665116465695), ((1, 18), ('3/407', '5/7', '60/77', '19/24'), ('7/477', '18/25', '53/67', '9/11'), '213E02EE2EEE1033E2EE32E1EE2E10EEE33BE32EE2E0EEE', 24, 195919455141902325189244833104411889), ((29, 33), ('1/93', '12/17', '18/23', '19/24'), ('6/409', '27/38', '72/91', '4/5'), '2103B2BE3BE03BEE3D0121EE13BD3BD2E1EE102EEE0EE', 23, 12795667280526321521856755622965400)]
assert len(ROOTS)==5
allmargin=[];grandleaf=0;grandsplit=0
for pair,low,high,tree,expected_count,expected_margin in ROOTS:
    lo=tuple(F(x) for x in low);hi=tuple(F(x) for x in high)
    assert all(U[k-1]<lo[d]<=hi[d]<U[k+1] for d,k in enumerate(I))
    assert hi[2]<lo[3] and hi[3]<Z
    assert all(lo[d]<hi[d] for d in range(4))
    cursor=[0];margins=[];splits=[0]
    def walk(lo,hi):
        j=cursor[0];assert j<len(tree)
        s=tree[j];cursor[0]+=1
        if s in LEAF:
            k=LEAF[s]
            bound=lower_base(lo,hi) if k is None else lower_shared(k,lo,hi)
            margin=bound.numerator//bound.denominator-Q
            assert margin>0,(pair,j,s,margin)
            margins.append(margin)
            return
        d=int(s);assert 0<=d<4 and lo[d]<hi[d]
        splits[0]+=1;mid=(lo[d]+hi[d])/2
        a=list(hi);a[d]=mid;b=list(lo);b[d]=mid
        walk(lo,tuple(a));walk(tuple(b),hi)
    walk(lo,hi)
    assert cursor[0]==len(tree) and len(margins)==expected_count
    assert len(margins)==splits[0]+1 and min(margins)==expected_margin
    print('C265_STANDALONE_ROOT_PASS',pair,'leaves',len(margins),'minimum',min(margins))
    allmargin.extend(margins);grandleaf+=len(margins);grandsplit+=splits[0]
assert grandleaf==308 and grandsplit==303
assert min(allmargin)==7469096285338240545368980763778606
print('C265_STANDALONE_EXACT_PASS',grandleaf,'strict_leaves',grandsplit,'splits',min(allmargin),'minimum_integer_margin')
