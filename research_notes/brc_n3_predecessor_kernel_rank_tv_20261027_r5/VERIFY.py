#!/usr/bin/env python3
"""Exact rational N=3 observer-kernel rank/mixture certificate (external BRC carrier)."""
from fractions import Fraction as F
ONE=F(1)
T={
    '': {'a': (F(1,3),F(2,3)), 'b': (F(2,3),F(1,3))},
    'a': {'ax': (F(1,2),F(1,4)), 'ay': (F(1,2),F(3,4))},
    'b': {'bx': (F(2,3),F(1,3)), 'by': (F(1,3),F(2,3))},
}
K_a={F(1,2):F(1,4), F(1):F(1,2), F(3,2):F(1,4)}
K_b={F(1,2):F(1,3), F(1):F(1,3), F(3,2):F(1,3)}
for h,k in [('ax',K_a),('by',K_b)]:
    T[h]={f'{h}:{y}':(q,q*y) for y,q in k.items()}
for h in ['ay','bx']:
    T[h]={f'{h}:u':(F(1,2),F(1,2)), f'{h}:v':(F(1,2),F(1,2))}
Q={'':ONE};P={'':ONE}; depth={'':0}; LR={'':ONE}
for t in range(3):
    for h in [h for h in list(depth) if depth[h]==t]:
        assert sum(q for q,p in T[h].values())==1
        assert sum(p for q,p in T[h].values())==1
        for ch,(q,p) in T[h].items():
            assert q>0 and p>0
            Q[ch]=Q[h]*q;P[ch]=P[h]*p;depth[ch]=t+1;LR[ch]=P[ch]/Q[ch]
assert sum(Q[h] for h in depth if depth[h]==3)==1
assert sum(P[h] for h in depth if depth[h]==3)==1
assert [LR[h] for h in ['a','b','ax','ay','bx','by']]==[2,F(1,2),1,3,F(1,4),1]
def eval_policy(continues, terminal_Q):
    reachQ={'':ONE}; reachP={'':ONE}
    eP=eQ=tP=tQ=F(0)
    for t in range(4):
        for h in [h for h in depth if depth[h]==t]:
            a,b=reachQ.get(h,0),reachP.get(h,0)
            if t==3:
                d=terminal_Q.get(h,F(0));assert 0<=d<=1
                eP+=b*d;eQ+=a*(1-d)
                continue
            c,d=continues.get(h,(F(0),F(0)))
            assert 0<=c<=1 and 0<=d<=1-c
            eP+=b*d;eQ+=a*(1-c-d)
            tP+=b*c;tQ+=a*c
            for ch,(q,p) in T[h].items():
                reachQ[ch]=a*c*q;reachP[ch]=b*c*p
    return (eP,eQ,tP,tQ)
pa={'':(ONE,0),'a':(ONE,0),'b':(F(0),0),'ax':(ONE,0),'ay':(F(0),0)}
qa={h:(ONE if h.startswith('ax:') and LR[h] in (F(1,2), F(3,2)) else F(0)) for h in depth if depth[h]==3}
pb={'':(ONE,0),'a':(F(0),0),'b':(F(3,4),0)};qb={}
pc={'':(ONE,0),'a':(F(1,2),0),'b':(F(3,8),0),'ax':(F(1,2),0),'by':(F(1,2),0),'ay':(F(0),0),'bx':(F(0),0)}
qc={h:(ONE if LR[h] in (F(1,2),F(3,2)) else F(0)) for h in depth if depth[h]==3}
A=eval_policy(pa,qa); B=eval_policy(pb,qb); C=eval_policy(pc,qc)
mean=tuple((a+b)/2 for a,b in zip(A,B))
diff=tuple(c-m for c,m in zip(C,mean))
assert A==(F(1,12),F(11,12),F(11,6),F(3,2))
assert B==(F(0),F(1),F(5,4),F(3,2))
assert mean==(F(1,24),F(23,24),F(37,24),F(3,2))
assert C==(F(7,144),F(137,144),F(37,24),F(3,2))
assert diff==(F(1,144),F(-1,144),F(0),F(0))
TV=lambda k,m:sum(abs(k.get(y,0)-m.get(y,0)) for y in set(k)|set(m))/2
etaA=Q['ax'];etaB=Q['by'];delta=TV(K_a,K_b)
assert (etaA,etaB)==(F(1,6),F(2,9))
assert delta==F(1,6)
minor=etaA*(etaB*K_b[F(1,2)])-etaB*(etaA*K_a[F(1,2)])
assert minor==F(1,324)
arrival_r=F(1,6);tv_bound=arrival_r*delta/4
assert tv_bound==F(1,144)
yset=sorted(set(K_a)|set(K_b))
target={y:F(1,12)*K_a[y] for y in yset}
actual={y:F(1,24)*(K_a[y]+K_b[y]) for y in yset}
leak_tv=sum(abs(actual[y]-target[y]) for y in yset)/2
assert leak_tv==tv_bound==F(1,144)
assert sum(actual.values())==sum(target.values())==F(1,12)
assert all(LR[h]==F(1) for h in ['ax','by'])
assert all(LR[h]==LR[j] for h,j in [('ax:1/2','by:1/2'),('ax:1','by:1'),('ax:3/2','by:3/2')])
print('MODEL: 10 positive leaves; Q/P normalization PASS; exact LR transport PASS')
print('ROOT_AND_COLLISION:', 'L1=(2,1/2)', 'L2=(1,3,1/4,1)')
print('ETA:',etaA,etaB,'RANK_MINOR:',minor,'TV_DIAMETER:',delta)
print('A:',A)
print('B:',B)
print('MEAN:',mean)
print('FLOW_AVERAGED_SEEDLESS:',C)
print('VECTOR_DIFFERENCE:',diff)
print('TERMINAL_Q_ARRIVAL_TARGET:',target)
print('TERMINAL_Q_ARRIVAL_ACTUAL:',actual)
print('TERMINAL_TV_LEAK:',leak_tv,'BOUND:',tv_bound)
print('EXACT_CERTIFICATE_PASS')
