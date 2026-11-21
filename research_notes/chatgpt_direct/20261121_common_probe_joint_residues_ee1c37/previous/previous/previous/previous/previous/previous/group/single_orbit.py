"""Enumerate occupied line sets under one translation orbit, up to the direction stabilizer."""
from pathlib import Path
from generate import maps,profiles
import sys
def bits(m):
    while m:
        low=m&-m
        yield low.bit_length()-1
        m-=low

def collect(work):
    lin,trans,syms=maps()
    rows={}
    with (work/'bank').open()as f:
        for _ in range(int(next(f))):
            s,c,n=map(int,next(f).split())
            rows[s,c]=[(lo | hi<<64)for lo,hi in (map(int,next(f).split())for _ in range(n))]
    ts=list(rows)
    ps=profiles(ts,8728)
    out=[]
    for p,step,_ in syms:
        if p!=5:continue
        lines=[];ix={}
        for v in range(125):
            if v in ix:continue
            ls=[];i=v
            while i not in ls:ls.append(i);i=step[i]
            for i in ls:ix[i]=len(lines)
            lines.append(ls)
        maps25={bytes(ix[t[g[z[0]]]]for z in lines) for g in lin if ix[g[step[0]]]==ix[0] for t in trans}
        for k,key in enumerate(ts):
            if not any(cnt[k]>=5 for _,cnt in ps):continue
            seeds={}
            for r in rows[key]:
                q=sum(1<<i for i in {ix[j]for j in bits(r)})
                if q.bit_count()==key[0]:seeds.setdefault(q,r)
            while seeds:
                q,r=next(iter(seeds.items()))
                for g in maps25:seeds.pop(sum(1<<g[i]for i in bits(q)),None)
                orbit=[r]
                for _ in range(4):orbit.append(sum(1<<step[i]for i in bits(orbit[-1])))
                u=sum(orbit)
                assert u.bit_count()==5*key[0]
                out.append((k,u,orbit))
    with (work/'single').open('w')as f:
        for k,u,masks in out:
            print(k,u%(1<<64),u>>64,*[x for m in masks for x in [m%(1<<64),m>>64]],file=f)
    print('One-orbit residual types',len(out),flush=True)
if __name__=='__main__':collect(Path(sys.argv[1]))
