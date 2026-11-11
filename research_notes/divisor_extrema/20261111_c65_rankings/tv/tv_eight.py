"""Exact rank and threshold certificates for the first eight TV schedules.

Designed for Python 3.10+. Pass the directory containing C64's
finite_certificate.py and suffix_limits.py and C63's certify_schedules.py.
"""
import argparse
import json
import sys
from fractions import Fraction as Q
from heapq import nsmallest
from math import comb
from pathlib import Path


def compressed(path):
    first = 0
    while first < len(path) and path[first] == 1:
        first += 1
    return {"leading_ones": first, "remainder": list(path[first:])}


def solve(model, utilities, endpoints):
    depth, cut = 15, 63
    stock_range = range(2, 66)
    data = {c: [(model.terminal_lower(c), (c-2,))] for c in stock_range}
    exact = lambda p: utilities.map_bounds(utilities.schedule_matrix(p, model))[1]
    decimal = lambda lower, upper: endpoints.enclose_decimals((lower, upper), 10)
    suffixes = ["00", "010", "001", "0020", "0110", "0101", "0011", "0002"]

    def normal(k, suffix):
        return (1,) * (k+1-len(suffix)) + tuple(map(int, suffix))

    def fifth(k):
        if k==3: return (1,0,1,0)
        if k==4: return (0,1,0,2,0)
        if k<=9: return normal(k,"0020")
        if k<=12: return (2,0)+(1,)*(k-3)+(0,0)
        return normal(k,"0110")

    rows = []
    for r in range(1,cut+1):
        current = {}
        for c in stock_range:
            candidates = []
            for m, step in enumerate(model.block_maps(r,c)):
                edge = model.derivative_lower(step)
                candidates.extend((edge*value, (m,)+path) for value,path in data[c-m])
            current[c] = nsmallest(depth,candidates)
        data = current
        k = r+1
        total = comb(2*k-1,k)
        first_bounds = nsmallest(depth,((value,(k+1-c,)+sub)
                                 for c in range(2,k+2) for value,sub in data[c]))
        complete = len(first_bounds) == total
        unseen_bound = first_bounds[-1][0]
        ranked = sorted((exact(path),path) for _,path in first_bounds)
        qualified = ranked[:min(8,total)]
        assert all(x[0]<y[0] for x,y in zip(qualified,qualified[1:]))
        if len(ranked)>len(qualified):
            assert qualified[-1][0] < ranked[len(qualified)][0]
        if not complete:
            assert qualified[-1][0] < unseen_bound
        best = qualified[0][0]
        if k>=3:
            assert qualified[4][1] == fifth(k)
        if k>=20:
            assert [p for _,p in qualified] == [normal(k,s) for s in suffixes]
        if k==19:
            assert [p for _,p in qualified] != [normal(k,s) for s in suffixes]
        if not complete and unseen_bound<=1000*best:
            # The only uncovered small stock is cheap to enumerate directly.
            assert k==4
            all_exact = [(exact(p),p) for p in endpoints.all_gaps(k)]
            assert len(all_exact)==total
            assert sorted(all_exact)[:8]==qualified
            in_ball = [p for v,p in all_exact if v<=1000*best]
        else:
            in_ball = [p for v,p in ranked if v<=1000*best]
        if k>=21:
            assert len(in_ball)==8 and set(in_ball)=={p for _,p in qualified}
        if k==20:
            assert len(in_ball)==9
        rows.append(dict(k=k, ranked=[compressed(p) for _,p in qualified],
                         TV_over_A=[decimal(v/best,v/best) for v,_ in qualified],
                         unseen_bound_over_A=None if complete else decimal(unseen_bound/best,unseen_bound/best),
                         schedules_within_1000=len(in_ball)))

    window=data[64]
    exact_bounds = []
    for _,path in window:
        mat=utilities.schedule_matrix(path,model,True,64)
        lo,_,hi=utilities.map_bounds(mat)
        exact_bounds.append((lo,hi,path))
    exact_bounds.sort()
    qualified=exact_bounds[:8]
    expected=[normal(64,s)[1:] for s in suffixes]
    assert [p for _,_,p in qualified]==expected
    assert all(hi<next_lo for (_,hi,_),(next_lo,_,_) in zip(qualified,qualified[1:]))
    unseen=window[-1][0]
    outside=min(unseen,*(lo for lo,hi,p in exact_bounds[8:]))
    ref_lo,ref_hi,_=qualified[0]
    assert qualified[-1][1]<1000*ref_lo
    assert outside>2600*ref_hi

    # A short terminal matrix for each eventual competitor gives a common
    # input coordinate and certified limiting ratios using a nested interval.
    A3 = normal(4,"00")[1:]
    def transform(path):
        return utilities.schedule_matrix(path,model,True,4)
    ref=transform(A3)
    interval=(Q(0),Q(1))
    prefix=(1,0,0,1)
    for k in range(5,21):
        prefix=utilities.compose(prefix,endpoints.block(k-1,k,1))
        new=endpoints.interval_image(prefix,(Q(0),Q(1)))
        assert interval[0]<=new[0]<new[1]<=interval[1]
        interval=new
    limits={}
    for suffix in suffixes:
        mat=transform(normal(4,suffix)[1:])
        ratio=sorted(endpoints.derivative_ratio(mat,ref,z) for z in interval)
        limits[suffix]=endpoints.enclose_decimals(ratio,35)

    return dict(finite=rows,cut=dict(r=63,c=64,cut_paths=[compressed(p) for _,_,p in qualified],
                 ratio_enclosures=[decimal(lo/ref_hi,hi/ref_lo) for lo,hi,_ in qualified],
                 outside_over_A_sup_lower=decimal(outside/ref_hi,outside/ref_hi),
                 external_high_prefix_exclusion_over_A=1000),
                 limiting_ratios=limits, arithmetic="exact Fractions, displayed intervals rounded outwards")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c64",type=Path,required=True)
    parser.add_argument("--model",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    sys.path.insert(0,str(args.c64.resolve()))
    import finite_certificate as utilities
    import suffix_limits as endpoints
    certificate=solve(utilities.read_model(args.model),utilities,endpoints)
    args.output.write_text(json.dumps(certificate,indent=2)+"\n")
    print("Exact finite cases:",len(certificate['finite']))
    print("Arbitrary-input cut:",certificate['cut'])
