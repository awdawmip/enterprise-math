"""Independent native two-block readout simulation and far-stock inversion."""
from fractions import Fraction as Q
from functools import lru_cache
from math import prod
import json

from far_decoder import NotCertified, _reconstruct, decode


@lru_cache(maxsize=8)
def _stock_chain(n):
    # Independent step data; product of integer subranges then reduce.
    def span(lo, hi):
        if hi-lo <= 32:
            return Q(prod(4*j+5 for j in range(lo,hi)),
                     prod(4*j+20 for j in range(lo,hi)))
        mid = (lo+hi)//2
        return span(lo,mid)*span(mid,hi)
    return span(2,n+1)


def _native(n,v,w):
    y=Q(1)
    for j in range(3,w+1):
        y *= Q(4*j+1,4*j+4)
    x=Q(840,(w+2)*(w+3)*(w+4))
    ends = [y*(x*a+b)/(1+x*y*a) for a,b in
            ((Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3)))]
    for outer,landing,k in ((v,w,3),(n,v,5)):
        if k == 3:
            rho=4*Q(prod(4*j+k for j in range(landing,outer+1)),
                    prod(4*j+4*k for j in range(landing,outer+1)))
        else:
            rho=4*_stock_chain(outer)/_stock_chain(landing-1)
        tau = rho*Q(28*(k-1+4*landing),k-1+landing)
        for i in range(3*k):
            tau *= Q(landing+k+i,outer+k+1+i)
        ends = [(rho+tau*z)/(1+tau*z) for z in ends]
    return max(ends)/min(ends)


def check():
    reconstruction_count=0
    for sign in (-1,1):
        for a in range(1,38):
            for b in range(1,38):
                exact=Q(sign*a,b)
                observed=exact+Q(3*2**36,7)
                assert _reconstruct(observed,6,35)==exact
                reconstruction_count+=1
    cases = []
    for c,n,templates in ((6,12000,[(v,w) for v in range(2,7) for w in range(2,v+1)]),
                          (100,11500,[(92,59)]),
                          (100,30000,[(2,2),(3,3),(73,3),(92,59),(100,100)])):
        heights=[]
        for v,w in templates:
            observed=_native(n,v,w)
            certificate={}
            assert decode(c,n,observed,certificate=certificate)==(v,w)
            assert certificate['outer_stock']==n
            heights.append(max(observed.numerator.bit_length(),observed.denominator.bit_length()))
        cases.append(dict(original=c,outer=n,templates=len(templates),
                          maximum_readout_bits=max(heights),
                          uniform_120_applies=certificate["uniform_120_applies"]))
    try:
        decode(6,7,_native(7,6,2))
    except NotCertified:
        pass
    else:
        raise AssertionError("unexpected uncertified recovery")
    return dict(cases=cases, native_roundtrips=sum(row['templates'] for row in cases),
                signed_lift_checks=reconstruction_count, inadequate_precision_rejected=True)


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
