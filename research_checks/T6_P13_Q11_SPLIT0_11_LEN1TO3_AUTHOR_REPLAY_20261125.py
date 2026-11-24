#!/usr/bin/env python3
"""Exact replay for p13 q11 split(0,11), lengths 1--3.
Source kernel de78443d23578a66d3ae79f2a045e4be8e756c50.
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca.
"""
from fractions import Fraction as F
from math import floor, comb
from itertools import product, combinations_with_replacement, groupby
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from collections import Counter
import hashlib,json,time
P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
A=[[int(i==j) for j in range(N)] for i in range(N)]
for k in range(1,7):
    mod=P**k;h=[pow(r,-k,mod) for r in range(1,P)]
    v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
    piv=next(i for i,x in enumerate(v) if x%P);inv=pow(v[piv],-1,mod);old=A[piv]
    A=[[mod*a for a in row] if i==piv else [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
M=Matrix(A);assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W));assert all(x.q==1 for x in U)
UI=U.inv();G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):mu[i][j]=(F(int(G[i,j]))-sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D);assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]
H=[[pow(r,-k,P**k) for r in range(1,P)] for k in range(1,7)]
def particular(q,r):
    x=[0]*N;A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,7):
        mod=P**k;h=H[k-1]
        target=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(x,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,t in enumerate(v) if t%P);factor=target*pow(v[piv],-1,mod)%mod;old=A[piv]
        x=[a+factor*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else [a-(v[i]*pow(v[piv],-1,mod)%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
    for k in range(1,7):assert (sum(t*h for t,h in zip(x,H[k-1]))+pow(P*q+r,-k,P**k))%(P**k)==0
    return x
C={(q,r):[F(x) for x in Matrix(1,N,particular(q,r))*UI] for q in range(1,12) for r in range(1,13)}
C={k:[x-floor(x) for x in v] for k,v in C.items()}
def patterns(total,length,low=1):
    if length==0:
        if total==0:yield ()
        return
    for q in range(low,total+1):
        for t in patterns(total-q,length-1,q):yield (q,)+t
def rosters(pat):
    groups=[len(tuple(g)) for _,g in groupby(pat)]
    for blocks in product(*(combinations_with_replacement(range(1,P),k) for k in groups)):
        yield tuple(zip(pat,(r for b in blocks for r in b)))
def search(neg):
    cn=sum(P*(P*q+r)-1 for q,r in neg)
    if cn>CAP:return True,0,[]
    radius=CAP**2+(CAP-cn)**2;assert radius<dmin
    c=[-sum((C[a][j] for a in neg),F(0)) for j in range(N)];c=[x-floor(x) for x in c];z=c[:];n=[0]*N;nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            u=[sum((c[j]+n[j])*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x.denominator==1 for x in u);u=[int(x) for x in u]
            masses=[sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg))%(P**k) for k in range(1,7)]
            assert residues==[0]*6
            norm=sum((w*x)**2 for w,x in zip(W,u));assert norm<=radius
            leaves.append(dict(neg=neg,u=u,masses=masses,residues=residues,norm_sq=norm,radius_sq=radius,budget_valid=max(masses)<=CAP));return
        nodes+=1;center=c[i]+sum((z[j]*mu[j][i] for j in range(i+1,N)),F(0));near=floor(-center)
        for ni in (near,near+1):
            sp=spent+D[i]*(center+ni)**2
            if sp<=radius:
                z[i]=c[i]+ni;n[i]=ni;descend(i-1,sp)
        z[i]=c[i]
    descend(N-1,F(0));return False,nodes,leaves
if __name__=='__main__':
    start=time.perf_counter();rows=[];witnesses=[]
    for L in range(1,4):
        for pat in patterns(11,L):
            raw=over=nodes=leaves=valid=0;digest=hashlib.sha256()
            for neg in rosters(pat):
                raw+=1;digest.update((repr(neg)+'\n').encode('ascii'));skip,nd,ws=search(neg);over+=skip;nodes+=nd;leaves+=len(ws);valid+=sum(w['budget_valid'] for w in ws);witnesses.extend(ws)
            expected=1
            for m in Counter(pat).values():expected*=comb(11+m,m)
            assert raw==expected
            row=dict(pattern=pat,raw=raw,over=over,search=raw-over,nodes=nodes,leaves=leaves,valid=valid,roster_sha256=digest.hexdigest());rows.append(row);print(json.dumps(row),flush=True)
    out=dict(schema='T6_P13_Q11_SPLIT0_11_LEN1TO3_AUTHOR_EXACT_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',p=13,valuation=1,total_q=11,split=[0,11],budget=2331,gs_min_sq=str(dmin),lattice_index='13^21',rows=rows,witnesses=witnesses,totals={k:sum(r[k] for r in rows) for k in ('raw','over','search','nodes','leaves','valid')},elapsed_s=time.perf_counter()-start,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
    with open('q11_split0_11_len1to3.json','w') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
    print('RESULT',json.dumps({k:v for k,v in out.items() if k!='rows'},separators=(',',':')),flush=True)
