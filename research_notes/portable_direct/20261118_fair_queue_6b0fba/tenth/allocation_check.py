"""Shared-budget metadata projections. No coefficient, amplitude, or FFT evaluation."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
import json
from math import comb, prod
from pathlib import Path

TOOL_SHA="a5031cbd860dbb9195e02fa872dc1abbc10e2b27f47a397125749b8078474529"


def load_quotient(repo):
    path=repo/"src/enterprise_math/composition_safe_collapse.py"
    assert sha256(path.read_bytes()).hexdigest()==TOOL_SHA
    spec=spec_from_file_location("finite_quotient",path)
    mod=module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_classes(specifications, hidden_count):
    # One bit per actual band, two bands total. Source identifiers are global.
    groups=[]; key_cost={}; points={}; start=0
    for role,(n,free,allowed) in enumerate(specifications):
        assert not free&allowed
        members=list(range(start,start+n));start+=n
        patterns=[m for m in (1,2,3) if m&~allowed==0]
        for i in members:
            for b in (0,1):
                if allowed>>b&1:
                    key_cost[i,b]=(i*7+b*3+i*b*2)%13
        groups.append(dict(members=members,free=free,patterns=patterns,role=role,silent=False))
        for i in members: points[i]=(role,free)
    # A hidden unit here is one real source/band key, charged exactly once.
    hidden=[]
    for k in range(hidden_count):
        key=(start+k//2,k%2)
        hidden.append(key);key_cost[key]=(k*9+3)%11
    groups.append(dict(members=hidden,free=0,patterns=[1],role=None,silent=True))
    return groups,key_cost,points


def shape_count(g,k):
    # Count by keys and by number of distinct used sources. No profile is generated.
    counts={(0,0):1}
    for m in g['patterns']:
        next_counts=Counter()
        for (used,items),count in counts.items():
            for r in range(min(len(g['members'])-items,(k-used)//m.bit_count())+1):
                next_counts[used+r*m.bit_count(),items+r]+=count
        counts=next_counts
    return counts


def certify(groups,k):
    shapes=[shape_count(g,k) for g in groups]
    caps=[len(g['members'])*max((m.bit_count() for m in g['patterns']),default=0) for g in groups]
    prefix=[1]+[0]*k; widths=[1]; P=0; assignment_bound=0; probes=0
    for i,z in enumerate(shapes):
        local=[0]*(k+1)
        for (t,h),n in z.items():
            P+=n;local[t]+=n
            if not groups[i]['silent'] and h:
                double=t-h
                singles=h-double
                dims=(double,singles//2,(singles+1)//2)
                d=sum(z>0 for z in dims)
                layer_cap=min(len(groups[i]['members']),d*h)
                counts_by_items=Counter(sum(v) for v in product(*(range(u+1) for u in dims)))
                count=0
                for r in range(layer_cap):
                    count+=counts_by_items[r]
                    assignment_bound+=n*(d+2)*count
        tail=sum(caps[i+1:])
        for t in range(max(0,k-caps[i]-tail),k+1):
            probes+=prefix[t]*(k-t-max(0,k-t-tail)+1)
        prefix=[sum(prefix[t-r]*local[r] for r in range(t+1)) for t in range(k+1)]
        widths.append(sum(prefix[max(0,k-sum(caps[i+1:])):]))
    J=sum(widths[1:]);Q=widths[-1]
    return dict(P=P,J=J,Q=Q,stage_units=P+J+Q,admissible_prefixes=widths,
        profile_weight_bucket_probes_bound=probes,
        price_scans_expected=sum(len(g['members'])*len(g['patterns']) for g in groups),
        witness_state_operations_bound=assignment_bound,
        raw_allocations=comb(sum(caps),k))


def local_profiles(g,k):
    pat=g['patterns'];n=len(g['members'])
    def visit(h,keys,items):
        if len(h)==len(pat):
            yield tuple(h),keys
            return
        w=pat[len(h)].bit_count()
        for r in range(min(n-items,(k-keys)//w)+1):
            yield from visit(h+[r],keys+w*r,items+r)
    yield from visit([],0,0)


def raw_keyset(g,i,m):
    if g['silent']:
        return (i,)
    return tuple((i,b) for b in (0,1) if m>>b&1)


def price(g,i,m,prices):
    return sum(prices[v] for v in raw_keyset(g,i,m))


def cheapest_lists(g,k,prices,stats):
    # Stable, bounded insertion, no sorting of all source names.
    lists={}
    for m in g['patterns']:
        entries=[]
        for i in g['members']:
            pair=(price(g,i,m,prices),i)
            j=0
            while j<len(entries) and entries[j]<pair:
                stats['price_comparisons']+=1;j+=1
            if j<len(entries):stats['price_comparisons']+=1
            stats['price_scans']+=1
            if j<k:
                entries.insert(j,pair)
                if len(entries)>k:entries.pop()
        lists[m]=entries
    return lists


def witness(g,h,lists,prices,stats):
    mpat=g['patterns'];total=sum(h)
    multiplicity=1;n=len(g['members'])
    for num in h:
        multiplicity*=comb(n,num);n-=num
    if g['silent']:
        keys=tuple(x for c,x in lists[1][:total])
        return multiplicity,sum(prices[x] for x in keys),keys
    if not total:return 1,0,()
    used=[j for j in range(len(h)) if h[j]]
    pool=sorted({x for j in used for c,x in lists[mpat[j]][:total]})
    dp={(0,)*len(h):(0,())}
    for i in pool:
        new=dict(dp)
        stats['witness_state_operations']+=2*len(dp)
        for state,(cost,keys) in dp.items():
            for j in used:
                stats['witness_state_operations']+=1
                if state[j]==h[j]:continue
                v=state[:j]+(state[j]+1,)+state[j+1:]
                candidate=(cost+price(g,i,mpat[j],prices),keys+raw_keyset(g,i,mpat[j]))
                if v not in new or candidate<new[v]:new[v]=candidate
        dp=new
    cost,keys=dp[tuple(h)]
    return multiplicity,cost,keys


def effect(totals):
    f=1000-sum((r+1)*(2*a+b+3*both) for r,(a,b,both) in enumerate(totals))
    g=1001-sum(2*b+both for a,b,both in totals)-totals[0][0]*totals[-1][1]
    return f,g


def coarse_effect(groups,rows):
    totals=[]
    for g,h in zip(groups,rows):
        if g['silent']:continue
        sums=[0,0,0]
        for m,n in [(0,len(g['members'])-sum(h))]+list(zip(g['patterns'],h)):
            observed=g['free']|m
            for j,mask in enumerate((1,2,3)): sums[j]+=n*int(observed&mask==mask)
        totals.append(sums)
    return effect(totals)


def projected(groups,prices,k,limit=4096):
    proof=certify(groups,k);stats=Counter()
    if proof['stage_units']>limit:
        return proof,dict(stats),None
    tables=[]; caps=[]
    for g in groups:
        lists=cheapest_lists(g,k,prices,stats)
        by_weight=defaultdict(list)
        for h,s in local_profiles(g,k):
            by_weight[s].append((h,*witness(g,h,lists,prices,stats)))
            stats['P']+=1
        tables.append(by_weight)
        caps.append(len(g['members'])*max((p.bit_count() for p in g['patterns']),default=0))
    records={}
    def join(i,used,hs,mass,cost,keys):
        if i==len(groups):
            e=coarse_effect(groups,hs);stats['Q']+=1
            records[hs]=(mass,cost,tuple(sorted(keys)),e)
            return
        remaining=sum(caps[i+1:])
        for w in range(max(0,k-used-remaining),k-used+1):
            stats['profile_weight_bucket_probes']+=1
            for h,m,c,kk in tables[i].get(w,()):
                stats['J']+=1
                join(i+1,used+w,hs+(h,),mass*m,cost+c,keys+kk)
    join(0,0,(),1,0,())
    assert all(stats[x]==proof[x] for x in ('P','J','Q'))
    assert stats['price_scans']==proof['price_scans_expected']
    assert stats['price_comparisons']<=k*stats['price_scans']
    for x in ('witness_state_operations','profile_weight_bucket_probes'):
        assert stats[x]<=proof[x+'_bound']
    return proof,dict(stats),records


def raw_observer(keys,groups,points):
    sets=dict((i,0) for i in points)
    for i,b in keys:
        if i in sets:sets[i]|=1<<b
    hs=[]
    totals=[]
    for g in groups:
        if g['silent']:
            hs.append((sum(e in keys for e in g['members']),))
        else:
            counts=Counter(sets[i] for i in g['members'])
            hs.append(tuple(counts[m] for m in g['patterns']))
            obs=[sets[i]|g['free'] for i in g['members']]
            totals.append(tuple(sum((m&v)==v for m in obs) for v in (1,2,3)))
    return tuple(hs),effect(totals)


def test_case(specifications,hidden,budget,tool,full_t6=False):
    groups,prices,points=build_classes(specifications,hidden)
    k=min(budget,len(prices))
    proof,stats,records=projected(groups,prices,k)
    assert records is not None
    seen={}; domains={}; obsmap={}; optima=[10**9]*3
    for row in combinations(sorted(prices),k):
        key,e=raw_observer(row,groups,points)
        price_total=sum(prices[v] for v in row)
        if key not in seen:seen[key]=[0,price_total,e]
        val=seen[key];val[0]+=1;val[1]=min(val[1],price_total)
        assert val[2]==e
        for i,x in enumerate((*e,max(e))):
            optima[i]=min(optima[i],price_total+x)
        if full_t6:
            domains[row]=key;obsmap[row]=e
    assert set(records)==set(seen)
    for key,(mass,c,keys,e) in records.items():
        assert seen[key]==[mass,c,e]
        assert len(set(keys))==len(keys)==k and all(x in prices for x in keys)
        assert sum(prices[x] for x in keys)==c and raw_observer(keys,groups,points)==(key,e)
    assert sum(m for m,c,keys,e in records.values())==proof['raw_allocations']
    reconstructed=[min(c+(*e,max(e))[i] for mass,c,keys,e in records.values()) for i in range(3)]
    assert reconstructed==optima
    if full_t6:
        assert tool.descends_through(domains,domains,obsmap)
        assert tool.fiber_constancy_witness(domains,domains,obsmap) is None
    best=min((c+max(e),keys,e,c) for mass,c,keys,e in records.values())
    return dict(groups=specifications,hidden=hidden,k=k,proof=proof,measured_metadata=stats,
                minima=optima,joint_witness=best,t6=full_t6)


def counterexamples(tool):
    u=((0,0),(0,1),(1,0),(1,1))
    rows=list(combinations(u,2))
    lanes={r:tuple(sum(b==z for i,b in r) for z in (0,1)) for r in rows}
    aligned={r:int(any((i,0) in r and (i,1) in r for i in (0,1))) for r in rows}
    bad=tool.fiber_constancy_witness(rows,lanes,aligned)
    assert bad and not tool.descends_through(rows,lanes,aligned)
    # In the fibre with one 10 and one 01, the cheapest sources cannot coincide.
    menu={(0,0):0,(0,1):0,(1,0):3,(1,1):7}
    candidates=[r for r in rows if lanes[r]==(1,1) and not aligned[r]]
    actual=min((sum(menu[x] for x in r),r) for r in candidates)
    assert actual[0]==3
    return dict(marginal_failure=bad,separate_list_price=0,true_witness_cost=actual)


def swap_support_test(tool):
    # All Boolean observers on the six two-out-of-four allocations.
    rows=[(1<<a)|(1<<b) for a,b in combinations(range(4),2)]
    checked=0
    for truth in range(1<<len(rows)):
        obs={row:(truth>>i)&1 for i,row in enumerate(rows)}
        equivalent=set()
        for a,b in combinations(range(4),2):
            swap=(1<<a)|(1<<b)
            if all(obs[row]==obs[row^swap] for row in rows if (row&swap).bit_count()==1):
                equivalent.add((a,b))
        admissible=[]
        for kept in range(16):
            forgotten=[j for j in range(4) if not kept>>j&1]
            expected=all(pair in equivalent for pair in combinations(forgotten,2))
            ok=tool.descends_through(rows,{row:row&kept for row in rows},obs)
            assert ok==expected
            if ok:admissible.append(kept.bit_count())
            checked+=1
        max_class=max(1+sum((min(a,b),max(a,b)) in equivalent for b in range(4) if a!=b)
                      for a in range(4))
        assert min(admissible)==4-max_class
    return checked


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path('.'))
    parser.add_argument('--output',type=Path)
    a=parser.parse_args();tool=load_quotient(a.repo)
    small=[]
    for spec,hidden in [([(3,0,3),(2,1,2)],2), ([(1,2,1),(3,0,3)],0),
                        ([(1,0,1),(1,3,0)],3), ([(2,0,3),(1,0,2)],1)]:
        for k in range(5):small.append(test_case(spec,hidden,k,tool,True))
    large=test_case([(6,0,3),(4,0,3)],12,4,tool)
    refused=projected(*build_classes([(1,0,3)]*16,0)[:2],k=4)
    assert refused[2] is None and not refused[1]
    output={'source_tool_sha256':TOOL_SHA,'all_binary_swap_support_tests':swap_support_test(tool),
        'small_cases':len(small),
        'small_allocations':sum(s['proof']['raw_allocations'] for s in small),
        'small_fibres':sum(s['proof']['Q'] for s in small),
        'small_cases_sha256':sha256(json.dumps(small,sort_keys=True).encode()).hexdigest(),
        'larger_exact_fixture':large,'pre_expansion_refusal':refused[:2],
        'counterexamples':counterexamples(tool),'scientific_BRC_operations':0}
    content=json.dumps(output,sort_keys=True,indent=2)+'\n'
    print(content,end='')
    if a.output:a.output.write_text(content)


if __name__=='__main__':
    main()
