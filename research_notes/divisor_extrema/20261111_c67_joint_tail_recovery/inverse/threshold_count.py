"""Exact direct enumeration of globally unique native readouts above a rational cutoff."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from math import comb
import json
import sys

def run(args):
    sys.path[:0]=[str(args.checks.resolve()),str(args.inherited.resolve())]
    from suffix_limits import all_gaps,block
    from observed_four import tail_forms
    from inverse_grid import scalar
    table=json.loads(args.frontier.read_text())
    mx=1+Q(table['records'][15]['H_minus_one_exact'])
    assert table['records'][15]['k']==17
    for row in table['records'][16:]:
        a,b,e=row['H_minus_one_enclosed']
        assert b*Q(10)**e<mx-1
    assert 144<(1-1/mx)**2*5**(table['up_to']+1)
    @lru_cache(None)
    def terminal(c):
        rows=sorted(tail_forms(c),key=lambda row:row[0]/row[1])
        return rows[0],rows[-1]
    blk=lru_cache(None)(block)
    rows=[]
    for k in range(2,args.limit+1):
        count,above,maxval,winners=0,0,1,[]
        for gap in all_gaps(k):
            h=scalar(k,gap,blk,terminal)
            count+=1;above+=int(h>mx)
            if h>maxval:maxval,winners=h,[gap]
            elif h==maxval:winners.append(gap)
        target=table['records'][k-2]
        assert winners==[tuple(target['gaps'])] or winners==[target['gaps']]
        assert count==comb(2*k-1,k)
        if 'H_minus_one_exact' in target:assert maxval-1==Q(target['H_minus_one_exact'])
        else:
            a,b,e=target['H_minus_one_enclosed']
            assert a*Q(10)**e<=maxval-1<=b*Q(10)**e
        rows.append(dict(k=k,all=count,above=above,maximum_matches_frontier=True))
        print(k,above,count,file=sys.stderr,flush=True)
    return dict(largest_H_at_k_ge_17=str(mx),previous_census_unique_through=16,
                total_above=sum(x['above'] for x in rows),size_breakdown=rows)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--frontier',type=Path,required=True)
    p.add_argument('--limit',type=int,default=10)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    args.output.write_text(json.dumps(run(args),indent=2)+'\n')
