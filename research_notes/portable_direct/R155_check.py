#!/usr/bin/env python3
"""Exact finite checks of R155 reversal cuts and infinite three-1 alias family.
External S23 finite mechanical-word observer. No native X6 claim.
"""
from fractions import Fraction
from math import gcd,lcm
from collections import defaultdict
import json


def stats(w):
    m=len(w)
    s=[0]
    for bit in w:s.append(s[-1]+bit)
    a=Fraction(0);b=Fraction(1)
    for i in range(m):
        for j in range(i+1,m+1):
            count=s[j]-s[i]
            a=max(a, Fraction(count-1,j-i))
            b=min(b, Fraction(count+1,j-i))
    if a>=b:return None
    U=min(a.denominator*(t+1)-j*a.numerator for j,t in enumerate(s))
    V=max(b.denominator*t-j*b.numerator for j,t in enumerate(s))
    return (a,b,U,V,s)


def fiber(d,L):
    a,b,U,V,_=d
    def ceil_div(x,y):return -((-x)//y)
    return ceil_div(L*b.numerator-V,b.denominator)-((L*a.numerator-U)//a.denominator)-1


def test_reversal():
    words=0;unequal=0;equal=0;cut_alias=0;count_alias=0;triples=0;nontrivial=0
    for m in range(1,13):
        for x in range(1<<m):
            w=f'{x:0{m}b}';d=stats([int(c) for c in w]);
            if d is None:continue
            words+=1
            a,b,U,V,s=d
            rev=w[::-1];dr=stats([int(c) for c in rev]);assert dr is not None
            assert (a,b)==dr[:2]
            # Formula: reversed min/max envelopes
            U_reverse=b.denominator*(s[-1]+1)-m*b.numerator if False else a.denominator*(s[-1]+1)-m*a.numerator-max(a.denominator*t-j*a.numerator for j,t in enumerate(s))
            V_reverse=b.denominator*s[-1]-m*b.numerator-min(b.denominator*t-j*b.numerator for j,t in enumerate(s))
            assert (U_reverse,V_reverse)==dr[2:4]
            # Observed equivalence in one affine period
            P=lcm(a.denominator,b.denominator)
            same=all(fiber(d,L)==fiber(dr,L) for L in range(1,P+1))
            if a.denominator!=b.denominator:
                unequal+=1
                assert same==((U,V)==dr[2:4]), (m,w,d,dr)
                if same:cut_alias+=int(w!=rev)
            else:equal+=1
            if same:count_alias+=int(w!=rev)
    return dict(words_checked=words,unequal_endpoint_words=unequal,equal_endpoint_words=equal,reversal_distinct_count_alias_words=count_alias,reversal_distinct_equal_cut_words=cut_alias)


def test_three_ones(maxh=60):
    counts=0; checkpoints=0; threshold_checks=0
    sample={}
    for h in range(2,maxh+1):
        A='1'+'0'*(h-1)+'1'+'0'*h+'1'
        B='1'+'0'*h+'1'+'0'*(h-1)+'1'
        assert A!=B and A[::-1]==B
        da=stats([int(c) for c in A]);db=stats([int(c) for c in B])
        expect=(Fraction(1,h+1),Fraction(1,h),h+1,h-1)
        assert da[:4]==db[:4]==expect, (h,da,db)
        # large and residue-sensitive inputs; this exact count formula holds for all L by cuts
        for L in [1,2,h,h+1,h*h-1,h*h+1,10**40+17,10**60+31]:
            f=fiber(da,L);g=fiber(db,L)
            assert f==g and f>=0
            counts+=1
        if h in (2,3,4,10,60):sample[str(h)]={'words':[A,B] if h<=4 else None,'alpha':str(da[0]),'beta':str(da[1]),'U':da[2],'V':da[3],'C_at_L1':fiber(da,1)}
        assert fiber(da,h*h-1)==0 and fiber(da,h*h)>=1
        for L in range(h*h,h*(h+1)+1):
            assert fiber(da,L)>=1 and fiber(db,L)>=1
            threshold_checks+=1
        checkpoints+=1
    return dict(h_range=[2,maxh],families=checkpoints,exact_count_comparisons=counts,threshold_checks=threshold_checks,samples=sample)


def test_all_identity_groups():
    ans=[]
    for m in range(1,13):
        groups=defaultdict(list)
        for x in range(1<<m):
            w=f'{x:0{m}b}';d=stats([int(c) for c in w]);
            if d is not None:groups[(d[0],d[1],d[2],d[3])].append(w)
        collisions=[v for v in groups.values() if len(v)>1]
        ans.append({'m':m,'word_count':sum(map(len,groups.values())),'equal_cut_collision_pairs':sum(len(v)*(len(v)-1)//2 for v in collisions),'max_equal_cut_group':max([len(v) for v in collisions],default=1)})
    return ans

if __name__=='__main__':
    payload={'marker':'R155_REVERSAL_AND_THREE_ONE_FAMILY_EXACT_PASS','observer':'EXTERNAL_TIED_PHASE_S23','verification_kind':'exact_integer_fraction_finite_regression','reversal':test_reversal(),'three_one':test_three_ones(),'groups':test_all_identity_groups(),'review':'NOT_REVIEWED','scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34'}
    with open('/mnt/data/R155_verification.json','w') as f:json.dump(payload,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:v for k,v in payload.items() if k!='groups'},ensure_ascii=False,indent=2))
    print('collision_pairs_total',sum(x['equal_cut_collision_pairs'] for x in payload['groups']))
