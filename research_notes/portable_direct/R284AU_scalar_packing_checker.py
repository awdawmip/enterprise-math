#!/usr/bin/env python3
"""Exact high-radix scalar Port reconstruction, positive integer matrices.
Python 3 standard library only; integer determinants via Bareiss elimination.
"""
import json, math, random, sys
from fractions import Fraction
from itertools import combinations, product

def weights3(n):
    w=[]
    for _ in range(n):
        forbidden=set()
        t=len(w)
        for k in range(1,4):
            for a in combinations(w,k-1):
                for b in combinations(w,k):
                    forbidden.add(sum(b)-sum(a))
        cand=(w[-1]+1 if w else 1)
        while cand in forbidden:
            cand+=1
        w.append(cand)
    for k in range(1,4):
        sums=[sum(s) for s in combinations(w,k)]
        assert len(sums)==len(set(sums)), (n,w,k)
    return w

def det_int(A):
    n=len(A)
    if n==0:return 1
    M=[row[:] for row in A]
    sign,denom=1,1
    for k in range(n-1):
        pivot=k
        while pivot<n and M[pivot][k]==0:pivot+=1
        if pivot==n:return 0
        if pivot!=k:M[pivot],M[k]=M[k],M[pivot];sign=-sign
        pk=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=M[i][j]*pk-M[i][k]*M[k][j]
                assert num%denom==0
                M[i][j]=num//denom
            M[i][k]=0
        denom=pk
    return sign*M[-1][-1]

def digits_balanced(value,base):
    out={}
    position=0
    while value:
        rem=value%base
        if rem>base//2:rem-=base
        if rem:out[position]=rem
        value=(value-rem)//base
        position+=1
    return out

def reconstruct(C,H):
    n=len(C)
    assert n>=2 and isinstance(H,int) and H>=1
    assert all(1<=v<=H for row in C for v in row)
    w=weights3(n)
    W=1+sum(w)
    max_coeff=(1<<n)*math.factorial(n)*H**n
    base=1 << ((2*max_coeff).bit_length()+1)
    D=[base**(W+x) for x in w]
    A=[[((D[i] if i==j else 0)-C[i][j]) for j in range(n)] for i in range(n)]
    F=det_int(A)
    Fdigits=digits_balanced(F,base)
    ds={}
    for v in range(1,n):
        T=[row[:] for row in A]
        T[0][v]-=1
        ds[v]=digits_balanced(det_int(T)-F,base)
    def code_missing(missing):
        return (n-len(missing))*W+sum(w)-sum(w[i] for i in missing)
    def coef(dig,missing):return dig.get(code_missing(missing),0)
    alpha=[-coef(Fdigits,{i}) for i in range(n)]
    P={}
    for i,j in combinations(range(n),2):
        P[i,j]=alpha[i]*alpha[j]-coef(Fdigits,{i,j})
    X=[[None]*n for _ in range(n)]
    for i in range(n):X[i][i]=Fraction(alpha[i])
    for v in range(1,n):
        X[v][0]=Fraction(-coef(ds[v],{0,v}))
        X[0][v]=Fraction(P[0,v])/X[v][0]
    for i,j in combinations(range(1,n),2):
        q=X[i][0]*alpha[j]-coef(ds[i],{0,i,j})
        X[i][j]=Fraction(q)/X[j][0]
        X[j][i]=Fraction(P[i,j])/X[i][j]
    observed_bits=[abs(F).bit_length()]
    for v in range(1,n):
        T=[row[:] for row in A]
        T[0][v]-=1
        observed_bits.append(abs(det_int(T)).bit_length())
    return X,{"n":n,"H":H,"weights":w,"W":W,"base_bits":base.bit_length(),
              "max_exponent":n*W+sum(w),"F_bits":abs(F).bit_length(),
              "nonzero_F_digits":len(Fdigits),"scalar_determinants":n,
              "max_observed_bits":max(observed_bits)}

def main():
    rng=random.Random(284021)
    records=[]
    for n,count in ((2,12),(3,16),(4,12),(5,7)):
        for t in range(count):
            H=2+(t%3)
            C=[[rng.randint(1,H) for _ in range(n)] for __ in range(n)]
            got,metrics=reconstruct(C,H)
            assert got==[[Fraction(x) for x in row] for row in C],(n,t,C,got)
            records.append(metrics)
    exhaustive_cases=0
    for vals in product((1,2), repeat=9):
        C=[list(vals[3*i:3*i+3]) for i in range(3)]
        got,_=reconstruct(C,2)
        assert got==[[Fraction(x) for x in row] for row in C]
        exhaustive_cases+=1
    example=[[2,1,3],[4,2,1],[1,3,2]]
    got,example_metrics=reconstruct(example,4)
    assert got==[[Fraction(x) for x in row] for row in example]
    result={"result":"PASS","method":"balanced radix exact integer determinant, Bareiss elimination; positive integer inputs; exact equality to source C",
            "seed":284021,"test_counts_by_n":{"2":12,"3":16,"4":12,"5":7},
            "total_random_cases":len(records),"exhaustive_binary_3x3_cases":exhaustive_cases,"plus_fixed_example":1,
            "scalar_measurements_each":"n = 1 diagonal baseline + n-1 directed star edges",
            "fixed_matrix":example,"fixed_example_metrics":example_metrics,
            "per_n_max_observed_bits":{str(n):max(x['max_observed_bits'] for x in records if x['n']==n) for n in (2,3,4,5)},
            "max_weight_by_n":{str(n):max(weights3(n)) for n in (2,3,4,5)},
            "independent_review":"NOT_REVIEWED",
            "scope_limit":"Finite tests do not prove arbitrary n; see proof for all-n theorem."}
    path=sys.argv[1] if len(sys.argv)>1 else 'R284AU_scalar_packing_exact_verification.json'
    with open(path,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
