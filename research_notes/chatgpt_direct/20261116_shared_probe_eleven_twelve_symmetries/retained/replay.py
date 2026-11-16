"""Free six classes of the eleven-label witness, or merge six from the twelve-label witness."""
import argparse,json,sys,subprocess
from pathlib import Path
from itertools import combinations
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor

def verify(last,work,workers):
    prev=last/'previous'
    sys.path.insert(0,str(prev/'bounds'))
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    _,obs=observations()
    observation_file(work/'obs')
    f=prev/'native/eleven.txt'
    labels=list(map(int,f.read_text().split()))
    tables={'old':[[i for i,t in enumerate(labels)if t==j]for j in range(11)],
            'bridge':json.loads((last/'twelve/groups.json').read_text())}
    out={}
    exe=work/'search';subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(last/'twelve/neighborhood.cpp'),'-o',str(exe)],check=True)
    for name,rows in tables.items():
        choices=list(combinations(range(len(rows)),6)); allowed=6 if name=='old' else 5
        tasks=[];costs=[class_cost(g,obs)for g in rows]
        for ids in choices:
            m=sum(1<<p for i in ids for p in rows[i])
            if m.bit_count()<=13*allowed:tasks.append([m%(1<<64),m>>64,allowed,sum(costs)-sum(costs[i]for i in ids),*ids])
        path=work/'tasks';path.write_text(''.join(' '.join(map(str,t))+'\n'for t in tasks))
        def test(i):
            end=min(i+18,len(tasks))
            s=subprocess.check_output([str(exe),str(work/'obs'),str(path),str(i),str(end),'11291'],text=True)
            data=[list(map(int,l.split()))for l in s.splitlines()]
            assert [r[0]for r in data]==list(range(i,end))and all(len(r)==3 and r[2]==0 for r in data)
            return sum(r[1]for r in data)
        with ThreadPoolExecutor(max_workers=workers)as pool:visits=sum(pool.map(test,range(0,len(tasks),18)))
        out[name]=dict(choices=len(choices),admitted=len(tasks),nodes=visits,feasible_at_11291=False)
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--last',type=Path,required=True);p.add_argument('--jobs',type=int,default=3)
    with TemporaryDirectory()as tmp:
        args=p.parse_args();print(json.dumps(verify(args.last.resolve(),Path(tmp),args.jobs),sort_keys=True))
