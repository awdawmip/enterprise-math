#!/usr/bin/env python3
"""Exact rational matching inputs. SymPy isolates polynomial roots; verification
uses rational endpoint signs, distinct intervals and exact rational moments.
No trigonometric numerical input or thickness-road generation is used.
"""
from fractions import Fraction as F
from math import prod
from pathlib import Path
import json
import sympy as sp


def frac(x):
    return F(int(x.p), int(x.q))


def cheb_value(m, x):
    if m == 0:
        return F(1)
    u, v = F(1), x
    for _ in range(1, m):
        u, v = v, 2*x*v-u
    return v


def ln_interval(x, count=240):
    """atanh series, exact positive tail; adequate here for x=28/5."""
    z = (x-1)/(x+1)
    assert 0 < z < 1
    val = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(count)), F(0))
    tail = 2*z**(2*count+1)/(F(2*count+1)*(1-z*z))
    return val, val+tail


def one_family(m, theta=F(1, 2)):
    z = sp.Symbol('z')
    poly = sp.Poly(sp.chebyshevt(m, z), z)
    eps = sp.Rational(1, 256*m**3)
    brackets = [(frac(a), frac(b)) for ((a,b),mult) in poly.intervals(eps=eps)
                if mult == 1]
    assert len(brackets) == m
    q = 1
    while F(1,q) > theta/F(512*m**3):
        q *= 2
    nodes, root_intervals = [], []
    radius = theta/F(128*m**3)
    for low, high in brackets:
        assert -1 < low <= high < 1
        if low == high:
            assert cheb_value(m,low) == 0
        else:
            assert cheb_value(m,low)*cheb_value(m,high) < 0
        lo, hi = theta*(1+low)/2, theta*(1+high)/2
        mid = (lo+hi)/2
        node = F((mid*q).__floor__(),q)
        assert max(abs(node-lo),abs(node-hi)) <= radius
        nodes.append(node)
        root_intervals.append([str(low),str(high)])
    assert all(brackets[j][1] < brackets[j+1][0] for j in range(m-1))
    assert all(0 < a < theta for a in nodes)
    assert all(nodes[j] < nodes[j+1] for j in range(m-1))
    weights = [prod((b/(b-a) for i,b in enumerate(nodes) if i!=j),start=F(1))
               for j,a in enumerate(nodes)]
    moments = [sum((v*a**r for v,a in zip(weights,nodes)),F(0)) for r in range(m)]
    assert moments == [F(1)]+[F(0)]*(m-1)
    product = prod(nodes,start=F(1))
    tv = sum(map(abs,weights),F(0))
    assert product <= 4*(theta/4)**m
    assert tv < 4*m
    return {'m':m,'theta':str(theta),'root_z_intervals':root_intervals,
            'nodes':list(map(str,nodes)),'weights':list(map(str,weights)),
            'root_max_error_upper':str(radius),'node_grid_denominator':q,
            'product':str(product),'ideal_product':str(2*(theta/4)**m),
            'weight_total_variation':str(tv),'weight_total_variation_float':float(tv),
            'moments_exact':list(map(str,moments)),
            'max_weight_numerator_bits':max(v.numerator.bit_length() for v in weights),
            'max_weight_denominator_bits':max(v.denominator.bit_length() for v in weights)}


def main():
    rows=[one_family(m) for m in range(1,17)]
    lo,hi=ln_interval(F(28,5))
    beta_lo,beta_hi=F(7,10)*(lo-1),F(7,10)*(hi-1)
    assert beta_lo > F(1,2)
    # Reading decimals are directed by exact integer division, not binary floats.
    den=10**45
    beta=[str((beta_lo*den).__floor__())+'/'+str(den),
          str(-(-beta_hi*den).__floor__())+'/'+str(den)]
    result={'schema':'RH_RATIONAL_CHEB_MATCHING_ORDER_V1',
            'status':'AUTHOR_EXACT_FINITE_CHECKS_NOT_INDEPENDENT_REVIEW',
            'coverage':{'degrees':list(range(1,17)),
                        'exact_moment_checks':sum(range(1,17)),
                        'rational_nodes':sum(range(1,17))},
            'beta_0p7_interval':beta,
            'beta_0p7_strictly_exceeds_half':True,
            'families':rows}
    out=Path(__file__).with_name('matching_order_certificate.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'coverage':result['coverage'],
                      'beta_0p7_strictly_exceeds_half':True,
                      'largest_checked_tv':max(v['weight_total_variation_float'] for v in rows)}))


if __name__=='__main__':
    main()
