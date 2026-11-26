"""Exact suffix-group packing with common physical prefix. EC49GAN."""
from functools import lru_cache
from math import comb
from collections import Counter
import json
from gal_path_hall import Bound, bitlist, maximal


def packing(b,k,h):
    n=b.n;s=b.full;d=k-h
    # Exact possible residuals after a physical prefix with symbolic padding.
    reach=[{s}]
    for depth in range(d):
        nxt=[set() for _ in range(depth+2)]
        for j,rs in enumerate(reach):
            for r in rs:
                nxt[j].add(r);nxt[j+1].add(r)
                for q in b.qs:
                    a=r&q;c=r^a
                    if a and c:nxt[j].add(a);nxt[j+1].add(c)
        reach=nxt
    @lru_cache(None)
    def recovered(r,t):
        if r.bit_count()<=1:return (r,)
        if not t:return (0,)
        return tuple(maximal([x|y for a in b.splits(r) for x in recovered(a,t-1) for y in recovered(r^a,t-1)] or [0]))
    width=1<<n;universe=(1<<width)-1
    absent=[universe//((1<<(1<<i))+1) for i in range(n)]
    @lru_cache(None)
    def allowed(g):
        a=universe
        for bit in bitlist(g):a&=absent[bit.bit_length()-1]
        return a
    dp=1;groups_count=0
    for j,rs in enumerate(reach):
        maxima=maximal([g for r in rs for g in recovered(r,h)])
        gs=set()
        for g in maxima:
            a=g
            while a:gs.add(a);a=(a-1)&g
        groups_count+=len(gs)
        for _ in range(comb(d,j)):
            nxt=dp
            for g in gs:nxt|=(dp&allowed(g))<<g
            if nxt==dp:break
            dp=nxt
            if dp==universe:break
        if dp==universe:break
    packed=dp.to_bytes((width+7)//8,'little')
    @lru_cache(None)
    def cap(t):
        if packed[t>>3]>>(t&7)&1:return t.bit_count()
        return max((cap(t^bit) for bit in bitlist(t)),default=0)
    return cap,dp,groups_count


def main():
    import sys
    old=json.load(open('sibling_packing.json'))['rows'];gal=json.load(open('gal_path_hall.json'))['rows'];stats=Counter();rows=[]
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 0;hi=int(sys.argv[2]) if len(sys.argv)>2 else 180
    for i,line in enumerate(open('ga_nodes.txt')):
        if not lo<=i<hi:continue
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])));f=b.full;row={'i':i,'budgets':[],'obstacles':[]}
        for d,exact,base,u1,u2,prev,_,cnt in old[i]['budgets']:
            c1,dp1,_=packing(b,d,1);assert c1(f)==prev and dp1.bit_count()==cnt
            c2,dp2,g2=packing(b,d,min(2,d));assert dp2&~dp1==0
            c3,dp3,g3=packing(b,d,min(3,d));assert dp3&~dp2==0
            v2,v3=c2(f),c3(f);assert exact<=v3<=v2<=prev
            row['budgets'].append([d,exact,prev,v2,v3,dp2.bit_count(),dp3.bit_count(),g2,g3]);stats['budgets']+=1
            stats['strict2']+=v2<prev;stats['strict3']+=v3<v2;stats['exact2']+=v2==exact;stats['exact3']+=v3==exact
            if d==k:
                for (t,_,_,_,u2),(tt,p) in zip(gal[i]['obstacles'],old[i]['obstacles']):
                    assert t==tt and c1(t)==p
                    v,w=c2(t),c3(t);m=t.bit_count();assert m-1<=w<=v<=p
                    row['obstacles'].append([t,p,v,w]);stats['obstacles']+=1;stats['reject2']+=v<m;stats['reject3']+=w<m;stats['combined2']+=min(v,u2)<m;stats['combined3']+=min(w,u2)<m
        rows.append(row);b.clear()
    print(json.dumps({'stats':dict(stats),'rows':rows},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
