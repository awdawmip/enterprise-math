"""Full three-tail H ranks. All finite decisions are strict rational comparisons."""
import argparse
from fractions import Fraction as Q
from heapq import nsmallest
from itertools import combinations
import json
from pathlib import Path

from finite_certificate import read_model, tail_weights, compose
from fourth_certificate import paths, bounded
from observable_minimum import T, hilbert_ratio
from suffix_limits import all_gaps


def tail_forms(stock):
    l0,l1,l2=tail_weights(stock)
    return [(l1*T[1][j]-l2*T[2][j],7*l0*T[0][j]+l2*T[2][j]) for j in range(3)]


def pullback(forms,matrix):
    a,b,c,d=matrix
    return [(p*a+q*c,p*b+q*d) for p,q in forms]


def log_bounds(forms):
    lower,upper=[],[]
    for (a,b),(c,d) in combinations(forms,2):
        x0,x1=abs(b),abs(a+b)
        y0,y1=abs(d),abs(c+d)
        assert b*(a+b)>0 and d*(c+d)>0
        wedge=abs(a*d-b*c)
        lower.append(wedge/(max(x0,x1)*max(y0,y1)))
        upper.append(wedge/(min(x0,x1)*min(y0,y1)))
    return max(lower),max(upper)


def word_forms(model,stock,path):
    mat=(1,0,0,1)
    for r,m in zip(range(len(path)-1,0,-1),path[:-1]):
        from itertools import islice
        a,b,c=next(islice(model.block_maps(r,stock),m,None))
        mat=compose((0,a,b-c,a+c),mat)
        stock-=m
    assert stock==2+path[-1]
    return pullback(tail_forms(stock),mat)


def compute(model):
    limit=63
    stocks=range(2,66)
    terminal={c:tail_forms(c) for c in stocks}
    data={c:[(log_bounds(terminal[c])[0],(c-2,))] for c in stocks}
    rows=[]
    for r in range(1,limit+1):
        current={}
        for c in stocks:
            choices=[]
            for m,step in enumerate(model.block_maps(r,c)):
                a,b,h=step
                if r==1:
                    bound=log_bounds(pullback(terminal[c-m],(0,a,b-h,a+h)))[0]
                    choices.append((bound,(m,c-m-2)))
                else:
                    bound=model.derivative_lower(step)
                    choices.extend((bound*value,(m,)+path) for value,path in data[c-m])
            current[c]=nsmallest(6,choices)
        data=current
        k=r+1
        if k<4: continue
        p=paths(k)
        all_six=nsmallest(6,((v,(k+1-c,)+sub) for c in range(2,k+2) for v,sub in data[c]))
        outside=min(v for v,path in all_six if path not in p.values())
        vals={key:hilbert_ratio(k,path) for key,path in p.items()}
        fourth='E' if k<=8 else 'D'
        other='D' if fourth=='E' else 'E'
        assert 1<vals['A']<vals['B']<vals['C']<vals[fourth]<vals[other],(k,vals)
        assert outside>vals[fourth]-1,(k,float(outside/(vals[fourth]-1)))
        rows.append(dict(k=k,fourth=fourth,lower_over_fourth_H_minus_one=bounded(outside/(vals[fourth]-1)),
                         E_over_D_excess=bounded((vals['E']-1)/(vals['D']-1))))
    cutpaths={key:p[1:] for key,p in paths(64).items() if key!='E'}
    intervals={key:log_bounds(word_forms(model,64,path)) for key,path in cutpaths.items()}
    outside=min(v for v,path in data[64] if path not in cutpaths.values())
    for x,y in zip("ABC","BCD"): assert intervals[x][1]<intervals[y][0]
    assert intervals['D'][1]<outside
    from finite_certificate import map_bounds,schedule_matrix
    a_lo,_,a_hi=map_bounds(schedule_matrix(cutpaths['A'],model,True,64))
    assert intervals['D'][1]<750*a_lo
    assert min(outside,*(x[0] for x in intervals.values()))>4*a_hi
    assert Q(377,378)*256*4>750
    assert Q(83,96)*Q(377,378)*Q(21,10)*600>750
    assert Q(83,96)*Q(377,378)*Q(21,10)**32*2>750
    small={}
    for k in (2,3):
        values=sorted((hilbert_ratio(k,path),path) for path in all_gaps(k))
        assert len({v for v,p in values})==len(values)
        small[k]=[list(p) for v,p in values[:4]]
    return dict(finite=rows,small_H_ranking=small,cut={key:[bounded(x/a_hi) for x in interval]
                    for key,interval in intervals.items()},other_cut_lower_over_A_TV_sup=bounded(outside/a_hi))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    out=compute(read_model(args.model))
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print(out["cut"],out["small_H_ranking"])
