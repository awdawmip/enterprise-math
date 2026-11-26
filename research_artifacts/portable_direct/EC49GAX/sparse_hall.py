"""GAX: exact <=3-target Hall witnesses, followed by GAV threshold fallback."""
from collections import Counter
from itertools import combinations
from random import Random
from time import perf_counter_ns
import json
import threshold_hall as prev
from witness_hall import verify
from gal_path_hall import Bound


def sparse(opts,caps,L):
    k=len(opts)-L
    if k<=0:return []
    if k>3:return None
    active=sum(1<<j for j,c in enumerate(caps) if c)
    ones=[1<<j for j,c in enumerate(caps) if c==1]
    twos=[1<<j for j,c in enumerate(caps) if c==2]
    freq=Counter(m&active for m in opts.values())
    z=freq[0]
    def take(w,s):
        return [t for t,m in opts.items() if (m&active)&~w==0][:s]
    if z>=k:return take(0,k)
    if k<=2:
        for a in ones:
            if z+freq[a]>=k+1:return take(a,k+1)
    if k==1:
        for a in twos:
            if z+freq[a]>=3:return take(a,3)
        for a,b in combinations(ones,2):
            if z+freq[a]+freq[b]+freq[a|b]>=3:return take(a|b,3)
    return None


def run():
    rng=Random(49261130);checks=0
    for _ in range(2000):
        m=rng.randrange(1,9);n=rng.randrange(0,15);caps=[rng.randrange(5) for _ in range(m)];opts={i:rng.randrange(1<<m) for i in range(n)}
        minimum={}
        for s in range(1,min(n,3)+1):
            for a in combinations(opts,s):
                w=0
                for t in a:w|=opts[t]
                deficit=s-sum(c for j,c in enumerate(caps) if w>>j&1)
                for k in range(1,deficit+1):minimum.setdefault(k,s)
        for k in range(1,5):
            if k>n:continue
            L=n-k;w=sparse(opts,caps,L)
            assert (None if w is None else len(w))==minimum.get(k)
            if w is not None:assert verify(opts,caps,L,True,w)
            checks+=1
    records=json.load(open('witness_records.json'));hist=Counter();tested=0
    for r in records:
        opts={int(t):v for t,v in r['opts'].items()};caps=r['caps'];L=r['L'];w=sparse(opts,caps,L)
        expect=r['ans'] and len(r['min'])<=3
        assert (w is not None)==expect
        if w is not None:
            assert verify(opts,caps,L,True,w) and len(w)==len(r['min']);hist[len(w)]+=1
        tested+=1
    base=prev.at_most
    def wrapped(opts,caps,L,st):
        st['sparse_calls']+=1
        w=sparse(opts,caps,L)
        if w is not None:
            st['sparse_hits']+=1;st['sparse_targets']+=len(w);return True
        return base(opts,caps,L,st)
    old=json.load(open('gap_target.json'))['rows'];out={}
    for mode,fn in [('baseline',base),('sparse',wrapped),('sparse',wrapped),('baseline',base)]:
        prev.at_most=fn;agg=Counter();search=Counter();rows=[];elapsed=0
        for i,line in enumerate(open('ga_nodes.txt')):
            k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
            for j in range(2):
                d=k+j;r=old[2*i+j];o=prev.ThresholdOracle(b,st);t0=perf_counter_ns();assert o.v(b.full,d,b.full)==r['cap'];assert o.graphs(d,r['qs'],r['goals'])==r['adj'];elapsed+=perf_counter_ns()-t0
                agg.update(o.threshold_stats);search.update(o.stats);rows.append(dict(o.threshold_stats))
            b.clear()
        out.setdefault(mode,[]).append({'stats':dict(agg),'search':dict(search),'ns':elapsed,'rows':rows})
    assert all(r['search']==out['baseline'][0]['search'] for runs in out.values() for r in runs)
    print(json.dumps({'synthetic_models':2000,'synthetic_thresholds':checks,'record_checks':tested,'sparse_hist':dict(hist),'runs':out},separators=(',',':')))
if __name__=='__main__':run()
