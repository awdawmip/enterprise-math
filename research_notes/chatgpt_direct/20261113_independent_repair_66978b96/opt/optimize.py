"""Exhaust all four-symbol one-probe encoders, up to relabelings leaving total read count invariant."""
from itertools import product,combinations
from collections import Counter,defaultdict
import argparse,json
from pathlib import Path
ROW=list(product(range(4), repeat=5))
def masks():
    pos=[[(r[k],r.count(r[k])>1) for k in range(5)] for r in ROW]
    return [sum(1<<j for j,q in enumerate(pos) if all(u!=v or not (dup or rep) for (u,dup),(v,rep) in zip(a,q))) for a in pos]
def count_queries(board):
    total=0;active=Counter()
    for a,b in combinations(range(5),2):
        for c,d in combinations(range(5),2):
            cells=defaultdict(list)
            for i,j in product(range(5),repeat=2):
                inn=(i in (a,b),j in (c,d))
                cells[(board[i][j],*inn)].append((i if inn[0] else -1,j if inn[1] else -1))
            for (col,u,v),ans in cells.items():
                assert len(set(ans))<=2
                if len(set(ans))==2:
                    total+=len(ans);active[int(u)+int(v)]+=len(ans)
    return total,dict(sorted(active.items()))
def run():
    mask=masks();results={}; hist=Counter();examples={};profiles=Counter();n=0
    def clique(pool,k,prefix):
        if len(prefix)==k:
            yield prefix;return
        while pool.bit_count()>=k-len(prefix):
            b=pool&-pool;i=b.bit_length()-1;pool-=b
            yield from clique(pool&mask[i],k,prefix+[i])
    for j,r in enumerate(ROW):
        if tuple(sorted(r))!=r or tuple(sorted(Counter(r).values(),reverse=True))!=tuple(r.count(t) for t in sorted(set(r))) or set(r)!=set(range(max(r)+1)):continue
        tag=''.join(map(str,r));cases=0
        for ix in clique(mask[j],4,[]):
            board=[r]+[ROW[i] for i in ix];v,prof=count_queries(board)
            hist[v]+=1;cases+=1;n+=1;examples.setdefault(v,[''.join(map(str,a)) for a in board]);profiles[v,tuple(prof.items())]+=1
        results[tag]=cases
    return dict(status='PASS',first_row_shape_completions=results,representatives_visited=n,totals_histogram=dict(sorted(hist.items())),best_total_reads=min(hist),worst_total_reads=max(hist),representative_best=examples[min(hist)],representative_worst=examples[max(hist)],profiles=[dict(reads=v,by_active=dict(p),representatives=n) for (v,p),n in sorted(profiles.items())],scope='representatives need not be distinct under remaining symmetries; counts of labelled encoders not asserted; exactly 2500 equally counted inputs per board')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('results.json'));a=p.parse_args();d=run();a.out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
