"""Recompute all native scenarios and the affine stabilizer of the C3 witness."""
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
    assert not any(bad[i][j] >> k & 1 for row in rows for i,j,k in combinations(row,3))
    prices=[class_cost(row,pair) for row in rows]
    table={frozenset(r) for r in rows}
    lin,tr,_=maps()
    stab=[]
    for a in lin:
        for t in tr:
            g=bytes(t[i] for i in a)
            if all(frozenset(g[i] for i in r) in table for r in rows): stab.append(g)
    assert len(stab)==3
    code=[0]*125
    for j,row in enumerate(rows):
        for p in row:code[p]=j
    receipt=json.loads(json.dumps(run(code,1)))
    assert sum(prices)==receipt['joint']['total_queries']==9996
    return {'receipt':receipt,'stabilizer':len(stab),'prices':prices,'sizes':list(map(len,rows))}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--round3',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().round3.resolve()),sort_keys=True,indent=2))
