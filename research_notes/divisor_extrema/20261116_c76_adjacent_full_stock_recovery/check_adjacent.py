"""Replay two-stock secants for truncations and compare physical reports to native paths."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import prod, comb
import json
from check_center_line import B, P
from check_finite import native_tail_ratios


@lru_cache(None)
def block(n, s, k):
    rho = 4 * prod((F(4*j+k,4*(j+k)) for j in range(s,n+1)),start=F(1))
    a = F(P(k,n),B(k,s))
    return a, a/rho


@lru_cache(None)
def ends(w, actual):
    W=F((w+2)*(w+3)*(w+4),840)
    Y=prod((F(4*j+1,4*j+4) for j in range(3,w+1)), start=F(1))
    lo=(F(5,4),F(3,2)) if w<=3 else (F(1,2),F(6))
    params=((F(5),F(3,32)),lo)
    return tuple((1+(W/(e*Y) if actual else 0))/(1+j*W) for j,e in params)


def width(values):
    return max(values)/min(values)


def projected_values(v,w,keep_middle,keep_tail):
    b,true_t=block(v,w,3)
    t=true_t if keep_middle else 0
    return tuple((1+t*p)/(1+b*p) for p in ends(w,keep_tail))


def physical(c,v,w):
    middle=projected_values(v,w,True,True)
    a,t=block(c,v,5)
    return width([(1+t*z)/(1+a*z) for z in middle])


def two_columns(c,v,w,keep_middle,keep_tail):
    middle=projected_values(v,w,keep_middle,keep_tail)
    scaled=sorted(B(5,v)/z for z in middle)
    p,q = P(5,c),P(5,c+1)
    def inverse_width(stock):
        return 1 / (width([1/(1+F(P(5,stock),B(5,v))*z) for z in middle])-1)
    y1,y2=inverse_width(c),inverse_width(c+1)
    I=(q*y2-p*y1)/(q-p)
    S=(y1-I)*p
    assert [S/(I+1),S/I]==scaled
    return scaled


def main():
    projected=matched=0
    for v in range(2,33):
        for w in range(2,v+1):
            c=v+9
            data={key:two_columns(c,v,w,*key) for key in product([False,True],repeat=2)}
            projected+=len(data)
            old,new=data[(False,False)],data[(False,True)]
            ratio=(new[1]-new[0])/(old[1]-old[0])
            z0,z1=ends(w,False),ends(w,True)
            assert ratio==abs((z1[1]-z1[0])/(z0[1]-z0[0]))
            assert new[1]>old[1]
            if v<=11:
                for stock in (v+4,v+5):
                    assert physical(stock,v,w)==width(native_tail_ratios(stock,v,w))
                    matched+=1
    finite=[]
    for c in (12,30,60):
        pad=1
        while pad**3<c*c:
            pad+=1
        for first_stock in (c,c+pad):
            rows=[(physical(first_stock,v,w),physical(first_stock+1,v,w))
              for v in range(2,c+1) for w in range(2,v+1)]
            assert len(set(rows))==comb(c,2)
            finite.append({'upper_stock':c,'first_stock':first_stock,'different_pairs':len(rows)})
    print(json.dumps({'truncated_secant_controls':projected,'native_reports':matched,
                      'complete_small_calibrations':finite},indent=2))


if __name__=='__main__':
    main()
