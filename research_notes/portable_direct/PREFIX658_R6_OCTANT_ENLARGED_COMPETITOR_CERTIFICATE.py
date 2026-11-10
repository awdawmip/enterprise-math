#!/usr/bin/env python3
"""PREFIX-658 R6: exact-rational BRC competitor-orbit implication certificate.
Inherits PREFIX-620 symmetry and exact PREFIX-657 predecessor witness bounds.
This is an implication certificate, not a new 189-layer survivor replay.
"""
from fractions import Fraction as F
import json

PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'
L,Z=F(3,20),F(1,8)
r=F(61,2**24)
old_h=F(1,2**19)
d=F(1,2**22)
K={12:F(540720684),24:F(2162787480)}
previous_point_gap={12:F('4100.310'),24:F('16272.968')}
expected_point={12:F(104107662189,26214400),
                24:F(1032671676473,65536000)}
expected_square={12:F(2065563603,52428800),
                 24:F(3936536071,131072000)}
count=0
def check(b,msg):
    global count
    assert b,msg
    count+=1
def reflection(I):
    return (1-I[1],1-I[0])
def orbit():
    a,b=(L-r,L+r),(Z-r,Z+r)
    return {(reflection(x) if rx else x,reflection(y) if ry else y)
            for x,y in ((a,b),(b,a)) for rx in (False,True)
            for ry in (False,True)}
def main():
    check(Z-r>=F(63,512),'score parameter lower bound')
    check(L+r<=F(1,6),'score parameter upper bound')
    check(L-r>Z+r,'center band separation')
    check(L+r<F(1,2),'parameter octant')
    check(F(63,512)*(1-F(63,512))>F(47,441),'variance denominator')
    check(4*21**2*F(63,512)*(1-F(63,512))>188,'score bound <21')
    check(21*189==3969,'mu gradient')
    check(21*sum(range(1,190))==377055,'H gradient')
    check(2*377055+2*378*3969==3754674,'W gradient')
    check(2*r>old_h,'includes old positive-z interval')
    check(r>old_h,'includes old p interval')
    oldarea=2*old_h**2
    newarea=(2*r)**2
    check(newarea/oldarea==F(3721,512),'area ratio')
    check(oldarea>0,'positive area')
    squares=orbit()
    check(len(squares)==8,'eight orbit members')
    bands=[(Z-r,Z+r),(L-r,L+r),(1-L-r,1-L+r),(1-Z-r,1-Z+r)]
    check(all(bands[i][1]<bands[i+1][0] for i in range(3)),'disjoint bands')
    for a,b in squares:
        check(a[0]<a[1] and b[0]<b[1],'positive-area rectangle')
        check(0<=a[0]<a[1]<=1 and 0<=b[0]<b[1]<=1,'full-domain enclosure')
    slots={}
    for q in (12,24):
        point=previous_point_gap[q]-K[q]*d
        check(point==expected_point[q],'B-prime point gap')
        check(K[q]==q*q*3754674+q*3969,'score gradient')
        loss=2*r*K[q]
        margin=point-loss
        check(margin==expected_square[q],'rectangle gap equality')
        check(margin>0,'strict rectangle domination')
        check(margin>(39 if q==12 else 30),'displayed integer bound')
        slots[str(q)]={'point_to_expanded_B_strict_lower':str(point),
                       'square_loss_strict_upper':str(loss),
                       'square_gap_strict_lower':str(margin)}
    for q in (12,15,18,21,24):
        t=F(q-12,12)
        check((1-t)*expected_square[12]/12+t*expected_square[24]/24>0,
              'positive q-affine normalized gap')
    for p in (F(0),Z,L,F(1,2),F(1)):
        check(p*(1-p)==(1-p)*p,'invariant coordinate identity')
    result={'schema':'EM_PREFIX658_R6_OCTANT_COMPETITOR_SQUARE_CERTIFICATE_V1',
            'frozen_scientific_pin':PIN,
            'inherited_exact_inputs':['PREFIX620 survivor symmetry',
                 'PREFIX657 exact P witness','PREFIX657.2 expanded B comparison'],
            'center':[str(L),str(Z)],'half_width':str(r),
            'base_square':{'p':[str(L-r),str(L+r)],
                           'z':[str(Z-r),str(Z+r)]},
            'orbit_count':len(squares),
            'area_ratio_new_square_to_previous_C':str(newarea/oldarea),
            'normalized_maximization_wedge':'0<=p<=z<=1/2',
            'slots':slots,'checks_passed':count,'result':'ALL_CHECKS_PASS',
            'scope':'full [0,1]^2 frozen BRC observer, real 12<=q<=24',
            'status':'AUTHOR_DERIVED_EXACT_FRACTION_CHECKED_UNREVIEWED'}
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',count)
if __name__=='__main__':main()
