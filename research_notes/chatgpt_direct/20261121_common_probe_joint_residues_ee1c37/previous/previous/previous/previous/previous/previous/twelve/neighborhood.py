"""Prove no strict improvement of the 10,147-read table keeps eight of its twelve classes."""
from pathlib import Path
from itertools import combinations
from tempfile import TemporaryDirectory
import argparse,json,sys,subprocess
HERE=Path(__file__).resolve().parent
def check(previous):
    sys.path.insert(0,str(previous/'bounds'))
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    lab=list(map(int,(previous/'bounds/twelve_10147.txt').read_text().split()))
    assert len(lab)==125 and set(lab)==set(range(12))
    rows=[[p for p,i in enumerate(lab) if i==j]for j in range(12)]
    _,menus=observations()
    prices=[class_cost(row,menus)for row in rows]
    assert sum(prices)==10147
    with TemporaryDirectory()as directory:
        tmp=Path(directory)
        observation_file(tmp/'obs')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(HERE/'neighborhood.cpp'),'-o',str(tmp/'check')],check=True)
        jobs=list(combinations(range(12),4))
        with (tmp/'jobs').open('w')as f:
            for replace in jobs:
                m=sum(1<<p for i in replace for p in rows[i])
                print(m%2**64,m>>64,4,10147-sum(prices[i]for i in replace),file=f)
        result=subprocess.check_output([str(tmp/'check'),str(tmp/'obs'),str(tmp/'jobs'),'0',str(len(jobs)),'10146'],text=True)
        lines=[tuple(map(int,l.split()))for l in result.splitlines()]
        assert [i for i,_,_ in lines]==list(range(len(jobs)))
        assert all(found==0 for _,_,found in lines)
    return dict(released_sets=len(jobs),nodes=sum(n for _,n,_ in lines),minimum=10147)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);a=p.parse_args()
    print(json.dumps(check(a.older.resolve()),sort_keys=True))
