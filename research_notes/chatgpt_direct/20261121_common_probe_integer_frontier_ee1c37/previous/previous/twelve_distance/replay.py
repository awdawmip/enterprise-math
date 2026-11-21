"""Every lower-cost table must move several original histories out of the same labels."""
import argparse,json,os,sys,subprocess
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
HERE=Path(__file__).resolve().parent
def verify(previous):
    previous=previous/'previous';r3=previous/'previous/previous';r2=r3/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(r2)
    sys.path[:0]=[str(r3/'group'),str(r2/'bounds')]
    from generate import observation_file
    from cyclic11 import observations
    rows=json.loads((previous/'c3/groups.json').read_text())
    bad,_=observations();extensions=[]
    for group in rows:
        banned=set(group)
        for i,j in combinations(group,2):banned.update(x for x in range(125)if bad[i][j]>>x&1)
        extensions.append(125-len(banned))
    assert not any(extensions)
    out=[]
    with TemporaryDirectory()as t:
        d=Path(t);observation_file(d/'input')
        (d/'source').write_text(''.join(f'{m%(1<<64)} {m>>64}\n'for m in [sum(1<<p for p in row)for row in rows]))
        subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/'edits.cpp','-o',d/'edit'],check=True)
        for loss in (4,):
            proc=subprocess.run([d/'edit',d/'input',d/'source',str(loss),'13','9995'],text=True,capture_output=True,check=True)
            sentinel,nodes=map(int,proc.stdout.split());assert sentinel==9996
            counts=[int(x.split()[1])for x in proc.stderr.splitlines()]
            out.append(dict(excess_at_most=loss-1,cover_nodes=nodes,classes_by_label=counts,feasible=False))
    return dict(single_point_extensions=extensions,source_cost=9996,budget=9995,unconditional_minimum_excess=4,
                minimum_moved_histories_using_seven_region_bound=12,exclusions=out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);a=p.parse_args()
    result=verify(a.previous.resolve())
    assert result==json.loads((HERE/"result.json").read_text())
    print(json.dumps(result,indent=2,sort_keys=True))
