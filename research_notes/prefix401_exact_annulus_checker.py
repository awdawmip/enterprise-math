#!/usr/bin/env python3
"""PREFIX-401: exact finite disk/annulus-feasibility algorithm for singular five-port slice.

Inputs: rational closed bands on I3,I4,I5,Cv; I1,I2,Cu are fixed.
No floating-point arithmetic is used in decisions.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations

N = F(75154)
K4 = F(300616, 3969)
K5 = F(2638189, 63504)
J4 = F(550600, 3969)
J5 = F(4417309, 63504)
CPLUS = F(5)
CMINUS = F(97357, 37577)

# (alpha,beta,gamma,constant): obs=alpha*(T*T+S*S)+beta*T+gamma*S+constant
OBS = {
    'I3': (F(1)/N, F(0), F(0), F(0)),
    'I4': (F(16)/N, F(16,63), F(0), K4),
    'I5': (F(53)/(8*N), F(61,504), F(0), K5),
    'Cv': (F(1)/N, F(490)/N, F(246)/N, F(1)),
}


def sign_rat(a):
    return (a > 0) - (a < 0)


@dataclass(frozen=True)
class Surd:
    a: F
    b: F
    d: F

    def __add__(self, other):
        if not isinstance(other, Surd):
            other = Surd(F(other), F(0), self.d)
        assert self.d == other.d
        return Surd(self.a + other.a, self.b + other.b, self.d)

    __radd__ = __add__

    def __neg__(self):
        return Surd(-self.a,-self.b,self.d)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Surd) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, Surd):
            other=Surd(F(other),F(0),self.d)
        assert self.d == other.d
        return Surd(self.a*other.a+self.b*other.b*self.d,
                    self.a*other.b+self.b*other.a,self.d)

    __rmul__ = __mul__

    def cmp0(self):
        """Exact sign of a+b*sqrt(d), d>=0 rational."""
        assert self.d >= 0
        a,b=self.a,self.b
        if b == 0 or self.d == 0:
            return sign_rat(a)
        if a == 0:
            return sign_rat(b)
        if sign_rat(a) == sign_rat(b):
            return sign_rat(a)
        q=a*a-b*b*self.d
        return sign_rat(q)*sign_rat(a)


@dataclass(frozen=True)
class P:
    x: Surd
    y: Surd
    tag: str


@dataclass(frozen=True)
class Circle:
    x: F
    y: F
    r2: F
    tag: str


def point(xa,xb,ya,yb,d,tag):
    return P(Surd(F(xa),F(xb),F(d)),Surd(F(ya),F(yb),F(d)),tag)


def circles_for_bands(bands):
    """bands: name -> (low, high), exact rational closed intervals."""
    cs=[]
    for name,(lo,hi) in bands.items():
        alpha,beta,gamma,constant=OBS[name]
        assert alpha > 0 and lo <= hi
        cx=-beta/(2*alpha)
        cy=-gamma/(2*alpha)
        minimum=constant-(beta*beta+gamma*gamma)/(4*alpha)
        rh=(hi-minimum)/alpha
        if rh < 0:
            return None # full feasible set empty
        rl=(lo-minimum)/alpha
        cs.append(Circle(cx,cy,rh,name+'_upper'))
        if rl > 0:
            cs.append(Circle(cx,cy,rl,name+'_lower'))
    # Coincident circles are the same locus; strip inequalities remain distinct at evaluation.
    seen=set(); out=[]
    for c in cs:
        key=(c.x,c.y,c.r2)
        if key not in seen:
            seen.add(key);out.append(c)
    return out


def candidates(cs):
    """<=2n+2*binom(n,2) points, with n<=8."""
    for a in cs:
        for s in (-1,1):
            yield point(a.x,F(s),a.y,0,a.r2,a.tag+('_L' if s<0 else '_R'))
    for a,b in combinations(cs,2):
        dx=b.x-a.x; dy=b.y-a.y
        dist2=dx*dx+dy*dy
        if dist2 == 0:
            continue # unequal concentric circles cannot intersect, equal ones were deduped
        t=(a.r2-b.r2+dist2)/2
        h2=a.r2-t*t/dist2
        if h2 < 0:
            continue
        x0=a.x+t*dx/dist2
        y0=a.y+t*dy/dist2
        for s in (-1,1) if h2>0 else (1,):
            yield point(x0,-F(s)*dy,y0,F(s)*dx,h2/dist2,a.tag+'~'+b.tag)


def eval_observation(p,name):
    alpha,beta,gamma,const=OBS[name]
    return alpha*(p.x*p.x+p.y*p.y)+beta*p.x+gamma*p.y+const


def violation(p,bands):
    for name,(lo,hi) in bands.items():
        q=eval_observation(p,name)
        if (q-lo).cmp0()<0:
            return (name,'BELOW',q-lo)
        if (q-hi).cmp0()>0:
            return (name,'ABOVE',q-hi)
    return None


def decide(bands):
    assert set(bands)==set(OBS)
    cs=circles_for_bands(bands)
    if cs is None:
        return False,None,0,0
    seen=0
    for p in candidates(cs):
        seen+=1
        if violation(p,bands) is None:
            return True,p,seen,len(cs)
    return False,None,seen,len(cs)


def bnd(c,e):
    return F(c)-F(e),F(c)+F(e)


def suite():
    cases=[
        ('nominal-positive-exact',{'I3':bnd(2,0),'I4':bnd(J4,0),'I5':bnd(J5,0),'Cv':bnd(CPLUS,0)},True),
        ('nominal-negative-exact',{'I3':bnd(2,0),'I4':bnd(J4,0),'I5':bnd(J5,0),'Cv':bnd(CMINUS,0)},True),
        ('joint-positive',{'I3':bnd(2,F(1,10)),'I4':bnd(J4,F(1,10)),'I5':bnd(J5,F(1,10)),'Cv':bnd(CPLUS,1)},True),
        ('joint-negative',{'I3':bnd(2,F(1,10)),'I4':bnd(J4,F(1,10)),'I5':bnd(J5,F(1,10)),'Cv':bnd(CMINUS,1)},True),
        ('joint-midpoint-no',{'I3':bnd(2,F(1,10)),'I4':bnd(J4,F(1,10)),'I5':bnd(J5,F(1,10)),'Cv':bnd((CPLUS+CMINUS)/2,1)},False),
        ('negative-I3-no',{'I3':bnd(-1,F(1,10)),'I4':bnd(J4,F(1,10)),'I5':bnd(J5,F(1,10)),'Cv':bnd(CPLUS,1)},False),
        ('exact-midpoint-no',{'I3':bnd(2,0),'I4':bnd(J4,0),'I5':bnd(J5,0),'Cv':bnd((CPLUS+CMINUS)/2,0)},False),
        ('larger-center-interior',{'I3':bnd(2,F(1,2)),'I4':bnd(J4,2),'I5':bnd(J5,2),'Cv':bnd(CPLUS,2)},True),
    ]
    for label,bands,expected in cases:
        result,p,n,nc=decide(bands)
        assert result==expected,(label,result,expected)
        assert n <= 72
        print(f'CHECK {label} verdict={"YES" if result else "NO"} tested={n} circle_count={nc} witness={p.tag if p else "none"}')

    delta=F(1,10); xi=F(1,10)
    dt=F(63,16)*xi+63*delta
    min_s2=N*(2-delta)-(122+dt)**2
    assert min_s2 > 355**2
    ds=(N*delta+(244+dt)*dt)/(355+368)
    H=delta+F(2,N)*(245*dt+123*ds)
    gap=(CPLUS-CMINUS)-2-2*H
    assert gap > 0
    assert F(1,10)>0 and len(OBS)==4
    print('BOUND deltaT=',dt,'min_sigma_squared=',min_s2,'sigma_lower=355')
    print('BOUND delta_sigma<=',ds,'H<=',H,'uniform_gap>',gap)
    print('PASS_PREFIX401_FINITE_72_CANDIDATE_FOUR_ANNULUS_FEASIBILITY_AND_INTERVAL_I3_BRANCH_SEPARATION')


if __name__=='__main__':
    suite()
