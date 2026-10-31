#!/usr/bin/env python3
"""Stage321-B: exact rational exterior-cover and expanded local Pareto certificates.

Requires only Python 3 standard library. No float values enter assertions.
Uses Stage307 unique global root, Stage315 MAP reset, Stage316 convolution,
and Stage320 B-box sharpness as mathematically stated external dependencies.
"""
from fractions import Fraction as Q
from math import comb

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(hi if hi is not None else lo)
        assert self.lo<=self.hi
    @staticmethod
    def of(z): return z if isinstance(z,I) else I(z)
    def __add__(self,z):
        z=I.of(z); return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,z): return self+-I.of(z)
    def __rsub__(self,z): return I.of(z)+-self
    def __mul__(self,z):
        z=I.of(z); v=(self.lo*z.lo,self.lo*z.hi,self.hi*z.lo,self.hi*z.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=I.of(z)
        assert z.lo*z.hi>0
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,z): return I.of(z)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2:return I(self.lo**n,self.hi**n)
        return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def within(self,a,b): return self.lo>Q(a) and self.hi<Q(b)

p=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
B=lambda k,z:z**k*(1-z)**(3-k)
def r(k,x,y): return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-p[k]
def d(x,y): return sum((Q(comb(3,k),2)*abs(r(k,x,y)) for k in range(4)),Q(0))
def extrema(k,a,b):
    v=[B(k,a),B(k,b)]
    if k in (1,2) and a<=Q(k,3)<=b: v.append(B(k,Q(k,3)))
    return min(v),max(v)
def lower(rect):
    a,b,c,e=rect; ans=Q(0)
    for k in range(4):
        l1,h1=extrema(k,a,b); l2,h2=extrema(k,c,e)
        lo=Q(4,5)*l1+Q(1,5)*l2-p[k]
        hi=Q(4,5)*h1+Q(1,5)*h2-p[k]
        ans+=Q(comb(3,k),2)*max(0,lo,-hi)
    return ans
def split(rect):
    a,b,c,e=rect
    if b-a>=e-c:
        m=(a+b)/2; return (a,m,c,e),(m,b,c,e)
    m=(c+e)/2; return (a,b,c,m),(a,b,m,e)

def exterior():
    bases=((Q(0),Q(23,100),Q(0),Q(1)),
           (Q(24,100),Q(1),Q(0),Q(1)),
           (Q(23,100),Q(24,100),Q(0),Q(55,100)),
           (Q(23,100),Q(24,100),Q(56,100),Q(1)))
    witness=(Q(231083940855,10**12),Q(555508857277,10**12))
    U=d(*witness); target=Q(1,50000)
    counts=[]; mingap=None
    for rect in bases:
        todo=[rect]; nodes=leaves=0
        while todo:
            v=todo.pop();nodes+=1
            z=lower(v)-U
            if z>target:
                leaves+=1
                if mingap is None or z<mingap: mingap=z
            else:
                assert nodes<100000
                todo.extend(split(v))
        counts.append((nodes,leaves))
    assert counts==[(335,168),(55,28),(29,15),(141,71)],counts
    assert mingap>target
    # d(x*,y*)<=d(witness). b=(5/16)d
    assert Q(5,16)*target==Q(1,160000)
    print('EXTERIOR_COUNTS',counts)
    print('EXTERIOR_MIN_EXACT_GAP_NUM_DEN',mingap.numerator,mingap.denominator)
    return mingap

def gradients(x,y):
    g0=(-Q(12,5)*(1-x)**2,-Q(3,5)*(1-y)**2)
    g1=(Q(4,5)*(1-x)*(1-3*x),Q(1,5)*(1-y)*(1-3*y))
    g2=(Q(4,5)*x*(2-3*x),Q(1,5)*y*(2-3*y))
    gc=(-(1-x)*(189-183*x)/256,Q(3,64)*y*(1-y))
    return g0,g1,g2,gc

