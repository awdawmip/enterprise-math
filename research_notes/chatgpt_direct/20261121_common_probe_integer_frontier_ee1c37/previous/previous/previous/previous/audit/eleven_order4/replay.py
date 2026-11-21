"""Decide whether eleven labels can respect any quarter-turn squaring to a point inversion."""
import argparse,json,subprocess,sys
from pathlib import Path
from tempfile import TemporaryDirectory
from functools import cache
from helpers import fixed,paired
HERE=Path(__file__).resolve().parent

def verify(older,group,work):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(group)]
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    from verify import MINIMA
    from generate import maps
    native=work/'native';observation_file(native);bad,pair=observations()
    lin,_,_=maps();identity=bytes(range(125))
    neg=bytes(25*(-(i//25)%5)+5*(-(i//5%5)%5)+(-i%5) for i in range(125))
    compose=lambda a,b:bytes(a[i]for i in b)
    allowed={g for g in lin if compose(g,g)==neg};roots=[];orbit_sizes=[]
    while allowed:
        g=min(allowed);eq={compose(a,compose(s,bytes(a.index(i)for i in range(125))))for a in lin for s in (g,compose(g,neg))}
        assert eq<=allowed;allowed-=eq;roots.append(g);orbit_sizes.append(len(eq))
    for name,perms in [('linear',lin),('rot',roots)]:
        (work/name).write_text(''.join(' '.join(map(str,p))+'\n'for p in perms))
    singles=fixed(work,roots,bad,pair,class_cost);pairs=paired(work,roots,bad,pair,class_cost)
    for name in ('class_seeds','orbits','cover'):
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/(name+'.cpp')),'-o',str(work/name)],check=True)
    subprocess.run([str(work/'class_seeds'),str(native),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
    received=[]
    for i in range(len(roots)):
        output=work/f'rows{i}'
        seedlog=subprocess.run([str(work/'orbits'),str(work/'linear'),str(work/'rot'),str(work/'seeds'),str(i),str(output)],check=True,text=True,capture_output=True)
        oid,npoint,nseed,ngroup,nrow=map(int,seedlog.stderr.split());assert oid==i and npoint==32
        cover=subprocess.run([str(work/'cover'),str(work/f'fix{i}'),str(work/f'duo{i}'),str(output)],check=True,text=True,capture_output=True)
        keys=list(map(int, cover.stdout.split()));assert len(keys)==7 and keys[-1]==0
        received.append(dict(generator_basis_image=[roots[i][j] for j in (25,5,1)],generators=orbit_sizes[i],fixed=singles[i],paired_candidates=pairs[i][0],pairs=pairs[i][1],quadruples=nrow,free_shapes=ngroup,small_nodes=keys[0],one_nodes=keys[1],one_residuals=keys[2],two_shapes=keys[3],two_options=keys[4],minimum_two_remainder=keys[5]))
    return {'labels':11,'cost_bound_used':False,'found':False,'types':received}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--older',type=Path,required=True);a.add_argument('--group',type=Path,required=True);args=a.parse_args()
    with TemporaryDirectory()as w:print(json.dumps(verify(args.older.resolve(),args.group.resolve(),Path(w)),indent=2,sort_keys=True))
