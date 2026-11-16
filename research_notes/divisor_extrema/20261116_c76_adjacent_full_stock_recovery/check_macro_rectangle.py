"""Uniform rational interval certificate for an explicit closed macro rectangle."""
from fractions import Fraction as F
import json
from check_macro_point import box, Interval, J, h, real


def narrow_inverse(fun, target, lo, hi, decreasing=True, steps=23):
    lo,hi=F(lo),F(hi)
    assert lo<hi
    if decreasing:
        assert fun(lo)>target>fun(hi)
    else:
        assert fun(lo)<target<fun(hi)
    for _ in range(steps):
        mid=(lo+hi)/2
        if (fun(mid)>target)==decreasing:
            lo=mid
        else:
            hi=mid
    return lo,hi


def check(x,y):
    m=1-x
    j=J(x,y)
    s=real(x,y)
    assert x.lo-y.hi>m.hi and y.lo>m.hi
    assert s.hi<0
    jac=real(x,y,True)
    assert jac.hi<0 or jac.lo>0
    assert j.hi<J(F(2,3),F(1,3))
    ab=lambda t:J(t,2*t-1)
    ablo=narrow_inverse(ab,j.hi,F(2,3),F(4,5))[0]
    abhi=narrow_inverse(ab,j.lo,F(2,3),F(4,5))[1]
    uab=Interval(ablo,abhi)
    sab=real(uab,2*uab-1)
    assert s.hi<min(sab.lo,-sab.hi)
    # All possible middle-gap roots, using monotonicity in m and J.
    u0=narrow_inverse(lambda t:J(t,t-m.lo),j.hi,m.lo+F(1,1000),1)[0]
    u1=narrow_inverse(lambda t:J(t,t-m.hi),j.lo,m.hi+F(1,1000),1)[1]
    u=Interval(u0,u1)
    sb=real(u,u-m)
    assert s.hi < min(sb.lo,-sb.hi), (float(s.hi),float(sb.lo),float(sb.hi))
    # Any terminal-shortest root must have x' >= 2m and x' <= 1.
    # h has only an interior maximum, so test its minimum on this interval.
    left=2*m.lo
    assert j.hi*m.hi**12<min(h(left),h(F(1)))
    cc=F(3,4)/(1+F(1,448))*h(F(1))
    yl=narrow_inverse(lambda t:cc/t**12,j.hi,'0.1','0.6')[0]
    yr=narrow_inverse(lambda t:cc/t**12,j.lo,'0.1','0.6')[1]
    sf=real(box(1),Interval(yl,yr))
    assert s.hi<min(sf.lo,-sf.hi)
    ff=lambda t:F(3,4)*J(t,t)
    xl=narrow_inverse(ff,j.hi,'0.01','0.15')[0]
    xr=narrow_inverse(ff,j.lo,'0.01','0.15')[1]
    same=Interval(xl,xr)
    sd=real(same,same)
    assert s.hi<min(sd.lo,-sd.hi)
    assert j.lo>J(F(1),F(1))
    return j,s,jac,sb


def main():
    # 1/500 by 1/500 cells. The endpoints shared by neighboring cells are included.
    lower=[F('0.79'),F('0.35')]
    side=F('0.02')
    count=10
    extrema=[[None,None] for _ in range(4)]
    for i in range(count):
        for k in range(count):
            cell=[Interval(a+side*t/count,a+side*(t+1)/count) for a,t in zip(lower,[i,k])]
            vals=check(*cell)
            for bounds,v in zip(extrema,vals):
                bounds[0]=v.lo if bounds[0] is None else min(v.lo,bounds[0])
                bounds[1]=v.hi if bounds[1] is None else max(v.hi,bounds[1])
    scales=10**6
    def floor_scaled(v):return (v.numerator*scales)//v.denominator
    return dict(x=['0.79','0.81'],y=['0.35','0.37'],cells=count*count,
                six_decimal_outward_bounds={key:[floor_scaled(p),-floor_scaled(-q)]
                for key,(p,q) in zip(['J','signed_real','log_slope','middle_real'],extrema)})
if __name__=='__main__':
    print(json.dumps(main(),indent=2))
