"""Dense conditional signature cache and physical replay for GAG frontiers."""
from functools import lru_cache
from collections import Counter
from time import perf_counter_ns
import hashlib,json,sys
from multi_target import physical
from recoverable_frontier import antichain
from forced_hole import obs


def indices(s):
    return tuple(i for i in range(s.bit_length()) if s>>i&1)


def pack(x, ids):
    return sum(1<<j for j,i in enumerate(ids) if x>>i&1)


def lift(x, ids):
    return sum(1<<i for j,i in enumerate(ids) if x>>j&1)


def signature(qs, ids):
    f=(1<<len(ids))-1
    a={pack(q,ids) for q in qs}
    return tuple(sorted({min(q,f^q) for q in a if q and q!=f}))


def cache():
    stats=Counter()
    @lru_cache(None)
    def rec(n, qs, d):
        stats['misses']+=1
        f=(1<<n)-1
        if n<=1:return {0:None}
        if not d:return {f:None}
        candidates={}
        for a in qs:
            ia,ib=indices(a),indices(f^a)
            pa,pb=signature(qs,ia),signature(qs,ib)
            left,right=rec(len(ia),pa,d-1),rec(len(ib),pb,d-1)
            stats['products']+=len(left)*len(right)
            la=[(lift(x,ia),x) for x in left]
            lb=[(lift(y,ib),y) for y in right]
            for x,u in la:
                for y,v in lb:
                    candidates.setdefault(x|y,(a,u,v))
            if 0 in candidates:return {0:candidates[0]}
        return {x:candidates[x] for x in antichain(candidates,n)}
    return rec,stats


def representatives(qs, ids):
    f=(1<<len(ids))-1
    reps={}
    for j,q in enumerate(qs):
        p=pack(q,ids)
        if p and p!=f:reps.setdefault(min(p,f^p),(j,p))
    return tuple(sorted(reps)),reps


def replay(rec, st, ids, d, loss, rep, counts):
    # ids are physical state indices, in the same order as the dense key.
    f=(1<<len(ids))-1
    sig,reps=rep(ids)
    witness=rec(len(ids),sig,d)[loss]
    if witness is None:
        assert loss==(0 if len(ids)<=1 else f) and (len(ids)<=1 or d==0)
        counts['leaves']+=1;counts['state_visits']+=len(ids)
        return ['leaf',list(ids)],lift(loss,ids)
    a,u,v=witness
    j,p=reps[a]; r,c=divmod(j,25)
    assert d>0 and p in (a,f^a)
    assert p==sum(1<<h for h,i in enumerate(ids) if obs(st[i],r,c))
    counts['queries']+=1;counts['answer_checks']+=len(ids)
    ia=tuple(ids[h] for h in indices(a));ib=tuple(ids[h] for h in indices(f^a))
    ta,ma=replay(rec,st,ia,d-1,u,rep,counts)
    tb,mb=replay(rec,st,ib,d-1,v,rep,counts)
    assert ma|mb==lift(loss,ids)
    # tree uses actual 0/1 answers, not canonical orientation.
    return [r,c,tb,ta] if p==a else [r,c,ta,tb],ma|mb


def main():
    old=json.load(open('recoverable_frontier.out'))['rows']
    rows=[]; tot=Counter(); shared,ss=cache(); timing=Counter(); rootkeys=set()
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*p=map(int,line.split()); st=list(zip(p[::2],p[1::2])); ids=tuple(range(n))
        t=perf_counter_ns(); qs=physical(st,10,25); sig=signature(qs,ids); timing['input_ns']+=perf_counter_ns()-t
        rootkeys.add((n,sig,k))
        cold,cs=cache();t=perf_counter_ns(); a=cold(n,sig,k);timing['cold_ns']+=perf_counter_ns()-t
        t=perf_counter_ns(); b=shared(n,sig,k);timing['shared_ns']+=perf_counter_ns()-t
        assert set(a)==set(b)==set(old[i]['frontier']) and a==b
        tot['cold_misses']+=cs['misses'];tot['cold_products']+=cs['products']
        tot['cold_hits']+=cold.cache_info().hits
        rows.append(dict(index=i,n=n,k=k,frontier=list(b),cold_misses=cs['misses']))
    tot['shared_misses']=ss['misses'];tot['shared_products']=ss['products'];tot['shared_hits']=shared.cache_info().hits;tot['root_keys']=len(rootkeys)
    before=shared.cache_info().misses
    for row,line in zip(rows,open('ga_nodes.txt')):
        k,n,*p=map(int,line.split());st=list(zip(p[::2],p[1::2]));qs=physical(st,10,25);ids=tuple(range(n));counts=Counter();digest=hashlib.sha256()
        def rep(ids):
            counts['representative_builds']+=1
            return representatives(qs,ids)
        if '--uncached' not in sys.argv:rep=lru_cache(None)(rep)
        t=perf_counter_ns()
        for loss in row['frontier']:
            tree,miss=replay(shared,st,ids,k,loss,rep,counts);assert miss==loss
            digest.update(json.dumps([loss,tree],separators=(',',':')).encode()+b'\n')
            # Independent state-by-state evaluation of actual-answer tree.
            for j,x in enumerate(st):
                node=tree;depth=0
                while node[0]!='leaf':
                    r,c,z,o=node;node=o if obs(x,r,c) else z;depth+=1
                assert depth<=k and j in node[1]
                assert (len(node[1])!=1)==bool(loss>>j&1)
                counts['independent_replays']+=1
            counts['witnesses']+=1
        timing['replay_ns']+=perf_counter_ns()-t
        row.update(counts=counts,tree_sha256=digest.hexdigest());tot.update(counts)
    assert shared.cache_info().misses==before
    print(json.dumps(dict(totals=tot,timing=timing,rows=rows),sort_keys=True))

if __name__=='__main__':main()
