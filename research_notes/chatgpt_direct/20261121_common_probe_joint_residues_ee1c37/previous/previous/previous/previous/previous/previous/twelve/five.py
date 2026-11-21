"""Find the exact minimum in both five-class neighborhoods from original observations."""
from pathlib import Path
from itertools import combinations
from concurrent.futures import ThreadPoolExecutor
from tempfile import TemporaryDirectory
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent
def run(old,workers):
    sys.path.insert(0,str(old/'bounds'))
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    _,menus=observations()
    initial=list(map(int,(old/'bounds/twelve_10147.txt').read_text().split()))
    oldrows=[[p for p,i in enumerate(initial) if i==j]for j in range(12)]
    newrows=json.loads((HERE/'groups.json').read_text())
    results={}
    with TemporaryDirectory()as directory:
        tmp=Path(directory)
        observation_file(tmp/'obs')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(HERE/'neighborhood.cpp'),'-o',str(tmp/'search')],check=True)
        for rows in [oldrows,newrows]:
            prices=[class_cost(row,menus)for row in rows]
            source=sum(prices)
            kept={}
            with (tmp/'jobs').open('w')as f:
                for i,replace in enumerate(combinations(range(12),5)):
                    m=sum(1<<p for j in replace for p in rows[j])
                    kept[i]=replace
                    print(m%2**64,m>>64,5,source-sum(prices[j]for j in replace),file=f)
            def part(i):
                last=min(i+10,792)
                raw=subprocess.check_output([str(tmp/'search'),str(tmp/'obs'),str(tmp/'jobs'),str(i),str(last),str(source-1)],text=True)
                lines=[list(map(int,l.split()))for l in raw.splitlines()]
                assert [r[0]for r in lines]==list(range(i,last))
                return lines
            with ThreadPoolExecutor(max_workers=workers)as pool:
                lines=[r for block in pool.map(part,range(0,792,10))for r in block]
            improvements=[(list(kept[i]),p)for i,_,p,*_ in lines if p]
            results[str(source)]=dict(released_sets=len(lines),nodes=sum(r[1]for r in lines),
                                      improved_subsets=improvements,
                                      minimum=min([source]+[p for _,p in improvements]))
    return results
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--jobs',type=int,default=2)
    a=p.parse_args();print(json.dumps(run(a.older.resolve(),a.jobs),sort_keys=True))
