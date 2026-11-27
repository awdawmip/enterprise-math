"""GBL: exact port factorization by tight basis exchange. Run from GBJ archive root."""
from collections import Counter
from random import Random
from time import perf_counter
import hashlib,json
import numpy as np
from port_observer import direct,compact
from residual_frontier import cut_costs,counts

def value(p,s):
    return min(v for w,v in p.items() if s&~w==0)

def factors(p,c):
    m=len(c); b=[]; prefix=last=0
    for i in range(m):
        prefix|=1<<i;v=value(p,prefix);b.append(v-last);last=v
    costs=cut_costs(b)
    tight=[w for w,v in p.items() if costs[w]==v]
    sig=[sum(1<<k for k,w in enumerate(tight) if w>>i&1) for i in range(m)]
    parent=list(range(m))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i in range(m):
        if not b[i]:continue
        for j in range(m):
            if i!=j and b[j]<c[j] and sig[j]&~sig[i]==0:
                parent[root(j)]=root(i)
    out={}
    for i in range(m):out[root(i)]=out.get(root(i),0)|(1<<i)
    return sorted(out.values())

def split(p,parts):
    out=[]
    for a in parts:
        q={}
        for w,v in p.items():
            t=w&a;q[t]=min(q.get(t,v),v)
        # Restriction is exactly a min envelope over projected support masks.
        out.append({w:v for w,v in q.items() if not any(w!=t and w&~t==0 and u<=v for t,u in q.items())})
    return out

def update(p,e):
    h=int(value(p,e)>0)
    if not h:return h,p
    q={w:v-int(e&~w==0) for w,v in p.items()}
    return h,{w:v for w,v in q.items() if not any(w!=t and w&~t==0 and u<=v for t,u in q.items())}

def dense(a,c):
    m=len(c);f=np.bincount(a,minlength=1<<m).astype(np.int64);cost=np.array(cut_costs(c),dtype=np.int64)
    for j in range(m):
        z=f.reshape(-1,2,1<<j);z[:,1,:]+=z[:,0,:]
    d=int(max(f-cost));g=cost-f+d
    for j in range(m):
        z=g.reshape(-1,2,1<<j);np.minimum(z[:,0,:],z[:,1,:],out=z[:,0,:])
    keep=np.ones(len(g),dtype=bool)
    for j in range(m):
        v=g.reshape(-1,2,1<<j);k=keep.reshape(-1,2,1<<j);k[:,0,:]&=v[:,0,:]<v[:,1,:]
    return len(a)-d,g.tolist(),{int(w):int(g[w]) for w in np.flatnonzero(keep)}

def check(g,p,c,st,tag):
    parts=factors(p,c); fs=split(p,parts);m=len(c);full=(1<<m)-1
    assert all(g[w]==sum(value(q,w&a) for a,q in zip(parts,fs)) for w in range(len(g)))
    # No factor admits any nontrivial additive split. For submodular g,
    # equality at the full factor is sufficient for all subqueries.
    for a in parts:
        w=(a-1)&a
        while w:
            assert g[w]+g[a^w]>g[a];st['minimality_checks']+=1;w=(w-1)&a
    st['coordinate_checks']+=len(g);st[tag+'_records']+=1;st[tag+'_global_support']+=len(p)
    st[tag+'_factor_support']+=sum(map(len,fs));st[tag+'_factor_dense']+=sum(1<<a.bit_count() for a in parts)
    st[tag+'_dense']+=len(g);st[tag+'_factor_count']+=len(parts);st[tag+'_nontrivial']+=sum(a.bit_count()>1 for a in parts)
    st[tag+'_max_width']=max(st[tag+'_max_width'],max(a.bit_count() for a in parts))
    return parts,fs

def main():
    rng=Random(492611271230);st=Counter();hist=Counter();examples=[];digest=hashlib.sha256()
    for _ in range(1000):
        m=rng.randrange(1,8);c=[rng.randrange(4) for j in range(m)];a=[rng.randrange(1<<m) for j in range(rng.randrange(14))]
        h,g=direct(a,c);p=compact(g,m);parts,fs=check(g,p,c,st,'random')
        for _ in range(4):
            e=rng.randrange(1<<m);live=[i for i,(w,q) in enumerate(zip(parts,fs)) if value(q,e&w)>0]
            union=0
            for i in live:union|=parts[i]
            # Check local coupling identity, including ignored zero-rank ports.
            local={w:g[w] for w in range(1<<m) if w&~union==0}
            a.append(e);h2,g2=direct(a,c);p2=compact(g2,m)
            assert h2-h==bool(live)
            for w in range(1<<m):
                v=g[w] if not live else g[w&~union]+min(local[w&union],local[(w|e)&union]-1)
                assert v==g2[w];st['local_update_checks']+=1
            parts,fs=check(g2,p2,c,st,'random');h,g,p=h2,g2,p2
    print(json.dumps({'random':dict(st)},sort_keys=True),flush=True)
    st=Counter();records=json.load(open('witness_records.json'))
    for i,r in enumerate(records):
        c=r['caps'];m=len(c);half=(1<<(m//2))-1;active=sum(1<<j for j,v in enumerate(c) if v);u=[];x=[]
        for v in r['opts'].values():
            e=v&active;(x if e&half and e&~half else u).append(v)
        h,g,p=dense(u,c);parts,fs=check(g,p,c,st,'initial')
        h,g,p=dense(u+x,c);assert (h<=r['L'])==r['ans'];parts,fs=check(g,p,c,st,'final')
        hist[tuple(sorted(a.bit_count() for a in parts))]+=1
        digest.update((json.dumps([i,h,parts,[sorted(q.items()) for q in fs]],separators=(',',':'))+'\n').encode())
        if len(examples)<5 and any(a.bit_count()>1 for a in parts):examples.append({'record':i,'caps':c,'rank':h,'parts':parts,'factor_support':[sorted(q.items()) for q in fs]})
    print(json.dumps({'frozen':dict(st),'final_width_histogram':[[list(k),v] for k,v in sorted(hist.items())],'examples':examples,'digest':digest.hexdigest(),'mismatches':0},sort_keys=True),flush=True)
if __name__=='__main__':main()
