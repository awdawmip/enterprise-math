#!/usr/bin/env python3
# Portable author extension of EM@64e28e47ca719fd7f8caa996b500aa79a12408dc:
# research_checks/T6_P13_Q12_GMP_REPLAY_20261125/t6_q12_exact_init.py
# Exact arithmetic, unchanged mixed congruences and side budget. Independent of native p17/D24.
from fractions import Fraction as F
from math import floor,comb,lcm
from itertools import combinations_with_replacement,groupby
from collections import Counter
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
import json,time,pathlib,hashlib
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
H=[[pow(r,-k,P**k) for r in range(1,P)] for k in range(1,7)]
def solve(target):
    x=[0]*N; A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k,h in enumerate(H,1):
        mod=P**k;t=(target[k-1]-sum(a*b for a,b in zip(x,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,y in enumerate(v) if y%P);inv=pow(v[piv],-1,mod);old=A[piv]
        x=[a+(t*inv%mod)*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
    assert all((sum(a*b for a,b in zip(x,h))-target[k-1])%P**k==0 for k,h in enumerate(H,1))
    return x,A
_,A=solve([0]*6);M=Matrix(A);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
assert abs(U.det())==P**21
assert all(sum(int(U[j,t])*h[t] for t in range(N))%P**k==0 for j in range(N) for k,h in enumerate(H,1))
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
# Include q=13, outside the old q<=12 lookup but in the same formula.
C0={(q,r):[F(x) for x in Matrix(1,N,solve([pow(P*q+r,-k,P**k) for k in range(1,7)])[0])*UI] for q in range(1,14) for r in range(1,13)}
C0={k:[x-floor(x) for x in v] for k,v in C0.items()}
B=lcm(*(x.denominator for v in C0.values() for x in v)); C={a:[int(x*B) for x in v] for a,v in C0.items()}
assert B==P**6
L=[lcm(*(mu[j][i].denominator for j in range(i+1,N))) for i in range(N)]
MM=[[int(mu[j][i]*L[i]) for j in range(i+1,N)] for i in range(N)]
K=[D[i]/(B*L[i])**2 for i in range(N)];Q=lcm(*(x.denominator for x in K));T=[int(x*Q) for x in K]
def patterns(total,low=1):
    if total==0:
        yield ();return
    for q in range(low,total+1):
        for tail in patterns(total-q,q):yield (q,)+tail
# Every feasible roster has sum of labels <= floor((CAP-169*13+len(pat))/13).
# Pruned generator uses only the positivity lower bound for labels still unassigned.
def feasible(pat,limit):
    def walk(rs,s):
        i=len(rs)
        if i==len(pat):yield tuple(zip(pat,rs));return
        lo=rs[-1] if i and pat[i]==pat[i-1] else 1
        hi=min(12,limit-s-(len(pat)-i-1))
        for a in range(lo,hi+1):yield from walk(rs+(a,),s+a)
    yield from walk((),0)
def count_dp(pat,limit):
    d=Counter({0:1});raw=1
    for m in Counter(pat).values():
        raw*=comb(11+m,m)
        # independent group-polynomial recursion: count multiplicity of each label, truncate degree
        g=Counter({(0,0):1})
        for t in range(1,13):
            h=Counter()
            for (k,s),v in g.items():
                for n in range(m-k+1):
                    if s+t*n<=limit:h[k+n,s+t*n]+=v
            g=h
        h=Counter()
        for s,v in d.items():
            for (k,t),n in g.items():
                if k==m and s+t<=limit:h[s+t]+=v*n
        d=h
    return raw,sum(d.values())
def search(neg):
    cn=sum(P*(P*q+r)-1 for q,r in neg);assert cn<=CAP
    radius=CAP**2+(CAP-cn)**2;bound=Q*radius
    c=[sum(C[a][i] for a in neg)%B for i in range(N)];z=c.copy();nodes=0;witness=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg))%(P**k) for k in range(1,7)];assert residues==[0]*6
            norm=sum((w*x)**2 for w,x in zip(W,u));assert norm<=radius and all((a-b)%B==0 for a,b in zip(z,c));assert spent==Q*norm
            masses=[sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            witness.append(dict(pos=[],neg=neg,z=z.copy(),u=u,residues=residues,norm_sq=norm,radius_sq=radius,masses=masses,budget_valid=max(masses)<=CAP));return
        nodes+=1
        h=L[i]*c[i]+sum(a*b for a,b in zip(MM[i],z[i+1:]))
        step=B*L[i];near=(-h)//step
        # The exact GS lower bound gives interval radius < one step, so only these two integers can lie inside.
        for n in (near,near+1):
            e=spent+T[i]*(h+step*n)**2
            if e<=bound:z[i]=c[i]+B*n;descend(i-1,e)
        z[i]=c[i]
    descend(N-1,0);return nodes,witness
start=time.perf_counter();rows=[]
for pat in patterns(13):
    limit=(CAP-169*13+len(pat))//13
    raw,n=count_dp(pat,limit);ws=[];nodes=0;seen=0
    for neg in feasible(pat,limit):
        seen+=1;nn,ww=search(neg);nodes+=nn;ws.extend(ww)
    assert seen==n
    rows.append(dict(pos_pattern=[],neg_pattern=pat,raw=raw,over=raw-n,search=n,nodes=nodes,leaves=len(ws),valid=sum(w['budget_valid'] for w in ws),witnesses=ws))
    if rows[-1]['valid']:print('CANDIDATE',rows[-1],flush=True)
totals={k:sum(r[k] for r in rows) for k in ('raw','over','search','nodes','leaves','valid')}
assert len(rows)==101
out=dict(schema='T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',source_initializer_blob='1097ff3a84242ea2c9347912697205f9681d8448',source_kernel_blob='bf7b072282e76be4f8dfb4605145c51bf3f52d46',p=P,valuation=1,total_q=13,split=[0,13],budget=CAP,gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,U=Urows,rows=rows,totals=totals,program_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED',scope='Six mixed congruences and both independent budgets; H0 and lower prime completion not implied; no formal claim or protected progress.')
pathlib.Path(__file__).with_name('T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print('RESULT',totals,'rows',len(rows),'dmin',dmin,'seconds',time.perf_counter()-start)
