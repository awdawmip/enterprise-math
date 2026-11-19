"""R004 finite graph-column measurements and independent exact decision checks."""
import argparse
import json
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import combinations,product
from math import prod
from pathlib import Path


def val(a,p,k):
    if not a:return k
    i=0
    while a%p==0:
        a//=p;i+=1
    return i


def log_span(rows,p,k):
    m=p**k
    rows=[[v%m for v in row] for row in rows]
    z=0
    while rows and rows[0]:
        h,i,j=min((val(v,p,k),i,j) for i,row in enumerate(rows) for j,v in enumerate(row))
        if h==k:break
        rows[0],rows[i]=rows[i],rows[0]
        for row in rows:row[0],row[j]=row[j],row[0]
        d=p**h
        mult=pow(rows[0][0]//d,-1,m)
        pivot=[v*mult%m for v in rows[0]]
        rows=[[(a-r[0]//d*b)%m for a,b in zip(r[1:],pivot[1:])] for r in rows[1:]]
        z+=k-h
    return z


def fiber(x,u,v,exps,p):
    return max(e-val((a-sum(t*z[j] for t,z in zip(u,x)))%p**e,p,e)
               for j,(a,e) in enumerate(zip(v,exps)))


def smith_check(p,exps,s,limit,domains=None):
    domains=domains or [max(exps)]*s
    k=max(exps+domains);r=p**k;t=len(exps)
    g=list(product(*[range(p**e) for e in exps]))
    possible=[[z for z in g if all(p**a*y%p**e==0 for e,y in zip(exps,z))] for a in domains]
    nstates=prod(map(len,possible))
    trials=0;first=None
    for ix,x in enumerate(product(*possible)):
        for iu,u in enumerate(product(*(range(p**a) for a in domains))):
            for iv,v in enumerate(g):
                if limit and (ix*13+iu*5+iv)%limit:continue
                A=[[p**(k-domains[i])*int(i==j) for j in range(s)]+[0]*t+[p**(k-domains[i])*u[i]] for i in range(s)]
                B=[[z[j] for z in x]+[(p**e if z==j else 0) for z in range(t)]+[v[j]] for j,e in enumerate(exps)]
                baseline=log_span([row[:-1] for row in A+B],p,k)-log_span([row[:-1] for row in A],p,k)
                delta=log_span(A+B,p,k)-log_span(A,p,k)-baseline
                assert delta==fiber(x,u,v,exps,p)
                assert baseline==sum(k-e for e in exps)
                if first is None and delta and any(any(z) for z in x) and any(u):
                    first=dict(A=A,B=B,prior_delta=baseline,increment=delta)
                trials+=1
    return dict(p=p,exps=exps,s=s,domains=domains,graph_count=nstates,smith_checks=trials,example=first)


def exhaustive(p,exps,s,domains=None,binary=False):
    domains=domains or [max(exps)]*s
    k=max(exps+domains)
    g=list(product(*[range(p**e) for e in exps]))
    possible=[[z for z in g if all(p**a*y%p**e==0 for e,y in zip(exps,z))] for a in domains]
    xs=list(product(*possible))
    fine=(1<<len(xs))-1
    tests=set()
    for u in product(*(range(p**a) for a in domains)):
        for v in g:
            parts={}
            for i,z in enumerate(xs):
                d=fiber(z,u,v,exps,p)
                if binary:d=int(d>0)
                parts[d]=parts.get(d,0)|(1<<i)
            if len(parts)>1:tests.add(tuple(sorted(parts.values())))
    tests=sorted(tests)
    @cache
    def worst(mask):
        if mask.bit_count()<=1:return 0
        ans=mask.bit_count()-1
        for test in tests:
            terms=[mask&z for z in test if mask&z]
            if len(terms)>1:
                ans=min(ans,1+max(worst(c) for c in terms))
        return ans
    edges=list(combinations(range(len(xs)),2))
    misses=[]
    for test in tests:
        unseen=sum(1<<j for j,(a,b) in enumerate(edges) if any((x>>a)&(x>>b)&1 for x in test))
        misses.append(unseen)
    @cache
    def separable(bits,budget):
        if not bits:return True
        if not budget:return False
        edge=(bits&-bits).bit_length()-1
        return any(separable(bits&x,budget-1) for x in misses if not x>>edge&1)
    al=worst(fine)
    bl=next(b for b in range(al,len(xs)) if separable((1<<len(edges))-1,b))
    h=[sum(e>=j for e in exps) for j in range(1,k+1)]
    assert al==sum((p**t-1)*sum(a>=j for a in domains) for j,t in enumerate(h,1))
    if binary and s == 1:
        assert bl == len(xs) - 1
    if not binary:
        assert bl==sum(len(slot)-len(slot)//p**h[0] for slot in possible)
    return dict(p=p,exps=exps,s=s,domains=domains,binary=binary,graphs=len(xs),distinct_tests=len(tests),
                adaptive_optimum=al,batch_optimum=bl,decision_masks=worst.cache_info().currsize,
                batch_cover_states=separable.cache_info().currsize)


def rounds(branch,limit):
    # branch[j-1] is the number of children at order p^j, bottom first.
    hmax=len(branch)
    size=lambda h,c: (1 if h==0 else c*prod(branch[:h-1])) if c else 0
    inf=10**20
    @cache
    def C(r,h,c):
        if size(h,c)<=1:return 0
        if r==0:return inf
        bound=size(h,c)-1
        return min(t+P(r-1,h,c,t) for t in range(bound+1))
    @cache
    def P(r,h,c,t):
        if C(r,h,c)<=t:return 0
        b=max(i for i in range(c) if C(r,h,i)<=t)
        ni=1 if h==1 else max(1,P(r,h-1,branch[h-2],t))
        return (c-b)*ni
    out=[C(r,hmax,branch[-1]) for r in range(1,limit+1)]
    assert out[0]==prod(branch)*(branch[0]-1)//branch[0]
    assert out[-1]==sum(q-1 for q in branch)
    return out


def brute_rounds(branch,R):
    # Direct simultaneous tests of full addresses in each parent state.
    labels=list(product(*(range(d) for d in branch[::-1])))
    dist=[[next((len(branch)-i for i,(a,b) in enumerate(zip(x,y)) if a!=b),0)
           for y in labels] for x in labels]
    @cache
    def solve(candidates,r):
        if len(candidates)<=1:return 0
        if r==0:return 10**9
        best=len(candidates)-1
        for m in range(1,best):
            for batch in combinations(candidates,m):
                parts={}
                for x in candidates:
                    row=tuple(dist[x][y] for y in batch)
                    parts.setdefault(row,[]).append(x)
                opt=m+max(solve(tuple(g),r-1) for g in parts.values())
                best=min(best,opt)
        return best
    result=[solve(tuple(range(len(labels))),i) for i in range(1,R+1)]
    assert result==rounds(branch,1+sum(d-1 for d in branch))[:R]
    return dict(children=branch,raw_minimax=result,cache=solve.cache_info().currsize)


def depth_distribution(branch):
    dist=Counter(min(j,branch[0]-1) for j in range(1,branch[0]+1))
    for d in branch[1:]:
        nxt=Counter()
        for k,n in dist.items():
            for i in range(d):nxt[k+i]+=n
        dist=nxt
    return dict(histogram=dict(sorted(dist.items())),mean=str(Fraction(sum(k*n for k,n in dist.items()),prod(branch))))


def main():
    parse=argparse.ArgumentParser()
    parse.add_argument('--out',type=Path)
    args=parse.parse_args()
    asym=[(2,[2],2),(2,[1,1],2),(3,[1],2),(2,[2,1],1),(2,[3,1],1),(3,[2],1),(2,[2,1],1,None,True),(2,[2,1],2,[1,2]),(2,[2,1],2,[1,2],True)]
    numeric=[exhaustive(*t) for t in asym]
    data=dict(exact_decision_checks=numeric,small_batch_bruteforce=[brute_rounds([2,2,2],3),brute_rounds([3,3],3)],
              matrix_checks=[smith_check(*z) for z in [(2,[2],2,1),(2,[1,1],2,1),(2,[2,1],2,9),(3,[2],2,29),(2,[2,2],2,101),(2,[2,1],2,1,[1,2])]],
              rounds_and_depth=[dict(children=d,costs=rounds(d,1+sum(q-1 for q in d)),**depth_distribution(d))
                                for d in ([2,2,2,2],[4,4],[4,2,2],[3,3,3],[4,4,2])])
    doc=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.out:args.out.write_text(doc)
    else:print(doc,end='')


if __name__=='__main__':
    main()
