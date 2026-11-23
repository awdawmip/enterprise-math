#!/usr/bin/env python3
"""Author exact replay: T6 maximal p13, v13=1, order10 split(1,9), negative length1..3.
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


# p13 order10 signed split(1,9): one positive q1 atom versus a negative order9 roster.
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


PATTERNS=((9,),(1,8),(2,7),(3,6),(4,5),
          (1,1,7),(1,2,6),(1,3,5),(1,4,4),(2,2,5),(2,3,4),(3,3,3))
def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--output",required=True)
    args=pa.parse_args()
    rows=[];witnesses=[]
    for pat in PATTERNS:
        st=dict(pattern=pat,negative_rosters=0,raw_pairs=0,common_cancel=0,
                vertical_overbudget=0,gs_searches=0,gs_nodes=0,ball_leaves=0,budget_valid=0)
        digest=hashlib.sha256()
        for neg in all_rosters(pat):
            st["negative_rosters"]+=1
            for r in range(1,P):
                pos=((1,r),)
                digest.update((repr((pos,neg))+"\n").encode("ascii"))
                st["raw_pairs"]+=1
                if pos[0] in neg:
                    st["common_cancel"]+=1
                    continue
                skip,n,leaves=pair_search(pos,neg)
                st["vertical_overbudget"]+=int(skip)
                st["gs_searches"]+=int(not skip)
                st["gs_nodes"]+=n
                st["ball_leaves"]+=len(leaves)
                st["budget_valid"]+=sum(int(v["budget_valid"]) for v in leaves)
                witnesses.extend(leaves)
        st["roster_pair_digest_sha256"]=digest.hexdigest()
        rows.append(st)
    keys=("negative_rosters","raw_pairs","common_cancel","vertical_overbudget",
          "gs_searches","gs_nodes","ball_leaves","budget_valid")
    totals={k:sum(st[k] for st in rows) for k in keys}
    assert totals["raw_pairs"]==107328
    out=dict(schema="EM_T6_P13_Q10_SPLIT1_9_NEG_LEN1TO3_AUTHOR_EXACT_V1",
       source_pin="d84bd940cfb093cdc60e569f15cad58772a51dca",
       side_mass_cap=CAP,gs_min_sq=str(dmin),pattern_rows=rows,
       totals=totals,witnesses=witnesses,
       status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    with open(args.output,"w",encoding="utf-8") as f:json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps({"totals":totals,"relaxed_witnesses":len(witnesses)}))
if __name__=="__main__":
    main()
