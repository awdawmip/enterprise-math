"""Seven-column jet/minor certificate on the central explicit alias subarc."""
from fractions import Fraction as Q
from rational_interval import Interval as I, box
from alias_jets import J, compute, det
import json


def center(x,y):
    return x**9/((1+112*x**15)*y**12)


def signed(x,y):
    A=4*x.sqrt().sqrt()**15; D=4*(y/x).sqrt().sqrt()**9
    B=Q(7,16)*A**5; L=Q(7,16)*D**5
    return B*L*(1-A)*(1-D)/(y.sqrt().sqrt()**3*(1+B*D)*(A+B*D))


def cert():
    m0=Q(1,5)
    y0=Q('0.38767863872593544')
    u0=Q('0.5208154216661198')
    width=Q(1,5*10**12)
    # Localize the limiting implicit curve at m0.
    vals=[]
    for sign in (-1,1):
        y=y0+sign*Q(1,10**14)
        tar=center(1-m0,y)
        lo=Q('0.52080'); hi=Q('0.52083')
        assert center(lo,lo-m0)>tar>center(hi,hi-m0)
        for _ in range(90):
            mid=(lo+hi)/2
            if center(mid,mid-m0)>tar:
                lo=mid
            else:
                hi=mid
        assert u0-width/2<lo<hi<u0+width/2
        u=I(lo,hi)
        diff=signed(box(1-m0),box(y))-signed(u,u-m0)
        assert diff.lo>0 if sign==1 else diff.hi<0
        vals.append([sign,1 if diff.lo>0 else -1])
    # The implicit roots along |m-1/5| <= 1e-14 stay inside the jet box,
    # by the previously certified |y'|<1, |u'|<2.
    rad=Q(1,10**14)
    M,Y,U=compute(I(m0-rad,m0+rad),I(y0-width,y0+width),I(u0-width,u0+width))
    M=M-J([M.a[0]]);Y=Y-J([Y.a[0]]);U=U-J([U.a[0]])
    cols=[J(1), M, Y, U, M*M, M*Y, M*U]
    limits=[('-1','-.01'),('-3','-1'),('-94','-91'),('-10800','-10500'),('-1100000','-700000')]
    for n,(lo,hi) in zip(range(3,8),limits):
        v=det([[f.a[k] for f in cols[2:n]] for k in range(2,n)])
        assert v.inside(lo,hi),(n,float(v.lo),float(v.hi))
    return dict(parameter_center='1/5',parameter_radius='1/100000000000000',root_signs=vals,
                leading_normalized_wronskians={str(n):r for n,r in zip(range(3,8),limits)})

if __name__=='__main__':
    print(json.dumps(cert(),indent=2))
