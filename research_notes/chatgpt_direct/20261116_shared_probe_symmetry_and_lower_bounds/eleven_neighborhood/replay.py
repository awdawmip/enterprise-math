"""Exhaust all five-class replacements in the 11,292 witness."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import json,subprocess,sys
HERE=Path(__file__).resolve().parent
def run(previous,work):
    sys.path.insert(0,str(previous/'bounds'))
    from prior_bounds import observation_file
    from cyclic11 import class_cost,observations
    bad,menus=observations()
    lab=list(map(int,(previous/'native/eleven.txt').read_text().split()))
    table=[[p for p,c in enumerate(lab)if c==k]for k in range(11)]
    prices=[class_cost(g,menus)for g in table];assert sum(prices)==11292
    tasks=[]
    for ids in combinations(range(11),5):
        union=sum(1<<p for i in ids for p in table[i])
        tasks.append([union%2**64,union>>64,5,11292-sum(prices[i]for i in ids),*ids])
    assert len(tasks)==462
    (work/'jobs').write_text(''.join(' '.join(map(str,j))+'\n'for j in tasks))
    observation_file(work/'input')
    subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',str(HERE.parent/'twelve/neighborhood.cpp'),'-o',str(work/'run')],check=True)
    def check(i):
        end=min(i+18,len(tasks))
        text=subprocess.check_output([str(work/'run'),str(work/'input'),str(work/'jobs'),str(i),str(end),'11291'],text=True)
        rows=[list(map(int,s.split()))for s in text.splitlines()]
        assert [r[0]for r in rows]==list(range(i,end)) and all(len(r)==3 and r[2]==0 for r in rows)
        return sum(r[1] for r in rows)
    with ThreadPoolExecutor(max_workers=2)as pool:nodes=sum(pool.map(check,range(0,len(tasks),18)))
    return dict(released_sets=len(tasks),nodes=nodes,minimum=11292)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',required=True,type=Path)
    with TemporaryDirectory()as temp:print(json.dumps(run(p.parse_args().older.resolve(),Path(temp)),sort_keys=True))
