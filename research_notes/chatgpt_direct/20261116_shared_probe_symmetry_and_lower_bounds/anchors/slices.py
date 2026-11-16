"""Verify the second cost-8717 split using exact counts on all 15 coordinate slices."""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import json,subprocess
from replay import HERE, bank, maps, LOW_MASK
from extra_triples import pair_orbits

def verify(work):
    lin,trans,_=maps()
    group=[bytes(t[i]for i in g)for g in lin for t in trans]
    rows=bank(work,lin,trans,8728)
    pairs=[pair for pair,st in pair_orbits(rows,group,(12,1104),(12,1104))]
    assert len(pairs)==6
    target=[(9,557),(10,744),(10,752)]
    with (work/'rows').open('w')as stream:
        print(len(target),file=stream)
        for size,cost in target:
            masks=rows[size,cost]
            print(size,cost,len(masks),file=stream)
            for m in masks:print(m&LOW_MASK,m>>64,file=stream)
    (work/'pairs').write_text(''.join(' '.join(str(i)for m in ab for i in(m&LOW_MASK,m>>64))+'\n'for ab in pairs))
    exe=work/'slices'
    subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/'slices.cpp'),'-o',str(exe)],check=True)
    def check(i):
        raw=subprocess.check_output([str(exe),str(work/'rows'),str(work/'pairs'),'752',str(i)],text=True,cwd=work)
        ix,price,size,nodes,found=map(int,raw.split())
        assert ix==i and price==752 and found==0
        return nodes
    with ThreadPoolExecutor(max_workers=3) as pool:
        ns=list(pool.map(check,range(len(pairs))))
    return {'cost':8717,'search_nodes_by_pair':ns,'solutions':0}

if __name__=='__main__':
    with TemporaryDirectory()as t:
        print(json.dumps(verify(Path(t)),sort_keys=True,indent=2))
