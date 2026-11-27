"""Exact sparse GBJ update; no dense materialization inside step()."""
from collections import Counter,defaultdict
from random import Random
from time import perf_counter
import hashlib,json,numpy as np
from port_observer import direct,compact,expand,push

def step(p,e):
    changed={w:v for w,v in p.items() if e&~w==0}
    h=int(min(changed.values())>0)
    if not h:return h,p
    groups=defaultdict(list)
    for w,v in changed.items():groups[v].append(w)
    # Only unchanged masks can be newly dominated, by changed strict
    # supersets whose OLD weight was exactly one greater.
    out={w:v-1 for w,v in changed.items()}
    for w,v in p.items():
        if w not in changed and not any(w&~t==0 for t in groups.get(v+1,())):out[w]=v
    return h,out

def table(a,c):
    n=1<<len(c); f=np.bincount(a,minlength=n).astype(np.int64); cost=np.zeros(n,dtype=np.int64)
    for j,x in enumerate(c):
        b=1<<j; f.reshape(-1,2*b)[:,b:]+=f.reshape(-1,2*b)[:,:b]
        cost[b:2*b]=cost[:b]+x
    d=int(max(f-cost)); g=cost-f+d
    for j in range(len(c)):
        b=1<<j; z=g.reshape(-1,2*b);np.minimum(z[:,:b],z[:,b:],out=z[:,:b])
    return len(a)-d,g

def envelope(g,m):
    keep=np.ones(len(g),dtype=bool)
    for j in range(m):
        b=1<<j; z=g.reshape(-1,2*b);keep.reshape(-1,2*b)[:,:b]&=z[:,:b]<z[:,b:]
    return {int(w):int(g[w]) for w in np.flatnonzero(keep)}

def check():
    st=Counter();rng=Random(492611271125)
    for _ in range(1000):
        m=rng.randrange(1,9);c=[rng.randrange(4) for j in range(m)];a=[rng.randrange(1<<m) for j in range(rng.randrange(16))]
        h,g=direct(a,c); p=compact(g,m); assert table(a,c)[1].tolist()==g
        for _ in range(8):
            e=rng.randrange(1<<m);inc,q=step(p,e); a.append(e);hh,gg=direct(a,c)
            assert inc==hh-h and q==compact(gg,m) and expand(q,m)==gg
            st['prefixes']+=1;st['coordinates']+=len(gg);h,p=hh,q
        st['graphs']+=1
    return dict(st)

def frozen():
    st=Counter();digest=hashlib.sha256();sample_digest=hashlib.sha256();jobs=[]
    records=json.load(open('witness_records.json'));selected=set(range(0,len(records),16))|{v[0] for v in json.load(open('dynamic_components.jsonl'))['frozen']['dependent']}
    for i,r in enumerate(records):
        c=r['caps'];m=len(c);half=(1<<(m//2))-1;active=sum(1<<j for j,v in enumerate(c) if v);u=[];x=[]
        for v in r['opts'].values():
            e=v&active;(x if e&half and e&~half else u).append(v)
        h,g=table(u,c);p=envelope(g,m);jobs.append((p,x,m));a=u.copy();st['initial_entries']+=len(p);st['dense_slots']+=len(g)
        for e in x:
            inc,q=step(p,e);a.append(e);hh,gg=table(a,c)
            assert inc==hh-h and q==envelope(gg,m) and q.keys()<=p.keys()
            st['prefixes']+=1;st['coordinates']+=len(gg);st['dependent']+=not inc;h,g,p=hh,gg,q
        assert (h<=r['L'])==r['ans'];e=(i*2654435761)%(1<<m);assert table(a+[e]*sum(c),c)[0]-h==g[e]
        st['probes']+=1;st['records']+=1;st['final_entries']+=len(p)
        line=(json.dumps([i,h,sorted(p.items())],separators=(',',':'))+'\n').encode();digest.update(line)
        if i in selected:sample_digest.update(line)
    print(json.dumps({'frozen':dict(st),'digest':digest.hexdigest(),'sample_digest':sample_digest.hexdigest()},sort_keys=True),flush=True)
    times=[]
    # Same already-built input envelopes; measure update-only including all insertions.
    for which in ('sparse','dense','dense','sparse'):
        t0=perf_counter();tot=0
        for p,x,m in jobs:
            for e in x:
                inc,p=step(p,e) if which=='sparse' else push(p,e,m)
                tot+=len(p)
        times.append([which,perf_counter()-t0,tot]);print(json.dumps({'timing':times[-1]}),flush=True)

if __name__=='__main__':
    print(json.dumps({'random':check()},sort_keys=True),flush=True)
    frozen()
