#!/usr/bin/env python3
"""Exact integer certificate for historical A3 weighted-relation closure vs integral lift.

Domain: capacities (m_i) in {1,2,3}^n, n=2 or 3;
all independent antisymmetric entries in [-5,5]; closure computed over Z.
Two independent decision tests: row-sum modular congruences C (mod M),
and a pivot congruence t (mod m_0). Neither assumes source code correctness.
"""
import itertools
import json
from math import gcd
from functools import reduce
from collections import Counter
from pathlib import Path


def closed(m, z):
    n=len(m)
    return all(z[i][i]==0 for i in range(n)) and all(
        z[i][j]==-z[j][i] and
        all(m[k]*z[i][j]+m[i]*z[j][k]+m[j]*z[k][i]==0 for k in range(n))
        for i in range(n) for j in range(n)
    )

def field(m,c):
    return tuple(tuple(m[j]*c[i]-m[i]*c[j] for j in range(len(m))) for i in range(len(m)))

def c_by_rows(m,z):
    M=sum(m); row=[sum(z[i]) for i in range(len(m))]
    for C in range(M):
        if all((m[i]*C+row[i])%M==0 for i in range(len(m))):
            c=tuple((m[i]*C+row[i])//M for i in range(len(m)))
            assert sum(c)==C
            assert field(m,c)==z
            return (C,c)
    return None

def c_by_pivot(m,z):
    for t in range(m[0]):
        if all((z[i][0]+m[i]*t)%m[0]==0 for i in range(len(m))):
            c=tuple((z[i][0]+m[i]*t)//m[0] for i in range(len(m)))
            assert c[0]==t
            assert field(m,c)==z
            return c
    return None

def make_field(n, values):
    z=[[0]*n for _ in range(n)]; idx=0
    for i in range(n):
        for j in range(i+1,n):
            z[i][j]=values[idx]; z[j][i]=-values[idx]; idx+=1
    return tuple(tuple(r) for r in z)

def main():
    stats=Counter(); examples=[]
    for n in (2,3):
        k=n*(n-1)//2
        for m in itertools.product((1,2,3),repeat=n):
            for vals in itertools.product(range(-5,6),repeat=k):
                stats['all_antisym_'+str(n)]+=1
                z=make_field(n,vals)
                if not closed(m,z):
                    continue
                stats['closed_'+str(n)]+=1
                by_rows=c_by_rows(m,z)
                by_pivot=c_by_pivot(m,z)
                if (by_rows is None)!=(by_pivot is None):
                    raise AssertionError((m,z,by_rows,by_pivot))
                g=reduce(gcd,m)
                gcd_rule=all(z[i][j]%g==0 for i in range(n) for j in range(n))
                if gcd_rule!=(by_rows is not None):
                    raise AssertionError(("gcd_lift_disagreement",m,z,by_rows,g))
                status='integral_'+str(n) if by_rows is not None else 'closed_not_integral_'+str(n)
                stats[status]+=1
                if by_rows is None and len(examples)<12:
                    examples.append({'m':m,'z':z})
    m=(2,2); z=((0,1),(-1,0))
    assert closed(m,z) and c_by_rows(m,z) is None and c_by_pivot(m,z) is None
    one=((0,),)
    assert closed((4,),one) and c_by_rows((4,),one) is not None
    out={'schema':'X6_UNIT165_A3_INTEGRAL_LIFT_EXACT_FINITE_CERT_V1',
         'frozen_comparison_commit':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
         'domain':'n in {2,3}, m_i in {1,2,3}, antisymmetric independent z_ij in [-5,5]',
         'algorithm':'Exhaust all antisymmetric arrays; among weighted-closed compare row-sum C mod M with independent pivot t mod m0 and gcd(m_i) divisibility of every Z_ij; construct and validate all satisfiable c',
         'new_universal_criterion':'A closed antisymmetric integral Z admits integral totals c iff gcd(m_1,...,m_n) divides every Z_ij. For a lift c0 all lifts are c0 + t*(m/g), t integer; compatible grand totals have residue C0 mod M/g.',
         'counts':dict(sorted(stats.items())),
         'counterexample':{'capacities':[2,2], 'field':[[0,1],[-1,0]],'closed':True, 'integer_lift':False, 'coarsened_to_single_group':{'capacities':[4], 'field':[[0]],'integer_lift':True}},
         'sample_unliftable':examples,'violations':0, 'status':'PASS',
         'no_original_native_R063_benchmark_execution':True}
    file=Path(__file__).with_name('X6_UNIT165_WEIGHTED_RELATION_INTEGRAL_LIFT_RESULTS_20261119.json')
    file.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','counts':out['counts'],'file':str(file)}))

if __name__=='__main__':main()
