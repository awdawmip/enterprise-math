"""Exact calibration and small cases for minimum in the three-tail readout H."""
from fractions import Fraction as Q
import json

from suffix_limits import all_gaps, block, interval_image


T = ((Q(1,15),Q(4,15),Q(2,3)),
     (Q(1,3),Q(1,3),Q(1,3)),
     (Q(32,45),Q(8,45),Q(1,9)))


def hilbert_ratio(k,gaps):
    c = k+1-gaps[0]
    endpoints = (Q(0),Q(1))
    for r,m in zip(range(k-1,0,-1),gaps[1:-1]):
        endpoints = interval_image(block(r,c,m),endpoints)
        c -= m
    weights = []
    for z in (Q(1,4),Q(1),Q(4)):
        mass=Q(1)
        for n in range(c,2,-1):
            mass*=n*z/(1+n*z)
        weights.append(mass)
    observations=[]
    for u in endpoints:
        # The row-normalization cancels in the range of the matched ratios.
        masses=[7*weights[0],u*weights[1],(1-u)*weights[2]]
        observations.append([sum(mass*row[j] for mass,row in zip(masses,T))
                             for j in range(3)])
    ratios=[x/y for x,y in zip(*observations)]
    return max(ratios)/min(ratios)


def main():
    # For A all final state vectors have exactly (7,u,1-u)/8.
    # Multiplying the three observation probabilities by 360 yields
    # (53-17u,92+7u,215+10u). The log-slope range multiplied by 8
    # is consequently bounded by 8*(17/36+7/92).
    assert all(sum(row)==1 for row in T)
    family_upper = 8*(Q(17,36)+Q(7,92))
    other_lower = Q(12,29)*14
    assert family_upper < Q(9,2) < other_lower
    small = {}
    for k in (2,3):
        ranked=sorted((hilbert_ratio(k,path),path) for path in all_gaps(k))
        assert ranked[0][1]==(1,)*(k-1)+(0,0)
        assert all(v>ranked[0][0] for v,_ in ranked[1:])
        small[k]=dict(count=len(ranked),minimum=str(ranked[0][0]),second=str(ranked[1][0]),
                      second_word=ranked[1][1])
    return dict(A_logH_over_TV_upper=str(family_upper),
                k_at_least_4_competitor_logH_over_A_TV_lower=str(other_lower),small_cases=small)


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
