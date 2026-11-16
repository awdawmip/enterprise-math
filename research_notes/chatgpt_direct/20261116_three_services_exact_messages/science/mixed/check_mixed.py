"""Certify the exact one-read and two-read message counts for a 2+1 action split."""
from collections import Counter,defaultdict
from itertools import combinations,product
from pathlib import Path
import json,subprocess,sys,tempfile

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'frontier9/common'))
from translation import enumerate_large
from mixed_reps import go as orbit_representatives
P=list(product(range(5),repeat=3))


def run():
    table=json.loads((HERE/'twelve.json').read_text())['table']
    assert len(table)==125 and set(table)==set(range(12))
    edges=set()
    reads=Counter()
    pair_budget=Counter()
    for m,k in product((1,2),repeat=2):
        for e in P:
            worlds=defaultdict(list)
            for i,(x,y,z) in enumerate(P):
                updated=(m*x%5,m*y%5,k*z%5)
                active=tuple(j for j in range(3) if (updated[j]-e[j])%5 in (0,1))
                out=tuple(updated[j]==e[j] for j in active)
                worlds[active].append((i,out))
            for active,rows in worlds.items():
                for (i,x),(j,y),(h,z) in combinations(rows,3):
                    if len({x,y,z})==3:edges.add((i,j,h))
                sub=defaultdict(list)
                pair_sub=defaultdict(list)
                for i,out in rows:
                    sub[table[i]].append(out)
                    x,y,_=P[i]
                    pair_sub[((x+2*y)%5)//2].append(out)
                for outcomes in sub.values():
                    distinct=set(outcomes)
                    assert 1<=len(distinct)<=2
                    if len(distinct)==2:
                        a,b=distinct
                        assert any(x!=y for x,y in zip(a,b))
                    reads[len(distinct)-1]+=len(outcomes)
                for outcomes in pair_sub.values():
                    # Count the adaptive reads for an explicit policy that first distinguishes the two tied axes.
                    pair_pos=[pos for pos,axis in enumerate(active) if axis<2]
                    pair_outputs={tuple(o[j] for j in pair_pos) for o in outcomes}
                    assert len(pair_outputs)<=2
                    third_pos=active.index(2) if 2 in active else None
                    for p in pair_outputs:
                        matching=[o for o in outcomes if tuple(o[j] for j in pair_pos)==p]
                        needs_third=third_pos is not None and len({o[third_pos] for o in matching})==2
                        pair_budget[int(len(pair_outputs)>1)+int(needs_third)]+=len(matching)
    assert len(edges)==73000 and reads=={0:36370,1:26130}
    assert len(pair_budget)==3 and sum(pair_budget.values())==62500
    nodes,anchored,large=enumerate_large(edges)
    ordered=sorted(large)
    by_size=Counter(s.bit_count() for s in ordered)
    assert by_size=={11:12000,12:625}
    reps=orbit_representatives([s for s in ordered if s.bit_count()==12])
    with tempfile.TemporaryDirectory() as d:
        root=Path(d)
        masks=root/'classes';masks.write_text('\n'.join(map(str,ordered)))
        idx=root/'indices';idx.write_text('\n'.join(map(str,reps)))
        exe=root/'lower'
        subprocess.run(['c++','-O3','-std=c++17',str(HERE/'packing_lower.cpp'),'-o',str(exe)],check=True)
        r=subprocess.check_output([str(exe),str(masks),str(idx)],text=True)
    audit=[list(map(int,line.split())) for line in r.splitlines()]
    assert [i for i,n,achieved in audit]==[4,5,6] and all(n>0 and achieved==0 for i,n,achieved in audit)
    return dict(forbidden_triples=len(edges),queries=reads,three_bucket_query_counts=pair_budget,
                large_class_search_nodes=nodes,classes_by_size=by_size,
                size12_symmetry_representatives=reps,extensions_checked=audit,
                one_read_minimum_messages=12)

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
