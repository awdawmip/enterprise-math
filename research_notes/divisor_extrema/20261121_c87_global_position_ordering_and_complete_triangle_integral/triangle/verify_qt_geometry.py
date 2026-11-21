"""Independent exact rational source-volume checks for C87 QT.

One route integrates the original source level s by alternating truncated
squares. The other integrates the new nonnegative broken line in h. They
share only the elementary exact integral of a linear positive part squared.
Finite tests support, but do not replace, QT_POSITIVE_INTEGRAL.md.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json
import c84_interval_kernel as k
from qt_positive_integral import source_volume_cell

def phi(a,b):
    if a<=0 and b<=0:return F(0)
    if a>=0 and b>=0:return(a*a+a*b+b*b)/3
    return max(a,b)**3/(3*abs(a-b))

def source_s(r,u,t):
    d=1/u
    lo=max(2*u*t,d);hi=min(r-2*u*(1-t),r-d)
    if lo>=hi:return F(0)
    cuts=[lo]+([r*t]if lo<r*t<hi else[])+[hi]
    def lengths(s):return(min(s/t,(r-s)/(1-t)),(r-s-d)/(1-t),(s-d)/t)
    total=F(0)
    for l,h in zip(cuts,cuts[1:]):
        L0,Lp,Lm=lengths(l);H0,Hp,Hm=lengths(h)
        for a,b in product((0,1),repeat=2):
            top=phi(2*L0-3*u-a*Lp-b*Lm,2*H0-3*u-a*Hp-b*Hm)
            bottom=phi(u-a*Lp-b*Lm,u-a*Hp-b*Hm)
            total+=(-1)**(a+b)*(h-l)*(top-bottom)
    return total/4

def source_h(r,u,t):
    d=1/u
    raw=[-u,u,3*u-2*d/(1-t),2*d/t-3*u]
    order=tuple(sorted(range(4),key=lambda i:raw[i]))
    points=[raw[i]for i in order]
    def value(h):return(r-F(3,2)*u-max(0,d+(1-t)*(h-3*u)/2)
                       -max(0,d-t*(h+3*u)/2)-max(u,abs(h))/2)
    values=[value(h)for h in points]
    total=max(0,values[0])**3/(3*(1+t)/2)
    total+=max(0,values[-1])**3/(3*(2-t)/2)
    total+=sum((b-a)*phi(x,y)for a,b,x,y
               in zip(points,points[1:],values,values[1:]))
    return total/4,order

def run():
    cases=positive=0;orders=set()
    for r in map(F,('7/3','5/2','8/3','14/5')):
        for i in range(1,40):
            u=F(i,24)
            if not 2/r<=u<=r/2:continue
            for j in range(1,24):
                t=F(j,24)
                a,order=source_h(r,u,t);b=source_s(r,u,t)
                assert a==b,(r,u,t,a,b)
                assert a>=0
                assert a==source_h(r,u,1-t)[0]
                enclosure=source_volume_cell(k.I.cv(u),k.I.cv(t),k.I.cv(r))
                assert F(enclosure.lo,k.Q)<=a<=F(enclosure.hi,k.Q)
                cases+=1;positive+=a>0;orders.add(order)
    # Whole cells straddling representative ordering and positivity boundaries.
    boxes=[
        (F(11,4),F(1),F(1,2),F(1,100)),
        (F(11,4),F(4,3),F(1,4),F(1,200)),
        (F(5,2),F(1),F(1,2),F(1,100)),
        (F(14,5),F(5,4),F(2,5),F(1,50))]
    checked_points=0
    for r,u,t,e in boxes:
        ui=k.I(k.I.cv(u-e).lo,k.I.cv(u+e).hi)
        ti=k.I(k.I.cv(t-e).lo,k.I.cv(t+e).hi)
        enclosure=source_volume_cell(ui,ti,k.I.cv(r))
        for i,j in product((-1,0,1),repeat=2):
            actual=source_h(r,u+i*e,t+j*e)[0]
            assert F(enclosure.lo,k.Q)<=actual<=F(enclosure.hi,k.Q)
            checked_points+=1
    result={
        'status':'PASS','exact_rational_source_cases':cases,
        'positive_source_cases':positive,
        'realized_knot_orders':len(orders),
        'reflection_identity_checks':cases,
        'directed_point_enclosure_checks':cases,
        'whole_cell_boundary_boxes':len(boxes),
        'exact_test_points_in_boundary_boxes':checked_points,
        'independent_eliminations':['source_level_s','endpoint_difference_h'],
        'finite_checks_are_universal_proof':False,
        'complete_QT_integral_recomputed_here':False}
    Path(__file__).with_name('qt_geometry_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
