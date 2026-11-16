"""Check the twelve-label witness against every public condition and the original receipts."""
from pathlib import Path
from itertools import combinations
import argparse,json,sys
HERE=Path(__file__).resolve().parent
def run(older,original):
    sys.path[:0]=[str(older/'bounds'),str(original)]
    from cyclic11 import observations,class_cost
    from verify_twelve import verify
    from frontier9.native.replay_joint import run as native
    labels=list(map(int,(HERE/'labels.txt').read_text().split()))
    rows=json.loads((HERE/'groups.json').read_text())
    assert len(rows)==12 and sorted(p for row in rows for p in row)==list(range(125))
    assert all(labels[p]==i for i,row in enumerate(rows) for p in row)
    old=list(map(int,(older/'bounds/twelve_10147.txt').read_text().split()))
    oldrows={frozenset(p for p,c in enumerate(old) if c==i)for i in set(old)}
    kept=len(oldrows&{frozenset(row)for row in rows})
    bad,obs=observations()
    assert not any(bad[a][b]>>c&1 for row in rows for a,b,c in combinations(sorted(row),3))
    report=verify(labels)
    assert report['reads_by_class']==[class_cost(row,obs)for row in rows]
    direct=native(labels,1)
    assert direct['joint']['by_queries']=={0:report['zero_reads'],1:report['one_read']} or json.loads(json.dumps(direct['joint']['by_queries']))=={'0':report['zero_reads'],'1':report['one_read']}
    return dict(retained_from_10147=kept,enumeration=report,native=direct)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True);p.add_argument('--original',type=Path,required=True);a=p.parse_args()
    print(json.dumps(run(a.older.resolve(),a.original.resolve()),sort_keys=True,indent=2))
