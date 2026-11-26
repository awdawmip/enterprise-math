"""GAU continuation: threshold-only capacitated matching, exact Boolean result."""
from collections import Counter
from functools import lru_cache
from math import comb
from random import Random
from time import perf_counter_ns
import json
from gal_path_hall import Bound, bitlist
from joint_hall import HallOracle
from peel_hall import cut_reference


def at_most(opts, caps, limit, stats):
    """True iff maximum unit-credit capacitated matching <= limit."""
    n=len(opts); stats['calls']+=1; stats['targets']+=n
    if limit<0: return False
    if n<=limit: return True
    active=sum(1<<j for j,c in enumerate(caps) if c)
    masks=sorted((m&active for m in opts.values()), key=int.bit_count)
    owners=[[] for _ in caps]; free=active
    def augment(t):
        nonlocal free
        seen=0
        def dfs(u):
            nonlocal seen,free
            available=masks[u]&free
            if available:
                j=(available&-available).bit_length()-1
                owners[j].append(u)
                if len(owners[j])==caps[j]: free &= ~(1<<j)
                return True
            choices=masks[u]&~seen
            while choices:
                bit=choices&-choices; j=bit.bit_length()-1; seen|=bit
                for i,v in enumerate(owners[j]):
                    if dfs(v): owners[j][i]=u; return True
                choices &= ~seen
            return False
        return dfs(t)
    h=0
    for t in range(n):
        stats['processed']+=1
        if augment(t): h+=1
        if h>limit:
            stats['lower_stop']+=1; return False
        if h+n-t-1<=limit:
            stats['upper_stop']+=1; return True
    return h<=limit

class ThresholdOracle(HallOracle):
    def __init__(self,b,st):
        super().__init__(b,st,True);self.threshold_stats=Counter()
        @lru_cache(None)
        def classes(s,d):
            return {t:sum(1<<j for j in {(w.bit_length()-1).bit_count() for w in bitlist(m)}) for t,m in self.profile(s,d)[2].items()}
        self.classes=classes
    def edge(self,a,b,d,t,limit):
        self.stats['cross_calls']+=1;t&=a|b
        if t.bit_count()<=limit:self.stats['size_prunes']+=1;return False
        v=self.v;hall=self.hall
        x=t&a&b;l=t&a&~b;r=t&b&~a
        def visit(l,r,x,root=False):
            self.stats['allocation_nodes']+=1
            if hall(a,d,l|x)+hall(b,d,r|x)<=limit:
                self.stats['hall_prunes']+=1;return False
            if root:
                self.stats['paired_calls']+=1
                wa=self.classes(a,d);wb=self.classes(b,d)
                opts={t:(wa.get(t,0) if t&(l|x) else 0)|((wb.get(t,0) if t&(r|x) else 0)<<(d+1)) for t in bitlist(l|r|x)}
                if at_most(opts,[comb(d,j) for j in range(d+1)]*2,limit,self.threshold_stats):
                    self.stats['paired_prunes']+=1;return False
            vl=v(a,d,l|x);vr=v(b,d,r|x)
            if vl+vr<=limit:self.stats['sum_prunes']+=1;return False
            if not x:self.stats['leaf_yes']+=1;return True
            if vl+v(b,d,r)>limit or v(a,d,l)+vr>limit:
                self.stats['extreme_yes']+=1;return True
            bit=x&-x;x^=bit
            return visit(l|bit,r,x) or visit(l,r|bit,x)
        return visit(l,r,x,True)

def main():
    rng=Random(49261128);syn=Counter();checks=0
    for _ in range(3000):
        m=rng.randrange(1,9);n=rng.randrange(0,33)
        caps=[rng.randrange(7) for _ in range(m)];opts={t:rng.randrange(1<<m) for t in range(n)}
        h=cut_reference(opts,caps)
        for limit in range(-1,n+1):
            assert at_most(opts,caps,limit,syn)==(h<=limit);checks+=1
    old=json.load(open('gap_target.json'))['rows'];totals={m:Counter() for m in ('word','threshold')};times=Counter();agg=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
        for h in range(2):
            row=old[2*i+h];d=k+h;assert (row['i'],row['d'])==(i,d)
            rr={'i':i,'d':d,'checks':{}}
            for m,o in [('word',HallOracle(b,st,True)),('threshold',ThresholdOracle(b,st))]:
                t0=perf_counter_ns();assert o.v(b.full,d,b.full)==row['cap'];adj=o.graphs(d,row['qs'],row['goals']);times[m]+=perf_counter_ns()-t0
                assert adj==row['adj'];totals[m].update(o.stats);rr['checks'][m]=dict(o.stats)
                if m=='threshold':agg.update(o.threshold_stats);rr['threshold']=dict(o.threshold_stats)
            assert rr['checks']['word']==rr['checks']['threshold'];rows.append(rr)
        b.clear()
    print(json.dumps({'synthetic_checks':checks,'synthetic':dict(syn),'stats':{m:dict(v) for m,v in totals.items()},'threshold':dict(agg),'times_ns':dict(times),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
