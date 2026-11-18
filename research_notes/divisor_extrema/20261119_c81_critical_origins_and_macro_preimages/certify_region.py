"""Certify globally univalent cells using only integer/rational spectral bounds."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

import numpy as np

INF = 2**60
UNIT = 2**20

def spectral_key(value):
    """Monotone quantization of a positive rational, rounded down.
    
    Each dyadic magnitude interval is split into UNIT equal subintervals.
    Zero is a separate exact endpoint. Only order comparisons are used.
    """
    if value == 0:
        return -INF
    a, b = value.as_integer_ratio()
    power = a.bit_length() - b.bit_length()
    if power >= 0:
        b <<= power
    else:
        a <<= -power
    if a < b:
        power -= 1
        a *= 2
    return power * UNIT + a * UNIT // b

def h_value(a, d):
    m = F(7,16)*a**4*d
    return 1/(a-1)+5-4*m/(1+m)-5*m*a/(1+m*a)

def endpoints(a,A,d,D):
    # Each cell lies entirely on one side of both synchronization lines.
    al,ah=sorted([abs(a-1),abs(A-1)])
    dl,dh=sorted([abs(d-1),abs(D-1)])
    ml=F(7,16)*a**4*d
    mh=F(7,16)*A**4*D
    lo=a**57*d**70*(al*dl/((1+mh)*(1+mh*A)))**15
    hi=A**57*D**70*(ah*dh/((1+ml)*(1+ml*a)))**15
    # h decreases in both coordinates separately on either side of A=1.
    hl=-INF if A==1 else (h_value(A,D)*UNIT).__floor__()
    hh=INF if a==1 else (h_value(a,d)*UNIT).__ceil__()
    return hl,hh,spectral_key(lo),spectral_key(hi)

def calculate(n):
    assert n%4==0 and 4<=n<=2048
    nodes=[F(4*i,n) for i in range(n+1)]
    rows=[endpoints(nodes[i],nodes[i+1],nodes[j],nodes[j+1])
          for i in range(n) for j in range(n)]
    ext=np.array(rows,dtype=np.int64)
    certified=[]
    for left in [True,False]:
        # Above 9/8, every same-side lower-d competitor is also excluded
        # by monotone growth of G/|1-d| on each fixed-h curve.
        other_side=np.array([(i<n//4)!=left for i in range(n) for j in range(n)])
        below=np.tile(np.arange(n)<n//4,n)
        other=ext[other_side].T
        both=ext[other_side|below].T
        for i in range(0 if left else n//4,n//4 if left else n):
            for j in range(n//4,n):
                h0,h1,g0,g1=other if 32*j>=9*n else both
                l,h,v,w=rows[i*n+j]
                possible=(h0<=h)&(h1>=l)&(g0<=w)&(g1>=v)
                if not possible.any():
                    certified.append((i,j))
    # Parameter cells have product masses in A and d. Each powered endpoint
    # is enclosed by exact integer bisection with denominator 10^12.
    scale=10**12
    def dyadic_bound(i,num,den):
        lo,hi=0,scale+1
        while hi-lo>1:
            mid=(lo+hi)//2
            if mid**den*n**num<=scale**den*i**num:
                lo=mid
            else:
                hi=mid
        return lo
    packs=[[dyadic_bound(i,num,den) for i in range(n+1)]
           for num,den in [(8,15),(4,9)]]
    da,dd=[[b-a for a,b in zip(vals,vals[1:])] for vals in packs]
    lower=sum(max(0,da[i]-1)*max(0,dd[j]-1) for i,j in certified)
    upper=sum((da[i]+1)*(dd[j]+1) for i,j in certified)
    assert lower<=upper
    intervals=[]
    for i,j in certified:
        if intervals and intervals[-1][0]==i and intervals[-1][2]==j:
            intervals[-1][2]=j+1
        else:
            intervals.append([i,j,j+1])
    return {'n':n,'cells':len(certified),'mass_bounds_1e12':
            [lower//scale,-(-upper//scale)],'row_runs':intervals}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n',nargs='+',type=int)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    results=[]
    for n in args.n:
        result=calculate(n)
        print(n,result['cells'],result['mass_bounds_1e12'],flush=True)
        results.append(result)
        args.output.write_text(json.dumps(results,indent=1)+'\n')
