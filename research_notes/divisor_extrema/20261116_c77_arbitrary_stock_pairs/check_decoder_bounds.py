"""Integer checks on the analytic bound and orientation-free two-jet inversion."""
from fractions import Fraction as Q
from itertools import product
from math import prod
import json


def main():
    cutoffs = 0
    cases = 0
    for M, gap in product((100,101,113,325,1000,10000),(0,1,300,2791)):
        C = 300*M+gap
        P = prod(range(C+6,C+21))
        p = (P-1).bit_length()
        q,T = p+62*M, 5*p+354*M+3
        N = 3*C-3-(C+5).bit_count()
        assert N-q >2*T+2
        cutoffs += 1

    for A,L,H,P,s in product((Q(183,43),Q(117,90)),(Q(49,16),Q(5,318)),
                               (Q(4,975),Q(48,5)),(101,32),(Q(2**32,9),Q(2**51,357))):
        P=Q(P)
        h,ell = P/(A*H),P/(A*L)
        R=(P+H)/(P+L)*(s*P+A*L)/(s*P+A*H)
        r0=(P+H)/(P+L)*L/H
        r1=r0*(ell-h)
        r2=-r1*h
        assert (R-r0)/s == r1/(1+s*h)
        assert ((R-r0)/s-r1)/s == r2/(1+s*h)
        phi = -r2/r1
        e = phi+r1/r0
        K=r0*e/phi
        recovered=(1/phi-K/e)/(K-1)
        assert (recovered,P/(recovered*phi),P/(recovered*e)) == (A,H,L)
        cases+=1
    return dict(height_valuation_certificates=cutoffs, orientation_agnostic_inversions=cases)


if __name__=='__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
