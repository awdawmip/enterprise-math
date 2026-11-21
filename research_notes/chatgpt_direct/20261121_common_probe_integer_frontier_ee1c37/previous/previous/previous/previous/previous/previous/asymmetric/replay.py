"""Verify the 8,723-read thirteen-label certificate, including original receipts."""
import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent

def verify(older,groupdir,original):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(groupdir),str(original)]
    from cyclic11 import observations,class_cost
    from generate import maps
    from frontier9.native.replay_joint import run
    groups=json.loads((HERE/'groups.json').read_text())
    assert len(groups)==13 and sorted(p for row in groups for p in row)==list(range(125))
    code=[None]*125
    bad,pair=observations()
    prices=[]
    for i,row in enumerate(groups):
        assert not any((bad[a][b]>>c)&1 for a,b,c in combinations(row,3))
        for p in row:code[p]=i
        prices.append((len(row),class_cost(row,pair)))
    assert Counter(prices)=={(9,557):7,(10,744):5,(12,1104):1}
    linear,trans,_=maps()
    group={bytes(t[j] for j in l) for t in trans for l in linear}
    table={frozenset(row) for row in groups}
    stabilizer=[g for g in group if {frozenset(g[p] for p in row) for row in table}==table]
    assert len(group)==12000 and stabilizer==[bytes(range(125))]
    raw=run(code,1)
    result=json.loads(json.dumps(raw))
    assert result['joint']['by_queries']=={'0':22527,'1':8723}
    return {'cost_profile':[[s,c,n]for (s,c),n in sorted(Counter(prices).items())],
            'affine_group_order':len(group),'table_stabilizer_order':len(stabilizer),
            'orbit_size':len(group)//len(stabilizer),'native':result}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--older',required=True,type=Path)
    p.add_argument('--group',required=True,type=Path)
    p.add_argument('--original',required=True,type=Path)
    a=p.parse_args()
    print(json.dumps(verify(a.older.resolve(),a.group.resolve(),a.original.resolve()),sort_keys=True,indent=2))
