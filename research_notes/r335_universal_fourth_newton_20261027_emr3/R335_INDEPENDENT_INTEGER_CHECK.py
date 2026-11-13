#!/usr/bin/env python3
"""Independent coefficient test directly from the original signed K/J B_s recurrence.

No symbolic-proof imports. Pure Python integers/Fraction, full signed tails kept.
This is a finite cross-check and not a proof of the all-r identity by itself.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from math import comb


def C(n,k): return comb(n,k) if 0 <= k <= n else 0

def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if not v:continue
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def term(n,coef,shift):
    return [0]*shift+[coef*C(n,j) for j in range(n+1)] if n>=0 else [0]

def K(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    out=[0]
    for j,v in enumerate(d,1):
        if v:out=add(out,term(i+1-j,-v,i-1))
    return out

def J(i):
    out=[0]
    for v,n in ((-C(3,i-1),i),(-C(6,i-1),i-1),(C(8,i-2),i-2)):
        if v:out=add(out,term(n,v,i))
    return out

def get_rows(max_s):
    Bs=[[1,1]]
    Ks=[[]]+[K(i) for i in range(1,13)]
    for s in range(1,max_s+1):
        row=J(s)
        for i in range(1,min(s,12)+1):row=add(row,mul(Ks[i],Bs[s-i]))
        while len(row)>1 and row[-1]==0:row.pop()
        Bs.append(row)
    return Bs

def direct_D(B,q,k):
    return sum((-1)**(k-v)*C(k,v)*2**(q-v)*(B[q+v][q] if q<len(B[q+v]) else 0)
               for v in range(k+1))

def differences(values):
    row=list(values);out=[]
    while row:
        out.append(row[0])
        row=[row[i+1]-row[i] for i in range(len(row)-1)]
    return out

def run(max_r=48):
    Bs=get_rows(3*max_r+2)
    triangle=0; exterior_neg=0
    for s,row in enumerate(Bs):
        for q in range(s+1):
            value=row[q] if q<len(row) else 0
            assert value>0,(s,q,value)
            triangle+=1
        exterior_neg+=sum(v<0 for v in row[s+1:])
    digest=hashlib.sha256()
    samples=[]
    for r in range(3,max_r+1):
        H=[Fraction(direct_D(Bs,r+u,u),5**u) for u in range(r+2)]
        c=differences(H)
        claim=Fraction(2*6**r*(1458*r**3-3681*r*r-1304*r+1425),10125)
        assert c[r-3]==claim,(r,c[r-3],claim)
        assert c[r-2]==Fraction(2*6**r*(243*r*r-245*r-182),675)
        assert c[r-1]==Fraction(6**r*(6*r-1),5)
        assert c[r]==6**r
        assert c[r+1]==0
        assert all(v>0 for v in c[:r+1]),(r,'difference cone')
        digest.update(f'{r},{c[r-3].numerator}/{c[r-3].denominator}\n'.encode('ascii'))
        if r<=7 or r==max_r:samples.append({'r':r,'fourth_newton':str(c[r-3])})
    return {
        'schema':'R335_INDEPENDENT_INTEGER_EVIDENCE_V1',
        'status':'PASS','range_r':[3,max_r],
        'checked_fourth_coefficients':max_r-2,
        'checked_prior_three_each':max_r-2,
        'checked_degree_extra_nodes':max_r-2,
        'inside_triangle_positive':triangle,
        'outside_triangle_negative_retained':exterior_neg,
        'signed_B_s_rows':[0,len(Bs)-1],
        'sha256_fourth_sequence':digest.hexdigest(),
        'samples':samples,
        'model':'original 12-step signed K/J, no truncation or float',
        'inference':'finite exact verification only, universal proof depends on R330 extraction',
        'review':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-r',type=int,default=48)
    parser.add_argument('--out',default='R335_INTEGER_EVIDENCE.json')
    opt=parser.parse_args()
    result=run(opt.max_r)
    with open(opt.out,'w',encoding='utf-8') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print('PASS:',result['range_r'],result['checked_fourth_coefficients'],'values;',result['inside_triangle_positive'],'triangle coefficients')
