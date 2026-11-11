"""Exact C65 first-eight ranking of three-tail probability ratios.

Supply the C64 checks directory on PYTHONPATH and C63 numeric model via --model.
Rows contain exact schedule identities. Displayed real bounds are outward rounded.
"""
import argparse
from fractions import Fraction as Q
from heapq import nsmallest
import json
from pathlib import Path

from finite_certificate import map_bounds, read_model, schedule_matrix
from fourth_certificate import bounded
from observable_minimum import hilbert_ratio
from observed_four import log_bounds, pullback, tail_forms, word_forms
from suffix_limits import all_gaps


def encode(gaps):
    """Use a canonical suffix code, stripping the common leading ones."""
    first_deviation = next(i for i,v in enumerate(gaps) if v!=1)
    if first_deviation:
        return 'S:' + ','.join(map(str,gaps[first_deviation:]))
    # Preserve the exceptional front for long initial-stock deviations.
    if len(gaps)>=5 and tuple(gaps[:2]) in ((0,2),(2,0),(0,1)):
        i=2
        while i<len(gaps) and gaps[i]==1:
            i+=1
        if i>2:
            return 'P:' + ','.join(map(str,gaps[:2])) + '|' + ','.join(map(str,gaps[i:]))
    return ','.join(map(str,gaps))


def compute(model,cut_stocks):
    """Certify small complete ranks, then compare arbitrary common input at cut."""
    cutoff=63
    stocks=range(2,66)
    depth=16
    terminal={c:tail_forms(c) for c in stocks}
    data={}
    finite=[]
    for r in range(1,cutoff+1):
        current={}
        for stock in stocks:
            options=[]
            for m,step in enumerate(model.block_maps(r,stock)):
                a,b,h=step
                if r==1:
                    bound=log_bounds(pullback(terminal[stock-m],(0,a,b-h,a+h)))[0]
                    options.append((bound,(m,stock-m-2)))
                else:
                    edge=model.derivative_lower(step)
                    options.extend((edge*value,(m,)+path) for value,path in data[stock-m])
            current[stock]=nsmallest(depth,options)
        data=current
        k=r+1
        selected=nsmallest(depth,((v,(k+1-c,)+sub) for c in range(2,k+2)
                                  for v,sub in data[c]))
        true=sorted((hilbert_ratio(k,path),path) for _,path in selected)
        n=min(8,len(true))
        assert all(v<w for (v,_),(w,_) in zip(true,true[1:n+1]))
        if len(selected)==depth:
            # All omitted paths have log H at least this lower-product threshold.
            threshold=selected[-1][0]
            assert true[n-1][0]-1<threshold,(k,float(threshold/(true[n-1][0]-1)))
            outside=bounded(threshold/(true[n-1][0]-1))
        else:
            outside=None # Every path evaluated
        observable_ball_count=None
        if k>=18:
            baseline=true[0][0]
            assert threshold>800*(baseline-1)
            inside=sum(value-1<800*(1-1/baseline) for value,path in true)
            outside_ball=sum(1-1/value>800*(baseline-1) for value,path in true)
            assert inside+outside_ball==len(true)
            assert inside==(9 if k==18 else 8)
            observable_ball_count=inside
        finite.append(dict(k=k,within_800_logH_A=observable_ball_count,top=[encode(path) for _,path in true[:n]],
                           cutoff_over_eighth_H_minus_one=outside))
    canonical=(1,)*62+(0,0)
    umin,_,umax=map_bounds(schedule_matrix(canonical,model,True,64))
    cut=[]
    for lower,path in data[64]:
        low,high=log_bounds(word_forms(model,64,path))
        cut.append((low,high,path))
    cut.sort()
    assert all(row[1] < after[0] for row, after in zip(cut[:8],cut[1:9]))
    assert cut[7][1] < data[64][-1][0]
    assert cut[7][1] < 3300*umin
    assert cut[0][0]>4*umax
    assert cut[7][1]<800*cut[0][0]
    assert min(data[64][-1][0],cut[8][0])>800*cut[0][1]
    assert 800*cut[0][1]<3500*umin
    # Case c=64, low canonical: its readout-to-own-TV factor exceeds 4 on every interval.
    # Others are >=14*umax in TV; last high return to zero has ratio >=256.
    h=Q(377,378); b=Q(21,10); obs=Q(53,37)
    assert 1000*4>3500 and obs*h*256*14>3500
    floors={int(stock):value for stock,value in cut_stocks['floor_by_stock'].items()}
    assert floors[63]>=601 and all(floor>1200 for stock,floor in floors.items() if stock!=63)
    assert obs*h*b*1200>3500 and obs*h*b*b*600>3500 and obs*h*b*600*16>3500
    assert obs*3791>3500 and obs*h*b**32*2>3500
    switches=[]
    for row in finite:
        if not switches or row['top']!=switches[-1]['top']:
            switches.append(dict(start=row['k'],top=row['top']))
    return dict(finite=finite,cut=[dict(code=encode(path),lower_over_A_sup=bounded(lo/umax),
                    upper_over_A_inf=bounded(hi/umin)) for lo,hi,path in cut[:9]],
                finite_change_rows=switches,retained_per_state=depth,
                excluded_cut_lower_over_A_sup=bounded(data[64][-1][0]/umax),
                any_high_defect_logH_over_A_TV_lower=3500)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--stocks',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=compute(read_model(args.model),json.loads(args.stocks.read_text()))
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['cut'],indent=2))
    print(*result['finite_change_rows'],sep='\n')
