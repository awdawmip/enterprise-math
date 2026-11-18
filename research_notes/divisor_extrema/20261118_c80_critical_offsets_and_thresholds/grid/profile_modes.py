"""Certified first axial mode amplitudes and their share of translation variance."""
from collections import Counter
from functools import cache
from pathlib import Path
import argparse
import json
import subprocess
import tempfile

from mpmath import iv, mp
from profile import BASE, UNIT, physical_pairs, approximate, multiplier

iv.dps=45
S=1<<60
CHUNK=10

@cache
def root_part(position,digit):
    if digit==0: return S,0
    phase=2*iv.pi*(digit<<(CHUNK*position))/UNIT
    vals=[]
    for v in (iv.cos(phase)*S,iv.sin(phase)*S):
        k=int(v.a)
        assert k-1<=v and v<=k+1
        vals.append(k)
    return tuple(vals)

def root(r):
    x,y=S,0
    for j in range(4):
        digit=(r>>(CHUNK*j)) & ((1<<CHUNK)-1)
        if digit:
            a,b=root_part(j,digit)
            x,y=(x*a-y*b)//S,(x*b+y*a)//S
    return x,y

def scaled_bracket(positive,scale=10**12):
    z=positive*scale
    lo=max(0,int(z.a))
    hi=int(z.b)+1
    return [lo,hi]

def interval_from_pair(pair,scale):
    return iv.mpf(pair)/scale

def axial(points,axis,geometry_error=4):
    # Shape translation contributes at most geometry_error/Q to the coefficient.
    n=len(points)
    with tempfile.TemporaryFile(mode="w+") as fp:
        print(n,UNIT,1,file=fp)
        for p in points: print(p[axis],p[1-axis],file=fp)
        fp.seek(0)
        res=subprocess.check_output([str(BASE/"sweep"),"--axis-jumps"],stdin=fp,text=True)
    jumps=Counter()
    for line in res.splitlines():
        t,h=map(int,line.split())
        jumps[t%UNIT]+=h
    assert sum(jumps.values())==0 and sum(abs(z) for z in jumps.values())<=2*n*UNIT
    x=y=0
    for r,w in jumps.items():
        if w:
            a,b=root(r)
            x+=a*w; y+=b*w
    approx=iv.sqrt(iv.mpf(x*x+y*y))/(2*iv.pi*n*UNIT*S)
    # Complex root errors after at most four fixed point products are <=32/S,
    # and all jump magnitudes sum to <=2*n*UNIT. Division by 2*pi yields <12/S.
    err=iv.mpf(geometry_error)/UNIT+iv.mpf(12)/S
    return [scaled_bracket(approx-err)[0],scaled_bracket(approx+err)[1]]

def selfcheck():
    # Independent direct phase enumeration on a coarse grid; integrate the
    # exponential analytically within each phase strip.
    from collections import Counter
    mp.dps=45
    Q=8
    for pts in [[(0,0)],[(3,4),(4,4)],[(5,2),(1,3),(3,4),(9,1),(15,7),(4,4)]]:
        real=[(x*(UNIT//Q),y*(UNIT//Q)) for x,y in pts]
        f=[[sum(v==1 for v in Counter(((x+a)//Q,(y+b)//Q) for x,y in pts).values())/mp.mpf(len(pts))
            for b in range(Q)] for a in range(Q)]
        for axis in range(2):
            if axis==1: f=list(zip(*f))
            ref=abs(sum((mp.exp(-2j*mp.pi*(i+1)/Q)-mp.exp(-2j*mp.pi*i/Q))/
                        (-2j*mp.pi)*sum(row)/Q for i,row in enumerate(f)))
            lo,hi=axial(real,axis,0)
            assert lo<=ref*10**12<=hi

def compute(c):
    n=c*(c-1)//2
    p=((c**9).bit_length()-1)//4
    sc=multiplier(c,p,0,"bits")
    pts=[tuple(approximate(iv,sc) for iv in vals) for vals in physical_pairs(c)]
    s=next(z for z in json.loads((BASE/"extrema_moments.json").read_text()) if z['c']==c)['stddev_unique_1e10']
    modes=[axial(pts,j) for j in (0,1)]
    amplitudes=[interval_from_pair(x,10**12) for x in modes]
    variance=interval_from_pair(s,10**10)**2
    shares=[2*x*x/variance for x in amplitudes]
    return dict(c=c,p=p,templates=n,mode_10_amplitude_1e12=modes[0],mode_01_amplitude_1e12=modes[1],
                mode_pm10_share_1e12=scaled_bracket(shares[0]),mode_pm01_share_1e12=scaled_bracket(shares[1]),
                combined_variance_share_1e12=scaled_bracket(sum(shares)),stddev_unique_1e10=s)

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("stocks",nargs="+",type=int)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    selfcheck()
    rows=[]
    for c in args.stocks:
        rows.append(compute(c))
        print(json.dumps(rows[-1]),flush=True)
        args.output.write_text(json.dumps(rows,indent=2)+"\n")
