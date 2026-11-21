"""Rebuild four-maximum packings and check all integer dual/partition certificates."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import tempfile
from orbits import observations,packings,setbits
HERE=Path(__file__).resolve().parent

def check(k,target):
    weights=json.loads((HERE/f'weights{k}.json').read_text())
    bad,pair=observations()
    pointed,reps,orbits=packings(bad,k)
    assert len(weights)==len(orbits)
    with tempfile.TemporaryDirectory() as w:
        work=Path(w)
        exe=work/'check'
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',f'-DNMAX={k}',str(HERE/'partition_cost.cpp'),'-o',str(exe)],check=True)
        def one(it):
            row,g=it
            group=reps[g[0]]
            space=(1<<125)-1
            for m in group:
                space ^= m
            u=list(setbits(space))
            assert len(u)==125-13*k
            ix={x:i for i,x in enumerate(u)}
            src=work/f'obs{g[0]}'
            with src.open('wb') as f:
                for x in u:
                    for y in u:
                        h=sum(1<<ix[v] for v in setbits(bad[x][y]&space))
                        f.write(h.to_bytes(16,'little'))
                        f.write(pair[x][y].to_bytes(32,'little'))
            stdin=' '.join(map(str,[1000,row['peak']]+row['point_weights']))+'\n'
            p=subprocess.run([str(exe),str(src),str(target)],input=stdin,capture_output=True,text=True,check=True)
            allowance,saved,nodes,found=map(int,p.stdout.split())
            assert not found
            return dict(remaining_deficit=allowance,retained_classes=saved,search_nodes=nodes)
        with ThreadPoolExecutor(max_workers=3) as pool:
            checks=list(pool.map(one,zip(weights,orbits)))
    return dict(maximal_classes=k,budget=target,lower_bound=target+1,
                pointed=len(pointed),pointed_types=len(reps),affine_types=len(orbits),
                total_nodes=sum(d['search_nodes'] for d in checks),checks=checks)
if __name__=='__main__':
    print(json.dumps(check(4,11364),indent=2))
