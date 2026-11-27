"""GBJ: normalized Hall residual port observer; exact integer masks.
Run in verified GBI archive root: python port_observer.py.
"""
from collections import Counter
from random import Random
import hashlib,json
from residual_frontier import counts,cut_costs,reference

def suffix_min(a,m):
    a=a.copy()
    for j in range(m):
        b=1<<j
        for w in range(len(a)):
            if not w&b:a[w]=min(a[w],a[w|b])
    return a

def direct(opts,c):
    m=len(c);f=counts(opts,m);cost=cut_costs(c)
    d=max(x-y for x,y in zip(f,cost))
    return len(opts)-d,suffix_min([y-x+d for x,y in zip(f,cost)],m)

def compact(g,m):
    return {w:v for w,v in enumerate(g) if all(g[w|1<<j]>v for j in range(m) if not w>>j&1)}

def expand(p,m):
    a=[max(p.values())+1]*(1<<m)
    for w,v in p.items():a[w]=v
    return suffix_min(a,m)

def push(p,e,m):
    h=int(min(v for w,v in p.items() if e&~w==0)>0)
    if not h:return h,p.copy()
    q={w:v-int(e&~w==0) for w,v in p.items()}
    return h,compact(expand(q,m),m)

def stats(p,g,c,st,tag):
    m=len(c);st[tag+'_entries']+=len(p);st[tag+'_dense']+=len(g)
    st[tag+'_modular']+=all(v==sum(g[1<<j] for j in range(m) if w>>j&1) for w,v in enumerate(g))
    st[tag+'_zero_rank']+=g[-1]==0
    st[tag+'_max_entries']=max(st[tag+'_max_entries'],len(p))

def run_random():
    rng=Random(492611271031);st=Counter()
    for _ in range(700):
        m=rng.randrange(1,8);c=[rng.randrange(4) for j in range(m)]
        a=[rng.randrange(1<<m) for j in range(rng.randrange(13))]
        h,g=direct(a,c);p=compact(g,m);assert expand(p,m)==g
        for e in range(1<<m):
            q=a+[e]*sum(c)
            assert reference(dict(enumerate(q)),c)-h==g[e]
            st['probe_checks']+=1
        for _ in range(8):
            e=rng.randrange(1<<m);inc,p2=push(p,e,m);a.append(e)
            h2,g2=direct(a,c)
            assert h2-h==inc and expand(p2,m)==g2 and p2==compact(g2,m)
            assert p2.keys()<=p.keys()
            assert g2==[min(v+1-inc,g[w|e]-inc) for w,v in enumerate(g)]
            st['prefix_checks']+=1;st['coordinate_checks']+=len(g);st['dependent_insertions']+=not inc
            h,g,p=h2,g2,p2
        st['graphs']+=1
    return dict(st)

def run_frozen(sample=True):
    st=Counter();digest=hashlib.sha256();examples=[]
    records=json.load(open('witness_records.json'))
    selected=set(range(0,len(records),16)) | {v[0] for v in json.load(open('dynamic_components.jsonl'))['frozen']['dependent']}
    for i,r in enumerate(records):
        if sample and i not in selected:continue
        c=r['caps'];m=len(c);half=(1<<(m//2))-1;active=sum(1<<j for j,v in enumerate(c) if v)
        u=[];x=[]
        for v in r['opts'].values():
            e=v&active
            (x if e&half and e&~half else u).append(v)
        h,g=direct(u,c);p=compact(g,m);stats(p,g,c,st,'initial');assert expand(p,m)==g
        start=len(p);a=u.copy()
        for e in x:
            inc,p2=push(p,e,m);a.append(e);h2,g2=direct(a,c)
            assert inc==h2-h and expand(p2,m)==g2 and p2==compact(g2,m)
            assert p2.keys()<=p.keys()
            st['prefix_checks']+=1;st['coordinate_checks']+=len(g);st['dependent_insertions']+=not inc
            h,g,p=h2,g2,p2
        assert h==reference(r['opts'],c) and (h<=r['L'])==r['ans']
        stats(p,g,c,st,'final');st['records']+=1;st['support_removed']+=start-len(p)
        e=(i*2654435761) % (1<<m)
        q=list(r['opts'].values())+[e]*sum(c)
        assert reference(dict(enumerate(q)),c)-h==g[e]
        st['probe_checks']+=1
        digest.update((json.dumps([i,h,sorted(p.items())],separators=(',',':'))+'\n').encode())
        if len(examples)<5 and not all(v==sum(g[1<<j] for j in range(m) if w>>j&1) for w,v in enumerate(g)):
            examples.append({'record':i,'caps':c,'rank':h,'support':sorted(p.items())})
    return dict(stats=st,digest=digest.hexdigest(),nonmodular_examples=examples,selection='stride16 union GBI dependent records' if sample else 'all')

if __name__=='__main__':
    import sys
    if 'sample' not in sys.argv and 'full' not in sys.argv:print(json.dumps({'random':run_random()},sort_keys=True),flush=True)
    if 'random' not in sys.argv:print(json.dumps({'frozen':run_frozen('full' not in sys.argv),'mismatches':0},sort_keys=True),flush=True)
