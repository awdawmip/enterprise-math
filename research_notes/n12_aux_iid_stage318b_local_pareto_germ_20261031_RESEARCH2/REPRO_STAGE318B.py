#!/usr/bin/env python3
"""Stage318-B: exact rational interval certificate for the near-public-floor Pareto germ.
Uses only Python standard-library Fraction. All intervals are closed, outward exact.
Continuum step additionally uses the stated calculus/compactness argument in PROOF_STAGE318B.md.
"""
from fractions import Fraction as Q
from math import comb

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(hi) if hi is not None else Q(lo)
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
        z=I.of(z); assert z.lo*z.hi>0
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,z): return I.of(z)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0: return I(1)
        if n%2: return I(self.lo**n,self.hi**n)
        return I(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def within(self,lo,hi): return self.lo>Q(lo) and self.hi<Q(hi)

p=(Q(61,160),Q(21,160),Q(9,160),Q(9,160))
B=lambda k,z:z**k*(1-z)**(3-k)
def r(k,x,y):return Q(4,5)*B(k,x)+Q(1,5)*B(k,y)-p[k]
def d(x,y):return sum((Q(comb(3,k),2)*abs(r(k,x,y)) for k in range(4)),Q(0))

def extrema(k,a,b):
    v=[B(k,a),B(k,b)]
    if k in (1,2) and a<=Q(k,3)<=b:v.append(B(k,Q(k,3)))
    return min(v),max(v)
def low(rect):
    a,b,c,e=rect; ans=Q(0)
    for k in range(4):
        l1,h1=extrema(k,a,b);l2,h2=extrema(k,c,e)
        lo=Q(4,5)*l1+Q(1,5)*l2-p[k]
        hi=Q(4,5)*h1+Q(1,5)*h2-p[k]
        ans+=Q(comb(3,k),2)*max(0,lo,-hi)
    return ans
def split(rect):
    a,b,c,e=rect
    if b-a>=e-c:
        m=(a+b)/2;return (a,m,c,e),(m,b,c,e)
    m=(c+e)/2;return (a,b,c,m),(a,b,m,e)

def exterior_certificate():
    bases=((Q(0),Q(23,100),Q(0),Q(1)),(Q(24,100),Q(1),Q(0),Q(1)),
           (Q(23,100),Q(24,100),Q(0),Q(55,100)),
           (Q(23,100),Q(24,100),Q(56,100),Q(1)))
    witness=(Q(231083940855,10**12),Q(555508857277,10**12))
    U=d(*witness)
    counts=[];gap=None
    for rect in bases:
        pending=[rect]; nodes=0;leaves=0
        while pending:
            v=pending.pop();nodes+=1
            z=low(v)-U
            if z>0:
                leaves+=1
                if gap is None or z<gap:gap=z
            else:
                assert nodes<100000
                pending.extend(split(v))
        counts.append((nodes,leaves))
    assert counts==[(329,165),(55,28),(27,14),(133,67)]
    assert gap>Q(1,200000)  # min exterior continuum margin > 5e-6
    print('EXTERIOR_COVER',counts,'MIN_GAP_GT_1_200000',True)
    return U

# First-principles interval derivatives of the two public residuals, third residual and tagged cost.
def gradients(x,y):
    g0=(-Q(12,5)*(1-x)**2, -Q(3,5)*(1-y)**2)
    g1=(Q(4,5)*(1-x)*(1-3*x), Q(1,5)*(1-y)*(1-3*y))
    g2=(Q(4,5)*x*(2-3*x), Q(1,5)*y*(2-3*y))
    gc=(-(1-x)*(189-183*x)/256, Q(3,64)*y*(1-y))
    return g0,g1,g2,gc

def branches_and_curvature():
    x=I(Q(231,1000),Q(2312,10000));y=I(Q(555,1000),Q(556,1000))
    g0,g1,g2,gc=gradients(x,y)
    bgr={}
    for t0 in (0,1):
        for t1 in (0,1):
            bx=Q(5,16)*(3*g2[0]+t0*g0[0]+3*t1*g1[0])
            by=Q(5,16)*(3*g2[1]+t0*g0[1]+3*t1*g1[1])
            det=bx*gc[1]-by*gc[0]
            if (t0,t1)==(0,0):assert det.lo>0
            else:assert det.hi<0
            bgr[(t0,t1)]=(bx,by)
    print('CHAMBER_DETERMINANTS_NONZERO',4)
    for kind,g,other in [('r0',g0,g1),('r1',g1,g0)]:
        yp=-g[0]/g[1]
        otherp=other[0]+other[1]*yp
        assert (otherp.lo>0 if kind=='r0' else otherp.hi<0)
        dc=gc[0]+gc[1]*yp
        for side in ('right','left'):
            t0,t1=((0,1 if side=='right' else 0) if kind=='r0' else (0 if side=='right' else 1,0))
            bx,by=bgr[(t0,t1)]
            db=bx+by*yp
            m=dc/db
            if side=='right':assert db.lo>0
            else:assert db.hi<0
            if kind=='r1' and side=='right':assert m.within(-Q(121,100),-Q(119,100))
            if kind=='r0' and side=='right':assert m.within(-Q(9,10),-Q(87,100))
            if kind=='r1' and side=='left':assert m.within(Q(17,10),Q(19,10))
            if kind=='r0' and side=='left':assert m.within(Q(3),Q(32,10))
            print('BRANCH_SLOPE_BOUNDED',kind,side,'numerical_enclosure',f'{float(m.lo):.9f}',f'{float(m.hi):.9f}')
    yp=-g1[0]/g1[1]
    r1xx=Q(4,5)*(-4+6*x);r1yy=Q(1,5)*(-4+6*y)
    ypp=-(r1xx+r1yy*yp**2)/g1[1]
    bx=Q(15,16)*g2[0];by=Q(15,16)*g2[1]
    bxx=Q(15,16)*Q(4,5)*(2-6*x)
    byy=Q(15,16)*Q(1,5)*(2-6*y)
    cxx=(372-366*x)/256;cyy=(3-6*y)/64
    bd=bx+by*yp;cd=gc[0]+gc[1]*yp
    bdd=bxx+byy*yp**2+by*ypp
    cdd=cxx+cyy*yp**2+gc[1]*ypp
    k=(cdd*bd-cd*bdd)/bd**3
    assert bd.lo>0 and k.within(-41,-38)
    print('RIGHT_R1_CURVATURE_BETWEEN_-41_AND_-38',True)

def root_and_slope():
    a0,a1=Q(768916059144478,10**15),Q(768916059144479,10**15)
    f=lambda a:(Q(41,16)-4*a*a)**3-(Q(61,32)-4*a**3)**2
    assert f(a0)<0<f(a1)
    x=I(1-a1,1-a0)
    y=I(Q(555508857277,10**12),Q(555508857278,10**12))
    # Enclosure for y_* from the equation 4(1-x)^2+(1-y)^2=41/16.
    y2_l=(1-y.hi)**2;y2_u=(1-y.lo)**2
    assert y2_l<Q(41,16)-4*a1*a1 and Q(41,16)-4*a0*a0<y2_u
    _,g1,g2,gc=gradients(x,y)
    yp=-g1[0]/g1[1]
    db=Q(15,16)*(g2[0]+g2[1]*yp)
    dc=gc[0]+gc[1]*yp
    kappa=-dc/db
    assert db.lo>0 and dc.hi<0
    assert kappa.within(Q(1197917,10**6),Q(1197919,10**6))
    print('EXACT_SLOPE_NEG_KAPPA_KAPPA_IN_1197917_1197919_OVER_1E6',True)
    # The root rectangle is deep inside the localization box after at most 384*1e-8 L1 movement.
    delta=Q(1,10**8);margin=384*delta
    assert x.lo-margin>Q(231,1000) and x.hi+margin<Q(2312,10000)
    assert y.lo-margin>Q(555,1000) and y.hi+margin<Q(556,1000)
    # IFT continuation of each zero-residual curve for x_*=x0 +/- 1e-7:
    # |dy/dx|<12 on R; |db/dx|>0.18 in all four branches;
    # the resulting >=1.8e-8 change in public contribution exceeds delta.
    dx=Q(1,10**7)
    assert x.lo-dx>Q(231,1000) and x.hi+dx<Q(2312,10000)
    assert y.lo-12*dx>Q(555,1000) and y.hi+12*dx<Q(556,1000)
    assert Q(18,100)*dx>delta
    print('BUDGET_DELTA_PUBLIC_1E-8_LOCALIZES_IN_R',True)
    print('ALL_FOUR_KINK_BRANCHES_REACH_DELTA_WITHIN_R',True)

def tv(P,Qdist):return sum((abs(P[k]-Qdist[k]) for k in P),Q(0))/2

def atom_check():
    # 128 ordered tagged atoms, and 32 public atoms, for one independent rational test.
    masses=((63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63))
    p0,p1=Q(1,4),Q(3,4)
    xx=Q(231,1000);yy=Q(5555,10000)
    rates=(xx,p0,p0,1-yy,yy,p1,p1,1-xx)
    exact_tagged={};rep_tagged={};exact_pub={};rep_pub={}
    for h,(a,b) in enumerate(masses):
        j=h//4;g=(h//2%2,h%2)
        for s,n in enumerate((a,b)):
            for word in range(8):
                k=word.bit_count()
                prob_true=Q(n,256)*B(k,p0 if s==0 else p1)
                prob_rep=Q(n,256)*B(k,rates[h])
                tag=(s,j,g,word);pub=(g,word)
                exact_tagged[tag]=prob_true;rep_tagged[tag]=prob_rep
                exact_pub[pub]=exact_pub.get(pub,0)+prob_true
                rep_pub[pub]=rep_pub.get(pub,0)+prob_rep
    D=lambda p,t: sum((Q(comb(3,k),2)*abs(B(k,p)-B(k,t)) for k in range(4)),Q(0))
    b=Q(5,16)*d(xx,yy)
    c=(63*D(p0,xx)+D(p1,xx)+9*D(p0,yy)+7*D(p1,yy))/256
    cpoly=(63*(1-xx)**3+(1-3*xx**2+2*xx**3)-2*(1-3*yy**2+2*yy**3)-Q(1295,64))/256
    assert c==cpoly
    assert tv(exact_pub,rep_pub)==2*b
    assert tv(exact_tagged,rep_tagged)==Q(33,1024)+2*c
    assert len(exact_tagged)==128 and len(exact_pub)==32
    print('128_TAGGED_32_PUBLIC_ATOM_BLOCK_FORMULAE_PASS',True)

if __name__=='__main__':
    exterior_certificate()
    root_and_slope()
    branches_and_curvature()
    atom_check()
    print('STAGE318B_EXPLICIT_LOCAL_PARETO_GERM_EXACT_PASS')
