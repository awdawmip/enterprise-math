"""Finite and cut certificates for the first three C62/C63 schedule values.

Run from this directory: python finite_certificate.py --model PATH --output FILE
PATH is the unchanged C63 numeric/certify_schedules.py. No third-party libraries.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from heapq import nsmallest
from math import gcd
from pathlib import Path


def read_model(path):
    spec = importlib.util.spec_from_file_location("c63_numeric", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def named_paths(k):
    prefix = (1,) * (k-2)
    return (prefix + (1,0,0), prefix + (0,1,0), prefix + (0,0,1))


def fraction_pair(x):
    return [str(x.numerator), str(x.denominator)]


def tail_weights(c):
    weights = [Q(1)] * 3
    for n in range(3,c+1):
        for i,z in enumerate((Q(1,4),Q(1),Q(4))):
            weights[i] *= n*z/(1+n*z)
    return weights


def compose(outer,inner):
    a,b,c,d = outer
    e,f,g,h = inner
    entries = (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
    factor = gcd(*entries)
    return tuple(x//factor for x in entries)


def primitive_matrix(entries):
    from math import lcm
    den = lcm(*(v.denominator for v in entries))
    raw = tuple(int(v*den) for v in entries)
    common = gcd(*raw)
    return tuple(v//common for v in raw)


def schedule_matrix(path,model,skip_initial=False,initial_stock=None):
    if skip_initial:
        internal,stock=path[:-1],initial_stock
    else:
        internal=path[1:-1]
        stock=len(path)-path[0]
    matrix=(1,0,0,1)
    for r,m in zip(range(len(internal),0,-1),internal):
        from itertools import islice
        a,b,c=next(islice(model.block_maps(r,stock),m,None))
        matrix=compose((0,a,b-c,a+c),matrix)
        stock-=m
    assert stock==path[-1]+2
    l0,l1,l2=tail_weights(stock)
    # Third coordinate strictly decreases with u. Its difference is exactly TV.
    return compose(primitive_matrix((-l2,l2,l1-l2,7*l0+l2)),matrix)


def map_bounds(matrix):
    a,b,c,d=matrix
    det=abs(a*d-b*c)
    min_den,max_den=sorted((abs(d),abs(c+d)))
    assert min_den>0 and d*(c+d)>0
    return (Q(det,max_den**2),Q(det,min_den*max_den),Q(det,min_den**2))


def calculate(model):
    cut=63
    # c<=65 covers every first stock for k<=64. For the common cut only c=64 is needed.
    stocks=range(2,66)
    data={c:[(model.terminal_lower(c),(c-2,))] for c in stocks}
    rows=[]
    for r in range(1,cut+1):
        current={}
        for c in stocks:
            options=[]
            for m,mobius in enumerate(model.block_maps(r,c)):
                edge=model.derivative_lower(mobius)
                options.extend((edge*value,(m,)+path) for value,path in data[c-m])
            current[c]=nsmallest(4,options)
        data=current
        k=r+1
        selected=nsmallest(4,((val,(k+1-c,)+path) for c in range(2,k+2)
                               for val,path in data[c]))
        if k<4:
            continue
        A,B,C=named_paths(k)
        outside=min(val for val,p in selected if p not in (A,B,C))
        da,db,dc=[map_bounds(schedule_matrix(p,model))[1] for p in (A,B,C)]
        assert da<db<dc<outside and dc<25*da
        rows.append(dict(k=k,B_over_A=fraction_pair(db/da),C_over_A=fraction_pair(dc/da),
                         other_lower_over_A=fraction_pair(outside/da),
                         fourth_bound_path=list(next(p for v,p in selected if v==outside))))
    stock=cut+1
    A,B,C=[p[1:] for p in named_paths(cut+1)]
    bounds=[map_bounds(schedule_matrix(p,model,True,stock)) for p in (A,B,C)]
    outside=min(v for v,p in data[stock] if p not in (A,B,C))
    (a0,_,a1),(b0,_,b1),(c0,_,c1)=bounds
    assert a1<b0 and b1<c0 and c1<outside and c1<25*a0
    return dict(finite=rows,cut=dict(r=cut,c=stock,B_lower_over_A_upper=fraction_pair(b0/a1),
                C_lower_over_B_upper=fraction_pair(c0/b1),
                other_lower_over_C_upper=fraction_pair(outside/c1),
                C_upper_over_A_lower=fraction_pair(c1/a0)),
                checked="integer and Fraction comparisons")


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=calculate(read_model(args.model))
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    for row in result["finite"][:3]:
        print(row["k"],*[float(Q(*map(int,row[key]))) for key in ("B_over_A","C_over_A","other_lower_over_A")])
    for key,pair in result["cut"].items():
        if isinstance(pair,list): print(key,float(Q(*map(int,pair))))
