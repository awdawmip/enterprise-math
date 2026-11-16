#!/usr/bin/env python3
"""R214 exact quotient and grouped-rank checks.
Standard library only. No native BRC evolution is performed.
Tests prove the stated finite coverage; general theorems have separate proofs.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial
from collections import deque
import json, random

@lru_cache(None)
def S(n,j):
    if j<0 or j>n:return 0
    if n==j==0:return 1
    if n==0:return 0
    return S(n-1,j-1)+j*S(n-1,j)

@lru_cache(None)
def C(r,L):
    return sum(S(L+1,j+1) for j in range(min(r,L)+1))

def fall(k,r):
    z=1
    for i in range(r):z*=k-i
    return z

def B(m,k,L):
    a=m*(k+1)
    return sum(a**h for h in range(L))

def total(m,k,L):
    return B(m,k,L)+m**L*sum(fall(k,r)*C(r,L) for r in range(k+1))

def state(w,L):
    s=()
    for d,p in w:
        if p:s=tuple(x for x in s if x!=p)+(p,)
    return (s,tuple(w[-L:]))

def compose(x,y,L):
    s1,t1=x;s2,t2=y
    s=tuple(p for p in s1 if p not in s2)+s2
    return (s,tuple((t1+t2)[-L:]))

def mask(tags):
    ans=0
    for p in tags:
        if p:ans |= 1<<(p-1)
    return ans

def qstate(x,L):
    s,t=x
    if len(t)<L:return ('short', t)
    return ('full',mask(s))

def qprod(x,y,L):
    if x[0]=='short' and y[0]=='short' and len(x[1])+len(y[1])<L:
        return ('short',x[1]+y[1])
    return ('full', (mask(p for _,p in x[1]) if x[0]=='short' else x[1]) |
                    (mask(p for _,p in y[1]) if y[0]=='short' else y[1]))

def qR(x,z):
    if x[0]=='full':return z[0]=='full' and (x[1]&z[1])==x[1]
    if z[0]=='full':return (mask(p for _,p in x[1])&z[1])==mask(p for _,p in x[1])
    return z[1][:len(x[1])]==x[1]

def qJ(x,z):
    if x[0]=='full':return z[0]=='full' and (x[1]&z[1])==x[1]
    if z[0]=='full':return (mask(p for _,p in x[1])&z[1])==mask(p for _,p in x[1])
    u=x[1];v=z[1]
    return any(v[i:i+len(u)]==u for i in range(len(v)-len(u)+1))

def digit_rank(xs,b):
    v=0
    for x in xs:v=v*b+x
    return v

def digit_unrank(z,b,n):
    out=[0]*n
    for i in range(n-1,-1,-1):z,out[i]=divmod(z,b)
    assert not z
    return tuple(out)

@lru_cache(None)
def suffix_dp(L,j):
    f=[[0]*(j+1) for _ in range(L+1)]
    f[0][j]=1
    for t in range(1,L+1):
        for h in range(j+1):
            f[t][h]=(h+1)*f[t-1][h]+(f[t-1][h+1] if h<j else 0)
    return f

def allowed(s,j,h):
    seen=list(s[len(s)-h:]) if h else []
    if h<j:seen.append(s[-h-1])
    return tuple(sorted((0,*seen)))

def hnext(x,s,j,h):
    return h+1 if h<j and x==s[-h-1] else h

def prov_rank(s,L,ps):
    j=len(set(ps)-{0})
    assert j<=min(L,len(s))
    offset=sum(S(L+1,v+1) for v in range(j))
    f=suffix_dp(L,j);h=0
    for i,p in enumerate(reversed(ps)):
        cand=allowed(s,j,h)
        assert p in cand
        for v in cand:
            if v>=p:break
            offset+=f[L-i-1][hnext(v,s,j,h)]
        h=hnext(p,s,j,h)
    assert h==j
    return offset

def prov_unrank(s,L,z):
    for j in range(min(L,len(s))+1):
        v=S(L+1,j+1)
        if z<v:break
        z-=v
    else:raise AssertionError('bad provenance offset')
    f=suffix_dp(L,j);h=0;rev=[]
    for i in range(L):
        for p in allowed(s,j,h):
            hh=hnext(p,s,j,h);v=f[L-i-1][hh]
            if z>=v:z-=v
            else:rev.append(p);h=hh;break
        else:raise AssertionError('no branch')
    assert z==0 and h==j
    return tuple(reversed(rev))

# Colexicographic subsets: rank(U) = sum_{i=1}^r binom(U_i-1,i).
def subset_rank(U):
    return sum(comb(v-1,i) for i,v in enumerate(U,start=1))

def subset_unrank(z,k,r):
    ans=[0]*r;maxv=k-1
    for i in range(r,0,-1):
        v=maxv
        while v>=i and comb(v,i)>z:v-=1
        assert v>=i-1
        ans[i-1]=v+1
        z-=comb(v,i) if v>=i else 0
        maxv=v-1
    assert z==0
    return tuple(ans)

def perm_rank(s,U):
    rem=list(U);z=0
    for i,v in enumerate(s):
        pos=rem.index(v)
        z+=pos*factorial(len(s)-i-1)
        rem.pop(pos)
    return z

def perm_unrank(z,U):
    rem=list(U);out=[]
    for i in range(len(U)):
        fact=factorial(len(U)-i-1)
        v,z=divmod(z,fact)
        out.append(rem.pop(v))
    assert z==0
    return tuple(out)

def grouped_rank(st,m,k,L):
    s,t=st;a=m*(k+1)
    if len(t)<L:
        assert state(t,L)[0]==s
        return sum(a**j for j in range(len(t)))+digit_rank([d*(k+1)+p for d,p in t],a)
    r=len(s);U=tuple(sorted(s));v=m**L*C(r,L)
    offset=B(m,k,L)+sum(comb(k,i)*factorial(i)*m**L*C(i,L) for i in range(r))
    pv=prov_rank(s,L,tuple(p for _,p in t))
    dirs=digit_rank([d for d,p in t],m)
    return offset+subset_rank(U)*factorial(r)*v+perm_rank(s,U)*v+pv*m**L+dirs

def grouped_unrank(z,m,k,L):
    assert 0<=z<total(m,k,L)
    a=m*(k+1)
    for h in range(L):
        if z<a**h:
            digits=digit_unrank(z,a,h)
            t=tuple(divmod(v,k+1) for v in digits)
            return state(t,L)
        z-=a**h
    for r in range(k+1):
        v=m**L*C(r,L)
        block=comb(k,r)*factorial(r)*v
        if z<block:break
        z-=block
    else:raise AssertionError('no group')
    sr,z=divmod(z,factorial(r)*v)
    U=subset_unrank(sr,k,r)
    pr,z=divmod(z,v)
    s=perm_unrank(pr,U)
    pv,d=divmod(z,m**L)
    ps=prov_unrank(s,L,pv)
    ds=digit_unrank(d,m,L)
    return (s,tuple(zip(ds,ps)))

def qcode_from_grouped_rank(z,m,k,L):
    b=B(m,k,L)
    if z<b:return z
    w=z-b
    for r in range(k+1):
        v=m**L*C(r,L);length=factorial(r)*v
        block=comb(k,r)*length
        if w<block:break
        w-=block
    else:raise AssertionError('range')
    U=subset_unrank(w//length,k,r)
    return b+mask(U)

def qcode_to_qstate(c,m,k,L):
    b=B(m,k,L)
    if c>=b:
        assert c<b+(1<<k)
        return ('full',c-b)
    a=m*(k+1)
    for h in range(L):
        if c<a**h:
            digits=digit_unrank(c,a,h)
            return ('short',tuple(divmod(v,k+1) for v in digits))
        c-=a**h
    raise AssertionError('bad code')

def reachable(m,k,L):
    alpha=tuple(product(range(m),range(k+1)))
    e=state((),L);seen={e};todo=deque([e])
    while todo:
        x=todo.popleft()
        for a in alpha:
            y=compose(x,state((a,),L),L)
            if y not in seen:seen.add(y);todo.append(y)
    return seen

def run():
    models=[(1,0,1),(1,1,1),(1,1,2),(2,1,2),(1,2,2),(2,2,2),(1,2,3),
            (2,0,3),(2,1,3),(1,3,2),(2,2,3)]
    report={'schema':'R214_GREEN_J_CONGRUENCE_AND_CODE_V1', 'status':'PASS',
            'arithmetic':'exact Python integers', 'model_results':[],
            'models':0,'rank_roundtrips':0,'homomorphism_tests':0,
            'ideal_pair_checks':0,'class_ideal_checks':0,'code_projection_checks':0}
    for m,k,L in models:
        st=sorted(reachable(m,k,L))
        n=total(m,k,L)
        assert len(st)==n,(m,k,L,len(st),n)
        seen=set();qlabels=set()
        for z in range(n):
            s=grouped_unrank(z,m,k,L)
            assert grouped_rank(s,m,k,L)==z
            q=qstate(s,L)
            assert qcode_to_qstate(qcode_from_grouped_rank(z,m,k,L),m,k,L)==q
            seen.add(s);qlabels.add(q)
            report['rank_roundtrips']+=1
            report['code_projection_checks']+=1
        assert seen==set(st)
        b=B(m,k,L)
        assert len(qlabels)==b+(1<<k)
        probes=st if n<=100 else st[:25]+st[-25:]
        for x in probes:
            for y in probes:
                assert qstate(compose(x,y,L),L)==qprod(qstate(x,L),qstate(y,L),L)
                report['homomorphism_tests']+=1
        if n<=100:
            for x in st:
                right={compose(x,v,L) for v in st}
                both={compose(u,y,L) for u in st for y in right}
                for z in st:
                    assert (z in right)==qR(qstate(x,L),qstate(z,L)),(m,k,L,x,z,'R')
                    assert (z in both)==qJ(qstate(x,L),qstate(z,L)),(m,k,L,x,z,'J')
                    report['ideal_pair_checks']+=2
                assert len({qstate(y,L) for y in both})==len({qstate(y,L) for y in st if qJ(qstate(x,L),qstate(y,L))})
                report['class_ideal_checks']+=1
        report['models']+=1
        report['model_results'].append({'m':m,'k':k,'L':L,'full_states':n,
            'quotient_states':b+(1<<k),'exhaustive_ideals':n<=100})
    m,k,L=12,6,2
    assert total(m,k,L)==1407685
    assert B(m,k,L)+(1<<k)==149
    rng=random.Random(214)
    samples=[0,1,2,83,84,85,86,total(m,k,L)//2,total(m,k,L)-1]
    samples += [rng.randrange(total(m,k,L)) for _ in range(3000)]
    for z in samples:
        st=grouped_unrank(z,m,k,L)
        assert grouped_rank(st,m,k,L)==z
        assert qcode_to_qstate(qcode_from_grouped_rank(z,m,k,L),m,k,L)==qstate(st,L)
        report['rank_roundtrips']+=1
        report['code_projection_checks']+=1
    report['x6']={'m':m,'k':k,'L':L,'full_states':total(m,k,L),
                  'green_J_classes':B(m,k,L)+(1<<k),
                  'optimal_full_action_bits':(total(m,k,L)-1).bit_length(),
                  'optimal_green_quotient_bits':(B(m,k,L)+(1<<k)-1).bit_length(),
                  'random_rank_samples':len(samples),
                  'full_support_class_interval_length_by_size':{
                      str(r):factorial(r)*m**L*C(r,L) for r in range(k+1)}}
    return report

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
