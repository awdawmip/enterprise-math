#!/usr/bin/env python3
"""Stage292-B: exact rational BRC finite-label sufficiency and three-fiber witness.
Standard library Fraction only; independent recomputation of all enumerated probabilities.
This code checks finite stated instances; the universal coupling theorem is in the proof.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

T = (F(1,64), F(1,32), F(31,32), F(63,64))
W_PLUS = tuple(F(x,256) for x in (4,126,2,124))
W_MINUS = tuple(F(x,256) for x in (124,2,126,4))
ONE = F(1)
B0, B1 = F(1,4), F(3,4)


def w2(t):
    assert F(0) < t < ONE
    return {'0': ONE-t, '10': t*(ONE-t), '11': t*t}


def tv(p, q):
    return sum((abs(p.get(k,F(0))-q.get(k,F(0))) for k in p.keys()|q.keys()), F(0)) / 2


def qbit(t):
    return int(t == T[0])


def root(t):
    return 0 if t <= F(1,2) else 1


def enum(weights, stages=3, baseline=False, include_state=False):
    """B and C kernels; A is Bernoulli stop words. Original hidden t only for generation.
    If include_state, observation includes (root,q) with their explicit types.
    """
    assert stages in (1,2,3)
    dist=defaultdict(F)
    for t,w in zip(T, weights):
        z, qb = root(t), qbit(t)
        pa = w2(t)
        for aw,paw in pa.items():
            if stages == 1:
                key=((z,qb,aw) if include_state else (aw,))
                dist[key]+=w*paw
                continue
            b = B0 if baseline else (B1 if qb else B0)
            for bw,pbw in w2(b).items():
                if stages == 2:
                    key=((z,qb,aw,bw) if include_state else (aw,bw))
                    dist[key]+=w*paw*pbw
                    continue
                c=B0 if baseline else (B1 if (qb and bw == '10') else B0)
                for cw,pcw in w2(c).items():
                    key=((z,qb,aw,bw,cw) if include_state else (aw,bw,cw))
                    dist[key]+=w*paw*pbw*pcw
    assert sum(dist.values())==ONE
    assert len(dist)=={1:3,2:9,3:27}[stages]*(1 if not include_state else 3)
    assert all(m>0 for m in dist.values())
    return dict(dist)


def check_source(name, weights):
    p=enum(weights,stages=3)
    approximate=enum(weights,stages=3,baseline=True)
    p2=enum(weights,stages=2)
    approx2=enum(weights,stages=2,baseline=True)
    t1_mass=weights[0]
    eb=t1_mass*tv(w2(B1),w2(B0))
    # In true B, word '10' has probability b*(1-b)=3/16 for b=3/4.
    ec=t1_mass*w2(B1)['10']*tv(w2(B1),w2(B0))
    assert eb==t1_mass/F(2)
    assert ec==t1_mass*F(3,32)
    assert tv(p2,approx2)==eb
    assert tv(p,approximate)==eb+ec==t1_mass*F(19,32)
    assert len(p)==27 and len(approximate)==27
    # The stronger root- and partition-tagged observation also has full support.
    tagged=enum(weights,stages=3,include_state=True)
    assert len(tagged)==81
    return eb,ec,tv(p,approximate)


def minimal_k3_labels():
    # For each past history h_ab, h_bc, h_ac the two reachable ports have
    # distinct conditional B stop-word laws W2(1/4), W2(3/4).
    T3=(0,1,2)
    histories={(0,1):(B0,B1),(1,2):(B0,B1),(0,2):(B0,B1)}
    edges=set()
    for nodes,params in histories.items():
        assert all(x>0 for x in w2(params[0]).values())
        assert all(x>0 for x in w2(params[1]).values())
        if w2(params[0])!=w2(params[1]): edges.add(frozenset(nodes))
    assert len(edges)==3
    sizes=[]
    for k in (1,2,3):
        valid=0
        for labels in product(range(k),repeat=3):
            if all(labels[tuple(e)[0]]!=labels[tuple(e)[1]] for e in edges):
                valid+=1
        sizes.append((k,valid))
    assert sizes==[(1,0),(2,0),(3,6)]
    return sizes


def main():
    assert all(w>0 for w in (*W_PLUS,*W_MINUS))
    assert sum(W_PLUS)==sum(W_MINUS)==ONE
    moments=[]
    for j in range(3):
        pp=sum((w*t**j for w,t in zip(W_PLUS,T)),F(0))
        mm=sum((w*t**j for w,t in zip(W_MINUS,T)),F(0))
        assert pp==mm
        moments.append(pp)
    assert moments==[ONE,F(1,2),F(3909,8192)]
    assert qbit(T[0]) and not any(qbit(t) for t in T[1:])
    assert root(T[0])==root(T[1])==0 and root(T[2])==root(T[3])==1
    assert w2(B0)!=w2(B1)
    vplus=check_source('plus',W_PLUS)
    vminus=check_source('minus',W_MINUS)
    assert vplus==(F(1,128),F(3,2048),F(19,2048))
    assert vminus==(F(31,128),F(93,2048),F(589,2048))
    assert tv(enum(W_PLUS,1),enum(W_MINUS,1))==0
    assert tv(enum(W_PLUS,2),enum(W_MINUS,2))==F(15,64)
    assert tv(enum(W_PLUS,3),enum(W_MINUS,3))==F(285,1024)
    assert enum(W_PLUS,2,baseline=True)==enum(W_MINUS,2,baseline=True)
    assert enum(W_PLUS,3,baseline=True)==enum(W_MINUS,3,baseline=True)
    assert tv(enum(W_PLUS,3),enum(W_MINUS,3)) < vplus[2]+vminus[2]
    assert minimal_k3_labels()==[(1,0),(2,0),(3,6)]
    print('stage292b: exact two-moment equality:', ', '.join(map(str,moments)))
    print('stage292b: pooled A TV=0; pooled A/B TV=15/64; pooled A/B/C TV=285/1024')
    print('stage292b: + policy B,C residuals:',*[str(x) for x in vplus])
    print('stage292b: - policy B,C residuals:',*[str(x) for x in vminus])
    print('stage292b: per-policy 3-stage error equals arrival-weighted sum of B and C kernel TV')
    print('stage292b: positive leaves each policy: 3 A; 9 A/B; 27 A/B/C; tagged 81')
    print('stage292b: three-history conflict K3 proper-color counts:',minimal_k3_labels())
    print('STAGE292B_MINIMAL_LABEL_THREE_FIBER_EXACT_PASS')

if __name__=='__main__':
    main()
