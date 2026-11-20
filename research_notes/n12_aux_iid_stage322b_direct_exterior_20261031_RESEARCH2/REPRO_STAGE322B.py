#!/usr/bin/env python3
"""Stage322-B experimental exact rational certificate of expanded Pareto germ.

Only stdlib Fraction arithmetic; all conclusions on real rectangles use rational interval
arithmetic, not floating point sampling. Depends on cited Stage307/315/316 theory.
"""
from fractions import Fraction as Q
from math import comb

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def of(z):return z if isinstance(z,I) else I(z)
    def __add__(self,z):
        z=I.of(z);return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,z):return self+-I.of(z)
    def __rsub__(self,z):return I.of(z)+-self
    def __mul__(self,z):
        z=I.of(z); v=[a*b for a in (self.lo,self.hi) for b in (z.lo,z.hi)];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=I.of(z); assert z.lo*z.hi>0
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,z):return I.of(z)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2:return I(self.lo**n,self.hi**n)
        return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def within(self,a,b):return self.lo>Q(a) and self.hi<Q(b)
    def __repr__(self):return f'I({self.lo},{self.hi})'

p=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
B=lambda k,z:z**k*(1-z)**(3-k)
def r(k,x,y):return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-p[k]
def d(x,y):return sum((Q(comb(3,k),2)*abs(r(k,x,y)) for k in range(4)),Q(0))
def extrema(k,a,b):
    v=[B(k,a),B(k,b)]
    if k in (1,2) and a<=Q(k,3)<=b:v.append(B(k,Q(k,3)))
    return min(v),max(v)
def lower(rect):
    a,b,c,e=rect;ans=Q(0)
    for k in range(4):
        l1,h1=extrema(k,a,b); l2,h2=extrema(k,c,e)
        lo=Q(4,5)*l1+Q(1,5)*l2-p[k]
        hi=Q(4,5)*h1+Q(1,5)*h2-p[k]
        ans+=Q(comb(3,k),2)*max(0,lo,-hi)
    return ans
def split(rect):
    a,b,c,e=rect
    if b-a>=e-c:
        m=(a+b)/2;return (a,m,c,e),(m,b,c,e)
    m=(c+e)/2;return (a,b,c,m),(a,b,m,e)

ROOT_X_LO=Q(231083940855521,10**15)
ROOT_X_HI=Q(231083940855522,10**15)
ROOT_Y_LO=Q(555508857277,10**12)
ROOT_Y_HI=Q(555508857278,10**12)
W=(Q(231083940855,10**12),Q(555508857277,10**12))
RX=(Q(229,1000),Q(2335,10000))
RY=(Q(550,1000),Q(562,1000))
DELTA=Q(1,20000)


def exterior():
    x0,x1=RX;y0,y1=RY
    bases=((Q(0),x0,Q(0),Q(1)),(x1,Q(1),Q(0),Q(1)),
           (x0,x1,Q(0),y0),(x0,x1,y1,Q(1)))
    U=d(*W); target=Q(16,5)*DELTA
    counts=[];mingap=None
    for rect in bases:
        todo=[rect]; nodes=leaves=0
        while todo:
            v=todo.pop();nodes+=1
            z=lower(v)-U
            if z>target:
                leaves+=1; mingap=z if mingap is None or z<mingap else mingap
            else:
                assert nodes<200000, (rect,nodes)
                todo.extend(split(v))
        counts.append((nodes,leaves))
    assert mingap is not None and mingap>target
    print('EXTERIOR_COUNTS',counts)
    print('EXTERIOR_MIN_GAP',mingap)
    print('TARGET',target, 'DIFFERENCE_POSITIVE',mingap-target)
    return counts,mingap

def gradients(x,y):
    g0=(-Q(12,5)*(1-x)**2,-Q(3,5)*(1-y)**2)
    g1=(Q(4,5)*(1-x)*(1-3*x),Q(1,5)*(1-y)*(1-3*y))
    g2=(Q(4,5)*x*(2-3*x),Q(1,5)*y*(2-3*y))
    gc=(-(1-x)*(189-183*x)/256,Q(3,64)*y*(1-y))
    return g0,g1,g2,gc

