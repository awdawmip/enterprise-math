#!/usr/bin/env python3
"""C306 author-level exact verification: factorization-free support-optimal Newton residues.

Mathematical result: for P in Z[t], deg <= d, gcd(s,content(P))
is determined by P(T+j) mod s*(d!)_supp(s), 0<=j<=d; this uniform
modulus is componentwise minimal. This file computes the 125 auxiliary
path applications conditional on the upstream C300 polynomial identity.
"""
from __future__ import annotations
import argparse, json, hashlib, os, sys, time
from math import factorial, gcd
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import C305_MODULAR_NEWTON_CONTENT as base


def supported_part(n:int, s:int)->tuple[int,int]:
    """Return (supported part of n for primes dividing s, gcd peeling rounds)."""
    if n<1 or s<1: raise ValueError('positive integers required')
    h=1; rem=n; rounds=0
    while rem>1:
        g=gcd(rem,s)
        if g==1: break
        h*=g;rem//=g;rounds+=1
    assert n%h==0 and gcd(rem,s)==1
    return h,rounds


def optimal_newton_gcd(s:int,d:int,values:list[int],M:int,h:int)->int:
    if s<1 or len(values)!=d+1 or M!=s*h:
        raise ValueError('bad Newton inputs')
    if s==1:return 1
    row=list(values); fact=1; out=s
    for k in range(d+1):
        if k: fact*=k
        a=gcd(fact,h)
        b=fact//a
        assert gcd(b,s)==1
        # Current row[0] is Delta^k P(T) modulo M.
        delta=row[0]
        assert delta%a==0, (k,a,delta)
        beta=((delta//a)*pow(b,-1,s))%s
        out=gcd(out,beta)
        if k<d:
            row=[(row[j+1]-row[j])%M for j in range(len(row)-1)]
    return out


def factorized_residues(s,groups,terms,cancels,d,T,M):
    vals=[]
    eval_p=base.eval_p
    for t in range(T,T+d+1):
        qv={q:eval_p(q,t) for q in groups}
        assert all(qv.values()), (t,'denominator zero')
        Q=1
        for q,e in groups.items():Q*=qv[q]**e
        c=eval_p(cancels[0],t)*eval_p(cancels[1],t)
        assert c!=0
        N=M*abs(c)
        v=0
        for coeff,nums,power in terms:
            qden=1
            for q,e in power.items():qden*=qv[q]**e
            assert Q%qden==0
            term=(coeff*(Q//qden))%N
            for n in nums:term=(term*eval_p(n,t))%N
            v=(v+term)%N
        assert v%abs(c)==0
        z=(v//abs(c))%M
        if c<0:z=(-z)%M
        vals.append(z)
    return vals


def run_one(i,paths,W,ref):
    st=time.monotonic()
    k24=int(ref['records'][i][1]);path=paths[i]
    s,groups,terms,cancels,d=base.prepare(i,path,k24,W)
    f=factorial(d);h,rounds=supported_part(f,s)
    M=s*h;old=s*f
    T=base.window_start(groups,d)
    residues=factorized_residues(s,groups,terms,cancels,d,T,M)
    g=optimal_newton_gcd(s,d,residues,M,h)
    oldrow=REF_ROWS[i]
    assert oldrow['index']==i and oldrow['degree']==d
    assert oldrow['content_gcd_dec']==str(g),(i,'C305 mismatch')
    assert oldrow['scalar_bit_length']==s.bit_length()
    assert oldrow['modulus_bit_length']==old.bit_length()
    return {
        'index':i,'degree':d,'sample_start':T,'sample_count':d+1,
        'scalar_bit_length':s.bit_length(),'factorial_bit_length':f.bit_length(),
        'supported_factorial_bit_length':h.bit_length(),'gcd_peel_rounds':rounds,
        'old_modulus_bit_length':old.bit_length(),
        'new_modulus_bit_length':M.bit_length(),
        'modulus_bit_reduction':old.bit_length()-M.bit_length(),
        'gcd_decimal':str(g),
        'reference_C305_exact_gcd_match':True,
        'newton_coefficient_count':d+1,
        'elapsed_seconds_observed':round(time.monotonic()-st,3),
    }


def run(indices,output):
    ref=json.loads((ROOT/'EM_C301_EXACT_PORTABLE/C293_125_REFINED_BRACKETS.json').read_text())
    assert len(ref['records'])==125
    paths,_=base.c288.build_paths()
    W,_=base.src.floor_fixed_masses()
    rows=[]
    for i in indices:
        row=run_one(i,paths,W,ref)
        print('C306_OPTIMAL_SUPPORT_PASS',i,'old',row['old_modulus_bit_length'],'new',row['new_modulus_bit_length'],'saved',row['modulus_bit_reduction'], 'sec',row['elapsed_seconds_observed'], flush=True)
        rows.append(row)
    obj={
        'schema':'C306_SUPPORT_OPTIMAL_MODULAR_NEWTON_AUTHOR_AUDIT_V1',
        'classification':'AUTHOR_EXACT_NOT_NATIVE_ADMITTED',
        'scope':'C195/H168 79-positive-rational-branch auxiliary on C293 frozen 125 paths',
        'source_C293_records_sha256':ref['records_sha256'],
        'compared_to':'C305_AUTHOR_COMPLETE_MODULAR_NEWTON_AUDIT_20261025.json',
        'path_count_checked':len(rows),
        'rows':rows,
        'limitations':'C300 polynomial cancellation identity is upstream author-level; no native X6/BRC or signed-phase equivalence; no formal Source/Driver review.'
    }
    Path(output).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print('C306_AUTHOR_EXACT_PASS',len(rows),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--indices',default='0,28,63')
    parser.add_argument('--output',default='C306_AUDIT.json')
    args=parser.parse_args()
    with open(ROOT/'C305_AUTHOR_COMPLETE_MODULAR_NEWTON_AUDIT_20261025.json') as f:
        REF_ROWS=json.load(f)['rows']
    ids=list(range(125)) if args.indices=='all' else [int(x) for x in args.indices.split(',')]
    run(ids,args.output)
