"""GBF: exact rank-two quotient of the GBE simple contracted observer."""
from itertools import combinations
from collections import Counter
from random import Random
import json, hashlib
from unit_slack import reduce_bank, enum_blocks
from unit_quotient import reps
from reverse_tight import bits,banks
from residual_frontier import reference,counts,cut_costs

def lines(x, cut2):
    # x has no loops or parallel pairs. All candidates of size >=3 are full lines
    # after removing strict subsets. Keep original target identities.
    groups={frozenset(t for t,e in x.items() if not e&~w) for w in cut2}
    groups={g for g in groups if len(g)>=3}
    out=sorted((g for g in groups if not any(g<h for h in groups)),key=lambda g:tuple(sorted(g)))
    assert all(len(a&b)<=1 for a,b in combinations(out,2))
    return out

def quotient(q, ls, reverse=False):
    q=dict(q)
    for g in (reversed(ls) if reverse else ls):
        present=sorted(g&q.keys(),reverse=reverse)
        for t in present[2:]:del q[t]
    return q

def random_checks():
    rng=Random(492611270631);st=Counter()
    for _ in range(1200):
        m=rng.randrange(1,8);c=[rng.randrange(1,4) for j in range(m)]
        u={f'u{i}':rng.randrange(1<<m) for i in range(rng.randrange(12))}
        W,h,p,rc,keep=reduce_bank(u,c);bl,s,_=enum_blocks(p,rc)
        x=reps({f'x{i}':rng.randrange(1<<len(rc)) for i in range(rng.randrange(9))},bl)
        ls=lines(x,[w for w,v in enumerate(s) if v==2]);st.update(graphs=1,lines=len(ls))
        # All triples compared to independent exact rank.
        for abc in combinations(x,3):
            q={t:x[t] for t in abc};r=reference(dict(p,**q),rc)-len(p)
            assert r==(2 if any(set(abc)<=g for g in ls) else 3);st['triples']+=1
        keys=list(x)
        for mask in range(1<<len(keys)):
            q={t:x[t] for i,t in enumerate(keys) if mask>>i&1};r=reference(dict(p,**q),rc)
            for rev in (False,True):
                q2=quotient(q,ls,rev);assert reference(dict(p,**q2),rc)==r;st['quotient_checks']+=1
            st['subsets']+=1
    return st

def frozen():
    rec=json.load(open('witness_records.json'));st=Counter();hist=Counter();pos=[];digest=hashlib.sha256()
    for i,r in enumerate(rec):
        c=r['caps'];opts=r['opts'];w=len(c)//2;active=sum(1<<j for j,v in enumerate(c) if v);u={};blocks=[];W=0;one=[];two=[]
        for j,(p,bc) in enumerate(banks(opts,c,[w,w])):
            bw,h,rp,rc,keep=reduce_bank(p,bc);bl,s,_=enum_blocks(rp,rc);W|=bw<<(j*w)
            orig=lambda b:sum(1<<keep[k] for k in bits(b))<<(j*w)
            blocks.extend(orig(b) for b in bl);one.append([orig(b) for b,v in enumerate(s) if v==1]);two.extend(orig(b) for b,v in enumerate(s) if v==2)
            u.update({t:v<<(j*w) for t,v in p.items()})
        two.extend(a|b for a in one[0] for b in one[1]);st['slack_two_cuts']+=len(two)
        sh={t:v&active&~W for t,v in opts.items() if t not in u and v&active}
        x=reps(sh,blocks);ls=lines(x,two);q=quotient(x,ls);q2=quotient(x,ls,True)
        H=reference(opts,c);base=reference(u,c)
        for a in (q,q2):assert reference(dict(u,**{t:opts[t] for t in a}),c)==H
        old=base+len(x)-H;new=base+len(q)-H;assert 0<=new<=old
        st.update(records=1,lines=len(ls),rank_two_removed=len(x)-len(q),rank_two_remaining=new,rank_two_representatives=len(q),rank_two_checks=2)
        hist[(old,new)]+=1
        if ls or old:
            row=dict(record=i,old=old,new=new,base=base,H=H,targets=x,lines=[sorted(g) for g in ls],witness_cuts=[v for v in two if any(all(not x[t]&~v for t in g) for g in ls)],retained=sorted(q),reverse_retained=sorted(q2));pos.append(row)
            for g in ls:
                for abc in combinations(g,3):assert reference(dict(u,**{t:opts[t] for t in abc}),c)==base+2;st['line_triples']+=1
        digest.update((json.dumps([i,old,new,[sorted(g) for g in ls],sorted(q),sorted(q2)],sort_keys=True)+'\n').encode())
    return dict(stats=st,hist={str(k):v for k,v in sorted(hist.items())},positive=pos,digest=digest.hexdigest())

if __name__=='__main__':
    print(json.dumps(dict(random=random_checks(),frozen=frozen(),mismatches=0),sort_keys=True))
