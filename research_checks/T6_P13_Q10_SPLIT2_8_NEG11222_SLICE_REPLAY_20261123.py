#!/usr/bin/env python3
"""Author exact replay: T6 maximal p13, v13=1, q-order10 signed split(2,8), negative pattern (1,1,2,2,2).
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


# p13 order9 signed split(1,8): plus-one-atom versus negative length 1 or 2.
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
    parser=argparse.ArgumentParser()
    parser.add_argument("--start",type=int,required=True)
    parser.add_argument("--end",type=int,required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    assert 0<=args.start<args.end<=28392
    pos_all=[((2,r),) for r in range(1,13)]+[
        ((1,r),(1,s)) for r,s in combinations_with_replacement(range(1,13),2)]
    assert len(pos_all)==90
    st=dict(start=args.start,end=args.end,negative_rosters=0,raw_signed_pairs=0,
            common_named_atom_canceled=0,vertical_original_mass_excess=0,
            gs_searches=0,gs_nodes=0,relaxed_sphere_witnesses=0,
            both_original_side_mass_valid=0)
    witnesses=[];roster_digest=hashlib.sha256();pair_digest=hashlib.sha256()
    for idx,neg in enumerate(all_rosters((1,1,2,2,2))):
        if idx>=args.end:break
        if idx<args.start:continue
        st["negative_rosters"]+=1
        roster_digest.update((repr(neg)+"\n").encode("ascii"))
        for pidx,pos in enumerate(pos_all):
            st["raw_signed_pairs"]+=1
            pair_digest.update((repr((idx,pidx,pos,neg))+"\n").encode("ascii"))
            if any(atom in neg for atom in pos):
                st["common_named_atom_canceled"]+=1
                continue
            skip,nodes,leaves=pair_search(pos,neg)
            if skip:
                st["vertical_original_mass_excess"]+=1
                continue
            st["gs_searches"]+=1
            st["gs_nodes"]+=nodes
            st["relaxed_sphere_witnesses"]+=len(leaves)
            st["both_original_side_mass_valid"]+=sum(int(z["budget_valid"]) for z in leaves)
            for z in leaves:
                z["negative_roster_index"]=idx
                z["positive_roster_index"]=pidx
                z["modular_residues"]=[
                    (sum(x*pow(r,-k,13**k) for r,x in enumerate(z["u"],1))+
                     sum(pow(13*q+r,-k,13**k) for q,r in pos)-
                     sum(pow(13*q+r,-k,13**k) for q,r in neg))%(13**k)
                    for k in range(1,7)]
                assert z["modular_residues"]==[0]*6
                witnesses.append(z)
    assert st["negative_rosters"]==args.end-args.start
    assert st["raw_signed_pairs"]==90*(args.end-args.start)
    assert st["gs_searches"]+st["vertical_original_mass_excess"]+st["common_named_atom_canceled"]==st["raw_signed_pairs"]
    result=dict(schema="EM_T6_P13_Q10_SPLIT2_8_NEG11222_AUTHOR_EXACT_SLICE_REPLAY_V1",
                frozen_science="awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca",
                positive_patterns=[(2,),(1,1)],negative_pattern=(1,1,2,2,2),
                source_order="negative q1 CWR(12,2) times q2 CWR(12,3); positive q2 single then q1 CWR(12,2)",
                budget_each_side=CAP,gs_min_sq=str(dmin),lattice_index="13^21",
                stats=st,roster_sha256=roster_digest.hexdigest(),
                pair_digest_sha256=pair_digest.hexdigest(),witnesses=witnesses,
                status="AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED")
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,sort_keys=True)
    print(json.dumps({k:v for k,v in result.items() if k!="witnesses"},sort_keys=True))

if __name__=="__main__":
    main()
