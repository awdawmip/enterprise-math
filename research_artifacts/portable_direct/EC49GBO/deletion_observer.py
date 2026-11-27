import json,hashlib,numpy as np
from collections import Counter
from random import Random
from time import perf_counter

def suffix(a,m):
    a=a.copy()
    for j in range(m):
        x=a.reshape(-1,2,1<<j);x[:,0,:]=np.minimum(x[:,0,:],x[:,1,:])
    return a

def canonical(a,m,w):
    g=suffix(a,m);p=np.ones(len(w),dtype=bool)
    for j in range(m):
        ix=w[(w&(1<<j))==0];p[ix]&=g[ix]<g[ix|(1<<j)]
    return g,p

def strict(a,m,w):
    v=a.copy();k=w.copy();u=np.full(len(w),int(a.max())+2);t=np.full(len(w),len(w)-1)
    for j in range(m):
        x=v.reshape(-1,2,1<<j);y=k.reshape(-1,2,1<<j)
        l=x[:,0,:].copy();r=x[:,1,:];p=y[:,0,:].copy();q=y[:,1,:]
        y[:,0,:]=np.where(l<r,p,np.where(l>r,q,p&q));x[:,0,:]=np.minimum(l,r)
    for j in range(m):
        ix=w[(w&(1<<j))==0];z=ix|(1<<j);l=u[ix];r=v[z]
        t[ix]=np.where(l<r,t[ix],np.where(l>r,k[z],t[ix]&k[z]));u[ix]=np.minimum(l,r)
    return u,t

def check(c,a,st,rng=None):
    m=len(c);w=np.arange(1<<m);s=sum((w>>j&1)*v for j,v in enumerate(c))
    for e in a:s-=((w&e)==e)
    u,k=strict(s,m,w);old=s<u;live=old.copy()
    for e in set(a):live|=(s==u)&((k&e)==e)&((w&e)!=e)
    union=np.zeros(len(w),dtype=bool)
    st['records']+=1;st['full_rows']+=len(w);st['static_rows']+=int(old.sum());st['one_delete_rows']+=int(live.sum());st['records_with_revival']+=int(np.any(live&~old))
    for e in [None]+sorted(set(a)):
        z=s.copy() if e is None else s+((w&e)==e)
        g,p=canonical(z,m,w);union|=p
        assert np.array_equal(suffix(np.where(live,z,int(z.max())+1),m),g)
        if e is None:assert np.array_equal(old,p)
        st['deletion_states']+=1;st['coordinate_checks']+=len(w)
        if rng:
            for _ in range(4):
                q=rng.randrange(len(w));z-=((w&q)==q)
                assert np.array_equal(suffix(np.where(live,z,int(z.max())+1),m),suffix(z,m))
                st['mixed_checks']+=len(w)
    assert np.array_equal(union,live)
    return int(old.sum()),int(live.sum())

def main():
    rng=Random(492611271530);st=Counter();t=perf_counter()
    for _ in range(1000):
        m=rng.randrange(1,8);c=[rng.randrange(4) for _ in range(m)];a=[rng.randrange(1<<m) for _ in range(rng.randrange(12))]
        check(c,a,st,rng)
    print(json.dumps({'random':dict(st),'seconds':perf_counter()-t},sort_keys=True),flush=True)
    st=Counter();d=hashlib.sha256();t=perf_counter()
    for i,r in enumerate(json.load(open('witness_records.json'))):
        v=check(r['caps'],list(r['opts'].values()),st);d.update((json.dumps([i,*v])+'\n').encode())
    print(json.dumps({'frozen':dict(st),'digest':d.hexdigest(),'seconds':perf_counter()-t,'mismatches':0},sort_keys=True),flush=True)
if __name__=='__main__':main()
