"""Complete the three other order-four types below 11,292 reads."""
import argparse,json,subprocess,sys
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from functools import cache
from fixed import fixed
HERE=Path(__file__).resolve().parent

def verify(older,group,work):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(group)]
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    from verify import MINIMA
    from generate import maps
    native=work/'native';observation_file(native);bad,pair=observations();lin,tr,_=maps()
    comp=lambda f,h:bytes(f[i] for i in h);eye=bytes(range(125));neg=bytes(25*(-(i//25)%5)+5*(-(i//5%5)%5)+(-i%5)for i in range(125))
    other={g for g in lin if (g2:=comp(g,g)) not in (eye,neg) and comp(g2,g2)==eye}
    reps=[];orbits=[];wanted=[(50,3,10),(20,25,1),(20,25,4)]
    for basis in wanted:
        g=next(g for g in other if tuple(g[i]for i in (25,5,1))==basis);g3=comp(g,comp(g,g));inv=lambda a:bytes(a.index(i)for i in range(125))
        eq={comp(a,comp(x,inv(a)))for a in lin for x in (g,g3)};assert eq<=other;other-=eq;reps.append(g);orbits.append(len(eq))
    assert not other and sum(orbits)==24
    @cache
    def lb(n,k,t):
        if k==0:return 0 if n==0 else 10**8
        if n<k or n>12*k+t:return 10**8
        return min(MINIMA[s]+lb(n-s,k-1,t-(s==13))for s in range(1,14)if s<13 or t)
    def caps(r):
        return {s:(11291-lb(125-r*s,11-r,2-r*(s==13)))//r for s in range(1,14)if (s<13 or r<=2) and MINIMA[s]*r+lb(125-r*s,11-r,2-r*(s==13))<=11291}
    assert caps(2)=={8:581,9:761,10:951,11:1131,12:1311,13:1498} and caps(4)=={10:842,11:1027,12:1207}
    (work/'linear').write_text(''.join(' '.join(map(str,p))+'\n'for p in lin));fix=fixed(work,reps,bad,pair,class_cost)
    for name in ('class_seeds','k4rows','altpaired','altcover'):
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(HERE/(name+'.cpp')),'-o',str(work/name)],check=True)
    subprocess.run([str(work/'class_seeds'),str(native),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
    results=[]
    for i,g in enumerate(reps):
        gfile=work/'perm';gfile.write_text(' '.join(map(str,g))+'\n');points=set(range(125));hist=Counter()
        while points:
            z=min(points);n=0
            while z in points:points.remove(z);n+=1;z=g[z]
            hist[n]+=1
        four=subprocess.run([str(work/'k4rows'),str(work/'linear'),str(gfile),str(work/'seeds'),'0',str(work/'four')],check=True,capture_output=True,text=True)
        _,n,_,shapes,quad=map(int,four.stderr.split());assert n==sum(hist.values());assert shapes==112
        with (work/'pairs').open('w')as out:
            two=subprocess.run([str(work/'altpaired'),str(native),str(gfile)],stdout=out,stderr=subprocess.PIPE,check=True,text=True)
        _,visits,npair=map(int,two.stderr.split());sol=subprocess.run([str(work/'altcover'),str(gfile),str(work/f'fix{i}'),str(work/'pairs'),str(work/'four')],check=True,text=True,capture_output=True)
        assert not sol.stdout;nodes,limit=map(int,sol.stderr.split());assert limit==11292
        results.append(dict(generators=orbits[i],basis_images=wanted[i],point_cycles=dict(sorted(hist.items())),fixed=fix[i],two_support=npair,four_support=quad,pair_generation_nodes=visits,cover_nodes=nodes))
    return dict(budget=11291,labels=11,other_order_four_generators=sum(orbits),types=results,found=False)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--older',required=True,type=Path);ap.add_argument('--group',required=True,type=Path);a=ap.parse_args()
    with TemporaryDirectory()as tmp:print(json.dumps(verify(a.older.resolve(),a.group.resolve(),Path(tmp)),indent=2,sort_keys=True))
