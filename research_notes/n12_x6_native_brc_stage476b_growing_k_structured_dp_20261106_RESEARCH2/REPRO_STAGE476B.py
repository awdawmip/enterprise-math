"""Stage476-B exact structured positive-BRC count/rank and finite future test."""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb
import json
A,B,C=0,1,2
D=range(12)

def family(k,u,b):
    m,n=2*k+2,3*k+2*u+4
    vis=[k+3+2*i for i in range(k)]
    hid=[3*k+5+2*i for i in range(u)]
    for loc in combinations(range(k+u),b):
        Q=[A]*n
        for i,j in enumerate(vis+hid): Q[j-1]=B if i in loc else C
        yield (A,)*m,tuple(Q),tuple(Q[j-1] for j in vis)

def Sfun(u):
    @lru_cache(None)
    def S(l,r):
        return int(0<=r<=u) if l==0 else S(l-1,r-1)+S(l-1,r)
    return S

def unrank(k,u,b,z):
    S=Sfun(u); assert 0<=z<S(k,b)
    out=[];r=b
    for l in range(k,0,-1):
        left=S(l-1,r-1)
        if z<left:out.append(B);r-=1
        else:out.append(C);z-=left
    assert z==0 and 0<=r<=u
    return tuple(out)

def rank(k,u,b,w):
    S=Sfun(u);r=b;z=0
    for l,v in zip(range(k,0,-1),w):
        if v==B:r-=1
        else:z+=S(l-1,r-1)
        assert S(l-1,r)>0
    return z

def pop(u,b,w):
    r=b-w.count(B)
    return comb(u,r) if 0<=r<=u else 0

def obs(p,q):
    def end(s):
        x=[0]*6
        for d in s:x[d%6]+=1 if d<6 else -1
        return tuple(x)
    def e(s):return tuple(sorted(Counter(zip(s,s[1:])).items()))
    return (len(p),len(q),end(p),end(q),e(p),e(q),sum(x==y for x,y in zip(p,q)))

def equal_all_future(p,q1,q2,k):
    assert obs(p,q1)==obs(p,q2)
    todo=[(p,0,0,None)];seen=set()
    while todo:
        cur,deleted,appended,qd=todo.pop()
        key=(cur,deleted,appended,qd)
        if key in seen:continue
        seen.add(key)
        x=q1 if qd is None else q1+(qd,)
        y=q2 if qd is None else q2+(qd,)
        if obs(cur,x)!=obs(cur,y):return False,len(seen)
        if deleted<k and len(cur)>1:todo.append((cur[:-1],deleted+1,appended,qd))
        if appended<k:
            for d in D:todo.append((cur+(d,),deleted,appended+1,qd))
        if qd is None:
            for d in D:todo.append((cur,deleted,appended,d))
    return True,len(seen)

def run():
    fcount=hcount=ccount=wc=0
    example=[]
    for k in range(1,8):
        for u in range(4):
            for b in range(k+u+1):
                records=list(family(k,u,b)); assert len(records)==comb(k+u,b)
                reference=obs(*records[0][:2]);counts=Counter();reps={}
                for p,q,w in records:
                    assert obs(p,q)==reference
                    counts[w]+=1;reps.setdefault(w,(p,q))
                S=Sfun(u); assert len(counts)==S(k,b)
                for i,w in enumerate(sorted(counts)):
                    assert counts[w]==pop(u,b,w) and rank(k,u,b,w)==i and unrank(k,u,b,i)==w
                assert sum(counts.values())==comb(k+u,b)
                if len(reps)>1:
                    w1,w2=sorted(reps)[0],sorted(reps)[-1]
                    p,q1=reps[w1];_,q2=reps[w2]
                    j=next(j for j in [k+3+2*i for i in range(k)] if q1[j-1]!=q2[j-1])
                    pp=p[:j-1]+(B,) if j<=len(p) else p+(A,)*(j-len(p)-1)+(B,)
                    assert obs(pp,q1)[-1]!=obs(pp,q2)[-1]
                    wc+=1
                if (k,u,b)==(3,2,2):
                    example=[[''.join('B' if v==B else 'C' for v in w),counts[w]] for w in sorted(counts)]
                fcount+=1;hcount+=len(records);ccount+=len(counts)
    audits=[]
    for k,u,b in [(1,2,1),(2,2,2)]:
        groups=defaultdict(list)
        for p,q,w in family(k,u,b):groups[w].append((p,q))
        group=next(g for g in groups.values() if len(g)>1)
        p,q1=group[0];_,q2=group[1]
        eq,states=equal_all_future(p,q1,q2,k);assert eq
        audits.append({'k':k,'u':u,'b':b,'states':states})
    k,u,b=40,31,33;S=Sfun(u);N=S(k,b);tot=comb(k+u,b)
    samples=[]
    for z in [0,1,N//2,N-2,N-1]:
        w=unrank(k,u,b,z);assert rank(k,u,b,w)==z
        samples.append({'rank':str(z),'B':w.count(B),'population':str(pop(u,b,w))})
    return {'brute_fibers':fcount,'raw_histories':hcount,'classes':ccount,
            'rank_unrank_checks':2*ccount,'witness_fibers':wc,
            'full_future_12_direction_audits':audits,'example_k3_u2_b2':example,
            'large':{'k':k,'u':u,'b':b,'m':2*k+2,'n':3*k+2*u+4,
                     'classes':str(N),'mass':str(tot),'samples':samples},
            'status':'ALL_ASSERTIONS_PASSED'}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
