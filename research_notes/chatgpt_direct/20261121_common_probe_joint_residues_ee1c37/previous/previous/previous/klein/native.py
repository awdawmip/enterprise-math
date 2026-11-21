"""Verify the Klein optimum on the original common-transform problem."""
import argparse,json,os,sys
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent

def verify(last):
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'original'),str(last/'group'),str(older/'bounds')]
    from frontier9.native.replay_joint import run
    from generate import maps
    from cyclic11 import observations,class_cost
    rows=json.loads((HERE/'groups.json').read_text())
    assert len(rows)==12 and sorted(sum(rows,[]))==list(range(125))
    bad,pair=observations()
    assert not any(bad[i][j]>>k&1 for row in rows for i,j,k in combinations(row,3))
    prices=[class_cost(row,pair)for row in rows]
    table={frozenset(r)for r in rows}
    L,T,_=maps();stab=[]
    for a in L:
        for t in T:
            g=bytes(t[i]for i in a)
            if all(frozenset(g[i]for i in row)in table for row in rows):stab.append(g)
    assert len(stab)==4
    code=[0]*125
    for j,row in enumerate(rows):
        for p in row:code[p]=j
    out=json.loads(json.dumps(run(code,1)))
    assert sum(prices)==out['joint']['total_queries']==10632
    return dict(prices=prices,sizes=list(map(len,rows)),receipt=out,stabilizer_order=len(stab))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--round3',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().round3.resolve()),indent=2,sort_keys=True))
