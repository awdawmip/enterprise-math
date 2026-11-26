"""Exact shared-root label compression for finite binary observations."""
from functools import lru_cache
from collections import Counter
from gal_path_hall import Bound, maximal, bitlist
import json


def color(adj):
    n=len(adj); full=(1<<n)-1
    def choose(rem,parts):
        return max(bitlist(rem),key=lambda b:(sum(bool(adj[b.bit_length()-1]&c) for c in parts), (adj[b.bit_length()-1]&rem).bit_count(),adj[b.bit_length()-1].bit_count(),-b))
    parts=[];rem=full
    while rem:
        b=choose(rem,parts);rem^=b;a=adj[b.bit_length()-1]
        for j,c in enumerate(parts):
            if not a&c:parts[j]|=b;break
        else:parts.append(b)
    best=parts[:]; calls=0
    def visit(rem,parts):
        nonlocal best,calls
        calls+=1
        if len(parts)>=len(best):return
        if not rem:best=parts[:];return
        b=choose(rem,parts);a=adj[b.bit_length()-1];rem^=b
        for j,c in enumerate(parts):
            if not a&c:
                parts[j]|=b;visit(rem,parts);parts[j]=c
        if len(parts)+1<len(best):visit(rem,parts+[b])
    visit(full,[])
    return best,calls


def analyze(b,k,pad=True):
    s=b.full;n=b.n
    @lru_cache(None)
    def rec(r,d):
        if r.bit_count()<=1:return (r,)
        if not d:return (0,)
        return tuple(maximal([x|y for a in b.splits(r) for x in rec(a,d-1) for y in rec(r^a,d-1)] or [0]))
    qs=[q for q in b.qs if q and q!=s]
    if pad:qs=[0]+qs+[s]
    left=[rec(q,k-1) for q in qs];right=[rec(s^q,k-1) for q in qs]
    frontier=rec(s,k)
    def accepted(t):return any(t&~x==0 for x in frontier)
    adj=[0]*len(qs);bad=[];cross=0;loose=set()
    for i,L in enumerate(left):
        for j,R in enumerate(right):
            witness=None
            for x in L:
                for y in R:
                    u=x|y;cross+=1;loose.add(u)
                    if witness is None and not accepted(u):witness=u
            if witness is not None:
                assert i!=j
                adj[i]|=1<<j;adj[j]|=1<<i;bad.append([i,j,witness])
    parts,calls=color(adj)
    assert sum(c.bit_count() for c in parts)==len(qs) and sum(parts)==(1<<len(qs))-1
    covered=set()
    for c in parts:
        ids=[v.bit_length()-1 for v in bitlist(c)]
        assert all(not adj[i]&c for i in ids)
        covered.update(x|y for i in ids for j in ids for x in left[i] for y in right[j])
    assert set(maximal(covered))==set(frontier)
    return dict(qs=qs,classes=parts,edges=sum(a.bit_count() for a in adj)//2,bad=bad,exact=list(frontier),loose=list(maximal(loose)),calls=calls,cross=cross)


def main():
    old=json.load(open('recoverable_frontier.out'))['rows'];prior=json.load(open('gan_pack.json'))['rows'];stats=Counter();hist=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])))
        row={'i':i,'budgets':[]}
        for d in (k,k+1):
            r=analyze(b,d);f=r['exact'];loose=r['loose'];p=len(r['classes']);q=len(r['qs']);stats['cases']+=1;stats['labels']+=q;stats['classes']+=p;stats['edges']+=r['edges'];stats['cross']+=r['cross'];stats['color_calls']+=r['calls'];hist[p]+=1
            assert max(x.bit_count() for x in f)==b.exact(b.full,d)
            if d==k:
                assert set(f)=={b.full^x for x in old[i]['frontier']}
                rejected=sum(not any(t&~x==0 for x in loose) for t in old[i]['obstructions']);stats['obstacles']+=len(old[i]['obstructions']);stats['loose_reject']+=rejected
                stats['same_full_cap']+=max(x.bit_count() for x in f)==max(x.bit_count() for x in loose)
            row['budgets'].append(dict(d=d,**r))
        rows.append(row);b.clear()
    print(json.dumps({'stats':dict(stats),'hist':dict(hist),'rows':rows},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
