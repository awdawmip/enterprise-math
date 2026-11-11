"""Exact finite and arbitrary-input certificates for fourth place (C64).

Run together with finite_certificate.py. Supply C63's original
numeric/certify_schedules.py using --model. Output uses rigorous rounded
enclosures for readability. The assertions compare exact rational numbers.
"""
import argparse
from fractions import Fraction as Q
from heapq import nsmallest
from pathlib import Path
import json

from finite_certificate import named_paths, read_model, schedule_matrix, map_bounds
from suffix_limits import enclose_decimals, derivative_ratio, block, compose, integer_matrix, interval_image


def paths(k):
    A,B,C = named_paths(k)
    D = (1,)*(k-3)+(0,0,2,0)
    E = (2,0)+(1,)*(k-3)+(0,0)
    items = dict(A=A,B=B,C=C,D=D,E=E)
    assert len(set(items.values()))==5
    assert all(len(path)==k+1 and sum(path)==k-1 for path in items.values())
    return items


def bounded(value):
    return enclose_decimals((value,value),8)


def run(model):
    cut = 63
    stocks = range(2,66)
    # Six suffice to guarantee a first path outside the five named paths.
    data = {c:[(model.terminal_lower(c),(c-2,))] for c in stocks}
    rows = []
    for r in range(1,cut+1):
        current = {}
        for c in stocks:
            candidates = []
            for m,mobius in enumerate(model.block_maps(r,c)):
                edge = model.derivative_lower(mobius)
                candidates.extend((v*edge,(m,)+p) for v,p in data[c-m])
            current[c] = nsmallest(6,candidates)
        data = current
        k = r+1
        if k<4:
            continue
        selected = nsmallest(6,((v,(k+1-c,)+p) for c in range(2,k+2)
                                for v,p in data[c]))
        candidates = paths(k)
        values = {name:map_bounds(schedule_matrix(p,model))[1] for name,p in candidates.items()}
        outside = min(v for v,p in selected if p not in candidates.values())
        fourth = 'E' if k<=9 else 'D'
        alternative = 'D' if k<=9 else 'E'
        assert values['A'] < values['B'] < values['C'] < values[fourth]
        assert values[fourth] < min(values[alternative],outside)
        rows.append(dict(k=k,fourth=fourth,E_over_A=bounded(values['E']/values['A']),
                         D_over_A=bounded(values['D']/values['A']),
                         outside_lower_over_A=bounded(outside/values['A'])))
    candidates = {key:p[1:] for key,p in paths(cut+1).items() if key!='E'}
    bounds = {key:map_bounds(schedule_matrix(p,model,True,cut+1)) for key,p in candidates.items()}
    outside = min(v for v,p in data[cut+1] if p not in candidates.values())
    for a,b in zip("ABC","BCD"):
        assert bounds[a][2]<bounds[b][0]
    assert bounds['D'][2]<outside
    assert bounds['D'][2]<190*bounds['A'][0]
    # Direct alternative bound: across every incoming interval from k>=5,
    # the ratio is sandwiched by the derivative ratios at the two endpoints.
    D3 = compose(integer_matrix((-1,1,0,8)),
                 compose(block(1,4,2),compose(block(2,4,0),block(3,4,0))))
    A3 = compose(integer_matrix((-115,124096,-51520,27872768)),block(3,4,1))
    prefix = (1,0,0,1)
    intervals = {}
    for k in range(4,21):
        if k>4:
            prefix = compose(prefix,block(k-1,k,1))
        incoming = interval_image(prefix,(Q(0),Q(1)))
        box = sorted(derivative_ratio(D3,A3,x) for x in incoming)
        if k>=5:
            assert Q(184)<box[0]<=box[1]<Q(185)
        if k in (4,5,10,20):
            intervals[k] = enclose_decimals(box,40)
    return dict(finite=rows,cut=dict(r=cut,c=cut+1,D_lower_over_C_upper=bounded(bounds["D"][0]/bounds["C"][2]),
                other_lower_over_D_upper=bounded(outside/bounds["D"][2]),
                other_lower_over_A_upper=bounded(outside/bounds["A"][2]),
                D_upper_over_A_lower=bounded(bounds["D"][2]/bounds["A"][0])),
                D3_matrix=D3,A3_matrix=A3,D_over_A_nested_enclosures=intervals)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=run(read_model(args.model))
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(result['cut'])
    print(*[x for x in result['finite'] if x['k'] in (4,9,10,64)],sep='\n')
