"""Enumerate affine maps of each of five planes, and all permutations of these planes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from itertools import permutations,product
from collections import Counter
from tempfile import TemporaryDirectory
import argparse,json,os,sys,subprocess
HERE=Path(__file__).resolve().parent
def verify(previous,groups):
    last=previous/'previous';older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'group'),str(older/'bounds')]
    from generate import observation_file
    from cyclic11 import observations,class_cost
    rows=json.loads(groups.read_text());masks=[sum(1<<p for p in r)for r in rows]
    _,q=observations()
    assert sum(class_cost(r,q)for r in rows)==9996
    # The embeddings have to leave x-planes parallel. This monomial subgroup of the
    # global cost isometries has 125 possible translations and 32 distinct linear parts.
    points=list(product(range(5),repeat=3))
    def ix(x):return 25*(x[0]%5)+5*(x[1]%5)+x[2]%5
    signs=list(product((1,-1),repeat=3))
    matrices={tuple(ix([v*s[i]*p[j[i]]for i in range(3)])for p in points)
              for v,j,s in product((1,2),((0,1,2),(0,2,1)),signs)}
    assert len(matrices)==32 and len(matrices)*125==4000
    with TemporaryDirectory()as temp:
        w=Path(temp);observation_file(w/'obs')
        (w/'m').write_text(''.join(f'{m%2**64} {m>>64}\n'for m in masks))
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++20',str(HERE/'planes.cpp'),'-o',str(w/'test')],check=True)
        def run(i):
            p=subprocess.run([str(w/'test'),str(w/'obs'),str(w/'m'),'0','2','9995',str(i),'4'],capture_output=True,text=True,check=True)
            cols=list(map(int,p.stdout.split()))
            spectrum={int(a):int(b)for a,b in (line.split()for line in p.stderr.splitlines())}
            return cols[1:],spectrum
        with ThreadPoolExecutor(max_workers=4)as pool:runs=list(pool.map(run,range(4)))
        nodes=list(map(sum,zip(*(x for x,c in runs))))
        spectrum=sum((Counter(c)for x,c in runs),Counter())
        assert spectrum=={9996:20} and nodes[-1]==20
        # Target yz translations and signed swaps have order 200. Their left action
        # on the first nonsingular affine plane map is free. Each class has 200 lifts.
        return dict(normalized_nodes=nodes,normalized_spectrum=dict(spectrum),
                    unnormalized_mappings=200*sum(spectrum.values()),preserving_monomial_subgroup=4000)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--groups',type=Path,required=True)
    a=p.parse_args();print(json.dumps(verify(a.previous.resolve(),a.groups.resolve()),indent=2,sort_keys=True))
