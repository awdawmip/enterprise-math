"""Exact scheduling, working W10 metadata fixture and full raw witness audit."""
import argparse
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations,combinations_with_replacement,permutations
from pathlib import Path
import json

@lru_cache(None)
def poly(group,k):
    n,d=group
    if d==0: return (1,)+(0,)*k
    if d==1: return tuple(int(i<=n) for i in range(k+1))
    # x double masks leave w-2*x single masks, with w-2*x+1 ways to split them.
    return tuple(sum(w-2*x+1 for x in range(max(0,w-n),w//2+1)) for w in range(k+1))

@lru_cache(None)
def width(prefix,remaining_capacity,k):
    h=[1]+[0]*k
    for g in prefix:
        v=poly(g,k)
        h=[sum(h[i]*v[j-i] for i in range(j+1)) for j in range(k+1)]
    return sum(h[max(0,k-remaining_capacity):])

def join(order,k):
    capacity=sum(n*d for n,d in order)
    total=0
    for i,(n,d) in enumerate(order,1):
        capacity-=n*d
        total+=width(tuple(sorted(order[:i])),min(capacity,k),k)
    return total

def canonical(gs,k):
    null = []
    buckets = {d: [[] for _ in range(k+1)] for d in (1,2)}
    for n,d in gs:
        if not n or not d:
            null.append((n,d))
        else:
            buckets[d][min(k,n)].append((n,d))
    single = [g for bucket in buckets[1] for g in bucket]
    double = [g for bucket in buckets[2] for g in bucket]
    if k<4: return [tuple(null+single+double)]
    small=[g for g in single if g[0]<4]
    high=[g for g in single if g[0]>=4]
    little=[g for g in double if g[0]==1]
    rest=[g for g in double if g[0]>=2]
    first=tuple(null+small+high+little+rest)
    if not high or not little: return [first]
    alt=tuple(null+small+little[:1]+high+little[1:]+rest)
    c=sum(n for n,d in small)
    a,b=len(high),len(little)
    if not rest and b==1: return [first]
    if a==1 and c<=1: return [alt]
    if (a==1 and c==2) or (a==2 and not c): return [first,alt]
    return [first]

def brute_small():
    # All unlabelled words in eight relevant capped types up to 5 groups.
    types=[(n,d) for d in (1,2) for n in (1,2,3,4)]
    inputs=words=0
    for size in range(1,6):
        for gs in combinations_with_replacement(types,size):
            orders=set(permutations(gs))
            for k in range(min(4,sum(n*d for n,d in gs))+1):
                best=min(join(v,k) for v in orders)
                winners=set(canonical(gs,k))
                assert all(join(order,k)==best for order in winners)
                if k==4:
                    small=[g for g in gs if g[1]==1 and g[0]<4]
                    high=[g for g in gs if g[1]==1 and g[0]>=4]
                    little=[g for g in gs if g[1]==2 and g[0]==1]
                    rest=[g for g in gs if g[1]==2 and g[0]>=2]
                    if high and little:
                        choices=[tuple(small+high+little+rest),tuple(small+little[:1]+high+little[1:]+rest)]
                        assert winners=={v for v in choices if join(v,k)==best}
                inputs+=1;words+=len(orders)
    return {'instances':inputs,'admissible_orders_tested':words}

def old_fixture(path, repo):
    digest = sha256(path.read_bytes()).hexdigest()
    assert digest == "0e4b0e4a2076e13d2dfae2bc1ec69a82ab145c6ed2bb75ae2cb8b358d27698a6"
    spec=spec_from_file_location('w10',path)
    m=module_from_spec(spec);spec.loader.exec_module(m)
    tool=m.load_quotient(repo)
    original=m.coarse_effect
    def check(sizes,hidden,orders):
        gs,prices,points=m.build_classes([(n,0,3) for n in sizes],hidden)
        raw={};seen={};effects={}
        for row in combinations(sorted(prices),4):
            label,e=m.raw_observer(row,gs,points)
            cost=sum(prices[x] for x in row)
            if label not in raw:raw[label]=[0,cost,e]
            raw[label][0]+=1;raw[label][1]=min(raw[label][1],cost)
            assert raw[label][2]==e
            seen[row]=label;effects[row]=e
        assert tool.descends_through(seen,seen,effects)
        assert tool.fiber_constancy_witness(seen,seen,effects) is None
        optima = [
            min(cost + (effect[0], effect[1], max(effect))[i] for _,cost,effect in raw.values())
            for i in range(3)
        ]
        output=[]
        for order in orders:
            perm=[gs[i] for i in order]
            def orig(h):return tuple(h[order.index(j)] for j in range(len(gs)))
            # Reorder metadata joins while restoring the frozen observer's role order.
            m.coarse_effect=lambda groups,hs:original(gs,orig(hs))
            try:
                proof,stats,records=m.projected(perm,prices,4)
            finally:
                m.coarse_effect=original
            signature=tuple((len(g['members']),max((mask.bit_count() for mask in g['patterns']),default=0)) for g in perm)
            assert proof['J']==join(signature,4)
            if records is not None:
                assert len(records)==len(raw)
                for h,(mult,c,keys,e) in records.items():
                    key=orig(h);assert [mult,c,e]==raw[key]
                    assert len(set(keys))==4 and sum(prices[u] for u in keys)==c
                    assert m.raw_observer(keys,gs,points)==(key,e)
            else: assert proof['stage_units']>4096 and not stats
            output.append({'order':order,'P':proof['P'],'J':proof['J'],'Q':proof['Q'],
                           'stage_units':proof['stage_units'],'prefixes':proof['admissible_prefixes'],
                           'weight_probes':stats.get('profile_weight_bucket_probes'),
                           'accepted':records is not None, 'executed_metadata_counts':dict(stats)})
        return {'all_raw_allocations':len(seen),'observer_fibres':len(raw),'orders':output, 'verified_raw_minima':optima}
    return {'w10':check([6,4],12,list(permutations(range(3)))),
            'separate_metadata_example':check([3,1,1,1,1,1],2,[tuple(range(7)),(6,1,2,3,4,5,0)]),'tool_sha256':m.TOOL_SHA,
            'w10_harness_sha256':sha256(path.read_bytes()).hexdigest()}

def probe_counterexample():
    # The underlying groups offer one and four keys respectively.
    groups=[(1,1),(2,2)]
    records=[]
    for order in permutations(groups):
        prefix=[1,0,0,0,0]
        tail=sum(n*d for n,d in order)
        probes=0
        for n,d in order:
            tail-=n*d
            for t in range(max(0,4-n*d-tail),5):
                probes+=prefix[t]*(5-t-max(0,4-t-tail))
            g=poly((n,d),4)
            prefix=[sum(prefix[i]*g[j-i] for i in range(j+1)) for j in range(5)]
        records.append({'types':order,'J':join(order,4),'bucket_probes':probes})
    assert [(r['J'],r['bucket_probes']) for r in records]==[(5,7),(6,5)]
    return records


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w10",type=Path,default=Path(__file__).resolve().parents[1]/"tenth"/"allocation_check.py")
    parser.add_argument("--repo",type=Path,default=Path.cwd(),help="repository with the frozen T6 source")
    args=parser.parse_args()
    result={'algebra':brute_small(),**old_fixture(args.w10,args.repo)}
    groups=[(4,1),(4,1),(1,2),(1,2)]
    result['nonadjacent_optima']=[{'types':v,'J':join(v,4)} for v in sorted(set(permutations(groups)))]
    result['J_and_probes_tradeoff']=probe_counterexample()
    print(json.dumps(result,sort_keys=True,indent=2))
