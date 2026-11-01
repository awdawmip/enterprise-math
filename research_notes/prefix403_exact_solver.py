#!/usr/bin/env python3
"""PREFIX-403: exact algebraic four-annulus lift for exact I3 and Cv.

Inputs: I1=1, exact rational (I3,Cv), four rational closed
measurement bands (I2,Cu,I4,I5). An undecidable comparison in this
SymPy implementation raises (never guesses); the theorem assumes a
complete exact real-algebraic comparator. No floating point in verdicts.
"""
from dataclasses import dataclass
from itertools import combinations
import sympy as S

Q = S.Rational
I = S.I
A4,B4,C4 = Q(5,2)+Q(9,2)*I, Q(3,2)+Q(7,2)*I, 4*I
A5,B5,C5 = Q(11,4)+Q(15,8)*I, Q(11,4)+Q(15,8)*I, Q(5,4)+Q(9,4)*I


def real(z):
    return S.simplify(S.re(S.expand_complex(z)))


def imag(z):
    return S.simplify(S.im(S.expand_complex(z)))


def sqabs(z):
    return S.simplify(S.expand_complex(z*S.conjugate(z)))


def sign(x):
    """Only return when SymPy establishes an exact algebraic sign."""
    x = S.simplify(x)
    y = S.sign(x)
    if y in (S.Integer(-1), S.Integer(0), S.Integer(1)):
        return int(y)
    if x.is_positive is True: return 1
    if x.is_negative is True: return -1
    if x.is_zero is True: return 0
    raise ArithmeticError(f'Exact algebraic sign unresolved: {x}')


@dataclass(frozen=True)
class Circle:
    x: object
    y: object
    r2: object
    tag: str


def make_circles(v, bands):
    centers = {
        'I2': (Q(0), Q(0), Q(1)),
        'Cu': (Q(-1), Q(0), Q(1)),
    }
    for label,a,b,c in [('I4',A4,B4,C4),('I5',A5,B5,C5)]:
        center = S.expand_complex(-(a+c*v)/b)
        centers[label] = (real(center),imag(center),sqabs(b))
    circles = []
    for name in ('I2','Cu','I4','I5'):
        lo,hi = bands[name]
        if sign(hi-lo)<0:
            raise ValueError('Reversed interval: '+name)
        cx,cy,alpha=centers[name]
        if sign(hi)<0: return None, centers
        rhi = S.simplify(hi/alpha)
        circles.append(Circle(cx,cy,rhi,name+':upper'))
        if sign(lo)>0:
            circles.append(Circle(cx,cy,S.simplify(lo/alpha),name+':lower'))
    distinct=[]
    for c in circles:
        if not any(sign(c.x-d.x)==sign(c.y-d.y)==sign(c.r2-d.r2)==0 for d in distinct):
            distinct.append(c)
    return distinct,centers


def candidates(circles):
    for c in circles:
        r = S.sqrt(c.r2)
        yield (S.simplify(c.x-r), c.y, c.tag+':L')
        if sign(c.r2)>0:
            yield (S.simplify(c.x+r), c.y, c.tag+':R')
    for a,b in combinations(circles,2):
        dx=S.simplify(b.x-a.x); dy=S.simplify(b.y-a.y)
        d2=S.simplify(dx*dx+dy*dy)
        if sign(d2)==0: continue
        t=S.simplify((a.r2-b.r2+d2)/(2*d2))
        h2=S.simplify(a.r2-t*t*d2)
        if sign(h2)<0: continue
        x0=S.simplify(a.x+t*dx); y0=S.simplify(a.y+t*dy)
        q=S.sqrt(S.simplify(h2/d2))
        for eps in ((1,) if sign(h2)==0 else (-1,1)):
            yield (S.simplify(x0-eps*dy*q),S.simplify(y0+eps*dx*q),a.tag+'~'+b.tag)


def violation(x,y,centers,bands):
    for name in ('I2','Cu','I4','I5'):
        cx,cy,alpha=centers[name]
        val=S.simplify(alpha*((x-cx)**2+(y-cy)**2))
        lo,hi=bands[name]
        if sign(val-lo)<0: return (name,'below',val-lo)
        if sign(val-hi)>0: return (name,'above',val-hi)
    return None


