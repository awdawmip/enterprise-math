"""GBH: fundamental exchange components of a fixed contracted matching observer."""
from collections import Counter
from itertools import combinations
from random import Random
import json, hashlib
from incremental_tight import Dynamic
from reverse_tight import bits,banks
from unit_slack import reduce_bank,enum_blocks
from unit_quotient import reps
from residual_frontier import reference
from bounded_slack import closures

def components(u,c,x):
    d=Dynamic(c)
    for t,w in u.items(): d.insert(t,w)
    assert d.h==len(u)
    basis=set()
    for t,w in x.items():
        old=d.h; d.insert(t,w)
        if d.h>old: basis.add(t)
    parent={t:t for t in x}
    def root(t):
        while parent[t]!=t:
            parent[t]=parent[parent[t]];t=parent[t]
        return t
    circuits={}; visits=0
    for t,w in x.items():
        if t in basis:continue
        reach=0; todo=w; circ={t}
        while todo:
            jbit=todo&-todo;todo^=jbit
            if reach&jbit:continue
            reach|=jbit;visits+=1
            j=jbit.bit_length()-1
            assert len(d.owners[j])==c[j]
            for y in d.owners[j]:
                if y in basis:circ.add(y)
                todo|=d.opts[y]&~reach
        for y in circ:parent[root(y)]=root(t)
        circuits[t]=sorted(circ)
    groups={}
    for t in x:groups.setdefault(root(t),[]).append(t)
    return sorted([sorted(g) for g in groups.values()]),basis,circuits,visits

def rank(u,c,x):return reference(dict(u,**x),c)-len(u)
def part(x,g):return {t:x[t] for t in g}
def validate(u,c,x,all_subsets=False):
    groups,B,cs,v=components(u,c,x)
    r=rank(u,c,x);assert len(B)==r
    assert sum(rank(u,c,part(x,g)) for g in groups)==r
    assert all(rank(u,c,part(x,g))==len(set(g)&B) for g in groups)
    if all_subsets:
        for t,circ in cs.items():
            want={t}|{b for b in B if rank(u,c,part(x,(B-{b})|{t}))==r}
            assert set(circ)==want
        keys=list(x)
        for m in range(1<<len(keys)):
            Q={t for j,t in enumerate(keys) if m>>j&1}
            assert rank(u,c,part(x,Q))==sum(rank(u,c,part(x,Q&set(g))) for g in groups)
        assert components(u,c,dict(reversed(list(x.items()))))[0]==groups
    return groups,B,cs,v

def random_checks():
    rng=Random(492611270826);st=Counter()
    for _ in range(1600):
        m=rng.randrange(1,8);c=[rng.randrange(1,4) for _ in range(m)]
        u={f'u{i}':rng.randrange(1<<m) for i in range(rng.randrange(12))}
        _,_,p,rc,_=reduce_bank(u,c)
        x={f'x{i}':rng.randrange(1<<len(rc)) for i in range(rng.randrange(9))}
        g,B,cs,v=validate(p,rc,x,True)
        st.update(graphs=1,subset_checks=1<<len(x),circuits=len(cs),components=len(g),reverse_order_checks=1)
    return st

def frozen():
    records=json.load(open('witness_records.json'));st=Counter();positive=[];digest=hashlib.sha256()
    for i,r in enumerate(records):
        c=r['caps'];opts=r['opts'];w=len(c)//2;active=sum(1<<j for j,v in enumerate(c) if v);u={};p={};rc=[];keep=[]
        for j,(a,bc) in enumerate(banks(opts,c,[w,w])):
            bw,h,rp,bc2,kp=reduce_bank(a,bc);off=len(rc)
            u.update({t:v<<(j*w) for t,v in a.items()});p.update({t:v<<off for t,v in rp.items()});rc.extend(bc2);keep.extend(j*w+k for k in kp)
        sh={t:sum(1<<j for j,k in enumerate(keep) if v>>k&1) for t,v in opts.items() if t not in u and v&active}
        g,B,cs,v=validate(p,rc,sh)
        st.update(records=1,raw_shared=len(sh),raw_components=len(g),raw_circuits=len(cs),raw_reach_visits=v,raw_core=sum(len(z) for z in g if len(set(z)&B)<len(z)))
        bl,_,_=enum_blocks(p,rc);x=reps(sh,bl)
        g,B,cs,v=validate(p,rc,x)
        core=[z for z in g if len(set(z)&B)<len(z)]
        st.update(simple_shared=len(x),simple_components=len(g),simple_circuits=len(cs),simple_reach_visits=v,simple_core=sum(map(len,core)),simple_deficient_cases=bool(cs))
        if cs:
            old=closures(p,rc,x,Counter(),False);new=[]
            st['old_pairs']+=len(x)*(len(x)-1)//2
            for z in core:
                st['component_pairs']+=len(z)*(len(z)-1)//2
                new.extend(closures(p,rc,part(x,z),Counter(),False))
            assert set(old)==set(new)
            positive.append(dict(record=i,core=core,basis=sorted(B),circuits=cs,lines=[sorted(z) for z in old]))
        digest.update((json.dumps([i,g,sorted(B),cs],sort_keys=True)+'\n').encode())
    return dict(stats=st,positive=positive,digest=digest.hexdigest())
if __name__=='__main__':print(json.dumps(dict(random=random_checks(),frozen=frozen(),mismatches=0),sort_keys=True))
