"""Exact bidirectional-viability and optimal-support check for frozen R5.
Standard-library-only; arithmetic for activation thresholds is Fraction.
"""
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
HEX56 = 'd500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'


def original_r5():
    pools = {3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n = -sum(W[i] for i in range(15) if mask >> i & 1)
        k = -sum(K0[i] for i in range(15) if mask >> i & 1)
        if n >= 3 and k%36 == 0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[k]) for k in (3,12,15)] == [538,298,229]
    hist = Counter((1-Fraction(36*k,n))/23 for k in pools for n in pools[k])
    assert len(hist)==953 and Counter(hist.values())=={1:869,2:56,3:28}
    x=[0]
    for z in sorted(hist): x.append(x[-1]+hist[z])
    raw=bytes.fromhex(HEX56)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little'); centers=[bits&3];bits>>=2
    for _ in range(212): centers.append(centers[-1]+3+(bits&3));bits>>=2
    assert bits==0 and centers[0]==1 and centers[-1]==952
    assert len(x)==954 and x[-1]==1065
    return x,centers


def make_graph(x,r):
    n=len(x)
    u=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    v=[bisect_left(x,x[p]-r) for p in range(n)]
    out=[[] for _ in x]; incoming=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+2*r+2)):
            if v[q]<=u[p]+1:
                w=sum(min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q+1))
                out[p].append((q,w)); incoming[q].append((p,w))
    starts={p for p in range(n) if x[p]-x[0]<=r}
    ends={p for p in range(n) if x[-1]-x[p]<=r}
    head={p:sum(x[p]-x[b] for b in range(p)) for p in starts}
    tail={p:sum(x[b]-x[p] for b in range(p+1,n)) for p in ends}
    return out,incoming,starts,ends,head,tail


def viability(out,incoming,starts,ends,k):
    # j selected centers from start; t remaining (including current).
    f=[set(),set(starts)]
    s=[set(),set(ends)]
    for _ in range(2,k+1):
        f.append({q for p in f[-1] for q,_ in out[p]})
        s.append({p for q in s[-1] for p,_ in incoming[q]})
    h=[None]+[s[t] & f[k-t+1] for t in range(1,k+1)]
    return f,s,h


def optimal_dp(out,incoming,starts,ends,head,tail,h,k):
    if not all(h[1:]): return None
    d=[None]*(k+1)
    d[1]={p:(tail[p],1) for p in h[1]}
    for t in range(2,k+1):
        row={}
        for p in h[t]:
            vals=[(w+d[t-1][q][0],d[t-1][q][1])
                  for q,w in out[p] if q in d[t-1]]
            if vals:
                a=min(cost for cost,_ in vals)
                row[p]=(a,sum(count for cost,count in vals if cost==a))
        assert set(row)==h[t]
        d[t]=row
    roots=[(head[p]+d[k][p][0],d[k][p][1])
           for p in starts if p in d[k]]
    if not roots: return None
    best=min(cost for cost,_ in roots)
    ways=sum(count for cost,count in roots if cost==best)
    a=[None]*(k+1)
    a[1]={p:head[p] for p in h[k]}
    for j in range(2,k+1):
        t=k-j+1
        a[j]={q:min(a[j-1][p]+w for p,w in incoming[q] if p in a[j-1])
              for q in h[t]}
    opt_support=[None]+[{p for p in h[t] if a[k-t+1][p]+d[t][p][0]==best}
                        for t in range(1,k+1)]
    return best,ways,d,opt_support


def rank(center,graph,h,dp):
    out,incoming,starts,ends,head,tail=graph
    k=len(center);best,ways,d,_=dp
    rr=sum(d[k][p][1] for p in starts if p<center[0] and p in d[k]
           and head[p]+d[k][p][0]==best)
    for i,(p,q) in enumerate(zip(center,center[1:])):
        t=k-i
        assert p in d[t] and q in d[t-1]
        assert any(v==q and w+d[t-1][v][0]==d[t][p][0]
                   for v,w in out[p] if v in d[t-1])
        rr+=sum(d[t-1][v][1] for v,w in out[p] if v<q and v in d[t-1]
                and w+d[t-1][v][0]==d[t][p][0])
    return rr


def check():
    x,center=original_r5();k=len(center);r=2
    graph=make_graph(x,r)
    out,incoming,starts,ends,head,tail=graph
    f,s,h=viability(out,incoming,starts,ends,k)
    dp=optimal_dp(*graph,h,k)
    best,ways,d,opts=dp
    assert sum(len(q) for q in out)==4383
    assert sum(map(len,s[1:]))==83813
    assert sum(map(len,f[1:]))==74967
    assert sum(map(len,h[1:]))==734
    assert sum(map(len,opts[1:]))==620
    assert (best,ways,rank(center,graph,h,dp))==(
        1070,1338767625695954932334592000,417027933051277583800994379)
    assert all(len(a)==max(a)-min(a)+1 for a in h[1:])
    cases=0
    for n in range(1,6):
        for increments in product((1,2,3),repeat=n):
            z=[0]
            for delta in increments: z.append(z[-1]+delta)
            for rad in range(4):
                for kk in range(1,len(z)+1):
                    g=make_graph(z,rad)
                    ff,ss,hh=viability(g[0],g[1],g[2],g[3],kk)
                    result=optimal_dp(*g,hh,kk)
                    full=[]
                    for subset in combinations(range(len(z)),kk):
                        ds=[min(abs(z[p]-z[q]) for q in subset)
                            for p in range(len(z))]
                        if max(ds)<=rad: full.append(sum(ds))
                    if not full: assert result is None
                    else:
                        assert result is not None
                        actual=min(full)
                        assert (result[0],result[1])==(actual,full.count(actual))
                        for t in range(1,kk+1):
                            j=kk-t
                            brute={subset[j]
                                   for subset in combinations(range(len(z)),kk)
                                   if all(min(abs(z[p]-z[q]) for q in subset)<=rad
                                          for p in range(len(z)))}
                            assert brute==hh[t]
                    cases+=1
    result={'PASS':True,'small_cases':cases,'bounds':len(x),'events':x[-1],
            'centers':k,'radius':r,'edges':sum(map(len,out)),
            'backward_cells':sum(map(len,s[1:])),
            'forward_cells':sum(map(len,f[1:])),
            'bidirectional_cells':sum(map(len,h[1:])),
            'optimal_support_cells':sum(map(len,opts[1:])),
            'min_cost':best,'optimal_count':str(ways),
            'rank':str(rank(center,graph,h,dp))}
    print(result)


if __name__=='__main__': check()
