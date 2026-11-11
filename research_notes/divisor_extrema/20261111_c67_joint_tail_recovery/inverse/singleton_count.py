"""Count provably singleton native readouts by conservative integer logarithms."""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from math import comb
import json
import sys
BITS=32
N=64
def logfloor(x):
    a,b=x.numerator**BITS,x.denominator**BITS
    n=a.bit_length()-b.bit_length()
    return n-int(a<b<<n) if n>=0 else n-int(a<<(-n)<b)

def run(args):
    sys.path[:0]=[str(args.checks.resolve()),str(args.inherited.resolve())]
    from observed_four import tail_forms
    from certify_schedules import block_maps
    data=json.loads(args.frontier.read_text())
    threshold=Q(data['records'][15]['H_minus_one_exact'])
    lo=logfloor(threshold)+1
    @lru_cache(None)
    def tail(c, left,right):
        rows=sorted(tail_forms(c),key=lambda row:row[0]/row[1])
        (p0,q0),(p1,q1)=rows[0],rows[-1]
        assert p1*q0-p0*q1>0
        pmax=max(p0*left/N+q0,p0*right/N+q0)
        qmax=max(p1*left/N+q1,p1*right/N+q1)
        return logfloor((p1*q0-p0*q1)/(pmax*qmax))
    @lru_cache(None)
    def maps(r,c):return tuple(block_maps(r,c))
    @lru_cache(None)
    def transition(r,c,m,left,right):
        a,b,h=maps(r,c)[m]
        dl=N*(a+h)+(b-h)*left
        dr=N*(a+h)+(b-h)*right
        low_d,high_d=sorted((dl,dr))
        # a*N is the common numerator of both output endpoints; outward grid.
        lnew=a*N*N//high_d
        rnew=-(-a*N*N//low_d)
        cost=logfloor(Q(a*abs(b-h)*N*N,high_d*high_d))
        return lnew,rnew,cost
    @lru_cache(None)
    def count(r,c,left,right,score):
        if not r:return int(score+tail(c,left,right)>=lo)
        return sum(count(r-1,c-m,lnew,rnew,score+cost)
                   for m in range(c-1)
                   for lnew,rnew,cost in (transition(r,c,m,left,right),))
    rows=[]
    for k in range(2,args.limit+1):
        qualifying=sum(count(k-1,k+1-first,0,N,0) for first in range(k))
        rows.append(dict(k=k,qualifying=qualifying,all=comb(2*k-1,k)))
        print(k,qualifying,flush=True,file=sys.stderr)
    return dict(certified_singletons=sum(v['qualifying'] for v in rows),
                compared_against='maximum H across k>=17; C66 proved all values with 2<=k<=16 distinct',
                threshold_H_minus_one=str(threshold),cells=N,log_units_per_bit=BITS,
                integer_threshold=lo,rows=rows)
if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--frontier',type=Path,required=True)
    p.add_argument('--limit',type=int,default=16)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    assert 2<=args.limit<=16
    args.output.write_text(json.dumps(run(args),indent=2)+'\n')
