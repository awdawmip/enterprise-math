"""Finite rational phase average, preserving all dependent competitors.

Input coordinates are already divided by the output grid width.
The exact formula is an inclusion-exclusion sum over all nonempty
cliques of the possible-collision graph, not a Poisson approximation.
"""

from fractions import Fraction as Q
from collections import Counter
from math import prod
from pathlib import Path
from argparse import ArgumentParser
import hashlib
import json

from all_origins_compare import load_kernel, origin_states


def phase_mean(values):
    n=len(values)
    d=len(values[0])
    assert n>0 and all(len(v)==d for v in values)
    adjacent=[{j for j in range(n) if i!=j and
               all(abs(a-b)<1 for a,b in zip(values[i],values[j]))}
              for i in range(n)]
    total=Q(0)
    terms=Counter()

    def visit(size,allowed,lo=None,hi=None):
        nonlocal total
        for i in sorted(allowed):
            lower=tuple(min(a,b) for a,b in zip(lo,values[i])) if lo is not None else values[i]
            upper=tuple(max(a,b) for a,b in zip(hi,values[i])) if hi is not None else values[i]
            volume=prod((1-b+a for a,b in zip(lower,upper)),start=Q(1))
            assert volume>0
            total+=(-1)**size*Q(size+1,n)*volume
            terms[size+1]+=1
            visit(size+1,{j for j in allowed & adjacent[i] if j>i},lower,upper)

    visit(0,set(range(n)))
    assert 0<=total<=1
    return total,dict(sorted(terms.items()))


def stability_bound(x,y):
    assert len(x)==len(y) and len(x)>0
    row_bounds=[]
    for a,b in zip(x,y):
        assert len(a)==len(b)
        no_change=prod((1-min(Q(1),abs(s-t)) for s,t in zip(a,b)),start=Q(1))
        row_bounds.append(1-no_change)
    return min(Q(1),Q(2,len(x))*sum(row_bounds))


def floorq(x):
    return x.numerator//x.denominator


def decimal_interval(q,places=12):
    scale=10**places
    lo=floorq(q*scale)
    hi=-floorq(-q*scale)
    return {"lower":str(Q(lo,scale)),"upper":str(Q(hi,scale)),
            "decimal_places":places}


def dyadic_partition_mean(designs,denominator):
    """Independent positive-volume sweep, used on the dyadic compilation."""
    rows=list(designs.values())
    n=len(rows[0])
    assert all([r[0] for r in points]==[r[0] for r in rows[0]] and
               [r[2] for r in points]==[r[2] for r in rows[0]] for points in rows)
    s0=origin_states([[r[0] for r in rows[0]]],0)
    sm=origin_states([[r[1] for r in points] for points in rows],0)
    s2=origin_states([[r[2] for r in rows[0]]],0)
    weighted=[0]*len(rows)
    total_volume=0
    for a0,b0,c0 in s0:
        for am,bm,cm in sm:
            for a2,b2,c2 in s2:
                volume=Q(denominator)**3*(b0-a0)*(bm-am)*(b2-a2)
                assert volume.denominator==1
                volume=int(volume)
                total_volume+=volume
                for di in range(len(rows)):
                    frequencies=Counter(zip(c0[0],cm[di],c2[0]))
                    count=sum(v==1 for v in frequencies.values())
                    weighted[di]+=volume*count
    assert total_volume==denominator**3
    return {key:Q(weighted[i],n*denominator**3) for i,key in enumerate(designs)},len(s0)*len(sm)*len(s2)


def main():
    ap=ArgumentParser()
    ap.add_argument("--kernel",type=Path,required=True)
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    kernel=load_kernel(args.kernel)
    c=8;p=10;B=4
    templates=[(v,w) for v in range(2,c+1) for w in range(2,v+1)]
    raw={m:[tuple(kernel.readout(n,*t) for n in (c,c+m,c+B)) for t in templates]
         for m in (1,2)}
    scaled={m:[tuple(Q(2)**p*g for g in point) for point in raw[m]] for m in raw}
    means={};cliques={}
    for m in raw:
        means[m],cliques[m]=phase_mean(scaled[m])
    gap=means[2]-means[1]
    assert gap>0

    q=p
    rejected=[]
    while True:
        epsilon=Q(2)**(p-q)
        uniform_pair_error=4*(1-(1-min(Q(1),epsilon))**3)
        if uniform_pair_error>=gap:
            rejected.append(q);q+=1;continue
        approximation={m:[tuple(Q(floorq(g*Q(2)**q),2**q)*Q(2)**p for g in point)
                          for point in raw[m]] for m in raw}
        approx_means={m:phase_mean(approximation[m])[0] for m in raw}
        approx_gap=approx_means[2]-approx_means[1]
        if approx_gap>uniform_pair_error:
            break
        rejected.append(q);q+=1
    individual_bounds={m:stability_bound(scaled[m],approximation[m]) for m in raw}
    for m in raw:
        assert abs(means[m]-approx_means[m])<=individual_bounds[m]
        assert individual_bounds[m]<=2*(1-(1-epsilon)**3)
    assert gap>=approx_gap-uniform_pair_error>0
    partition_means,partition_cells=dyadic_partition_mean(approximation,2**(q-p))
    assert partition_means==approx_means

    # The coefficient 2 is attained by a two-point one-dimensional example.
    x=[(Q(0),),(Q(1,4),)]
    y=[(Q(0),),(Q(1,2),)]
    mx,_=phase_mean(x);my,_=phase_mean(y)
    sharp=stability_bound(x,y)
    assert my-mx==sharp==Q(1,4)

    result={
        "arithmetic":"fractions.Fraction; exact inclusion-exclusion with joint competitors",
        "kernel_sha256":hashlib.sha256(args.kernel.read_bytes()).hexdigest(),
        "base_inventory":c,"outer_gap":B,"precision":p,"templates":len(templates),
        "positions":{
            str(m):{"stocks":[c,c+m,c+B],"exact_mean_unique_fraction":str(means[m]),
                    "outward_interval":decimal_interval(means[m]),"clique_counts":cliques[m]}
            for m in raw},
        "midpoint_minus_quarter":{"exact_gap":str(gap),"outward_interval":decimal_interval(gap)},
        "rational_truncation_certificate":{
            "raw_readout_fraction_bits":q,
            "scaled_coordinate_error_bound":str(epsilon),
            "uniform_pair_error_bound":str(uniform_pair_error),
            "approximate_mean_fractions":{str(m):str(approx_means[m]) for m in raw},
            "approximate_gap":str(approx_gap),
            "certified_true_gap_lower_bound":str(approx_gap-uniform_pair_error),
            "actual_individual_stability_bounds":{str(m):str(individual_bounds[m]) for m in raw},
            "independent_positive_partition_cells":partition_cells,
            "partition_and_inclusion_exclusion_equal":True,
            "claim":"This q is a sufficient certificate precision, not a global optimum for every possible checker."},
        "sharpness_example":{"X":[["0"],["1/4"]],"Y":[["0"],["1/2"]],
                             "means":[str(mx),str(my)],"bound":str(sharp)},
        "all_checks_passed":True,
    }
    path=args.output or Path(__file__).with_name("phase_average_results.json")
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"means":{m:decimal_interval(means[m]) for m in raw},
                      "gap":decimal_interval(gap),"sufficient_raw_fraction_bits":q,
                      "certified_gap_lower":str(approx_gap-uniform_pair_error),
                      "clique_counts":cliques},indent=2))


if __name__=="__main__":
    main()
