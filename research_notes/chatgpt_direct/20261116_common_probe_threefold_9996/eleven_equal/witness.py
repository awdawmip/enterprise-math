"""Verify the five-maximum witness with stabilizer of order exactly three."""
import argparse,json,sys,os
from pathlib import Path
from itertools import combinations

def verify(last):
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(older/'bounds'),str(last/'group'),str(last/'original')]
    from generate import maps
    from cyclic11 import observations,class_cost
    from frontier9.native.replay_joint import run
    rows=json.loads(Path(__file__).with_name('groups.json').read_text())
    assert sorted(sum(rows,[]))==list(range(125))
    bad,pair=observations()
    assert not any(bad[a][b]>>c&1 for row in rows for a,b,c in combinations(row,3))
    maps_,trans,_=maps();table={frozenset(r)for r in rows}
    st=sum(all(frozenset(t[a[p]]for p in r) in table for r in rows)for a in maps_ for t in trans)
    assert st==3 and sum(class_cost(r,pair)for r in rows)==11292
    labels=[0]*125
    for j,row in enumerate(rows):
        for i in row:labels[i]=j
    res=json.loads(json.dumps(run(labels,1)))
    assert res['joint']['total_queries']==11292
    return {'stabilizer':st,'receipt':res}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--round3',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().round3.resolve()),sort_keys=True,indent=2))
