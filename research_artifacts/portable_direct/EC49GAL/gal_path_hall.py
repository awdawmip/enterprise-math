"""Exact individual answer-weight supports and prefix-conditioned matching bounds."""
from functools import lru_cache
from math import comb
from collections import Counter
from pathlib import Path
import json
from verify_gak import intervals


def maximal(ms):
    out=[]
    for m in sorted(set(ms),key=lambda x:(-x.bit_count(),x)):
        if not any(m&~x==0 for x in out):out.append(m)
    return out


def layers(ms,k):
    ms=maximal(ms);out=[[0]]
    for _ in range(k):out.append(maximal([a|b for a in out[-1] for b in ms]+out[-1]))
    return out


def bitlist(s):
    while s:
        b=s&-s;s^=b;yield b


class Bound:
    def __init__(self,st):
        self.n=len(st);self.full=(1<<self.n)-1
        self.qs=tuple(sorted({sum(1<<i for i,(u,h) in enumerate(st) if u>>r&1 and not h>>j&1) for r in range(10) for j in range(25)}))

    @lru_cache(None)
    def opts(self,s,k):
        out=[]
        for b in bitlist(s):
            pos=layers([s&~q for q in self.qs if q&b],k)
            neg=layers([s&q for q in self.qs if not q&b],k)
            out.append((b,sum(1<<j for j in range(k+1) if any(a|c==s^b for a in pos[k-j] for c in neg[j]))))
        return tuple(out)

    @lru_cache(None)
    def path(self,s,b,p,m):
        if s==b:return True
        for q in self.qs:
            t=s&q if q&b else s&~q
            if t==s:continue
            if q&b and p and self.path(t,b,p-1,m):return True
            if not q&b and m and self.path(t,b,p,m-1):return True
        return False

    @lru_cache(None)
    def windows(self,s,k):
        opts=self.opts(s,k);out=[]
        for j in range(1<<(k+1)):
            e=sum(b for b,o in opts if o&~j==0)
            cap=sum(comb(k,h) for h in range(k+1) if j>>h&1)
            if e.bit_count()>cap:out.append((e,cap))
        return tuple(out)

    @lru_cache(None)
    def splits(self,s):
        return tuple(sorted({min(s&q,s&~q) for q in self.qs if s&q and s&~q}))

    @lru_cache(None)
    def upper(self,s,k,t,l):
        t &= s
        if not t:return 0
        if s.bit_count()==1:return 1
        if not k:return 0
        base=t.bit_count()-max([0]+[(e&t).bit_count()-c for e,c in self.windows(s,k)])
        if not l or not base:return base
        return min(base,max((self.upper(a,k-1,t&a,l-1)+self.upper(s^a,k-1,t&(s^a),l-1) for a in self.splits(s)),default=0))

    @lru_cache(None)
    def exact(self,s,k):
        if s.bit_count()<=1:return s.bit_count()
        if not k:return 0
        return max((self.exact(a,k-1)+self.exact(s^a,k-1) for a in self.splits(s)),default=0)

    def clear(self):
        for f in (self.opts,self.path,self.windows,self.splits,self.upper,self.exact):f.cache_clear()


def interval_cap(st,k,t):
    iv=intervals(st,k);o=[sum(1<<j for j in range(k+1) if a<=j<=b) for a,b in iv]
    return t.bit_count()-max(sum(1 for i,x in enumerate(o) if t>>i&1 and x&~j==0)-sum(comb(k,h) for h in range(k+1) if j>>h&1) for j in range(1<<(k+1)))


def main():
    prev=json.loads(Path('recoverable_frontier.out').read_text())['rows']; rows=[];rank=Counter();stats=Counter()
    for i,line in enumerate(Path('ga_nodes.txt').read_text().splitlines()):
        k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));assert n==len(st)
        b=Bound(st);f=b.full;entry={'i':i,'n':n,'k':k,'budgets':[],'obstacles':[]}
        for d in (k,k+1):
            for bit,mask in b.opts(f,d):
                for j in range(d+1):
                    assert bool(mask>>j&1)==b.path(f,bit,d-j,j)
                    stats['path_checks']+=1
            exact=b.exact(f,d);u=[b.upper(f,d,f,l) for l in range(3)];old=interval_cap(st,d,f)
            assert exact<=u[2]<=u[1]<=u[0]<=old<=n
            if d==k:assert exact==n-min(m.bit_count() for m in prev[i]['frontier'])
            entry['budgets'].append([d,exact,old,*u]);stats['budget_checks']+=1
        for t in prev[i]['obstructions']:
            m=t.bit_count();old=interval_cap(st,k,t);u=[b.upper(f,k,t,l) for l in range(3)]
            exact=m-min((t&f0).bit_count() for f0 in prev[i]['frontier'])
            assert exact==m-1 and exact<=u[2]<=u[1]<=u[0]<=old<=m
            stats['obstruction_checks']+=1
            rank[m,'total']+=1
            for name,val in zip(('interval','path','prefix1','prefix2'),[old,*u]):
                if val<m:rank[m,name]+=1
            entry['obstacles'].append([t,old,*u])
        rows.append(entry);b.clear()
    print(json.dumps({'stats':dict(stats),'rank':[[r,l,v] for (r,l),v in sorted(rank.items())],'rows':rows},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
