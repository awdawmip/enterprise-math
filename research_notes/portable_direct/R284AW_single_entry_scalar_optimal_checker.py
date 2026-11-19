#!/usr/bin/env python3
"""Exact integer checker for R284AW. Python standard library only."""
import hashlib
import itertools
import json
import random
from pathlib import Path
from math import factorial

def det_bareiss(matrix):
    n = len(matrix)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in matrix]
    sign = 1
    old = 1
    for k in range(n-1):
        if a[k][k] == 0:
            z = next((j for j in range(k+1,n) if a[j][k]), None)
            if z is None:
                return 0
            a[k], a[z] = a[z], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                assert num % old == 0
                a[i][j] = num//old
            a[i][k] = 0
        old = pivot
    return sign*a[n-1][n-1]

def weights_b3(n):
    w=[]
    for t in range(n):
        forbidden=set()
        for k in (1,2,3):
            if k <= t:
                for a in itertools.combinations(w,k-1):
                    sa=sum(a)
                    for b in itertools.combinations(w,k):
                        forbidden.add(sum(b)-sa)
        candidate=(w[-1]+1) if w else 1
        while candidate in forbidden:
            candidate+=1
        w.append(candidate)
    for k in (1,2,3):
        if k<=n:
            ss=[sum(t) for t in itertools.combinations(w,k)]
            assert len(ss)==len(set(ss))
    return w

def balanced_digits(z, base):
    assert base & (base-1)==0
    result={}
    i=0
    while z:
        div,rem=divmod(z,base)
        if rem>=base//2:
            rem-=base
            div+=1
        if rem:
            result[i]=rem
        z=div
        i+=1
    return result

def measurements_and_recover(C,H):
    n=len(C)
    assert n>=2 and H>=1 and all(1<=a<=H for row in C for a in row)
    weights=weights_b3(n)
    W=1+sum(weights)
    def exponents(subset):
        return len(subset)*W+sum(weights[i] for i in subset)
    emax=exponents(tuple(range(n)))
    A=(2**n)*factorial(n)*(H**n)
    B=1<<(2*A).bit_length()
    assert B>2*A
    R=emax+1
    D=[B**(W+w) for w in weights]
    def measure(v,z):
        matrix=[[(-C[i][j]+(D[i] if i==j else 0)) for j in range(n)] for i in range(n)]
        matrix[0][v]-=z
        return det_bareiss(matrix)
    y={1:measure(1,B**R)}
    for v in range(2,n):
        y[v]=measure(v,1)
    digits=balanced_digits(y[1],B)
    baseline_digits={j:val for j,val in digits.items() if j<R}
    first_response_digits={j-R:val for j,val in digits.items() if j>=R}
    def coeff(digit_map, absent):
        keep=tuple(j for j in range(n) if j not in absent)
        return digit_map.get(exponents(keep),0)
    diagonal=[-coeff(baseline_digits,{i}) for i in range(n)]
    recovered=[[0]*n for _ in range(n)]
    for i in range(n):
        recovered[i][i]=diagonal[i]
    pairs={}
    for i in range(n):
        for j in range(i+1,n):
            pairs[(i,j)]=diagonal[i]*diagonal[j]-coeff(baseline_digits,{i,j})
    responses={1:first_response_digits}
    y0=sum(c*(B**e) for e,c in baseline_digits.items())
    assert y0 + sum(c*B**(e+R) for e,c in first_response_digits.items())==y[1]
    for v in range(2,n):
        responses[v]=balanced_digits(y[v]-y0,B)
    for v in range(1,n):
        val=-coeff(responses[v],{0,v})
        assert val>0
        recovered[v][0]=val
        p=pairs[(0,v)]
        assert p%val==0
        recovered[0][v]=p//val
    for i in range(1,n):
        for j in range(i+1,n):
            q=diagonal[j]*recovered[i][0]-coeff(responses[i],{0,i,j})
            assert q%recovered[j][0]==0
            x=q//recovered[j][0]
            assert x>0
            recovered[i][j]=x
            assert pairs[(i,j)]%x==0
            recovered[j][i]=pairs[(i,j)]//x
    assert recovered==C
    return {'n':n,'H':H,'queries':len(y),'base_bits':B.bit_length()-1,
            'separator_shift':R,'max_diagonal_bits':max(z.bit_length() for z in D),
            'max_query_bits':max(z.bit_length() for z in y.values()),
            'weights':weights,'matrix':C,'readings_sha256':hashlib.sha256(json.dumps(y,sort_keys=True).encode()).hexdigest()}

def indistinguishability_witness(n, edges, H=4):
    comp=list(range(n))
    def root(x):
        while comp[x]!=x:
            comp[x]=comp[comp[x]]
            x=comp[x]
        return x
    for a,b in edges:
        ra,rb=root(a),root(b)
        if ra!=rb:
            comp[rb]=ra
    groups=[root(i) for i in range(n)]
    assert len(set(groups))>=2
    base=groups[0]
    t=[2 if group==base else 1 for group in groups]
    C=[[2]*n for _ in range(n)]
    Cp=[[2*t[i]//t[j] for j in range(n)] for i in range(n)]
    assert C!=Cp and all(1<=a<=H for row in Cp for a in row)
    for a,b in edges:
        assert t[a]==t[b]
    return C,Cp

def main():
    rng=random.Random(2842719)
    cases=[]
    for n,num in [(2,12),(3,28),(4,24),(5,10),(6,4)]:
        for k in range(num):
            H=rng.randint(2,4)
            C=[[rng.randint(1,H) for _ in range(n)] for _ in range(n)]
            cases.append(measurements_and_recover(C,H))
    for arr in itertools.product((1,2),repeat=9):
        C=[list(arr[i*3:(i+1)*3]) for i in range(3)]
        cases.append(measurements_and_recover(C,2))
    lower=0
    for n in range(3,8):
        edges=[(i,i+1) for i in range(n-2)]
        C,Cp=indistinguishability_witness(n,edges,4)
        for _ in range(15):
            D=[rng.randint(0,35) for _ in range(n)]
            v=rng.choice(edges)
            z=rng.randint(-20,20)
            def f(A):
                M=[[D[i]*(i==j)-A[i][j] - (z if (i,j)==v else 0) for j in range(n)] for i in range(n)]
                return det_bareiss(M)
            assert f(C)==f(Cp)
            lower+=1
    report={
        'research_unit':'R284AW','status':'PASS','seed':2842719,
        'exact_integer_reconstructions':len(cases),
        'exhaustive_3x3_binary_matrices':512,
        'adaptive_lower_bound_test_readings':lower,
        'query_counts_by_dimension':{str(n):n-1 for n in range(2,7)},
        'max_diagonal_bits':max(c['max_diagonal_bits'] for c in cases),
        'max_query_bits':max(c['max_query_bits'] for c in cases),
        'exemplar':cases[0],
        'implementation':'Python standard library integer Bareiss; balanced signed radix',
        'logical_scope':'finite testing; theorem proof supplied separately',
        'independent_review':'NOT_REVIEWED'
    }
    with (Path(__file__).with_name('R284AW_single_entry_scalar_optimal_verification.json')).open('w',encoding='utf-8') as f:
        json.dump(report,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:v for k,v in report.items() if k!='exemplar'},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
