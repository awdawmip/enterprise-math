#!/usr/bin/env python3
"""Author exact replay: T6 maximal p13, v13=1, q-order9 signed split(4,5), positive (1,1,2) triple, negative q5 lengths 1..3.
Source: frozen taskbook d84bd940cfb093cdc60e569f15cad58772a51dca.
Uses only exact integer and rational arithmetic; author evidence, not Native Result.
"""
from fractions import Fraction as F
from math import floor, comb
from itertools import product, combinations_with_replacement, groupby
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from collections import Counter
import hashlib, json, argparse

P,CAP,N=13,2331,12
W=[P*r-1 for r in range(1,P)]
A=[[int(i==j) for j in range(N)] for i in range(N)]
for k in range(1,7):
    mod=P**k;h=[pow(r,-k,mod) for r in range(1,P)]
    v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
    piv=next(i for i,x in enumerate(v) if x%P);inv=pow(v[piv],-1,mod);old=A[piv]
    A=[[mod*a for a in row] if i==piv else
       [a-(v[i]*inv%mod)*b for a,b in zip(row,old)] for i,row in enumerate(A)]
M=Matrix(A)
assert abs(M.det())==P**21
Rw=(hermite_normal_form(M.T).T*Matrix.diag(*W)).lll(delta=F(3,4))
U=Rw*Matrix.diag(*(F(1,w) for w in W))
assert all(x.q==1 for x in U)
UI=U.inv()
G=Rw*Rw.T
mu=[[F(0)]*N for _ in range(N)];D=[]
for i in range(N):
    for j in range(i):
        mu[i][j]=(F(int(G[i,j]))-
                 sum(mu[i][t]*mu[j][t]*D[t] for t in range(j)))/D[j]
    D.append(F(int(G[i,i]))-sum(mu[i][j]**2*D[j] for j in range(i)))
dmin=min(D)
assert dmin>2*CAP**2
Urows=[[int(U[j,t]) for t in range(N)] for j in range(N)]

def particular(q,r):
    x=[0]*N
    A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,7):
        mod=P**k;h=[pow(j,-k,mod) for j in range(1,P)]
        target=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(x,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,t in enumerate(v) if t%P)
        factor=target*pow(v[piv],-1,mod)%mod;old=A[piv]
        x=[a+factor*b for a,b in zip(x,old)]
        A=[[mod*a for a in row] if i==piv else
           [a-(v[i]*pow(v[piv],-1,mod)%mod)*b for a,b in zip(row,old)]
           for i,row in enumerate(A)]
    for k in range(1,7):
        mod=P**k
        assert (sum(t*pow(j,-k,mod) for j,t in enumerate(x,1))+
                pow(P*q+r,-k,mod))%mod==0
    return x

c_atom={(q,r):[F(x) for x in Matrix(1,N,particular(q,r))*UI]
        for q in range(1,10) for r in range(1,P)}

def patterns(total, length, low=1):
    if length==0:
        if total==0:yield ()
        return
    for q in range(low,total+1):
        for tail in patterns(total-q,length-1,q):yield (q,)+tail

def all_rosters(pat):
    groups=[len(tuple(g)) for _,g in groupby(pat)]
    for blocks in product(*(combinations_with_replacement(range(1,P),k) for k in groups)):
        yield tuple(zip(pat,(r for block in blocks for r in block)))

