"""Stage478-B: Exact three-letter Euler-BRC fiber counts, random-access classes.
Stdlib-only Python 3; all counts are exact integers. Independent proof in PROOF_STAGE478B.md.
"""
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache
from math import factorial
import json
ABC="ABC"
PAIRS=tuple(a+b for a in ABC for b in ABC)
IDX={e:i for i,e in enumerate(PAIRS)}
def edge(a,b):
    z=[0]*9;z[IDX[a+b]]=1;return tuple(z)
def edges(w):
    z=[0]*9
    for a,b in zip(w,w[1:]):z[IDX[a+b]]+=1
    return tuple(z)
def add(*vs):return tuple(map(sum,zip(*vs)))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def minor_det(a):
    if len(a)==0:return 1
    if len(a)==1:return a[0][0]
    if len(a)==2:return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    raise ValueError("Three-letter basis only")
@lru_cache(None)
def N(l,s,t,e):
    if len(e)!=9 or any(v<0 for v in e) or sum(e)!=l-1 or l<1:return 0
    if l==1:return int(s==t and not any(e))
    out=[sum(e[i*3:i*3+3]) for i in range(3)]
    inn=[sum(e[j*3+i] for j in range(3)) for i in range(3)]
    a=ABC.index(s);b=ABC.index(t)
    if any(out[v]-inn[v]!=(v==a)-(v==b) for v in range(3)):return 0
    active=[v for v in range(3) if out[v]+inn[v] or v in (a,b)]
    rest=[v for v in active if v!=b]
    if any(out[v]==0 for v in rest):return 0
    L=[[out[v]-e[3*v+v] if v==w else -e[3*v+w] for w in rest] for v in rest]
    tree=minor_det(L)
    if tree<=0:return 0
    numer=tree*factorial(out[b])
    for v in rest:numer*=factorial(out[v]-1)
    den=1
    for v in e:den*=factorial(v)
    assert numer%den==0
    return numer//den
@lru_cache(None)
def Ndp(s,t,e):
    if any(v<0 for v in e):return 0
    if not sum(e):return int(s==t)
    ans=0
    for b in ABC:
        pos=IDX[s+b]
        if e[pos]:
            f=list(e);f[pos]-=1
            ans+=Ndp(b,t,tuple(f))
    return ans
def base(m):
    z=[0]*9;z[0]=m-1;return tuple(z)
def theta(m,w,h):
    return add(base(m),edge("A",w[0]),edges(w),edge(w[-1],"A"),
               edge("A",h[0]),edges(h),edge(h[-1],"A"))
@lru_cache(None)
def hidden(s,t,ew,T,u,m):
    z=minus(T,add(base(m),edge("A",s),ew,edge(t,"A")))
    if any(v<0 for v in z):return 0
    ans=0
    for a in ABC:
        for b in ABC:
            h=minus(z,add(edge("A",a),edge(b,"A")))
            if all(v>=0 for v in h):ans+=N(u,a,b,h)
    return ans
def compositions(bnd,total,p=()):
    if len(p)==8:
        if 0<=total<=bnd[8]:yield p+(total,)
        return
    for i in range(min(total,bnd[len(p)])+1):
        yield from compositions(bnd,total-i,p+(i,))
def types(k,u,T):
    m=2*k+2
    room=minus(T,base(m))
    if any(v<0 for v in room):return
    for e in compositions(room,k-1):
        for s in ABC:
            for t in ABC:
                count=N(k,s,t,e)
                if count:
                    weight=hidden(s,t,e,T,u,m)
                    if weight:yield count,weight
def summarize(k,u,T):
    rows=list(types(k,u,T))
    return {"classes":sum(a for a,b in rows),
            "population":sum(a*b for a,b in rows),
            "supported_types":len(rows)}
def population(w,u,T):
    return hidden(w[0],w[-1],edges(w),T,u,2*len(w)+2)
def prefix_count(p,k,u,T):
    if not p:return summarize(k,u,T)["classes"]
    e=edges(p);m=2*k+2;remain=minus(T,add(base(m),e))
    if any(v<0 for v in remain):return 0
    ans=0
    for g in compositions(remain,k-len(p)):
        for t in ABC:
            c=N(k-len(p)+1,p[-1],t,g)
            if c and hidden(p[0],t,add(e,g),T,u,m):ans+=c
    return ans
def rank(w,u,T):
    if not population(w,u,T):raise ValueError("not supported")
    r=0;p=""
    for x in w:
        for y in ABC:
            if y==x:break
            r+=prefix_count(p+y,len(w),u,T)
        p+=x
    return r
def unrank(i,k,u,T):
    if not 0<=i<summarize(k,u,T)["classes"]:raise ValueError("rank")
    p=""
    for _ in range(k):
        for x in ABC:
            n=prefix_count(p+x,k,u,T)
            if i<n:p+=x;break
            i-=n
        else:raise AssertionError("rank exhausted")
    return p
def brute(k,u,rank_checks=False):
    d=defaultdict(lambda:defaultdict(int));m=2*k+2
    for w0 in product(ABC,repeat=k):
        w="".join(w0)
        for h0 in product(ABC,repeat=u):
            h="".join(h0)
            d[theta(m,w,h)][w]+=1
    cnt=checks=rchecks=0
    for T,cs in d.items():
        z=summarize(k,u,T)
        assert z["classes"]==len(cs)
        assert z["population"]==sum(cs.values())
        for ix,(w,n) in enumerate(sorted(cs.items())):
            assert population(w,u,T)==n
            checks+=1
            if rank_checks:
                assert rank(w,u,T)==ix and unrank(ix,k,u,T)==w
                rchecks+=1
        cnt+=1
    return {"k":k,"u":u,"fibers":cnt,"classes_checked":checks,"rank_checks":rchecks}
def run():
    tested=0
    for l in range(1,8):
        d=Counter()
        for w0 in product(ABC,repeat=l):
            w="".join(w0);d[(w[0],w[-1],edges(w))]+=1
        for (s,t,e),mass in d.items():
            assert N(l,s,t,e)==Ndp(s,t,e)==mass
            tested+=1
    z=add(edge("A","A"),edge("B","B"),edge("C","C"))
    assert N(4,"A","A",z)==0
    params=((1,1),(1,2),(2,1),(2,2),(3,2),(2,3))
    small=[brute(k,u,k+u<=4) for k,u in params]
    k=24;u=18;m=2*k+2
    w=("ABCCABCAAB"*5)[:k]
    h=("BCAACBBC"*5)[:u]
    T=theta(m,w,h)
    lg=summarize(k,u,T)
    r=lg["classes"]//2;W=unrank(r,k,u,T)
    assert rank(W,u,T)==r
    assert 0<lg["classes"]<=lg["population"]<=3**(k+u)
    return {"status":"ALL_ASSERTIONS_PASSED","model":"P=A^m,Q=A^m W A H A; W,H in ABC; P POP/APPEND<=k, Q POP=0 APPEND<=1; future APPEND native 12 directions",
            "euler_exact_verified_lengths":"1..7","euler_distinct_types_checked":tested,
            "small_brute_fibers":small,
            "large":{"k":k,"u":u,"m":m,"n":m+k+u+2,
                     "witness_w":w,"witness_h":h,"theta":list(T),**lg,
                     "rank_spot_checks":[{"rank":r,"word":W,"population":population(W,u,T)}]},
            "arithmetic":"exact Python integers, no floating point"}
if __name__=="__main__":print(json.dumps(run(),ensure_ascii=False,indent=2))
