"""Stage472-B standalone positive-integer BRC, fixed A/B/C embedded in signed X6.
Counts exact full-observer repair populations and supports for m-1 <= t <= n.
Future equivalence is Stage469-B's separately audited premise.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product
import json

D=range(3); Z=(0,)*9; ix=lambda a,b:3*a+b

def inc(c,a,b):
    v=list(c);v[ix(a,b)]+=1;return tuple(v)

def fits(c,d):return all(x<=y for x,y in zip(c,d))

def ec(w):
    z=Z
    for a,b in zip(w,w[1:]):z=inc(z,a,b)
    return z

def obs(p,q):return (len(p),len(q),ec(p),ec(q),sum(a==b for a,b in zip(p,q)))

def last(ep):
    f=[sum(ep[ix(a,b)] for b in D)-sum(ep[ix(b,a)] for b in D) for a in D]
    r=[a for a in D if all(f[x]==(x==0)-(x==a) for x in D)]
    assert len(r)==1
    return r[0]

def repair(p,q,t):
    m=len(p)
    return (p[m-2],)+((q[m-1],) if t>m else ())+((q[m],) if t>m+1 else ())+q[t-1:]

def solve(phi,t):
    m,n,EP,EQ,K=phi; assert 4<=m<n and m-1<=t<=n
    pm=last(EP);tag_len=1+(t>m)+(t>m+1)
    # BRC H_t: original prefix mass with ordered adjacency and overlap counters.
    h={(0,0,Z,Z,1,-1,-1,-1):1}
    for j in range(2,t+1):
        nx=defaultdict(int)
        for (lp,lq,pe,qe,k,p1,qm,q1),w in h.items():
            for p in ((pm,) if j==m else D if j<m else (None,)):
                pp=inc(pe,lp,p) if p is not None else pe
                if not fits(pp,EP):continue
                for q in D:
                    qq=inc(qe,lq,q)
                    if not fits(qq,EQ):continue
                    kk=k+(p==q if p is not None else 0)
                    if kk>K:continue
                    nx[(p if p is not None else lp,q,pp,qq,kk,p if j==m-1 else p1,
                        q if j==m and t>m else qm,q if j==m+1 and t>m+1 else q1)]+=w
        h=nx
    if t==m-1:
        nx=defaultdict(int)
        for (lp,lq,pe,qe,k,p1,qm,q1),w in h.items():
            if inc(pe,lp,pm)==EP:nx[(pm,lq,EP,qe,k,lp,qm,q1)]+=w
        h=nx
    by=defaultdict(list)
    for (lp,lq,pe,qe,k,p1,qm,q1),w in h.items():
        if pe!=EP:continue
        hd=(p1,)+((qm,) if t>m else ())+((q1,) if t>m+1 else ())+ (lq,)
        assert -1 not in hd
        by[hd].append((qe,k,w))
    @lru_cache(None)
    def tail(hd,j,q,edges,extra):
        if j==n:
            pop=sum(w for e,k,w in by[hd] if k+extra==K and all(e[z]+edges[z]==EQ[z] for z in range(9)))
            return (int(pop>0),pop)
        s=mass=0
        for z in D:
            e=inc(edges,q,z)
            if not fits(e,EQ):continue
            ext=extra+(int(z==pm) if t==m-1 and j+1==m else 0)
            if ext>K:continue
            a,b=tail(hd,j+1,z,e,ext);s+=a;mass+=b
        return (s,mass)
    heads=sorted(by)
    roots={hd:(hd,t,hd[-1],Z,0) for hd in heads}
    values={hd:tail(*root) for hd,root in roots.items()}
    def descend(hd,j,q,e,x,z):
        ne=inc(e,q,z)
        if not fits(ne,EQ):return None
        xx=x+(int(z==pm) if t==m-1 and j+1==m else 0)
        return (hd,j+1,z,ne,xx) if xx<=K else None
    def unrank(rank):
        assert 0<=rank<support
        for hd in heads:
            if rank<values[hd][0]:break
            rank-=values[hd][0]
        key=list(hd);st=roots[hd]
        while st[1]<n:
            for z in D:
                child=descend(*st,z)
                a=tail(*child)[0] if child else 0
                if rank>=a:rank-=a
                else:key.append(z);st=child;break
            else:raise AssertionError('unrank path')
        return tuple(key)
    def rankmass(key):
        if len(key)!=tag_len+1+n-t:return None
        hd=tuple(key[:tag_len+1]);st=roots.get(hd)
        if st is None:return None
        rank=sum(values[h][0] for h in heads if h<hd)
        for z in key[tag_len+1:]:
            for x in D:
                if x>=z:break
                child=descend(*st,x)
                if child:rank+=tail(*child)[0]
            st=descend(*st,z)
            if st is None:return None
        a,w=tail(*st)
        return (rank,w) if a else None
    support=sum(v[0] for v in values.values());pop=sum(v[1] for v in values.values())
    return {'support':support,'population':pop,'prefix_states':len(h),
            'tag_heads':len(heads),'suffix_states':tail.cache_info().currsize,
            'unrank':unrank,'rankmass':rankmass}

def test():
    stats=Counter()
    for m,n,t in [(4,5,3),(4,5,4),(4,5,5),(4,6,3),(4,6,4),(4,6,5),(4,6,6),
                  (5,6,4),(5,6,5),(5,6,6),(5,7,4),(5,7,5),(5,7,6),(5,7,7)]:
        fibers=defaultdict(list)
        for pp in product(D,repeat=m-1):
            for qq in product(D,repeat=n-1):
                p=(0,)+pp;q=(0,)+qq;fibers[obs(p,q)].append((p,q))
        chosen=sorted(fibers.items(),key=lambda v:(-len(v[1]),repr(v[0])))[:40]
        for phi,pairs in chosen:
            actual=Counter(repair(p,q,t) for p,q in pairs)
            r=solve(phi,t)
            assert r['support']==len(actual) and r['population']==len(pairs)
            for rank,key in enumerate(sorted(actual)):
                assert r['rankmass'](key)==(rank,actual[key])
                assert r['unrank'](rank)==key
                stats['classes']+=1
            stats['fibers']+=1
        stats['configs']+=1
    p=(0,)*35
    q=(0,)
    for z in (1,)*14+(2,)*12:q+=(z,0)
    q+=(0,)*3
    assert len(q)==56
    large=[]
    for t in (34,35,36,37,56):
        v=solve(obs(p,q),t)
        assert v['population']==11154643500
        for r in (0,1,100,1000):
            if r<v['support']:assert v['rankmass'](v['unrank'](r))[0]==r
        large.append({'t':t,'support':v['support'],'population':v['population'],
                      'prefix_states':v['prefix_states'],'suffix_states':v['suffix_states']})
    return dict(stats),large

if __name__=='__main__':
    small,large=test()
    print(json.dumps({'stage':'472-B','small':small,'large':large,'ok':True},indent=2))
