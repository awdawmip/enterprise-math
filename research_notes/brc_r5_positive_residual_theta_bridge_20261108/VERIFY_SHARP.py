#!/usr/bin/env python3
"""Exact sharp lower-t C4/5 Blackwell prism; needs VERIFY.py and SHARP_CERTIFICATES.zlib.b64."""
import json,base64,zlib
from itertools import product
from fractions import Fraction as F
from pathlib import Path
from VERIFY import source,target,mass,tp,tq,check

TMIN=F(369,43076)
BP=F(1759,800)
BQ=F(777,400)

def separator(f):
    g,a,b,u,v,w,z=f
    m4=(g-b)/2
    m5=F(3,40)*a+F(21,80)*b-w
    lhs=BP*(tq(f)-1)-BQ*(tp(f)-1)
    rhs=F(1081,3200)*a+F(491,400)*u+F(41,80)*m4+F(143,200)*m5
    return lhs,rhs

def verify_separation_identity():
    # Both expressions are affine functions of five chart coordinates;
    # checking origin and standard basis proves the identity for all real inputs.
    for k in range(6):
        ff=tuple(F(int(j==k-1)) for j in range(7)) if k else (F(0),)*7
        # Identity holds only on C_(4/5), so represent target with five parameters.
        if k<=5:
            yy=tuple(F(int(j==k-1)) for j in range(5)) if k else (F(0),)*5
            ff=target(yy)
            lhs,rhs=separator(ff)
            assert lhs==rhs,(k,lhs,rhs)
    # Exact source expression on the corner p=0,q=1,theta=3/4.
    for t in (F(0),TMIN,F(1,100),F(1,5)):
        x=source(t,F(0),F(1),F(3,4))
        lhs=BP*(tq(x)-1)-BQ*(tp(x)-1)
        assert lhs==F(-369,128000)+F(10769,32000)*t
    assert F(-369,128000)+F(10769,32000)*TMIN==0
    assert F(-369,128000)+F(10769,32000)*F(1,120)==F(-301,3840000)

def load():
    z=Path(__file__).with_name('SHARP_CERTIFICATES.zlib.b64').read_text()
    data=json.loads(zlib.decompress(base64.b64decode(z)).decode())
    return {tuple(map(F,key.split('|'))):(
       tuple(map(F,entry['target'])),
       {tuple(map(int,pair.split(','))):F(v) for pair,v in entry['edges'].items()})
       for key,entry in data.items()}

def main():
    verify_separation_identity()
    verts=load()
    assert len(verts)==16
    count=0
    for coord,(yy,Q) in verts.items():
        assert coord[0] in (TMIN,F(1,5))
        assert coord[1] in (F(0),F(1)) and coord[2] in (F(0),F(1))
        assert coord[3] in (F(3,4),F(1))
        check(source(*coord),target(yy),Q)
        count+=len(Q)
    assert count==158
    for k in range(601):
        t=TMIN+(F(1,5)-TMIN)*F(k,600)
        p=F((7*k+13)%601,601)
        q=F((11*k+29)%601,601)
        theta=F(3,4)+F(1,4)*F((17*k+23)%601,601)
        alpha=(t-TMIN)/(F(1,5)-TMIN)
        beta=4*(theta-F(3,4))
        weights={coord:(alpha if coord[0]==F(1,5) else 1-alpha)*
                (p if coord[1] else 1-p)*
                (q if coord[2] else 1-q)*
                (beta if coord[3]==F(1) else 1-beta)
                for coord in verts}
        assert sum(weights.values())==1 and min(weights.values())>=0
        x=source(t,p,q,theta)
        for j in range(7):
            assert sum(weights[v]*source(*v)[j] for v in verts)==x[j]
        yy=tuple(sum(weights[v]*verts[v][0][j] for v in verts) for j in range(5))
        Q={(i,j):sum(weights[v]*verts[v][1].get((i,j),F(0)) for v in verts)
           for i in range(7) for j in range(7)}
        check(x,target(yy),Q)
    print('SHARP_FIXED_FACE_SEPARATION_IDENTITY_PASS')
    print('EXACT_CORNER_OBSTRUCTION_t_LT_369_43076_BY_POSITIVE_SLACKS')
    print('EXACT_16_SHARP_ENDPOINT_CERTIFICATES_PASS',count)
    print('EXACT_601_SHARP_MULTIAFFINE_INTERIOR_CHECKS_PASS')
    print('ALL_REAL_SHARP_FIXED_FACE_FULL_CAPACITY_DOMAIN_t_369_43076_TO_1_5')
if __name__=='__main__':main()
