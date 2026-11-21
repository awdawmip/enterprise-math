"""Verify a single optimal chain with simultaneous least point and class changes."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse,json,sys
HERE=Path(__file__).resolve().parent

def verify(previous):
    second=previous/'previous/previous/previous/previous'
    sys.path[:0]=[str(second/'curve'),str(second/'bounds')]
    from verify import cheap_line_partitions,lower,MINIMA
    from cyclic11 import observations,class_cost
    bad,menus=observations()
    rows=list(map(frozenset,cheap_line_partitions(21)))
    cert=list(map(frozenset,json.loads((HERE/'new_labels.json').read_text())))
    def audit(rows):
        assert all(rows) and sorted(x for r in rows for x in r)==list(range(125))
        assert not any(bad[x][y]>>z&1 for r in rows for x,y,z in combinations(sorted(r),3))
        assert sum(class_cost(r,menus) for r in rows)==lower(125,len(rows))
    audit(rows)
    totals=[0,0]
    levels={}
    for k in range(21,125):
        small,rem=divmod(125,k+1)
        # Any optimal target has just these sizes. Its extra unmatched name
        # already requires every history in one of its classes to change label.
        permitted={small,small+1} if rem else {small}
        assert all(s in permitted for s in range(1,14)if MINIMA[s]+lower(125-s,k)==lower(125,k+1))
        if k<63:
            q=cert[k-21]
        else:
            pair=next(r for r in rows if len(r)==2)
            q=frozenset([min(pair)])
        assert len(q)==small
        new=[r-q for r in rows]+[q]
        audit(new)
        old_sizes=Counter(map(len,rows)); new_sizes=Counter(map(len,new))
        changed=k-len(set(rows)&set(new))
        size_bound=sum((old_sizes-new_sizes).values())
        assert changed==size_bound
        totals[0]+=len(q);totals[1]+=changed
        levels[str(k)]=[small,changed]
        rows=new
    assert len(rows)==125 and len(cert)==42
    return dict(first=21,last=125,optimal_steps=len(levels),cumulative_reassignments=totals[0],
                cumulative_replaced_old_classes=totals[1],per_transition=levels)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().previous.resolve()),indent=2,sort_keys=True))
