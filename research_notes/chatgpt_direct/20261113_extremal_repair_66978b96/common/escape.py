"""Sparse reserve message and conditional late encoder flag on a common-change source."""
from pathlib import Path
import json,argparse
from collections import Counter,defaultdict
from itertools import product,combinations
from hybrid import CODE
P=list(product(range(5),repeat=3))
def observe():
    groups=[]
    for d in (1,3):
        for start in P:
            bb=defaultdict(list)
            for i,w in enumerate(P):
                k=tuple(j for j in range(3)if(w[j]-start[j])%5 in (0,d))
                y=tuple(int(w[j]!=start[j]) for j in k);bb[k].append((i,y))
            groups.extend((d,start,k,g)for k,g in bb.items())
    return groups
def audit(B,obs):
    hist=Counter(); triples=set()
    for d,start,k,g in obs:
        b=defaultdict(list)
        for i,yy in g:b[B[i]].append((i,yy))
        for col,rows in b.items():
            sz=len({y for i,y in rows})
            if sz>2:
                triples.update(tuple(sorted((i,j,k))) for (i,y),(j,z),(k,w) in combinations(rows,3)if len({y,z,w})==3)
            else:hist[sz-1]+=len(rows)
    return hist,triples
def run():
    obs=observe();_,tr=audit(CODE,obs);T=sorted(tr);assert len(T)==2 and set(T[0]).isdisjoint(T[1])
    options=[]
    for a,b in product(*T):
        tab=list(CODE);tab[a]=tab[b]=11;hist,tr=audit(tab,obs);assert not tr and sum(hist.values())==31250 and len(Counter(tab))==12
        options.append({'moved_rows':[a,b],'moved_histories':[P[a],P[b]],'original_labels':[CODE[a],CODE[b]],'reads':hist[1],'read_histogram':dict(hist)})
    best=min(options,key=lambda row:(row['reads'],row['moved_rows']))
    return {'status':'PASS','scope':'fewest changes to this fixed eleven-message table to restore worst-case one read when adding one extra label, and optimal read count among all such minimal repairs routing exactly two rows into the single reserved label','two_distinct_disjoint_failing_triples':T,'minimum_changed_rows':2,'minimum_fraction_using_reserved_label':[2,125],'full_digit_width_old_and_new':4,'least_accumulated_supplements_among_nine':best,'repairs':options}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('escape_results.json'));args=ap.parse_args();d=run();args.out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(d['least_accumulated_supplements_among_nine'])
