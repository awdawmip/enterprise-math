"""Eleven-label improvement excludes all four-element elementary abelian symmetry groups."""
import argparse,json,sys,subprocess
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
from functools import cache
from fixed import build
from balance import check
HERE=Path(__file__).resolve().parent

def verify(older,group,work):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(group)]
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    from generate import maps
    from verify import MINIMA
    native=work/'native';observation_file(native);bad,pair=observations();L,_,_=maps()
    @cache
    def lb(n,k,t):
        if not k:return 0 if n==0 else 10**8
        if n<k or n>12*k+t:return 10**8
        return min(MINIMA[s]+lb(n-s,k-1,t-(s==13))for s in range(1,14)if s<13 or t)
    def caps(r):
        return {s:(11291-lb(125-r*s,11-r,2-r*(s==13)))//r for s in range(1,14)if (s<13 or r<=2) and MINIMA[s]*r+lb(125-r*s,11-r,2-r*(s==13))<=11291}
    assert caps(2)=={8:581,9:761,10:951,11:1131,12:1311,13:1498} and caps(4)=={10:842,11:1027,12:1207}
    identity=bytes(range(125));comp=lambda a,b:bytes(a[x]for x in b);inv={a:bytes(a.index(i)for i in range(125))for a in L}
    invs=[a for a in L if a!=identity and comp(a,a)==identity]
    remaining={frozenset((identity,a,b,comp(a,b))) for a,b in combinations(invs,2)if comp(a,b)==comp(b,a)}; assert len(remaining)==25
    reps=[];counts=[]
    while remaining:
        h=min(remaining,key=lambda x:sorted(x));s=sorted(h-{identity});g=[identity,s[0],s[1],comp(s[0],s[1])]
        orb={frozenset(comp(t,comp(q,inv[t]))for q in g)for t in L};assert orb<=remaining;remaining-=orb;reps.append(g);counts.append(len(orb))
    (work/'v4all').write_text(''.join(' '.join(str(j)for g in G for j in g)+'\n'for G in reps))
    (work/'linear').write_text(''.join(' '.join(map(str,g))+'\n'for g in L));fix=build(work,bad,pair,class_cost)
    for name in ('class_seeds','pairs','quadruples'):
        subprocess.run(['c++','-std=c++17','-mpopcnt','-O3',str(HERE/(name+'.cpp')),'-o',str(work/name)],check=True)
    subprocess.run([str(work/'class_seeds'),str(native),str(work/'seeds')],check=True,stdout=subprocess.DEVNULL)
    for i in range(len(reps)):
        subprocess.run([str(work/'quadruples'),str(work/'linear'),str(work/'v4all'),str(work/'seeds'),str(i),str(work/f'qbank{i}')],check=True,stderr=subprocess.DEVNULL)
        for h in (1,2,3):
            with (work/f'pbank{i}.{h}').open('w')as out:
                subprocess.run([str(work/'pairs'),str(native),str(work/'v4all'),str(i),str(h)],stdout=out,stderr=subprocess.DEVNULL,check=True)
    facts=check(work)
    for i,d in enumerate(facts):d.update(conjugates=counts[i],basis_images=[[g[j]for j in (25,5,1)]for g in reps[i][1:]],fixed_supports=fix[i])
    return dict(labels=11,budget=11291,num_subgroups=sum(counts),classes=facts,found=False)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--older',required=True,type=Path);ap.add_argument('--group',required=True,type=Path);a=ap.parse_args()
    with TemporaryDirectory()as temp:print(json.dumps(verify(a.older.resolve(),a.group.resolve(),Path(temp)),indent=2,sort_keys=True))
