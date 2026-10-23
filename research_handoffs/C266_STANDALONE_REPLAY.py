#!/usr/bin/env python3
"""C266 standalone exact six-root / 1530-leaf rational auxiliary proof replay.

No third-party imports. Six preorder trees are certificate data, not proof
authorities: every leaf's rational inequality is recomputed from 79 nodes.
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
ROOTS=[([23, 29], ['1/104', '34/49', '18/23', '19/24'], ['6/409', '27/38', '34/43', '4/5'], '23011BCC11BCC011E2C3CC2C3CC11E0CC02CCC3011BDC11BDC0112EE23C01BCC3C02C1BC2CC23C102CCC0CC3C012C3CC2CC12CC2CC11E02C3CC2CE023CC3CC2C3CC', 66, 25754627181721861699725646546279580), ([12, 29], ['3/371', '7/10', '18/23', '19/24'], ['6/409', '27/38', '53/67', '4/5'], '23C012C3C01CCC2C3C0CC12C0CC2C0CC3011DD1DDC01230CC012CC2C0CC12CC2CC30CC0120CC0CC20CC0CC12CC2C3CC23C012CCC12CCC30CC0120CC0CC2CC12CC2CC1203C1CC3CC03C1C2CC3C1CC203CC3CC03C12CCC3CC', 88, 46890424184761894156170614618712718), ([23, 28], ['1/104', '34/49', '18/23', '4/5'], ['2/137', '7/10', '34/43', '9/11'], '1203E1BEE031BE1B3ED3E1BE20321EE1E03EEE321EE1E02E3EE2EE2E1E0EE302EEE302E1EE2EE2E0EE0321E032EE21EE1E0EE3E2E1EE103EEE0321EE1EE21E03E2EE3EE1E03E2E1EE3E2EE32EE21E0EE1E03E2EEE3210EE0231EEE31E0EE1EE23EE31EEE102EEE0231E02EE2EE1EE31E02E3EE2EE1E0EE231EEE31E02EEE1EE12EE203EB3EB03DB3DB3021EE1E3E2EE2E1EE3021E2EE1E2E3EE21EE1EE01D2EE1DD', 162, 1788669815076504029785421006152887), ([27, 30], ['2/189', '7/10', '32/41', '4/5'], ['3/205', '12/17', '37/47', '17/21'], '21032BE2EE3E0EE032BE2E1EE3E0EE10312E03E1EEE2E03E1E2EE3E1EE120EE032E1EE2E1E0EE3E2EE2031EE1E2EEE0312E0EE2E03E1EEE12E302EEE02EEE203EEE301E2EE1EE012EE2EE1EE31E2EE12EE2E3EE301EEE012EE2EE1EE03120EE031EE12EE2E0EE3E1EE20EE031EE12E0EE2E0EE3E1EE12031EE12EE2EE3E1EE0312E031EE12EE2EE3E1EE20EE031EE12EE2EE3E1EE1203E1EEE3012EE2E0EE1E2EE012E3EE2E30EE0EE12EE2EE2031EE1EE3EE3012E03EEE2E03EEE12EE2EE012E30EE0EE2E301EEE01EEE12EE2EE312EE2EE12E30EE0EE2E301EEE01EEE2031EE12EE2EE3E1EE03120EE031EE12EE2EE3E1EE20EE031EE12EE2EE3E1EE12031EE1EE3EE3012E03E1EEE2E03E1EEE12EE2EE012E301EEE01EEE2E301EEE01EEE12EE2EE2031EE1EE3EE3012E03EEE2E03EEE12EE2EE021EE1301EEE01EEE30EE0EE2E1EE312E0EE2EE12E301EEE01EEE2E301EEE01EEE3012EE2EE1EE012E3E1EE2E3E1EE12EE2EE', 360, 4638422976475146033089763949860511), ([16, 28], ['1/119', '16/23', '18/23', '13/16'], ['3/205', '12/17', '15/19', '9/11'], '13021A23AA300CCCA13DD3202C0CC2CC020C3CC0C3CC23CC3CC202CCC01DD1BD21E02EEE10DD032C2CCD3DD021D2AA1D32AAD21BD1D0DD3202301CCC0CC30102CC2C3CC2C0C3CC12C3CC2C3CC012CC2CC1CC023CC31CCC2C3CC02301203CC3CC031CCC31C2CCC203CC31CCC0312CC2CCC312C3CC2CCC1230CCC301C2CCC0CC230CCC3012CC2CC1CC0CC0120CC0CC20CC0CC12C3CC2C3CC3012031C2CCC312CC23CC3CC1C2CC031C2C0CC1CC312CC20C3CC03CC3CC1C2CC20312C0CC2CCC3123CC30CCC23CC30CCC12CC2CC03120CC0CC20CC0CC12CC2CC31230CCC03CC31CCC230CCC30CCC12C0CC2CC12301C2C3CC1C2CC01CCC3012CC23CC30CCC1C2CC01C2CC1CC230123CC3CC23CC3CC12CC2CC012CC2CCC301230CCC301CCCC230CCC30CCC123CC3CC23CC3CC012CC2CC1CC0120C3CC03CC3CC20C3CC03CC3CC123CC3CC23CC30CCC02312C3CC2C3CC1CC31230CCC30CCC230CCC301CCCC12CC2CC231C0CBC310CB0CBC2023CC30CCC2C0CC02301CCCC301CC1CCC203CCC03CCC', 381, 1441085415662878829686364295197984), ([4, 26], ['2/271', '7/10', '60/77', '4/5'], ['6/409', '42/59', '11/14', '13/16'], '12032C1EE12E0EE2E0EE32BC12BE2EE031203C0EE3CE030CC01EE1E2EE31EE12EE2E0EE203C0CC3C3CC030CC012EE2EE12EE2EE33CC12E03C1EEE2E03C3CCE32010EE01EE1EE11EE1EE0101E2E3E0BB1E2E3E3CC012E30BB0BB2E30BB0BB12E31EE3CC2E33CC3CC112E0EE20EE031EE3CC3E1EE1203EEE031EE30CC0CC31EE3CC203CCE033CC30CC0CC33CC3CC20101EE3CC03CC3CC132CCC32CCC01032C1E0BB2C1EE32C1E3CC2C1EE032C10BB0BB2C10BB0BB32C13CC3CC2C13CC3CC13201EEC01E3CC1E3CC20CC01E3CC1E3CC32013CCCC0130CC0CC30CCC13CC3CC20CC013CC3CC13CC3CC3102E3C1E2EE2E3C0EE02E3C12EE2EE2E3C0CC1023E3CC31E2E0EE32C1E0EE2C0CC23EE30EE0EE0231EE3CC312E03E3CCE2E03C3CCE32C013CC3CCC2C01CCC23E0CB30EE0CC2032B1EE2E1EE32BE2E1EE031203C0EE3CE030CC012EEE12EEE33CC12E0EE2EE20EE03E0EE3E1EE12030EE03CC3CC31EE3CC03012E3E0BB2EE12E3E3CC2EE032C10BBE2C10BBE32C13CCE2C13CCE3120EE031EE3CC31EE3CC2E03E3CCE320CC013CC3CC13CCE20CC013CCE13CCE203E0EE3EE0301EE1EE01EE1EE312EEE12E0EEE3102E3C12EEE2E3C0EB02EE2EE1023E3CC312E03EEE2EE32C01EEC2C0CC23EE30EE0EE02E31EE1EE2E3E0EB', 473, 903503865712265886784690054399388)]
import os
if 'C266_ROOT_IDX' in os.environ: ROOTS=[ROOTS[int(os.environ['C266_ROOT_IDX'])]]
proof_leaves=0;proof_splits=0;all_margins=[]
for pair,low,high,tree,expected_leaves,expected_margin in ROOTS:
    lo=tuple(F(x) for x in low);hi=tuple(F(x) for x in high)
    assert all(U[k-1]<lo[d]<=hi[d]<U[k+1] for d,k in enumerate(I))
    assert hi[2]<lo[3] and hi[3]<Z
    cursor=[0];margins=[];splits=[0]
    def walk(lo,hi):
        assert cursor[0]<len(tree)
        tok=tree[cursor[0]];cursor[0]+=1
        if tok in LEAF:
            k=LEAF[tok]
            lb=lower_base(lo,hi) if k is None else lower_shared(k,lo,hi)
            margin=lb.numerator//lb.denominator-Q
            assert margin>0,(pair,cursor[0],margin)
            margins.append(margin);return
        axis=int(tok)
        assert 0<=axis<4 and lo[axis]<hi[axis]
        splits[0]+=1
        mid=(lo[axis]+hi[axis])/2
        h=list(hi);h[axis]=mid
        l=list(lo);l[axis]=mid
        walk(lo,tuple(h));walk(tuple(l),hi)
    walk(lo,hi)
    assert cursor[0]==len(tree) and len(margins)==expected_leaves
    assert len(margins)==splits[0]+1 and min(margins)==expected_margin
    print('C266_INDEPENDENT_STANDALONE_ROOT_PASS',pair,'leaves',len(margins),'minimum',min(margins),flush=True)
    proof_leaves+=len(margins);proof_splits+=splits[0];all_margins.extend(margins)
assert proof_splits==proof_leaves-len(ROOTS)
print('C266_INDEPENDENT_STANDALONE_EXACT_PASS',proof_leaves,proof_splits,min(all_margins),flush=True)
