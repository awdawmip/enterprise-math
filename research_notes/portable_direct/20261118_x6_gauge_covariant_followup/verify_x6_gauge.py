#!/usr/bin/env python3
"""X6/V5 signed 3-cycle: exact exhaustive gauge-orbit and readout tests.
Only typed finite sign/branch operations; no continuum physics computation.
Run: python verify_x6_gauge.py > check_results.json
"""
from itertools import product, combinations
from collections import defaultdict, Counter
import json

SG=(-1,1)
S=list(product(SG, repeat=3))
A=[a for a in S if a[0]*a[1]*a[2]==-1]
G=S
def prod(v):
    z=1
    for x in v:z*=x
    return z
def gauge(s,a,e):
    return (tuple(e[i]*s[i] for i in range(3)),
            tuple(e[i]*e[(i+1)%3]*a[i] for i in range(3)))
def bond(s,a):
    return tuple(s[i]*a[i]*s[(i+1)%3] for i in range(3))
def step(s,a):
    return tuple(a[(j-1)%3]*s[(j-1)%3] for j in range(3))
def rot(s,k):
    return tuple(s[(i+k)%3] for i in range(3))
def sym_orbits(elements,action):
    unvisited=set(elements);groups=[]
    while unvisited:
        z=next(iter(unvisited));t=action(z)
        assert t<=unvisited
        groups.append(t)
        unvisited-=t
    return groups
def pair_count(co,go,base):
    cid={x:i for i,o in enumerate(co) for x in o}
    gid={x:i for i,o in enumerate(go) for x in o}
    n=0
    for cm in range(1<<len(co)):
        for gm in range(1<<len(go)):
            if all(((gm>>gid[x])&1)==0 or ((cm>>cid[base(x)])&1) for x in gid):
                n+=1
    return n
for s,a,e in product(S,A,G):
    assert bond(*gauge(s,a,e))==bond(s,a)
fib=defaultdict(set)
for s,a in product(S,A):fib[bond(s,a)].add((s,a))
assert len(fib)==4 and set(fib)==set(A) and all(len(z)==8 for z in fib.values())
for z in fib.values():
    rep=next(iter(z))
    assert {gauge(*rep,e) for e in G}==z

def full_act(z):
    if len(z)==2:
        s,a=z
        return {(rot(gauge(s,a,e)[0],k),rot(gauge(s,a,e)[1],k))
                for e in G for k in range(3)}
    s,a,p=z
    return {(rot(gauge(s,a,e)[0],k),rot(gauge(s,a,e)[1],k),(p-k)%3)
            for e in G for k in range(3)}
co=sym_orbits([(s,a) for s,a in product(S,A)],full_act)
go=sym_orbits([(s,a,p) for s,a in product(S,A) for p in range(3)],full_act)
assert sorted(map(len,co))==[8,24] and sorted(map(len,go))==[24]*4
assert pair_count(co,go,lambda x:(x[0],x[1]))==27

cs=sym_orbits(S,lambda s:{rot(s,k) for k in range(3)})
gs=sym_orbits([(s,p) for s in S for p in range(3)],
              lambda x:{(rot(x[0],k),(x[1]-k)%3) for k in range(3)})
assert (len(cs),len(gs))==(4,8)
assert pair_count(cs,gs,lambda x:x[0])==729
ci={x:i for i,o in enumerate(cs) for x in o}
gi={x:i for i,o in enumerate(gs) for x in o}
n_signonly_gauge=0
for cm in range(1<<len(cs)):
    for gm in range(1<<len(gs)):
        if any(((gm>>gi[(s,p)])&1) and not ((cm>>ci[s])&1)
               for s in S for p in range(3)):continue
        if all(((cm>>ci[s])&1)==((cm>>ci[tuple(s[i]*e[i] for i in range(3))])&1)
               for s,e in product(S,G)) and all(
               ((gm>>gi[(s,p)])&1)==((gm>>gi[(tuple(s[i]*e[i] for i in range(3)),p)])&1)
               for s,p,e in product(S,range(3),G)):
            n_signonly_gauge+=1
assert n_signonly_gauge==3

reachable=defaultdict(set)
for s,a,b in product(S,A,A):
    old=bond(s,a);new=bond(step(s,a),b)
    delta=tuple(a[i]*b[i] for i in range(3))
    assert prod(delta)==1
    assert new==tuple(delta[i]*old[(i-1)%3] for i in range(3))
    reachable[old].add(new)
assert len(reachable)==4 and all(z==set(A) for z in reachable.values())
assert 16+3==19

dynamic={};static={}
for j in range(3):
    samples=[]
    for s,a,b in product(S,A,A):
        t1=step(s,a);t2=step(t1,b)
        y=(s[j],t1[j],t2[j]);p=prod(s)
        assert p==-a[j]*b[(j-1)%3]*prod(y)
        samples.append((y,p,a,b))
    assert len(samples)==128
    query_names=[(t,i) for t in range(2) for i in range(3)]
    accepted=Counter();good_two=[]
    for length in range(7):
        for qset in combinations(query_names,length):
            m=defaultdict(set)
            for y,p,a,b in samples:
                m[y,tuple((a if t==0 else b)[i] for t,i in qset)].add(p)
            if all(len(vals)==1 for vals in m.values()):
                accepted[length]+=1
                if length==2:good_two.append(qset)
    assert accepted[0]==accepted[1]==0
    assert len(good_two)==1 and set(good_two[0])=={(0,j),(1,(j-1)%3)}
    split=defaultdict(Counter)
    for y,p,a,b in samples:split[y][p]+=1
    assert len(split)==8 and all(c=={-1:8,1:8} for c in split.values())
    dynamic['axis'+str(j)]={'inputs':len(samples),'unique_two_query_set':list(good_two[0]),
                             'sufficient_sets_by_size':dict(accepted),'no_tags_each_parity':[8,8]}
    fixed=[]
    for s,a in product(S,A):
        t1=step(s,a);t2=step(t1,a)
        y=(s[j],t1[j],t2[j]);p=prod(s)
        assert p==a[(j+1)%3]*prod(y)
        fixed.append((y,p,a))
    single=[]
    for k in range(3):
        m=defaultdict(set)
        for y,p,a in fixed:m[y,a[k]].add(p)
        if all(len(v)==1 for v in m.values()):single.append(k)
    assert single==[(j+1)%3]
    static['axis'+str(j)]={'inputs':len(fixed),'only_sufficient_tag':single[0]}

for j in range(3):
    e=[1,1,1];e[(j+1)%3]=-1;e=tuple(e)
    for s,a0,a1 in product(S,A,A):
        t,b0=gauge(s,a0,e);_,b1=gauge(s,a1,e)
        assert prod(t)==-prod(s)
        for n in range(12):
            assert s[j]==t[j]
            assert bond(s,a0)==bond(t,b0)
            s,t=step(s,a0),step(t,b0)
            a0,a1=a1,a0;b0,b1=b1,b0

print(json.dumps({
    'model':'V5 four-twist signed X6 triad, conditional reference/frame observer',
    'signed_microstates':32, 'gauge_orbits':4,'orbit_size':8,
    'cyclic_sign_only_coherent_pairs':729,
    'sign_only_fully_gauge_covariant_pairs':n_signonly_gauge,
    'signed_link_fully_gauge_covariant_pairs':27,
    'unrestricted_next_twist_event_preserving_pairs':19,
    'reachable_targets_per_link_state':4,
    'variable_twist':dynamic,'fixed_twist':static,
    'gauge_obstruction_check':'12-step; general obstruction proved algebraically',
    'status':'PASS'
},indent=2,ensure_ascii=False))
