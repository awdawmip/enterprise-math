"""Decide cost improvement under the order-three cyclic coordinate permutation."""
import argparse,json,subprocess,sys
from pathlib import Path
from tempfile import TemporaryDirectory
from functools import cache
from selection import select,reduce
from fixed import fixed
from incumbent import verify as incumbent
HERE=Path(__file__).resolve().parent

def verify(older,group,work):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(group)]
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    from verify import MINIMA
    from generate import maps
    native=work/'native';observation_file(native);bad,pair=observations();lin,tr,_=maps()
    g=bytes(25*(i//5%5)+5*(i%5)+i//25 for i in range(125));eye=bytes(range(125));comp=lambda f,h:bytes(f[i]for i in h)
    order3={a for a in lin if a!=eye and comp(a,comp(a,a))==eye}
    assert order3=={comp(a,comp(x,bytes(a.index(i)for i in range(125))))for a in lin for x in (g,comp(g,g))}
    @cache
    def lb(n,k,t):
        if k==0:return 0 if n==0 else 10**8
        if n<k or n>12*k+t:return 10**8
        return min(MINIMA[s]+lb(n-s,k-1,t-(s==13)) for s in range(1,14) if s<13 or t)
    caps={s:(11291-lb(125-3*s,8,2))//3 for s in range(1,13) if 3*MINIMA[s]+lb(125-3*s,8,2)<=11291}
    assert caps=={9:691,10:875,11:1059,12:1242}
    for name,perms in [('linear',lin),('rot',[g])]:
        (work/name).write_text(''.join(' '.join(map(str,p))+'\n'for p in perms))
    singles=fixed(work,[g],bad,pair,class_cost);support_count,raw=select(work,g);normalizer,reps=reduce(work,g,lin,tr)
    for name in ('class_seeds','orbits','trimixed','trimatch'):
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/(name+'.cpp')),'-o',str(work/name)],check=True)
    subprocess.run([str(work/'class_seeds'),str(native),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
    output=work/'rows';seedlog=subprocess.run([str(work/'orbits'),str(work/'linear'),str(work/'rot'),str(work/'seeds'),'0',str(output)],check=True,text=True,capture_output=True)
    idx,n,normalized,shapes,nrow=map(int,seedlog.stderr.split());assert idx==0 and n==45
    records=[]
    for i in range(3):
        run=subprocess.run([str(work/'trimixed'),str(work/'trifix0'),str(output),str(i),'0','1'],check=True,text=True,capture_output=True)
        assert not run.stdout
        v=run.stderr.split();assert v[-1]=='0';records.append(dict(triples=i,nodes=int(v[2]),complement_lookups=int(v[4])))
    match=subprocess.run([str(work/'trimatch'),str(output),str(work/'trireps'),'0','1'],check=True,text=True,capture_output=True)
    assert not match.stdout and int(match.stderr.split()[-1])==reps
    return dict(labels=11,maximum_cost=11291,incumbent=incumbent(older,lin,tr,bad,pair,class_cost),order_three_generators=len(order3),fixed_supports=singles[0],free_shapes=shapes,triple_supports=nrow,normalizer_actions=normalizer,three_triples_legal_pairs=raw,three_triples_supports=support_count,three_triples_orbits=reps,smaller_cases=records,found=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--group',type=Path,required=True);args=p.parse_args()
    with TemporaryDirectory()as tmp:print(json.dumps(verify(args.older.resolve(),args.group.resolve(),Path(tmp)),indent=2,sort_keys=True))
