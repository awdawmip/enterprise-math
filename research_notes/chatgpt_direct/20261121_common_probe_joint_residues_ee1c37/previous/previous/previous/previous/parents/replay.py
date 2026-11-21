"""Determine how many native histories can belong to the union of ten to thirteen full parents."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
from itertools import combinations
import argparse,json,subprocess,sys

HERE=Path(__file__).resolve().parent

def run(older,jobs):
    sys.path.insert(0,str(older/'bounds'))
    from geometry import linear_actions,inventory
    from cyclic11 import observations,class_cost
    bad,menus=observations()
    parents,centers=inventory(linear_actions(),bad,menus)
    # The full native census at sizes 12 and 13 and the affine description of every parent
    # are archived in the previous bounds and class enumeration.
    assert len(parents)==250 and all(row.bit_count()==13 for row in parents)
    from assignment import check as verify_assignment
    witnesses=json.loads((HERE/'witnesses.json').read_text())
    for k,w in witnesses.items():
        indices=w['parent_indices']
        assert len(set(indices))==int(k)
        used=0;groups=[]
        for i in indices:
            m=parents[i] &~used
            groups.append([x for x in range(125)if m>>x&1])
            used |= parents[i]
        assert len(groups)==int(k) and all(groups)
        assert all(not any(bad[x][y]>>z&1 for x,y,z in combinations(row,3)) for row in groups)
        assert [len(row) for row in groups]==w['sizes']
        assert sum(class_cost(row,menus) for row in groups)==w['partition_cost']
        assert used.bit_count()==w['covered']
    optimum=verify_assignment(parents,witnesses['13']['parent_indices'],menus,class_cost)
    expected=json.loads((HERE/'result.json').read_text())
    with TemporaryDirectory()as tmp:
        folder=Path(tmp)
        subprocess.run(['c++','-O3','-mpopcnt','-std=c++20',HERE/'cover.cpp','-o',folder/'check'],check=True)
        bank=''.join(f'{m%(1<<64)} {m>>64}\n'for m in parents)
        def check(e):
            a=subprocess.check_output([folder/'check',str(e['parents']),str(e['missing_at_most'])],text=True,input=bank)
            k,h,n,yes=map(int,a.split());assert yes==0
            return dict(parents=k,missing_at_most=h,nodes=n,feasible=False)
        with ThreadPoolExecutor(max_workers=jobs)as pool:
            stats=list(pool.map(check,expected['exclusions']))
        from orderproof import check as pairs
        cases=pairs(folder,parents,centers,3,jobs)
    return {'twelve_anchored_pairs':cases,'largest_unions':{k:v['covered']for k,v in witnesses.items()},'fixed_thirteen_assignment':optimum,'exclusions':stats,'attained_coverage':{k:v['covered']for k,v in witnesses.items()}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args();out=run(a.older.resolve(),a.jobs)
    print(json.dumps(out,sort_keys=True),flush=True)
    assert out==json.loads((HERE/'result.json').read_text())
