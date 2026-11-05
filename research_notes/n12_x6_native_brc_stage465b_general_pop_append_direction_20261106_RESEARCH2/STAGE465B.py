from collections import defaultdict
from functools import lru_cache
from itertools import product
import json

ALPHABET=tuple(range(12))
A,B,C=0,2,4 # +E1, +E2, +E3

def observer(p,q):
    def endpoint(w):
        a=[0]*6
        for d in w:a[d//2]+=1 if d%2==0 else -1
        return tuple(a)
    def adj(w):
        h=[0]*144
        for x,y in zip(w,w[1:]):h[12*x+y]+=1
        return tuple((i,v) for i,v in enumerate(h) if v)
    return (len(p),len(q),endpoint(p),endpoint(q),adj(p),adj(q),sum(x==y for x,y in zip(p,q)))

def signature(p,q,hp,hq,rp,rq):
    @lru_cache(None)
    def f(p,q,a,b,c,d):
        children=[]
        if a and p: children.append(('POP_P',f(p[:-1],q,a-1,b,c,d)))
        if b and q: children.append(('POP_Q',f(p,q[:-1],a,b-1,c,d)))
        if c:
            for z in ALPHABET:children.append((f'APP_P_{z}',f(p+(z,),q,a,b,c-1,d)))
        if d:
            for z in ALPHABET:children.append((f'APP_Q_{z}',f(p,q+(z,),a,b,c,d-1)))
        return (observer(p,q),tuple(children))
    return f(p,q,hp,hq,rp,rq)

def wordlist(n):
    # original A/B fixed-end, isolated B
    ans=[]
    for t in product((A,B),repeat=n-2):
        w=(A,)+t+(A,)
        if all(not(w[i]==w[i+1]==B) for i in range(n-1)):ans.append(w)
    return ans

def binary_checks():
    stats={'parameter_configs':0,'nonempty_fibers':0,'history_pairs_checked':0,'distinct_base_classes':0,'full12_append_actions':12}
    for m,n in ((2,3),(3,4),(3,5),(4,5)):
        # rP up to one, Q pop horizon full
        for hp in (0,1,min(2,m)):
            for hq in (0,1,n-1):
                for rp in (0,1):
                    stats['parameter_configs']+=1
                    fibers=defaultdict(list)
                    for p in wordlist(m):
                        for q in wordlist(n):fibers[observer(p,q)].append((p,q))
                    for hist in fibers.values():
                        if len(hist)<2:continue
                        stats['nonempty_fibers']+=1
                        sig0=[signature(p,q,hp,hq,rp,0) for p,q in hist]
                        sig1=[signature(p,q,hp,hq,rp,1) for p,q in hist]
                        for i in range(len(hist)):
                            for j in range(i+1,len(hist)):
                                if (sig0[i]==sig0[j])!=(sig1[i]==sig1[j]):
                                    raise AssertionError((m,n,hp,hq,rp,hist[i],hist[j]))
                                stats['history_pairs_checked']+=1
                        stats['distinct_base_classes']+=len(set(sig0))
    return stats

def ternary_witness():
    p1=(A,B,A,C,A,A,A)
    p2=(A,C,A,B,A,A,A)
    q=(A,)*9
    assert observer(p1,q)==observer(p2,q)
    s0_1=signature(p1,q,2,6,0,0)
    s0_2=signature(p2,q,2,6,0,0)
    assert s0_1==s0_2
    s1_1=signature(p1,q,2,6,0,1)
    s1_2=signature(p2,q,2,6,0,1)
    assert s1_1!=s1_2
    qshort=(A,)*3
    k1=observer(p1,qshort+(B,))[-1]
    k2=observer(p2,qshort+(B,))[-1]
    assert (k1,k2)==(2,3)
    return {'P1':'A B A C A A A','P2':'A C A B A A A','Q':'A'*9,
      'initial_observer_equal':True,'POP_P<=2_POP_Q<=6_equal':True,
      'Q_append_B_distinguishes':True,'K_after_6_Q_POP_then_APPEND_Q_B':[k1,k2],
      'B':'native +E2','C':'native +E3'}

if __name__=='__main__':
    import time
    t=time.time(); out={'stage':'465B','binary':binary_checks(),'ternary':ternary_witness()}
    out['duration_seconds']=round(time.time()-t,3)
    print(json.dumps(out,indent=2,ensure_ascii=False))

