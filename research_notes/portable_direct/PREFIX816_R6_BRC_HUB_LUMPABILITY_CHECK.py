#!/usr/bin/env python3
"""Exact integer exhaustive checker for PREFIX-816. Python standard library only."""
import json
from itertools import product, combinations


def states(m,q):
    return tuple(s for s in range(1<<m) if s.bit_count()<=q)


def edge_weights(s,m,q,alpha,beta):
    out={}
    for i in range(m):
        t=s^(1<<i)
        if s&(1<<i):
            out[t]=beta[i]
        elif s.bit_count()<q:
            out[t]=alpha[i]
    return out


def row_by_level(s,m,q,alpha,beta):
    row=[0]*(q+1)
    for t,v in edge_weights(s,m,q,alpha,beta).items():
        row[t.bit_count()]+=v
    return tuple(row)


def is_lumpable(m,q,alpha,beta):
    seen={}
    for s in states(m,q):
        k=s.bit_count(); row=row_by_level(s,m,q,alpha,beta)
        if k in seen and seen[k]!=row: return False
        seen[k]=row
    return True


def prediction(m,q,alpha,beta):
    if m==1 or q==0: return True
    if len(set(beta))!=1: return False
    return q==1 or len(set(alpha))==1


def path_levels(s,m,q,alpha,beta,h):
    current={s:1}
    for _ in range(h):
        nxt={}
        for x,w in current.items():
            for y,v in edge_weights(x,m,q,alpha,beta).items():
                nxt[y]=nxt.get(y,0)+w*v
        current=nxt
    z=[0]*(q+1)
    for x,w in current.items(): z[x.bit_count()]+=w
    return tuple(z)


def quotient(m,q,alpha,beta):
    rows=[]
    for k in range(q+1):
        row=[0]*(q+1)
        if k>0: row[k-1]=k*beta[0]
        if k<q: row[k+1]=sum(alpha) if q==1 else (m-k)*alpha[0]
        rows.append(tuple(row))
    return tuple(rows)


def quotient_path(k,B,h):
    n=len(B); v=[0]*n; v[k]=1
    for _ in range(h):
        v=[sum(v[i]*B[i][j] for i in range(n)) for j in range(n)]
    return tuple(v)


def main():
    checked=0; true_cases=0; false_cases=0; trajectory_checks=0
    per_dimension={}
    for m in range(2,5):
        local=0
        for q in range(m+1):
            for a in product(range(3),repeat=m):
                for b in product(range(3),repeat=m):
                    actual=is_lumpable(m,q,a,b)
                    predicted=prediction(m,q,a,b)
                    assert actual==predicted, (m,q,a,b,actual,predicted)
                    checked+=1; local+=1
                    if actual: true_cases+=1
                    else: false_cases+=1
                    if actual and (checked % 19==0 or m==2 and q==1):
                        B=quotient(m,q,a,b)
                        for s in states(m,q):
                            for h in range(5):
                                assert path_levels(s,m,q,a,b,h)==quotient_path(s.bit_count(),B,h)
                                trajectory_checks+=1
        per_dimension[str(m)]=local
    # Explicit sharp witnesses, including the exceptional q=1 regime.
    assert is_lumpable(3,1,(1,2,3),(2,2,2))
    assert quotient(3,1,(1,2,3),(2,2,2))==((0,6),(2,0))
    assert not is_lumpable(3,1,(1,2,3),(1,2,1))
    assert row_by_level(1,3,2,(1,2,1),(1,1,1))[2]==3
    assert row_by_level(2,3,2,(1,2,1),(1,1,1))[2]==2
    result={
      'schema':'ENTERPRISE_MATH_PREFIX816_EXACT_CHECK_V1',
      'proof_target':'exact strong cardinality lumpability of BRC hub toggle graph',
      'domain':{'m':[2,3,4],'q':'all 0..m','alpha_beta_values':[0,1,2], 'paths_h':[0,1,2,3,4]},
      'all_weight_patterns_checked':checked,
      'lumpable_cases':true_cases,
      'non_lumpable_cases':false_cases,
      'per_m_checks':per_dimension,
      'trajectory_assertions':trajectory_checks,
      'zero_failures':True,
      'counterexamples':{'q1_nonuniform_birth_lumpable':{'alpha':[1,2,3],'beta':[2,2,2],'B':[[0,6],[2,0]]},'q2_nonuniform_birth_nolump':{'alpha':[1,2,1],'beta':[1,1,1],'birth_from_singleton0':3,'birth_from_singleton1':2}},
      'scope':'finite exhaustive unit test; general theorem established by separate proof'
    }
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
