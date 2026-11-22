#!/usr/bin/env python3
"""Exact author census of p13, order 8 split (2,6); run start end first-side indices."""
from fractions import Fraction as F
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from math import floor, prod
import hashlib, sys, json, time
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
A=[[int(i==j) for j in range(N)] for i in range(N)]
for k in range(1,7):
    mod=P**k
    h=[pow(r,-k,mod) for r in range(1,P)]
    v=[sum(x*y for x,y in zip(row,h))%mod for row in A]
    pivot=next(i for i,x in enumerate(v) if x%P)
    inv=pow(v[pivot],-1,mod)
    old=A[pivot]
    A=[[mod*a for a in row] if i==pivot else [a-((v[i]*inv)%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
M=Matrix(A)
assert abs(M.det())==P**21
R=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=R*Matrix.diag(*(F(1,w) for w in W))
UI=U.inv()
assert all(x.q==1 for x in U)
assert abs(R.det())==P**21*prod(W)
G=R*R.T
mu=[[F(0) for _ in range(N)] for _ in range(N)]
D=[]
for i in range(N):
    for j in range(i):
        mu[i][j]=(F(int(G[i,j]))-sum(mu[i][a]*mu[j][a]*D[a] for a in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D)
assert dmin==F(78577530278042129705264382752517501995032553011464356025,4243983974238642688103181306691645151538473248349)
assert dmin>2*CAP*CAP
basis=[[int(U[j,t]) for t in range(N)] for j in range(N)]

def particular(q,r):
    u=[0]*N
    Q=[[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,7):
        mod=P**k
        h=[pow(j,-k,mod) for j in range(1,P)]
        res=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(u,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in Q]
        piv=next(i for i,x in enumerate(v) if x%P)
        inv=pow(v[piv],-1,mod)
        u=[a+((res*inv)%mod)*b for a,b in zip(u,Q[piv])]
        old=Q[piv]
        Q=[[mod*x for x in row] if i==piv else [a-((v[i]*inv)%mod)*b for a,b in zip(row,old)] for i,row in enumerate(Q)]
    for k in range(1,7):
        mod=P**k
        assert (sum(x*pow(j,-k,mod) for j,x in enumerate(u,1))+pow(P*q+r,-k,mod))%mod==0
    return u

atom_c={}
for q in range(1,7):
    for r in range(1,P):
        v=Matrix(1,N,particular(q,r))*UI
        atom_c[(q,r)]=tuple(F(x) for x in v)

def parts(n,low=1):
    if n==0:yield ()
    for q in range(low,n+1):
        for tail in parts(n-q,q):yield(q,)+tail

def rosters(k):
    if k==0:return[()]
    out=[]
    for pattern in parts(k):
        def rec(i,cur):
            if i==len(pattern):
                out.append(tuple(cur));return
            low=cur[-1][1] if i and pattern[i]==pattern[i-1] else 1
            for r in range(low,P):rec(i+1,cur+[(pattern[i],r)])
        rec(0,[])
    return sorted(out)

def info(s):
    cost=sum(P*(P*q+r)-1 for q,r in s)
    cc=tuple(sum((atom_c[z][j] for z in s),F(0)) for j in range(N))
    return(cost,cc,set(s))
L=rosters(2);R=rosters(6)
assert len(L)==90 and len(R)==42614
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
end=int(sys.argv[2]) if len(sys.argv)>2 else 1
assert 0<=start<end<=len(L)
right=[(s,*info(s)) for s in R]
left=[(s,*info(s)) for s in L[start:end]]
ct={k:0 for k in ('raw','common_cancelled','vert_over_cap','evaluated','nodes','sphere_leaves','budget_valid')}
leaves=[]
digest=hashlib.sha256();t0=time.monotonic()
for pos,cp,vp,sp in left:
    for neg,cn,vn,sn in right:
        ct['raw']+=1
        digest.update(str((pos,neg)).encode('ascii')+b'\n')
        if not sp.isdisjoint(sn):ct['common_cancelled']+=1;continue
        if cp>CAP or cn>CAP:ct['vert_over_cap']+=1;continue
        ct['evaluated']+=1
        c=[x-y for x,y in zip(vp,vn)]
        radius=(CAP-cp)**2+(CAP-cn)**2
        assert radius<dmin
        z=c[:];n=[0]*N
        def search(i,spent):
            if i<0:
                ct['sphere_leaves']+=1
                u=[sum((c[j]+n[j])*basis[j][t] for j in range(N)) for t in range(N)]
                assert all(x.denominator==1 for x in u)
                u=[int(x) for x in u]
                masses=(cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u)))
                ct['budget_valid']+=int(max(masses)<=CAP)
                for k in range(1,7):
                    mod=P**k
                    assert (sum(x*pow(r,-k,mod) for r,x in enumerate(u,1))
                            +sum(pow(P*q+r,-k,mod) for q,r in pos)
                            -sum(pow(P*q+r,-k,mod) for q,r in neg))%mod==0
                leaves.append({'plus':pos,'minus':neg,'u':u,'masses':masses,'radius_sq':radius})
                return
            ct['nodes']+=1
            center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
            near=floor(-center)
            for ni in (near,near+1):
                new=spent+D[i]*(center+ni)**2
                if new<=radius:
                    z[i]=c[i]+ni;n[i]=ni
                    search(i-1,new)
            z[i]=c[i]
        search(N-1,F(0))
    print('completed left',pos,'elapsed',round(time.monotonic()-t0,2),'counts',ct,flush=True)
result={'schema':'T6_P13_Q8_SPLIT2_6_AUTHOR_EXACT_PARTIAL_V1','status':'AUTHOR_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED','scope':{'first_side_range':[start,end],'first_side_total':90,'second_side_total':len(R),'frozen_each_side_cap':CAP,'p':P,'vertical_total':8,'split':[2,6]},'lattice_index':str(P**21),'lattice_min_gs_sq':str(dmin),'checks':ct,'ordered_pairs_sha256':digest.hexdigest(),'relaxed_leaves':leaves,'unvisited_first_side_range':[end,90]}
print(json.dumps(result,ensure_ascii=False,default=str),flush=True)
