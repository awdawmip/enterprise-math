"""C67 exact all-inventory 02/20 separation certificate.

Cross products are evaluated without coefficient division, so reductions may
be used even at primes that divide an entry or a content factor.
"""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import isqrt, prod
from pathlib import Path
import json
import sys

BOUND=5000
PRIMES=(17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101)


def dual(r,c,m):
    k=2*r+1
    v=c-m
    a=prod(k+4*(c-j) for j in range(m+1))
    b=prod(k+c-j for j in range(m+1))
    e=(k-1+v)*prod(4*k+c-j for j in range(m+1))
    t=28*(k-1+4*v)*a*b
    return t,a*e,t,4**m*e*b


def multiply(u,v):
    a,b,h,d=u
    e,f,g,i=v
    return a*e+b*g,a*f+b*i,h*e+d*g,h*f+d*i


def coefficients(r,c):
    a,b,h,d=multiply(dual(r,c,0),dual(r-1,c,2))
    e,f,g,i=multiply(dual(r,c,2),dual(r-1,c-2,0))
    return a*g-e*h,a*i+b*g-e*d-f*h,b*i-f*d


def rho2_positive(r,c):
    k=2*r+1
    return prod(k+4*(c-j) for j in range(3))>16*prod(k+c-j for j in range(3))


def rational_pair_possible(r,c):
    if not rho2_positive(r,c):
        return False
    a,b,d=coefficients(r,c)
    if a==b==d==0:
        return True
    if a==0 or a*d<=0 or a*b>=0:
        return False
    disc=b*b-4*a*d
    return disc>0 and isqrt(disc)**2==disc


def finite(limit):
    """Bit j is set only if c=j can have a square discriminant at every tested prime."""
    tables=[]
    bits=4*limit+1
    for p in PRIMES:
        squares={i*i%p for i in range(p)}
        repeats=((1<<(p*((bits+p-1)//p)))-1)//((1<<p)-1)
        table=[]
        for r in range(p):
            row=0
            for c in range(p):
                a,b,d=coefficients(r,c)
                if (b*b-4*a*d)%p in squares:
                    row |= 1<<c
            table.append(row*repeats)
        tables.append((p,table))
    survivors=0
    checked=0
    for r in range(2,limit):
        lower,upper=2*r+1,4*r-1
        mask=((1<<(upper+1))-(1<<lower))
        checked+=upper-lower+1
        for p,table in tables: mask &= table[r%p]
        while mask:
            bit=mask & -mask
            c=bit.bit_length()-1
            mask-=bit
            survivors+=1
            assert not rational_pair_possible(r,c),(r,c)
    return dict(first_r=2,last_r=limit-1,total_middle_stocks=checked,primes=list(PRIMES),
                surviving_residue_sieve=survivors,possible_positive_rational_fixed_pairs=0)


def nonscalar():
    import sympy as sp
    r,c=sp.symbols('r c')
    a,_,d=coefficients(r,c)
    primitive=[]
    for polynomial in (a,d):
        linear=[]
        nonlinear=[]
        for factor,exponent in sp.factor_list(polynomial)[1]:
            poly=sp.Poly(factor,r,c)
            if poly.total_degree()==1:
                # All discarded affine factors are positive throughout r>=2,c>=4.
                assert factor.subs({r:2,c:4})>0
                assert poly.coeff_monomial(r)>=0 and poly.coeff_monomial(c)>=0
                linear.append(factor)
            else:
                assert exponent==1
                nonlinear.append(factor)
        assert len(nonlinear)==1 and linear
        primitive.append(nonlinear[0])
    res=sp.Poly(sp.resultant(*primitive,c),r).primitive()[1]
    shift=res.shift(2)
    if shift.LC()<0: shift=-shift
    assert all(value>0 for value in shift.all_coeffs())
    return dict(nonlinear_degrees=[sp.Poly(y,r,c).total_degree() for y in primitive],
                resultant_degree=res.degree(),positive_shifted_coefficients=len(shift.all_coeffs()),
                shifted_constant=str(shift.TC()))


def large():
    r=BOUND
    height=4*28**4*(32*r)**20
    assert 34**16>2**81 and Q(4*r,r-3)+1<Q(81,16)
    assert 32*r*height*Q(33,35)**(r-3)<1
    assert Q(33,35)*Q(r,r-21)<1
    return dict(first_r=r,common_reverse_edges_after_first=r-3,
                root_height_bound="4*28^4*(32*r)^20",diameter_bound="32*r*(33/35)^(r-3)")


def model_check(check_dir):
    sys.path.insert(0,str(check_dir.resolve()))
    from suffix_limits import block
    checks=0
    for r in range(1,11):
        for c in range(2,23):
            for m in (0,1,2):
                if c<m+2:continue
                _,b,h,d=block(r,c,m)
                t,v,_,u=dual(r,c,m)
                assert Q(t,u)==Q(b,d-b) and Q(v,u)==1+Q(h,d-b)
                checks+=1
    return checks


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--checks',type=Path,required=True)
    args=ap.parse_args()
    print(json.dumps(dict(inherited_block_checks=model_check(args.checks),nonscalar=nonscalar(),
                          large=large(),finite=finite(BOUND)),indent=2))
