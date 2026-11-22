#!/usr/bin/env python3
"""Replay author-level, bounded maximal-p13 T6 order8 finite census.
Usage: python T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py 0 8 0 10000
Args are (positive_vertical_order,negative_vertical_order,start,end), with
slices of the first side's canonical sorted full named roster. Every slice is
closed only after the process finishes; no unvisited slice can be marked EMPTY.
Exact SymPy/Fraction arithmetic, no native authorization or reviewer status.
"""
import importlib.util, itertools, json, math, sys, hashlib
from pathlib import Path
from fractions import Fraction as F
from sympy import Matrix
p=Path(__file__).with_name("T6_P13_Q2_ALL_SPLITS_GLOBAL_AFFINE_CHECK_20261123.py")
s=importlib.util.spec_from_file_location("t6_p13_q2",p)
prior=importlib.util.module_from_spec(s);s.loader.exec_module(prior)
P,CAP,N,W,U,UI=prior.P,prior.CAP,prior.N,prior.W,prior.U,prior.UI
mu,D,dmin=prior.mu,prior.D,prior.dmin
assert dmin>2*CAP*CAP
assert len(sys.argv)==5, "usage: script.py a b start end"
a,b,start,end=map(int,sys.argv[1:])
assert a+b==8 and a<=b and a>=0 and 0<=start<=end
atom={}
for q in range(1,9):
    for r in range(1,P):
        v=Matrix(1,N,prior.prior.particular(q,r))*UI
        atom[(q,r)]=tuple(F(x) for x in v)
def parts(n,low=1):
    if n==0:yield ()
    for q in range(low,n+1):
        for tail in parts(n-q,q):yield (q,)+tail
def rosters(k):
    if k==0:return [()]
    out=[]
    for pattern in parts(k):
        def rec(i,cur):
            if i==len(pattern):
                out.append(tuple(cur));return
            low=cur[-1][1] if i and pattern[i]==pattern[i-1] else 1
            for r in range(low,P):rec(i+1,cur+[(pattern[i],r)])
        rec(0,[])
    return sorted(out)
known={0:1,1:12,2:90,3:520,4:2535,5:10908,6:42614,7:153960,8:521235}
L=rosters(a);R=rosters(b)
assert len(L)==known[a] and len(R)==known[b] and end<=len(L)
def info(s):
    return (sum(P*(P*q+r)-1 for q,r in s),
            [sum(atom[z][j] for z in s) for j in range(N)],set(s))
left={s:info(s) for s in L[start:end]}
right=None  # stream second-side coordinates instead of allocating 521235 vectors
basis=[[int(U[j,t]) for t in range(N)] for j in range(N)]
count=dict(raw=0,common_cancelled=0,vert_over_cap=0,evaluated=0,
           nodes=0,sphere_leaves=0,budget_valid=0)
leaves=[];digest=hashlib.sha256()
for pos in L[start:end]:
    cp,vp,sp=left[pos]
    for neg in R:
        cn,vn,sn=info(neg)
        count["raw"]+=1
        # Stable exact source order digest, including discarded pairs.
        digest.update(str((pos,neg)).encode("ascii")+b"\n")
        if not sp.isdisjoint(sn):
            count["common_cancelled"]+=1;continue
        if cp>CAP or cn>CAP:
            count["vert_over_cap"]+=1;continue
        count["evaluated"]+=1
        c=[x-y for x,y in zip(vp,vn)]
        radius=(CAP-cp)**2+(CAP-cn)**2
        assert radius<dmin
        z=c[:];n=[0]*N
        def search(i,spent):
            if i<0:
                count["sphere_leaves"]+=1
                u=[sum((c[j]+n[j])*basis[j][t] for j in range(N)) for t in range(N)]
                assert all(x.denominator==1 for x in u)
                u=[int(x) for x in u]
                masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),
                        cn+sum(w*max(0,-x) for w,x in zip(W,u))]
                count["budget_valid"]+=int(max(masses)<=CAP)
                for k in range(1,7):
                    mod=P**k
                    assert (sum(x*pow(r,-k,mod) for r,x in enumerate(u,1))
                            +sum(pow(P*q+r,-k,mod) for q,r in pos)
                            -sum(pow(P*q+r,-k,mod) for q,r in neg))%mod==0
                leaves.append(dict(plus=pos,minus=neg,u=u,masses=masses,
                                   norm_sq=sum((w*x)**2 for w,x in zip(W,u)),
                                   radius_sq=radius))
                return
            count["nodes"]+=1
            center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
            near=math.floor(-center)
            for ni in (near,near+1):
                new=spent+D[i]*(center+ni)**2
                if new<=radius:
                    z[i]=c[i]+ni;n[i]=ni
                    search(i-1,new)
            z[i]=c[i]
        search(N-1,F(0))
print(json.dumps(dict(scope=dict(order=8,split=[a,b],first_side_range=[start,end],
                           first_side_total=len(L),second_side_total=len(R)),
                      counts=count,ordered_pairs_sha256=digest.hexdigest(),
                      relaxed_leaves=leaves,
                      scientific_status="AUTHOR_EXACT_FINITE_ONLY_UNREVIEWED_NOT_ADMITTED"),
                 ensure_ascii=False))
