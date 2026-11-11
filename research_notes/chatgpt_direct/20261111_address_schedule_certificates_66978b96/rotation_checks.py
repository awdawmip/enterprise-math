"""Finite checks for fixed-target prescribed-address key scheduling.

Keys here are already certified (or used in the relaxed key-scheduling lower
bound); no hidden request values and no simulated primitive commands. The
separate kernel adapter runs the physical BRC integration.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse, json


def weight(key, width):
    return 2*key.bit_count() + 4*(1-((key>>(width-1))&1))


def palettes(r):
    width=r.bit_length()
    full=list(range(1,r+2)); h=1<<(width-1)
    high=[k for k in full if k & h]
    return width,full,high


def ordered(keys,b):
    return sorted(keys,key=lambda k:(weight(k,b),k))


def check_path(ds, path, b):
    holding={}
    assert len(ds)==len(path)
    for d,k in zip(ds,path):
        assert k not in holding.values()
        holding[d]=k
    return sum(weight(k,b) for k in path)


def exact(ds,keys,b):
    """Independent labelled-state DP: explicitly retain each address's key."""
    ds=tuple(ds); keys=tuple(keys)
    dim=max(ds,default=-1)+1
    @lru_cache(None)
    def solve(t,slots):
        if t==len(ds):return 0,()
        best=None
        for k in keys:
            if k in slots:continue
            s=list(slots);s[ds[t]]=k
            z=solve(t+1,tuple(s))
            if z is None:continue
            cand=weight(k,b)+z[0],(k,)+z[1]
            if best is None or cand<best:best=cand
        return best
    return solve(0,(None,)*dim)


def rotation(r,s,T,keys):
    b=r.bit_length(); seq=ordered(keys,b)[:min(s+1,T)]
    if len(seq)<min(s+1,T):return None
    path=tuple(seq[t%len(seq)] for t in range(T)) if T else ()
    ds=tuple(t%s for t in range(T))
    return check_path(ds,path,b),path


def intervals(ds):
    n=len(ds); nxt={}; ends=[n-1]*n
    for t in range(n-1,-1,-1):
        ends[t]=nxt.get(ds[t],n-1);nxt[ds[t]]=t
    diff=[0]*(n+1)
    for t,e in enumerate(ends):diff[t]+=1;diff[e+1]-=1
    depth=[];cur=0
    for v in diff[:-1]:cur+=v;depth.append(cur)
    return ends,depth


def cheapest_and_common(ds,cheap,commons,b):
    """Best schedule using one cheap key and q equally priced common keys.

    A skip at each time is allowed only when q ordinary keys cover its depth.
    Taking I[t] designates it the cheap key and jumps beyond its closed end.
    """
    n=len(ds);ends,depth=intervals(ds);q=len(commons)
    assert cheap not in commons and len(set(commons))==q
    assert q and len({weight(k,b) for k in commons})==1
    assert weight(cheap,b)<weight(commons[0],b)
    omega=max(depth,default=0)
    if omega>q+1:return None
    if not n:return (0,(),0,0)
    q=min(q,omega);commons=commons[:q]
    score=[None]*(n+1);take=[False]*n;score[n]=0
    for t in range(n-1,-1,-1):
        after=score[ends[t]+1]
        best=None if after is None else 1+after
        take[t]=best is not None
        if depth[t]<=q and score[t+1] is not None and (best is None or score[t+1]>best):
            best=score[t+1];take[t]=False
        score[t]=best
    if score[0] is None:return None
    chosen=set();t=0
    while t<n:
        if take[t]:chosen.add(t);t=ends[t]+1
        else:t+=1
    last={k:-1 for k in commons};path=[]
    for t in range(n):
        if t in chosen:path.append(cheap)
        else:
            k=next(k for k in commons if last[k]<t)
            path.append(k);last[k]=ends[t]
    cost=check_path(ds,path,b)
    assert cost==len(chosen)*weight(cheap,b)+(n-len(chosen))*weight(commons[0],b)
    return cost,tuple(path),score[0],max(depth,default=0)


def advance(states,d,keys,b):
    out={}
    for slots,cost in states.items():
        for k in keys:
            if k in slots:continue
            s=(k,slots[1]) if d==0 else (slots[0],k)
            x=cost+weight(k,b)
            if s not in out or x<out[s]:out[s]=x
    return out


def last_cost(states,keys,b):
    return min(c+min(weight(k,b) for k in keys if k not in slots)
               for slots,c in states.items())


def shortest_separation(r,maxT):
    """All binary address words, modulo swapping addresses and final write.

    Three cheapest vs certified high region vs all legal keys (relaxed).
    The actual choice of the final destination cannot affect the key cost.
    """
    b,full,high=palettes(r);three=ordered(high,b)[:3]
    sets=[three,high,full]
    rows=[dict(T=t,words=0,high_better=0,full_better=0) for t in range(1,maxT+1)]
    witnesses={}
    start={(None,None):0}
    def evaluate(prefix,states):
        t=len(prefix)+1;row=rows[t-1];row['words']+=1
        vals=[last_cost(a,k,b) for a,k in zip(states,sets)]
        for j,label in [(1,'high'),(2,'full')]:
            if vals[j]<vals[0]:
                row[label+'_better']+=1
                if label not in witnesses or t<witnesses[label]['T']:
                    ds=prefix+(0,);witnesses[label]=dict(T=t,destinations=ds,
                        three_cost=vals[0],extended_cost=vals[j])
        if t==maxT:return
        for d in ((0,) if not prefix else (0,1)):
            evaluate(prefix+(d,),[advance(a,d,k,b) for a,k in zip(states,sets)])
    evaluate((),[start,start,start])
    return dict(rows=rows,first=witnesses)


