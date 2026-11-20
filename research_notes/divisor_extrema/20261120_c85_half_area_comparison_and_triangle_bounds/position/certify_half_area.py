"""Exact rational certificate for C85's half-area position comparison.

All signs are decided using fractions. Decimal displays are outward intervals.
The analytical input and all remainder proofs are in HALF_AREA_COMPARISON.md.
No Monte Carlo or floating-point quadrature is used here.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def log_ratio_bounds(z, terms=96):
    """Bounds log((1+z)/(1-z)), 0<z<1, by the positive atanh series."""
    assert 0 < z < 1
    lo = 2*sum((z**(2*n+1)/F(2*n+1) for n in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo, lo+tail


def atan_bounds(z, terms=48):
    """Alternating-series bounds for arctan(z), 0<z<1."""
    partial = sum(((-1)**n*z**(2*n+1)/F(2*n+1)
                   for n in range(terms)), F(0))
    nextterm = (-1)**terms*z**(2*terms+1)/F(2*terms+1)
    return min(partial,partial+nextterm),max(partial,partial+nextterm)


def root_fraction_bounds(power, denominator, decimal_digits=40):
    """Enclose denominator^(-1/power) by adjacent decimal rationals."""
    scale = 10**decimal_digits
    target = scale**power//denominator
    lo,hi = 0,scale+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**power<=target:lo=mid
        else:hi=mid
    a,b=F(lo,scale),F(hi,scale)
    assert a**power<=F(1,denominator)<b**power
    return a,b


def K_bounds(terms=96):
    blo,bhi = root_fraction_bounds(2,2)
    def term(b,n):
        return 48*b**(n+7)/F((n+3)*(n+5)*(n+7))
    lo=sum((term(blo,n) for n in range(terms)),F(0))
    hi=sum((term(bhi,n) for n in range(terms)),F(0))
    hi+=term(bhi,terms)/(1-bhi)
    return lo,hi


def decimal_bound(x,digits,up):
    scale=10**digits
    n=x.numerator*scale//x.denominator
    if up and F(n,scale)<x:n+=1
    sign='-' if n<0 else ''
    whole,part=divmod(abs(n),scale)
    return f'{sign}{whole}.{part:0{digits}d}'


def encoded(lo,hi,digits=18):
    assert lo<=hi
    # Compress only the output endpoints, rounding outwards to 160 binary bits.
    # The sign tests above use the full exact fractions.
    scale=1<<160
    lo=F(lo.numerator*scale//lo.denominator,scale)
    hi=F(-((-hi.numerator*scale)//hi.denominator),scale)
    return {'lower':{'numerator':str(lo.numerator),'denominator':str(lo.denominator)},
            'upper':{'numerator':str(hi.numerator),'denominator':str(hi.denominator)},
            'outward_decimal':[decimal_bound(lo,digits,False),
                               decimal_bound(hi,digits,True)]}


def main():
    kl,ku=K_bounds()
    l3,u3=log_ratio_bounds(F(1,2))
    l2,u2=log_ratio_bounds(F(1,3))
    ql,qu=(3*l3-2)/4,(3*u3-2)/4
    cl,cu=ql*kl,qu*ku
    d=F(7,270)
    gaplo,gaphi=d-cu,d-cl
    q5lo,q5hi=F(8,5)*l2-F(3,5),F(8,5)*u2-F(3,5)
    range_lo=F(77,192)-F(100,9)*ku*q5hi
    range_hi=F(77,192)-F(100,9)*kl*q5lo
    assert ku<F(69129,1000000)
    assert cu<F(22395,1000000)<d
    assert gaplo>F(3531,1000000)
    assert range_lo>F(10053,1000000)

    # K(a)<=8(1-a)^3 K(1/2), a in[1/2,1].
    # z=2^(-1/20), P=integral_.5^1 (1-a)^3 a^(-39/20) da = H0+H1*z.
    zl,zu=root_fraction_bounds(20,2)
    H0=-F(20,19)-60+F(20,7)-F(20,41)
    H1=F(40,19)+60-F(10,7)+F(5,41)
    pl,pu=H0+H1*zl,H0+H1*zu
    assert 0<pl<pu
    a5l,a5u=atan_bounds(F(1,5));a239l,a239u=atan_bounds(F(1,239))
    pil,piu=16*a5l-4*a239u,16*a5u-4*a239l
    zetal,zetau=pil*pil/6,piu*piu/6
    numerator_lo=2*d*zl/19-F(2,5)*cu*pu
    numerator_hi=2*d*zu/19-F(2,5)*cl*pl
    tail_lo,tail_hi=numerator_lo/zetau,numerator_hi/zetal
    assert tail_lo>F(1361,1000000)
    result={'status':'proved_with_exact_rational_bounds',
            'arithmetic':'fractions.Fraction; positive series geometric tails; alternating atan tails; certificate endpoints outward to 160 binary fractional bits',
            'series_terms':{'K':96,'log':96,'atan':48},
            'K_half':encoded(kl,ku),'Q_quarter':encoded(ql,qu),
            'QK_half':encoded(cl,cu),'quarter_gap_numerator':encoded(gaplo,gaphi),
            'uniform_position_range_bracket':encoded(range_lo,range_hi),
            'weighted_high_area_gap_lower_formula':encoded(tail_lo,tail_hi),
            'interpretation':{'weighted_gap':'(1/20) integral_.5^infty (F_quarter-F_mid) a^(-19/20) da is at least the displayed lower formula',
                              'global_sufficient_condition':'(1/20) integral_0^.5 (F_mid-F_quarter) a^(-19/20) da < 1361/1000000'},
            'strict_tests':['QK_half < 22395/1000000 < 7/270',
                            'quarter gap numerator > 3531/1000000',
                            'uniform position range bracket > 10053/1000000',
                            'weighted high area gap lower formula > 1361/1000000']}
    out=Path(__file__).with_name('half_area_certificate.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v.get('outward_decimal') for k,v in result.items()
                      if isinstance(v,dict) and 'outward_decimal' in v},indent=2))


if __name__=='__main__':main()
