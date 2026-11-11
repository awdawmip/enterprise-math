"""Additional finite-rank and cutoff certificates for fourth place in the C62 family."""
import argparse
from heapq import nsmallest
import json
from math import factorial
from edge_helpers import Q, edge_parameters, ordered_three, slope_range, standard_three, terminal_lower, word_tv


def front_pair(k):
    return (2,0)+(1,)*(k-3)+(0,0)


def terminal_pair(k):
    return (1,)*(k-3)+(0,0,2,0)


def next_six(r, previous):
    next_bounds = {}
    for c in previous:
        options = []
        for m,tau,rho in edge_parameters(r,c):
            L = tau*abs(rho-1)/(tau+max(1,rho))**2
            assert L>0
            options.extend((L*cost,(m,)+path) for cost,path in previous[c-m])
        next_bounds[c] = nsmallest(6,options)
    return next_bounds


def cut(layer):
    r = 63
    A,B,C = (path[1:] for path in standard_three(64))
    D = terminal_pair(64)[1:]
    alo,U = slope_range(r,64,A)
    _,chi = slope_range(r,64,C)
    dlo,dhi = slope_range(r,64,D)
    outside = min(z for z,p in layer[64] if p not in {A,B,C,D})
    assert chi < dlo <= dhi < 185*alo
    assert dlo > Q(184016,1000)*U and dhi < Q(184018,1000)*U
    assert outside > 344*U
    inventory = {}
    for c in [63]+list(range(65,73)):
        s=c-r-1
        W=Q(16)**s if s<=0 else 16**(s-1)*Q(factorial(2*r+c+1),factorial(3*r+3))
        ratio = W*layer[c][0][0]/U
        assert ratio > (601 if c==63 else 49508)
        inventory[c] = float(ratio)
    return {'D_slope_div_supA_display':[float(dlo/U),float(dhi/U)],
            'other_suffix_lower_div_supA_display':float(outside/U),
            'weighted_cut_lower_div_supA_display':inventory}


def run():
    layer = {c:[(terminal_lower(c),(c-2,))] for c in range(2,73)}
    rows=[]
    for k in range(2,65):
        layer=next_six(k-1,layer)
        if k==2:
            assert sum(len(layer[c]) for c in range(2,4))==3
            continue
        triple=ordered_three(k)
        E,D=front_pair(k),terminal_pair(k)
        winner=E if k<=9 else D
        candidates=set(triple)|{E,D}
        six=nsmallest(6,((z,(k+1-c,)+p) for c in range(2,k+2) for z,p in layer[c]))
        other=min(z for z,p in six if p not in candidates)
        actual={p:word_tv(k,p) for p in candidates}
        A=actual[triple[0]]
        assert actual[triple[0]]<actual[triple[1]]<actual[triple[2]]<actual[winner]<other
        challenger=(D if winner==E else E)
        if challenger not in triple:
            assert actual[winner]<actual[challenger]
        if k>=10:
            assert actual[D]<185*A
        rows.append({'k':k,'winner':'front_pair' if winner==E else 'terminal_pair',
                     'front_div_first_display':float(actual[E]/A),
                     'terminal_div_first_display':float(actual[D]/A),
                     'remaining_lower_div_first_display':float(other/A)})
    return {'proof':'positive edge weights, six least pathwise bounds, exact comparison of five named candidates',
            'k2_family_size':3,'finite_records':rows,'cut':cut(layer),'exact_tests_passed':True}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='rank_four.json')
    args=p.parse_args()
    evidence=run()
    with open(args.output,'w') as file:json.dump(evidence,file,indent=2)
    print('Certified finite fourth-place ranks and r=63 gluing inequalities.')
