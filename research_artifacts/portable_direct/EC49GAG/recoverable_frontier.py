"""Exact weight-independent minimal missed-set antichain, frozen BRC16943."""
from functools import lru_cache
from collections import Counter, defaultdict
from time import perf_counter_ns
import json
from multi_target import model, physical


def antichain(values, n):
    # Indexed subset tests, with rank order (GAE/GAF specialization).
    postings = [0] * n
    active = 0
    keep = []
    for x in sorted(set(values), key=lambda x: (x.bit_count(), x)):
        cand = active
        missing = ((1 << n) - 1) ^ x
        while cand and missing:
            b = missing & -missing
            cand &= ~postings[b.bit_length() - 1]
            missing ^= b
        if cand:
            continue
        bit = 1 << len(keep)
        active |= bit
        keep.append(x)
        while x:
            b = x & -x
            postings[b.bit_length() - 1] |= bit
            x ^= b
    return tuple(keep)


def missed(n, qs, k):
    full = (1 << n) - 1
    stats = Counter()
    @lru_cache(None)
    def rec(s, d):
        stats['subproblems'] += 1
        if s.bit_count() <= 1:
            return (0,)
        if not d:
            return (s,)
        candidates = set()
        # Duplicate conditional partitions are equivalent for this observer.
        splits = {min(s & q, s & ~q) for q in qs if s & q and s & ~q}
        for a in sorted(splits):
            b = s ^ a
            left, right = rec(a, d-1), rec(b, d-1)
            stats['products'] += len(left) * len(right)
            for x in left:
                for y in right:
                    candidates.add(x | y)
            if 0 in candidates:
                return (0,)
        stats['candidates'] += len(candidates)
        return antichain(candidates, n)
    return rec(full, k), stats


def blocker(fam, n):
    out = (0,)
    for edge in fam:
        if not edge:
            return ()
        new = set()
        for x in out:
            if x & edge:
                new.add(x)
            else:
                e = edge
                while e:
                    b = e & -e
                    new.add(x | b)
                    e ^= b
        out = antichain(new, n)
    return out


def weight(mask, w):
    ans = 0
    while mask:
        b = mask & -mask
        ans += w[b.bit_length()-1]
        mask ^= b
    return ans


def main():
    cases = defaultdict(list)
    for row in json.load(open('deficit_slots.out'))['rows']:
        cases[row['index']].append(row)
    previous = json.load(open('capacity_rank.out'))['nodes']
    counts=Counter(); hist=Counter(); rankhist=Counter(); timings=Counter(); out=[]; witness=None
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*p=map(int,line.split()); st=list(zip(p[::2],p[1::2])); full,qs,cert,split,ref,_=model(n,physical(st,10,25))
        t=perf_counter_ns(); fam,stats=missed(n,qs,k); timings['frontier_ns']+=perf_counter_ns()-t
        counts.update(stats); counts['nodes']+=1;counts['frontier_records']+=len(fam); hist[len(fam)]+=1
        t=perf_counter_ns(); bad=blocker(fam,n); timings['blocker_ns']+=perf_counter_ns()-t
        assert set(blocker(bad,n))==set(fam)
        counts['duality_checks']+=1;counts['obstructions']+=len(bad)
        for b in bad:rankhist[b.bit_count()]+=1
        assert set(b for b in bad if b.bit_count()<=4)==set(previous[i]['antichain'])
        assert min(x.bit_count() for x in fam)==n-previous[i]['score']
        assert all(ref(full,b)>k and all(ref(full,b^(1<<j))<=k for j in range(n) if b>>j&1) for b in bad)
        counts['obstruction_reference_checks']+=len(bad)
        for row in cases[i]:
            w=row['weights'];t=perf_counter_ns(); val=sum(w)-min(weight(x,w) for x in fam);timings['weight_eval_ns']+=perf_counter_ns()-t
            assert val==row['pruned']['value']==row['pruned']['reference'];counts['weighted_checks']+=1
        # Cross-check the whole Boolean function via direct designated-target DP on small nodes.
        if n<=10:
            for a in range(1<<n):
                assert (not all(a&x for x in fam))==(ref(full,a)<=k)
                counts['full_target_checks']+=1
        sizes=sorted(set(x.bit_count() for x in fam))
        if len(sizes)>1:
            counts['nonuniform_nodes']+=1
            if witness is None:
                x=max(fam,key=int.bit_count);w=[int(not (x>>j&1)) for j in range(n)]
                small=[y for y in fam if y.bit_count()==sizes[0]]
                witness=dict(index=i,k=k,n=n,missed=x,weights=w,capacity=sum(w),restricted_capacity=sum(w)-min(weight(y,w) for y in small),frontier=list(fam))
                assert witness['restricted_capacity']<witness['capacity']
        out.append(dict(index=i,n=n,k=k,frontier=list(fam),obstructions=list(bad),missed_sizes=sizes))
    print(json.dumps(dict(counts=counts,frontier_hist=hist,obstruction_rank_hist=rankhist,timings=timings,witness=witness,rows=out),sort_keys=True))


if __name__=='__main__':main()
