"""First two transformations are equal; the third is independently selected."""
from pathlib import Path
from itertools import product
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]))
from next_repair.native import native_recovery as k


def run(table):
    old_encode = k.encode
    rules = sorted(set((m,m,t) for m,t in product(k.MAPS,repeat=2)))
    def encode(h,policy):
        if policy=='partial':return table[25*h[0]+5*h[1]+h[2]]
        return old_encode(h,policy)
    k.encode=encode
    k.possible.cache_clear()
    compiler=k.core.prior.Compiler(slots=15)
    T,G,counts=k.component_table(compiler)
    stats=k.Stats()
    sampled=set()
    try:
        for h in product(range(5),repeat=3):
            label=encode(tuple(G[v] for v in h),'partial')
            for maps in rules:
                for edges in product(range(5),repeat=3):
                    keys=list(zip(h,maps,edges))
                    receipt=tuple(T[*key,0][0] for key in keys)
                    def actual_read(i,endpoint):
                        assert endpoint==edges[i]+1
                        return T[*keys[i],1][1]
                    result,trace=k.decode('partial',maps,edges,receipt,label,actual_read,1)
                    reads={i for i,key,bit in trace}
                    terms=[T[*key,int(i in reads)] for i,key in enumerate(keys)]
                    assert result==tuple(t[2] for t in terms)
                    cost=sum(t[3] for t in terms)
                    stats.add(h,maps,edges,label,receipt,result,trace,cost)
                    sample=(maps,tuple(sorted(reads)),tuple(v==11 for v in receipt))
                    if sample not in sampled:
                        sampled.add(sample)
                        init=[k.old(compiler,v) for v in h]
                        msg=encode(tuple(t[1] for t in init),'partial')
                        ps=[t[0] for t in init]
                        for p,m in zip(ps,maps):k.update(p,m)
                        verified=k.real_path(ps,h,maps,edges,msg,'partial',1)
                        assert verified==(receipt,result,trace,cost)
    finally:
        k.encode=old_encode
        k.possible.cache_clear()
    return {'original_components':counts,'full_raw_paths':len(sampled),'joint':stats.result()}

if __name__=='__main__':
    table=json.loads((HERE/'twelve.json').read_text())['table']
    print(json.dumps(run(table),indent=2,sort_keys=True))
