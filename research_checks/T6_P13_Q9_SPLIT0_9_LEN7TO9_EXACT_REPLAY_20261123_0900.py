#!/usr/bin/env python3
"""Author exact replay: T6 maximal p13, v13=1, order9 split(0,9), roster lengths 7..9.
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

# Reproduce one canonical, contiguous source-order slice at a time.
# Allowed patterns exhaust the residual length 7..9 roster partition of 9.
PATTERNS = {
    "1111113": (1,1,1,1,1,1,3),
    "1111122": (1,1,1,1,1,2,2),
    "11111112": (1,1,1,1,1,1,1,2),
    "111111111": (1,1,1,1,1,1,1,1,1),
}
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--pattern", choices=PATTERNS, required=True)
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--end",type=int)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    pat=PATTERNS[args.pattern]
    groups=[len(tuple(g)) for _,g in groupby(pat)]
    expected=1
    for n in groups:
        expected*=comb(11+n,n)
    end=expected if args.end is None else args.end
    assert 0<=args.start<end<=expected
    stats=dict(start=args.start,end=end,visited=0,overbudget=0,gs_nodes=0,ball_leaves=0,budget_valid=0)
    witness=[];digest=hashlib.sha256()
    for idx,roster in enumerate(all_rosters(pat)):
        if idx>=end:break
        if idx<args.start:continue
        digest.update((repr(roster)+"\n").encode("ascii"))
        skip,n,leaves=search_one(roster)
        stats["visited"]+=1;stats["overbudget"]+=int(skip)
        stats["gs_nodes"]+=n;stats["ball_leaves"]+=len(leaves)
        stats["budget_valid"]+=sum(int(x["budget_valid"]) for x in leaves)
        witness.extend(leaves)
    assert stats["visited"]==end-args.start
    result=dict(schema="EM_T6_P13_Q9_LEN7TO9_AUTHOR_EXACT_SLICE_V1",
        frozen_science="d84bd940cfb093cdc60e569f15cad58772a51dca",
        pattern=pat,roster_total=expected,source_order="q-group product/combinations_with_replacement r=1..12",
        cap=CAP,index=P**21,gs_min_sq=str(dmin),stats=stats,
        roster_sha256=digest.hexdigest(),witnesses=witness,
        status="AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED")
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(result,f,sort_keys=True,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!="witnesses"},sort_keys=True))
if __name__=="__main__":
    main()
