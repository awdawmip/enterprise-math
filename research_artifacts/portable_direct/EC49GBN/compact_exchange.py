"""GBN follow-on: port-width signatures and cached greedy-prefix search."""
import json,hashlib,sys
from time import perf_counter
from random import Random
from collections import Counter
import numpy as np
from residual_frontier import cut_costs
from cached_exchange import part,base,ref,sparse,cached

def compact(fs,c,e,b0,st):
    n=len(c)
    def val(s):return sum(min(v for w,v in p.items() if not (s&f)&~w) for f,p in fs)
    if not val(e):return 0,[f for f,p in fs],b0
    # Given old greedy base in fixed port order, prefix values are its sums.
    pref=[0]
    for v in b0:pref.append(pref[-1]+v)
    lo,hi=1,n
    while lo<hi:
        mid=(lo+hi)//2;s=(1<<mid)-1
        st['binary_probes']+=1
        if val(s|e)==pref[mid]:hi=mid
        else:lo=mid+1
    b=b0.copy();b[lo-1]-=1;assert b[lo-1]>=0
    owner={};families=[];ds=0
    def sig(t,f):
        u=0;inter=f;k=[f]*n
        for w in t:
            u|=w;inter&=w
            v=w
            while v:
                bit=v&-v;k[bit.bit_length()-1]&=w;v^=bit
        return u,inter,k
    for l,(f,p) in enumerate(fs):
        rows=[(w,v-sum(b[i] for i in range(n) if w>>i&1)) for w,v in p.items()]
        a=min(v for w,v in rows);d=min(v for w,v in rows if not (e&f)&~w)
        assert a==0 and d>=0;ds+=d
        for i in range(n):
            if f>>i&1:owner[i]=l
        families.append([sig([w for w,v in rows if v==a],f),sig([w for w,v in rows if v==d and not (e&f)&~w],f)])
        st['local_rows']+=len(rows)
    assert ds==1
    def ok(i,j):
        st['exchange_tests']+=1;ki,kj=owner[i],owner[j]
        for (_,inter,k),(u,_,_) in zip(families[ki],families[kj]):
            if ki==kj:
                if not k[j]>>i&1:return False
            elif u>>j&1 and not inter>>i&1:return False
        return True
    return 1,part(c,b,ok),b

def dense(a,c):
    n=len(c);f=np.bincount(a,minlength=1<<n).astype(np.int64);cost=np.array(cut_costs(c),dtype=np.int64)
    for j in range(n):
        z=f.reshape(-1,2,1<<j);z[:,1,:]+=z[:,0,:]
    d=int(max(f-cost));g=cost-f+d
    for j in range(n):
        z=g.reshape(-1,2,1<<j);np.minimum(z[:,0,:],z[:,1,:],out=z[:,0,:])
    return len(a)-d,g.tolist()

def run(c,u,x,st,oldst,digest,i):
    a=list(u);h,g=dense(a,c);p=ref(g,c);b=base(g.__getitem__,len(c))
    for e in x:
        fs=[(f,sparse(g,f)) for f in p]
        t=perf_counter();inc,q,b2=compact(fs,c,e,b,st);st['seconds']+=perf_counter()-t
        t=perf_counter();inc0,q0=cached(fs,c,e,oldst);oldst['seconds']+=perf_counter()-t
        a.append(e);h2,g2=dense(a,c);p2=ref(g2,c)
        assert inc==inc0==h2-h and q==q0==p2 and b2==base(g2.__getitem__,len(c)),(i,e,q,p2)
        st['prefixes']+=1;st['successful']+=inc
        for w,v in enumerate(g2):assert v==sum(g2[w&f] for f in q)
        st['coordinate_checks']+=len(g2)
        for f in q:
            w=(f-1)&f
            while w:
                assert g2[w]+g2[f^w]>g2[f];st['minimality_checks']+=1;w=(w-1)&f
        h,g,p,b=h2,g2,p2,b2
    st['records']+=1;digest.update((json.dumps([i,h,p],separators=(',',':'))+'\n').encode());return h

def main():
    rng=Random(492611271430);st=Counter();old=Counter();digest=hashlib.sha256()
    for i in range(1000):
        n=rng.randrange(1,8);c=[rng.randrange(4) for j in range(n)];u=[rng.randrange(1<<n) for j in range(rng.randrange(14))];x=[rng.randrange(1<<n) for j in range(5)];run(c,u,x,st,old,digest,i)
    print(json.dumps({'random':dict(st),'old':dict(old),'digest':digest.hexdigest()},sort_keys=True),flush=True)
    st=Counter();old=Counter();digest=hashlib.sha256();stride=int(sys.argv[1])
    for i,r in enumerate(json.load(open('witness_records.json'))):
        if i%stride:continue
        c=r['caps'];half=(1<<(len(c)//2))-1;active=sum(1<<j for j,v in enumerate(c) if v);u=[];x=[]
        for v in r['opts'].values():
            e=v&active;(x if e&half and e&~half else u).append(v)
        h=run(c,u,x,st,old,digest,i);assert (h<=r['L'])==r['ans']
    print(json.dumps({'frozen':dict(st),'old':dict(old),'stride':stride,'digest':digest.hexdigest(),'mismatches':0},sort_keys=True),flush=True)
if __name__=='__main__':main()
