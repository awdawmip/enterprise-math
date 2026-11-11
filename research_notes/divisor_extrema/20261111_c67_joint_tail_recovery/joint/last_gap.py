"""Rational certificates for decoding arbitrarily large stock at the last block."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import sys

# 32 times T_0j/T_2j and T_1j/T_2j.
A = (3, 48, 192)
B = (15, 60, 96)


def terminal(v, i, y):
    d = (v+2)*(v+3)*(v+4)
    return y*(840*A[i]+d*B[i])/(32*d+840*y*A[i])


def extremum(v):
    return 1 if v <= 3 else 2


def tau_max(v):
    return Q(28*(3+4*v)*(2+4*v), (12+v)*(2+v))


def tau_ratio(v):
    return Q(4*(v+11)*(4*v+2)*(v+1),(4*v-1)*(v+2)*(4*v-2))


def y_stock(v):
    y = Q(1)
    for n in range(3, v+1):
        y *= Q(4*n+1,4*n+4)
    return y


def exact_increment(v, y, tau):
    ratio = tau_ratio(v)
    yprev = y*Q(4*v+4,4*v+1)
    h,l = terminal(v,extremum(v),y),terminal(v,0,y)
    hp,lp = terminal(v-1,extremum(v-1),yprev),terminal(v-1,0,yprev)
    return ratio*(h-l)-(hp-lp)+tau*(h*lp-l*hp)


def homogeneous_term(v, i, n, d, s):
    """Y = t*n/d, return numerator divided by t and positive denominator."""
    scale = (v+2)*(v+3)*(v+4)
    return n*(840*A[i]+scale*B[i]), 32*scale*d+840*s*n*A[i]


def positivity_value(v, t, maximum):
    # Here y=t/(2+2t); every factor in the clearing denominator is positive.
    n,d=1,2+2*t
    h,dh=homogeneous_term(v,2,n,d,t)
    l,dl=homogeneous_term(v,0,n,d,t)
    hp,dhp=homogeneous_term(v-1,2,4*(v+1)*n,(4*v+1)*d,t)
    lp,dlp=homogeneous_term(v-1,0,4*(v+1)*n,(4*v+1)*d,t)
    rn,rd=4*(v+11)*(4*v+2)*(v+1), (4*v-1)*(v+2)*(4*v-2)
    nn,nd=(28*(3+4*v)*(2+4*v),(12+v)*(2+v)) if maximum else (0,1)
    return (rn*nd*(h*dl-l*dh)*dhp*dlp-rd*nd*(hp*dlp-lp*dhp)*dh*dl
            +nn*rd*t*(h*lp*dl*dhp-l*hp*dh*dlp))


def newton(values):
    out=[]
    while values:
        out.append(values[0])
        values=[b-a for a,b in zip(values,values[1:])]
    return out


def cubic_coeffs(f):
    a,b,c,d=newton([f(i) for i in range(4)])
    # coefficients times 6 in the monomial basis 1,t,t²,t³
    return [6*a,6*b-3*c+2*d,3*c-3*d,d]


def certify(maximum):
    degree=19 if maximum else 17
    rows=[cubic_coeffs(lambda t:positivity_value(16+i,t,maximum)) for i in range(degree+1)]
    coefficients=[newton([row[j] for row in rows]) for j in range(4)]
    assert all(a>=0 for col in coefficients for a in col) and coefficients[0][0]>0
    for x,t in ((0,3),(10,9),(30,11)):
        reconstructed=sum(a*comb(x,i)*t**j for j,col in enumerate(coefficients)
                          for i,a in enumerate(col))
        assert reconstructed==6*positivity_value(16+x,t,maximum)
        v=16+x;y=Q(t,2+2*t)
        assert exact_increment(v,y,tau_max(v) if maximum else 0)>0
    all_positive=[a for col in coefficients for a in col if a>0]
    return dict(maximum=maximum,x_degree=degree,t_degree=3,positive_coefficients=len(all_positive),
                minimum_positive=str(min(all_positive)))


def brute(model_dir):
    sys.path.insert(0,str(model_dir.resolve()))
    from suffix_limits import block
    from observed_four import tail_forms
    from functools import cache
    columns=cache(tail_forms)
    count=0
    direct=[]
    for c in range(2,73):
        jlist=[]
        for m in range(c-1):
            v=c-m
            a,b,e,d=block(1,c,m)
            slopes=[(p*a+t*e)/(p*b+t*d) for p,t in columns(v)]
            j=max(map(abs,slopes))/min(map(abs,slopes))
            t=Q(b,d-b)
            y=y_stock(v)
            modeled=(1+t*terminal(v,extremum(v),y))/(1+t*terminal(v,0,y))
            assert j==modeled
            jlist.append(j)
            count+=1
        assert all(a>b for a,b in zip(jlist,jlist[1:]))
        if c==5:
            direct=[str(x) for x in jlist]
    return dict(stocks_checked=[2,72],exact_three_column_cases=count,c5_J_at_m_0_through_3=direct)


def main(args):
    finite=[]
    for v in range(3,16):
        y=y_stock(v)
        bounds=[exact_increment(v,y,t) for t in (0,tau_max(v))]
        assert min(bounds)>0
        finite.append(dict(v=v,lower=str(min(bounds))))
    assert y_stock(16)<Q(1,2)
    data=dict(base_stocks=finite,large_stock_certificates=[certify(z) for z in (False,True)],
              adjacent_gap_precision_exponent='45/4',interior_v_power='19/2')
    if args.c64:
        data['native_matrix_check']=brute(args.c64)
    print(json.dumps(data,indent=2))


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--c64',type=Path)
    main(p.parse_args())
