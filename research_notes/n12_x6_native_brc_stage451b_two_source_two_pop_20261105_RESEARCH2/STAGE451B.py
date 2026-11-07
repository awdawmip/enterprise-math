#!/usr/bin/env python3
"""Stage451-B verifier: exact integer grouped DP and full 12-direction futures."""
from collections import defaultdict
from itertools import combinations
import json
A,B=0,1
D=tuple(range(12))
def words(n,k):
    for ix in combinations(range(1,n-1),k):
        if all(b-a>1 for a,b in zip(ix,ix[1:])):
            w=[A]*n
            for j in ix:w[j]=B
            yield tuple(w)
def mismatch(p,q):return sum(a!=b for a,b in zip(p,q))
def fiber(m,n,kp,kq,d):
    return [(p,q) for p in words(m,kp) for q in words(n,kq) if mismatch(p,q)==d]
def repair(p,q,r):
    m,n=len(p),len(q);h=min(n-1,m+r)
    return (p[m-3],p[m-2],q[n-3],q[n-2],*q[m-2:h])
def prefix_transfer(m,kp,kq,d):
    T=defaultdict(int)
    for a in ((A,) if m==3 else (A,B)):
     for b in (A,B):
      for c in (A,B):
       for e in (A,B):
        dp={(0,0,0,A,A):1}
        for i in range(2,m+1):
            nxt=defaultdict(int)
            ps=(A,) if i==m else (a,) if i==m-2 else (b,) if i==m-1 else (A,B)
            qs=(c,) if i==m-1 else (e,) if i==m else (A,B)
            for (x,y,z,prevp,prevq),v in dp.items():
                for pp in ps:
                    if pp==B and prevp==B:continue
                    xp=x+(pp==B)
                    if xp>kp:continue
                    for qq in qs:
                        if qq==B and prevq==B:continue
                        yq=y+(qq==B);zz=z+(pp!=qq)
                        if yq<=kq and zz<=d:nxt[xp,yq,zz,pp,qq]+=v
            dp=nxt
        for (x,y,z,prevp,prevq),v in dp.items():
            if x==kp and z==d:T[a,b,c,e,y]+=v
    return T
def window_transfer(m,n,r,kq):
    h=min(n-1,m+r);W=defaultdict(int)
    for c in (A,B):
     for e in (A,B):
      for u in (A,B):
       for v in (A,B):
        dp={(0,A):1}
        for i in range(m-1,h+1):
            xs=[c] if i==m-1 else [e] if i==m else [A,B]
            if i==n-2:xs=[x for x in xs if x==u]
            if i==n-1:xs=[x for x in xs if x==v]
            nxt=defaultdict(int)
            for (s,last),cnt in dp.items():
                for x in xs:
                    if x==B and last==B:continue
                    if s+(x==B)<=kq:nxt[s+(x==B),x]+=cnt
            dp=nxt
        for (s,t),cnt in dp.items():W[c,e,s,t,u,v]+=cnt
    return W
def suffix_transfer(h,n,kq):
    S=defaultdict(int)
    for t in (A,B):
     for u in (A,B):
      for v in (A,B):
        dp={(0,t):1}
        for i in range(h+1,n+1):
            xs=[A] if i==n else [A,B]
            if i==n-2:xs=[x for x in xs if x==u]
            if i==n-1:xs=[x for x in xs if x==v]
            nxt=defaultdict(int)
            for (s,last),cnt in dp.items():
                for x in xs:
                    if x==B and last==B:continue
                    if s+(x==B)<=kq:nxt[s+(x==B),x]+=cnt
            dp=nxt
        for (s,last),cnt in dp.items():S[t,u,v,s]+=cnt
    return S
def grouped(m,n,kp,kq,d,r):
    assert 3<=m<n
    h=min(n-1,m+r)
    T=prefix_transfer(m,kp,kq,d)
    W=window_transfer(m,n,r,kq)
    S=suffix_transfer(h,n,kq)
    groups={};classes=population=0
    for (c,e,s,t,u,v),wc in W.items():
     for a in (A,B):
      for b in (A,B):
        pop=0
        for j in range(kq+1):
            k=kq-j-(s-(c==B)-(e==B))
            if k>=0:pop+=T.get((a,b,c,e,j),0)*S.get((t,u,v,k),0)
        if pop:
            classes+=wc;population+=wc*pop
            groups[a,b,c,e,s,t,u,v]=(wc,pop)
    return {'qF':classes,'population':population,'groups':groups,'h':h,'window_descriptors':len(W)}
