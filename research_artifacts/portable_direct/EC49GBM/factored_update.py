"""Exact sparse factor update, BRC16943 integer-mask observer. No dense table in update."""
from port_observer import direct, compact
from collections import Counter
from random import Random
from time import perf_counter
import json, hashlib, sys

def bits(w):
    while w:
        b=w&-w;yield b;w^=b

def value(p,s):
    return min(v for w,v in p.items() if not s&~w)

def prune(q):
    out={}
    for w,v in sorted(q.items(),key=lambda a:(a[1],-a[0].bit_count(),a[0])):
        if not any(not w&~t for t in out):out[w]=v
    return out

def project(p,f,e=0):
    q={}
    for w,v in p.items():
        if e&~w:continue
        t=w&f;q[t]=min(v,q.get(t,v))
    return prune(q)

def total(fs,s):return sum(value(p,s&f) for f,p in fs)

def partition(fs, c, e=None, st=None):
    # Greedy base of g or g contracted by one fresh target.
    mask=0
    for f,p in fs:mask|=f
    ix=list(bits(mask)); b={}; s=last=0
    for i in ix:
        s|=i;v=total(fs,s)
        if e is not None:v=min(v,total(fs,s|e)-1)
        b[i]=v-last;last=v
    # A nonnegative probe multiplicity z extends iff the two independent
    # support minima have slack >=0 and >=1 respectively.
    def feasible(z):
        a=d=0
        for f,p in fs:
            vals=[(w,v-sum(z[i] for i in bits(w))) for w,v in p.items()]
            a+=min(v for w,v in vals)
            if e is not None:d+=min(v for w,v in vals if not (e&f)&~w)
        return a>=0 and (e is None or d>=1)
    parent={i:i for i in ix}
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    for i in ix:
        if not b[i]:continue
        for j in ix:
            if i==j or b[j]>=c[j.bit_length()-1] or root(i)==root(j):continue
            b[i]-=1;b[j]+=1
            if st is not None:st['exchange_tests']+=1
            if feasible(b):parent[root(j)]=root(i)
            b[i]+=1;b[j]-=1
    out={}
    for i in ix:out[root(i)]=out.get(root(i),0)|i
    return sorted(out.values())

def restricted(fs,f,e,st):
    # Separate min envelopes for g(S) and g(S union E)-1.
    def term(shift):
        q={0:-int(shift)}
        for a,p in fs:
            local=project(p,f&a,(e&a) if shift else 0)
            st['local_product_pairs']+=len(q)*len(local)
            q={w|t:v+u for w,v in q.items() for t,u in local.items()}
        return q
    if min(total(fs,f),total(fs,f|e)-1)==0:return {f:0}
    q=term(False)
    for w,v in term(True).items():q[w]=min(v,q.get(w,v))
    return prune(q)

def initialize(p,c,st):
    f=(1<<len(c))-1;fs=[(f,p)]
    return [(a,project(p,a)) for a in partition(fs,c,st=st)]

def push(fs,e,c,st):
    active=[(f,p) for f,p in fs if value(p,e&f)>0]
    if not active:return 0,fs
    d=0
    for f,p in active:d|=f
    e&=d
    st['active_width']+=d.bit_count();st['global_width']+=len(c)
    # For one active factor use GBK reweighting directly, then split.
    if len(active)==1:
        f,p=active[0];q=prune({w:v-int(not e&~w) for w,v in p.items()})
        updated=[(a,project(q,a)) for a in partition([(f,q)],c,st=st)]
    else:
        st['global_product_avoided']+=prod(len(p) for f,p in active)
        updated=[(a,restricted(active,a,e,st)) for a in partition(active,c,e,st)]
    return 1,sorted([(f,p) for f,p in fs if not f&d]+updated)

def prod(xs):
    a=1
    for x in xs:a*=x
    return a

def check(fs,g,st):
    assert all(total(fs,w)==v for w,v in enumerate(g))
    st['coordinate_checks']+=len(g)
    for f,p in fs:
        w=(f-1)&f
        while w:
            assert g[w]+g[f^w]>g[f];st['minimality_checks']+=1;w=(w-1)&f

def run(c,u,x,st,digest=None,i=0):
    h,g=direct(u,c);fs=initialize(compact(g,len(c)),c,st);check(fs,g,st)
    a=list(u);st['initial_factor_entries']+=sum(len(p) for f,p in fs)
    for e in x:
        t=perf_counter();inc,fs=push(fs,e,c,st);st['update_seconds']+=perf_counter()-t
        a.append(e);h2,g=direct(a,c);assert h2-h==inc;h=h2;check(fs,g,st)
        st['prefix_checks']+=1
    st['final_factor_entries']+=sum(len(p) for f,p in fs);st['records']+=1
    if digest is not None:digest.update((json.dumps([i,h,[(f,sorted(p.items())) for f,p in fs]],separators=(',',':'))+'\n').encode())
    return h

def main():
    rng=Random(492611271330);st=Counter()
    for _ in range(600):
        m=rng.randrange(1,8);c=[rng.randrange(4) for j in range(m)];u=[rng.randrange(1<<m) for j in range(rng.randrange(14))];x=[rng.randrange(1<<m) for j in range(5)];run(c,u,x,st)
    print(json.dumps({'random':dict(st)},sort_keys=True),flush=True)
    st=Counter();digest=hashlib.sha256();records=json.load(open('witness_records.json'))
    stride=int(sys.argv[1]) if len(sys.argv)>1 else 1
    for i,r in enumerate(records):
        if i%stride:continue
        c=r['caps'];m=len(c);half=(1<<(m//2))-1;active=sum(1<<j for j,v in enumerate(c) if v);u=[];x=[]
        for v in r['opts'].values():
            e=v&active;(x if e&half and e&~half else u).append(v)
        h=run(c,u,x,st,digest,i);assert (h<=r['L'])==r['ans']
    print(json.dumps({'frozen':dict(st),'stride':stride,'digest':digest.hexdigest(),'mismatches':0},sort_keys=True),flush=True)
if __name__=='__main__':main()
