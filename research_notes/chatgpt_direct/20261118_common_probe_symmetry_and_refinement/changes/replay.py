"""Verify the least number of old classes that must change between neighboring optimal budgets."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse, json, sys

HERE=Path(__file__).resolve().parent

def solve(previous):
    second=previous/'previous/previous/previous'
    sys.path[:0]=[str(second/'bounds'),str(second/'curve')]
    from cyclic11 import class_cost,observations
    from verify import cheap_line_partitions,MINIMA,lower
    bad,obs=observations()
    def canon(rs):return {tuple(sorted(r))for r in rs}
    def check(rows,k):
        assert len(rows)==k and sorted(x for r in rows for x in r)==list(range(125))
        assert not any(bad[x][y]>>z&1 for r in rows for x,y,z in combinations(r,3))
        assert sum(class_cost(r,obs)for r in rows)==lower(125,k)
    def profile(m):
        a,b=divmod(125,m)
        return Counter({s:n for s,n in ((a,m-b),(a+1,b))if n})
    # Test that each individual size in an optimal table belongs to the balanced support.
    # Point count and number of classes then uniquely give its multiplicities.
    for k in range(21,126):
        assert all(s in profile(k) for s in range(1,14)if MINIMA[s]+lower(125-s,k-1)==lower(125,k))
    certificates=json.loads((HERE/'replacements.json').read_text())
    stats={}
    for k in range(21,125):
        if k<=24:
            old=cheap_line_partitions(k)
            new=cheap_line_partitions(k+1)
        elif k<=62:
            proof=certificates[str(k)]
            old_first=proof['basis']=='coarse'
            base=cheap_line_partitions(k if old_first else k+1)
            drop=set(proof['remove'])
            formed=[r for j,r in enumerate(base)if j not in drop]+proof['replacement']
            old,new=(base,formed)if old_first else(formed,base)
        else:
            old=cheap_line_partitions(k)
            j=next(i for i,r in enumerate(old)if len(r)==2)
            new=[r for i,r in enumerate(old)if i!=j]+[[p]for p in old[j]]
        check(old,k);check(new,k+1)
        changed=k-len(canon(old)&canon(new))
        bound=sum((profile(k)-profile(k+1)).values())
        assert changed==bound
        stats[k]=changed
    return stats

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',required=True,type=Path)
    print(json.dumps(solve(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
