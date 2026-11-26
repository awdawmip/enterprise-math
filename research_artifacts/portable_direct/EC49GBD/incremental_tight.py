"""Exact incremental largest tight cut, with raw labels retained separately."""
from collections import Counter
from random import Random
from time import perf_counter
from reverse_tight import bits, banks, enum_tight, reverse_tight
import json, hashlib

class Dynamic:
    def __init__(self,caps):
        self.caps=caps; self.m=len(caps); self.full=(1<<self.m)-1
        self.live=sum(1<<j for j,c in enumerate(caps) if c)
        self.free=self.live; self.h=0; self.opts={}
        self.owners=[[] for c in caps]; self.out=[0]*self.m;self.pred=[0]*self.m
        self.stats=Counter()
    def back(self,seed,allowed):
        reach=todo=seed
        while todo:
            b=todo&-todo;todo^=b
            j=b.bit_length()-1
            new=self.pred[j]&allowed&~reach
            reach|=new;todo|=new
        return reach
    def insert(self,t,mask):
        assert t not in self.opts
        self.opts[t]=mask
        self.stats['insertions']+=1
        if not mask&self.live:
            self.stats['blocked']+=1
            return self.full^self.live,self.h
        # Search without changing the matching. A successful path is a list
        # of (resource, owner index, new occupant); terminal index is None.
        seen=0
        def search(u):
            nonlocal seen
            for j in bits(self.opts[u]&self.live&~seen):
                b=1<<j
                if seen&b:continue
                seen|=b
                if self.free&b:return [(j,None,u)]
                for k,v in enumerate(self.owners[j]):
                    p=search(v)
                    if p is not None:return [(j,k,u)]+p
            return None
        path=search(t);assert path is not None
        changed=sum(1<<j for j,k,u in path)
        self.stats['successful']+=1
        self.stats['full_live_scan_budget']+=self.live.bit_count()
        self.stats['path_vertices']+=len(path)
        # Direct insertion leaving a free slot cannot alter any old route.
        last=path[-1][0]
        shortcut=len(path)==1 and len(self.owners[last])+1<self.caps[last]
        affected=0 if shortcut else self.back(changed,self.live)
        self.stats['affected_vertices']+=affected.bit_count()
        self.stats['free_shortcut']+=shortcut
        for j,k,u in path:
            if k is None:self.owners[j].append(u)
            else:self.owners[j][k]=u
        self.h+=1
        if len(self.owners[last])==self.caps[last]:self.free&=~(1<<last)
        # Update only the outgoing rows altered by augmentation.
        for j,k,u in path:
            row=0
            for v in self.owners[j]:row|=self.opts[v]&self.live
            for b in bits(self.out[j]^row):
                self.pred[b]^=1<<j
            self.out[j]=row
        if not shortcut:
            outside=self.live&~affected
            seeds=self.free&affected
            for j in bits(affected):
                if self.out[j]&outside:seeds|=1<<j
            keep=self.back(seeds,affected)
            lost=affected&~keep
            self.stats['newly_blocked']+=lost.bit_count()
            self.live&=~lost
            # Stale rows to removed resources are harmless: all traversals
            # are masked to live. Keep owners and labels for provenance.
        return self.full^self.live,self.h

def run(opts,caps,ref=True):
    D=Dynamic(caps);prefix={};out=[]
    for t,mask in opts.items():
        prefix[t]=mask
        val=D.insert(t,mask);out.append(val)
        if ref:assert val==enum_tight(prefix,caps),(opts,caps,prefix,val)
    assert (D.full^D.live,D.h)==enum_tight(opts,caps) if ref else True
    return D.stats,out

def main():
    rng=Random(492611270430);sr=Counter();sf=Counter();digest=hashlib.sha256()
    for i in range(3000):
        m=rng.randrange(10);caps=[rng.randrange(4) for _ in range(m)]
        active=sum(1<<j for j,c in enumerate(caps) if c)
        opts={t:rng.randrange(1<<m)&active for t in range(rng.randrange(26))}
        for o in (opts,dict(reversed(list(opts.items())))):
            stats,_=run(o,caps);sr.update(stats)
    records=json.load(open('witness_records.json'))
    cases=[g for r in records for g in banks(r['opts'],r['caps'],[len(r['caps'])//2]*2)]
    for opts,caps in cases:
        stats,out=run(opts,caps);sf.update(stats)
        digest.update((json.dumps(out,separators=(',',':'))+'\n').encode())
    def dynamic_all():
        for opts,caps in cases:run(opts,caps,False)
    def recompute_all():
        for opts,caps in cases:
            p={}
            for t,mask in opts.items():p[t]=mask;reverse_tight(p,caps)
    timings=[]
    for i in range(3):
        row={}
        for f in ((dynamic_all,recompute_all) if i%2==0 else (recompute_all,dynamic_all)):
            start=perf_counter();f();row[f.__name__]=perf_counter()-start
        timings.append(row)
    D=Dynamic([1]*400)
    for t in range(400):assert D.insert(t,1<<t)==((1<<(t+1))-1,t+1)
    print(json.dumps(dict(random_graphs=3000,random_orders=6000,random_stats=sr,records=len(records),banks=len(cases),frozen_stats=sf,prefix_output_sha256=digest.hexdigest(),timings=timings,wide_analytic_stats=D.stats,mismatches=0),sort_keys=True))
if __name__=='__main__':main()
