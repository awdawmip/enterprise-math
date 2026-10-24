#!/usr/bin/env python3
"""C284 exact 12-bit dyadic threshold-crossing certificates for 187 hulls.

Run from this directory with C284_C275_FROZEN_SOURCE.py:
    python C284_EXACT_DYADIC_ROOT_BRACKETS.py
Only Fraction arithmetic is used for decisions. Author proof, not native BRC.
"""
import json
from fractions import Fraction
from hashlib import sha256
import C284_C275_FROZEN_SOURCE as c

N=12
DEN=1<<N

def point(w,h,t):
    return tuple(a+t*(b-a) for a,b in zip(w,h))

def produce():
    assert len(c.U)==79 and len(c.D)==35 and len(c.I)==4
    assert len(c.P)==2
    hulls=c.classify()
    assert len(hulls)==595
    weights,_=c.fixed_data()
    def value(v):return c.direct(v,weights)
    for w in c.P:
        assert c.admissible(w)
        assert 1000*value(w)<999*c.Q
    records=[]
    touches=inner=0
    for (i,j),(lo,hi,kind) in sorted(hulls.items()):
        if kind=='safe':continue
        available=[s for s,w in enumerate(c.P) if c.inside(w,lo,hi)]
        if not available:continue
        s=available[0]
        w,h=c.P[s],c.positive_point(lo,hi)
        assert c.admissible(h) and c.inside(h,lo,hi)
        assert c.active(55,h)+c.active(56,h)>3*c.Q
        left,right=0,DEN
        for step in range(N):
            mid=(left+right)//2
            assert left<mid<right
            v=point(w,h,Fraction(mid,DEN))
            assert c.admissible(v) and c.inside(v,lo,hi)
            sign=value(v)-c.Q
            if sign<0:left=mid
            elif sign>0:right=mid
            else:raise AssertionError("exact dyadic root at "+repr((i,j,mid)))
        assert right-left==1
        a,b=point(w,h,Fraction(left,DEN)),point(w,h,Fraction(right,DEN))
        assert c.admissible(a) and c.admissible(b)
        assert c.inside(a,lo,hi) and c.inside(b,lo,hi)
        assert value(a)<c.Q<value(b)
        records.append([i,j,s+1,left])
        touches+=kind=='touch';inner+=kind=='cross'
    assert len(records)==187 and (touches,inner)==(111,76)
    assert len({(r[0],r[1]) for r in records})==187
    digest=sha256(json.dumps(records,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    result={
      'schema':'C284_DYADIC_THRESHOLD_BRACKETS_V1',
      'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
      'parent':'C275_AUTHOR_EXACT_187_MIXED',
      'n':N,'denominator':DEN,'total':187,
      'touch':touches,'cross':inner,'exact_midpoint_roots':0,
      'certificate_sha256':digest,
      'encoding':'[box_i,box_j,witness_1_based,k]: F(v(k/4096))<Q<F(v((k+1)/4096)); no uniqueness claimed',
      'records':records,'formal_Source_claim':False,'driver_admitted':False,
      'native_BRC_or_X6_transfer':False}
    return result

if __name__=='__main__':
    result=produce()
    with open('C284_187_EXACT_DYADIC_BRACKETS.json','w',encoding='utf-8') as fp:
        json.dump(result,fp,ensure_ascii=False,indent=2);fp.write('\n')
    print('C284_DYADIC_187_PASS', result['total'], result['touch'],result['cross'],result['certificate_sha256'])