def search_one(roster):
    cn=sum(P*(P*q+r)-1 for q,r in roster)
    if cn>CAP:return (True,0,[])
    radius=CAP**2+(CAP-cn)**2
    assert radius<dmin
    c=[-sum(c_atom[q,r][j] for q,r in roster) for j in range(N)]
    z=c[:];n=[0]*N;nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            u=[sum((c[j]+n[j])*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x.denominator==1 for x in u)
            u=[int(x) for x in u]
            masses=[sum(w*max(0,x) for w,x in zip(W,u)),
                    cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            for k in range(1,7):
                m=P**k
                assert (sum(x*pow(r,-k,m) for r,x in enumerate(u,1))-
                        sum(pow(P*q+r,-k,m) for q,r in roster))%m==0
            leaves.append(dict(roster=roster,u=u,masses=masses,
                               radius_sq=radius,budget_valid=max(masses)<=CAP))
            return
        nodes+=1
        center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
        near=floor(-center)
        for ni in (near,near+1):
            next_spent=spent+D[i]*(center+ni)**2
            if next_spent<=radius:
                z[i]=c[i]+ni;n[i]=ni
                descend(i-1,next_spent)
        z[i]=c[i]
    descend(N-1,F(0))
    return (False,nodes,leaves)


# Complete q5 negative named roster versus a positive (4,r) atom; shared names cancel.
# Exclude shared named atom; its cancellation belongs to the prior lower-order case.
def pair_search(pos,neg):
    cp=sum(P*(P*q+r)-1 for q,r in pos)
    cn=sum(P*(P*q+r)-1 for q,r in neg)
    if cp>CAP or cn>CAP:return (True,0,[])
    radius=(CAP-cp)**2+(CAP-cn)**2
    assert radius<dmin
    c=[sum((c_atom[q,r][j] for q,r in pos),F(0))-
       sum((c_atom[q,r][j] for q,r in neg),F(0)) for j in range(N)]
    z=c[:];n=[0]*N;nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            u=[sum((c[j]+n[j])*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x.denominator==1 for x in u)
            u=[int(x) for x in u]
            masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),
                    cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            for k in range(1,7):
                m=P**k
                assert (sum(x*pow(r,-k,m) for r,x in enumerate(u,1))+
                        sum(pow(P*q+r,-k,m) for q,r in pos)-
                        sum(pow(P*q+r,-k,m) for q,r in neg))%m==0
            leaves.append(dict(pos=pos,neg=neg,u=u,masses=masses,
                               radius_sq=radius,budget_valid=max(masses)<=CAP))
            return
        nodes+=1
        center=c[i]+sum((z[j]*mu[j][i] for j in range(i+1,N)),F(0))
        near=floor(-center)
        for ni in (near,near+1):
            next_spent=spent+D[i]*(center+ni)**2
            if next_spent<=radius:
                z[i]=c[i]+ni;n[i]=ni
                descend(i-1,next_spent)
        z[i]=c[i]
    descend(N-1,F(0))
    return (False,nodes,leaves)

def main():
    rows=[]; witnesses=[]; h=hashlib.sha256();rosters=0
    positive=[((1,r1),(1,r2),(2,r3))
        for r1,r2 in combinations_with_replacement(range(1,13),2)
        for r3 in range(1,13)]
    for length in range(1,4):
        for pat in patterns(5,length):
            st=dict(pattern=pat,raw_pairs=0,common_canceled=0,
                    overbudget=0,gs_nodes=0,ball_leaves=0,budget_valid=0)
            for neg in all_rosters(pat):
                rosters+=1;h.update((str(neg)+'\n').encode())
                for pos in positive:
                    st["raw_pairs"]+=1
                    if any(a in neg for a in pos):
                        st["common_canceled"]+=1
                        continue
                    skip,n,leaves=pair_search(pos,neg)
                    st["overbudget"]+=int(skip)
                    st["gs_nodes"]+=n
                    st["ball_leaves"]+=len(leaves)
                    st["budget_valid"]+=sum(int(z["budget_valid"]) for z in leaves)
                    witnesses.extend(leaves)
            rows.append(st)
            print("COMPLETE",st,flush=True)
    result=dict(schema="EM_T6_P13_Q9_SPLIT4_5_POS_Q112_NEG_LEN1TO3_V1",
        frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
        cap=CAP,index=P**21,gs_min_sq=str(dmin),
        negative_rosters=rosters,roster_sha256=h.hexdigest(),
        rows=rows,witnesses=witnesses,
        status="AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    with open("T6_P13_Q9_SPLIT4_5_POS_Q112_NEG_LEN1TO3_AUTHOR_EXACT_CERT.json","w",encoding="utf-8") as f:
        json.dump(result,f,sort_keys=True,indent=2)
if __name__=="__main__":
    main()
