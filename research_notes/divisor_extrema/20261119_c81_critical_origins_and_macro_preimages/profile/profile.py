"""Certified averages over all translations of the adjacent physical C79 grids.

Build: g++ -O3 -std=c++17 -o sweep sweep.cpp
Run: python profile.py 8 16 24 32 48 64 96 128 256 --output results.json
Use --scale continuum for exactly 2^t*c^(9/4) relative resolution; the default
uses physical integer p=floor((9/4)log2(c))+t. Requires adjacent critical_bins.py.
"""
from argparse import ArgumentParser
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
import subprocess
import tempfile

import critical_bins as C

BASE = Path(__file__).resolve().parent
UNIT = 1 << 40
D = C.UNIT

def physical_pairs(c):
    C.prepare(c+1)
    C.terminal.cache_clear()
    for v in range(2,c+1):
        for w in range(2,v+1):
            middle=C.block(v,w,3,C.terminal(w))
            yield [C.full_width(n,v,middle) for n in (c,c+1)]

def multiplier(c,base,offset,scale):
    if scale=="bits":
        p=base+offset
        if p<0: raise ValueError("nonnegative precision required")
        return D<<p,D<<p
    # floor(c^(9/4)2^BITS) by exact nested integer square roots.
    a=isqrt(isqrt((c**9)<<(4*C.BITS)))
    hi=a+int(a**4!=((c**9)<<(4*C.BITS)))
    if offset>=0: return a<<offset,hi<<offset
    den=1<<(-offset)
    return a//den,-((-hi)//den)

def approximate(iv,scale):
    # Subtracting the common 1 is one translation and leaves all averages
    # and separations invariant. Guaranteed coordinate error <= 1/UNIT.
    a,b=iv
    if a<D: raise ValueError("negative lower bound after centering")
    lo=(a-D)*scale[0]*UNIT
    hi=(b-D)*scale[1]*UNIT
    den=D*D
    k=(lo+den//2)//den
    assert (k-1)*den<=lo<=hi<=(k+1)*den
    if not (abs(k)+4*UNIT<1<<61): raise ValueError("64-bit sweep range")
    return k

def interval(num,den,radius):
    # Output integer brackets in units of 1e-10 with outward rounding.
    return [max(0,(num-radius)*10**10//den),
            min(10**10,-((-(num+radius)*10**10)//den))]

def summarize(c,scale,offset):
    n=c*(c-1)//2
    base=((c**9).bit_length()-1)//4
    mult=multiplier(c,base,offset,scale)
    with tempfile.TemporaryFile(mode="w+") as fp:
        print(n,UNIT,1,file=fp)
        for vals in physical_pairs(c):
            print(*(approximate(iv,mult) for iv in vals),file=fp)
        fp.seek(0)
        out=subprocess.check_output([str(BASE/"sweep")],stdin=fp,text=True)
    single,occupied,double,robust_lo,robust_hi=map(int,out.split())
    den=n*UNIT*UNIT
    radius=4*n*UNIT  # bound on integrated indicators per moved square
    result=dict(c=c,templates=n,scale=scale,t=offset,
                mean_unique_1e10=interval(single,den,radius),
                best_decoding_1e10=interval(occupied,den,radius),
                exactly_two_arrangements_1e10=interval(2*double,den,2*radius),
                robust_count=[robust_lo,robust_hi])
    if scale=="bits": result['p']=base+offset
    if scale=="bits" and offset==0 and c in (8,16,24):
        old=next(z for z in json.loads((BASE/"c79_offset_profile.json").read_text()) if z["c"]==c)
        a,b=result["mean_unique_1e10"]
        assert a>=100*old["mean_unique_rate_times_1e8_floor"] and b<=100*old["mean_unique_rate_times_1e8_ceil"]
        result["c79_small_bracket_verified"]=True
    return result

if __name__=="__main__":
    p=ArgumentParser(description=__doc__)
    p.add_argument("stocks",nargs="+",type=int)
    p.add_argument("--offset",type=int,default=0)
    p.add_argument("--scale",choices=("bits","continuum"),default="bits")
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    rows=[]
    for c in args.stocks:
        rows.append(summarize(c,args.scale,args.offset))
        print(json.dumps(rows[-1],ensure_ascii=False),flush=True)
        args.output.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n")
