#!/usr/bin/env python3
"""R223 exact test: exchangeable Markov source survival and ideal readout.
Usage: python R223_exchangeable_markov_spectral_check.py
Writes R223_verification.json beside this script. Standard library only.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json


def stirling(n, j):
    row = [1]
    for i in range(1, n+1):
        nxt = [0]*(i+1)
        for z in range(1, i+1):
            nxt[z] = (row[z-1] if z-1<len(row) else 0) + (z*row[z] if z<len(row) else 0)
        row = nxt
    return row[j] if 0 <= j < len(row) else 0


def weights(m,k,L):
    return [factorial(r)*m**L*sum(stirling(L+1,j+1) for j in range(min(r,L)+1)) for r in range(k+1)]


def ideals(m,k,L):
    W=weights(m,k,L)
    return [sum(comb(k-r,j-r)*W[j] for j in range(r,k+1)) for r in range(k+1)]


def transition(k,a):
    n=k+1
    P=[[((a if i==j else Q(0)) + (1-a)/n) for j in range(n)] for i in range(n)]
    assert all(min(row)>=0 and sum(row)==1 for row in P)
    return P


def direct(m,k,L,a,nmax):
    P=transition(k,a)
    n=k+1
    T=ideals(m,k,L)
    state={(i,(0 if i==0 else (1<<(i-1)))):Q(1,n) for i in range(n)}
    ans=[]
    for _ in range(nmax):
        ans.append(sum(v*T[mask.bit_count()] for (i,mask),v in state.items()))
        nxt={}
        for (i,mask),v in state.items():
            for j in range(n):
                if P[i][j]:
                    key=(j,mask | (0 if j==0 else 1<<(j-1)))
                    nxt[key]=nxt.get(key,Q(0))+v*P[i][j]
        assert sum(nxt.values())==1
        state=nxt
    return ans


def modes(m,k,L,a,nmax):
    n=k+1
    W=weights(m,k,L)
    lam=[a+(1-a)*Q(r+1,n) for r in range(k+1)]
    amp=[Q(comb(k,r)*W[r]*(r+1),n) for r in range(k+1)]
    out=[sum(amp[r]*lam[r]**(t-1) for r in range(k+1)) for t in range(1,nmax+1)]
    return out,lam,amp


def poly(lam):
    coef=[Q(1)]
    for v in lam:
        nxt=[Q(0)]*(len(coef)+1)
        for j,c in enumerate(coef):
            nxt[j]-=v*c
            nxt[j+1]+=c
        coef=nxt
    return coef


def rank(mat):
    a=[list(row) for row in mat]
    if not a:return 0
    rr,cc=len(a),len(a[0])
    p=0
    for j in range(cc):
        i=next((i for i in range(p,rr) if a[i][j]),None)
        if i is None:continue
        a[p],a[i]=a[i],a[p]
        q=a[p][j]
        a[p]=[x/q for x in a[p]]
        for i in range(rr):
            if i!=p and a[i][j]:
                t=a[i][j]
                a[i]=[x-t*y for x,y in zip(a[i],a[p])]
        p+=1
        if p==rr:break
    return p


def run():
    cases=0
    equalities=0
    rank_cases=0
    recurrence=0
    differences=0
    zero_boundary=0
    for k in (1,2,3):
        for a in (Q(0),Q(1,4),Q(-1,2*k),Q(-1,k),Q(1)):
            for m in (1,12):
                for L in (1,2,3):
                    nmax=L+2*(k+1)+10
                    brute=direct(m,k,L,a,nmax)
                    vals,lams,amps=modes(m,k,L,a,nmax)
                    for t in range(L,nmax+1):
                        assert brute[t-1]==vals[t-1],(k,a,m,L,t)
                        equalities+=1
                    assert len(set(lams))==(1 if a==1 else k+1)
                    assert all(0<=x<=1 for x in lams)
                    H=[[vals[L+i+j-1] for j in range(k+1)] for i in range(k+1)]
                    r=rank(H)
                    expected=1 if a==1 else k+1-(1 if a==Q(-1,k) and L>=2 else 0)
                    assert r==expected,(k,a,m,L,r,expected)
                    rank_cases+=1
                    c=poly(lams)
                    for t in range(L,nmax-(k+1)+1):
                        assert sum(c[j]*vals[t+j-1] for j in range(k+2))==0
                        recurrence+=1
                    for t in range(L,L+5):
                        for j in range(5):
                            d=sum((-1)**(j-i)*comb(j,i)*vals[t+i-1] for i in range(j+1))
                            assert (-1)**j*d>=0,(k,a,m,L,t,j)
                            differences+=1
                    if a==Q(-1,k):zero_boundary+=1
                    cases+=1
    seq,lam,amp=modes(1,2,1,Q(-1,4),8)
    assert lam==[Q(1,6),Q(7,12),Q(1)]
    assert amp==[Q(1,3),Q(8,3),Q(4)]
    assert seq[:4]==[Q(7),Q(101,18),Q(59,12),Q(367,81)]
    negative_example={
        "alpha":"-1/4",
        "full_transition_eigenvalues":["1","-1/4","-1/4"],
        "observable_lambda":[str(x) for x in lam],
        "amplitudes":[str(x) for x in amp],
        "first_eight_expectations":[str(x) for x in seq],
        "minimal_degree":3
    }
    W=weights(12,6,2)
    values,lambdas,amp=modes(12,6,2,Q(1,4),20)
    assert W==[144,576,1440,4320,17280,86400,518400]
    assert lambdas==[Q(10+3*r,28) for r in range(7)]
    assert rank([[values[2+i+j-1] for j in range(7)] for i in range(7)])==7
    assert values[11]==Q(149648228779334204799,226775649501184)
    x6={
        "m":12,"k":6,"L":2,"alpha":"1/4",
        "W":W,
        "observable_lambda":[str(x) for x in lambdas],
        "amplitudes":[str(x) for x in amp],
        "E_2":str(values[1]),
        "E_12":str(values[11]),
        "limit":W[-1],
        "minimal_recurrence_degree":7
    }
    result={
        "result":"PASS",
        "arithmetic":"Fraction, exact integer and rational only",
        "finite_configurations":cases,
        "direct_vs_spectral_equalities":equalities,
        "hankel_rank_cases":rank_cases,
        "recurrence_identity_checks":recurrence,
        "alternating_difference_checks":differences,
        "zero_boundary_cases":zero_boundary,
        "coverage":{"k":[1,2,3],"m":[1,12],"L":[1,2,3],"alpha":["0","1/4","-1/(2k)","-1/k","1"]},
        "negative_spectrum_witness":negative_example,
        "six_source_example":x6,
        "scope":"General theorem algebraic; direct exact tests limited to finite families; native BRC untested; independent review not performed"
    }
    target=Path(__file__).with_name("R223_verification.json")
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
    print("PASS",cases,equalities,rank_cases,recurrence,differences)
    return result

if __name__=="__main__":
    run()
