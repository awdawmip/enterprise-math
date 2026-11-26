"""EC49 continuation: capacitated sign-count matching without word expansion."""
from collections import Counter,defaultdict
from functools import lru_cache
from math import comb
from time import perf_counter_ns
import json
from joint_hall import HallOracle
from gal_path_hall import Bound,bitlist

def class_match(opts,caps):
    """opts maps target -> iterable of class indices; integral capacity per class."""
    occupants=[[] for _ in caps]
    def aug(t,seen):
        for c in opts[t]:
            if c in seen:continue
            seen.add(c);v=occupants[c]
            if len(v)<caps[c]:v.append(t);return True
            for i,u in enumerate(v):
                if aug(u,seen):v[i]=t;return True
        return False
    return sum(aug(t,set()) for t in sorted(opts,key=lambda t:len(opts[t])))

class ClassOracle(HallOracle):
    def __init__(self,b,st,each=False):
        super().__init__(b,st,True)
        self.each=each
        @lru_cache(None)
        def profile(s,d):
            fibers=defaultdict(list)
            for bit in bitlist(s):
                u,h=st[bit.bit_length()-1];fibers[u].append((bit,h))
            options=[];dead=0
            for f in fibers.values():
                B=f[0][1];A=0
                for _,h in f:B&=h;A|=h
                p=(A^B).bit_count();b=14-B.bit_count()
                assert b>=0 and len(f)==sum(comb(p,z) for z in range(min(p,b)+1))
                assert len({h for _,h in f})==len(f) and all(h.bit_count()<=14 for _,h in f)
                for bit,h in f:
                    z=(h^B).bit_count();lo=z;hi=min(d,d if z==b else d-p+z)
                    if lo>hi:dead|=bit
                    else:options.append((bit,lo,hi))
            end=[[] for _ in range(d+1)]
            for a in range(d+1):
                for c in range(a,d+1):
                    m=sum(bit for bit,lo,hi in options if a<=lo and hi<=c)
                    cap=sum(comb(d,j) for j in range(a,c+1))
                    if m.bit_count()>cap:end[c].append((a,m,cap))
            self.stats['profiles']+=1
            return dead,tuple(tuple(x) for x in end),{bit:tuple(range(lo,hi+1)) for bit,lo,hi in options}
        self.profile=profile
        @lru_cache(None)
        def hall(s,d,t):
            self.stats['hall_misses']+=1
            if not t:return 0
            dead,end,_=profile(s,d);t&=~dead
            if not any(end):return t.bit_count()
            f=[0]*(d+2)
            for c,ws in enumerate(end):
                f[c+1]=max([f[c]]+[f[max(0,a-1)]+(m&t).bit_count()-cap for a,m,cap in ws])
            return t.bit_count()-f[-1]
        self.hall=hall
    def paired(self,a,b,d,l,r,x):
        wa=self.profile(a,d)[2];wb=self.profile(b,d)[2];shift=d+1
        opts={t:(wa.get(t,()) if t&(l|x) else ()) + (tuple(c+shift for c in wb.get(t,())) if t&(r|x) else ()) for t in bitlist(l|r|x)}
        self.stats['paired_calls']+=1
        return class_match(opts,[comb(d,j) for j in range(d+1)]*2)
    def edge(self,a,b,d,t,limit):
        self.stats['cross_calls']+=1;t&=a|b
        if t.bit_count()<=limit:self.stats['size_prunes']+=1;return False
        v=self.v;hall=self.hall
        x=t&a&b;l=t&a&~b;r=t&b&~a
        def visit(l,r,x,root=False):
            self.stats['allocation_nodes']+=1
            if hall(a,d,l|x)+hall(b,d,r|x)<=limit:
                self.stats['hall_prunes']+=1;return False
            if (root or (self.each and x)) and self.paired(a,b,d,l,r,x)<=limit:
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
    old=json.load(open('gap_target.json'))['rows'];stats={m:Counter() for m in ('word','class','each')};times=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
        for h in range(2):
            row=old[2*i+h];d=k+h;qs=row['qs'];goals=row['goals'];assert row['i']==i and row['d']==d
            rr={'i':i,'d':d,'checks':{}}
            for m,o in [('word',HallOracle(b,st,True)),('class',ClassOracle(b,st)),('each',ClassOracle(b,st,True))]:
                t0=perf_counter_ns();assert o.v(b.full,d,b.full)==row['cap'];adj=o.graphs(d,qs,goals);elapsed=perf_counter_ns()-t0
                assert adj==row['adj'];stats[m].update(o.stats);times[m]+=elapsed
                rr['checks'][m]=dict(o.stats)
            assert rr['checks']['word']==rr['checks']['class']
            rows.append(rr)
        b.clear()
    print(json.dumps({'stats':{m:dict(v) for m,v in stats.items()},'times_ns':dict(times),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
