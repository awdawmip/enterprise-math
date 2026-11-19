#!/usr/bin/env python3
"""R284AM: exact exterior-tensor span DP for principal rank of U V^T.
Pure Python Fractions for span operations; SymPy only in independent regression.
"""
import itertools
import json
import random
from fractions import Fraction
from math import comb


def determinant(a):
    """Exact integer/rational determinant by fraction-preserving elimination."""
    n=len(a)
    if n==0: return 1
    mat=[[Fraction(v) for v in row] for row in a]
    sign=1
    det=Fraction(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if mat[j][i]),None)
        if pivot is None: return 0
        if pivot!=i:
            mat[i],mat[pivot]=mat[pivot],mat[i]
            sign=-sign
        p=mat[i][i]
        det*=p
        for j in range(i+1,n):
            if mat[j][i]:
                t=mat[j][i]/p
                for k in range(i+1,n): mat[j][k]-=t*mat[i][k]
                mat[j][i]=0
    d=det*sign
    return int(d) if d.denominator==1 else d


class Span:
    def __init__(self, dimension):
        self.dimension=dimension
        self.pivots={}
        self.witnesses=[]  # original, unmodified z_S; no arbitrary linear-combination labels

    def add(self, vector, subset):
        w=list(map(Fraction,vector))
        for p in sorted(self.pivots):
            if w[p]:
                t=w[p]
                row=self.pivots[p]
                w=[x-t*y for x,y in zip(w,row)]
        pivot=next((i for i,x in enumerate(w) if x),None)
        if pivot is None: return False
        den=w[pivot]
        self.pivots[pivot]=[x/den for x in w]
        self.witnesses.append((subset,tuple(vector)))
        return True

    def contains(self, vector):
        w=list(map(Fraction,vector))
        for p in sorted(self.pivots):
            if w[p]:
                t=w[p]
                w=[x-t*y for x,y in zip(w,self.pivots[p])]
        return not any(w)


def plucker(A,S,j,r,columns):
    return [determinant([[A[i][k] for k in J] for i in S]) for J in columns[j]]


def exterior_principal_rank(U,V,return_bases=False):
    m=len(U)
    assert m==len(V) and m>=1
    r=len(U[0]); assert r>=1 and all(len(x)==r for x in U+V)
    columns={j:list(itertools.combinations(range(r),j)) for j in range(r+1)}
    grades=[Span(comb(r,j)**2) for j in range(r+1)]
    grades[0].add([1],())
    candidates=0
    for i in range(m):
        for j in range(min(i+1,r),0,-1):
            for S,_ in list(grades[j-1].witnesses):
                T=S+(i,)
                a=plucker(U,T,j,r,columns)
                b=plucker(V,T,j,r,columns)
                tensor=[x*y for x in a for y in b]
                grades[j].add(tensor,T)
                candidates+=1
    max_rank=0; witness=()
    for j in range(1,r+1):
        nc=comb(r,j)
        for S,z in grades[j].witnesses:
            dot=sum(z[k*nc+k] for k in range(nc))
            if dot:
                max_rank,witness=j,S
                break
    expected=sum(comb(r,j)**2 for j in range(r+1))
    assert sum(len(G.witnesses) for G in grades)<=expected
    result={"m":m,"factor_width":r,"principal_rank":max_rank,
            "witness_1based":[i+1 for i in witness],
            "witness_det":determinant([[sum(U[a][z]*V[b][z] for z in range(r)) for b in witness] for a in witness]),
            "dimensions":[len(G.witnesses) for G in grades],"total_span_bound":expected,
            "candidate_states":candidates}
    if return_bases: return result,grades
    return result


def verify_all_subsets(U,V,grades):
    """Independent small-instance regression: every true subset state lies in DP span."""
    m=len(U);r=len(U[0])
    columns={j:list(itertools.combinations(range(r),j)) for j in range(r+1)}
    checks=0
    for j in range(r+1):
        for S in itertools.combinations(range(m),j):
            a=plucker(U,S,j,r,columns)
            b=plucker(V,S,j,r,columns)
            z=[x*y for x in a for y in b]
            assert grades[j].contains(z), ('span missing',S)
            checks+=1
    return checks