def rectangle():
    x=I(Q(23055,100000),Q(23157,100000))
    y=I(Q(555,1000),Q(556,1000))
    g0,g1,g2,gc=gradients(x,y)
    for t0,t1 in ((0,0),(0,1),(1,0),(1,1)):
        bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0])
        by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
        det=bx*gc[1]-by*gc[0]
        if (t0,t1)==(0,0): assert det.lo>0
        else: assert det.hi<0
    print('CHAMBER_DETERMINANTS_SIGNED',4)
    bounds={('r1','right'):(Q(-122,100),Q(-118,100)),
            ('r0','right'):(Q(-91,100),Q(-86,100)),
            ('r1','left'):(Q(17,10),Q(19,10)),
            ('r0','left'):(Q(29,10),Q(33,10))}
    branch_min=None
    for kind,g,other in (('r0',g0,g1),('r1',g1,g0)):
        assert g[1].hi<0
        v=-g[0]/g[1]
        assert v.within(-13,13)
        cross=other[0]+other[1]*v
        if kind=='r0':assert cross.lo>0
        else:assert cross.hi<0
        dc=gc[0]+gc[1]*v
        for side in ('right','left'):
            if kind=='r0':t0,t1=0,1 if side=='right' else 0
            else:t0,t1=(0 if side=='right' else 1),0
            bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0])
            by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
            db=bx+by*v
            if side=='right': assert db.lo>Q(18,100)
            else: assert db.hi< -Q(18,100)
            lo,hi=bounds[kind,side]
            slope=dc/db
            assert slope.within(lo,hi),(kind,side,slope.lo,slope.hi)
            m=db.lo if side=='right' else -db.hi
            branch_min=m if branch_min is None else min(branch_min,m)
            print('BRANCH',kind,side,'SLOPE_ENCLOSURE',str(slope.lo),str(slope.hi))
    v=-g1[0]/g1[1]
    ypp=-(Q(4,5)*(-4+6*x)+Q(1,5)*(-4+6*y)*v**2)/g1[1]
    bx=Q(15,16)*g2[0];by=Q(15,16)*g2[1]
    bxx=Q(15,16)*Q(4,5)*(2-6*x);byy=Q(15,16)*Q(1,5)*(2-6*y)
    cxx=(372-366*x)/256;cyy=(3-6*y)/64
    bd=bx+by*v;cd=gc[0]+gc[1]*v
    bdd=bxx+byy*v**2+by*ypp
    cdd=cxx+cyy*v**2+gc[1]*ypp
    curvature=(cdd*bd-cd*bdd)/bd**3
    assert bd.lo>0 and curvature.within(-42,-37)
    print('CURVATURE_EXACT_BOUNDS',str(curvature.lo),str(curvature.hi))
    return branch_min

def budget():
    delta=Q(31,5000000)  # 6.2e-6
    old=Q(11,10000000)
    assert delta/old==Q(62,11)
    assert delta<Q(1,160000)
    root_x_lo=Q(231083940855521,10**15)
    root_x_hi=Q(231083940855522,10**15)
    root_y_lo=Q(555508857277,10**12)
    root_y_hi=Q(555508857278,10**12)
    mu=Q(5,16)*Q(2109,50000)
    radius=delta/mu
    assert radius==Q(124,263625)
    margin=min(root_x_lo-Q(23055,100000),Q(23157,100000)-root_x_hi,
               root_y_lo-Q(555,1000),Q(556,1000)-root_y_hi)
    assert margin==Q(23157,100000)-root_x_hi
    assert radius<margin
    length=Q(1,27000)
    assert 13*length<min(root_y_lo-Q(555,1000),Q(556,1000)-root_y_hi)
    assert length<min(root_x_lo-Q(23055,100000),Q(23157,100000)-root_x_hi)
    assert Q(18,100)*length>delta
    print('DELTA',delta,'FACTOR',delta/old,'RADIUS',radius,'MARGIN',margin)
    print('KINK_REACH_LOWER',Q(18,100)*length)

if __name__=='__main__':
    exterior()
    rectangle()
    budget()
    print('STAGE321B_EXPANDED_RECTANGLE_EXTERIOR_PARETO_EXACT_PASS')
