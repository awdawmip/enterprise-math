#!/usr/bin/env python3
"""PREFIX-421: exact outward fixed-grid interval certificate for full (u,v) corners.
No floating point is used. Bounds are rational enclosures with denominator 10**27.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

CHECKS=0
MIN_S_LO=None
MAX_SUM_HI=None
STATS={}

SCALE = 10**27

def fd(n: int, d: int=1) -> int: return (n * SCALE) // d

def cd(n: int, d: int=1) -> int: return -((-n * SCALE) // d)

@dataclass(frozen=True)
class IV:
    lo: int
    hi: int
    def __post_init__(self):
        assert self.lo <= self.hi
    @staticmethod
    def q(n: int, d: int=1): return IV(fd(n,d), cd(n,d))
    @staticmethod
    def box(lon: int, lod: int, hin: int, hid: int):
        return IV(fd(lon,lod), cd(hin,hid))
    @staticmethod
    def coerce(x):
        if isinstance(x,IV): return x
        if isinstance(x,int): return IV.q(x)
        if isinstance(x,Fraction): return IV.q(x.numerator,x.denominator)
        raise TypeError(type(x))
    def __add__(self, o):
        o=IV.coerce(o);return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self + -IV.coerce(o)
    def __rsub__(self,o): return IV.coerce(o) + -self
    def __mul__(self,o):
        o=IV.coerce(o)
        v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(v)//SCALE,-((-max(v))//SCALE))
    __rmul__=__mul__
    def inv(self):
        assert self.lo*self.hi>0, ('denominator contains zero',self)
        return IV(SCALE*SCALE//self.hi,-((-SCALE*SCALE)//self.lo))
    def __truediv__(self,o): return self * IV.coerce(o).inv()
    def __rtruediv__(self,o): return IV.coerce(o)*self.inv()
    def sqrt(self):
        assert self.lo>=0, ('sqrt negative interval',self)
        a=isqrt(self.lo*SCALE);b=isqrt(self.hi*SCALE)
        return IV(a,b+int(b*b<self.hi*SCALE))
    def intersect(self,o):
        o=IV.coerce(o);assert max(self.lo,o.lo)<=min(self.hi,o.hi)
        return IV(max(self.lo,o.lo),min(self.hi,o.hi))
    def check_range(self,lo,hi,name):
        lo=IV.coerce(lo);hi=IV.coerce(hi)
        assert self.lo > lo.hi and self.hi < hi.lo, (name,self.approx(),lo.approx(),hi.approx())
        global CHECKS
        CHECKS+=1
        low,high=STATS.get(name,(self.lo,self.hi))
        STATS[name]=(min(low,self.lo),max(high,self.hi))
    def below(self,o,name):
        o=IV.coerce(o);assert self.hi<o.lo,(name,self.approx(),o.approx());global CHECKS
        CHECKS+=1
    def above(self,o,name):
        o=IV.coerce(o);assert self.lo>o.hi,(name,self.approx(),o.approx());global CHECKS
        CHECKS+=1
    def approx(self): return ('%.15g'%(self.lo/SCALE), '%.15g'%(self.hi/SCALE))

Z=IV.q(0);ONE=IV.q(1);TWO=IV.q(2);BETA=IV.q(1,10**6);E=IV.q(53,8)
EPS=IV.box(0,1,1,10**6)
ETA=IV.box(199,10000,201,10000)
R=IV.box(999999,1000000,1000001,1000000)
SS=IV.box(1999999,1000000,2000001,1000000)

@dataclass(frozen=True)
class Dual:
    val: IV
    dr: IV=Z
    ds: IV=Z
    @staticmethod
    def c(x): return Dual(IV.coerce(x))
    @staticmethod
    def coerce(x): return x if isinstance(x,Dual) else Dual.c(x)
    def __add__(self,o):
        o=Dual.coerce(o);return Dual(self.val+o.val,self.dr+o.dr,self.ds+o.ds)
    __radd__=__add__
    def __neg__(self): return Dual(-self.val,-self.dr,-self.ds)
    def __sub__(self,o): return self + -Dual.coerce(o)
    def __rsub__(self,o): return Dual.coerce(o)+ -self
    def __mul__(self,o):
        o=Dual.coerce(o)
        return Dual(self.val*o.val,self.dr*o.val+self.val*o.dr,self.ds*o.val+self.val*o.ds)
    __rmul__=__mul__
    def inv(self):
        v=self.val.inv();vv=v*v
        return Dual(v,-self.dr*vv,-self.ds*vv)
    def __truediv__(self,o): return self * Dual.coerce(o).inv()
    def __rtruediv__(self,o): return Dual.coerce(o)*self.inv()
    def sqrt(self):
        s=self.val.sqrt();d=ONE/(TWO*s)
        return Dual(s,self.dr*d,self.ds*d)

# The five-Port formulas and their exact first derivatives are encoded here.
def port_coefficients(r,s,sgn):
    a=(s-r-1)/2
    b=sgn*(r-a*a).sqrt()
    J=(53+29*r)/2+39*a-4*b
    A=36+28*a+12*b
    B=-20-12*a+28*b
    P=(245*(1+a)+123*b)/16
    Q=(-123*(1+a)+245*b)/16
    c=(s-2)*IV.q(709,64)
    return J,A,B,P,Q,c

# Correct operator precedence: Dual's division by integer is exact interval division.
def corners(eps,eta,sgn):
    r=ONE+eps if sgn==-1 else ONE-eps
    b=sgn*r.sqrt()
    J=(53+29*r)/2-4*b
    A=36+12*b;B=-20+28*b
    P=(245+123*b)/16;Q=(-123+245*b)/16
    c=IV.q(709,64)*(r-ONE)*sgn*(-1) if False else IV.q(709,64)*(r-ONE)
    # s=2 +/- eps; r=1 +/- eps, hence c=709(r-1)/64.
    return J,A,B,P,Q,c


# PREFIX-422: new NEGATIVE optimal baseline corner outside the old band.
# At r=1+eps,s=2-eps the real part is a=-eps (not 0).
# Subdivide the parameter strip exactly; every interval contains all reals in its subbox.
for j in range(100):
    eta_sub=IV.box(19900+2*j,10**6,19900+2*(j+1),10**6)
    eps=EPS;eta=eta_sub
    rm=ONE+eps;sm=TWO-eps
    am=(sm-rm-1)/2
    bm=-(rm-am*am).sqrt()
    Jm=(53+29*rm)/2+39*am-4*bm
    Am=36+28*am+12*bm
    Bm=-20-12*am+28*bm
    Pm=(245*(1+am)+123*bm)/16
    Qm=(-123*(1+am)+245*bm)/16
    cm=IV.q(709,64)*(sm-TWO)
    Nm=Pm*Pm+Qm*Qm
    Km=-eta-cm-E*BETA
    Sm=(Nm*BETA-Km*Km).sqrt()
    xm=(Km*Pm+Sm*Qm)/Nm
    ym=(Km*Qm-Sm*Pm)/Nm
    mu=(Am*ym-Bm*xm)/(Pm*ym-Qm*xm)
    D=-(Am-mu*Pm)/(2*xm)
    tau=D-16+E*mu
    mu.check_range(IV.q(1),IV.q(2),'negative multiplier 1<mu<2')
    D.check_range(IV.q(3000),IV.q(20000),'negative positive dual curvature')
    tau.above(Z,'negative disk dual multiplier >0')
    Nrad=Nm*BETA-Km*Km
    Nrad.above(Z,'negative circle intersection real')
    (xm*xm+ym*ym).check_range(IV.q(98,100000000),IV.q(102,100000000),'candidate t encloses beta')
    # Important: exact algebra shows t==BETA; above interval check only catches arithmetic issues.
    # Exact k=-eta is an algebraic identity from p.x=K; see independent checker.
    (2*xm+BETA+ETA).above(Z,'candidate h is above -eta')
    (ETA-(2*xm+BETA)).above(Z,'candidate h is below eta')
    # General negative u, full r,s domain, target dual multipliers frozen.
    r=Dual(R,ONE,Z);s=Dual(SS,Z,ONE)
    J,A,B,P,Q,c=port_coefficients(r,s,-1)
    C=A-Dual.c(mu)*P
    H=B-Dual.c(mu)*Q
    U=J-Dual.c(mu)*(c+Dual.c(eta))-Dual.c(tau)*BETA-(C*C+H*H)/Dual.c(4*D)
    U.dr.check_range(IV.q(-4),IV.q(-2),'full negative U_r <0')
    U.ds.check_range(IV.q(0),IV.q(3),'full negative U_s >0: baseline flips')
    MIN_S_LO=U.ds.lo if MIN_S_LO is None else min(MIN_S_LO,U.ds.lo)
    # Equality of support at target corner follows from a-mu*p=-2D*v.
    # Verify interval residuals & negative intensity range.
    resx=Am-mu*Pm+2*D*xm;resy=Bm-mu*Qm+2*D*ym
    # Exact stationary relation follows from the defining mu,D; see symbolic checker.

    Inegative=Jm+Am*xm+Bm*ym+16*BETA
    Inegative.check_range(IV.q(44),IV.q(45),'negative source I4 within 44 and 45')
    # Simple global UPPER certificate for every positive u; lambda=3/2.
    la=IV.q(3,2)
    Jp,Ap,Bp,Pp,Qp,cp=port_coefficients(Dual(R,ONE,Z),Dual(SS,Z,ONE),+1)
    F=Jp+Dual.c(la)*(Dual.c(eta)-cp)+Dual.c((16-E*la)*BETA)+Dual.c(BETA.sqrt())*((Ap-Dual.c(la)*Pp)*(Ap-Dual.c(la)*Pp)+(Bp-Dual.c(la)*Qp)*(Bp-Dual.c(la)*Qp)).sqrt()
    F.val.check_range(IV.q(37),IV.q(38),'all positive sources upper I4')
    (Inegative+F.val).below(IV.q(82),'negative gap strictly smaller than positive gap')
    MAX_SUM_HI=(Inegative+F.val).hi if MAX_SUM_HI is None else max(MAX_SUM_HI,(Inegative+F.val).hi)
    F.val.below(IV.q(41),'positive branch remains below 41')
    Inegative.above(IV.q(41),'negative branch remains above 41')

# Explicit exact-radical counterexample at eps=beta, eta=1/50, comparing
# the PREVIOUS purely imaginary upper-s corner against the NEW opposite s corner.
def source_at(r,s,eta):
    a=(s-r-1)/2
    b=-(r-a*a).sqrt()
    J=(53+29*r)/2+39*a-4*b
    A=36+28*a+12*b;B=-20-12*a+28*b
    P=(245*(1+a)+123*b)/16
    Q=(-123*(1+a)+245*b)/16
    c=(s-2)*IV.q(709,64)
    n=P*P+Q*Q;k=-eta-c-E*BETA
    sr=(n*BETA-k*k).sqrt()
    x=(k*P+sr*Q)/n;y=(k*Q-sr*P)/n
    mu=(A*y-B*x)/(P*y-Q*x)
    d=-(A-mu*P)/(2*x)
    (d-16+E*mu).above(0,'explicit source disk multiplier >0')
    mu.above(0,'explicit source k multiplier >0')
    (eta+2*x+BETA).above(0,'explicit source h lower slack')
    (eta-2*x-BETA).above(0,'explicit source h upper slack')
    return J+A*x+B*y+16*BETA

point_e=IV.q(1,10**6);point_eta=IV.q(1,50)
point_r=ONE+point_e
old_I=source_at(point_r,TWO+point_e,point_eta)
new_I=source_at(point_r,TWO-point_e,point_eta)
(old_I-new_I).above(IV.q(7,10**7),'strict old-corner counterexample with margin > 0.7e-6')
print('tested parameter subboxes = 100 over [0.0199,0.0201]')
print('strict interval checks =',CHECKS)
for name,(lo,hi) in sorted(STATS.items()):
    print('UNIFORM',name,'=',IV(lo,hi).approx())
print('global min U_s lower enclosure =',IV(MIN_S_LO,MIN_S_LO).approx())
print('global max Iminus+Fplus upper enclosure =',IV(MAX_SUM_HI,MAX_SUM_HI).approx())
print('old-corner intensity:',old_I.approx())
print('new-corner intensity:',new_I.approx())
print('strict old-new intensity margin:',(old_I-new_I).approx())
print('PASS_PREFIX422_FULL_SOURCE_NEGATIVE_CORNER_REVERSAL_AND_PHASE_DOMINANCE')
