"""Rebuild modular tests and compare all small entries with original three-state joint masses."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

PRIME=2**61-1

def reduce_value(x):
    return x.numerator*pow(x.denominator,-1,PRIME)%PRIME

def main(prior, cap):
    sys.path.insert(0,str(prior.resolve()))
    from mixed_kernel import responses
    controls=0
    with TemporaryDirectory() as directory:
        exe=Path(directory)/'last_block'
        src=Path(__file__).with_name('last_block.cpp')
        subprocess.run(['g++','-O3','-std=c++17',str(src),'-o',str(exe)],check=True)
        raw=subprocess.check_output([str(exe),'28','dump'],text=True)
        for line in raw.splitlines():
            c,v,*results=map(int,line.split())
            rows,_=responses(1,c,(c-v,v-2))
            z=[(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j]) for j in (3,4,5)]
            h=max(z)/min(z)
            assert results==[reduce_value(x) for x in [*z,h+1/h]]
            controls+=1
        summary=list(map(int,subprocess.check_output([str(exe),str(cap)],text=True).split()))
    assert summary==[cap,cap*(cap-1)//2,3*cap*(cap-1)//2]
    return dict(prime=PRIME,limit=cap,stocks=cap-1,words=summary[1],anonymous_columns=summary[2],
                scalar_H_signatures=summary[1],maximum_control_stock=28,native_words=controls,native_columns=3*controls)

if __name__=='__main__':
    opts=argparse.ArgumentParser(description=__doc__)
    opts.add_argument('--prior',required=True,type=Path)
    opts.add_argument('--cap',type=int,default=8192)
    args=opts.parse_args()
    print(json.dumps(main(args.prior,args.cap),indent=2))
