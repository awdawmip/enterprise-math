#!/usr/bin/env python3
"""Stage453-B: exact finite verification of arbitrary-budget key and BRC population."""
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache
import json

A, B = 0, 1  # +E_1, -E_1; 2..11 are the remaining signed native axes.
DIRECTIONS = tuple(range(12))

def words(length, defects):
    if length < 2:
        return [tuple([A] * length)] if defects == 0 else []
    out=[]
    for bits in product((A,B),repeat=length-2):
        w=(A,)+bits+(A,)
        if sum(x==B for x in w)==defects and all(w[i]!=B or w[i-1]!=B for i in range(1,length)):
            out.append(w)
    return out

def observer(P,Q):
    # Endpoint native 6-vector; each direction j=2*a+sgn has weight (+1,-1).
    def end(W):
        v=[0]*6
        for s in W:v[s//2]+=1 if s%2==0 else -1
        return tuple(v)
    def edges(W):
        return tuple(sorted(Counter(zip(W,W[1:])).items()))
    return (len(P),len(Q),end(P),end(Q),edges(P),edges(Q),sum(a==b for a,b in zip(P,Q)))

def key(P,Q,pP,pQ,rP,rQ):
    m,n=len(P),len(Q)
    cp=min(max(0,m-pP),max(0,n-pQ))
    coords={}
    for i in range(max(1,m-pP),m):coords[('P',i)]=P[i-1]
    for i in range(max(1,n-pQ),n):coords[('Q',i)]=Q[i-1]
    for i in range(cp+1,min(m,n+rQ)+1):coords[('P',i)]=P[i-1]
    for i in range(cp+1,min(n,m+rP)+1):coords[('Q',i)]=Q[i-1]
    return tuple(sorted(coords.items())),cp

def population_dp(m,n,kp,kq,d,k):
    forced=dict(k)
    # No pair is fabricated: each raw (P,Q) contributes +1.
    D={(0,0,0,A,A):1}
    for i in range(1,n+1):
        N=defaultdict(int)
        for (a,b,x,lp,lq),cnt in D.items():
            optsP=(A,B) if i<=m else (None,)
            optsQ=(A,B)
            for pv in optsP:
                if i<=m and (i==1 or i==m) and pv!=A:continue
                if pv is not None and forced.get(('P',i),pv)!=pv:continue
                if pv==B and lp==B:continue
                for qv in optsQ:
                    if (i==1 or i==n) and qv!=A:continue
                    if forced.get(('Q',i),qv)!=qv:continue
                    if qv==B and lq==B:continue
                    na=a+(pv==B) if pv is not None else a
                    nb=b+(qv==B)
                    nx=x+(pv!=qv) if pv is not None else x
                    if na>kp or nb>kq or nx>d:continue
                    N[(na,nb,nx,pv if pv is not None else lp,qv)]+=cnt
        D=N
    return sum(cnt for (a,b,x,lp,lq),cnt in D.items() if (a,b,x)==(kp,kq,d))

class TreeChecker:
    def __init__(self):
        self.memo={};self.intern={};self.count=0
    def signature(self,P,Q,pp,pq,ap,aq):
        state=(P,Q,pp,pq,ap,aq)
        if state in self.memo:return self.memo[state]
        children=[]
        if pp:
            if P:children.append(('P_POP',self.signature(P[:-1],Q,pp-1,pq,ap,aq)))
        if pq:
            if Q:children.append(('Q_POP',self.signature(P,Q[:-1],pp,pq-1,ap,aq)))
        if ap:
            for z in DIRECTIONS: children.append((('P_APPEND',z),self.signature(P+(z,),Q,pp,pq,ap-1,aq)))
        if aq:
            for z in DIRECTIONS: children.append((('Q_APPEND',z),self.signature(P,Q+(z,),pp,pq,ap,aq-1)))
        sig=(observer(P,Q),tuple(children))
        if sig not in self.intern:self.intern[sig]=len(self.intern)+1
        v=self.intern[sig]
        self.memo[state]=v
        return v

def test():
    families=0; pairs=0; histories=0; dp_checks=0; signatures=0
    examples=[]
    configs=[]
    for m in range(4,7):
      for n in range(m+1,min(9,m+3)):
        for kp in range(0,min(3,(m-1)//2)+1):
          for kq in range(0,min(3,(n-1)//2)+1):
            for pP,pQ,rP,rQ in [(1,min(3,n-1),0,0),(min(2,m-1),min(4,n-1),0,0),(1,min(3,n-1),1,0),(1,min(3,n-1),0,1)]:
                configs.append((m,n,kp,kq,pP,pQ,rP,rQ))
    # Restrict full 12-direction recursion to at most one APPEND for tractable exhaustive checking.
    checker=TreeChecker()
    for m,n,kp,kq,pP,pQ,rP,rQ in configs:
        O=defaultdict(list)
        for P in words(m,kp):
          for Q in words(n,kq):O[observer(P,Q)].append((P,Q))
        for obs, fiber in O.items():
          if len(fiber)>30:continue
          families+=1;histories+=len(fiber)
          kk=defaultdict(list);ss=defaultdict(list)
          for P,Q in fiber:
            k,c=key(P,Q,pP,pQ,rP,rQ)
            sig=checker.signature(P,Q,pP,pQ,rP,rQ)
            kk[k].append((P,Q));ss[sig].append((P,Q))
          Kpart=sorted(tuple(sorted(v)) for v in kk.values()); Spart=sorted(tuple(sorted(v)) for v in ss.values())
          assert Kpart==Spart,(m,n,kp,kq,pP,pQ,rP,rQ,obs,Kpart,Spart)
          for k,h in kk.items():
            assert population_dp(m,n,kp,kq,m-obs[-1],k)==len(h),(m,n,kp,kq,k,h)
            dp_checks+=1
          pairs+=len(fiber)*(len(fiber)-1)//2
    P1=tuple([A,A,A,A,B,A,A]);P2=tuple([A,B,A,A,A,A,A]);Q=tuple([A,A,B,A,A,A,A,A])
    assert observer(P1,Q)==observer(P2,Q)
    assert key(P1,Q,1,4,0,0)!=key(P2,Q,1,4,0,0)
    def qpop4(p,q):
      seq=[observer(p,q)]
      for _ in range(4):q=q[:-1];seq.append(observer(p,q))
      return [o[-1] for o in seq]
    k1=qpop4(P1,Q);k2=qpop4(P2,Q)
    assert k1==[5,5,4,3,3] and k2==[5,5,4,3,2],(k1,k2)
    return {'marker':'STAGE453B_ARBITRARY_BUDGET_EXACT_REPAIR_PASS', 'configs':len(configs), 'fibers':families,'histories':histories,'history_pairs':pairs,'population_dp_checks':dp_checks,'memoized_future_states':len(checker.memo),'distinct_future_signatures':len(checker.intern),'native_append_direction_count':len(DIRECTIONS),'witness':{'m':7,'n':8,'pP':1,'pQ':4,'rP':0,'rQ':0,'P1':'AAAABAA','P2':'ABAAAAA','Q':'AABAAAAA','initial_K':5,'after_Q_POP_1_to_4_K_P1':k1,'after_Q_POP_1_to_4_K_P2':k2}}


def summary_class(m,n,pP,pQ,rP,rQ,K):
    fd=dict(K)
    c=min(max(0,m-pP),max(0,n-pQ));t=min(n,m+rP);u=max(1,n-pQ)
    get=lambda src,i:fd.get((src,i),A if i==1 or (src=='P' and i==m) or (src=='Q' and i==n) else None)
    part=(get('P',c),get('Q',c)) if c else (None,None)
    bP=bQ=d=0
    for i in range(c+1,m+1):
        p,q=get('P',i),get('Q',i);assert p is not None and q is not None
        bP+=(p==B);bQ+=(q==B);d+=(p!=q)
    pair=(bP,bQ,d,get('P',c+1) if c<m else None,get('Q',c+1) if c<m else None,get('Q',m) if c<m else None)
    if t<u-1:
        left=list(range(m+1,t+1));right=list(range(u,n+1))
        qonly=(1,sum(get('Q',i)==B for i in left),sum(get('Q',i)==B for i in right),get('Q',left[0]) if left else None,get('Q',left[-1]) if left else None,get('Q',right[0]) if right else None)
    else:
        tail=list(range(m+1,n+1))
        qonly=(0,sum(get('Q',i)==B for i in tail),get('Q',tail[0]) if tail else None)
    return (part,pair,qonly)

def check_grouping():
    combinations=0;keys=0;groups=0
    for m in range(4,8):
      for n in range(m+1,min(m+4,10)):
       for kp in range(3):
        for kq in range(3):
         O=defaultdict(list)
         for P in words(m,kp):
          for Q in words(n,kq):O[observer(P,Q)].append((P,Q))
         for o,f in O.items():
          for pP,pQ,rP,rQ in [(1,4,0,0),(2,3,1,0),(1,0,2,0),(0,1,2,0),(0,0,1,0),(0,5,0,0)]:
           byKey=defaultdict(int)
           for P,Q in f:byKey[key(P,Q,pP,pQ,rP,rQ)[0]]+=1
           bySummary=defaultdict(set)
           for K,mass in byKey.items():bySummary[summary_class(m,n,pP,pQ,rP,rQ,K)].add(mass)
           assert all(len(ms)==1 for ms in bySummary.values()),(m,n,kp,kq,pP,pQ,rP,rQ,bySummary)
           combinations+=1;keys+=len(byKey);groups+=len(bySummary)
    return {'summary_mass_constancy_parameter_fibers':combinations,'summary_distinct_keys_checked':keys,'summary_groups_checked':groups}

if __name__=='__main__':
    print(json.dumps({**test(),**check_grouping()},indent=2,sort_keys=True))
