"""EC49GBB: exact exclusive maximal-tight-cut reduction, fixed labeled observer."""
from collections import Counter
from random import Random
from itertools import combinations
import json
from residual_frontier import reference, counts, cut_costs


def reduce_graph(opts,caps,widths):
    active=sum(1<<j for j,c in enumerate(caps) if c)
    opts={t:w&active for t,w in opts.items()}
    banks=[];off=0
    for w in widths:
        banks.append(((1<<w)-1)<<off);off+=w
    assert off==len(caps)
    exclusive=[{} for _ in widths];shared={};zeros=[]
    for t,w in opts.items():
        ids=[i for i,b in enumerate(banks) if b&w]
        if len(ids)==1:exclusive[ids[0]][t]=w
        elif ids:shared[t]=w
        else:zeros.append(t)
    blocked=0;fixed=0;deficit=0;dead_excl=set();off=0
    for u,width in zip(exclusive,widths):
        f=counts((w>>off for w in u.values()),width)
        c=cut_costs(caps[off:off+width]);d=max(a-b for a,b in zip(f,c));W=0
        for j,(a,b) in enumerate(zip(f,c)):
            if a-b==d:W|=j
        assert f[W]-c[W]==d
        global_W=W<<off
        dead_excl.update(t for t,w in u.items() if w&~global_W==0)
        fixed+=c[W];deficit+=d;blocked|=global_W;off+=width
    live_shared={t:w&~blocked for t,w in shared.items()}
    loops=[t for t,w in live_shared.items() if not w]
    live={t:w&~blocked for t,w in opts.items() if t not in dead_excl and w&~blocked}
    # Remaining positive-capacity coordinates renumbered, retain original label mapping.
    keep=[j for j,c in enumerate(caps) if c and not (blocked>>j&1)]
    reduced={t:sum(1<<i for i,j in enumerate(keep) if w>>j&1) for t,w in live.items()}
    rcaps=[caps[j] for j in keep]
    H=fixed+reference(reduced,rcaps)
    B=sum(map(len,exclusive))-deficit+len(shared)
    stats={'exclusive_deleted':len(dead_excl),'fixed_credit':fixed,'shared':len(shared),'shared_loops':len(loops),'shared_edges_removed':sum((w&blocked).bit_count() for w in shared.values()),'resources_removed':(active&blocked).bit_count(),'resources_before':active.bit_count(),'shared_edges_before':sum(w.bit_count() for w in shared.values()),'residual_after_loops':B-H-len(loops)}
    return B,H,loops,stats,blocked,exclusive,shared,fixed,reduced,rcaps


def main():
    rng=Random(492611270230);test=0
    for i in range(1500):
        widths=[rng.randrange(1,4) for _ in range(2+i%3)];caps=[rng.randrange(4) for _ in range(sum(widths))];opts={t:rng.randrange(1<<len(caps)) for t in range(rng.randrange(20))}
        B,H,loops,st,blocked,exclusive,shared,fixed,reduced,rcaps=reduce_graph(opts,caps,widths);assert H==reference(opts,caps);assert st['residual_after_loops']>=0
        # Verify all small shared subsets against the original full graph, keeping exclusive targets fixed.
        if len(shared)<=5:
            u={t:w for group in exclusive for t,w in group.items()};xs=list(shared)
            for mask in range(1<<len(xs)):
                sub=dict(u);sub.update({t:shared[t] for j,t in enumerate(xs) if mask>>j&1})
                # Reuse the SAME blocked cut and coordinate map for every subset.
                assert fixed+reference({t:w for t,w in reduced.items() if t in sub},rcaps)==reference(sub,caps);test+=1
    print(json.dumps({'random_graphs':1500,'subset_checks':test},sort_keys=True))
    records=json.load(open('witness_records.json'));st=Counter();hist=Counter();positive=[];after=[]
    for i,r in enumerate(records):
        caps=r['caps'];opts=r['opts'];w=len(caps)//2
        B,H,loops,s,blocked,exclusive,shared,fixed,reduced,rcaps=reduce_graph(opts,caps,[w,w]);assert H==reference(opts,caps) and (H<=r['L'])==r['ans'];assert s['residual_after_loops']>=0
        st.update(s);hist[(B-H,len(loops))]+=1
        if B>H:positive.append([i,B,H,loops,blocked])
        if s['residual_after_loops']:
            u={t:w for group in exclusive for t,w in group.items()};xs=[t for t in shared if t not in loops];base=reference(u,caps);j=s['residual_after_loops']
            witness=None
            for k in range(2,len(xs)+1):
                for q in combinations(xs,k):
                    if base+k-reference(dict(u,**{t:shared[t] for t in q}),caps)==j:
                        witness=list(q);break
                if witness is not None:break
            assert witness is not None
            after.append([i,j,witness])
    print(json.dumps({'records':len(records),'stats':dict(st),'histogram':{str(k):v for k,v in sorted(hist.items())},'positive_records':positive,'after_loop_records':after},sort_keys=True))
if __name__=='__main__':main()
