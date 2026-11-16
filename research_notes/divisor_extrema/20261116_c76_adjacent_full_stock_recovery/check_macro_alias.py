"""Certify a nontrivial arc of real three-observable aliases by interval signs."""
from fractions import Fraction as F
import json
from check_macro_point import box, Interval, J, real


def signed_derivative(x,y,p,q):
    # p=d(log x)/dy_target, q=d(log y)/dy_target.
    a=4*x.sqrt().sqrt()**15
    d=4*(y/x).sqrt().sqrt()**9
    b=F(7,16)*a**5
    da=F(15,4)*p
    dd=F(9,4)*(q-p)
    return real(x,y)*(-F(3,4)*q+5*da+5*dd-a*da/(1-a)-d*dd/(1-d)
                      -(5*da+dd)*b*d/(1+b*d)-(a*da+b*d*(5*da+dd))/(a+b*d))


def main():
    # Parameterizing the competing branch by its first landing u automates
    # the J match. We instead bracket u for each fixed y at the two ends.
    m = Interval('0.199999999','0.200000001')
    x = 1-m
    bounds = [('0.38767','0.52080224','0.52080227','-0.000005','-0.000003'),
              ('0.38769','0.52083273','0.52083276','0.000004','0.000006')]
    for y,lo,hi,dlo,dhi in bounds:
        y=box(F(y))
        j=J(x,y)
        assert J(box(F(lo)),box(F(lo))-m).lo > j.hi
        assert J(box(F(hi)),box(F(hi))-m).hi < j.lo
        u=Interval(lo,hi)
        diff=real(x,y)-real(u,u-m)
        assert diff.inside(dlo,dhi)
    # The inverse middle-branch root grows with y for each fixed m.
    whole_u=Interval(bounds[0][1],bounds[1][2])
    whole_y=Interval(bounds[0][0],bounds[1][0])
    assert x.lo-whole_y.hi>m.hi and whole_y.lo>m.hi
    assert 1-whole_u.hi>m.hi and whole_u.lo-m.hi>m.hi
    assert real(x,whole_y).hi<0
    # Transversality across the entire certified joint box.
    v=whole_u-m
    slope=9/whole_u-1680*whole_u**14/(1+112*whole_u**15)-12/v
    du=-12/(whole_y*slope)
    derivative=(signed_derivative(x,whole_y,box(0),1/whole_y)
                -signed_derivative(whole_u,v,du/whole_u,du/v))
    assert derivative.inside('0.42','0.52')
    return dict(derivative_interval=['0.42','0.52'],m_interval=['0.199999999','0.200000001'],
                target_second=['0.38767','0.38769'],
                competitor_first=[bounds[0][1],bounds[1][2]],
                signed_real_difference_at_y_lo=bounds[0][-2:],
                signed_real_difference_at_y_hi=bounds[1][-2:],
                shared_shortest_types=['first','middle'])
if __name__=='__main__':
    print(json.dumps(main(),indent=2))
