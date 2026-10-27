#!/usr/bin/env python3
"""Exact Fraction certificate for N4 single-collision TV minimax, external two-law tree."""
import json
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

N = {1: {'A':(F(1,2),F(1,2),None), 'B':(F(1,2),F(3,2),None)},
     2: {'AU':(F(1,6),F(1),'A'), 'AV':(F(1,3),F(1,4),'A'),
         'BU':(F(1,4),F(1),'B'), 'BV':(F(1,4),F(2),'B')}}
N[3] = {}
for parent,(q,r,_) in N[2].items():
    eps = {'AU':F(1,10),'AV':F(0),'BU':F(4,5),'BV':F(0)}[parent]
    for i,s in enumerate((-1,1)):
        N[3][parent+str(i)] = (q/2,r*(1+s*eps),parent)
N[4] = {}
for parent,(q,r,_) in N[3].items():
    eta = F(0) if parent=='AV0' else F(3,50) if parent=='AV1' else F(1,20)
    for i,s in enumerate((-1,1)):
        N[4][parent+str(i)] = (q/2,r*(1+s*eta),parent)
for t in N:
    assert len(N[t]) == 2**t
    assert all(q>0 and r>0 for q,r,_ in N[t].values())
    assert sum(q for q,r,_ in N[t].values()) == 1
    assert sum(q*r for q,r,_ in N[t].values()) == 1
    if t<4:
        for h,(q,r,_) in N[t].items():
            children=[(cq,cr) for cq,cr,pa in N[t+1].values() if pa==h]
            assert len(children)==2 and sum(cq for cq,cr in children)==q
            assert sum(cq*cr for cq,cr in children)==q*r
assert N[2]['AU'][1] == N[2]['BU'][1] == 1
assert N[3]['AV0'][1] == N[3]['AV1'][1] == F(1,4)
P,Q,C = (F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))

def full(t,h,r):
    if t==1:return C
    if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[h]
    if t==3:return {'AV0':Q,'AV1':C,'BU0':Q,'BU1':P}.get(h,P)
    return Q if 100*r<F(2501,100) else P

def joint(t,h,r):
    if t==1:return C
    if t==2:return {F(1):(F(2,5),F(0),F(3,5)),F(1,4):C,F(2):P}[r]
    if t==3:return {F(9,10):(F(7,19),F(0),F(12,19)),F(11,10):P,
       F(1,4):(F(0),F(13,20),F(7,20)),F(1,5):Q,F(9,5):P,F(2):P}[r]
    return {F(171,200):P,F(189,200):Q,F(1,4):Q,
            F(47,200):P,F(53,200):P}.get(r,P)

def single3(t,h,r):
    if t==1:return C
    if t==2:return {'AU':P,'AV':C,'BU':C,'BV':P}[h]
    if t==3:
        if h in ('AV0','AV1'):return (F(0),F(1,2),F(1,2))
        return Q if h=='BU0' else P
    if h in ('AV00','AV01'):return (F(253,500),F(247,500),F(0))
    if h=='AV10':return Q
    return P

def outcome(policy):
    out=[F(0)]*16
    for leaf,(q,r4,_) in N[4].items():
        alive=F(1)
        for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
            a=policy(t,h,N[t][h][1]);assert all(v>=0 for v in a) and sum(a)==1
            for d in (0,1):
                out[2*(t-1)+d]+=q*alive*a[d]
                out[8+2*(t-1)+d]+=q*r4*alive*a[d]
            alive*=a[2]
        assert alive==0
    assert sum(out[:8])==sum(out[8:])==1
    return tuple(out)

def tv(u,v,start):
    return sum(abs(u[i]-v[i]) for i in range(start,start+8))/2

def score(vec,W):return sum(vec[i]*W[i] for i in range(16))

