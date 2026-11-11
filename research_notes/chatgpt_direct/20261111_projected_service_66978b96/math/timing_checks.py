"""Independent enumeration: all partitions, all allowed binary tests; no use of theorem in optimizer."""
import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path


def parts(N):
    cells = []
    def gen(i):
        if i == N:
            yield tuple(cells)
        else:
            bit=1<<i
            for k in range(len(cells)):
                cells[k] |= bit
                yield from gen(i+1)
                cells[k] ^= bit
            cells.append(bit)
            yield from gen(i+1)
            cells.pop()
    yield from gen(0)


def span(rows):
    V={0}
    for r in rows:
        V |= {v ^ r for v in V}
    return tuple(sorted(V))


def count(n, family):
    N=2**n; B=tuple(parts(N)); rows=tuple(range(1,N)); views=0
    tests={j:sum(1<<h for h in range(N) if ((h==j) if family=='star' else ((h&j).bit_count()%2))) for j in rows}
    if family=='linear':
        spaces={}
        for k in range(n+1):
            for ds in itertools.combinations(rows,k):
                V=span(ds)
                if len(V)==2**k: spaces.setdefault(V,[]).append(ds)
        demands={k:[sets[0] for V,sets in spaces.items() if len(V)==2**k] for k in range(n+1)}
        # All tests available. Equal row space gives equal partition of outputs even for different bases.
    else:
        demands={k:list(itertools.combinations(rows,k)) for k in range(N)}
    result=[]
    for k, demands_k in demands.items():
        # partition costs separately for each alternative demand
        worst=[0]*len(B); ahead=[0]*(n+1)
        for d in demands_k:
            @lru_cache(None)
            def solve(w):
                if all(not (w & tests[j]) or not (w & ~tests[j]) for j in d):return 0
                return min(1+max(solve(y),solve(z)) for j in rows for y,z in [(w&tests[j],w&~tests[j])] if y and z)
            costs=[max(solve(w) for w in b) for b in B]
            worst=[max(x,y) for x,y in zip(worst,costs)]
            for s in range(n+1):
                ahead[s]=max(ahead[s], min(c for c,b in zip(costs,B) if len(b)<=2**s))
            views+=len(B)
        for s in range(n+1):
            blind=min(c for c,b in zip(worst,B) if len(b)<=2**s)
            if family=='linear':
                assert ahead[s]==max(0,k-s) and blind==min(k,n-s)
            else:
                assert ahead[s]==(k>>s) and blind==min(k,(N-1)>>s)
            result.append(dict(demand_size_or_rank=k,bits=s,announced=ahead[s],unannounced=blind))
    return dict(worlds=N,partitions=len(B),distinct_demands=sum(map(len,demands.values())),
                partition_demand_pairs=views,results=result)


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('timing_results.json'));a=p.parse_args()
    out={'status':'PASS','scope':'control enumeration; all physical marker columns available; one representative basis per linear demand subspace', 'families':{}}
    for n in (1,2,3):
        for family in ('linear','star'):out['families'][f'{family}_{n}']=count(n,family)
    out['total_partition_demand_pairs']=sum(v['partition_demand_pairs'] for v in out['families'].values())
    a.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('PASS',out['total_partition_demand_pairs'])
if __name__=='__main__':main()
