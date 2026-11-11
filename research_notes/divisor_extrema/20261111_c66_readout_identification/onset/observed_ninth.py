"""Exact ninth-place and 63-pair cut checks for the calibrated three-tail readout."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from heapq import nsmallest
import json
from pathlib import Path
from finite_certificate import read_model, map_bounds, schedule_matrix
from fourth_certificate import bounded
from observed_four import log_bounds, pullback, tail_forms, word_forms
from observable_minimum import hilbert_ratio


def code(path):
    first = next(i for i, m in enumerate(path) if m != 1)
    if path[:2] == (2, 0) and path[2:-2] == (1,)*(len(path)-4) and path[-2:] == (0, 0):
        return "E"
    return ",".join(map(str,path[first:])) if first else "full:" + ",".join(map(str,path))


def run(model, stocks):
    layer = {}
    finite = []
    depth = 16
    for r in range(1,64):
        new = {}
        for c in range(2,66):
            options = []
            for m,(a,b,h) in enumerate(model.block_maps(r,c)):
                if r == 1:
                    terminal = pullback(tail_forms(c-m),(0,a,b-h,a+h))
                    options.append((log_bounds(terminal)[0],(m,c-m-2)))
                else:
                    slope = model.derivative_lower((a,b,h))
                    options.extend((slope*v,(m,)+path) for v,path in layer[c-m])
            new[c] = nsmallest(depth,options)
        layer = new
        k = r + 1
        if k < 3: continue
        selected = nsmallest(depth,((v,(k+1-c,)+tail) for c in range(2,k+2) for v,tail in layer[c]))
        actual = sorted((hilbert_ratio(k,path),path) for _,path in selected)
        assert actual[7][0] < actual[8][0] < actual[9][0]
        last_bound = selected[-1][0]
        if len(selected) == depth: assert actual[8][0]-1 < last_bound
        finite.append(dict(k=k,ninth=code(actual[8][1])))
    base = (1,)*62+(0,0)
    vlow,_,vhigh = map_bounds(schedule_matrix(base,model,True,64))
    cut = sorted((*log_bounds(word_forms(model,64,path)),path) for _,path in layer[64])
    lo,hi,path = cut[8]
    assert code(path) == "0,2,0,0" and max(t[1] for t in cut[:8]) < lo
    assert min(cut[9][0],layer[64][-1][0]) > hi and hi < 11200*vlow
    assert cut[1][0]>63*vhigh and layer[64][-1][0]>63*vhigh and cut[0][0]>4*vhigh
    a,h,b=Q(53,37),Q(377,378),Q(21,10)
    floors = {int(c):v for c,v in stocks['floor_by_stock'].items()}
    assert floors[63]>600 and min(v for c,v in floors.items() if c!=63)>=49508
    lower = {'64_A':4*3500, '64_other':h*256*63,'2_to_96_except_63_64':a*h*b*49508,
             '63_many_defects':a*h*b**4*600, '63_negative_initial':a*h*b*600*16,
             '63_nonnegative_initial':a*h*3840*600,'above_96':a*h*2*b**32}
    assert min(lower.values())>=14000
    runs=[]
    for row in finite:
        if not runs or runs[-1]['ninth']!=row['ninth']: runs.append(dict(start=row['k'],ninth=row['ninth']))
    return dict(finite_changes=runs,finite_scales=len(finite),cut_over_A_TV=[bounded(lo/vhigh),bounded(hi/vlow)],
                first_excluded_over_A_upper=bounded(min(cut[9][0],layer[64][-1][0])/vhigh),
                high_defect_log_H_over_Delta_A_lower=14000,cut_code=code(path))


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--model',type=Path,required=True)
    ap.add_argument('--stocks',type=Path,required=True)
    args=ap.parse_args()
    print(json.dumps(run(read_model(args.model),json.loads(args.stocks.read_text())),indent=2))
