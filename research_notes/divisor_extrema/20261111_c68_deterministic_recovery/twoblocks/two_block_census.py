"""Compile and verify the finite two-block H(0,1) certificate, including the high-stock junction."""
import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from tempfile import TemporaryDirectory
from stock_shift import block,points,words

PRIME=2**61-1


def mod(x):
    return (x.numerator%PRIME)*pow(x.denominator,-1,PRIME)%PRIME


def certificate(rows,limit):
    assert len(rows)==limit-1
    native=0
    for c,line in enumerate(rows,2):
        stock,n,low,high=map(int,line.split())
        assert (stock,n)==(c,comb(c,2)) and 0<=low<=high<PRIME
        if c<=24:
            signatures=[]
            for path in words(2,c):
                z=points(2,c,path)
                h=max(z)/min(z)
                signatures.append(mod(h+1/h))
            signatures.sort()
            assert len(set(signatures))==n and (low,high)==(signatures[0],signatures[-1])
            native+=n
    example=(2,8,(1,2,3))
    hpoints=points(*example)
    val=max(hpoints)/min(hpoints)
    V=1024
    c=V
    rho,tau=block(2,c,0)
    while rho>=1 or 4*tau/rho>=Q(15,5+4*V):
        c+=1
        rho*=Q(5+4*c,4*(5+c))
        tau*=Q(5+4*c,4*(20+c))
    assert c==2249 and limit>=c
    return dict(depth=2,stocks=[2,limit],total_by_stock=comb(limit+1,3),
                largest_family=comb(limit,2),prime=PRIME,colliding_within_family=0,
                exact_fraction_replays=native,finite_last=[int(x) for x in rows[-1].split()],
                finite_rows_sha256=hashlib.sha256(('\n'.join(rows)+'\n').encode()).hexdigest(),
                infinite_junction=dict(c_from=c,landing_stock_up_to=V),
                sample=dict(r=example[0],c=example[1],word=example[2],H=str(val)))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--limit',type=int,default=2249)
    p.add_argument('--read-rows',type=Path,help='use rows from a separate complete C++ run')
    args=p.parse_args()
    if args.read_rows:rows=args.read_rows.read_text().splitlines()
    else:
        with TemporaryDirectory() as d:
            exe=Path(d)/'two_block'
            subprocess.run(['g++','-O3','-std=c++17',str(Path(__file__).with_suffix('.cpp')),'-o',str(exe)],check=True)
            rows=subprocess.run([str(exe),str(args.limit)],capture_output=True,text=True,check=True).stdout.splitlines()
    print(json.dumps(certificate(rows,args.limit),indent=2))
