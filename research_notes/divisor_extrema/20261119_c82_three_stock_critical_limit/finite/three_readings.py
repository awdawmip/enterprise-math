"""Certified physical bins for c, c+sqrt(c), c+2sqrt(c) at L=1."""
from argparse import ArgumentParser
from itertools import product
from math import isqrt
from pathlib import Path
import json

import numpy as np
import critical_bins as C
from native import native_tail_ratios

def singles(keys):
    _,counts=np.unique(keys,axis=0,return_counts=True)
    return int(np.count_nonzero(counts==1))

def calculate(c):
    b=isqrt(c)
    assert b*b==c and c&(c-1)==0
    p=2*(c.bit_length()-1)
    stocks=[c,c+b,c+2*b]
    C.prepare(stocks[-1])
    C.terminal.cache_clear()
    rows=[]
    native=0
    for v in range(2,c+1):
        for w in range(2,v+1):
            middle=C.block(v,w,3,C.terminal(w))
            values=[C.full_width(n,v,middle) for n in stocks]
            if c<=16:
                for n,(lo,hi) in zip(stocks,values):
                    tail=native_tail_ratios(n,v,w)
                    exact=max(tail)/min(tail)
                    assert lo<=exact*C.UNIT<=hi
                    native+=1
            # Half-grid events suffice for all eight origin configurations.
            bins=[C.bin_number(value,p+1,(0,1))-(1<<(p+1))
                  for value in values]
            rows.append(bins)
    table=np.array(rows,dtype=np.int64)
    records=[]
    for origin in product(range(2),repeat=3):
        keys=(table+np.array(origin))//2
        records.append({'offsets_halves':list(origin),
                        'pair_0_1':singles(keys[:,:2]),
                        'pair_0_2':singles(keys[:,[0,2]]),
                        'triple':singles(keys)})
    return {'c':c,'b':b,'p':p,'L':1,'n':len(rows),'native_enclosures':native,
            'interval_bits':C.BITS,'origins':records}

if __name__=='__main__':
    parser=ArgumentParser()
    parser.add_argument('c',nargs='+',type=int)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    results=[]
    for c in args.c:
        r=calculate(c)
        results.append(r)
        args.output.write_text(json.dumps(results,indent=2)+'\n')
        print(c,r['n'],[min(x['triple'] for x in r['origins']),
                         max(x['triple'] for x in r['origins'])],flush=True)
