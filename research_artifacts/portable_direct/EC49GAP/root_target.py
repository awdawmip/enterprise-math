"""Targeted exact cross-union threshold oracle, no recovered-family enumeration."""
from functools import lru_cache
from collections import Counter
from time import perf_counter_ns
import json
from gal_path_hall import Bound, maximal, bitlist
from root_color import color
from root_color_verify import clique

class Oracle:
    def __init__(self,b):
        self.b=b; self.stats=Counter()
        @lru_cache(None)
        def v(s,d,t):
            assert not t&~s
            self.stats['scalar_misses']+=1
            if not t:return 0
            if s.bit_count()<=1:return t.bit_count()
            if not d:return 0
            ceiling=min(t.bit_count(),1<<d)
            best=0
            for a in b.splits(s):
                c=s^a
                if min((t&a).bit_count(),1<<(d-1))+min((t&c).bit_count(),1<<(d-1))<=best:continue
                best=max(best,v(a,d-1,t&a)+v(c,d-1,t&c))
                if best==ceiling:break
            return best
        self.v=v

    def edge(self,a,b,d,t,limit):
        """Whether some cross union recovers >limit targets from t."""
        self.stats['cross_calls']+=1
        t &= a|b
        if t.bit_count()<=limit:
            self.stats['size_prunes']+=1;return False
        v=self.v
        x=t&a&b; l=t&a&~b; r=t&b&~a
        def visit(l,r,x):
            self.stats['allocation_nodes']+=1
            vl=v(a,d,l|x);vr=v(b,d,r|x)
            if vl+vr<=limit:
                self.stats['sum_prunes']+=1;return False
            if not x:
                self.stats['leaf_yes']+=1;return True
            if vl+v(b,d,r)>limit or v(a,d,l)+vr>limit:
                self.stats['extreme_yes']+=1;return True
            bit=x&-x;x^=bit
            return visit(l|bit,r,x) or visit(l,r|bit,x)
        return visit(l,r,x)

    def graphs(self,k,qs,goals):
        s=self.b.full; adj=[[0]*len(qs) for _ in goals]
        for i,a in enumerate(qs):
            for j,q in enumerate(qs):
                for g,(t,limit) in enumerate(goals):
                    if self.edge(a,s^q,k-1,t,limit):
                        assert i!=j
                        adj[g][i]|=1<<j;adj[g][j]|=1<<i
        return adj

def reference(b,k,qs,goals):
    # independent maximal-family enumeration, used only after targeted graph construction
    @lru_cache(None)
    def f(s,d):
        if s.bit_count()<=1:return (s,)
        if not d:return (0,)
        return tuple(maximal(x|y for a in b.splits(s) for x in f(a,d-1) for y in f(s^a,d-1)))
    left=[f(q,k-1) for q in qs];right=[f(b.full^q,k-1) for q in qs]
    adj=[[0]*len(qs) for _ in goals]
    for i,L in enumerate(left):
        for j,R in enumerate(right):
            pending=set(range(len(goals)))
            for x in L:
                for y in R:
                    u=x|y
                    found=[g for g in pending if (u&goals[g][0]).bit_count()>goals[g][1]]
                    for g in found:
                        adj[g][i]|=1<<j;adj[g][j]|=1<<i;pending.remove(g)
                    if not pending:break
                if not pending:break
    return adj

def main():
    old=json.load(open('gao_color.json'))['rows'];obs=json.load(open('recoverable_frontier.out'))['rows'];stats=Counter();times=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])))
        for h in range(2):
            d=k+h;qs=old[i]['budgets'][h]['qs'];o=Oracle(b)
            t0=perf_counter_ns();cap=o.v(b.full,d,b.full);t1=perf_counter_ns()
            assert cap==max(x.bit_count() for x in old[i]['budgets'][h]['exact'])
            goals=[(b.full,cap)]
            if i==125 and h==0:goals += [(t,t.bit_count()-1) for t in obs[i]['obstructions'] if t.bit_count()==11]
            adj=o.graphs(d,qs,goals);t2=perf_counter_ns();ref=reference(b,d,qs,goals);t3=perf_counter_ns();assert adj==ref
            combined=[0]*len(qs)
            for g in adj:
                for j,a in enumerate(g):combined[j]|=a
            parts,_=color(combined);c=clique(combined,(1<<len(qs))-1,len(parts));assert c is not None
            row={'i':i,'d':d,'cap':cap,'qs':qs,'goals':goals,'adj':adj,'classes':parts,'clique':c,'stats':dict(o.stats)}
            rows.append(row);stats.update(o.stats);stats['cases']+=1;stats['goals']+=len(goals);stats['edges']+=sum(a.bit_count() for a in combined)//2;stats['labels']+=len(qs);stats['classes']+=len(parts)
            times.update({'scalar':t1-t0,'target_graph':t2-t1,'family_reference':t3-t2})
        b.clear()
    print(json.dumps({'stats':dict(stats),'times_ns':dict(times),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
