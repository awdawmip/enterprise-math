"""Last-sibling packing relaxation, EC49GAL continuation, exact bitset DP."""
from functools import lru_cache
from itertools import combinations
from math import comb
from collections import Counter
import json
from gal_path_hall import Bound, layers, bitlist


def pair_support(b,s,p,d):
    if not any(q&p and p&~q for q in b.qs):
        return 0
    pos=layers([s&~q for q in b.qs if q&p==p],d)
    neg=layers([s&q for q in b.qs if not q&p],d)
    return sum(1<<j for j in range(d+1) if any(a|c==s^p for a in pos[d-j] for c in neg[j]))


def packing(b,s,k):
    # root only, dense state labels. A bit at position M represents reachable target mask M.
    assert s==b.full and k>=1
    n=b.n;d=k-1;slots=[[] for _ in range(k)]
    for bit,o in b.opts(s,k):
        for j in range(k):
            if o&(3<<j):slots[j].append(bit)
    pairs=[]
    for x,y in combinations(bitlist(s),2):
        p=x|y; o=pair_support(b,s,p,d)
        if o:pairs.append((p,o))
        for j in range(k):
            if o>>j&1:slots[j].append(p)
    # each bit in allowed[g] marks a mask disjoint from group g.
    width=1<<n; universe=(1<<width)-1
    absent=[universe//((1<<(1<<i))+1) for i in range(n)]
    allowed={}
    for groups in slots:
        for g in groups:
            a=universe
            for bit in bitlist(g):a&=absent[bit.bit_length()-1]
            allowed[g]=a
    dp=1
    for j,groups in enumerate(slots):
        for _ in range(comb(d,j)):
            nxt=dp
            for g in groups:nxt|=(dp&allowed[g])<<g
            dp=nxt
    packed=dp.to_bytes((width+7)//8,'little')
    @lru_cache(None)
    def cap(t):
        if packed[t>>3]>>(t&7)&1:return t.bit_count()
        return max((cap(t^bit) for bit in bitlist(t)),default=0)
    return cap,pairs,dp.bit_count()


def main():
    old=json.load(open('gal_path_hall.json'))['rows'];front=json.load(open('recoverable_frontier.out'))['rows'];stats=Counter();rank=Counter();rows=[]
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*a=map(int,line.split());b=Bound(list(zip(a[::2],a[1::2])));f=b.full;row={'i':i,'budgets':[],'obstacles':[]}
        for d,exact,_,base,u1,u2 in old[i]['budgets']:
            cap,pairs,count=packing(b,f,d);v=cap(f);assert exact<=v<=n
            row['budgets'].append([d,exact,base,u1,u2,v,len(pairs),count]);stats['budgets']+=1
            stats['strict_vs_base']+=v<base;stats['strict_vs_prefix1']+=v<u1;stats['strict_vs_prefix2']+=v<u2;stats['exact']+=v==exact
            if d==k:
                row['pairs']=pairs
                for t,_,base,u1,u2 in old[i]['obstacles']:
                    m=t.bit_count();v=cap(t);assert m-1<=v<=m
                    row['obstacles'].append([t,v]);rank[m,'total']+=1;rank[m,'packing']+=v<m;rank[m,'new_vs_prefix2']+=v<u2;stats['obstacles']+=1
            cap.cache_clear()
        b.clear();rows.append(row)
    print(json.dumps({'stats':dict(stats),'rank':[[r,l,v] for (r,l),v in sorted(rank.items())],'rows':rows},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
