"""Certified prefix pruning for original exact three-tail readouts."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb, isqrt
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys

SCALE=2**80
BINS=8
LOG_BASE=16
PRIME=2**61-1


def floor_log_scaled(num,den):
    """Exact floor of LOG_BASE·log2(num/den)."""
    n,d=num**LOG_BASE,den**LOG_BASE
    gap=n.bit_length()-d.bit_length()
    if gap>=0: return gap-int(n<d<<gap)
    return gap-int((n<<(-gap))<d)


def ceiling_for_threshold(threshold):
    # log H < 12·5^(-k/2). threshold is a positive lower bound on log h.
    k=2
    while threshold**2 * 5**k < 144: k+=1
    return k-1


def envelopes(ceiling,select_until,threshold,terminal,maps):
    n=BINS
    tables,starts,bounds={}, {}, {}
    prev={}
    for c in range(2,ceiling+2):
        rows=sorted(terminal(c),key=lambda row:row[0]/row[1])
        (a,b),(d,e)=rows[0],rows[-1]
        det=abs(a*e-b*d)
        prev[c]=[]
        for i in range(n+1):
            y=SCALE**2*(a*i+b*n)*(d*i+e*n)/(n**2*det)
            prev[c].append(isqrt(y.numerator//y.denominator))
        assert min(prev[c])>0
    for r in range(1,ceiling):
        cur={}
        for c in range(2,ceiling+2):
            edges=list(maps(r,c))
            vals=[]
            for m,(a,b,h) in enumerate(edges):
                child=prev[c-m]
                det_n2=n*n*a*abs(b-h)
                col=[]
                for i in range(n+1):
                    den=n*a+(n-i)*h+i*b
                    j,z=divmod(n*n*a,den)
                    assert 0<=j<n
                    weighted=(den-z)*child[j]+z*child[j+1]
                    col.append(isqrt(weighted*weighted//det_n2))
                vals.append(col)
            nodes=cur[c]=[min(v) for v in zip(*vals)]
            assert min(nodes)>0
            if r<select_until and c<=select_until+1:
                penalized=[]
                for (a,b,h),col in zip(edges,vals):
                    z=min(range(n+1),key=lambda i: Q(col[i],nodes[i]))
                    cost=floor_log_scaled(col[z]**2,nodes[z]**2)
                    assert cost>=0
                    penalized.append((a%PRIME,(b-h)%PRIME,(a+h)%PRIME,int(b>h),cost))
                tables[r,c]=penalized
        k=r+1
        upper={c:sum(Q(SCALE**2,n*x*y) for x,y in zip(cur[c],cur[c][1:]))
               for c in range(2,k+2)}
        bounds[k]=max(upper.values())
        if k<=select_until:
            starts[k]=[floor_log_scaled(v.numerator*threshold.denominator,
                                        v.denominator*threshold.numerator) for v in upper.values()]
        prev=cur
    return tables,starts,bounds


def scalar(k,gaps,block,terminal):
    x,y=(0,1),(1,1)
    c=k+1-gaps[0]
    for r,m in zip(range(k-1,0,-1),gaps[1:]):
        a,b,z,d=block(r,c,m)
        x=(b*x[1],z*x[0]+d*x[1])
        y=(b*y[1],z*y[0]+d*y[1])
        c-=m
    (a,b),(g,h)=terminal(c)
    value=Q((a*x[0]+b*x[1])*(g*y[0]+h*y[1]),(a*y[0]+b*y[1])*(g*x[0]+h*x[1]))
    return max(value,1/value)


def to_field(v):
    return v.numerator*pow(v.denominator,-1,PRIME)%PRIME


def run(args):
    sys.path[:0]=[str(args.checks.resolve()),str(args.inherited.resolve())]
    from suffix_limits import all_gaps,block
    from observed_four import tail_forms
    from certify_schedules import block_maps
    if args.small<2 or args.small>16: raise ValueError('small must lie in 2..16')
    @lru_cache(None)
    def terminal(c):
        rows=sorted(tail_forms(c),key=lambda row:row[0]/row[1])
        return rows[0],rows[-1]
    blk=lru_cache(None)(block)
    all_h=sorted(scalar(k,path,blk,terminal) for k in range(2,args.small+1) for path in all_gaps(k))
    assert len(all_h)==len(set(all_h))
    threshold=1-1/all_h[0]
    ceiling=ceiling_for_threshold(threshold)
    last=min(ceiling,args.max_scan)
    table,starts,bounds=envelopes(ceiling,last,threshold,terminal,block_maps)
    included=[k for k in range(17,ceiling+1) if bounds[k]>=threshold]
    assert all(k<=last for k in included), ('increase --max-scan', included)
    targets=sorted(set(map(to_field,all_h)))
    assert len(targets)==len(all_h)
    inp=[str(last)]
    for c in range(2,last+2):
        lo,hi=terminal(c)
        inp.append(' '.join(str(to_field(v)) for v in (*hi,*lo)))
    for r in range(1,last):
        for c in range(2,last+2):
            inp.extend(' '.join(map(str,e)) for e in table[r,c])
    inp.append(str(len(targets)))
    inp.extend(map(str,targets))
    check_k=min(args.small,6)
    for k in [check_k]+included:
        inp.append(f"{k} {int(k<=check_k)} "+' '.join(str(x) for x in starts[k]))
    with TemporaryDirectory() as temp:
        exe=Path(temp)/'bounded'
        subprocess.run(['g++','-std=c++17','-O3',str(Path(__file__).with_suffix('.cpp')),'-o',str(exe)],check=True)
        result=subprocess.run([str(exe)],input='\n'.join(inp)+'\n',text=True,capture_output=True,check=True)
    rows=[dict(zip(('k','visited_prefixes','retained_leaves','hits'),map(int,row.split()))) for row in result.stdout.splitlines()]
    assert rows[0]['hits']==rows[0]['retained_leaves']==comb(2*check_k-1,check_k)
    assert all(t['hits']==0 for t in rows[1:]),rows
    return dict(small_through=args.small,targets=len(all_h),smallest_H=str(all_h[0]),
                threshold_log_lower=str(threshold),analytic_ceiling=ceiling,global_higher_scale_candidates=included,
                largest_higher_scale_log_H_upper=str(bounds[17]),maximizers_at_or_above_17=[k for k in range(17,ceiling+1) if bounds[k]==max(bounds[j] for j in range(17,ceiling+1))],
                grid_bins=BINS,integer_scale_bits=80,log_units_per_bit=LOG_BASE,
                tested=rows,modular_prime=PRIME,complete_candidate_family_size=sum(comb(2*k-1,k) for k in included),
                previous_census_families='all words, k=2,...,16 (C66)')


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--small',type=int,default=8)
    p.add_argument('--max-scan',type=int,default=24)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    args.output.write_text(json.dumps(run(args),indent=2)+'\n')