def certify_tv_chambers():
    # Each sign is sign[B_k(p)-B_k(t)], for 0<=k<=3.
    cases=(
        ('quarter-x',Q(1,4),RX,(-1,+1,+1,+1)),
        ('threequarter-x',Q(3,4),RX,(-1,-1,+1,+1)),
        ('quarter-y',Q(1,4),RY,(+1,+1,-1,-1)),
        ('threequarter-y',Q(3,4),RY,(-1,-1,+1,+1)),
    )
    for name,center,(low,high),signs in cases:
        for k,s in enumerate(signs):
            low_val,high_val=extrema(k,low,high)
            z=B(k,center)
            if s==1:assert z>high_val,(name,k,'positive')
            else:assert z<low_val,(name,k,'negative')
    # Differentiating D3 in this sign chamber yields exactly the gc
    # formulas in gradients, rather than merely a numerical approximation.
    print('D3_CHAMBERS_CERTIFIED',len(cases)*4)

def rectangle():
    # Split the enlarged R into 4x4 rational rectangles to avoid
    # false dependence blowup from naive whole-box interval arithmetic.
    x0,x1=RX; y0,y1=RY
    count=0
    slopes={('r0','right'):(Q(-1),Q(-4,5)),
            ('r1','right'):(Q(-5,4),Q(-11,10)),
            ('r1','left'):(Q(17,10),Q(19,10)),
            ('r0','left'):(Q(27,10),Q(7,2))}
    for i in range(4):
      for j in range(4):
        x=I(x0+(x1-x0)*i/4,x0+(x1-x0)*(i+1)/4)
        y=I(y0+(y1-y0)*j/4,y0+(y1-y0)*(j+1)/4)
        assert r(2,x,y).lo>0 and r(3,x,y).hi<0,(i,j,'residual signs')
        g0,g1,g2,gc=gradients(x,y)
        assert gc[0].hi<0 and gc[1].lo>0
        for t0,t1 in ((0,0),(0,1),(1,0),(1,1)):
            bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0])
            by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
            det=bx*gc[1]-by*gc[0]
            if (t0,t1)==(0,0):assert det.lo>0,(i,j,'positive det')
            else:assert det.hi<0,(i,j,'negative det',t0,t1)
        for kind,g,other in (('r0',g0,g1),('r1',g1,g0)):
            assert g[1].hi<0,(i,j,kind,'gy')
            v=-g[0]/g[1]
            assert v.within(-Q(25,2),Q(25,2)),(i,j,kind,'slope bound')
            cross=other[0]+other[1]*v
            if kind=='r0':assert cross.lo>0,(i,j,kind,'cross')
            else:assert cross.hi<0,(i,j,kind,'cross')
            dc=gc[0]+gc[1]*v
            for side in ('right','left'):
                if kind=='r0':t0,t1=0,1 if side=='right' else 0
                else:t0,t1=(0 if side=='right' else 1),0
                bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0])
                by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
                db=bx+by*v
                if side=='right':assert db.lo>Q(4,25),(i,j,kind,side,'budget derivative')
                else:assert db.hi<-Q(4,25),(i,j,kind,side,'budget derivative')
                lo,hi=slopes[kind,side]
                assert (dc/db).within(lo,hi),(i,j,kind,side,'tagged-cost slope')
        # Strict negative curvature of c as a function of b on r1=0/right.
        v=-g1[0]/g1[1]
        ypp=-(Q(4,5)*(-4+6*x)+Q(1,5)*(-4+6*y)*v**2)/g1[1]
        bx=Q(15,16)*g2[0]; by=Q(15,16)*g2[1]
        bxx=Q(15,16)*Q(4,5)*(2-6*x); byy=Q(15,16)*Q(1,5)*(2-6*y)
        cxx=(372-366*x)/256; cyy=(3-6*y)/64
        bd=bx+by*v;cd=gc[0]+gc[1]*v
        bdd=bxx+byy*v**2+by*ypp
        cdd=cxx+cyy*v**2+gc[1]*ypp
        curvature=(cdd*bd-cd*bdd)/bd**3
        assert bd.lo>0 and curvature.within(-46,-34),(i,j,'curvature',curvature)
        count+=1
    assert count==16
    print('LOCAL_TILE_COUNT',count)
    print('ALL_CHAMBER_DETERMINANTS_AND_BRANCH_SLOPES_CERTIFIED')
    print('R1_RIGHT_CURVATURE_STRICT', '-46 < C3_second_derivative < -34')
    return slopes

def budget():
    L=Q(1,2500) # x extension gives 0.16*L > delta
    assert Q(4,25)*L>DELTA
    assert L<min(ROOT_X_LO-RX[0],RX[1]-ROOT_X_HI)
    assert 13*L<min(ROOT_Y_LO-RY[0],RY[1]-ROOT_Y_HI)
    print('KINK_REACH_LOWER',Q(4,25)*L)

if __name__=='__main__':
    certify_tv_chambers()
    exterior()
    rectangle()
    budget()
    print('STAGE322B_50_MICRO_GLOBAL_GERM_EXACT_PASS')
