#!/usr/bin/env python3
"""R284AN: exact intrinsic-rank factor reduction and integer-primitive exterior-span DP.

Requires sympy for only exact input rank-factorization and independent test oracle.
The span phase uses integer arithmetic only. It retains each genuine named subset.
"""
from __future__ import annotations
from itertools import combinations
from math import comb, gcd, lcm
import json, random, time
from pathlib import Path
import sympy as sp


def intrinsic_factors(U,V):
    U=sp.Matrix(U); V=sp.Matrix(V)
    assert U.rows==V.rows and U.cols==V.cols
    # Do not form the m-by-m product.
    PU,AU=U.rank_decomposition()
    PV,AV=V.rank_decomposition()
    H=AU*AV.T
    if H.is_zero_matrix:
        return sp.zeros(U.rows,0),sp.zeros(U.rows,0)
    L,F=H.rank_decomposition()
    X,Y=PU*L, PV*F.T
    assert X.cols==Y.cols
    return X,Y


def integral_rows(M):
    ints=[]; denoms=[]
    for i in range(M.rows):
        den=1
        for x in M.row(i): den=lcm(den, int(sp.denom(x)))
        denoms.append(den)
        ints.append([int(den*x) for x in M.row(i)])
    return ints, denoms


def wedge_append(coeff,row,j,r,oldcols,newcols):
    oldidx={t:i for i,t in enumerate(oldcols)}
    out=[]
    for J in newcols:
        z=0
        for pos,k in enumerate(J):
            t=J[:pos]+J[pos+1:]
            z+=(-1 if (j-1-pos)%2 else 1)*coeff[oldidx[t]]*row[k]
        out.append(z)
    return tuple(out)


