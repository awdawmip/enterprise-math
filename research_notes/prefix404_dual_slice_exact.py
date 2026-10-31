#!/usr/bin/env python3
"""PREFIX-404 author-side exact solver: I1,I2,Cu exact; I3,Cv,I4,I5 closed rational bands.

This solves the complementary slice of PREFIX-403 (not the full all-noisy problem).
Every comparison must be established symbolically. Unknown -> exception, never NO.
"""
from dataclasses import dataclass
from itertools import combinations
import sympy as S

Q = S.Rational
I = S.I
A4, B4, C4 = Q(5,2)+Q(9,2)*I, Q(3,2)+Q(7,2)*I, 4*I
A5, B5, C5 = Q(11,4)+Q(15,8)*I, Q(11,4)+Q(15,8)*I, Q(5,4)+Q(9,4)*I
LABELS = ('I3','Cv','I4','I5')


def real(z): return S.simplify(S.re(S.expand_complex(z)))
def imag(z): return S.simplify(S.im(S.expand_complex(z)))
def abs2(z): return S.simplify(S.expand_complex(z*S.conjugate(z)))


def sign(x):
    x = S.simplify(x)
    s = S.sign(x)
    if s in (S.Integer(-1), S.Integer(0), S.Integer(1)):
        return int(s)
    if x.is_positive is True: return 1
    if x.is_negative is True: return -1
    if x.is_zero is True: return 0
    raise ArithmeticError('Unresolved exact sign: ' + str(x))


@dataclass(frozen=True)
class Circle:
    x: object
    y: object
    r2: object
    tag: str


def centers_for_u(u):
    return {
        'I3': (Q(0), Q(0), Q(1)),
        'Cv': (Q(-1), Q(0), Q(1)),
        'I4': (real(-(A4+B4*u)/C4), imag(-(A4+B4*u)/C4), abs2(C4)),
        'I5': (real(-(A5+B5*u)/C5), imag(-(A5+B5*u)/C5), abs2(C5)),
    }


def make_circles(u, bands):
    centers = centers_for_u(u)
    circles = []
    for name in LABELS:
        lo, hi = bands[name]
        if sign(hi-lo)<0: raise ValueError('Reversed interval: ' + name)
        if sign(hi)<0: return None, centers
        x,y,alpha = centers[name]
        circles.append(Circle(x,y,S.simplify(hi/alpha),name+':upper'))
        if sign(lo)>0:
            circles.append(Circle(x,y,S.simplify(lo/alpha),name+':lower'))
    distinct=[]
    for c in circles:
        if not any(sign(c.x-d.x)==0 and sign(c.y-d.y)==0
                   and sign(c.r2-d.r2)==0 for d in distinct):
            distinct.append(c)
    return distinct,centers


def candidates(circles):
    for c in circles:
        r = S.sqrt(c.r2)
        yield (S.simplify(c.x-r), c.y, c.tag+':L')
        if sign(c.r2)>0:
            yield (S.simplify(c.x+r),c.y,c.tag+':R')
    for a,b in combinations(circles,2):
        dx=S.simplify(b.x-a.x); dy=S.simplify(b.y-a.y)
        d2=S.simplify(dx*dx+dy*dy)
        if sign(d2)==0: continue
        t=S.simplify((a.r2-b.r2+d2)/(2*d2))
        h2=S.simplify(a.r2-t*t*d2)
        if sign(h2)<0: continue
        x0=S.simplify(a.x+t*dx); y0=S.simplify(a.y+t*dy)
        rad=S.sqrt(S.simplify(h2/d2))
        for epsilon in ((1,) if sign(h2)==0 else (-1,1)):
            yield (S.simplify(x0-epsilon*dy*rad),
                   S.simplify(y0+epsilon*dx*rad),a.tag+'~'+b.tag)


def violations(x,y,centers,bands):
    for name in LABELS:
        cx,cy,alpha=centers[name]
        value=S.simplify(alpha*((x-cx)**2+(y-cy)**2))
        lo,hi=bands[name]
        if sign(value-lo)<0: return (name,'below',value-lo)
        if sign(value-hi)>0: return (name,'above',value-hi)
    return None


def decide(j, cu, bands):
    """Complete in algebraic-number model; return (YES/NO,witness,checked,circles).

    All four bands rational finite closed intervals; j,cu exact rationals.
    The mathematical result assumes a complete comparator. This SymPy
    implementation raises if any required exact comparison is unresolved.
    """
    if set(bands)!=set(LABELS): raise ValueError('Specify exactly four bands')
    if sign(j)<0: return False,None,0,0
    x=S.simplify((cu-1-j)/2)
    d2=S.simplify(j-x*x)
    if sign(d2)<0: return False,None,0,0
    d=S.sqrt(d2)
    uroots=[S.simplify(x+I*d)] if sign(d2)==0 else [S.simplify(x+I*d),S.simplify(x-I*d)]
    checked=0; maxcircles=0
    for u in uroots:
        circles,centers=make_circles(u,bands)
        if circles is None: continue
        maxcircles=max(maxcircles,len(circles))
        for a,b,tag in candidates(circles):
            checked+=1
            if violations(a,b,centers,bands) is None:
                return True,(u,S.simplify(a+I*b),tag),checked,maxcircles
    return False,None,checked,maxcircles


def measurements(u,v):
    return {'I2':abs2(u),'Cu':abs2(1+u),
            'I3':abs2(v),'Cv':abs2(1+v),
            'I4':abs2(A4+B4*u+C4*v),
            'I5':abs2(A5+B5*u+C5*v)}


def band(center, radius): return (S.simplify(center-radius), S.simplify(center+radius))


def test_suite():
    assert abs2(C4)==16 and abs2(C5)==Q(53,8)
    assert abs2(A4)==Q(53,2) and abs2(A5)==Q(709,64)
    # Two exact u-observers, noisy v-observers. Tight exact v=0 in the first example.
    m=measurements(0,0)
    bands={'I3':band(0,Q(1,10)), 'Cv':band(1,Q(1,100)),
           'I4':band(m['I4'],Q(1,2)), 'I5':band(m['I5'],Q(1,2))}
    yes,w,n,k=decide(Q(0),Q(1),bands)
    assert yes and w and n<=144
    assert all(sign(measurements(w[0],w[1])[key]-bands[key][0])>=0 and
               sign(measurements(w[0],w[1])[key]-bands[key][1])<=0 for key in bands)
    print('PASS dual rational/noisy YES',n,'candidates',k,'circles')
    bad={**bands,'I4':(Q(0),Q(1))}
    no,w,n,k=decide(Q(0),Q(1),bad)
    assert not no and w is None and n<=144
    print('PASS dual rational/noisy NO',n,'candidates',k,'circles')

    # Two u branches. A zero-radius I3 band forces v=0, and exact I4/I5 are tested.
    m=measurements(I,0)
    tight={name:band(m[name],Q(0)) for name in LABELS}
    yes,w,n,k=decide(Q(1),Q(2),tight)
    assert yes and w and n<=144
    assert w[0] in (I,-I) and w[1]==0
    print('PASS dual two-u-branches YES',n,'candidates',k,'circles')
    wrong={**tight,'I4':(Q(1000),Q(1000))}
    no,w,n,k=decide(Q(1),Q(2),wrong)
    assert not no and w is None and n<=144
    print('PASS dual two-u-branches NO',n,'candidates',k,'circles')
    print('PASS_PREFIX404_DUAL_144_CANDIDATES_EXACT_U_NOISY_V')

if __name__=='__main__': test_suite()
