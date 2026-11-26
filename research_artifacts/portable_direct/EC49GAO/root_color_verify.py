"""Verify chromatic certificates and target-specific label alphabets."""
import json
from collections import Counter
from functools import lru_cache
from root_color import color
from gal_path_hall import Bound, bitlist, maximal


def clique(adj,rem,k):
    if not k:return 0
    while rem.bit_count()>=k:
        b=rem&-rem;rem^=b
        c=clique(adj,rem&adj[b.bit_length()-1],k-1)
        if c is not None:return b|c
    return None


def main():
    x=json.load(open('gao_color.json'));old=json.load(open('recoverable_frontier.out'))['rows'];certs=[];counts=Counter()
    for row in x['rows']:
        for r in row['budgets']:
            n=len(r['qs']);adj=[0]*n
            for i,j,w in r['bad']:
                assert not any(w&~v==0 for v in r['exact'])
                adj[i]|=1<<j;adj[j]|=1<<i
            c=clique(adj,(1<<n)-1,len(r['classes']));assert c is not None
            assert all((adj[b.bit_length()-1]&c)==c^b for b in bitlist(c))
            assert all(not adj[b.bit_length()-1]&p for p in r['classes'] for b in bitlist(p))
            assert sum(r['classes'])==(1<<n)-1 and sum(p.bit_count() for p in r['classes'])==n
            certs.append([row['i'],r['d'],n,len(r['classes']),r['edges'],c]);counts['matched_clique_coloring']+=1
    k,n,*a=map(int,open('ga_nodes.txt').read().splitlines()[125].split());b=Bound(list(zip(a[::2],a[1::2])));s=b.full
    @lru_cache(None)
    def family(r,d):
        if r.bit_count()<=1:return frozenset([0,r])
        if not d:return frozenset([0])
        return frozenset(x|y for q in b.splits(r) for x in family(q,d-1) for y in family(r^q,d-1))
    r=x['rows'][125]['budgets'][0];qs=r['qs'];F=family(s,k); assert set(maximal(F))==set(r['exact'])
    targets=[t for t in old[125]['obstructions'] if t.bit_count()==11];v=max(t.bit_count() for t in F);assert len(targets)==6 and v==13
    graphs={name:[0]*len(qs) for name in ('all_targets','full_capacity','six_rank11','combined')};loose=set()
    for i,q in enumerate(qs):
        for j,p in enumerate(qs):
            # Use exact maxima derived from separately constructed full downward families.
            U={a|b for a in maximal(family(q,k-1)) for b in maximal(family(s^p,k-1))};loose.update(U)
            tests=[any(u not in F for u in U),any(u.bit_count()>v for u in U),any(t&~u==0 for u in U for t in targets)]
            tests.append(tests[1] or tests[2])
            for name,fail in zip(graphs,tests):
                if fail:assert i!=j;graphs[name][i]|=1<<j;graphs[name][j]|=1<<i
    assert set(maximal(loose))==set(r['loose'])
    specific={}
    for name,adj in graphs.items():
        parts,_=color(adj);c=clique(adj,(1<<len(qs))-1,len(parts));assert c is not None
        specific[name]={'classes':[[qs[j] for j in range(len(qs)) if p>>j&1] for p in parts],'clique':[qs[j] for j in range(len(qs)) if c>>j&1],'edges':sum(a.bit_count() for a in adj)//2}
    print(json.dumps({'counts':dict(counts),'certificates':certs,'node125':specific,'rank11':targets},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
