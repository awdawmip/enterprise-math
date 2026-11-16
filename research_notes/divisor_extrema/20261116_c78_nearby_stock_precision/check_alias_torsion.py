"""Implicit curvature certificate via analytic directional log derivatives."""
from fractions import Fraction as Q
from rational_interval import Interval, box
import json


def jets(x,y,X,Y,XX=None,YY=None):
    """Directional derivatives along the line (x+tX,y+tY), through order two."""
    ux, uy=X/x,Y/y
    angle=112*x**15
    e=angle/(1+angle)
    j1=(9-15*e)*ux-12*uy
    j2=-(9-15*e)*ux**2-225*e*(1-e)*ux**2+12*uy**2
    # Exact local log derivatives of A,D,B=bA^5,L=bD^5,Z=BD.
    A=4*x.sqrt().sqrt()**15
    D=4*(y/x).sqrt().sqrt()**9
    B=Q(7,16)*A**5; Z=B*D
    aa,dd=Q(15,4)*ux,Q(9,4)*(uy-ux)
    aaa,ddd=-Q(15,4)*ux**2,Q(9,4)*(ux**2-uy**2)
    zz,zzz=5*aa+dd,5*aaa+ddd
    # S'/S for nonzero S. f'' of log(1-A) etc handled by Bernoulli weight.
    n1,n2=A/(A-1),D/(D-1)
    e1,e2=Z/(1+Z),Z/(A+Z)
    f1=-Q(3,4)*uy+5*aa+5*dd+n1*aa+n2*dd-e1*zz-aa-e2*(zz-aa)
    f2=(Q(3,4)*uy**2+5*aaa+5*ddd+n1*aaa+n2*ddd+n1*(1-n1)*aa**2+n2*(1-n2)*dd**2
        -e1*zzz-e1*(1-e1)*zz**2-aaa-e2*(zzz-aaa)-e2*(1-e2)*(zz-aa)**2)
    if XX is None:
        return (j1,f1),(j2,f2)
    def logs(v, first, second):
        a,b=first/v,second/v
        return a,b-a*a,2*a*a*a-3*a*b
    xlog=logs(x,X,XX); ylog=logs(y,Y,YY)
    def scale(w,k):
        return tuple(k*a for a in w)
    def plus(*terms):
        return tuple(sum(ws,box(0)) for ws in zip(*terms))
    def minus(w,t):
        return plus(w,scale(t,-1))
    def combine(w,t,fraction):
        p,pp,ppp=minus(w,t)
        h=fraction*(1-fraction)
        return (t[0]+fraction*p,t[1]+fraction*pp+h*p*p,
                t[2]+fraction*ppp+3*h*p*pp+h*(1-2*fraction)*p*p*p)
    zero=scale(xlog,0)
    jlog=plus(scale(xlog,9),scale(ylog,-12),scale(combine(scale(xlog,15),zero,e),-1))
    alog=scale(xlog,Q(15,4))
    dlog=scale(minus(ylog,xlog),Q(9,4))
    blog=scale(alog,5)
    zlog=plus(blog,dlog)
    flog=plus(scale(ylog,-Q(3,4)),blog,scale(dlog,5),combine(alog,zero,n1),
              combine(dlog,zero,n2),scale(combine(zlog,zero,e1),-1),scale(combine(zlog,alog,e2),-1))
    return jlog[2],flog[2]



def solve(Y,U,R):
    det=Y[0]*U[1]-Y[1]*U[0]
    return ((R[0]*U[1]-R[1]*U[0])/det,
            (Y[0]*R[1]-Y[1]*R[0])/det)


def bound(m,y,u):
    x=1-m; v=u-m
    def slopes(dx,dy,du,dm,order=0):
        left=jets(x,y,box(dx),box(dy))[order]
        right=jets(u,v,box(du),box(du)-dm)[order]
        return [left[i]-right[i] for i in (0,1)]
    jy=slopes(0,1,0,0)
    ju=slopes(0,0,1,0)
    source=slopes(-1,0,0,1)
    Y,U=solve(jy,ju,[-s for s in source])
    second=slopes(-1,Y,U,1,1)
    YY,UU=solve(jy,ju,[-s for s in second])
    lhs=jets(x,y,box(-1),Y,box(0),YY)
    rhs=jets(u,v,U,U-1,UU,UU)
    YYY,UUU=solve(jy,ju,[rhs[i]-lhs[i] for i in (0,1)])
    return YY,UU,YYY,UUU,YY*UUU-UU*YYY


def main():
    m=Interval('0.199999999','0.200000001')
    y=Interval('0.38767','0.38769')
    u=Interval('0.52080224','0.52083276')
    bounds = [('-0.373','-0.258'),('-0.852','-0.707'),('-46','-35'),('-29','-15'),('-36','-14')]
    for t,(lo,hi) in zip(bound(m,y,u),bounds):
        assert t.inside(lo,hi)
    return dict(ranges=dict(zip(('y2','u2','y3','u3','y2u3_minus_u2y3'),bounds)))
if __name__=='__main__':
    print(json.dumps(main(),indent=2))
