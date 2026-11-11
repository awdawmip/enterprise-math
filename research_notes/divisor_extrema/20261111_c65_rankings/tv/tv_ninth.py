"""Exact supplement for the ninth TV schedule and its first stable scale."""
import argparse
import json
from heapq import nsmallest
from math import comb
from pathlib import Path
import sys


def predict(k):
    if k == 3:
        return (0, 0, 0, 2)
    if k == 4:
        return (0, 1, 1, 1, 0)
    if k == 5:
        return (2, 0, 1, 0, 1, 0)
    if k <= 8:
        return (1,) * (k - 3) + (0, 0, 1, 1)
    if k <= 19:
        return (1,) * (k - 3) + (0, 0, 0, 2)
    if k <= 32:
        return (2, 0) + (1,) * (k - 3) + (0, 0)
    return (1,) * (k - 3) + (0, 2, 0, 0)


def run(model, matrices, enclose):
    stocks = range(2, 66)
    layer = {c: [(model.terminal_lower(c), (c-2,))] for c in stocks}
    finite = []
    for r in range(1, 64):
        next_layer = {}
        for c in stocks:
            options = []
            for m, transform in enumerate(model.block_maps(r, c)):
                slope = model.derivative_lower(transform)
                options.extend((slope*v, (m,)+tail) for v, tail in layer[c-m])
            next_layer[c] = nsmallest(15, options)
        layer = next_layer
        k = r+1
        if k < 3:
            continue
        retained = nsmallest(15, ((v,(k+1-c,)+tail) for c in range(2,k+2)
                                  for v,tail in layer[c]))
        exact = sorted((matrices.map_bounds(matrices.schedule_matrix(path,model))[1],path)
                       for _,path in retained)
        delta, winner = exact[8]
        assert exact[7][0] < delta < exact[9][0]
        assert winner == predict(k)
        if len(retained) < comb(2*k-1, k):
            assert delta < retained[-1][0]
        finite.append(dict(k=k, ratio=enclose((delta/exact[0][0],)*2, 12)))

    retained = layer[64]
    cuts = []
    for _,path in retained:
        lower, _, upper = matrices.map_bounds(matrices.schedule_matrix(path,model,True,64))
        cuts.append((lower,upper,path))
    cuts.sort()
    low, high, winner = cuts[8]
    assert winner == predict(65)[2:]
    assert max(x[1] for x in cuts[:8]) < low
    unseen = min(retained[-1][0], *(x[0] for x in cuts[9:]))
    assert unseen > high
    base_low, base_high, _ = cuts[0]
    assert high < 3500 * base_low  # HIGH_3500.md excludes every high defect.
    return dict(finite=finite, ninth_after_32="left-pad 0200 with ones to k+1 gaps",
                cut_ninth_over_A=enclose((low/base_high, high/base_low), 12),
                cut_remaining_lower_over_A=enclose((unseen/base_high,)*2, 12),
                cut_first_excluded_bound_over_A=enclose((retained[-1][0]/base_high,)*2,12),
                high_defect_lower_over_A=3500, first_stable_k=33)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--c64', type=Path, required=True)
    parser.add_argument('--model', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.c64.resolve()))
    import finite_certificate, suffix_limits
    result = run(finite_certificate.read_model(args.model), finite_certificate,
                 suffix_limits.enclose_decimals)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print({k:v for k,v in result.items() if k!='finite'})
