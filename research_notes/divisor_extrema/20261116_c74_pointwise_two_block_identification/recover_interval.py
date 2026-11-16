"""Invert a pair of H(0,1) readings from two different initial stocks, first landing known."""
from fractions import Fraction
from math import isqrt
import json
from check_same import outer, inner_intervals, rank_invariant


def roots(a,b,c):
    if a==0:
        if b: return [-c/b]
        raise ValueError('degenerate or inconsistent readings')
    det=b*b-4*a*c
    if det<0:return []
    root=Fraction(isqrt(det.numerator),isqrt(det.denominator))
    if root*root!=det:return []
    return list({(-b+root)/(2*a),(-b-root)/(2*a)})


def recover(v,c,g,cc,gg):
    if cc<=c or c<v:raise ValueError('distinct ordered legal stocks required')
    data=[]
    for n,value in ((c,g),(cc,gg)):
        p,q=outer(n,v)
        r=value if q>p else 1/value
        e=(r-1)/(q-p)
        data.append((p*q,p+q,1/e-p))
    s,t,z=data[0];S,T,Z=data[1]
    offset=(Z-z)/(T-t)
    slope=(S-s)/(T-t)
    # z = s*u + t*h + h(h+1)/u, with h=offset-slope*u.
    quadratic=s-t*slope+slope*slope
    linear=t*offset-slope*(2*offset+1)-z
    const=offset*(offset+1)
    solutions=[]
    for u in roots(quadratic,linear,const):
        h=offset-slope*u
        if u<=0 or h<=0: continue
        interval=(h/u,(h+1)/u)
        solutions.append(interval)
    return solutions


def read(n,v,I):
    p,q=outer(n,v)
    r=1+(q-p)*rank_invariant(p,q,I)
    return max(r,1/r)


if __name__=='__main__':
    tested=0
    for v in range(2,27):
        for _,I in inner_intervals(v):
            for c,cc in ((v,v+1),(v+2,2*v),(v+3,2*v+5)):
                if cc<=c:continue
                recovered=recover(v,c,read(c,v,I),cc,read(cc,v,I))
                assert recovered==[I]
                tested+=1
    print(json.dumps(dict(two_stock_interval_recoveries=tested)))
