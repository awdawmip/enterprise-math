"""GBN: cached local tight signatures; exact frozen-mask replay."""
import json,sys,hashlib
from collections import Counter
from random import Random
from residual_frontier import cut_costs
from port_observer import direct

def part(c,b,ok):
    p=[1<<i for i in range(len(c))]
    for i in range(len(c)):
        for j in range(len(c)):
            if i!=j and b[i]>0 and b[j]<c[j] and p[i]!=p[j] and ok(i,j):
                a,d=p[i],p[j];p=[a|d if v in (a,d) else v for v in p]
    return sorted(set(p))

def base(v,n):
    s=last=0;b=[]
    for i in range(n):
        s|=1<<i;q=v(s);b.append(q-last);last=q
    return b

def signature(t,n):
    return [sum(1<<k for k,w in enumerate(t) if w>>i&1) for i in range(n)],(1<<len(t))-1

def ref(g,c):
    b=base(g.__getitem__,len(c));cost=cut_costs(b)
    s,_=signature([w for w,v in enumerate(g) if v==cost[w]],len(c))
    return part(c,b,lambda i,j:not s[j]&~s[i])

def sparse(g,f):
    q={};w=f
    while True:
        v=g[w]
        if all(g[w|1<<i]>v for i in range(f.bit_length()) if (f&~w)>>i&1):q[w]=v
        if not w:return q
        w=(w-1)&f

def cached(fs,c,e,st):
    n=len(c)
    def val(s):return sum(min(v for w,v in p.items() if not (s&f)&~w) for f,p in fs)
    if not val(e):return 0,[f for f,p in fs]
    b=base(lambda s:min(val(s),val(s|e)-1),n);owner={};families=[];ds=0
    for k,(f,p) in enumerate(fs):
        rows=[(w,v-sum(b[i] for i in range(n) if w>>i&1)) for w,v in p.items()]
        a=min(v for w,v in rows);d=min(v for w,v in rows if not (e&f)&~w)
        assert a==0 and d>=0;ds+=d
        for i in range(n):
            if f>>i&1:owner[i]=k
        families.append([signature([w for w,v in rows if v==a],n),signature([w for w,v in rows if v==d and not (e&f)&~w],n)])
        st['local_rows']+=len(rows)
    assert ds==1
    def ok(i,j):
        st['exchange_tests']+=1;ki,kj=owner[i],owner[j]
        for (si,all_i),(sj,_) in zip(families[ki],families[kj]):
            if ki==kj:
                if sj[j]&~si[i]:return False
            elif sj[j] and si[i]!=all_i:return False
        return True
    return 1,part(c,b,ok)

def run(c,u,x,st,digest,i):
    a=list(u);h,g=direct(a,c);p=ref(g,c)
    for e in x:
        inc,q=cached([(f,sparse(g,f)) for f in p],c,e,st)
        a.append(e);h2,g2=direct(a,c);p2=ref(g2,c)
        assert inc==h2-h and q==p2,(i,e,q,p2)
        st['prefixes']+=1;st['successful']+=inc
        for w,v in enumerate(g2):assert v==sum(g2[w&f] for f in q)
        st['coordinate_checks']+=len(g2)
        for f in q:
            w=(f-1)&f
            while w:
                assert g2[w]+g2[f^w]>g2[f];st['minimality_checks']+=1;w=(w-1)&f
        h,g,p=h2,g2,p2
    st['records']+=1;digest.update((json.dumps([i,h,p],separators=(',',':'))+'\n').encode());return h

def main():
    rng=Random(492611271430);st=Counter();digest=hashlib.sha256()
    for i in range(1000):
        n=rng.randrange(1,8);c=[rng.randrange(4) for j in range(n)];u=[rng.randrange(1<<n) for j in range(rng.randrange(14))];x=[rng.randrange(1<<n) for j in range(5)];run(c,u,x,st,digest,i)
    print(json.dumps({'random':dict(st),'digest':digest.hexdigest()},sort_keys=True),flush=True)
    st=Counter();digest=hashlib.sha256();stride=int(sys.argv[1])
    for i,r in enumerate(json.load(open('witness_records.json'))):
        if i%stride:continue
        c=r['caps'];half=(1<<(len(c)//2))-1;active=sum(1<<j for j,v in enumerate(c) if v);u=[];x=[]
        for v in r['opts'].values():
            e=v&active;(x if e&half and e&~half else u).append(v)
        h=run(c,u,x,st,digest,i);assert (h<=r['L'])==r['ans']
    print(json.dumps({'frozen':dict(st),'stride':stride,'digest':digest.hexdigest(),'mismatches':0},sort_keys=True),flush=True)
if __name__=='__main__':main()
