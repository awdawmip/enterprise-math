"""Exact finite two-measure non-iid observer quotient checks (author only)."""
from collections import defaultdict
from fractions import Fraction as R

P, Q, C = 'P', 'Q', 'C'

def eval_policy(p, q, act, N=2):
    live = {(): (R(1), R(1))}; action_flows = defaultdict(lambda: defaultdict(R))
    obs = [R(0) for _ in range(4)]
    for n in range(N+1):
        next_live = defaultdict(lambda: [R(0),R(0)])
        for h,(mp,mq) in live.items():
            a = act(h)
            assert sum(a.values()) == 1
            for z in a: assert a[z] >= 0
            for z in (P,Q): action_flows[h][z] += mp*a[z]
            obs[0] += mp*a[Q]; obs[1] += mq*a[P]
            if n < N:
                action_flows[h][C] += mp*a[C]
                obs[2] += mp*a[C]; obs[3] += mq*a[C]
                for y,w in p[h].items():
                    nx=h+(y,)
                    next_live[nx][0] += mp*a[C]*w
                    next_live[nx][1] += mq*a[C]*q[h][y]
        live = {h:tuple(v) for h,v in next_live.items()}
    return tuple(obs), action_flows

def predictive_counts(p,q,T,N=2):
    levels={0:[()]};mass={(): (R(1),R(1))}
    for n in range(N):
        levels[n+1]=[]
        for h in levels[n]:
            for y,pp in p[h].items():
                z=h+(y,);levels[n+1].append(z)
                mass[z]=(mass[h][0]*pp,mass[h][1]*q[h][y])
    cls={}
    for n in range(N,-1,-1):
        sig={}
        for h in levels[n]:
            LR=mass[h][1]/mass[h][0]
            if n==N:sig[h]=(repr(T(h)),LR)
            else:
                row=defaultdict(R)
                for y,v in p[h].items():row[cls[h+(y,)]]+=v
                sig[h]=(repr(T(h)),LR,tuple(sorted(row.items())))
        names={v:i for i,v in enumerate(sorted(set(sig.values()),key=repr))}
        for h in levels[n]:cls[h]=names[sig[h]]
    return tuple(len({cls[h] for h in levels[n]}) for n in range(N+1))

def positive():
    first={'a':R(1,2),'b':R(1,2)}
    rows={('a',):{'0A':R(1,2),'0B':R(1,10),'1A':R(1,10),'1B':R(3,10)},
          ('b',):{'0A':R(1,5),'0B':R(2,5),'1A':R(1,5),'1B':R(1,5)}}
    p={():first,**rows}; q={():first,**{h:{y:v*(R(4,3) if y[0]=='0' else R(1,2)) for y,v in row.items()} for h,row in rows.items()}}
    for h in p:
        assert sum(p[h].values())==sum(q[h].values())==1
    for h in [('a',),('b',)]:
        assert sum(v for y,v in p[h].items() if y[0]=='0')==R(3,5)
        assert sum(v for y,v in q[h].items() if y[0]=='0')==R(4,5)
    assert p[('a',)]!=p[('b',)]
    T=lambda h:'root' if not h else ('x' if len(h)==1 else h[-1][0])
    terminal={('a','0A'):R(1,3),('a','0B'):R(2,3),('a','1A'):R(1,5),('a','1B'):R(4,5),
              ('b','0A'):R(2,7),('b','0B'):R(3,7),('b','1A'):R(5,7),('b','1B'):R(1,7)}
    def full(h):
        if not h:return {P:R(0),Q:R(0),C:R(1)}
        if len(h)==1:return ({P:R(1,6),Q:R(1,3),C:R(1,2)} if h[0]=='a'
                             else {P:R(1,4),Q:R(1,4),C:R(1,2)})
        v=terminal[h];return {P:v,Q:1-v}
    original,flows=eval_policy(p,q,full)
    mass=defaultdict(R);u=defaultdict(lambda:defaultdict(R))
    for h,row in flows.items():
        n=len(h);k=(n,T(h));s=sum(row.values());mass[k]+=s
        for a,v in row.items():u[k][a]+=v
    beta={k:{a:u[k][a]/mass[k] for a in ([P,Q] if k[0]==2 else [P,Q,C])} for k in mass}
    quotient,_=eval_policy(p,q,lambda h:beta[len(h),T(h)])
    assert original==quotient==(R(341,600),R(10489,25200),R(3,2),R(3,2))
    assert beta[1,'x']=={P:R(5,24),Q:R(7,24),C:R(1,2)}
    assert beta[2,'0'][P]==R(97,252) and beta[2,'1'][P]==R(151,280)
    print('NONIID_POSITIVE_QUOTIENT PASS',original)
    assert predictive_counts(p,q,T)==(1,1,2)
    print('POSITIVE_PREDICTIVE_CLASS_COUNTS (1,1,2)')

def negative():
    first={'a':R(1,2),'b':R(1,2)}
    p={():first,('a',):{'0':R(9,10),'1':R(1,10)},('b',):{'0':R(1,2),'1':R(1,2)}}
    q={():first,('a',):{'0':R(1,10),'1':R(9,10)},('b',):{'0':R(1,2),'1':R(1,2)}}
    def full(h):
        if not h:return {P:R(0),Q:R(0),C:R(1)}
        if h==('a',):return {P:R(0),Q:R(0),C:R(1)}
        if h==('b',):return {P:R(1,2),Q:R(1,2),C:R(0)}
        return {P:R(1) if h[1]=='0' else R(0),Q:R(0) if h[1]=='0' else R(1)}
    v,_=eval_policy(p,q,full)
    assert v==(R(3,10),R(3,10),R(3,2),R(3,2))
    assert p[()]["a"]==q[()]["a"] and p[()]["b"]==q[()]["b"]
    bound=R(1)-R(4,5)*R(3,4)/R(2)
    assert bound==R(7,10)>v[0]+v[1]
    print('NONIID_LR_ONLY_OBSTRUCTION PASS',v,'error_sum_lower_bound',bound)
    T=lambda h:'root' if not h else ('x' if len(h)==1 else h)
    assert predictive_counts(p,q,T)==(1,2,4)
    print('NEGATIVE_PREDICTIVE_CLASS_COUNTS (1,2,4)')
    err=(R(3,4),R(3,4))
    assert sum(err)==R(3,2)!=R(1)
    print('NO_LR_OBSTRUCTION PASS',err)

if __name__=='__main__':
    positive();negative();print('ALL_EXACT_AUTHOR_CHECKS_PASS')
