"""Compute the full cost range on 12-label partitions with eight cheap near-full classes."""
from pathlib import Path
import json,subprocess,tempfile
import geometry
from six13 import enumerate_classes
from cyclic11 import setbits, observations, class_cost

HERE=Path(__file__).resolve().parent

def verify(directory):
    bad,pair=observations()
    actions=geometry.linear_actions()
    parents,centres=geometry.inventory(actions,bad,pair)
    path=directory/'parents.txt'
    path.write_text(''.join(f'{p%(1<<64)} {p>>64} {c}\n'for p,c in zip(parents,centres)))
    raw=subprocess.check_output([str(directory/'parent_packing'),'8',str(path)],text=True)
    based=[list(map(int,l.split())) for l in raw.splitlines() if l[0].isdigit()]
    key=geometry.normalize(parents,centres,actions)
    reps={key(p)for p in based}
    results=[]
    for parent_family in reps:
        residues=geometry.residuals([parents[i]for i in parent_family])
        assert len(residues)==1
        space=next(iter(residues))
        points=list(setbits(space))
        ix={p:i for i,p in enumerate(points)}
        compress=lambda m:sum(1<<ix[p] for p in setbits(m))
        header=''.join(str(compress(bad[x][y]&space))+' '+' '.join(str((pair[x][y]>>(64*j))%2**64)
                for j in range(4))+'\n' for x in points for y in points)
        data=header+''.join(f'{compress(s)} {class_cost(list(setbits(s)),pair)}\n'
                           for s in enumerate_classes(space,7,bad))
        count,least,most=map(int,subprocess.check_output([str(directory/'residual_four')],input=data,text=True).split())
        results.append(dict(residual_covers=count,residual_min=least,residual_max=most,total_min=8*1116+least,total_max=8*1116+most))
    return sorted(results,key=lambda r:r['residual_min'])

def run():
    with tempfile.TemporaryDirectory() as tmp:
        work=Path(tmp)
        for stem in ('parent_packing','residual_four'):
            subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/(stem+'.cpp')),'-o',str(work/stem)],check=True)
        return verify(work)

if __name__=='__main__':print(json.dumps(run(),indent=2))