def primitive(v):
    g=0
    for x in v: g=gcd(g,abs(x))
    if not g: return tuple(v)
    w=tuple(x//g for x in v)
    first=next(x for x in w if x)
    return tuple(-x for x in w) if first<0 else w


class IntegerSpan:
    def __init__(self,n):
        self.n=n
        self.rows={} # pivot index -> primitive integral echelon row
        self.basis=[] # (named tuple, raw wedge_U, raw wedge_V), not arbitrary linear combos
        self.max_intermediate_bits=0
        self.reductions=0
    def reduce(self,vector):
        v=list(vector)
        self.max_intermediate_bits=max(self.max_intermediate_bits,max((abs(x).bit_length() for x in v),default=0))
        for p in sorted(self.rows):
            if v[p]:
                w=self.rows[p]
                a=v[p]; b=w[p]
                v=[b*x-a*y for x,y in zip(v,w)]
                v=list(primitive(v))
                self.max_intermediate_bits=max(self.max_intermediate_bits,max((abs(x).bit_length() for x in v),default=0))
                self.reductions+=1
        return tuple(v)
    def add(self,S,a,b):
        tensor=tuple(x*y for x in a for y in b)
        reduced=self.reduce(tensor)
        p=next((i for i,x in enumerate(reduced) if x),None)
        if p is None: return False
        self.rows[p]=primitive(reduced)
        self.basis.append((S,tuple(a),tuple(b)))
        return True
    def contains(self,vector):
        return not any(self.reduce(vector))


def solve(U,V, certify=False):
    U=sp.Matrix(U); V=sp.Matrix(V)
    m=U.rows
    X,Y=intrinsic_factors(U,V)
    k=X.cols
    xi,dx=integral_rows(X);yi,dy=integral_rows(Y)
    cols={j:list(combinations(range(k),j)) for j in range(k+1)}
    spans=[IntegerSpan(comb(k,j)**2) for j in range(k+1)]
    spans[0].add((),(1,),(1,))
    candidate_count=0
    t0=time.perf_counter()
    for i in range(m):
        for j in range(min(k,i+1),0,-1):
            for S,a,b in list(spans[j-1].basis):
                ta=wedge_append(a,xi[i],j,k,cols[j-1],cols[j]);tb=wedge_append(b,yi[i],j,k,cols[j-1],cols[j])
                spans[j].add(S+(i,),ta,tb)
                candidate_count+=1
    d=0; witness=None; det=None
    for j in range(1,k+1):
        for S,a,b in spans[j].basis:
            tr=sum(x*y for x,y in zip(a,b))
            if tr:
                d=j;witness=S
                divisor=1
                for i in S:divisor*=dx[i]*dy[i]
                det=sp.Rational(tr,divisor)
                break
    report={'status':'PASS','m':m,'input_factor_width':U.cols,'intrinsic_rank':k,
        'original_ambient':comb(2*U.cols,U.cols),'compressed_ambient':comb(2*k,k),
        'principal_rank':d,'witness_1based':([i+1 for i in witness] if witness else []),
        'witness_det':str(det) if det is not None else None,
        'basis_dimensions':[len(g.basis) for g in spans],
        'candidate_states':candidate_count,
        'max_intermediate_bits':max(g.max_intermediate_bits for g in spans),
        'integer_row_reductions':sum(g.reductions for g in spans),
        'span_elapsed_seconds':round(time.perf_counter()-t0,6),
        'higher_grade_zero_trace':all(all(sum(x*y for x,y in zip(a,b))==0 for _,a,b in spans[j].basis) for j in range(d+1,k+1))}
    if witness:
        C=U*V.T
        check=C.extract(list(witness),list(witness)).det(method='bareiss')
        assert det==check and det!=0
    if certify:
        report['named_basis_1based']=[[[i+1 for i in S] for S,_,_ in grade.basis] for grade in spans]
    return report,spans,(X,Y)


def exhaustive(U,V):
    C=sp.Matrix(U)*sp.Matrix(V).T
    d=0
    for j in range(1,min(C.rows,C.rank())+1):
        for S in combinations(range(C.rows),j):
            if C.extract(S,S).det(method='bareiss')!=0:d=j
    return d


def check_closure(X,Y,spans):
    m=X.rows;k=X.cols
    xi,_=integral_rows(X);yi,_=integral_rows(Y)
    cols={j:list(combinations(range(k),j)) for j in range(k+1)}
    seen=0
    for j in range(1,k+1):
        for S in combinations(range(m),j):
            a=(1,);b=(1,)
            for idx,t in enumerate(S):
                a=wedge_append(a,xi[t],idx+1,k,cols[idx],cols[idx+1]);b=wedge_append(b,yi[t],idx+1,k,cols[idx],cols[idx+1])
            assert spans[j].contains([x*y for x in a for y in b])
            seen+=1
    return seen


def run():
    rng=random.Random(284014)
    tests=0;closure=0; examples=[]
    for m in range(2,8):
        for r in range(1,min(m,4)+1):
            for trial in range(3):
                U=[[rng.randint(-4,7) for _ in range(r)] for __ in range(m)]
                V=[[rng.randint(-4,7) for _ in range(r)] for __ in range(m)]
                out,spans,(X,Y)=solve(U,V)
                assert out['principal_rank']==exhaustive(U,V),(m,r,trial,out)
                closure+=check_closure(X,Y,spans)
                tests+=1
    # Factor widths 3 and 8 but actual matrix rank 1 or 2.
    for m,r in ((12,8),(24,8),(32,10)):
        p=[rng.randint(1,9) for _ in range(m)];q=[rng.randint(1,9) for _ in range(m)]
        x=[rng.randint(1,9) for _ in range(m)];y=[rng.randint(1,9) for _ in range(m)]
        A=[[p[i],q[i]] for i in range(m)];B=[[x[i],y[i]] for i in range(m)]
        # Columns are different linear combinations; the C matrix stays rank 2.
        T=sp.Matrix([[1+z,z+2] for z in range(r)])
        # Use factors U=A T.T and V=B T.T ; C rank <=2.
        U=sp.Matrix(A)*T.T;V=sp.Matrix(B)*T.T
        out,_,_=solve(U,V)
        assert out['intrinsic_rank']==2 and out['principal_rank']==2
        examples.append(out)
    # Both factors rank 2, C rank only 1 (orthogonal coefficient spaces).
    m=5
    p=sp.Matrix([1,2,3,4,5]);q=sp.Matrix([2,3,5,7,11]);h=sp.Matrix([3,1,4,1,5]);z=sp.zeros(m,1)
    U=p.row_join(q).row_join(z)
    V=z.row_join(h).row_join(p)
    out,spans,(X,Y)=solve(U,V)
    assert U.rank()==V.rank()==2 and out['intrinsic_rank']==1 and out['principal_rank']==1
    examples.append(out)
    # Nilpotent C with no nonzero principal minor.
    U=[[1],[0]];V=[[0],[1]]
    out,spans,_=solve(U,V)
    assert out['principal_rank']==0 and out['intrinsic_rank']==1
    examples.append(out)
    result={'status':'PASS','checker':'R284AN_intrinsic_rank_fraction_free_checker.py',
            'arithmetic':'Integer-primitive fraction-free span; exact SymPy rational factor-rank decomposition and independent determinant oracle',
            'random_seed':284014,'exhaustive_small_instances':tests,'subset_closure_checks':closure,
            'examples':examples,'review':'NOT_REVIEWED'}
    with open(Path(__file__).with_name('R284AN_exact_verification.json'),'w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
