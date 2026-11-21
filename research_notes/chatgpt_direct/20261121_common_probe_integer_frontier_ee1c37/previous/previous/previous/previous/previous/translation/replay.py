"""Rebuild all eleven- and twelve-label tables with a nonzero translation symmetry."""
import argparse,json,os,subprocess,sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations,product
from pathlib import Path
from tempfile import TemporaryDirectory
from geometry import export
HERE=Path(__file__).resolve().parent

def verify(last,work):
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'group'),str(older/'curve'),str(older/'bounds')]
    from generate import observation_file,maps
    from translation import DIRECTIONS,POINTS,ix,shift
    from cyclic11 import observations,class_cost
    observation_file(work/'obs');export(work/'geometry')
    for name in ['spectrum','large','quotient']:
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(HERE/(name+'.cpp')),'-o',str(work/name)],check=True)
    subprocess.run([str(work/'large'),str(work/'obs'),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
    def one(i):
        args=[str(work/'obs'),str(work/'geometry'),str(work/'seeds'),str(i),str(work)]
        raw=subprocess.check_output([str(work/'spectrum'),*args],text=True,stderr=subprocess.DEVNULL)
        optimum=subprocess.check_output([str(work/'quotient'),*args],text=True,stderr=subprocess.DEVNULL)
        costs=[list(map(int,line.split()))for line in raw.splitlines()]
        mins=[list(map(int,line.split()))for line in optimum.splitlines()]
        for d,k,x,y,_,_ in mins:
            for t,price in [(1,x),(2,y)]:assert min((v for dd,kk,tt,v,n in costs if (dd,kk,tt)==(d,k,t)),default=1000000)==price
        return costs,mins
    with ThreadPoolExecutor(max_workers=3)as pool:blocks=list(pool.map(one,range(5)))
    census=[r for block,_ in blocks for r in block]
    with (HERE/'spectrum.txt').open()as f:assert census==[list(map(int,line.split()))for line in f]
    linear,translations,_=maps();bad,obs=observations()
    witness={}
    for i in (2,4):
        rows=json.loads((HERE/f'groups{i}.json').read_text())
        assert len(rows)==12 and sorted(sum(rows,[]))==list(range(125))
        assert all(not any(bad[a][b]>>c&1 for a,b,c in combinations(row,3))for row in rows)
        price=sum(class_cost(row,obs)for row in rows)
        canonical={frozenset(r) for r in rows}
        stabilizer=[]
        for h in linear:
          for t in translations:
            g=bytes(t[p]for p in h)
            if {frozenset(g[p] for p in r)for r in rows}==canonical:stabilizer.append(g)
        orbit=len(linear)*len(translations)//len(stabilizer)
        d=DIRECTIONS[i]; base=ix(d)
        directions={min(frozenset(ix(tuple(t*x for x in POINTS[h[base]]))for t in range(1,5)))for h in linear}
        m=min(v for di,k,r,v,n in census if di==i and k==12)
        total=sum(n for di,k,r,v,n in census if (di,k,v)==(i,12,m))
        assert price==m and total*len(directions)>=orbit
        if i==4:assert orbit==total*len(directions)
        witness[str(i)]=dict(directions=len(directions),best=price,stabilizer=len(stabilizer),orbit=orbit,tables_at_minimum=total*len(directions))
    return dict(quotients=[m for _,m in blocks],examples=witness)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--last',type=Path,required=True)
    with TemporaryDirectory()as tmp:print(json.dumps(verify(p.parse_args().last.resolve(),Path(tmp)),sort_keys=True))
