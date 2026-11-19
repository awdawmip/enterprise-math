#!/usr/bin/env python3
"""Exact-rational verification of R284AK, positive nonsymmetric two-sided factor family.
No stochastic dependency, no floating-point arithmetic, auxiliary Port pencil only.
"""
from itertools import combinations
import json
import sympy as sp


def make(k):
    assert k >= 2
    a = [1] * (k+1)
    # U top block has repeated rows; V bottom block has repeated rows.
    e = [a[:j+1] + [2] + a[j+2:] for j in range(k)]
    U = sp.Matrix([a for _ in range(k)] + e)
    V = sp.Matrix(e + [a for _ in range(k)])
    C = U * V.T
    return U,V,C


def formula(k, x):
    m=2*k
    p=sp.prod(x)
    first=-(k+2)*sum(sp.prod(x[j] for j in range(m) if j != i) for i in range(m))
    second=sum((1-(k+1)*(i==j))*sp.prod(x[l] for l in range(m) if l != i and l != k+j) for i in range(k) for j in range(k))
    return p+first+second


def check_port(k, C):
    m=2*k; q=2*m; K=q+1
    N=sp.BlockMatrix([[sp.zeros(m),sp.eye(m)],[C,sp.zeros(m)]]).as_explicit()
    R=max(sum(N[i,j] for j in range(q)) for i in range(q))
    c=sp.Rational(1,16*(K+R+1)); g=sp.Rational(1,16)
    delta=sp.Rational(1,256*K)
    t=[c*sp.Rational((i%3)+1,4) for i in range(q)]
    H=c*sp.ones(K)+c*sp.diag(N,sp.zeros(1))+sp.diag(*t,0)
    B=sp.eye(K)-delta*sp.ones(K)
    A=sp.BlockMatrix([[B,-H,sp.zeros(K)],
                      [-delta*sp.ones(K),B,-g*sp.eye(K)],
                      [-g*sp.eye(K),sp.zeros(K),sp.zeros(K)]]).as_explicit()
    x=[t[i]*t[i+m] for i in range(m)]
    scaled=sp.prod(x)-(k+2)*c**2*sum(sp.prod(x[j] for j in range(m) if j!=i) for i in range(m))
    scaled+=c**4*sum((1-(k+1)*(i==j))*sp.prod(x[z] for z in range(m) if z!=i and z!=k+j) for i in range(k) for j in range(k))
    expected=(-1)**K*g**(2*K)*c*scaled
    observed=A.det(method='domain-ge')
    assert observed==expected, (k,observed,expected)
    assert max(sum(H[i,j] for j in range(K)) for i in range(K)) < 1
    assert min(H)>0
    assert delta*K+g<1
    return (3*K,observed!=0)


def check():
    detail=[]; total_minor=0; total_full=0; total_coefficient=0; port_checks=0
    for k in [2,3,4,5]:
        m=2*k
        U,V,C=make(k)
        assert U.rank()==V.rank()==C.rank()==k+1
        assert all(int(C[i,j])>0 for i in range(m) for j in range(m))
        minors_by_order={}
        for d in range(m+1):
            nonzero=0
            for I in combinations(range(m),d):
                minor= C.extract(I,I).det() if I else 1
                if minor != 0: nonzero+=1
                if d>=3: assert minor==0,(k,I,minor)
                if d==2:
                    cross=(I[0]<k<=I[1]); expect=(1-(k+1)*(I[0]==I[1]-k)) if cross else 0
                    assert minor==expect,(k,I,minor,expect)
                if d==1: assert minor==k+2
                total_minor+=1
            minors_by_order[str(d)]=nonzero
        assert minors_by_order['2']==k*k
        assert all(count==0 for d,count in minors_by_order.items() if int(d)>2)
        for test_idx in range(3):
            # Full, independently evaluated 4k-by-4k block determinant.
            u=[sp.Rational((i+test_idx)%4,5) for i in range(m)]
            v=[sp.Rational((2*i+test_idx+1)%5,7) for i in range(m)]
            x=[u[i]*v[i] for i in range(m)]
            Du=sp.diag(*u); Dv=sp.diag(*v)
            direct=sp.det(sp.BlockMatrix([[Du,sp.eye(m)],[C,Dv]]).as_explicit())
            predicted=formula(k,x)
            assert direct==predicted,(k,test_idx,direct,predicted)
            total_full+=1
        for i in range(k):
            for j in range(k):
                I=[i,k+j]
                assert C.extract(I,I).det()==1-(k+1)*(i==j)
                total_coefficient+=1
        port_dim,port_nonzero=check_port(k,C)
        port_checks+=1
        detail.append({'port_matrix_order':port_dim,'port_determinant_nonzero':bool(port_nonzero),'k':k,'m':m,'rank_C':int(C.rank()),'corank_pencil':k-1,
                       'principal_order':2,'first_degree':4*k-4,'rank_lower_bound':2*(k-1),
                       'degree_gap':2*(k-1), 'principal_nonzero_counts':minors_by_order,
                       'full_block_checks':3})
    result={'result':'PASS','arithmetic':'exact sympy Rational/Integer',
            'coverage':'k=2..5; all 2^(2k) principal subsets; 3 full block samples/k',
            'principal_minors_checked':total_minor,'full_block_determinants_checked':total_full,
            'cross_pair_coefficient_checks':total_coefficient,
            'complete_port_checks':port_checks,'families':detail,
            'independent_review':'NOT_REVIEWED'}
    return result


if __name__=='__main__':
    print(json.dumps(check(),ensure_ascii=False,sort_keys=True,indent=2))
