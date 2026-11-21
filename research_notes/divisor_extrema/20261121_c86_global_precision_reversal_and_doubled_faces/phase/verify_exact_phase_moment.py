#!/usr/bin/env python3
"""Meaningful exact checks of the rational-basis phase/radial algorithm."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import hashlib
import json

from exact_phase_moment import curve, moment_terms, compare, evaluate

HERE=Path(__file__).resolve().parent


def curve_value(intervals, scale, sigma):
    x=sigma/scale
    if x >= F(1,intervals[-1][1]):
        return F(1)
    for left,right,poly in intervals:
        lo=F(0) if left is None else F(1,left)
        hi=F(1,right)
        if lo <= x <= hi:
            return sum(c*x**k for k,c in enumerate(poly))
    raise AssertionError((sigma,intervals))


def direct_phase_volume(A,d,p,q,sigma):
    """Integrate all endpoint-eligible integer vectors without pruning.

    The coordinate bound follows directly from |sigma*Bn|_infinity<=1.
    Nonprimitive vectors are included as a separate check of that reduction.
    """
    a,b,c,e=A
    radius=F(d,sigma)
    mb=int(radius*(abs(e)+abs(b))/(d*d))
    nb=int(radius*(abs(c)+abs(a))/(d*d))
    marks=[]
    for m in range(-mb,mb+1):
        for n in range(-nb,nb+1):
            if not(m or n):continue
            u=F(sigma*(a*m+b*n),d)
            v=F(sigma*(c*m+e*n),d)
            if max(abs(u),abs(v))>1:continue
            marks.append((u,F(q-p,q)*u+F(p,q)*v,v))
    cuts=[]
    for j in (0,2):
        values={F(0),F(1)}
        for row in marks:
            for z in (-row[j],1-row[j]):
                if 0<z<1:values.add(z)
        cuts.append(sorted(values))
    volume=F(0)
    for l,h in zip(cuts[0],cuts[0][1:]):
        x=(l+h)/2
        for low,high in zip(cuts[1],cuts[1][1:]):
            y=(low+high)/2
            middle=[row[1]for row in marks if 0<x+row[0]<1 and 0<y+row[2]<1]
            if F(0) in middle:continue
            positive=min([F(1)]+[z for z in middle if z>0])
            negative=min([F(1)]+[-z for z in middle if z<0])
            volume+=(h-l)*(high-low)*max(F(0),positive+negative-1)
    return volume


def check_continuity(intervals):
    assert intervals[0][0] is None and intervals[0][2][0] == 0
    for first,second in zip(intervals,intervals[1:]):
        assert first[1]==second[0]
        x=F(1,first[1])
        assert sum(c*x**i for i,c in enumerate(first[2])) == sum(c*x**i for i,c in enumerate(second[2]))
    x=F(1,intervals[-1][1])
    assert sum(c*x**i for i,c in enumerate(intervals[-1][2]))==1


def main():
    square_positions=[(1,4),(1,2),(1,3),(2,5),(3,4)]
    for p,q in square_positions:
        intervals,metadata=curve((1,0,0,1),1,p,q)
        t=min(F(p,q),1-F(p,q))
        for left,right,poly in intervals:
            lo=F(0) if left is None else F(1,left)
            hi=F(1,right)
            if q*(lo+hi)/2<F(1,2):
                expected=(0,0,0,2*t*q**3)
            else:
                expected=(1,(-6+2*t)*q,(10-4*t)*q*q,(-4+2*t)*q**3)
            assert poly==expected
        check_continuity(intervals)
    cases=[('square',(1,0,0,1),1,1),
           ('rotated_square',(3,-4,4,3),5,-1),
           ('shear',(2,1,0,2),2,-1),
           ('rectangle',(1,0,0,4),2,-1)]
    phase_checks=0
    for name,A,d,sign in cases:
        for p,q in ((1,4),(1,2)):
            intervals,metadata=curve(A,d,p,q)
            check_continuity(intervals)
            for sigma in (F(1,4),F(1,2),F(2,3),F(1),F(3,2)):
                expected=direct_phase_volume(A,d,p,q,sigma)
                assert curve_value(intervals,q*d,sigma)==expected
                phase_checks+=1
        result=compare(A,d)
        lo,hi=map(F,result['difference']['interval'])
        assert (lo>0 if sign>0 else hi<0)
        target=HERE/(name+'_exact.json')
        target.write_text(json.dumps(result,indent=2)+'\n')
    square=json.loads((HERE/'square_exact.json').read_text())
    expression={F(row['base']):F(row['coefficient'])for row in square['difference']['moment_terms']}
    assert expression=={F(1):F(100,7161),F(1,2):-F(5,462)}
    # Same square shape, changed physical orientation.
    A=(3,-4,4,3)
    assert A[0]**2+A[2]**2==25 and A[1]**2+A[3]**2==25
    assert A[0]*A[1]+A[2]*A[3]==0
    # A right unimodular shear relabels the identical lattice; the exact
    # moments must remain unchanged despite a different covering-radius box.
    for p,q in ((1,4),(1,2)):
        c1,_=curve((3,-4,4,3),5,p,q)
        c2,_=curve((3,-1,4,7),5,p,q)
        assert moment_terms(c1,5*q)==moment_terms(c2,5*q)
    result={'schema':'C86_RATIONAL_PHASE_VALIDATION_V1','status':'PASS',
            'all_interval_square_formula_positions':len(square_positions),
            'unpruned_complete_endpoint_integrations':phase_checks,
            'certified_example_signs':{'square':'+','rotated_square':'-','shear':'-','rectangle':'-'},
            'C85_square_expression_reproduced':True,
            'same_shape_rotation_verified':True,'unimodular_relabeling_checks':2,
            'proof_arithmetic':'integers and Fraction; integer tenth-root bisection',
            'implementation_sha256':hashlib.sha256((HERE/'exact_phase_moment.py').read_bytes()).hexdigest()}
    (HERE/'exact_phase_validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
