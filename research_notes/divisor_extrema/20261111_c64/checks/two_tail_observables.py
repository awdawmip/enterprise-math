"""C64: complete two-tail identification and exact switching rule for H.

All arithmetic and all ordering checks are exact. Requires the adjacent C64
suffix_limits.py and observable_minimum.py for the three-state C62 kernel.
"""
from fractions import Fraction as Q
from itertools import combinations
import json

from suffix_limits import all_gaps, block, interval_image
from observable_minimum import T


TAILS=("557","575","755")
PAIRS=tuple(combinations(range(3),2))


def tail_weights(length):
    weights=[]
    for z in (Q(1,4),Q(1),Q(4)):
        w=Q(1)
        for n in range(3,length+3):
            w*=n*z/(1+n*z)
        weights.append(w)
    return weights


def pair_readouts(k,gaps):
    c=k+1-gaps[0]
    endpoints=(Q(0),Q(1))
    for r,m in zip(range(k-1,0,-1),gaps[1:-1]):
        endpoints=interval_image(block(r,c,m),endpoints)
        c-=m
    assert c-2==gaps[-1]
    a,b,h=tail_weights(gaps[-1])
    obs=[]
    for u in endpoints:
        state_weights=(7*a,u*b,(1-u)*h)
        obs.append([sum(w*T[i][j] for i,w in enumerate(state_weights)) for j in range(3)])
    ratios=[x/y for x,y in zip(*obs)]
    stats=tuple(max(ratios[i],ratios[j])/min(ratios[i],ratios[j]) for i,j in PAIRS)
    return stats,max(ratios)/min(ratios)


def endpoint_slope(length):
    """Signed d log(p575/p755)/dTV at u=1 with orientation pi2 decreasing."""
    zero,one,two=tail_weights(length)
    x=7*zero/one
    t=one/two
    assert x==Q(840,(length+4)*(length+5)*(length+6))
    return (x+1)*(6*t*x-4*x-1)/((2*x+1)*(4*x+5))


def main():
    basic=[endpoint_slope(length) for length in range(3)]
    sharp=Q(287,11520)
    assert basic==[Q(104,495),Q(25,378),-sharp]
    # For every length >=3, t<=1547/2560<2/3 and x<=5/3.
    # Thus -signed slope >= (x+1)/[(2x+1)(4x+5)], decreasing in x>=0:
    # derivative numerator = -(8*x*x+16*x+9). At x=5/3 it equals 24/455.
    assert tail_weights(3)[1]/tail_weights(3)[2]==Q(1547,2560)<Q(2,3)
    assert Q(24,455)>sharp
    a_upper=8*(Q(7,92)-Q(2,43))
    assert a_upper==Q(234,989)<14*sharp
    full_upper=Q(908,207)
    assert min(Q(17,32)+Q(4,15),Q(17,32)+Q(10,30))*14>full_upper
    cases={}
    count=0
    for k in range(2,7):
        stats=[]
        for gaps in all_gaps(k):
            hs,H=pair_readouts(k,gaps)
            index=0 if gaps[-1]<=1 else 1
            assert H==hs[index] and all(h<H for j,h in enumerate(hs) if j!=index)
            stats.append((gaps,hs))
            count+=1
        table=[]
        for j,(i0,i1) in enumerate(PAIRS):
            ranked=sorted((hs[j],g) for g,hs in stats)
            a=(1,)*(k-1)+(0,0)
            expected=(0,0,1) if (k,j)==(2,2) else a
            assert ranked[0][1]==expected and ranked[0][0]<ranked[1][0]
            if k<=3:
                table.append(dict(pair=[TAILS[i0],TAILS[i1]],minimum=str(ranked[0][0]),
                                  minimizer=ranked[0][1],second=str(ranked[1][0]),second_path=ranked[1][1],
                                  A_statistic=str(next(hs[j] for g,hs in stats if g==a))))
        if table:
            cases[k]=table
    return dict(status="PASS",full_vs_pair_exact_complete_checks=count,k_checked=[2,6],
                full_H_rule={"last_gap_0_or_1":["557","575"],"last_gap_at_least_2":["557","755"]},
                weak_pair=["575","755"],sharp_absolute_TV_slope_lower=str(sharp),
                A_weak_pair_log_slope_upper=str(a_upper),edge_cases=cases)


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
