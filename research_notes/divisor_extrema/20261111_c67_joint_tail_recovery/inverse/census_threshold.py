"""Conservatively classify exact H above/below the maximum from size 17 onward."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
def run(args):
    sys.path[:0]=[str(args.checks.resolve()),str(args.inherited.resolve())]
    from observed_four import tail_forms
    from certify_schedules import block_maps
    from upper_frontier import terminal_forms
    table=json.loads(args.frontier.read_text())
    D=Q(table['records'][15]['H_minus_one_exact'])
    inp=[f'{args.limit} {float(D)!r}']
    min_t=Q(1)
    path_min={(0,c):(Q(1),Q(1)) for c in range(2,args.limit+2)}
    def to_line(vals):
        assert all(x>0 and x<=1 for x in vals)
        # Check the exact value represented by the ASCII decimal after parsing.
        for q in vals:assert abs(Q(float(q))/q-1)<=Q(1,2**52)
        return ' '.join(repr(float(x)) for x in vals)
    for c in range(2,args.limit+2):
        (p,q)=terminal_forms(c,tail_forms).columns
        p0,p1=[Q(x,max(p)) for x in p];q0,q1=[Q(x,max(q)) for x in q]
        values=[p1,p0,q1,q0,p1*q0-p0*q1]
        min_t=min(min_t,*values)
        inp.append(to_line(values))
    for r in range(1,args.limit):
        for c in range(2,args.limit+2):
            floors=[]
            for m,(a,b,h) in enumerate(block_maps(r,c)):
                a,b,h=[Q(x,max(a,b,h)) for x in [a,b,h]]
                det=a*abs(h-b)
                child,cdet=path_min[r-1,c-m]
                floors.append((child*min(a,b,h),cdet*det))
                inp.append(to_line([a,b,h,det])+f' {int(b>h)}')
            path_min[r,c]=tuple(map(min,zip(*floors)))
    # Every nonzero coordinate at depth s is at least min_e**s, and 2**s
    # is an upper bound. During a positive dot product each nonzero summand
    # meets the same bound with one additional coefficient.
    min_coeff,min_det=map(min,zip(*path_min.values()))
    lower=min(min_t**2*min_coeff**2*D,min_t*min_det)
    assert lower>Q(2)**(-990)
    assert 2**(2*args.limit+5)<2**990
    assert abs(Q(float(D))/D-1)<=Q(1,2**52)
    with TemporaryDirectory() as temp:
        exe=Path(temp)/'count'
        subprocess.run(['g++','-std=c++17','-O3','-ffp-contract=off','-fno-fast-math',str(Path(__file__).with_suffix('.cpp')),'-o',str(exe)],check=True)
        proc=subprocess.run([str(exe)],input='\n'.join(inp)+'\n',text=True,capture_output=True,check=True)
    rows=[]
    for line in proc.stdout.splitlines():
        k,a,b,n=map(int,line.split())
        assert a+b+n==comb(2*k-1,k) and n==0
        rows.append(dict(k=k,above=a,below=b,undecided=n))
    direct=json.loads(args.direct.read_text())['size_breakdown']
    assert all(rows[z['k']-2]['above']==z['above'] for z in direct if z['k']<=args.limit)
    return dict(threshold_H_minus_one=str(D),certified_above=sum(x['above'] for x in rows),
                native_words=sum(x['above']+x['below'] for x in rows),undecided=0,
                compared_to_full_exact_rational_enumeration_through_k=direct[-1]['k'],
                lower_bound_exceeds_2_to_minus_990=True,rows=rows)
if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--frontier',type=Path,required=True)
    p.add_argument('--direct',type=Path,required=True)
    p.add_argument('--limit',type=int,default=16)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    assert 2<=args.limit<=16
    args.output.write_text(json.dumps(run(args),indent=2)+'\n')
