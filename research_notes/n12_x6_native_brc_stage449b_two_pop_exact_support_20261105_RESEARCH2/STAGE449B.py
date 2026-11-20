"""Native-X6 two-sided POP/APPEND exact quotient check (stdlib)."""
from itertools import combinations
from collections import defaultdict
from functools import lru_cache
import json

D = tuple(range(12)) # 0=+E1, 1=-E1, 2..11=other signed native directions

def paths(n,k):
    for bs in combinations(range(1,n-1),k):
        if all(b-a>1 for a,b in zip(bs,bs[1:])):
            yield tuple(int(i in bs) for i in range(n))

def observer(p,q):
    def end(t):
        v=[0]*6
        for z in t:v[z//2]+=1 if z%2==0 else -1
        return tuple(v)
    def adj(t):
        a=[0]*144
        for x,y in zip(t,t[1:]):a[x*12+y]+=1
        return tuple(a)
    return len(p),len(q),end(p),end(q),adj(p),adj(q),sum(x==y for x,y in zip(p,q))

def repair(p,q,r):
    m,n=len(p),len(q)
    h=min(n-1,m+r)
    return p[m-2],q[n-2],q[m-1:h]

@lru_cache(None)
def future(p,q,pp,qp,ap,aq):
    options=[]
    if pp:options.append(('P-',future(p[:-1],q,0,qp,ap,aq)))
    if qp:options.append(('Q-',future(p,q[:-1],pp,0,ap,aq)))
    for z in D:
        if ap:options.append((f'P+{z}',future(p+(z,),q,pp,qp,ap-1,aq)))
        if aq:options.append((f'Q+{z}',future(p,q+(z,),pp,qp,ap,aq-1)))
    return observer(p,q),tuple(options)

def support(m,n,kp,kq,d,r):
    h=min(n-1,m+r); ell=h-m
    state={(0,0,0,0,0,0):1}; transitions=0
    for i in range(1,m+1):
        nxt=defaultdict(int)
        for (a,b,e,u,v,beta),count in state.items():
            for x in ((0,) if i in (1,m) else (0,1)):
                if u*x:continue
                for y in ((0,) if i==1 else (0,1)):
                    if v*y:continue
                    aa,bb,ee=a+x,b+y,e+(x!=y)
                    if aa<=kp and bb<=kq and ee<=d:
                        nxt[(aa,bb,ee,x,y,x if i==m-1 else beta)]+=count;transitions+=1
        state=nxt
    T=defaultdict(int)
    for (a,b,e,u,v,beta),count in state.items():
        if a==kp and e==d:T[(beta,v,b)]+=count
    W=defaultdict(int)
    for q0 in (0,1):
        ww={(q0,q0):1}
        for i in range(ell):
            nxt=defaultdict(int)
            for (s,v),count in ww.items():
                for z in (0,1):
                    if not (v*z):nxt[(s+z,z)]+=count
            ww=nxt
        for (s,v),count in ww.items():W[(q0,s,v)]+=count
    @lru_cache(None)
    def U(v,gamma,rem):
        if rem<0:return 0
        t=n-h; state={(v,0):1}
        if t==1 and gamma!=v:return 0
        for i in range(1,t+1):
            nxt=defaultdict(int)
            for (prev,used),count in state.items():
                for z in ((0,) if i==t else ((gamma,) if i==t-1 else (0,1))):
                    if prev*z:continue
                    if used+z<=rem:nxt[(z,used+z)]+=count
            state=nxt
        return state.get((0,rem),0)
    qF=total=0
    for (q,s,v),howmany in W.items():
        for beta in (0,1):
            for gamma in (0,1):
                pop=sum(c*U(v,gamma,kq-b-s+q) for (be,qq,b),c in T.items() if be==beta and qq==q)
                if pop:qF+=howmany;total+=howmany*pop
    return qF,total,transitions

def audit():
    tiny=[(5,7,1,1),(5,7,1,2),(5,7,2,1),(5,7,2,2),(4,5,1,1),(4,6,1,1),(5,6,1,2),(6,7,2,2)]
    checks={'future_cases':len(tiny),'future_fibers':0,'future_histories':0,'future_classes':0,'history_pairs':0}
    for m,n,kp,kq in tiny:
        fibers=defaultdict(list)
        for p in paths(m,kp):
            for q in paths(n,kq):fibers[observer(p,q)].append((p,q))
        for hs in fibers.values():
            keys=[repair(p,q,1) for p,q in hs]
            sig=[future(p,q,1,1,1,1) for p,q in hs]
            mapping=defaultdict(set)
            for k,v in zip(keys,sig):mapping[k].add(v)
            assert all(len(v)==1 for v in mapping.values())
            assert len(mapping)==len(set(sig))
            checks['future_fibers']+=1;checks['future_histories']+=len(hs)
            checks['future_classes']+=len(mapping);checks['history_pairs']+=len(hs)*(len(hs)-1)//2
    dp={'parameter_fibers':0,'histories_summed':0,'classes_summed':0}
    for m in range(3,9):
        for n in range(m+1,min(11,m+4)):
            for kp in range(0,min(3,(m-1)//2)+1):
                for kq in range(0,min(3,(n-1)//2)+1):
                    fibers=defaultdict(list)
                    for p in paths(m,kp):
                        for q in paths(n,kq):fibers[m-observer(p,q)[-1]].append((p,q))
                    for d,hs in fibers.items():
                        for r in (0,1,2,3):
                            qF,pop,_=support(m,n,kp,kq,d,r)
                            assert (qF,pop)==(len(set(repair(p,q,r) for p,q in hs)),len(hs))
                            dp['parameter_fibers']+=1;dp['histories_summed']+=len(hs);dp['classes_summed']+=qF
    z=support(64,80,15,17,1,12)
    return {'status':'STAGE449B_TWO_POP_QUOTIENT_AND_SUPPORT_PASS','full_native_append_directions':12,
            'exact_future':checks,'support_dynamic_program':dp,
            'large_case':{'m':64,'n':80,'kP':15,'kQ':17,'mismatch_d':1,'rP':12,'qF':z[0],'population':str(z[1]),'prefix_transitions':z[2]},
            'future_cached_states':future.cache_info().currsize}

if __name__=='__main__':print(json.dumps(audit(),sort_keys=True,indent=2))
