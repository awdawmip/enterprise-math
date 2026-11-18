"""Compressed all-phase extrema, using interval-certified order on both axes."""
from argparse import ArgumentParser
from pathlib import Path
from fractions import Fraction
from math import isqrt
import json
import subprocess
import tempfile

import critical_bins as C
from profile import BASE, UNIT, physical_pairs

def axis(intervals,p):
    size=len(intervals)
    bins,times=[0]*size,[0]*size
    events=[]
    integer=[]
    for i,(a,b) in enumerate(intervals):
        a <<= p
        b <<= p
        base=a//C.UNIT
        if base!=b//C.UNIT:
            raise ArithmeticError("unresolved bin, increase interval precision")
        if not (0<=base<(1<<30)):
            raise ArithmeticError("outside 32-bit grid index range")
        bins[i]=base
        if a==b==base*C.UNIT:
            integer.append(i)
            continue
        l,r=(base+1)*C.UNIT-b,(base+1)*C.UNIT-a
        if not 0<l<=r<C.UNIT:
            raise ArithmeticError("unresolved endpoint")
        events.append((l,r,i))
    events.sort()
    rank,prev,prev_lo=0,0,0
    cuts=[0]
    for l,r,i in events:
        if l>prev:
            rank+=1
            knot=(l+r)*UNIT//(2*C.UNIT)
            assert (knot-1)*C.UNIT<=l*UNIT<=r*UNIT<=(knot+1)*C.UNIT
            cuts.append(knot)
        elif not(l==r==prev==prev_lo):
            raise ArithmeticError("unresolved breakpoint order, increase interval precision")
        times[i]=rank
        prev,prev_lo=r,l
    k=rank+1
    for i in integer: times[i]=k
    return bins,times,k,cuts+[UNIT]

def extrema(c,offset=0):
    p=((c**9).bit_length()-1)//4 + offset
    assert p>=0
    try_bits=(176,240,360,520)
    for bits in try_bits:
        # critical_bins operations use these globals, and prepare() re-creates
        # prefixes and clears the kernel cache; physical_pairs clears tails.
        C.BITS=bits
        C.UNIT=1<<bits
        C.ONE=(C.UNIT,C.UNIT)
        try:
            x,y=zip(*physical_pairs(c))
            xb,xt,xc,xcut=axis(x,p)
            yb,yt,yc,ycut=axis(y,p)
            break
        except ArithmeticError:
            if bits==try_bits[-1]: raise
    n=len(xb)
    with tempfile.TemporaryFile(mode="w+") as fp:
        print(n,xc,yc,file=fp)
        print(*xcut,file=fp)
        print(*ycut,file=fp)
        for row in zip(xb,yb,xt,yt): print(*row,file=fp)
        fp.seek(0)
        result=subprocess.check_output([str(BASE/"extrema"),"--moments"],stdin=fp,text=True)
    low,high,first,second=map(int,result.split())
    mean=Fraction(first,UNIT*UNIT*n)
    m2=Fraction(second,UNIT*UNIT*n*n)
    var=m2-mean**2
    # Independently, rounding each phase breakpoint moves an expected <=2N/Q
    # words, and moving one word changes the singleton count by at most 2.
    # By triangle inequality |E V^2 - E V'^2| <=8/Q, |Var V - Var V'| <=16/Q.
    err=Fraction(16,UNIT)
    scale=10**10
    lo=isqrt(int(max(Fraction(0),var-err)*scale**2))
    hi0=min(Fraction(1),var+err)*scale**2
    hi=isqrt(int(hi0))
    hi+=int(hi**2<hi0)
    result=dict(c=c,p=p,templates=n,phase_rectangles=xc*yc,interval_bits=bits,
                min_unique=low,max_unique=high,stddev_unique_1e10=[lo,hi],
                mean_unique_1e10=[int((mean-Fraction(4,UNIT))*scale),
                                  -int((-(mean+Fraction(4,UNIT))*scale)//1)])
    if c in (8,16,24) and offset==0:
        old=next(z for z in json.loads((BASE/"c79_offset_profile.json").read_text()) if z["c"]==c)
        assert (low,high,xc*yc)==(old["min_unique"],old["max_unique"],old["translation_rectangles"])
        result["c79_extrema_verified"]=True
    return result

if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("stocks",nargs="+",type=int)
    p.add_argument("--offset",type=int,default=0)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    rows=[]
    for c in args.stocks:
        rows.append(extrema(c,args.offset))
        print(json.dumps(rows[-1]),flush=True)
        args.output.write_text(json.dumps(rows,indent=2)+"\n")
