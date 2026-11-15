#!/usr/bin/env python3
"""R192: exact finite evidence for source-last-occurrence affine representations.
Uses integer arithmetic only; no P000 physical dynamics or native BRC updates are simulated.
"""
import itertools
import json
from math import comb
from pathlib import Path


def states(k):
    a = list(range(k))
    return [p for r in range(k+1) for p in itertools.permutations(a,r)]


def star(p,q):
    t=set(q)
    return tuple(x for x in p if x not in t)+tuple(q)


def features(k):
    return [(i,) for i in range(k)]+list(itertools.combinations(range(k),2))


def observe(p,U):
    for x in reversed(p):
        if x in U:
            return x+1
    return 0


def vector(p,F):
    return tuple(observe(p,U) for U in F)


def affine(p,F):
    # R183 action induced by a whole word p: x -> diag*x + shift
    support=set(p)
    d=tuple(0 if support.intersection(U) else 1 for U in F)
    b=vector(p,F)
    return d,b


def then(a,b):
    d1,v1=a; d2,v2=b
    return tuple(x*y for x,y in zip(d2,d1)),tuple(x*y+z for x,y,z in zip(d2,v1,v2))


def rank_int(matrix):
    """Exact rational rank via Fraction-free integer elimination over Q."""
    A=[list(row) for row in matrix]
    if not A: return 0
    m=len(A);n=len(A[0]);r=0
    for col in range(n):
        pivot=next((t for t in range(r,m) if A[t][col]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        a=A[r][col]
        for t in range(r+1,m):
            if A[t][col]:
                c=A[t][col]
                A[t]=[a*A[t][z]-c*A[r][z] for z in range(n)]
                # divide by a common gcd for fast exact elimination
                from math import gcd
                g=0
                for u in A[t]: g=gcd(g,abs(u))
                if g>1: A[t]=[u//g for u in A[t]]
        r+=1
        if r==m: break
    return r


def witness_rows(k):
    F=features(k)
    # Baseline, k singleton states, and binom(k,2) pair antisymmetric differences.
    rows=[(1,*vector((),F))]
    rows.extend((1,*vector((i,),F)) for i in range(k))
    for i,j in itertools.combinations(range(k),2):
        v=vector((i,j),F);w=vector((j,i),F)
        rows.append((0,*(x-y for x,y in zip(v,w))))
    return rows


def verify(k):
    F=features(k);S=states(k)
    mat={s:affine(s,F) for s in S}
    assert len(mat)==len(S)==sum(__import__('math').factorial(k)//__import__('math').factorial(k-r) for r in range(k+1))
    assert len(set(mat.values()))==len(S)
    assert all(mat[s][1]==vector(s,F) for s in S)
    comp=0
    for p in S:
        for q in S:
            assert then(mat[p],mat[q])==mat[star(p,q)]
            comp+=1
    return {"k":k,"states":len(S),"features":len(F),"affine_product_checks":comp,"distinct_actions":len(set(mat.values())),"status":"PASS"}


def main():
    semigroup=[verify(k) for k in range(1,6)]
    ranks=[]
    for k in range(1,11):
        d=k+comb(k,2)
        rank=rank_int(witness_rows(k))
        assert rank==d+1
        ranks.append({"k":k,"observer_features":d,"witness_matrix_rank":rank,"expected_rank":d+1})
    # The k=2 R183 realization has full 3-dimensional affine orbit.
    F=features(2)
    orbit=[vector(s,F) for s in [(),(0,),(1,),(0,1),(1,0)]]
    assert rank_int([[x-y for x,y in zip(p,orbit[0])] for p in orbit[1:]])==3
    # Explicit right regular band relations hold in the k=2 action.
    a=affine((0,),F);b=affine((1,),F)
    assert then(then(a,b),a)==then(b,a)
    assert then(then(b,a),b)==then(a,b)
    assert then(a,a)==a and then(b,b)==b
    result={
        "schema":"EM_R192_EXACT_EVIDENCE_V1",
        "result":"R192_AFFINE_QUERY_MINIMALITY_PASS",
        "date":"2026-11-16",
        "scientific_input_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        "method":"exact integer rank and full finite semigroup action enumeration",
        "semigroup_checks":semigroup,
        "linear_readout_witness_ranks":ranks,
        "total_semigroup_product_checks":sum(x["affine_product_checks"] for x in semigroup),
        "k2_orbit_affine_rank":3,
        "k2_converse":"symbolic geometric proof in companion Markdown; finite testing is not the general lower-bound proof",
        "project_native_brc_execution":"NOT_EXECUTED",
        "independent_review":"NOT_REVIEWED",
    }
    outfile=Path(__file__).with_name('R192_verification.json')
    outfile.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({"result":result["result"],"checks":result["total_semigroup_product_checks"],"rank_k_max":ranks[-1]},ensure_ascii=False))


if __name__=='__main__':main()
