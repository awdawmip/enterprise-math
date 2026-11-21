"""Search every alternative partition of up to five specified incumbent rows."""
import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
HERE = Path(__file__).resolve().parent

def solve(previous, workers):
    sys.path.insert(0,str(previous/'previous/previous/previous/bounds'))
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    rows=json.loads((previous/'c3/groups.json').read_text())
    _,menus=observations()
    price=[class_cost(r,menus) for r in rows]
    masks=[sum(1<<x for x in r) for r in rows]
    g=[25*(i//5%5)+5*(i%5)+i//25 for i in range(125)]
    act=[rows.index(sorted(g[x]for x in r))for r in rows]
    out={}
    with TemporaryDirectory() as name:
        w=Path(name)
        observation_file(w/'obs')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'different.cpp','-o',w/'search'],check=True)
        for k,cap in ((2,31250),(3,31250),(4,10500),(5,10131)):
            opts=[]
            for t in combinations(range(12),k):
                one=tuple(sorted(act[i] for i in t))
                two=tuple(sorted(act[i] for i in one))
                if t!=min(t,one,two):continue
                m=sum(masks[i] for i in t)
                opts.append([m%2**64,m>>64,k,9996-sum(price[i]for i in t),*[u for i in t for u in (masks[i]%2**64,masks[i]>>64)]])
            (w/'jobs').write_text(''.join(' '.join(map(str,r))+'\n'for r in opts))
            def run(i):
                text=subprocess.check_output([w/'search',w/'obs',w/'jobs',str(i),str(min(i+4,len(opts))),str(cap)],text=True)
                return [list(map(int,l.split()))for l in text.splitlines()]
            with ThreadPoolExecutor(workers) as pool:
                hits=[r for chunk in pool.map(run,range(0,len(opts),4))for r in chunk]
            assert [r[0]for r in hits]==list(range(len(opts))) and all(len(r)==3 and r[2]==0 for r in hits)
            out[str(k)]=dict(representatives=len(opts), budget=cap,nodes=sum(r[1]for r in hits), alternatives=0)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args()
    print(json.dumps(solve(a.previous.resolve(),a.jobs),indent=2,sort_keys=True))
