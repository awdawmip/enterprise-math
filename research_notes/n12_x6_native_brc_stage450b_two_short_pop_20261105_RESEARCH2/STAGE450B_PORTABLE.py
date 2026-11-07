"""Stage450-B: exact X6 future-equivalence classes (P:2 POP, Q:1 POP)."""
from itertools import combinations
from collections import defaultdict
from functools import lru_cache
import json
D=range(12) # even +Ei, odd -Ei

def paths(n,k):
    for bs in combinations(range(1,n-1),k):
        if all(y-x>1 for x,y in zip(bs,bs[1:])):
            yield tuple(int(i in bs) for i in range(n))

def obs(p,q):
    def end(w):
        v=[0]*6
        for x in w:v[x//2]+=1 if x%2==0 else -1
        return tuple(v)
    def edges(w):
        v=[0]*144
        for x,y in zip(w,w[1:]):v[12*x+y]+=1
        return tuple(v)
    return len(p),len(q),end(p),end(q),edges(p),edges(q),sum(x==y for x,y in zip(p,q))

def key(p,q,r):
    m,n=len(p),len(q);h=min(n-1,m+r)
    return p[m-3],p[m-2],q[n-2],q[m-2:h]

@lru_cache(None)
def future(p,q,pp,qp,ap,aq):
    out=[]
    if pp:out.append(('P-',future(p[:-1],q,pp-1,qp,ap,aq)))
    if qp:out.append(('Q-',future(p,q[:-1],pp,qp-1,ap,aq)))
    for z in D:
        if ap:out.append((f'P+{z}',future(p+(z,),q,pp,qp,ap-1,aq)))
        if aq:out.append((f'Q+{z}',future(p,q+(z,),pp,qp,ap,aq-1)))
    return obs(p,q),tuple(out)

def support(m,n,kp,kq,d,r):
    h=min(n-1,m+r);ell=h-m
    T={(0,0,0,0,0,0):1};steps=0
    for i in range(1,m):
        nxt=defaultdict(int)
        for (a,b,e,lp,lq,alpha),cnt in T.items():
            for x in ((0,) if i==1 else (0,1)):
                if lp*x:continue
                for y in ((0,) if i==1 else (0,1)):
                    if lq*y:continue
                    A,B,E=a+x,b+y,e+(x!=y)
                    if A<=kp and B<=kq and E<=d:
                        nxt[(A,B,E,x,y,x if i==m-2 else alpha)]+=cnt;steps+=1
        T=nxt
    prefix=defaultdict(int)
    for (a,b,e,beta,qprev,alpha),cnt in T.items():
        if a==kp:prefix[(alpha,beta,qprev,b,e)]+=cnt
    W=defaultdict(int)
    for qprev in (0,1):
      for q0 in (0,1):
        if qprev*q0:continue
        states={(q0,q0):1}
        for _ in range(ell):
            nxt=defaultdict(int)
            for (s,last),cnt in states.items():
                for z in (0,1):
                    if not last*z:nxt[(s+z,z)]+=cnt
            states=nxt
        for (s,v),cnt in states.items():W[(qprev,q0,s,v)]+=cnt
    @lru_cache(None)
    def U(v,gamma,R):
        if R<0:return 0
        t=n-h
        if t==1 and gamma!=v:return 0
        states={(v,0):1}
        for i in range(1,t+1):
            nxt=defaultdict(int)
            for (last,b),cnt in states.items():
                opts=(0,) if i==t else ((gamma,) if i==t-1 else (0,1))
                for z in opts:
                    if not last*z and b+z<=R:nxt[(z,b+z)]+=cnt
            states=nxt
        return states.get((0,R),0)
    @lru_cache(None)
    def M(alpha,beta,gamma,qprev,q0,s,v):
        return sum(cnt*U(v,gamma,kq-b-s) for (a,be,qp,b,e),cnt in prefix.items()
                   if (a,be,qp,e)==(alpha,beta,qprev,d-q0))
    qF=population=0
    for (qprev,q0,s,v),num in W.items():
      for alpha in (0,1):
       for beta in (0,1):
        for gamma in (0,1):
            count=M(alpha,beta,gamma,qprev,q0,s,v)
            if count:qF+=num;population+=num*count
    return qF,population,steps,M

def audit():
    exact={'fibers':0,'histories':0,'pairs':0,'classes':0}
    for m,n,kp,kq in ((3,4,0,1),(4,5,1,1),(4,6,1,1),(5,6,1,2),(5,7,1,1)):
        fibers=defaultdict(list)
        for p in paths(m,kp):
            for q in paths(n,kq):fibers[obs(p,q)].append((p,q))
        for hist in fibers.values():
            keys=[key(p,q,1) for p,q in hist]
            signatures=[future(p,q,2,1,1,1) for p,q in hist]
            assert all((keys[i]==keys[j])==(signatures[i]==signatures[j])
                       for i in range(len(hist)) for j in range(i+1,len(hist)))
            exact['fibers']+=1;exact['histories']+=len(hist)
            exact['pairs']+=len(hist)*(len(hist)-1)//2;exact['classes']+=len(set(keys))
    dp={'fibers':0,'histories':0,'classes':0,'pop_checks':0}
    for m in range(3,9):
      for n in range(m+1,min(11,m+4)):
       for kp in range(min(3,(m-1)//2)+1):
        for kq in range(min(3,(n-1)//2)+1):
         fibers=defaultdict(list)
         for p in paths(m,kp):
          for q in paths(n,kq):fibers[m-obs(p,q)[-1]].append((p,q))
         for d,hist in fibers.items():
          for r in (0,1,2,3):
            qF,pop,_,M=support(m,n,kp,kq,d,r)
            groups=defaultdict(int)
            for p,q in hist:groups[key(p,q,r)]+=1
            assert (qF,pop)==(len(groups),len(hist))
            for (alpha,beta,gamma,w),cnt in groups.items():
                assert M(alpha,beta,gamma,w[0],w[1],sum(w[1:]),w[-1])==cnt
                dp['pop_checks']+=1
            dp['fibers']+=1;dp['histories']+=len(hist);dp['classes']+=len(groups)
    a,b,steps,_=support(64,80,15,17,1,12)
    return {'status':'STAGE450B_TWO_P_ONE_Q_POP_EXACT_SUPPORT_PASS',
      'native_directions':12,'full_future':exact,'dp':dp,
      'large':{'m':64,'n':80,'kP':15,'kQ':17,'d':1,'rP':12,
               'qF':a,'population':str(b),'prefix_transitions':steps},
      'future_cached_states':future.cache_info().currsize}
if __name__=='__main__':print(json.dumps(audit(),indent=2,sort_keys=True))
