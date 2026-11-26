"""EC49GAY: label-preserving bitset Hall cuts, frozen BRC16943."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb
from time import perf_counter_ns
import json
import threshold_hall as prev
from gal_path_hall import Bound, bitlist

class MaskOracle(prev.ThresholdOracle):
    def __init__(self,b,st,sparse=True):
        super().__init__(b,st)
        self.sparse=sparse
        @lru_cache(None)
        def eligible(s,d,w):
            if not w:return self.profile(s,d)[0]
            return sum(t for t,m in self.classes(s,d).items() if m&~w==0)|self.profile(s,d)[0]
        self.eligible=eligible
    def paired_cut(self,a,b,d,t,L):
        k=t.bit_count()-L
        if k<=0:return True
        if L<0:return False
        st=self.threshold_stats
        st['cut_calls']+=1
        f=self.eligible
        A=t&(~a|f(a,d,0));B=t&(~b|f(b,d,0))
        z=A&B
        if z.bit_count()>=k:
            st['zero_hits']+=1;return True
        if self.sparse and k<=2:
            # Each bank has positive binomial capacities. Enumerate only W of cost <=3-k.
            cs=[comb(d,j) for j in range(d+1)]
            one=[(i,1<<j) for i in (0,1) for j,c in enumerate(cs) if c==1]
            def cut(u,v,c):
                st['sparse_tests']+=1
                p=A if not u else t&(~a|f(a,d,u))
                q=B if not v else t&(~b|f(b,d,v))
                return (p&q).bit_count()>=c+k
            for i,w in one:
                if cut(w if i==0 else 0,w if i==1 else 0,1):
                    st['one_hits']+=1;return True
            if k==1:
                for i in (0,1):
                    for j,c in enumerate(cs):
                        if c==2 and cut(1<<j if i==0 else 0,1<<j if i==1 else 0,2):
                            st['two_hits']+=1;return True
                for (i,w),(j,v) in combinations(one,2):
                    if cut((w if i==0 else 0)|(v if j==0 else 0),(w if i==1 else 0)|(v if j==1 else 0),2):
                        st['two_hits']+=1;return True
        # Targets with empty neighborhoods can never contribute. Retain full physical states.
        wa=self.classes(a,d);wb=self.classes(b,d)
        opts={u:wa.get(u,0)|(wb.get(u,0)<<(d+1)) for u in bitlist(t&~z)}
        st['fallbacks']+=1;st['zero_removed']+=z.bit_count()
        return prev.at_most(opts,[comb(d,j) for j in range(d+1)]*2,L,st)
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
                if self.paired_cut(a,b,d,l|r|x,limit):
                    self.stats['paired_prunes']+=1;return False
            vl=v(a,d,l|x);vr=v(b,d,r|x)
            if vl+vr<=limit:self.stats['sum_prunes']+=1;return False
            if not x:self.stats['leaf_yes']+=1;return True
            if vl+v(b,d,r)>limit or v(a,d,l)+vr>limit:
                self.stats['extreme_yes']+=1;return True
            bit=x&-x;x^=bit
            return visit(l|bit,r,x) or visit(l,r|bit,x)
        return visit(l,r,x,True)

def run():
    old=json.load(open('gap_target.json'))['rows'];out={}
    for mode in ('baseline','zero','sparse','sparse','zero','baseline'):
        agg=Counter();search=Counter();rows=[];elapsed=0
        for i,line in enumerate(open('ga_nodes.txt')):
            k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
            for j in range(2):
                d=k+j;r=old[2*i+j];o=prev.ThresholdOracle(b,st) if mode=='baseline' else MaskOracle(b,st,mode=='sparse')
                t0=perf_counter_ns();assert o.v(b.full,d,b.full)==r['cap'];assert o.graphs(d,r['qs'],r['goals'])==r['adj'];elapsed+=perf_counter_ns()-t0
                agg.update(o.threshold_stats);search.update(o.stats);rows.append([i,d,dict(o.threshold_stats)])
            b.clear()
        out.setdefault(mode,[]).append({'stats':dict(agg),'search':dict(search),'ns':elapsed,'rows':rows})
    assert all(r['search']==out['baseline'][0]['search'] for runs in out.values() for r in runs)
    print(json.dumps(out,separators=(',',':')))
if __name__=='__main__':run()
