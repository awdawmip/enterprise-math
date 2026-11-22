"""Exact comparison of original finite inventory designs over every grid origin.

The grid convention is floor(2**p * g + u), 0 <= u < 1.  Breakpoints
and input readouts are exact Fractions.  The phase sweep itself uses
integer bucket labels; endpoint and breakpoint phases are included by
the half-open, right-continuous convention.
"""

from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path


def load_kernel(path):
    spec = importlib.util.spec_from_file_location("c78_exact_kernel", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def floorq(x):
    return x.numerator // x.denominator


def origin_states(value_columns, precision):
    """Common partition for one or several competing axes.

    Each return row is (left, right, tuple of complete integer bin columns).
    On [left,right) all labels are exactly as recorded, including left.
    """
    scale = Q(2)**precision
    columns = [[floorq(scale*x) for x in values] for values in value_columns]
    events = defaultdict(list)
    for ci, values in enumerate(value_columns):
        for i, value in enumerate(values):
            x = scale*value
            fractional = x-floorq(x)
            if fractional:
                events[1-fractional].append((ci, i))
    states = []
    left = Q(0)
    for point in sorted(events):
        states.append((left, point, tuple(tuple(c) for c in columns)))
        for ci, i in events[point]:
            columns[ci][i] += 1
        left = point
    states.append((left, Q(1), tuple(tuple(c) for c in columns)))
    assert states[0][0] == 0 and states[-1][1] == 1
    assert all(a < b for a, b, _ in states)
    assert all(states[i][1] == states[i+1][0] for i in range(len(states)-1))
    return states


def simple_dyadic(a, b):
    denominator=1
    while True:
        numerator=-((-a.numerator*denominator)//a.denominator)
        point=Q(numerator,denominator)
        if point < b:
            assert a <= point
            return point
        denominator*=2


def compact_witness(box, counts):
    offsets=[simple_dyadic(a,b) for a,b in box]
    return {"offsets": [str(x) for x in offsets], "unique_counts": counts,
            "phase_box": [[str(a),str(b)] for a,b in box]}


def uniform_precision(values, templates):
    if len(values)==1:
        return {"minimum_precision":0,"minimum_pair_separation":None,
                "pairs_checked":0,"reason":"A one-template catalog is always unique."}
    candidates=[]
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            distance=max(abs(a-b) for a,b in zip(values[i],values[j]))
            candidates.append((distance,i,j))
    distance,i,j=min(candidates)
    if not distance:
        return {"minimum_precision":None,"duplicate_templates":[templates[i],templates[j]]}
    p=0
    while Q(2)**p*distance<1:
        p+=1
    assert Q(2)**p*distance>=1
    assert p==0 or Q(2)**(p-1)*distance<1
    return {"minimum_precision":p,
            "minimum_pair_separation":str(distance),
            "minimizing_pair":[templates[i],templates[j]],
            "pairs_checked":len(candidates),
            "scaled_separation_at_minimum":str(Q(2)**p*distance)}


def compare(c, outer_gap, middles, precision, kernel):
    """Complete all-origin ranges; no distributional or independence assumption."""
    assert c >= 2 and outer_gap >= 2
    assert all(0 < d < outer_gap for d in middles)
    templates = [(v, w) for v in range(2, c+1) for w in range(2, v+1)]
    stocks = [c] + [c+d for d in middles] + [c+outer_gap]
    data = [[kernel.readout(n, v, w) for v, w in templates] for n in stocks]
    s0 = origin_states([data[0]], precision)
    sm = origin_states(data[1:-1], precision)
    s2 = origin_states([data[-1]], precision)
    designs = len(middles)
    n = len(templates)
    lo, hi = [n]*designs, [0]*designs
    solo_min_witness,solo_max_witness={},{}
    pairs = [(i,j) for i in range(designs) for j in range(i+1, designs)]
    pair_min = {ij:n for ij in pairs}
    pair_max = {ij:-n for ij in pairs}
    witnesses_min, witnesses_max = {}, {}
    evaluated_cells = 0
    all_endpoint_unique_cells = 0

    def update(counts, box):
        for i,count in enumerate(counts):
            if count<lo[i] or i not in solo_min_witness:
                lo[i]=count
                solo_min_witness[i]=compact_witness(box,counts)
            if count>hi[i] or i not in solo_max_witness:
                hi[i]=count
                solo_max_witness[i]=compact_witness(box,counts)
        for ij in pairs:
            i,j = ij
            delta = counts[i]-counts[j]
            if delta < pair_min[ij]:
                pair_min[ij] = delta
                witnesses_min[ij] = compact_witness(box, counts)
            if delta > pair_max[ij]:
                pair_max[ij] = delta
                witnesses_max[ij] = compact_witness(box, counts)

    for a0, b0, cols0 in s0:
        for a2, b2, cols2 in s2:
            groups = defaultdict(list)
            for i, tag in enumerate(zip(cols0[0], cols2[0])):
                groups[tag].append(i)
            tied = [indices for indices in groups.values() if len(indices)>1]
            already_unique = sum(len(indices)==1 for indices in groups.values())
            if not tied:
                update([n]*designs, ((a0,b0),(sm[0][0],sm[0][1]),(a2,b2)))
                all_endpoint_unique_cells += len(sm)
                continue
            for am, bm, columns in sm:
                counts = [already_unique]*designs
                for di,bins in enumerate(columns):
                    for indices in tied:
                        frequency = Counter(bins[i] for i in indices)
                        counts[di] += sum(mult==1 for mult in frequency.values())
                update(counts, ((a0,b0),(am,bm),(a2,b2)))
                evaluated_cells += 1

    pair_results = []
    for ij in pairs:
        i,j = ij
        pair_results.append({
            "middle_gaps": [middles[i], middles[j]],
            "difference": "first unique count minus second unique count",
            "minimum": pair_min[ij], "maximum": pair_max[ij],
            "minimum_witness": witnesses_min[ij],
            "maximum_witness": witnesses_max[ij],
        })

    # Independent direct reconstruction checks each extrema witness from raw g.
    checked = 0
    all_witnesses=list(solo_min_witness.values())+list(solo_max_witness.values())
    all_witnesses += [pair[name] for pair in pair_results
                      for name in ("minimum_witness", "maximum_witness")]
    for witness in all_witnesses:
            offsets = tuple(map(Q,witness["offsets"]))
            exact_counts=[]
            for di in range(designs):
                tags = [tuple(floorq(Q(2)**precision*data[col][i]+offsets[j])
                              for j,col in enumerate((0,di+1,len(data)-1)))
                        for i in range(n)]
                frequency=Counter(tags)
                exact_counts.append(sum(mult==1 for mult in frequency.values()))
            assert exact_counts==witness["unique_counts"]
            checked+=1

    cells = len(s0)*len(sm)*len(s2)
    assert evaluated_cells+all_endpoint_unique_cells==cells
    return {
        "base_inventory": c, "outer_gap": outer_gap,
        "middle_gaps": middles, "precision": precision,
        "templates": n, "origin_domain": "[0,1)^3; three independent global grid origins",
        "comparison_coupling": "Same first, middle, and last origin for all compared designs",
        "arithmetic": "fractions.Fraction and exact integers",
        "partition_intervals": [len(s0),len(sm),len(s2)],
        "complete_phase_cells": cells,
        "evaluated_tied_cells": evaluated_cells,
        "endpoint_unique_cells": all_endpoint_unique_cells,
        "unique_count_ranges": [[lo[i],hi[i]] for i in range(designs)],
        "individual_minimum_witnesses": [solo_min_witness[i] for i in range(designs)],
        "individual_maximum_witnesses": [solo_max_witness[i] for i in range(designs)],
        "uniform_full_identification_precision": [
            uniform_precision([tuple(data[col][i] for col in (0,di+1,len(data)-1))
                               for i in range(n)],templates) for di in range(designs)],
        "pairwise_differences": pair_results,
        "extrema_direct_checks": checked,
        "all_checks_passed": True,
    }


def main():
    p=ArgumentParser()
    p.add_argument("--kernel",type=Path,required=True)
    p.add_argument("--c",type=int,default=8)
    p.add_argument("--gap",type=int,default=4)
    p.add_argument("--middles",type=int,nargs="+",default=[1,2])
    p.add_argument("--precisions",type=int,nargs="+",default=list(range(4,17)))
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    kernel=load_kernel(args.kernel)
    results=[]
    for precision in args.precisions:
        row=compare(args.c,args.gap,args.middles,precision,kernel)
        results.append(row)
        print(json.dumps({"p":precision,"ranges":row["unique_count_ranges"],
                          "differences":[[r["minimum"],r["maximum"]] for r in row["pairwise_differences"]],
                          "cells":row["complete_phase_cells"]}),flush=True)
    output=args.output or Path(__file__).with_name("all_origins_results.json")
    output.write_text(json.dumps({"results":results},indent=2)+"\n")


if __name__=="__main__":
    main()
