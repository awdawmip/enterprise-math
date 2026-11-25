from functools import lru_cache
from collections import Counter
from random import Random
import json,time
from multi_target import model, physical

def solve(n, qs, blocks, k, w, prune=True):
    full=(1<<n)-1
    local=[]; mixed=[]; stats=Counter()
    for q in qs:
        sides=[a for a in (q,full^q) if any(a&b==a for b in blocks)]
        if sides: local.append(min(sides))
        else: mixed.append(q)
    local=tuple(sorted(set(local)))
    @lru_cache(None)
    def weight(s):
        if not s:return 0
        a=s&-s
        return w[a.bit_length()-1]+weight(s^a)
    @lru_cache(None)
    def v(s,d):
        if not s:return 0
        if s.bit_count()==1:return weight(s)
        if not d:return 0
        return max(v(s&q,d-1)+v(s&~q,d-1) for q in qs if s&q and s&~q)
    def put(out,key,L):
        if L<out.get(key,float('inf')):out[key]=L
    def reduce(out,where):
        stats[where+'_raw']+=len(out)
        if prune:
            keep={}
            for (m,c),loss in sorted(out.items(),key=lambda a:(a[1],a[0][0].bit_count()+a[0][1].bit_count(),a[0])):
                if any(u&m==u and r&c==r for u,r in keep):continue
                keep[m,c]=loss
            out=keep
        stats[where+'_kept']+=len(out)
        return out
    @lru_cache(None)
    def prof(s,start):
        out={(0,s):0}
        for q in local:
            a=s&q
            if not a:continue
            for t in range(start,k+1):
                loss=weight(a)-v(a,k-t)
                for (m,c),z in prof(s^a,t+1).items():
                    put(out,(m|1<<(t-1),c),z+loss)
        return reduce(out,'local')
    dp={(0,0):0};peak=1
    for b in blocks:
        nxt={}
        for (m,c),z in dp.items():
            for (u,r),y in prof(b,1).items():
                if m&u:continue
                put(nxt,(m|u,c|r),z+y)
        dp=reduce(nxt,'merge');peak=max(peak,len(dp))
    best=weight(full); best_nomix=best
    for (m,c),loss in dp.items():
        t=m.bit_length();d=k-t
        stop=loss+(weight(c) if c.bit_count()>1 else 0)
        best=min(best,stop);best_nomix=min(best_nomix,stop)
        if not d:continue
        for q in mixed:
            a=c&q;b=c&~q
            best=min(best,loss+weight(c)-v(a,d-1)-v(b,d-1));stats['mixed_evals']+=1
    return dict(value=weight(full)-best,reference=v(full,k),no_mixed=weight(full)-best_nomix,peak=peak,final=len(dp),**stats)

def main():
    old=json.load(open('mixed_prefix.out')); rows=[];tot=Counter();rng=Random(16943)
    for i,line in enumerate(open('ga_nodes.txt')):
        k,n,*p=map(int,line.split());st=list(zip(p[::2],p[1::2]));full,qs,*_=model(n,physical(st,10,25))
        blocks=[sum(1<<j for j,(u,h) in enumerate(st) if u==b) for b in sorted({u for u,h in st})]
        rank=json.load(open('capacity_rank.out'))['nodes'][i]['greedy_witness']
        masks=[full,rank]+[rank^(1<<j) for j in range(n) if rank>>j&1]
        vals=next((r['values'] for r in old['rows'] if r['index']==i),None)
        weights=[tuple((t>>j)&1 for j in range(n)) for t in masks]+[tuple(rng.randrange(6) for _ in range(n))] if vals is None else [tuple(r['weights']) for r in vals]
        for j,w in enumerate(weights):
            a=solve(n,qs,blocks,k,w,True); b=solve(n,qs,blocks,k,w,False)
            assert a['value']==b['value']==a['reference'] and a['no_mixed']==b['no_mixed'],(i,j,a,b)
            if vals is not None:assert a['value']==vals[j]['value'] and a['no_mixed']==vals[j]['no_mixed'],(i,j,a,vals[j])
            rows.append(dict(index=i,test=j,weights=w,pruned=a,unpruned=b))
            tot['frozen_checks']+=1
            for x,r in [('p_',a),('u_',b)]:
                for key in ['local_raw','local_kept','merge_raw','merge_kept','mixed_evals','final']:tot[x+key]+=r.get(key,0)
    for i in range(200):
        n=rng.randrange(3,11);full=(1<<n)-1;cut=rng.randrange(1,n);blocks=[(1<<cut)-1,full^((1<<cut)-1)]
        qs=tuple(sorted({1<<j for j in range(n)}|{rng.randrange(1,full) for _ in range(5)}));w=tuple(rng.randrange(6) for _ in range(n));k=rng.randrange(0,5)
        a=solve(n,qs,blocks,k,w,True);b=solve(n,qs,blocks,k,w,False)
        assert a['value']==b['value']==a['reference'] and a['no_mixed']==b['no_mixed'],(i,a,b)
        tot['synthetic_checks']+=1
    print(json.dumps(dict(stats=tot,rows=rows),sort_keys=True))
if __name__=='__main__':main()
