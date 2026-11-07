#!/usr/bin/env python3
"""Stage329-B: exact rational Bernstein proof of restricted-cusp allocation switch.

Auxiliary two-source, three-visit Bernoulli BRC model only. Standard-library
Fraction arithmetic throughout; every global rectangle bound is certified by
49 exact tensor-product Bernstein coefficients, not floating sampling.
"""
from fractions import Fraction as Q
from math import comb, isqrt

Z = Q(0)
ONE = Q(1)

def const(c): return {(0, 0): Q(c)} if c else {}
def var(i): return {(1, 0): ONE} if i == 0 else {(0, 1): ONE}
def add(a, b):
    d = dict(a)
    for ij, v in b.items():
        d[ij] = d.get(ij, Z) + v
        if not d[ij]: del d[ij]
    return d

def neg(p): return {ij: -v for ij, v in p.items()}
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    d = {}
    for (i, j), z in a.items():
        for (k, l), w in b.items():
            ix = (i+k, j+l)
            d[ix] = d.get(ix, Z) + z*w
    return {ij: v for ij, v in d.items() if v}
def sc(p, v): return {ij: z*Q(v) for ij, z in p.items() if z*Q(v)}
def pw(p, n):
    r=const(1)
    for _ in range(n): r=mul(r,p)
    return r

def df(p, axis):
    r={}
    for (i,j),v in p.items():
        d=(i,j)[axis]
        if d:
            ix=(i-1,j) if axis==0 else (i,j-1)
            r[ix]=r.get(ix,Z)+d*v
    return r

def b2bern_bounds(p,x0,x1,y0,y1):
    """Exact continuous range enclosure on a rectangle via tensor Bernstein."""
    n=max((ij[0] for ij in p), default=0)
    m=max((ij[1] for ij in p), default=0)
    coeff={}
    for (i,j),v in p.items():
        for a in range(i+1):
            for b in range(j+1):
                w=v*comb(i,a)*Q(x0)**(i-a)*(Q(x1)-Q(x0))**a
                w*=comb(j,b)*Q(y0)**(j-b)*(Q(y1)-Q(y0))**b
                coeff[(a,b)]=coeff.get((a,b),Z)+w
    ber=[]
    for k in range(n+1):
        for l in range(m+1):
            ber.append(sum((v*Q(comb(k,i),comb(n,i))*Q(comb(l,j),comb(m,j))
                for (i,j),v in coeff.items() if i<=k and j<=l),Z))
    assert len(ber)==(n+1)*(m+1)
    return min(ber),max(ber),n,m,len(ber)

X,Y=var(0),var(1)
U=const(1)
GX=lambda z: mul(z,sub(const(2),sc(z,3)))
HX=lambda z: mul(sub(U,z),sub(U,sc(z,3)))
B=lambda k,z: mul(pw(z,k),pw(sub(U,z),3-k))
CX=sc(mul(sub(U,X),sub(const(189),sc(X,183))),Q(-1,256))
CY_L=sc(mul(Y,sub(U,Y)),Q(3,64))
CY_R=add(CY_L,sc(GX(Y),Q(21,256)))
D=sub(mul(GX(X),HX(Y)),mul(GX(Y),HX(X)))
assert D==mul(sub(X,Y),add(sub(sc(mul(X,Y),6),sc(X,3)),sub(const(2),sc(Y,3))))

def cusp_curvature_numerator(cy):
    n=sub(mul(CX,HX(Y)),sc(mul(cy,HX(X)),4))
    n_dot=sub(mul(df(n,0),HX(Y)),sc(mul(df(n,1),HX(X)),4))
    d_dot=sub(mul(df(D,0),HX(Y)),sc(mul(df(D,1),HX(X)),4))
    return sub(mul(n_dot,D),mul(n,d_dot))

# Broad rectangle includes the entire original-right r1=0 arc, both sides
# of the single source-tagged cusp, through y=577/1000.
x0,x1=Q(231,1000),Q(239,1000)
y0,y1=Q(555,1000),Q(577,1000)
Kleft=cusp_curvature_numerator(CY_L)
Kright=cusp_curvature_numerator(CY_R)
for name,K in (("left",Kleft),("right",Kright)):
    lo,hi,n,m,count=b2bern_bounds(K,x0,x1,y0,y1)
    assert (n,m,count)==(6,6,49)
    assert Q(1,25)<lo<=hi<Q(7,100), (name,lo,hi)
    print(name,"K_BERNSTEIN_MIN_MAX",lo,hi,"COUNT",count)
