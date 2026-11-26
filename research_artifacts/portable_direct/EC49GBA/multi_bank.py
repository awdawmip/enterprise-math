"""EC49GBA exact integer bank contraction; fixed target-label observer."""
from collections import Counter
from random import Random
import json
from residual_frontier import reference


def match(opts, caps, widths):
    """Saturate exclusive ranks, then augment shared targets; return certificate."""
    active = sum(1 << j for j, c in enumerate(caps) if c)
    opts = {t: w & active for t, w in opts.items()}
    banks = []
    offset = 0
    for w in widths:
        banks.append(((1 << w)-1) << offset)
        offset += w
    assert offset == len(caps)
    groups = [[] for _ in banks]
    shared = []
    for t, w in opts.items():
        ids = [i for i, b in enumerate(banks) if w & b]
        if len(ids) == 1:
            groups[ids[0]].append(t)
        elif ids:
            shared.append(t)
    owners = [[] for _ in caps]
    used = set()
    stats = Counter()

    def augment(t, seen):
        w = opts[t]
        while w:
            bit = w & -w
            w ^= bit
            j = bit.bit_length()-1
            if j in seen:
                continue
            seen.add(j)
            stats['resource_visits'] += 1
            if len(owners[j]) < caps[j]:
                owners[j].append(t)
                return True
            for k, old in enumerate(owners[j]):
                if augment(old, seen):
                    owners[j][k] = t
                    return True
        return False

    ranks = []
    for group in groups:
        a = 0
        for t in group:
            if augment(t, set()):
                used.add(t)
                a += 1
        ranks.append(a)
    B = sum(ranks)+len(shared)
    for t in shared:
        # Prefer direct unused resource before exchange paths.
        w = opts[t]
        direct = False
        while w:
            bit = w & -w
            w ^= bit
            j = bit.bit_length()-1
            if len(owners[j]) < caps[j]:
                owners[j].append(t)
                direct = True
                stats['shared_direct'] += 1
                break
        if direct or augment(t, set()):
            used.add(t)
        if not direct:
            stats['shared_exchange_attempts'] += 1
    # Independent Hall certificate: close all unmatched targets under alternating arcs.
    A = set(opts) - used
    todo = list(A)
    W = 0
    while todo:
        w = opts[todo.pop()] & ~W
        W |= w
        while w:
            bit = w & -w
            w ^= bit
            j = bit.bit_length()-1
            for t in owners[j]:
                if t not in A:
                    A.add(t)
                    todo.append(t)
    H = len(used)
    assert {t for group in owners for t in group} == used
    assert sum(map(len, owners)) == H
    assert all(len(group) <= caps[j] and all(opts[t] & (1 << j) for t in group) for j, group in enumerate(owners))
    assert len(A)-sum(c for j,c in enumerate(caps) if W & (1 << j)) == len(opts)-H
    Q = [t for t in shared if opts[t] & ~W == 0]
    # Q is a maximizer of |Q|-sum_i incremental rank_i(Q).
    # Check it against independent exact cut ranks when J is positive.
    if B > H:
        inc = 0
        offset = 0
        for group, width, rank in zip(groups, widths, ranks):
            local = {t: (opts[t] >> offset) & ((1 << width)-1) for t in group+Q}
            inc += reference(local, caps[offset:offset+width])-rank
            offset += width
        assert len(Q)-inc == B-H
    return B, H, Q, stats


def main():
    rng = Random(492611270130)
    hist = Counter(); stats = Counter()
    for i in range(2000):
        widths = [rng.randrange(1,4) for _ in range(2+i%3)]
        caps = [rng.randrange(4) for _ in range(sum(widths))]
        opts = {t: rng.randrange(1 << len(caps)) for t in range(rng.randrange(20))}
        B,H,Q,s = match(opts,caps,widths)
        assert H == reference(opts,caps)
        hist[len(widths)] += 1
        stats.update(s)
    print(json.dumps({'random_graphs_by_banks':dict(hist),'stats':dict(stats)},sort_keys=True))
    hist=Counter();stats=Counter();positive=[];records=json.load(open('witness_records.json'))
    for i,r in enumerate(records):
        caps=r['caps'];opts=r['opts'];w=len(caps)//2
        B,H,Q,s=match(opts,caps,[w,w]);assert H==reference(opts,caps) and (H<=r['L'])==r['ans']
        hist[B-H]+=1;stats.update(s)
        if B>H:positive.append([i,B,H,r['L'],Q])
    print(json.dumps({'records':len(records),'histogram':dict(hist),'stats':dict(stats),'positive_records':positive},sort_keys=True))

if __name__=='__main__':main()
