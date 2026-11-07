#!/usr/bin/env python3
"""Author-side exact native-prefix constructive local search within EC49FDV schedules.
Science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Not an optimality certificate; costs and validity independently checked.
"""
import json, random, collections, time, itertools, os
from pathlib import Path
from EC49FDV_NATIVE_WITNESSES import word_pool, native, signature, prefixes, verify_full, key, Q

original=json.loads(Path('EC49FDV_NATIVE_CONSTRUCTIONS.json').read_text())
variants=sorted(original,key=lambda r:r['cost'])[:8]
R=random.Random(49321)
records=[]

def search(seed, cycles=170, steps=220):
    baseline=seed['words']; keys=seed['keys']; schedule=seed['schedule']
    fixed={str(h):list(baseline[str(h)]) for h in (2,3)}
    horizons=range(4,10)
    groups=[]
    for h in horizons:
        k=tuple(keys[schedule[h-4]])
        pool=word_pool(h,k)
        for sig in sorted(set(x[1] for x in pool)):
            groups.append((str(h),sig,[w for w,bit in pool if bit==sig]))
    assert sum(len(set(x[1] for x in word_pool(h,tuple(keys[schedule[h-4]]))) ) for h in horizons)==18
    assert all(sum(1 for g in groups if g[0]==str(h))==Q[h] for h in horizons)
    # Build exact prefix masks across finite candidate words (every primitive step in every word).
    wset=set(w for _,_,pool in groups for w in pool) | set(w for ws in fixed.values() for w in ws)
    universe=set().union(*(prefixes(w) for w in wset))
    ids={pr:i for i,pr in enumerate(sorted(universe))}
    def wordmask(w):
        m=0
        for p in prefixes(w):m |= 1<<ids[p]
        return m
    mask={w:wordmask(w) for w in wset}
    fixed_mask=0
    for ws in fixed.values():
        for w in ws:fixed_mask |= mask[w]
    wordgroups=[g[2] for g in groups]
    costs=[]
    for i,g in enumerate(groups):
        assert len([w for w in baseline[g[0]] if signature(w)==g[1]])==1,(g,baseline[g[0]])
        costs.append([baseline[g[0]][next(j for j,w in enumerate(baseline[g[0]]) if signature(w)==g[1])]])
    initial=[arr[0] for arr in costs]
    assert len(initial)==18
    def score(picks):
        u=fixed_mask
        for w in picks:u |= mask[w]
        return u.bit_count()
    def hill(picks,maxpasses=30):
        scores=[]
        for pass_idx in range(maxpasses):
            modified=0
            order=list(range(len(groups)););R.shuffle(order)
            for i in order:
                u=fixed_mask
                for j,w in enumerate(picks):
                    if j!=i:u |= mask[w]
                current=picks[i]; old=(u|mask[current]).bit_count()
                # Tie bias to smaller word (not runtime system)
                best=old; candidates=[current]
                for w in wordgroups[i]:
                    if w==current:continue
                    v=(u|mask[w]).bit_count()
                    if v<best:best=v;candidates=[w]
                    elif v==best and v<old:candidates.append(w)
                new=R.choice(candidates)
                if best<old and new!=current:picks[i]=new;modified+=1
            if not modified:break
        return picks
    best=hill(initial.copy())
    bestcost=score(best)
    baseline_cost=score(initial)
    trial=best[:]
    for t in range(cycles):
        if t%12==0:trial=best[:]
        for i in R.sample(range(len(groups)),R.choice([2,3,4,5,6])):
            trial[i]=R.choice(wordgroups[i])
        trial=hill(trial[:],maxpasses=12)
        current=score(trial)
        if current<bestcost:
            bestcost=current;best=trial[:]
            print('best',seed['cost'],'->',bestcost,'t',t,flush=True)
        # keep slightly worse states for diversification, reset every 12 iters
    system={h:ws[:] for h,ws in fixed.items()}
    for (h,s,pool),w in zip(groups,best):system.setdefault(h,[]).append(w)
    cost,all_keys=verify_full(system)
    assert cost==bestcost and len(all_keys)==5
    record={'source_baseline_cost':seed['cost'],'cost':cost,'keys':seed['keys'],'switch_after':seed['switch_after'],
            'schedule':schedule,'early_seed':{h:fixed[h] for h in ('2','3')},'words':system,'all_keys':[list(k) for k in all_keys],
            'method':'seeded stochastic 1-block exact primitive-prefix coordinate descent; verified explicit full witness; not optimum',
            'candidate_pool_sizes':{f'H{h}/{sig}':len(pool) for h,sig,pool in groups}}
    return record

if __name__=='__main__':
    ts=time.time()
    for i,x in enumerate(variants):
        print('variant',i,'base',x['cost'],'keys',x['keys'],flush=True)
        rec=search(x,cycles=int(os.getenv('CYCLES','80')))
        records.append(rec)
        Path('EC49FDW_SEARCH_WITNESSES_FAST.json').write_text(json.dumps(records,indent=2)+'\n')
    print('min',min(r['cost'] for r in records),'time',time.time()-ts,flush=True)