def run():
    nc=0;rot_rows=[]
    for r in range(2,8):
        b,full,high=palettes(r)
        for s in range(1,min(r,3)+1):
            for T in range(1,11):
                ds=tuple(t%s for t in range(T))
                for pool in [full,high]:
                    dp=exact(ds,pool,b); form=rotation(r,s,T,pool)
                    assert (None if dp is None else dp[0])==(None if form is None else form[0])
                    nc+=1
    caps=[]
    for r in range(2,128):
        b,G,H=palettes(r);h=1<<(b-1)
        theta=sum((k-h).bit_count()<=2 for k in H)
        gs=[weight(k,b) for k in ordered(G,b)]
        hs=[weight(k,b) for k in ordered(H,b)]
        for j in range(1,len(G)+1):
            high_attains=(j<=len(H) and hs[:j]==gs[:j])
            assert high_attains==(j<=theta)
        if r in (2,4,6,7,8,14,30,62,126):caps.append(dict(r=r,b=b,high_count=len(H),theta=theta))
    for r,s in [(6,2),(6,3),(14,2),(14,3),(14,7)]:
        b,G,H=palettes(r);L=s+1;seq=ordered(H,b)[:L];weights=[weight(k,b) for k in seq]
        rot_rows.append(dict(r=r,s=s,keys=seq,weights=weights,period_sum=sum(weights),
                relaxed_global_period_sum=sum(weight(k,b) for k in ordered(G,b)[:L])))
    ps=0
    for r,k in [(6,1),(6,2),(14,3)]:
        b,G,H=palettes(r);weights=[weight(c,b) for c in ordered(H,b)]
        for n in range(2,9):
            ds=tuple(range(k))+(k,)*n
            cost=((n+1)//2)*weights[0]+(n//2)*weights[1]+sum(weights[2:k+2])
            got=exact(ds,H,b);assert got[0]==cost;ps+=1
    interval_counts={}
    for r,s,tmax in [(6,2,7),(6,3,4),(14,2,8),(30,3,4)]:
        b,G,H=palettes(r);h=1<<(b-1);commons=[k for k in H if weight(k,b)==4];n=0
        for t in range(1,tmax+1):
            for ds in product(range(s),repeat=t):
                model=cheapest_and_common(ds,h,commons,b)
                brute=exact(ds,[h]+commons,b)
                assert (None if model is None else model[0])==(None if brute is None else brute[0])
                if len(commons)>=max(intervals(ds)[1]):
                    full=exact(ds,H,b);assert model[0]==full[0]
                n+=1
        interval_counts[str((r,s,tmax))]=n
    examples=[]
    for r,ds in [(6,(0,1,1,1)),(14,(0,0,1,1,0,1,1,0)),
                 (6,(0,0,1,1,0,0,0,0,1,0,0,0,0,0))]:
        b,G,H=palettes(r);h=1<<(b-1)
        sols={n:exact(ds,K,b) for n,K in [('three_cheapest',ordered(H,b)[:3]),('all_high',H),('all_legal_relaxation',G)]}
        greedy=[];holds={}
        for d in ds:
            k=next(k for k in ordered(H,b) if k not in holds.values())
            greedy.append(k);holds[d]=k
        assert all(sol is not None and check_path(ds,sol[1],b)==sol[0] for sol in sols.values())
        a=cheapest_and_common(ds,h,[k for k in H if weight(k,b)==4],b)
        examples.append(dict(r=r,destinations=ds,greedy=dict(cost=check_path(ds,greedy,b),keys=greedy),
            exact={n:dict(cost=sol[0],keys=sol[1]) for n,sol in sols.items()},
            low_two_tier_cost=a[0] if a else None,ends_zero_based=intervals(ds)[0]))
    shorter={str(r):shortest_separation(r,t) for r,t in [(14,8),(6,14)]}
    assert [shorter[str(r)]['first']['high']['T'] for r in (14,6)]==[8,14]
    for e,vs in zip(examples,[(14,12,12),(26,24,24),(46,44,44)]):
        g=e['greedy']['cost'];h=e['exact']['all_high']['cost'];f=e['exact']['all_legal_relaxation']['cost']
        assert (g,h,f)==vs
    return dict(status='PASS',scope='Finite integer control checks only; all_legal_relaxation ignores initial old blockers. Theorems provide general coverage. Physical BRC observations and costs are separate.',
           rotation_labelled_comparisons=nc,threshold_all_r='2 through 127, all legal prefix sizes',
           selected_thresholds=caps,rotation_examples=rot_rows,parked_family_comparisons=ps,
           labelled_interval_comparisons=interval_counts,examples=examples,
           all_binary_address_words_mod_first_rename_and_last_irrelevance=shorter)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).with_name('rotation_results.json'));a=p.parse_args()
    result=run();a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','rotation_labelled_comparisons','parked_family_comparisons','labelled_interval_comparisons']}))
