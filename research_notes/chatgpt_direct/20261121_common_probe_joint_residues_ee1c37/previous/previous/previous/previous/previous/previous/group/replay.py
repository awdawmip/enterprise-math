"""Rebuild affine symmetry and partial-orbit restrictions from the original class census."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import argparse,json,subprocess,tempfile
from generate import main as generate
from single_orbit import collect
from partial_orbits import make
from neighbors import prepare
from packet_floor import make as rotation
from isometry import verify as isometries

HERE=Path(__file__).resolve().parent

def solve(executable,work,rows,flags,output_index=-1):
    def one(i):
        proc=subprocess.run([str(executable),str(work),str(i),*flags],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,text=True)
        lines=[list(map(int,l.split()))for l in proc.stdout.splitlines()]
        assert all(v[-1]==0 for v in lines), (i,proc.stderr)
        return len(lines),sum(v[-2]for v in lines)
    with ThreadPoolExecutor(max_workers=2)as pool:
        verdict=list(pool.map(one,rows))
    return {'anchors':len(verdict),'profile_cases':sum(n for n,_ in verdict),'search_nodes':sum(s for _,s in verdict)}

def run(work,lengths=(3,),neighbors=(3,)):
    generate(work)
    syms=work/'symmetries'
    residual=work/'residual'
    for name,exe in [('orbits.cpp',syms),('one.cpp',residual)]:
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(HERE/name),'-o',str(exe)],check=True)
    perm=[list(map(int,l.split())) for l in (work/'maps').read_text().splitlines()]
    # Central inversion (order two, unique fixed point) has its separate counted certificate.
    ids=[i for i,(p,*g) in enumerate(perm)if p!=2 or sum(j==g[j]for j in range(125))!=1]
    assert len(ids)==10
    out={'pair_isometries':isometries(),'other_prime_symmetries':solve(syms,work,ids,[])}
    for k in lengths:
        n=make(work,k,8728)
        out[f'translated_{k}']=solve(residual,work,range(n),['8728',str(k)])
    for k in neighbors:
        prepare(work,k)
        n=len((work/f'neighbor{k}').read_text().splitlines())
        out[f'retain_{k}']=solve(residual,work,range(n),['8727',str(k),'anchor'])
    rotation(work)
    (work/'neighbor4_rot').replace(work/'neighbor4')
    n=len((work/'neighbor4').read_text().splitlines())
    out['rotation_orbit']=solve(residual,work,range(n),['8727','4','anchor'])
    return out

if __name__=='__main__':
    with tempfile.TemporaryDirectory()as tmp:
        print(json.dumps(run(Path(tmp)),sort_keys=True))
