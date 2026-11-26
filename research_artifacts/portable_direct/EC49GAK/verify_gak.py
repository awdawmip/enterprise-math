from collections import Counter, defaultdict
from functools import lru_cache
from math import comb
from pathlib import Path
import json

def interval_hist(st,k,H=14):
    by=defaultdict(list)
    for u,h in st:by[u].append(h)
    hist=Counter()
    for u,hs in by.items():
        B=hs[0];A=0
        for h in hs:B&=h;A|=h
        pp=(A^B).bit_count();b=H-B.bit_count()
        if pp>k:return None
        assert len(hs)==sum(comb(pp,z) for z in range(min(pp,b)+1))
        for z in range(min(pp,b)+1):
            hist[z,k if z==b else k-pp+z]+=comb(pp,z)
    return hist


def interval_witness(st,k,H=14):
    hist=interval_hist(st,k,H)
    if hist is None:return ('free',)
    for a in range(k+1):
        for b in range(a,k+1):
            n=sum(v for (l,h),v in hist.items() if l>=a and h<=b)
            cap=sum(comb(k,j) for j in range(a,b+1))
            if n>cap:return (a,b,n,cap)
    return None


def feasible(st,k,R=10,C=25):
    n=len(st);full=(1<<n)-1
    rows=[sum(1<<i for i,(u,h) in enumerate(st) if u>>r&1) for r in range(R)]
    cols=[sum(1<<i for i,(u,h) in enumerate(st) if not(h>>j&1)) for j in range(C)]
    qs=tuple(sorted({a&b for a in rows for b in cols}-{0,full}))
    @lru_cache(None)
    def rec(s,d):
        if s.bit_count()<=1:return True
        if d==0 or s.bit_count()>1<<d:return False
        for q in qs:
            a=s&q;b=s^a
            if a and b and rec(a,d-1) and rec(b,d-1):return True
        return False
    return rec(full,k)


def intervals(st,k,H=14):
    by=defaultdict(list)
    for u,h in st:by[u].append(h)
    data={}
    for u,hs in by.items():
        B=hs[0];A=0
        for h in hs:B&=h;A|=h
        pp=(A^B).bit_count();b=H-B.bit_count()
        for h in hs:
            zc=(h^B).bit_count()
            data[u,h]=(zc,k if zc==b else k-pp+zc)
    return [data[x] for x in st]


def main():
    fr=json.loads(Path('recoverable_frontier.out').read_text())
    stats=Counter(); rows=[]; rankstats=Counter(); node_stats=[]
    for i,line in enumerate(Path('ga_nodes.txt').read_text().splitlines()):
        k,n,*a=map(int,line.split()); st=list(zip(a[::2],a[1::2]))
        for d in (k,k+1):
            wit=interval_witness(st,d); yes=feasible(st,d)
            assert not (wit and yes)
            stats['frozen']+=1
            stats['word_reject' if wit and wit[0]!='free' else 'free_reject' if wit else 'pass']+=1
            stats['exact_yes' if yes else 'exact_no']+=1
            if wit and wit[0]!='free' and n<=2**d:stats['new_word_reject_beyond_count_free']+=1
            rows.append([i,d,int(yes),wit])
        row=fr['rows'][i];iv=intervals(st,k)
        assert row['k']==k and row['n']==n and row['index']==i
        masks=[]
        for l in range(k+1):
            for h in range(l,k+1):
                m=sum(1<<j for j,(a,b) in enumerate(iv) if a>=l and b<=h)
                cap=sum(comb(k,j) for j in range(l,h+1))
                if m.bit_count()>cap:masks.append((m,cap,l,h))
        hit=0
        for t in row['obstructions']:
            rank=t.bit_count()
            rankstats[rank,'total']+=1
            if any((m&t).bit_count()>cap for m,cap,_,_ in masks):
                rankstats[rank,'hit']+=1;hit+=1
        node_stats.append({'i':i,'hits':hit,'total':len(row['obstructions']),
            'min_window_rank':min((cap+1 for _,cap,_,_ in masks),default=None),
            'min_actual_rank':min(x.bit_count() for x in row['obstructions'])})
    out={'stats':dict(stats),'rows':rows,'rankstats':[[r,t,v] for (r,t),v in sorted(rankstats.items())],
         'nodes':node_stats}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
