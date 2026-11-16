#!/usr/bin/env python3
"""Exact finite checks of the R215 principal-ideal counting formulas.
Pure Python standard library; no floating point. The test is for the
paired-event observer algebra, not for native physical BRC dynamics.
"""
from collections import deque
from math import comb
import json


def stirling2(n, j):
    if j < 0 or j > n: return 0
    row=[1]
    for x in range(1,n+1):
        new=[0]*(x+1)
        for y in range(1,x+1):
            new[y]=(y*row[y] if y<len(row) else 0)+(row[y-1] if y-1<len(row) else 0)
        row=new
    return row[j]


def W(m,r,L):
    from math import factorial
    return factorial(r)*m**L * sum(stirling2(L+1,j+1) for j in range(min(r,L)+1))


def T(m,k,L,r):
    return sum(comb(k-r,j-r)*W(m,j,L) for j in range(r,k+1))


def avoid_counts(alphabet,pattern,L):
    """Number of pattern-avoiding words of each length < L, KMP DFA."""
    h=len(pattern)
    if h==0: return [0]*L
    pi=[0]*h
    for i in range(1,h):
        j=pi[i-1]
        while j and pattern[i]!=pattern[j]: j=pi[j-1]
        if pattern[i]==pattern[j]: j+=1
        pi[i]=j
    nxt=[]
    for p in range(h):
        row=[]
        for c in alphabet:
            q=p
            while q and pattern[q]!=c: q=pi[q-1]
            if pattern[q]==c: q+=1
            row.append(q)
        nxt.append(row)
    dp=[0]*h; dp[0]=1
    out=[]
    for _ in range(L):
        out.append(sum(dp))
        new=[0]*h
        for p,v in enumerate(dp):
            if v:
                for q in nxt[p]:
                    if q<h: new[q]+=v
        dp=new
    return out


def ideal_counts(m,k,L,state):
    order,tail=state; r=len(order); a=m*(k+1)
    t=T(m,k,L,r)
    if len(tail)==L: return t,t
    h=len(tail)
    right=sum(a**(n-h) for n in range(h,L))+t
    if not h: return right,right
    alphabet=tuple((d,s) for d in range(m) for s in range(k+1))
    avoid=avoid_counts(alphabet,tail,L)
    two=sum(a**n-avoid[n] for n in range(L))+t
    return right,two


def append(st,e,L):
    old,tail=st
    tag=e[1]
    if tag:
        old=tuple(x for x in old if x!=tag)+(tag,)
    return old,(tail+(e,))[-L:]


def finite_monoid(m,k,L):
    alphabet=tuple((d,s) for d in range(m) for s in range(k+1))
    empty=((),())
    reps={empty:()}; q=deque([empty])
    while q:
        s=q.popleft()
        for e in alphabet:
            t=append(s,e,L)
            if t not in reps:
                reps[t]=reps[s]+(e,);q.append(t)
    return list(reps),reps


def check_model(m,k,L):
    states,reps=finite_monoid(m,k,L)
    ix={s:i for i,s in enumerate(states)}; n=len(states)
    mult=[]
    for s in states:
        row=[]
        for t in states:
            z=s
            for e in reps[t]: z=append(z,e,L)
            row.append(ix[z])
        mult.append(row)
    checks=0
    for i,s in enumerate(states):
        right=set(mult[i])
        two={mult[p][z] for p in range(n) for z in right}
        nr,nt=ideal_counts(m,k,L,s)
        assert (len(right),len(two))==(nr,nt),(m,k,L,s,len(right),len(two),nr,nt)
        checks+=1
    expected=sum((m*(k+1))**h for h in range(L))+sum(comb(k,r)*W(m,r,L) for r in range(k+1))
    assert n==expected,(m,k,L,n,expected)
    return {'m':m,'k':k,'L':L,'states':n,'right_and_two_sided_ideals_exactly_checked':checks,'pairwise_products':n*n}


def main():
    specs=[(1,0,2),(1,1,2),(1,1,3),(1,1,4),(1,2,2),(1,2,3),(2,0,2),(2,1,2),(2,1,3),(2,2,2)]
    results=[check_model(*p) for p in specs]
    a=(1,1,4)
    aa=( (1,), ((0,1),(0,1)) )
    ab=( (1,), ((0,1),(0,0)) )
    assert ideal_counts(*a,aa)==(19,20),ideal_counts(*a,aa)
    assert ideal_counts(*a,ab)==(19,21),ideal_counts(*a,ab)
    evidence={'schema':'R215_EXACT_CHECK_V1','result':'PASS','models':results,'total_states_checked':sum(r['states'] for r in results),'pairwise_products':sum(r['pairwise_products'] for r in results),'witness':{'m':1,'k':1,'L':4,'pattern_11':{'right_ideal':19,'two_sided_ideal':20},'pattern_10':{'right_ideal':19,'two_sided_ideal':21}},'scope':'Complete enumeration of specified finite J monoids; symbolic proof separate. Exact nonnegative integers only.'}
    print(json.dumps(evidence,indent=2,ensure_ascii=False))
    with open('/mnt/data/R215_verification.json','w') as f:json.dump(evidence,f,indent=2,ensure_ascii=False)
if __name__=='__main__':main()
