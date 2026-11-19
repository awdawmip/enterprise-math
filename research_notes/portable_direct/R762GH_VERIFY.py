#!/usr/bin/env python3
"""R762GH exact full-state finite certificate: integer arithmetic, standard library only."""
import json
from collections import defaultdict, Counter
from itertools import permutations, product

STARS=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
IDENT=tuple(range(6))
EVENTS=tuple((j,s) for j in range(4) for s in (1,-1))

def rotation(j,s):
    a,b,c=STARS[j]; p=list(IDENT)
    if s==1: p[a],p[b],p[c]=b,c,a
    else: p[a],p[b],p[c]=c,a,b
    return tuple(p)

def compose(p,q):
    return tuple(p[q[i]] for i in range(6))

def evaluate(word):
    n=[0]*4; g=IDENT
    for j,s in word:
        n[j]+=s
        g=compose(rotation(j,s),g)
    return tuple(n),g

def cycle_type(p):
    seen=set(); lens=[]
    for i in range(6):
        if i not in seen:
            k=i; length=0
            while k not in seen:
                seen.add(k);length+=1;k=p[k]
            lens.append(length)
    return ''.join(str(x) for x in sorted(lens,reverse=True))

def full_dp(max_length=8):
    dp={(0,0,0,0,IDENT):1}; out=[]
    for m in range(max_length+1):
        returns=defaultdict(lambda:[0,0])
        for (*n,g),value in dp.items():
            if len(set(n))==1:
                returns[n[0]][1]+=value
                if g==IDENT:returns[n[0]][0]+=value
        assert sum(dp.values())==8**m
        out.append({'m':m,'states':len(dp),'returns':{
            str(a):{'joint_identity':hit,'relative_only':allcount}
            for a,(hit,allcount) in sorted(returns.items())}})
        if m==max_length:break
        nxt=defaultdict(int)
        for (*n,g),v in dp.items():
            for j,s in EVENTS:
                nn=list(n);nn[j]+=s
                nxt[(*nn,compose(rotation(j,s),g))]+=v
        dp=nxt
    return out

def invert(p):
    q=[0]*6
    for i,j in enumerate(p):q[j]=i
    return tuple(q)

def find_eight_step_witness(a):
    halves={}
    for word in product(EVENTS,repeat=4):
        halves.setdefault(evaluate(word),word)
    for (n,g),front in halves.items():
        need=tuple(a-n[i] for i in range(4))
        back=halves.get((need,invert(g)))
        if back is not None:
            result=front+back
            assert evaluate(result)==((a,)*4,IDENT)
            return [[j,s] for j,s in result]
    raise AssertionError('missing witness')

def monotone_positive_count(a):
    dp={(0,0,0,0,IDENT):1}
    for step in range(4*a):
        nxt=defaultdict(int)
        for (*n,g),value in dp.items():
            for j in range(4):
                if n[j]<a:
                    nn=list(n);nn[j]+=1
                    nxt[(*nn,compose(rotation(j,1),g))]+=value
        dp=nxt
    return dp.get((a,a,a,a,IDENT),0)

def main():
    assert all(compose(rotation(j,1),rotation(j,-1))==IDENT for j in range(4))
    cycle_types=Counter()
    for order in permutations(range(4)):
        n,g=evaluate([(j,1) for j in order])
        assert n==(1,)*4
        cycle_types[cycle_type(g)]+=1
    assert dict(cycle_types)=={'42':16,'33':4,'51':4}
    rows=full_dp()
    def v(m,a,typ):return rows[m]['returns'][str(a)][typ]
    for m,expected in [(4,{0:(120,168),1:(0,24)}),
                       (6,{0:(2192,5120),1:(0,1440)}),
                       (8,{0:(44632,190120),1:(16,73920),2:(8,2520)})]:
        for a,(both,rel) in expected.items():
            assert (v(m,a,'joint_identity'),v(m,a,'relative_only'))==(both,rel)
            if a:assert v(m,-a,'joint_identity')==both
    w1=find_eight_step_witness(1);w2=find_eight_step_witness(2)
    pcounts=[monotone_positive_count(a) for a in (1,2,3)]
    assert pcounts==[0,8,2116],pcounts
    assert evaluate([(j,1) for j in range(4) for _ in range(3)])==((3,)*4,IDENT)
    result={
      'model':'CANDIDATE_SIGNED_K4_STAR_DIRECT_PRODUCT_LIFT',
      'stars':[list(s) for s in STARS],
      'orientation':'positive 3-cycle in given STAR order, negative its inverse; left-composed',
      'depth_change':'2a iff signed counts n0=n1=n2=n3=a',
      'four_plus_cycle_type_counts':dict(sorted(cycle_types.items())),
      'full_dp_exact_m_0_to_8':rows,
      'length8_witness_a1':w1,'length8_witness_a2':w2,
      'positive_only_identity_counts_a1_a2_a3':pcounts,
      'L(a)':'8 if abs(a)=1 else 4*abs(a) for abs(a)>=2',
      'author_verification':'PASS','independent_review':'NOT_REVIEWED'}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
