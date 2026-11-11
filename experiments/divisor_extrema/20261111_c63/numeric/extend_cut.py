"""Verify r=63 for all stock c>=97 and the unrestricted large-stock tail.

Run after certify_schedules.py 100 --cut-output cut63_full.json.
All dyadic rounding is downwards. No floating-point operations are used.
"""
from fractions import Fraction
from itertools import islice
import json
from math import factorial
from pathlib import Path

from certify_schedules import block_maps, derivative_lower, terminal_lower

ROOT = Path(__file__).resolve().parent


def floor_log2(value):
    """Largest integer e with 2^e<=value for positive Rational value."""
    a,b = value.as_integer_ratio()
    e = a.bit_length()-b.bit_length()
    return e - ((a < (b << e)) if e>=0 else ((a << -e)<b))


def dyadic(e):
    return Fraction(2**e,1) if e>=0 else Fraction(1,2**(-e))


def run():
    cut=json.loads((ROOT/'cut63_full.json').read_text())
    r0=63
    sup=Fraction(*map(int,cut['ahead_derivative_sup']))
    coarse=(Fraction(2,460)**r0 * factorial(r0+1) /
            (16**(r0+2)*factorial(3*r0+3)*sup))
    threshold=r0+2
    while coarse*4**threshold<=2:
        threshold+=1
    maxstock=threshold-1
    # For c<=96, cut63_full.json is sharper and includes the noncanonical case.
    data=[None,None]+[floor_log2(terminal_lower(c)) for c in range(2,maxstock+1)]
    exact_m=12
    for r in range(1,r0+1):
        layer=[None,None]
        for c in range(2,maxstock+1):
            exact_bounds=[floor_log2(derivative_lower(mobius)) for mobius in
                          islice(block_maps(r,c),exact_m+1)]
            best=min(exp+data[c-m] for m,exp in enumerate(exact_bounds))
            n=2*r+c+1
            rho_numer=1
            rho_denom=1
            for m in range(c-1):
                rho_numer*=2*r+1+4*(c-m)
                rho_denom*=(n-m)*(4 if m else 1)
                if m<=exact_m:
                    continue
                if 10*abs(rho_numer-rho_denom)>=rho_denom:
                    # L >= (1/25)16^(-m) > 2^(-5-4*m).
                    e=-5-4*m
                else:
                    # Near resonance tau/(tau+M)^2 ≥ 1/460.
                    a=abs(rho_numer-rho_denom)
                    b=460*rho_denom
                    e=a.bit_length()-b.bit_length()
                    below_power = a < (b << e) if e>=0 else (a << -e) < b
                    if below_power:
                        e-=1
                best=min(best,e+data[c-m])
            layer.append(best)
        data=layer
    ratios=[]
    for c in range(97,threshold):
        weight=Fraction(16**(c-r0-2)*factorial(2*r0+c+1),factorial(3*r0+3))
        ratios.append((dyadic(data[c])*weight/sup,c))
    minimum, argmin=min(ratios)
    assert minimum>2
    return dict(r=r0, finite_start=97, finite_end=maxstock, exact_m=exact_m,
                finite_min_at=argmin, finite_min_ratio_floor=minimum//1,
                terminal_dyadic_slope_exponents=data[97:],
                large_stock_start=threshold,
                large_stock_ratio_at_start=[str(x) for x in (coarse*4**threshold).as_integer_ratio()],
                rational_canonical_sup=[str(sup.numerator),str(sup.denominator)])


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
