#!/usr/bin/env python3
"""R5 Q(a,b,d): exact first moments, centroid and atlas-escape mean.
Only standard-library fractions; source: PR #1866 abstract 7-facet polytope,
PR #1859 exact fixed-marginal coupling identification/cost.
"""
from fractions import Fraction as F
from math import factorial

ZERO = F(0)
def poly(k): return {(0,0): F(k)}
def varx(): return {(1,0): F(1)}
def vary(): return {(0,1): F(1)}
def add(p,q):
    o = dict(p)
    for e,c in q.items(): o[e] = o.get(e,ZERO)+c
    return {e:c for e,c in o.items() if c}
def scale(p,c): return {e:c*v for e,v in p.items() if c*v}
def mul(p,q):
    o={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():o[i+k,j+l]=o.get((i+k,j+l),ZERO)+a*b
    return {e:c for e,c in o.items() if c}
def integ(p):
    return sum((c*F(factorial(i)*factorial(j),factorial(i+j+2)) for (i,j),c in p.items()),ZERO)

def add3(*pp):
    o={}
    for p in pp:o=add(o,p)
    return o

def calc(a,b,d):
    L1,L2=F(23,13)*a,F(23,18)*a
    B=add(poly(23*b),scale(varx(),23*a))
    D=add(poly(23*d),scale(vary(),F(115,18)*a))
    B2,BD,D2=mul(B,B),mul(B,D),mul(D,D)
    area=scale(add3(scale(B2,25),scale(BD,180),scale(D2,117)),F(1,20700))
    B3,B2D,BD2,D3=mul(B2,B),mul(B2,D),mul(B,D2),mul(D2,D)
    Mu=scale(add3(scale(B3,7375),scale(B2D,48600),scale(BD2,63180),scale(D3,27378)),F(1,128547000))
    Mv=scale(add3(scale(B3,250),scale(B2D,2700),scale(BD2,9720),scale(D3,6903)),F(1,14283000))
    V=L1*L2*integ(area)
    moments=(L1*L2*L1*integ(mul(varx(),area)),L1*L2*L2*integ(mul(vary(),area)),L1*L2*integ(Mu),L1*L2*integ(Mv))
    return V, tuple(m/V for m in moments)

def independent_polygon_moments(B,D):
    pts=((ZERO,ZERO),(B/18,ZERO),((10*B+13*D)/115,(5*B+18*D)/115),(ZERO,D/10))
    area=mu=mv=ZERO
    for i,j,k in ((0,1,2),(0,2,3)):
        (x1,y1),(x2,y2),(x3,y3)=(pts[i],pts[j],pts[k])
        t=((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
        assert t>0
        area+=t;mu+=t*(x1+x2+x3)/3;mv+=t*(y1+y2+y3)/3
    return area,mu,mv

for B,D in ((F(1),F(2)),(F(5,3),F(7,11)),(F(1,100),F(10))):
    A,U,V=independent_polygon_moments(B,D)
    assert A == (25*B*B+180*B*D+117*D*D)/20700
    assert U == (7375*B**3+48600*B*B*D+63180*B*D*D+27378*D**3)/128547000
    assert V == (250*B**3+2700*B*B*D+9720*B*D*D+6903*D**3)/14283000

A=F(3997,690000); B=F(170189123,37621284000); D=F(8294919533,677183112000)
vol, means=calc(A,B,D)
assert vol == F(17113607962497316638837165221,503876396283588297216000000000000000)
expected=(F(2355585076519534536727043,652766585956905903520171875),
F(35502889966272874093017097,14461290519660684631831500000),
F(1464603788539721806976442485094641,90675386274443700028094716941000000),
F(181049273329192438370158704401311,7254030901955496002247577355280000))
assert means==expected
c=F(225713944957,3385915560000)
escape=c+F(28,23)*means[1]+F(5,23)*means[2]+F(13,23)*means[3]
assert escape==F(688104890147354659193365423065427,7884816197777713045921279734000000)
assert c<escape<F(8555233477,73606860000)
for aa,bb,dd in ((F(1),F(1),F(1)),(F(1,2),F(3,4),F(2,5))):
    v,m=calc(aa,bb,dd)
    closed=F(12167,90979200)*aa**2*(2125*aa**2+7200*aa*bb+17640*aa*dd+5400*bb**2+38880*bb*dd+25272*dd**2)
    assert v==closed
    assert ZERO<m[0]<F(23,13)*aa and ZERO<m[1]<F(23,18)*aa
    assert all(x>0 for x in m)
print('PASS_INDEPENDENT_FIBER_TRIANGLE_FIRST_MOMENTS (3 exact samples)')
print('PASS_GENERAL_POSITIVE_PARAMETER_COORDINATE_CENTROID_FORMULA (3 exact samples)')
print('PASS_FIXED_VOLUME_AND_FOUR_EXACT_CENTROID_COORDINATES')
print('PASS_FIXED_ATLAS_ESCAPE_EXACT_MEAN_AND_BOUNDS')
print('FIXED_VOLUME',vol)
for name,v in zip('stuv',means):print('MEAN_'+name,v)
print('MEAN_ESCAPED_MASS',escape)
print('MEAN_ESCAPED_MASS_DECIMAL',format(float(escape),'.15g'))