def obs(p,q):
    def vect(w):
        v=[0]*6;J=[0]*144
        for x in w:v[x//2]+=1 if x%2==0 else -1
        for x,y in zip(w,w[1:]):J[12*x+y]+=1
        return tuple(v),tuple(J)
    return (len(p),len(q),*vect(p),*vect(q),mismatch(p,q))
def full_futures(histories,pp=2,qp=2,rp=1,rq=0):
    memo={};ids={}
    def visit(p,q,pp,qp,rp,rq):
        key=(p,q,pp,qp,rp,rq)
        if key in memo:return memo[key]
        children=[]
        if pp and len(p)>1:children.append(('P:POP',visit(p[:-1],q,pp-1,qp,rp,rq)))
        if qp and len(q)>1:children.append(('Q:POP',visit(p,q[:-1],pp,qp-1,rp,rq)))
        if rp:
            for x in D:children.append((('P:APPEND',x),visit(p+(x,),q,pp,qp,rp-1,rq)))
        if rq:
            for x in D:children.append((('Q:APPEND',x),visit(p,q+(x,),pp,qp,rp,rq-1)))
        val=(obs(p,q),tuple(children))
        if val not in ids:ids[val]=len(ids)
        memo[key]=ids[val]
        return memo[key]
    part=defaultdict(list)
    for p,q in histories:part[visit(p,q,pp,qp,rp,rq)].append((p,q))
    return part,len(memo)
def check(m,n,kp,kq,d,r,rq=0,full=False):
    raw=fiber(m,n,kp,kq,d)
    direct=defaultdict(list)
    for p,q in raw:direct[repair(p,q,r)].append((p,q))
    G=grouped(m,n,kp,kq,d,r)
    assert len(direct)==G['qF'] and len(raw)==G['population']
    for key,v in direct.items():
        a,b,u,z,*W=key
        g=(a,b,W[0],W[1],sum(x==B for x in W),W[-1],u,z)
        assert G['groups'][g][1]==len(v)
    states=0
    if full and raw:
        fut,states=full_futures(raw,2,2,r,rq)
        assert len(fut)==len(direct)
        class_of={h:key for key,v in direct.items() for h in v}
        for vs in fut.values():assert len({class_of[h] for h in vs})==1
        sig_of={h:s for s,vs in fut.items() for h in vs}
        for vs in direct.values():assert len({sig_of[h] for h in vs})==1
    return len(raw),len(direct),states
def run():
    tests=[];future_states=0
    cases=[(4,5,1,1,0,0),(5,6,1,1,1,0),(6,7,1,2,1,0),
           (5,7,1,1,1,0),(5,8,1,2,1,0),(5,6,1,1,0,1),
           (5,6,1,1,1,1),(5,7,1,1,1,1)]
    for m,n,kp,kq,r,rq in cases:
        for d in range(kp+kq+1):
            if not fiber(m,n,kp,kq,d):continue
            raw,qf,states=check(m,n,kp,kq,d,r,rq,full=True)
            tests.append([m,n,kp,kq,d,r,rq,raw,qf,states]);future_states+=states
    checks=raw_total=0
    for m in range(3,10):
     for n in range(m+1,min(m+5,13)):
      for kp in range(min(3,(m-1)//2)+1):
       for kq in range(min(3,(n-1)//2)+1):
        for r in range(min(4,n-m+1)):
         for d in range(min(kp+kq,m)+1):
            raw,qf,_=check(m,n,kp,kq,d,r)
            checks+=1;raw_total+=raw
    G=grouped(64,80,15,17,1,12)
    return {'status':'STAGE451B_TWO_SOURCE_TWO_POP_GROUPED_DP_PASS',
            'full_case_count':len(tests),'future_state_total':future_states,
            'grouped_parameter_checks':checks,'direct_raw_history_total':raw_total,
            'full_cases':tests,
            'large':{'qF':G['qF'],'population':G['population'],
                     'group_count':len(G['groups']),'window_descriptor_count':G['window_descriptors'],'h':G['h']}}
if __name__=='__main__':print(json.dumps(run(),indent=2))
