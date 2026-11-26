"""GBG: bounded-slack edge cuts and rank-two seed closures; exact integer replay."""
from itertools import combinations
from collections import Counter
from random import Random
from copy import deepcopy
import json, hashlib
from unit_slack import reduce_bank, enum_blocks
from unit_quotient import reps
from reverse_tight import bits,banks,reverse_tight
from residual_frontier import reference,counts,cut_costs
from rank_two import lines
from incremental_tight import Dynamic

def maximal(ws):
    return sorted(w for w in ws if not any(w!=v and w&~v==0 for v in ws))

def bounded(opts,caps,k,st):
    m=len(caps); D=Dynamic(caps)
    for t,w in opts.items():D.insert(t,w)
    assert D.h==len(opts) and D.live==(1<<m)-1
    sink=m+len(opts);pred=[[] for _ in range(sink+1)];cheap=[];eid=0
    def edge(a,b,c):
        nonlocal eid
        pred[b].append((a,eid))
        if c<=k:cheap.append((eid,c))
        eid+=1
    nodes={t:m+i for i,t in enumerate(opts)}
    for j,os in enumerate(D.owners):
        for t in os:
            edge(j,nodes[t],1)
            for a in bits(opts[t]):edge(nodes[t],a,k+1)
        free=caps[j]-len(os)
        if free:edge(j,sink,free)
    def lost(skip):
        seen={sink};todo=[sink]
        while todo:
            j=todo.pop()
            for a,e in pred[j]:
                if e not in skip and a not in seen:seen.add(a);todo.append(a)
        return sum(1<<j for j in range(m) if j not in seen)
    ws=set()
    def visit(start,budget,chosen):
        st['failure_probes']+=1;ws.add(lost(chosen))
        for i in range(start,len(cheap)):
            e,c=cheap[i]
            if c<=budget:visit(i+1,budget-c,chosen|{e})
    visit(0,k,set());st['distinct_lost']+=len(ws)-1
    return maximal(ws-{0})

def closures(u,c,x,st,adaptive=True):
    base=reverse_tight(u,c)[1]
    if adaptive and reverse_tight(dict(u,**x),c)[1]==base+len(x):
        st['independent_skip']+=1;return []
    groups=set()
    for a,b in combinations(x,2):
        w,h=reverse_tight(dict(u,**{a:x[a],b:x[b]}),c)
        assert h==base+2
        g=frozenset(t for t,v in x.items() if t in (a,b) or v&~w==0)
        assert a in g and b in g
        st['pair_seed_queries']+=1
        if len(g)>=3:groups.add(g)
    return sorted(groups,key=lambda g:tuple(sorted(g)))

def check(u,c,x,st,kmax=2,adaptive=True):
    s=[a-b for a,b in zip(cut_costs(c),counts(u.values(),len(c)))];assert s[0]==0 and all(v>=1 for v in s[1:])
    for k in range(1,kmax+1):
        out=bounded(u,c,k,st);ref=maximal({w for w,v in enumerate(s) if w and v<=k});assert out==ref,(u,c,k,out,ref)
        st['cut_checks']+=1;st['enumerated_cuts']+=len(s)
        if k==2:
            got=lines(x,out);want=lines(x,[w for w,v in enumerate(s) if v==2]);assert got==want
            assert closures(u,c,x,st,adaptive)==want
            st['line_checks']+=1;st['lines']+=len(want)
    return want

def random_checks():
    rng=Random(492611270731);st=Counter()
    for _ in range(1500):
        m=rng.randrange(1,8);c=[rng.randrange(1,4) for _ in range(m)]
        u={f'u{i}':rng.randrange(1<<m) for i in range(rng.randrange(12))}
        _,_,p,rc,_=reduce_bank(u,c);bl,_,_=enum_blocks(p,rc)
        x=reps({f'x{i}':rng.randrange(1<<len(rc)) for i in range(rng.randrange(9))},bl)
        check(p,rc,x,st,3,False);st['graphs']+=1
    return st

def frozen():
    records=json.load(open('witness_records.json'));st=Counter();pos=[];digest=hashlib.sha256()
    for i,r in enumerate(records):
        c=r['caps'];opts=r['opts'];w=len(c)//2;active=sum(1<<j for j,v in enumerate(c) if v);u={};p={};W=0;rc=[];keep=[]
        for j,(a,bc) in enumerate(banks(opts,c,[w,w])):
            bw,h,rp,bc2,kp=reduce_bank(a,bc);W|=bw<<(j*w);off=len(rc)
            u.update({t:v<<(j*w) for t,v in a.items()});p.update({t:v<<off for t,v in rp.items()});rc.extend(bc2);keep.extend(j*w+k for k in kp)
        sh={t:sum(1<<j for j,k in enumerate(keep) if v>>k&1) for t,v in opts.items() if t not in u and v&active}
        bl,_,_=enum_blocks(p,rc);x=reps(sh,bl)
        g=check(p,rc,x,st,2);st['records']+=1
        if g:pos.append(dict(record=i,groups=[sorted(z) for z in g],masks={t:opts[t] for z in g for t in z}))
        digest.update((json.dumps([i,[sorted(z) for z in g]],sort_keys=True)+'\n').encode())
    return dict(stats=st,positive=pos,digest=digest.hexdigest())

if __name__=='__main__':
    print(json.dumps(dict(random=random_checks(),frozen=frozen(),mismatches=0),sort_keys=True))