def exhaustive_rank(U,V):
    m=len(U);r=len(U[0])
    C=[[sum(U[i][t]*V[k][t] for t in range(r)) for k in range(m)] for i in range(m)]
    d=0; w=()
    for j in range(1,min(r,m)+1):
        for S in itertools.combinations(range(m),j):
            if determinant([[C[a][b] for b in S] for a in S]): d,w=j,S
    return d,w


def ak_factors(k):
    r=k+1
    a=[1]*r
    b=[a[:i+1]+[2]+a[i+2:] for i in range(k)]
    return [a[:]]*k+b,b+[a[:]]*k


def run():
    rng=random.Random(284013)
    count=0
    closure_checks=0
    grade_counts={}
    for m in range(2,9):
        for r in range(1,min(m,4)+1):
            for trial in range(6):
                U=[[rng.randint(1,7) for _ in range(r)] for _ in range(m)]
                V=[[rng.randint(1,7) for _ in range(r)] for _ in range(m)]
                out,grades=exterior_principal_rank(U,V,return_bases=True)
                closure_checks+=verify_all_subsets(U,V,grades)
                d,_=exhaustive_rank(U,V)
                assert out['principal_rank']==d, (m,r,trial,out,d)
                assert (out['witness_det']!=0)==(d>0)
                grade_counts[str(r)]=max(grade_counts.get(str(r),0),sum(out['dimensions']))
                count+=1
    signed_count=0
    for m in range(2,8):
        for r in range(1,min(m,4)+1):
            for trial in range(5):
                U=[[rng.randint(-4,4) for _ in range(r)] for _ in range(m)]
                V=[[rng.randint(-4,4) for _ in range(r)] for _ in range(m)]
                out=exterior_principal_rank(U,V)
                assert out['principal_rank']==exhaustive_rank(U,V)[0]
                signed_count+=1
    # A rank-one matrix with nonzero off-diagonal but all principal minors zero.
    nil_U=[[1],[0]];nil_V=[[0],[1]]
    nil=exterior_principal_rank(nil_U,nil_V)
    assert nil['principal_rank']==0 and exhaustive_rank(nil_U,nil_V)[0]==0
    examples={'zero_principal_rank_nilpotent':nil}
    U=[[1,1],[1,2],[1,3]]
    V=[[1,1],[1,2],[1,1]]
    out=exterior_principal_rank(U,V)
    assert out['principal_rank']==2
    examples['R284AL_cancellation']=out
    for k in (2,3,4):
        U,V=ak_factors(k)
        out=exterior_principal_rank(U,V)
        assert out['principal_rank']==2
        assert exhaustive_rank(U,V)[0]==2
        examples[f'R284AK_k{k}']=out
    U=[[rng.randint(1,100) for _ in range(3)] for _ in range(64)]
    V=[[rng.randint(1,100) for _ in range(3)] for _ in range(64)]
    long=exterior_principal_rank(U,V)
    assert long['principal_rank']==3
    result={"status":"PASS","signed_tests_exhaustive":signed_count,"arithmetic":"Python Fraction exact; independent brute-force determinants",
            "small_instance_subset_span_memberships":closure_checks, "seed":284013,
            "test_cases_exhaustive":count,"exhaustive_dimensions":"2<=m<=8, 1<=r<=min(4,m), six deterministic positive integer pairs per (m,r)",
            "grade_span_max_by_rank":grade_counts,"examples":examples,
            "long_case_m64_r3":long,"checker":"R284AM_exterior_span_principal_rank_checker.py",
            "theorem_review":"NOT_REVIEWED"}
    with open('/mnt/data/R284AM_exact_verification.json','w',encoding='utf-8') as fp:json.dump(result,fp,ensure_ascii=False,indent=2)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
