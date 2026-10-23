#!/usr/bin/env python3
"""C266 compact, standalone exact 3-root / 735-leaf proof replay.

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
ROOTS=[((4, 16), ('2/271', '7/10', '60/77', '4/5'), ('6/409', '42/59', '11/14', '9/11'), '120312EE2E0EE32C10EE0EE2C10EE0EE312BE2EE32C1EE2C0CC0312030EE0EE3E1EE0301EE1EE01E2E3E0BE1E2E3E1EE31E2EE102EEE20EE03E1EE3E1EE2030EE01EE1EE3E1EE0301EE1EE012E3E0BE2E3E0BE12E31EE1EE2E31EE1EE312E0EE2E0EE120EE031EE10EE0EE31EE1E2EE20EE031EE10EE0EE31EE12EEE312001EE1EE1E3EE00132EEE32E0BE2EE132EEE32E1EE2E1EE132E0EE2E0EE320EE01E0EE1EE20EE01EE1EE2003CC31EEC312EE2EE2CC00312E0BE2E0BE21EE10BE0BE312E10EE0EE2E30CC0CC21EE11EE3CC31201EEE010EE03EE3EE13EE3EE203CCE030C2CC0CC32CC2CC210EE0EE101E0EE1EE030CCC3CC21003CB3CB3CC030CCC3CC01301EE1EEC302CC2CCC131E2EEC32C0CCC31023EE31EE1E2E0EE2E3E0EE023E1EE31EE12E03E1EEE2E03E1EEE23EE30EE0EE31021EE132EEE32E01EEE2E0EE20EE0EE0231EEC312E01EEE2E03CCE21EE101EEE03CCE20EE03CCE0213CB3CB131EEC32CCC21EE10EE0EE2032E1EE132B0EE2BE32BE2BE32E1EE132BE2BE3EE031203E0EE3E1EE0301EE1EE012E3E0BE2EE12E3E1EE2EE312EEE120EE031EE10EEE3E1EE2E03E1EEE203EEE030EE01EE1EE3E12EEE312001EE1EE13EEE00132E0BE2E0BB32EE2EE132E1EE2E1EE32EE2EE1320EE010EE0EE13EEE20EE01EE1EE32E01EE1EE2E0EE200EE1EE0013EEE13EEE132EE2EEE21030CCC3CB00EEE10302CC2CCC32C1EEC003CB3CB3CB31023EE31EE12E0EE2EE2E3E0EE02E3E1EE2E3EE31021EE132E01EEE2E0EE32EE2EE20EE0EE02E13EEE2E0EE0213CBE132CCC3CB21EE10EEE', 581, 5158902987695659637439900477932651), ((12, 29), ('3/371', '7/10', '18/23', '19/24'), ('6/409', '27/38', '53/67', '4/5'), '23C012C3C01CCC2C3C0CC12C0CC2C0CC3011DD1DDC01230CC012CC2C0CC12CC2CC30CC0120CC0CC20CC0CC12CC2C3CC23C012CCC12CCC30CC0120CC0CC2CC12CC2CC1203C1CC3CC03C1C2CC3C1CC203CC3CC03C12CCC3CC', 88, 46890424184761894156170614618712718), ((23, 29), ('1/104', '34/49', '18/23', '19/24'), ('6/409', '27/38', '34/43', '4/5'), '23011BCC11BCC011E2C3CC2C3CC11E0CC02CCC3011BDC11BDC0112EE23C01BCC3C02C1BC2CC23C102CCC0CC3C012C3CC2CC12CC2CC11E02C3CC2CE023CC3CC2C3CC', 66, 25754627181721861699725646546279580)]
assert len(ROOTS)==3
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
    print('C266_STANDALONE_ROOT_PASS',pair,'leaves',len(margins),'minimum',min(margins))
    allmargin.extend(margins);grandleaf+=len(margins);grandsplit+=splits[0]
assert grandleaf==735 and grandsplit==732
assert min(allmargin)==5158902987695659637439900477932651
print('C266_STANDALONE_EXACT_PASS',grandleaf,'strict_leaves',grandsplit,'splits',min(allmargin),'minimum_integer_margin')
