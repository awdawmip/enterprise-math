#!/usr/bin/env python3
"""R329 independent exact signed-tail BRC polynomial recurrence cross-check.
Runs separate from r329_symbolic.py; does not evaluate its rational K/A construction.
No native-time/phase or physical-model interpretation.
"""
from math import comb
from fractions import Fraction
import json, argparse, hashlib

def C(n,k):return comb(n,k) if 0<=k<=n else 0

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def scale(a,v):return [v*x for x in a]

def times(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:c[i+j]+=v*w
    return c

def power_one_plus_t(n):
    assert n>=0
    return [C(n,k) for k in range(n+1)]

def shift(a,n):return [0]*n+a

def build_K(i):
    d=[-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2), C(7,i-2),-C(9,i-3)]
    terms=[[0]]
    p=[0]
    for j,v in enumerate(d,1):
        if v:
            assert i+1-j>=0
            p=add(p,scale(power_one_plus_t(i+1-j),-v))
    return shift(p,i-1)

def build_J(s):
    terms=[(-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)]
    p=[0]
    for v,e in terms:
        if v:
            assert e>=0
            p=add(p,scale(power_one_plus_t(e),v))
    return shift(p,s)

def compute_B(max_s):
    kernels=[None]+[build_K(i) for i in range(1,13)]
    b=[[1,1]]
    for s in range(1,max_s+1):
        poly=build_J(s)
        for i in range(1,min(s,12)+1):
            poly=add(poly,times(kernels[i],b[s-i]))
        b.append(poly)
    return b

def eval_shift(coeffs_desc,u):
    result=Fraction(0)
    for coeff in coeffs_desc:
        result=result*u+Fraction(coeff)
    return result

def verify(Q,table):
    b=compute_B(2*Q)
    assert b[0]==[1,1]
    triangle_count=0
    signed_tail_neg=0
    for s,poly in enumerate(b):
        for q in range(s+1):
            assert q<len(poly) and poly[q]>0,(s,q)
            triangle_count+=1
        signed_tail_neg+=sum(c<0 for c in poly[s+1:])
    exact_matches=0
    differences_checked=0
    min_d=None
    first_d=[]
    h=hashlib.sha256()
    for q in range(Q+1):
        n=[2**(q-u)*b[q+u][q] for u in range(q+1)]
        assert all(type(x)==int for x in n)
        diffs=[]
        while n:
            diffs.append(n[0]);n=[n[i+1]-n[i] for i in range(len(n)-1)]
        assert all(d>0 for d in diffs),('negative D',q)
        differences_checked+=len(diffs)
        for k,d in enumerate(diffs):h.update(f'{q},{k},{d}\n'.encode())
        for r in range(min(q,len(table)-1)+1):
            k=q-r
            predicted=Fraction(5)**k*eval_shift(table[r]['shift_coeffs'],q-r)
            assert predicted.denominator==1 and predicted.numerator==diffs[k],(q,r,predicted,diffs[k])
            exact_matches+=1
            if q==r and r>=5:first_d.append({'r':r,'D_at_q_eq_r':str(diffs[k])})
    return {'schema':'EM_R329_INDEPENDENT_INTEGER_V1','max_q':Q,'max_s':2*Q,
         'signed_outside_triangle_negative_coefficients':signed_tail_neg,
         'triangle_positive_checks':triangle_count,
         'newton_positive_checks':differences_checked,
         'diagonal_exact_matches':exact_matches,
         'newton_values_sha256':h.hexdigest(),'diagonal_q_eq_r':first_d,
         'status':'PASS','integer_semantics':'Python arbitrary precision, no float',
         'limitations':'Finite recurrence cross-check through q <= Q only; unbounded proof is symbolic finite-diagonal positive-shift argument.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--q',type=int,default=48);p.add_argument('--symbolic',required=True);p.add_argument('--json',required=True);args=p.parse_args()
    tbl=json.load(open(args.symbolic))['results']
    out=verify(args.q,tbl)
    with open(args.json,'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))
