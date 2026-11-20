"""Exact total read cost at every fine budget, conditional on preserving each old message."""
from pathlib import Path
from tempfile import TemporaryDirectory
from functools import cache
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent

def verify(previous):
    fifth=previous/'previous'
    fourth=fifth/'previous'
    third=fourth/'previous'
    second=third/'previous'
    sys.path[:0]=[str(second/'bounds'),str(second/'curve')]
    from cyclic11 import class_cost,observations
    from prior_bounds import observation_file
    from verify import lower
    obs=observations()[1]
    read=lambda path:json.loads(path.read_text())
    tables=read(fourth/'eleven_six_counts/groups.json')+[read(fifth/'eleven_equal/groups.json'),read(fifth/'c3/groups.json'),read(third/'asymmetric8721/groups.json')]
    unique=sorted({tuple(sorted(r))for groups in tables for r in groups})
    raw=''.join(' '.join(map(str,[len(r),*r]))+'\n'for r in unique)
    with TemporaryDirectory()as temp:
        w=Path(temp)
        observation_file(w/'obs')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'class_curve.cpp','-o',w/'curve'],check=True)
        out=iter(subprocess.check_output([w/'curve',w/'obs'],input=raw,text=True).splitlines())
    row_cost={}
    for r in unique:
        costs=[]
        for n in range(1,len(r)+1):
            j,c,*masks=map(int,next(out).split())
            assert j==n and len(masks)==n
            children=[[x for i,x in enumerate(r)if mask>>i&1]for mask in masks]
            assert all(children) and sorted(sum(children,[]))==list(r)
            assert sum(class_cost(v,obs)for v in children)==c
            costs.append(c)
        row_cost[r]=costs
    assert next(out,None) is None
    seven=[0,11,19,27,55,95,103]
    six=[14,16,28,70,80,102]
    parent=tuple(sorted(seven+six))
    assert parent in {tuple(sorted(r)) for r in tables[2]}
    assert [class_cost(x,obs) for x in (parent,seven,six)]==[1296,312,204]
    assert row_cost[parent][1]==516
    curves=[]
    for table in tables:
        last={0:0}
        for r in table:
            new={}
            for n,c in last.items():
                for j,v in enumerate(row_cost[tuple(sorted(r))],1):
                    q=n+j;new[q]=min(new.get(q,10**9),c+v)
            last=new
        assert last[125]==0
        curves.append(last)
    eleven={n:min(v[n]for v in curves[:3])for n in range(11,126)}
    values=dict(eleven_optimal_orbits=eleven,eleven_A=curves[0],eleven_B=curves[1],eleven_C=curves[2],twelve_threefold=curves[3],thirteen=curves[4])
    return dict(curves=values,first_global_optimal_fine_budget_at_least_14={
        name:min(n for n,c in curve.items() if n>=14 and c==lower(125,n)) for name,curve in values.items()})

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().previous.resolve()),sort_keys=True,separators=(',',':')))
