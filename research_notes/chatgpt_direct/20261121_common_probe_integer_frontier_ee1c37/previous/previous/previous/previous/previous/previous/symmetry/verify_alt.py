"""Test a prescribed 13-label type with two least-cost 12-classes and relaxed 10-classes."""
from pathlib import Path
import argparse, json, tempfile, subprocess, sys
from inversion import load_classes,indexes
from itertools import permutations, product
HERE=Path(__file__).resolve().parent
LOW=(1<<64)-1
def run(older,prices,solver):
    with tempfile.TemporaryDirectory() as temp:
        work=Path(temp)
        bank,_=load_classes(older,work,None)
        population=bank[12,1104]
        pts=list(product(range(5),repeat=3))
        def index(p):
            return 25*(p[0]%5)+5*(p[1]%5)+p[2]%5
        maps=[bytes(index([d*s[j]*p[pm[j]]+b[j] for j in range(3)]) for p in pts)
              for s,pm,d,b in product(product((-1,1),repeat=3),permutations(range(3)),(1,2),pts)]
        def image(mask,g):
            return sum(1<<g[j] for j in indexes(mask))
        first=min(population)
        assert {image(first,g) for g in maps}==set(population)
        stabilizer=[g for g in maps if image(first,g)==first]
        remaining={p for p in population if not p&first}; jobs=[]
        while remaining:
            other=min(remaining)
            equiv={image(other,g) for g in stabilizer}
            equiv.update(image(first,g) for g in maps if image(other,g)==first)
            assert equiv <= remaining
            remaining-=equiv
            jobs.append((first,other))
        assert len(jobs)==6
        (work/'pairs').write_text(''.join(f'{u&LOW} {u>>64} {v&LOW} {v>>64}\n' for u,v in jobs))
        with (work/'rows').open('w') as f:
            for (s,c),values in sorted(bank.items()):
                if c not in (557,744,747):continue
                print(s,c,len(values),file=f)
                for m in sorted(values):print(m&LOW,m>>64,0,file=f)
        # This upstream finite size/cost profile list is exhaustive by the menu census.
        # The six unordered double-core placements are exhaustive by the action just checked.
        cpp=HERE/'alternates.cpp'
        exe=work/'pack'
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++17',str(cpp),'-o',str(exe)],check=True)
        results={}
        for cost in prices:
            uneven=(cost-8709)//3
            text=subprocess.check_output([str(exe),str(work/'rows'),str(work/'pairs'),str(uneven),'0','1'],cwd=work,text=True)
            rows=[list(map(int,l.split())) for l in text.splitlines()]
            assert [r[0] for r in rows]==list(range(6))
            results[cost]=rows
        return results
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--older',required=True,type=Path)
    p.add_argument('--prices',nargs='+',type=int,default=[8712,8715],choices=[8712,8715])
    a=p.parse_args()
    print(json.dumps(run(a.older.resolve(),a.prices,None),indent=2))
