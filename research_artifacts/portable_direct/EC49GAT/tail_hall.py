"""EC49 continuation: exact sparse binomial-tail matching for interval banks."""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from random import Random
from time import perf_counter_ns
import json
from joint_hall import HallOracle
from gal_path_hall import Bound, bitlist

@lru_cache(None)
def tail_layout(d,n):
    # n>0; return rich interval (or None), scarce (index, capacity).
    tails=[]; c=1
    for j in range(d//2+1):
        if c>=n:
            return (j,d-j), tuple(tails)
        tails.append((j,c))
        if d-j!=j: tails.append((d-j,c))
        c=c*(d-j)//(j+1)
    return None,tuple(tails)

def match(opts,caps):
    occ=[[] for _ in caps]
    def aug(t,seen):
        for j in opts[t]:
            if j in seen: continue
            seen.add(j)
            if len(occ[j])<caps[j]:
                occ[j].append(t); return True
            for i,u in enumerate(occ[j]):
                if aug(u,seen):
                    occ[j][i]=t; return True
        return False
    return sum(aug(t,set()) for t in sorted(opts,key=lambda t:len(opts[t])))

def sparse(d,ivs,stats=None):
    # ivs: target -> pair of intervals, None means no eligibility.
    n=len(ivs)
    if not n:return 0
    rich,tails=tail_layout(d,n)
    paid=0; opts={}; m=len(tails)
    for t,ii in ivs.items():
        if rich is not None and any(i is not None and i[0]<=rich[1] and i[1]>=rich[0] for i in ii):
            paid+=1; continue
        opts[t]=tuple(b*m+k for b,i in enumerate(ii) if i is not None for k,(j,c) in enumerate(tails) if i[0]<=j<=i[1])
    if stats is not None:
        stats.update({'tail_calls':1,'targets':n,'paid':paid,'scarce_slots':2*m,'scarce_edges':sum(map(len,opts.values()))})
    return paid+match(opts,[c for j,c in tails]*2)

def brute(d,ivs):
    # Independent explicit word matching (small d only).
    words=1<<d; mate={}
    opts={t:[b*words+w for b,i in enumerate(ii) if i is not None for w in range(words) if i[0]<=w.bit_count()<=i[1]] for t,ii in ivs.items()}
    def aug(t,seen):
        for w in opts[t]:
            if w in seen:continue
            seen.add(w)
            if w not in mate or aug(mate[w],seen):mate[w]=t;return True
        return False
    return sum(aug(t,set()) for t in opts)

class TailOracle(HallOracle):
    def __init__(self,b,st):
        super().__init__(b,st,True)
        @lru_cache(None)
        def iv(s,d):
            fibers=defaultdict(list)
            for bit in bitlist(s):
                u,h=st[bit.bit_length()-1]; fibers[u].append((bit,h))
            out={}
            for f in fibers.values():
                B=f[0][1]; A=0
                for _,h in f:B&=h; A|=h
                p=(A^B).bit_count(); cap=14-B.bit_count()
                assert cap>=0 and len(f)==sum(comb(p,z) for z in range(min(p,cap)+1))
                assert len({h for _,h in f})==len(f) and all(h.bit_count()<=14 for _,h in f)
                for bit,h in f:
                    z=(h^B).bit_count(); hi=d if z==cap else min(d,d-p+z)
                    if z<=hi:out[bit]=(z,hi)
            return out
        self.iv=iv; self.tail_stats=Counter()
    def paired(self,a,b,d,l,r,x):
        wa=self.iv(a,d);wb=self.iv(b,d)
        ivs={t:(wa.get(t) if t&(l|x) else None,wb.get(t) if t&(r|x) else None) for t in bitlist(l|r|x)}
        self.stats['paired_calls']+=1
        return sparse(d,ivs,self.tail_stats)

def main():
    rng=Random(49261126); syn=Counter()
    for _ in range(2000):
        d=rng.randrange(9); n=rng.randrange(1,31)
        def iv():
            if rng.randrange(4)==0:return None
            a,b=sorted((rng.randrange(d+1),rng.randrange(d+1)));return a,b
        ii={t:(iv(),iv()) for t in range(n)}
        assert sparse(d,ii,syn)==brute(d,ii)
    huge=[]
    for d in (16,256,10**6,10**12):
        ii={t:((1,d-1),None) for t in range(40)}
        ii.update({t:((0,0),(d,d)) for t in range(40,60)})
        assert sparse(d,ii)==42
        rich,tails=tail_layout(d,len(ii)); huge.append([d,rich,len(tails)*2,42])
    old=json.load(open('gap_target.json'))['rows']; totals={m:Counter() for m in ('word','tail')}; times=Counter(); tail=Counter(); rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
        for h in range(2):
            row=old[2*i+h]; d=k+h; qs=row['qs'];goals=row['goals']; assert (row['i'],row['d'])==(i,d)
            rr={'i':i,'d':d,'checks':{}}
            for m,o in [('word',HallOracle(b,st,True)),('tail',TailOracle(b,st))]:
                t0=perf_counter_ns();assert o.v(b.full,d,b.full)==row['cap'];adj=o.graphs(d,qs,goals);times[m]+=perf_counter_ns()-t0
                assert adj==row['adj'];totals[m].update(o.stats);rr['checks'][m]=dict(o.stats)
                if m=='tail':tail.update(o.tail_stats);rr['tail']=dict(o.tail_stats)
            assert rr['checks']['word']==rr['checks']['tail'];rows.append(rr)
        b.clear()
    print(json.dumps({'synthetic':dict(syn),'huge':huge,'stats':{m:dict(v) for m,v in totals.items()},'tail':dict(tail),'times_ns':dict(times),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