def decide(k,q,bands):
    """Return verdict, source witness (u,v), and checked candidate count.

    If no algebraic sign routine is available for an input, raise rather
    than treating it as NO. Mathematical 144-candidate theorem is general.
    """
    if set(bands)!=set(('I2','Cu','I4','I5')):
        raise ValueError('Specify exactly four observation bands')
    if sign(k)<0: return False,None,0,0
    c=S.simplify((q-1-k)/2)
    d2=S.simplify(k-c*c)
    if sign(d2)<0: return False,None,0,0
    d=S.sqrt(d2)
    roots=[S.simplify(c+I*d)] if sign(d2)==0 else [S.simplify(c+I*d),S.simplify(c-I*d)]
    checked=0; maxcircles=0
    for v in roots:
        circles,centers=make_circles(v,bands)
        if circles is None: continue
        maxcircles=max(maxcircles,len(circles))
        for x,y,tag in candidates(circles):
            checked+=1
            if violation(x,y,centers,bands) is None:
                return True,(S.simplify(x+I*y),v,tag),checked,maxcircles
    return False,None,checked,maxcircles


def interval(q,e): return (S.simplify(q-e), S.simplify(q+e))


def observables(u,v):
    return {'I2':sqabs(u),'Cu':sqabs(1+u),
            'I3':sqabs(v),'Cv':sqabs(1+v),
            'I4':sqabs(A4+B4*u+C4*v),
            'I5':sqabs(A5+B5*u+C5*v)}


def run_suite():
    u0=Q(59,63); up=u0+I/Q(10000); v=1+I
    o=observables(up,v)
    assert o['I2']-Q(3481,3969)==Q(1,10**8)
    assert o['Cu']-Q(14884,3969)==Q(1,10**8)
    bands={'I2':interval(Q(3481,3969),Q(1,10**8)),
           'Cu':interval(Q(14884,3969),Q(1,10**8)),
           'I4':interval(o['I4'],0),'I5':interval(o['I5'],0)}
    yes,w,n,m=decide(o['I3'],o['Cv'],bands)
    assert yes and w is not None and n<=144
    assert all(sign(observables(w[0],w[1])[j]-bands[j][0])>=0 and sign(observables(w[0],w[1])[j]-bands[j][1])<=0 for j in bands)
    print('PASS precise-variable-u repair: YES', 'checked',n,'circles',m, 'v=',w[1])

    # The same real record with nominal exact u observables is impossible,
    # reproducing PREFIX-402's sound frozen-u witness boundary in a full solver.
    frozen={'I2':interval(Q(3481,3969),0),
            'Cu':interval(Q(14884,3969),0),
            'I4':interval(o['I4'],0),'I5':interval(o['I5'],0)}
    no,w,n,m=decide(o['I3'],o['Cv'],frozen)
    assert not no and w is None and n<=144
    print('PASS nominal-u impossible: NO','checked',n,'circles',m)

    # Non-rational source root: k=2, Cv=3 gives v=+/-i sqrt(2).
    # Setting I2=0 forces u=0; other bands are wide rational enclosures.
    radical={'I2':(Q(0),Q(0)),'Cu':(Q(1),Q(1)),
             'I4':(Q(0),Q(1000)),'I5':(Q(0),Q(1000))}
    yes,w,n,m=decide(Q(2),Q(3),radical)
    assert yes and w and n<=144
    print('PASS quadratic-v-source: YES', 'checked',n,'circles',m)

    no,w,n,m=decide(Q(2),Q(3),{**radical,'Cu':(Q(4),Q(4))})
    assert not no and w is None and n<=144
    print('PASS quadratic-v-conflict: NO', 'checked',n,'circles',m)
    assert sqabs(B4)==Q(29,2) and sqabs(B5)==Q(709,64)
    print('PASS_PREFIX403_144_CANDIDATES_NOISY_U_EXACT_I3_CV')


if __name__=='__main__': run_suite()