# D=(x-y)F, F=6xy-3x-3y+2 increasing in x and decreasing in y.
Fmin=6*x0*y1-3*x0-3*y1+2
assert Fmin==Q(187861,500000)
assert (y0-x1)*Fmin>Q(1,9)
assert Q(16,9)*Q(7,100)*9**3<Q(100)
print("CERTIFIED_CURVATURE: -100 < phi'' < 0 ON BOTH SMOOTH BRANCH CHAMBERS")

# Every one of the 16 source-tagged polynomial differences has a constant
# strict sign throughout this box except (a=3/4,z=y,k=2).
for label,a,variable,vl,vr in (
    ("x_1/4",Q(1,4),X,x0,x1), ("x_3/4",Q(3,4),X,x0,x1),
    ("y_1/4",Q(1,4),Y,y0,y1), ("y_3/4",Q(3,4),Y,y0,y1)):
    for k in range(4):
        if label=="y_3/4" and k==2:
            # B_2(3/4)-B_2(y)=(4y-3)(16y^2-4y-3)/64.
            special=sc(mul(sub(sc(Y,4),const(3)),
                               sub(sub(sc(pw(Y,2),16),sc(Y,4)),const(3))),Q(1,64))
            assert sub(B(k,const(a)),B(k,variable))==special
            continue
        P=sub(B(k,const(a)),B(k,variable))
        box=(vl,vr,y0,y1) if variable is X else (x0,x1,vl,vr)
        lo,hi,_,_,_=b2bern_bounds(P,*box)
        assert lo>0 or hi<0, (label,k,lo,hi)
# Confirm that those sign chambers imply the closed-form c_x and c_y
# derivatives independently of the source author's simplified formulas.
def peval(p,xa,ya):
    return sum((v*xa**i*ya**j for (i,j),v in p.items()),Z)

def tag_cost_polynomial(y_post):
    acc={}
    comps=((Q(1,4),X,63),(Q(3,4),X,1),
           (Q(1,4),Y,9),(Q(3,4),Y,7))
    for a,z,weight in comps:
        subcost={}
        for k,w in enumerate((1,3,3,1)):
            p=sub(B(k,const(a)),B(k,z))
            sample=peval(p,Q(235,1000),Q(576 if y_post else 565,1000))
            assert sample != 0
            subcost=add(subcost,sc(p,Q(w,2)*(1 if sample>0 else -1)))
        acc=add(acc,sc(subcost,Q(weight,256)))
    return acc
Cleft=tag_cost_polynomial(False)
Cright=tag_cost_polynomial(True)
assert df(Cleft,0)==CX and df(Cleft,1)==CY_L
assert df(Cright,0)==CX and df(Cright,1)==CY_R
print("EXACT_16_TAGGED_DIFFERENCE_CHAMBERS_PASS (15 strict; 1 algebraic cusp)")
print("TAGGED_COST_GRADIENT_POLYNOMIAL_IDENTITIES_PASS")

# The curve r_1(x,y)=0 is strictly increasing y(x) inside the rectangle:
# dr_1/dx=4h(x)/5>0, dr_1/dy=h(y)/5<0. Along it b=15r_2/16
# and b'>0, hence s=b-beta_* is a legitimate strictly increasing coordinate.
# Right initial point brackets are inherited as stated in Stage328.
xstar_l,xstar_h=Q(231083940855521,10**15),Q(231083940855522,10**15)
ystar_l,ystar_h=Q(555508857277,10**12),Q(555508857278,10**12)
assert x0<xstar_l<xstar_h<x1 and y0<ystar_l<ystar_h<y1

Bq=lambda k,z:z**k*(1-z)**(3-k)
r1=lambda xx,yy: Q(4,5)*Bq(1,xx)+Q(1,5)*Bq(1,yy)-Q(21,160)
r2=lambda xx,yy: Q(4,5)*Bq(2,xx)+Q(1,5)*Bq(2,yy)-Q(9,160)
r3=lambda xx,yy: Q(4,5)*Bq(3,xx)+Q(1,5)*Bq(3,yy)-Q(9,160)

def root_x(ylo,yhi,lo,hi,steps=85):
    assert r1(lo,ylo)<0 and r1(hi,yhi)>0
    for _ in range(steps):
        mid=(lo+hi)/2
        if r1(mid,ylo)<0: lo=mid
        elif r1(mid,yhi)>0: hi=mid
        else: break
    assert r1(lo,ylo)<0 and r1(hi,yhi)>0
    return lo,hi