def bellman(W,mode):
    def c(t,r,d):return W[2*(t-1)+d]+r*W[8+2*(t-1)+d]
    stage3={}
    for h,(q,r,_) in N[3].items():
        continuation=sum(cq/q*min(c(4,r4,0),c(4,r4,1))
                         for k,(cq,r4,parent) in N[4].items() if parent==h)
        stage3[h]=(c(3,r,0),c(3,r,1),continuation)
    key2=lambda h: 'U' if mode=='2' and h in ('AU','BU') else h
    key3=lambda h: ('AVx' if h in ('AV0','AV1') else 'BVx' if h in ('BV0','BV1') else h) if mode=='3' else h
    keys2=sorted(set(key2(h) for h in N[2]))
    rows={}; total_cases=0
    for r1 in product(range(3),repeat=2):
        first=dict(zip(('A','B'),r1));best=None
        for r2 in product(range(3),repeat=len(keys2)):
            total_cases+=1;second=dict(zip(keys2,r2)); val=F(0);groups=defaultdict(list)
            for h,(q,r,_) in N[1].items():
                if first[h]!=2:val+=q*c(1,r,first[h])
            for h,(q,r,parent) in N[2].items():
                if first[parent]!=2:continue
                d=second[key2(h)]
                if d!=2:val+=q*c(2,r,d)
                else:
                    for k,(cq,cr,pa) in N[3].items():
                        if pa==h:groups[key3(k)].append(k)
            for names in groups.values():
                val+=min(sum(N[3][h][0]*stage3[h][d] for h in names) for d in range(3))
            if best is None or val<best:best=val
        rows[''.join('PQC'[d] for d in r1)]=best
    assert total_cases==(243 if mode=='2' else 729)
    return min(rows.values()),rows,total_cases

Fv,D2,D3=outcome(full),outcome(joint),outcome(single3)
assert tv(Fv,D2,0)==tv(Fv,D2,8)==F(7,380)
assert tv(Fv,D3,0)==tv(Fv,D3,8)==F(1,2000)
for t,pi,which in ((2,joint,('AU','BU')),(3,single3,('AV0','AV1'))):
    assert pi(t,which[0],N[t][which[0]][1]) == pi(t,which[1],N[t][which[1]][1])
W2=tuple(F(x) for x in (0,0,3,45,45,-45,-45,-45,0,0,-29,50,-50,50,50,50))
W3=(F(1,10),F(1,10),F(1,10),F(1,10),F(1,10),-F(11,125),F(1,10),-F(1,10),
    F(2,5),F(2,5),-F(2,5),F(2,5),-F(2,5),F(17,50),-F(2,5),F(2,5))
low2,rows2,cases2=bellman(W2,'2')
low3,rows3,cases3=bellman(W3,'3')
assert score(Fv,W2)==-F(467,12) and low2==-F(425,12)
assert score(Fv,W3)==-F(613,2000) and low3==-F(153,500)
osc2=(max(W2[:8])-min(W2[:8]))+(max(W2[8:])-min(W2[8:]))
osc3=(max(W3[:8])-min(W3[:8]))+(max(W3[8:])-min(W3[8:]))
assert osc2==190 and osc3==1
assert (low2-score(Fv,W2))/osc2==F(7,380)
assert (low3-score(Fv,W3))/osc3==F(1,2000)
assert F(7,380)+F(1,2000)-F(7,380)==F(1,2000)>0
fmt=lambda v: str(v)
result={
 'status':'PASS_EXACT_FRACTION_N4_SINGLE_COLLISION_TV',
 'source_model':'N4 two-law ordered history tree, prior author-side model, frozen 2026-10-28',
 'cases':{'t2_only':cases2,'t3_only':cases3},
 'observation_order':'Q-law then P-law; t=1..4 each STOP P, STOP Q',
 'F':[fmt(v) for v in Fv], 'sigma_t2':[fmt(v) for v in D2],
 'sigma_t3':[fmt(v) for v in D3],
 'exact_values':{'d2':fmt(F(7,380)),'d3':fmt(F(1,2000)),
   'd23_from_prior_proof':fmt(F(7,380)),'strict_subadditivity_gap':fmt(F(1,2000))},
 'dual2':{'weights':[fmt(x) for x in W2],'F':fmt(score(Fv,W2)),'global_min':fmt(low2),
    'oscillation_sum':fmt(osc2),'root_table':{k:fmt(v) for k,v in sorted(rows2.items())}},
 'dual3':{'weights':[fmt(x) for x in W3],'F':fmt(score(Fv,W3)),'global_min':fmt(low3),
    'oscillation_sum':fmt(osc3),'root_table':{k:fmt(v) for k,v in sorted(rows3.items())}}
}
print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))
