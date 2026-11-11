"""Rigorous finite top-three and 63-pair cut certificate. Python standard library."""
import argparse
import json
from heapq import nsmallest
from math import comb, factorial

from edge_helpers import Q, edge_parameters, ordered_three, slope_range, standard_three, terminal_lower, word_tv


def next_layer(r, previous):
    next_bounds = {}
    for c in previous:
        candidates = []
        for m, tau, rho in edge_parameters(r, c):
            edge = tau*abs(rho-1)/(tau+max(1,rho))**2
            assert edge > 0
            candidates.extend((edge*cost, (m,)+path) for cost, path in previous[c-m])
        # Each first edge prefixes a disjoint set of paths, its weight is positive.
        # Four records suffice after excluding any three specified complete paths.
        next_bounds[c] = nsmallest(4, candidates)
    return next_bounds


def lower_outside(four, excluded):
    return min((cost for cost,path in four if path not in excluded), default=None)


def cut_certificate(layer):
    r = 63
    A, B, C = (p[1:] for p in standard_three(64))
    alo, U = slope_range(r,64,A)
    blo, bhi = slope_range(r,64,B)
    clo, chi = slope_range(r,64,C)
    other = lower_outside(layer[64], {A,B,C})
    assert U > 0 and alo > Q(99999,100000)*U
    assert U < blo <= bhi < clo <= chi < 24*alo
    assert blo > Q(1503122,100000)*U and bhi < Q(1503132,100000)*U
    assert clo > Q(2351969,100000)*U and chi < Q(2351984,100000)*U
    assert other > 177*U
    inventory = {}
    for c in range(65,70):
        surplus = c-r-1
        W = 16**(surplus-1)*Q(factorial(2*r+c+1),factorial(3*r+3))
        ratio = W*layer[c][0][0]/U
        assert ratio > 49508
        inventory[str(c)] = float(ratio)
    return {
        'cut_r':r, 'cut_c':64, 'slope_ranges_div_A_sup_display':{
            'A':[float(alo/U),1.0], 'B':[float(blo/U),float(bhi/U)],
            'C':[float(clo/U),float(chi/U)]},
        'other_lower_div_A_sup_display':float(other/U),
        'weighted_lower_div_A_sup_display':inventory,
        'exact_tests_passed':True,
    }


def certify():
    layer = {c:[(terminal_lower(c),(c-2,))] for c in range(2,70)}
    finite = []
    for k in range(2,65):
        layer = next_layer(k-1,layer)
        four = nsmallest(4, ((cost, (k+1-c,)+path)
                           for c in range(2,k+2) for cost,path in layer[c]))
        winners = ordered_three(k)
        a,b,c = (word_tv(k,path) for path in winners)
        other = lower_outside(four,winners)
        assert a < b < c
        if k == 2:
            assert other is None and len(four)==3
        else:
            assert other is not None and other > c
        if k >= 4:
            assert other > 28*a and c < 24*a
        finite.append({'k':k,'schedule_count':str(comb(2*k-1,k)),
                       'second_div_first_display':float(b/a),'third_div_first_display':float(c/a),
                       'other_lower_div_first_display':float(other/a) if other else None})
    return {'algorithm':'four smallest path lower bounds; all assertions use exact fractions',
            'finite_records':finite, 'number_of_schedules_covered':str(sum(int(row['schedule_count']) for row in finite)),
            'cut':cut_certificate(layer)}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='top64.json')
    args=parser.parse_args()
    result=certify()
    with open(args.output,'w') as file:
        json.dump(result,file,indent=2)
    print('Passed k=2..64 finite rank checks and r=63 cut checks.')