# ydag=(1+sqrt(13))/8 rational square-root isolation.
scale=10**35
q=isqrt(13*scale*scale)
rootlo=(Q(scale)+q)/(8*scale)
roothi=(Q(scale)+q+1)/(8*scale)
assert (8*rootlo-1)**2<13 and (8*roothi-1)**2>13
assert ystar_h<rootlo<roothi<y1
xdag_l,xdag_h=root_x(rootlo,roothi,Q(237,1000),Q(238,1000))
assert xstar_h<xdag_l<xdag_h<x1

# End of the small post-cusp branch is y=577/1000, with x uniquely solving r1=0.
xend_l,xend_h=root_x(y1,y1,Q(238,1000),Q(239,1000))
assert xdag_h<xend_l<xend_h<x1
# On the whole arc, r2 increases from a strictly positive value and r3
# increases to a strictly negative value; r0 decreases from its zero at star.
assert r2(xstar_l,ystar_l)>0 and r3(xend_h,y1)<0
Bstar_l=Q(15,16)*r2(xstar_l,ystar_l)
Bstar_h=Q(15,16)*r2(xstar_h,ystar_h)
Bdag_l=Q(15,16)*r2(xdag_l,rootlo)
Bdag_h=Q(15,16)*r2(xdag_h,roothi)
Bend_l=Q(15,16)*r2(xend_l,y1)
Bend_h=Q(15,16)*r2(xend_h,y1)
assert Q(0)<Bdag_l-Bstar_h
assert Bdag_h-Bstar_l < Bend_l-Bstar_h
assert Q(0)< Bend_l-Bdag_h < Bend_h-Bdag_l < Q(3,20000)
assert Bend_h-Bstar_l < 2*(Bdag_l-Bstar_h)
def compact_interval(lo,hi,scale=10**12):
    return f"({lo*scale//1}/{scale}, {-((-hi*scale)//1)}/{scale})"
print("S_RANGE eps_cusp",compact_interval(Bdag_l-Bstar_h,Bdag_h-Bstar_l))
print("S_RANGE eps_end",compact_interval(Bend_l-Bstar_h,Bend_h-Bstar_l))
print("POST_CUSP_SPAN_LT_3_OVER_20000_PASS")

# Exact interval arithmetic for one-sided marginal slope gap.
class I:
    def __init__(self,lo,hi=None):
        self.lo=Q(lo);self.hi=Q(hi if hi is not None else lo)
        assert self.lo<=self.hi
    def __add__(self,b):
        b=IV(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-IV(b)
    def __rsub__(self,b):return IV(b)+-self
    def __mul__(self,b):
        b=IV(b);q=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I(min(q),max(q))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=IV(b);assert b.lo>0 or b.hi<0
        return self*I(1/b.hi,1/b.lo)
    def __pow__(self,n):
        assert n>=0
        if n==0:return I(1)
        if n%2:return self*(self**(n-1))
        a=self**(n//2);return a*a

def IV(z):return z if isinstance(z,I) else I(z)
def hI(z):return (1-z)*(1-3*z)
def gI(z):return z*(2-3*z)
def slope(xx,yy,right):
    yp=-4*hI(xx)/hI(yy)
    bp=Q(15,16)*(Q(4,5)*gI(xx)+Q(1,5)*gI(yy)*yp)
    cx=-(1-xx)*(189-183*xx)/256
    cy=3*yy*(1-yy)/64
    if right:cy=cy+Q(21,256)*gI(yy)
    assert bp.lo>0
    return (cx+cy*yp)/bp

s0=slope(I(xstar_l,xstar_h),I(ystar_l,ystar_h),False)
spost=slope(I(xdag_l,xdag_h),I(rootlo,roothi),True)
assert spost.lo-s0.hi>Q(1,30)
print("SLOPE_INITIAL",compact_interval(s0.lo,s0.hi,10**6))
print("SLOPE_CUSP_RIGHT",compact_interval(spost.lo,spost.hi,10**6))
print("CERTIFIED_SLOPE_JUMP_GT_1_OVER_30")
# For any 0<u<=eps_end-eps_cusp<3/20000, right slope is
# >= right_cusp_slope -100*u > initial_slope, whereas the left
# slope at u is <= initial_slope. Thus cusp-pinned split beats endpoint.
assert Q(1,30)-100*Q(3,20000)>0
print("STAGE329B_BERNSTEIN_TWO_CHAMBER_CUSP_PIN_RESTRICTED_SWITCH_EXACT_PASS")
