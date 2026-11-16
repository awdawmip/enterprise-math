#!/usr/bin/env python3
"""R225 exact arithmetic checks; abstract scalar observer only, not native BRC."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json

def stirling2(n,k):
    if n==0: return int(k==0)
    if k==0: return 0
    return k*stirling2(n-1,k)+stirling2(n-1,k-1)

def weights(m,k,L):
    return [factorial(r)*m**L*sum(stirling2(L+1,j+1)
            for j in range(min(r,L)+1)) for r in range(k+1)]

def ideal_T(W,k):
    return [sum(comb(k-r,s-r)*W[s] for s in range(r,k+1))
            for r in range(k+1)]

def atoms(pi,alpha,m,L):
    k=len(pi)-1; W=weights(m,k,L)
    result=[]
    for mask in range(1<<k):
        q=pi[0]+sum(pi[i+1] for i in range(k) if mask>>i&1)
        lam=alpha+(1-alpha)*q
        result.append((mask,W[mask.bit_count()]*q,lam))
    return result

def spectral(n,pi,alpha,m,L):
    return sum((c*lam**(n-1) for _,c,lam in atoms(pi,alpha,m,L)),Q(0))

def dynamic(n,pi,alpha,m,L):
    k=len(pi)-1
    T=ideal_T(weights(m,k,L),k)
    v={(j,1<<(j-1) if j else 0):pi[j] for j in range(k+1)}
    for step in range(2,n+1):
        w={}
        for (old,mask),mass in v.items():
            for j in range(k+1):
                p=(alpha if old==j else 0)+(1-alpha)*pi[j]
                if p:
                    s=(j,mask|(1<<(j-1) if j else 0))
                    w[s]=w.get(s,Q(0))+mass*p
        v=w
    assert sum(v.values())==1
    return sum((mass*T[mask.bit_count()] for (_,mask),mass in v.items()),Q(0))

def rank_hankel(v):
    d=(len(v)+1)//2
    a=[[v[i+j] for j in range(d)] for i in range(d)]
    rank=0
    for c in range(d):
        piv=next((i for i in range(rank,d) if a[i][c]),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        x=a[rank][c]
        for j in range(c,d): a[rank][j]/=x
        for i in range(rank+1,d):
            if a[i][c]:
                z=a[i][c]
                for j in range(c,d): a[i][j]-=z*a[rank][j]
        rank+=1
    return rank

def mod_hankel_det(nums,alpha_num,alpha_den,m,L,p):
    den=sum(nums)
    pi=[x*pow(den,-1,p)%p for x in nums]
    alpha=alpha_num*pow(alpha_den,-1,p)%p
    k=len(pi)-1; W=weights(m,k,L); modes=[]
    for mask in range(1<<k):
        q=(pi[0]+sum(pi[i+1] for i in range(k) if mask>>i&1))%p
        lam=(alpha+(1-alpha)*q)%p
        c=W[mask.bit_count()]*q*pow(lam,L-1,p)%p
        modes.append((c,lam))
    d=len(modes)
    terms=[c for c,_ in modes]; moments=[]
    for _ in range(2*d-1):
        moments.append(sum(terms)%p)
        terms=[t*lam%p for t,(_,lam) in zip(terms,modes)]
    a=[[moments[i+j] for j in range(d)] for i in range(d)]
    det=1; rank=0
    for j in range(d):
        piv=next((i for i in range(j,d) if a[i][j]),None)
        if piv is None: return 0,rank
        if piv!=j:
            a[j],a[piv]=a[piv],a[j]; det=(-det)%p
        pivot=a[j][j]; det=det*pivot%p
        inv=pow(pivot,-1,p)
        for i in range(j+1,d):
            if a[i][j]:
                z=a[i][j]*inv%p
                for x in range(j+1,d):
                    a[i][x]=(a[i][x]-z*a[j][x])%p
                a[i][j]=0
        rank+=1
    return det,rank

def frac(x):
    return str(x.numerator)+"/"+str(x.denominator)

def run():
    cases=0; comparisons=0; differences=0; ranks=0
    for k in (1,2,3):
        for m in (1,12):
            for L in (1,2,3):
                for nums in ([1]*(k+1),list(range(1,k+2)),
                             [1]+[2**i for i in range(1,k+1)]):
                    pi=[Q(x,sum(nums)) for x in nums]
                    pmin=min(pi)
                    for alpha in (Q(0),Q(1,4),
                                  -pmin/(2*(1-pmin)),Q(1)):
                        P=[[alpha*(i==j)+(1-alpha)*pi[j]
                            for j in range(k+1)] for i in range(k+1)]
                        assert all(sum(row)==1 and all(t>=0 for t in row)
                                   for row in P)
                        modes=atoms(pi,alpha,m,L)
                        assert all(0<=lam<=1 for _,_,lam in modes)
                        for n in range(L,max(7,L+1)):
                            assert dynamic(n,pi,alpha,m,L)==spectral(n,pi,alpha,m,L)
                            comparisons+=1
                        unique={lam for _,_,lam in modes if lam>0 or L==1}
                        d=len(unique)
                        terms=[spectral(L+n,pi,alpha,m,L) for n in range(2*d-1)]
                        assert rank_hankel(terms)==d
                        ranks+=1
                        for n in range(L,L+4):
                            for j in range(5):
                                alternating=sum(((-1)**t)*comb(j,t)*
                                  spectral(n+t,pi,alpha,m,L) for t in range(j+1))
                                assert alternating>=0
                                differences+=1
                        cases+=1
    nums=[1,2,4,8,16,32,64]
    pi=[Q(x,127) for x in nums]; alpha=Q(1,4)
    modes=atoms(pi,alpha,12,2)
    assert len({lam for _,_,lam in modes})==64
    assert all(c>0 and lam>0 for _,c,lam in modes)
    W=weights(12,6,2)
    assert W==[144,576,1440,4320,17280,86400,518400]
    terms={}
    for n in (2,3,4,12):
        x=spectral(n,pi,alpha,12,2)
        assert x==dynamic(n,pi,alpha,12,2)
        terms[str(n)]=frac(x); comparisons+=1
    determinants=[]
    for p in (1000000007,1000000009):
        det,rank=mod_hankel_det(nums,1,4,12,2,p)
        assert rank==64 and det!=0
        determinants.append({"prime":p,"det_hankel64_mod_p":det,"rank":rank})
    rare=min(pi[1:])
    rho=1-(1-alpha)*rare
    coefficient=sum((W[5]*(1-pi[i]) for i in range(1,7)
                     if pi[i]==rare),Q(0))
    result={
      "schema":"EM_R225_NONUNIFORM_RESETTING_EXACT_VERIFICATION_V1",
      "classification":"EXACT_FINITE_CHECKED_NOT_INDEPENDENTLY_REVIEWED",
      "model":"scalar source-support principal-ideal query, not native BRC dynamics",
      "parameter_cases_checked":cases,
      "dynamic_vs_spectral_comparisons":comparisons,
      "alternating_difference_checks":differences,
      "exact_hankel_rank_checks":ranks,
      "witness":{
        "m":12,"k":6,"L":2,"pi_numerators":nums,"pi_denominator":127,
        "alpha":frac(alpha),"distinct_positive_atoms":64,
        "minimal_rational_recurrence_degree":64,"W":W,"f_n":terms,
        "hankel_determinants":determinants,
        "asymptotic_decay_ratio":frac(rho),
        "asymptotic_leading_coefficient":frac(coefficient),"limit":W[6]},
      "result":"PASS"}
    Path(__file__).with_name("R225_nonuniform_reset_verification.json").write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__":
    run()
