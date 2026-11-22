#!/usr/bin/env python3
"""Author recheck of maximal-p13 total vertical orders 4,5,6 for frozen T6.
Run: python research_checks/T6_P13_Q4_Q6_AUTHOR_AFFINE_RECHECK_20261123.py 4
Requires sympy and the pinned q0/q1/q2 checkers in this directory.
Pure integer/Fraction computations. Not independent review or Native Result.
"""
import importlib.util, itertools, json, math, sys
from pathlib import Path
from fractions import Fraction as F
from sympy import Matrix
p=Path(__file__).with_name("T6_P13_Q2_ALL_SPLITS_GLOBAL_AFFINE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p13_q2",p)
prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
P,CAP,N,W,U,UI=prior.P,prior.CAP,prior.N,prior.W,prior.U,prior.UI
mu,D,dmin=prior.mu,prior.D,prior.dmin
assert dmin>2*CAP*CAP
order=int(sys.argv[1]) if len(sys.argv)>1 else 4
assert order in (4,5,6)
A={}
for q in range(1,order+1):
    for r in range(1,P):
        v=Matrix(1,N,prior.prior.particular(q,r))*UI
        A[(q,r)]=tuple(F(x) for x in v)
def partitions(n,minimum=1):
    if n==0:
        yield []
    for q in range(minimum,n+1):
        for tail in partitions(n-q,q):
            yield [q]+tail
def roster(k):
    if k==0:return [()]
    out=[]
    for part in partitions(k):
        def walk(i,cur):
            if i==len(part):
                out.append(tuple(cur));return
            low=cur[-1][1] if i and part[i]==part[i-1] else 1
            for r in range(low,P):walk(i+1,cur+[(part[i],r)])
        walk(0,[])
    assert len(out)==len(set(out))
    return sorted(out)
states={k:roster(k) for k in range(order+1)}
known={0:1,1:12,2:90,3:520,4:2535,5:10908,6:42614}
assert all(len(x)==known[k] for k,x in states.items())
def state_info(s):
    return (sum(P*(P*q+r)-1 for q,r in s),
            [sum(A[z][j] for z in s) for j in range(N)],set(s))
info={s:state_info(s) for pool in states.values() for s in pool}
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
splits={4:((0,4),(1,3),(2,2)),5:((0,5),(1,4),(2,3)),
        6:((0,6),(1,5),(2,4),(3,3))}[order]
result={};leaves=[]
for split in splits:
    a,b=split
    pairs=itertools.combinations(states[a],2) if a==b else itertools.product(states[a],states[b])
    count={'raw':0,'cancelled':0,'evaluated':0,'nodes':0,'sphere_leaves':0,'budget_valid':0}
    for plus,minus in pairs:
        count['raw']+=1
        cp,vp,sp=info[plus];cn,vn,sn=info[minus]
        if not sp.isdisjoint(sn):
            count['cancelled']+=1;continue
        if cp>CAP or cn>CAP:continue
        count['evaluated']+=1
        c=[x-y for x,y in zip(vp,vn)]
        radius=(CAP-cp)**2+(CAP-cn)**2
        assert radius<dmin
        z=c[:];n=[0]*N
        def rec(i,spent):
            if i<0:
                count['sphere_leaves']+=1
                u=[sum((c[j]+n[j])*Urows[j][t] for j in range(N)) for t in range(N)]
                assert all(x.denominator==1 for x in u)
                u=[int(x) for x in u]
                pm=cp+sum(w*max(0,x) for w,x in zip(W,u))
                nm=cn+sum(w*max(0,-x) for w,x in zip(W,u))
                good=pm<=CAP and nm<=CAP
                count['budget_valid']+=int(good)
                for k in range(1,7):
                    mod=P**k
                    assert (sum(x*pow(r,-k,mod) for r,x in enumerate(u,1))
                        +sum(pow(P*q+r,-k,mod) for q,r in plus)
                        -sum(pow(P*q+r,-k,mod) for q,r in minus))%mod==0
                leaves.append({'split':split,'plus':plus,'minus':minus,'u':u,'masses':[pm,nm],
                               'norm_sq':sum((w*x)**2 for w,x in zip(W,u)),
                               'radius_sq':radius})
                return
            count['nodes']+=1
            center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
            near=math.floor(-center)
            for ni in (near,near+1):
                nxt=spent+D[i]*(center+ni)**2
                if nxt<=radius:
                    z[i]=c[i]+ni;n[i]=ni;rec(i-1,nxt)
            z[i]=c[i]
        rec(N-1,F(0))
    result[str(split)]=count
expected={
4:((2535,0,2535,8803,1),(6240,1080,5160,16765,0),(4005,792,3213,10450,0)),
5:((10908,0,10908,34393,0),(30420,6240,24180,72758,0),(46800,12312,34488,100595,1)),
6:((42614,0,42614,130186,0),(130896,30420,100476,281443,2),
   (228150,70020,158130,423495,1),(134940,44496,90444,239594,2))}
for sp,ex in zip(splits,expected[order]):
    got=result[str(sp)]
    assert tuple(got[k] for k in ('raw','cancelled','evaluated','nodes','sphere_leaves'))==ex
    assert got['budget_valid']==0
print(json.dumps({'order':order,'splits':result,'relaxed_leaves':leaves,
                  'conclusion':'AUTHOR_EXACT_FINITE_EXCLUSION_UNREVIEWED_NOT_ADMITTED'},
                 ensure_ascii=False,default=str))
