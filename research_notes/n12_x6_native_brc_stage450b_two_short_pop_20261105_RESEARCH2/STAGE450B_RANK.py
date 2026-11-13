"""Polynomial class support rank/unrank and exact internal-history rank/unrank for Stage450-B.
Run from same directory as STAGE450B_PORTABLE.py.
"""
from functools import lru_cache
from collections import defaultdict
from STAGE450B_PORTABLE import support, paths, key, obs
import json

def coder(m,n,kp,kq,d,r):
    qF,pop,_,M=support(m,n,kp,kq,d,r)
    ell=min(n-1,m+r)-m
    size=5+ell
    @lru_cache(None)
    def count(bits):
        if len(bits)>size:return 0
        result=0
        for alpha in (0,1):
          if len(bits)>0 and alpha!=bits[0]:continue
          for beta in (0,1):
           if len(bits)>1 and beta!=bits[1]:continue
           for gamma in (0,1):
            if len(bits)>2 and gamma!=bits[2]:continue
            for qprev in (0,1):
             if len(bits)>3 and qprev!=bits[3]:continue
             for q0 in (0,1):
              if len(bits)>4 and q0!=bits[4]:continue
              if qprev*q0:continue
              states={(q0,q0):1}
              for j in range(ell):
               nxt=defaultdict(int)
               for (s,v),amount in states.items():
                for z in (0,1):
                 if len(bits)>5+j and z!=bits[5+j]:continue
                 if not v*z:nxt[(s+z,z)]+=amount
               states=nxt
              for (s,v),amount in states.items():
               if M(alpha,beta,gamma,qprev,q0,s,v)>0:result+=amount
        return result
    def rank(k):
        bits=k[:3]+k[3]
        if len(bits)!=size or count(bits)!=1:raise ValueError('unsupported class')
        result=0
        for i,z in enumerate(bits):
            if z:result+=count(bits[:i]+(0,))
        return result
    def unrank(k):
        if k<0 or k>=qF:raise ValueError('class out of range')
        bits=()
        for _ in range(size):
            zeros=count(bits+(0,))
            if k<zeros:bits+=(0,)
            else:k-=zeros;bits+=(1,)
        assert k==0
        return bits[:3]+(bits[3:],)
    assert count(())==qF
    return rank,unrank

def num_hist(m,n,kp,kq,d,r,k,pfix=(),qfix=()):
    alpha,beta,gamma,w=k
    reqP={0:0,m-3:alpha,m-2:beta,m-1:0}
    reqQ={0:0,n-2:gamma,n-1:0}
    reqQ.update({m-2+j:z for j,z in enumerate(w)})
    for j,z in enumerate(pfix):
        reqP[j]=z if (j not in reqP or reqP[j]==z) else 2
    for j,z in enumerate(qfix):
        reqQ[j]=z if (j not in reqQ or reqQ[j]==z) else 2
    states={(0,0,0,0,0):1}
    for j in range(n):
        nxt=defaultdict(int)
        for (a,b,e,lp,lq),amount in states.items():
            for x in ((0,1) if j<m else (None,)):
                if j<m and ((j in reqP and x!=reqP[j]) or lp*x):continue
                for y in (0,1):
                    if (j in reqQ and y!=reqQ[j]) or lq*y:continue
                    A=a+(x or 0);B=b+y;E=e+(x!=y if x is not None else 0)
                    if A<=kp and B<=kq and E<=d:
                        nxt[(A,B,E,x if x is not None else 0,y)]+=amount
        states=nxt
    return sum(cnt for (a,b,e,_,_),cnt in states.items() if (a,b,e)==(kp,kq,d))

def history_rank(m,n,kp,kq,d,r,k,p,q):
    if key(p,q,r)!=k:raise ValueError('class mismatch')
    v=0
    for i,z in enumerate(p):
        if z:v+=num_hist(m,n,kp,kq,d,r,k,p[:i]+(0,))
    for j,z in enumerate(q):
        if z:v+=num_hist(m,n,kp,kq,d,r,k,p,q[:j]+(0,))
    return v

def history_unrank(m,n,kp,kq,d,r,k,index):
    if not 0<=index<num_hist(m,n,kp,kq,d,r,k):raise ValueError('bad rank')
    p=q=()
    for _ in range(m):
        c=num_hist(m,n,kp,kq,d,r,k,p+(0,))
        if index<c:p+=(0,)
        else:p+=(1,);index-=c
    for _ in range(n):
        c=num_hist(m,n,kp,kq,d,r,k,p,q+(0,))
        if index<c:q+=(0,)
        else:q+=(1,);index-=c
    assert index==0
    return p,q

def audit():
    checks=0;hchecks=0;cases=0
    for m in range(3,9):
      for n in range(m+1,min(11,m+4)):
       for kp in range(min(3,(m-1)//2)+1):
        for kq in range(min(3,(n-1)//2)+1):
         fibers=defaultdict(list)
         for p in paths(m,kp):
          for q in paths(n,kq):fibers[m-obs(p,q)[-1]].append((p,q))
         for d,hs in fibers.items():
          for r in range(4):
           rank,unrank=coder(m,n,kp,kq,d,r)
           seen={key(p,q,r) for p,q in hs}
           for k in seen:
               assert unrank(rank(k))==k
               checks+=1
               if hchecks<100:
                   p,q=next((p,q) for p,q in hs if key(p,q,r)==k)
                   idx=history_rank(m,n,kp,kq,d,r,k,p,q)
                   assert history_unrank(m,n,kp,kq,d,r,k,idx)==(p,q)
                   hchecks+=1
           cases+=1
    a,b=coder(64,80,15,17,1,12)
    assert a(b(0))==0 and a(b(1045))==1045
    return {'status':'STAGE450B_POLYNOMIAL_RANK_UNRANK_PASS',
            'fibers':cases,'class_rank_roundtrips':checks,
            'history_rank_roundtrips':hchecks,'large_last_class_index':1045}
if __name__=='__main__':print(json.dumps(audit(),sort_keys=True,indent=2))
