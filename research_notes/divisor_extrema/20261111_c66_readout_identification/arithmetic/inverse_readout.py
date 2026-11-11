"""Exact inverse fiber for a specified rational three-tail readout, all scales."""
import argparse
from fractions import Fraction as F
from math import isqrt, comb
from pathlib import Path
import json
import sys


def finite_ceiling(h):
    """Every word with this H has k <= the returned integer."""
    assert h>1
    p,d=h.numerator,h.denominator
    t=1
    while 3**(t-1)*(p-d)<=2*(2*t+1)*p:
        t+=1
    return 2*t-1


def block_factors(r,c):
    K=2*r+1
    rho=F(K+4*c,K+c)
    for m in range(c-1):
        u,v=rho.numerator,rho.denominator
        # Infinitesimal Hilbert contraction of the block; lower round only
        # its square root, retaining a rigorous rational upper factor.
        scale=2**12
        root=isqrt(scale*scale*u*v)
        contraction=F(scale*abs(u-v),scale*(u+v)+2*root)
        first=min(F(2*max(1,m)),abs(rho-1)/min(F(1),rho))
        yield m,first,contraction
        if m<c-2:
            n=c-m-1
            rho*=F(K+4*n,4*(K+n))


def upper_log_spreads(ceiling):
    # At terminal stock the normalized columns are a Hilbert nonexpansive
    # stochastic map. Hidden reweighting is projectively isometric.
    stocks=range(2,ceiling+2)
    previous={c:F(1) for c in stocks}
    values={}
    for r in range(1,ceiling):
        current={}
        k=r+1
        spread_bound=F(0)
        for c in stocks:
            factors=list(block_factors(r,c))
            current[c]=max(f*previous[c-m] for m,_,f in factors)
            if c<=k+1:
                spread_bound=max(spread_bound,*(initial*previous[c-m] for m,initial,_ in factors))
        values[k]=spread_bound
        previous=current
    return values


def run(h,all_gaps,hilbert_ratio):
    if h<=1:
        return dict(H=str(h),preimages=[],reason='Every feasible schedule has H strictly greater than one.')
    ceiling=finite_ceiling(h)
    bounds=upper_log_spreads(ceiling)
    log_lower=(h-1)/h
    candidates=[k for k,upper in bounds.items() if upper>=log_lower]
    matches=[]
    larger=[]
    for k in candidates:
        for path in all_gaps(k):
            actual=hilbert_ratio(k,path)
            if actual==h:
                matches.append(dict(k=k,gaps=path))
            elif actual>h:
                larger.append(dict(k=k,gaps=path,H=str(actual)))
    return dict(H=str(h),all_scale_ceiling=ceiling,candidate_sizes=candidates,
                exact_schedules_compared=sum(comb(2*k-1,k) for k in candidates),preimages=matches,larger=larger)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--H',type=F)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    sys.path.insert(0,str(args.model.resolve()))
    from suffix_limits import all_gaps
    from observable_minimum import hilbert_ratio
    hs=[args.H] if args.H is not None else [hilbert_ratio(2,x) for x in all_gaps(2)]+[F(17,16)]
    rows=[run(h,all_gaps,hilbert_ratio) for h in hs]
    result=dict(inverses=rows)
    if args.H is None:
        # All 48 measured values on k<=4, compared with every larger k.
        little=[hilbert_ratio(k,path) for k in range(2,5) for path in all_gaps(k)]
        threshold=min(little)
        ceiling=finite_ceiling(threshold)
        bounds=upper_log_spreads(ceiling)
        outside=max(bounds[k] for k in range(17,ceiling+1))
        assert outside<(threshold-1)/threshold
        assert len(little)==48 and len(set(little))==48
        result['unrestricted_decoding_k_through_4']=dict(
            smallest_H=str(threshold),small_schedules=len(little),all_scale_ceiling=ceiling,
            minimum_log_H_lower=str((threshold-1)/threshold),max_outside_modular_census_upper=str(outside),
            outside_maximizer=[k for k in range(17,ceiling+1) if bounds[k]==outside],
            in_range_proof='joint finite-field no-duplicates certificate, all 405187824 full arrangements k=2..16')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
