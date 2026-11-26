"""EC49GBE: disjoint unit-slack blocks and single-edge cut certificates.
Run from the verified EC49GBD reproduction archive. Integer mask observer only.
"""
import json, hashlib
from random import Random
from collections import Counter
from itertools import combinations
from reverse_tight import bits, enum_tight, banks
from residual_frontier import counts, cut_costs, reference
from incremental_tight import Dynamic

def reduce_bank(opts,caps):
    W,h=enum_tight(opts,caps)
    keep=[j for j,c in enumerate(caps) if c and not (W>>j&1)]
    p={t:sum(1<<i for i,j in enumerate(keep) if w>>j&1) for t,w in opts.items() if w&~W}
    return W,h,p,[caps[j] for j in keep],keep

def enum_blocks(opts,caps):
    s=[c-f for c,f in zip(cut_costs(caps),counts(opts.values(),len(caps)))]
    assert s[0]==0 and all(v>=1 for v in s[1:])
    one=[w for w,v in enumerate(s) if v==1]
    blocks=sorted(w for w in one if not any(w!=v and w&~v==0 for v in one))
    assert all(not a&b for a,b in combinations(blocks,2))
    return blocks,s,one

def edge_blocks(opts,caps):
    m=len(caps); D=Dynamic(caps)
    for t,w in opts.items(): D.insert(t,w)
    assert D.h==len(opts) and D.live==(1<<m)-1
    # Reverse graph with unique edge IDs and integer capacities.
    # Resource -> occupant costs one; occupant -> allowed resource costs >1.
    sink=m+len(opts); pred=[[] for _ in range(sink+1)]; unit=[]; eid=0
    def edge(a,b,c):
        nonlocal eid
        pred[b].append((a,eid));
        if c==1:unit.append(eid)
        eid+=1
    tnodes={t:m+i for i,t in enumerate(opts)}
    for j,os in enumerate(D.owners):
        for t in os:
            edge(j,tnodes[t],1)
            for k in bits(opts[t]):edge(tnodes[t],k,2)
        free=caps[j]-len(os)
        if free:edge(j,sink,free)
    def lost(skip):
        seen={sink}; todo=[sink]
        while todo:
            j=todo.pop()
            for k,i in pred[j]:
                if i!=skip and k not in seen:seen.add(k);todo.append(k)
        return sum(1<<j for j in range(m) if j not in seen)
    assert lost(-1)==0
    cand=set(lost(i) for i in unit)-{0}
    return sorted(w for w in cand if not any(w!=v and w&~v==0 for v in cand)),len(unit)

def check_bank(opts,caps,stats,all_insert=False):
    W,h,p,c,keep=reduce_bank(opts,caps)
    bl,s,one=enum_blocks(p,c); eg,edges=edge_blocks(p,c);assert bl==eg
    stats.update(banks=1,live_resources=len(c),unit_cuts=len(one),blocks=len(bl),covered=sum(v.bit_count() for v in bl),edge_probes=edges,enumerated_cuts=len(s))
    stats['nonempty_block_banks']+=bool(bl)
    for w in bl:stats[f'block_size_{w.bit_count()}']+=1
    if all_insert:
        for mask in range(1,1<<len(c)):
            pred=next((b for b in bl if mask&~b==0),0)
            q=dict(p); q['__new__']=mask
            assert enum_tight(q,c)==(pred,len(p)+1)
            stats['single_insertion_checks']+=1
    return W,[sum(1<<keep[j] for j in bits(b)) for b in bl]

def main():
    rng=Random(492611270533); rand=Counter(); frozen=Counter(); pair=Counter(); hist=Counter(); pos=[]; digest=hashlib.sha256()
    for _ in range(1600):
        m=rng.randrange(8);c=[rng.randrange(4) for j in range(m)];active=sum(1<<j for j,v in enumerate(c) if v)
        p={str(i):rng.randrange(1<<m)&active for i in range(rng.randrange(18))}
        check_bank(p,c,rand,True)
    rec=json.load(open('witness_records.json'))
    for i,r in enumerate(rec):
        caps=r['caps'];opts=r['opts'];q=len(caps)//2;active=sum(1<<j for j,c in enumerate(caps) if c)
        uvs=banks(opts,caps,[q,q]); W=0;blocks=[];u={}
        for j,(p,c) in enumerate(uvs):
            w,bl=check_bank(p,c,frozen,False);W|=w<<(j*q);blocks.extend(b<<(j*q) for b in bl);u.update({t:v<<(j*q) for t,v in p.items()})
        sh={t:(v&active&~W) for t,v in opts.items() if t not in u and v&active}
        loops=sum(v==0 for v in sh.values());live={t:v for t,v in sh.items() if v}
        ids={t:next((b for b in blocks if v&~b==0),0) for t,v in live.items()}
        # rank of every live shared pair, independently checked with original exclusive graph
        base=reference(u,caps)
        for a,b in combinations(live,2):
            p=dict(u);p[a]=opts[a]&active;p[b]=opts[b]&active
            expected=1 if ids[a] and ids[a]==ids[b] else 2
            assert reference(p,caps)-base==expected
            pair['pairs']+=1;pair['dependent_pairs']+=expected==1
        count=Counter(v for v in ids.values() if v)
        lb=sum(v-1 for v in count.values());H=reference(opts,caps);J=base+len(sh)-H;liveJ=J-loops
        assert 0<=lb<=liveJ
        hist[(liveJ,lb)]+=1
        if liveJ:pos.append(dict(record=i,live_residual=liveJ,pair_lb=lb,block_ids=ids,blocks=blocks,blocked=W))
        digest.update((json.dumps([i,W,blocks,ids,liveJ,lb],sort_keys=True)+'\n').encode())
    print(json.dumps(dict(random_graphs=1600,random=rand,records=len(rec),frozen=frozen,pairs=pair,live_residual_vs_pair_lower_bound={str(k):v for k,v in sorted(hist.items())},frozen_output_sha256=digest.hexdigest(),positive_records=pos,mismatches=0),sort_keys=True))
    # Same singleton/pair signatures, different triple rank: U2,3 versus U3,3.
    p={'e':7};c=[1,1,1]; assert enum_blocks(p,c)[0]==[1,2,4]
    for k in (1,2,3):
        for subset in combinations(range(3),k):
            x={str(j):1<<j for j in subset}; assert reference(dict(p,**x),c)-1==min(k,2);assert reference(x,c)==k
    print(json.dumps(dict(triple_counterexample='three unit resources; one exclusive target with mask 7 versus no exclusive targets',single_and_pair_equal=True,triple_ranks=[2,3])))
if __name__=='__main__':main()
