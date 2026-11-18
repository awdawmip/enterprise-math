"""Per-template isolation areas in an interval-certified square sweep.

Set C80_GRID to the directory containing the tagged C80 critical_bins.py, or
place that file alongside this script. Run c++ -O3 -std=c++17 individual.cpp
-o individual before running the Python driver.
"""
from argparse import ArgumentParser
from fractions import Fraction as F
from pathlib import Path
import json, os, subprocess, sys, tempfile
BASE=Path(__file__).resolve().parent
if os.environ.get('C80_GRID'): sys.path.insert(0,os.environ['C80_GRID'])
import critical_bins as C
Q=1<<40
REPORT=10**12

def axis(intervals,p):
    """Exact ranks of both square endpoints, with bounded dyadic locations."""
    e=[]
    d=C.UNIT
    for i,(low,high) in enumerate(intervals):
        low=(low-d)<<p
        high=(high-d)<<p
        pos=(low*Q+d//2)//d
        if not ((pos-1)*d<=low*Q<=high*Q<=(pos+1)*d):
            raise ArithmeticError('unresolved coordinates')
        if abs(pos)+4*Q>=1<<61: raise ArithmeticError('sweep coordinate overflow')
        for end in (0,1):
            e.append((low+end*d,high+end*d,pos+end*Q,i,end))
    e.sort()
    loc=[]
    ranks=[[None,None] for _ in intervals]
    l0=h0=None
    for low,high,pos,i,end in e:
        if h0 is None or low>h0: loc.append(pos)
        elif low!=high or low!=h0 or low!=l0: raise ArithmeticError('unresolved endpoint order')
        elif loc[-1]!=pos: raise ArithmeticError('same endpoint with unequal dyadic positions')
        ranks[i][end]=len(loc)-1
        l0,h0=low,high
    assert all(u<=v for u,v in zip(loc,loc[1:]))
    return loc,ranks

def bracket(x,eps=0):
    a=max(0,x-eps); b=min(1,x+eps)
    return [int((a*REPORT)//1),-int((-b*REPORT)//1)]

def finite(c):
    p=((c**9).bit_length()-1)//4
    for precision in (176,272,400):
        C.BITS=precision; C.UNIT=1<<precision; C.ONE=(C.UNIT,C.UNIT)
        C.prepare(c+1); C.terminal.cache_clear()
        pairs=[[],[]]
        for v in range(2,c+1):
            for w in range(2,v+1):
                middle=C.block(v,w,3,C.terminal(w))
                for i in (0,1): pairs[i].append(C.full_width(c+i,v,middle))
        try: xs,xr=axis(pairs[0],p); ys,yr=axis(pairs[1],p); break
        except ArithmeticError:
            if precision==400: raise
    n=len(xr)
    with tempfile.TemporaryFile(mode='w+') as f:
        print(n,len(xs),len(ys),file=f)
        print(*xs,file=f); print(*ys,file=f)
        for x,y in zip(xr,yr): print(*x,*y,file=f)
        f.seek(0)
        lines=subprocess.check_output([str(BASE/'individual')],stdin=f,text=True).splitlines()
    records=[tuple(map(int,line.split())) for line in lines]
    areas=[r[0] for r in records]
    possible=sum(r[1] for r in records); robust=sum(r[2] for r in records)
    assert len(areas)==n and min(areas)>=0 and max(areas)<=Q**2
    weight=F(sum(areas),n*Q**2)
    weight2=F(sum(a*a for a in areas),n*Q**4)
    flip=2*(weight-weight2)
    prev=BASE/'c80_extrema_moments.json'
    result={'c':c,'p':p,'n':n,'bits':precision,'never':n-possible,
            'sometimes':possible-robust,'always':robust,
            'mean_q_1e12':bracket(weight,F(4,Q)),
            'mean_q_squared_1e12':bracket(weight2,F(8,Q)),
            'independent_offsets_switch_1e12':bracket(flip,F(8,Q))}
    # |u(1-u)-v(1-v)| <= |u-v| on [0,1].
    if prev.exists():
        with prev.open() as f: old=next((r for r in json.load(f) if r['c']==c),None)
        if old is not None:
            al,ah=[F(a,10**10) for a in old['mean_unique_1e10']]
            assert max(al,weight-F(4,Q))<=min(ah,weight+F(4,Q))
            al,ah=[F(a,10**10) for a in old['stddev_unique_1e10']]
            h=flip/2
            eps=F(4,Q)
            # Ratio of empirical offset-count variance to the independent-Bernoulli counterfactual.
            if h>eps:
                aa=n*al*al/(h+eps); bb=n*ah*ah/(h-eps)
                result['variance_ratio_1e8']=[int(aa*10**8),-int((-bb*10**8)//1)]
                sqrt_two_upper=F(14142135623731,10**13)
                assert sqrt_two_upper**2>2
                conservative_flip=F(result['independent_offsets_switch_1e12'][0],REPORT)
                if conservative_flip>0:
                    cancel=max(0,1-sqrt_two_upper*ah/conservative_flip)
                    result['cancellation_lower_1e8']=int(cancel*10**8)
    # Each geometric overlap contributes at most 4/Q to total summed area errors per template, hence
    # max_i error ≤ 4N/Q. Success/failure/robust classifications above use true endpoint ranks.
    for percent in (1,25,50,75,99):
        lower=sum(a*(100*Q)>=(percent*Q+4*n*100)*(Q**2) for a in areas)
        upper=sum(a*(100*Q)>=(percent*Q-4*n*100)*(Q**2) for a in areas)
        result[f'q_ge_{percent}pct']=[lower,upper]
    return result

if __name__=='__main__':
    p=ArgumentParser()
    p.add_argument('sizes',nargs='+',type=int)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    rows=[]
    for c in args.sizes:
        rows.append(finite(c)); print(json.dumps(rows[-1]),flush=True)
        args.output.write_text(json.dumps(rows,indent=2)+'\n')
