#!/usr/bin/env python3
"""Independent exact integer check of R334 all-r coefficient (finite cross-check).

Signed 12-step BRC recurrence is built in dict-polynomial arithmetic.
This code does not import the separate symbolic proof program and never
truncates coefficients outside the triangular domain.
"""
from __future__ import annotations
import argparse,hashlib,json
from collections import defaultdict
from fractions import Fraction
from math import comb

def bc(n,k):return comb(n,k) if 0<=k<=n else 0

def term(n,scale,shift):
    return {shift+j:scale*bc(n,j) for j in range(n+1) if scale*bc(n,j)} if n>=0 else {}

def merge(*polys):
    v=defaultdict(int)
    for p in polys:
        for k,x in p.items():v[k]+=x
    return {k:x for k,x in v.items() if x}

def conv(a,b):
    out=defaultdict(int)
    for k,v in a.items():
        for j,w in b.items():out[k+j]+=v*w
    return {k:v for k,v in out.items() if v}

def kernel(i):
    coeff=[-bc(4,i)+bc(2,i-1),bc(5,i-1)-bc(5,i-2),bc(7,i-2),-bc(9,i-3)]
    return merge(*(term(i+1-j,-coeff[j-1],i-1) for j in range(1,5) if coeff[j-1]))

def forcing(i):
    return merge(term(i,-bc(3,i-1),i),term(i-1,-bc(6,i-1),i),term(i-2,bc(8,i-2),i))

def rows(max_s):
    B=[{0:1,1:1}];Ks=[{}]+[kernel(i) for i in range(1,13)]
    for s in range(1,max_s+1):
        B.append(merge(forcing(s),*(conv(Ks[i],B[s-i]) for i in range(1,min(s,12)+1))))
    return B

def D(B,q,u):
    return sum((-1)**(u-v)*bc(u,v)*(2**(q-v))*B[q+v].get(q,0) for v in range(u+1))

def forward(vals):
    a=vals[:];c=[]
    while a:
        c.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    return c

def main(max_r=80):
    B=rows(3*max_r+2)
    for s,row in enumerate(B):
        for q in range(s+1):
            assert row.get(q,0)>0,(s,q,row.get(q,0))
    outside=sum(v<0 for s,row in enumerate(B) for k,v in row.items() if k>s)
    dig=hashlib.sha256();results=[]
    for r in range(2,max_r+1):
        V=[Fraction(D(B,r+u,u),5**u) for u in range(r+2)]
        C=forward(V)
        third=C[r-2]
        expected=Fraction(2*6**r*(243*r*r-245*r-182),675)
        assert third==expected,(r,third,expected)
        assert C[r-1]==Fraction(6**r*(6*r-1),5),(r,'penultimate')
        assert C[r]==6**r,(r,'highest')
        assert C[r+1]==0,(r,'degree bound extra node')
        assert all(v>0 for v in C[:r+1]),(r,'positive cone')
        dig.update(f'{r},{third.numerator}/{third.denominator}\n'.encode())
        if r<=5 or r==max_r:results.append({'r':r,'third':str(third),'expected':str(expected)})
    return {
        'schema':'R334_INDEPENDENT_INTEGER_CHECK_V1',
        'status':'PASS','r_interval':[2,max_r],
        'checked_third_coefficients':max_r-1,
        'checked_top_two_coefficients_each':max_r-1,
        'checked_extra_degree_nodes':max_r-1,
        'B_signed_rows':[0,len(B)-1],
        'inside_triangle_positive':len(B)*(len(B)+1)//2,
        'outside_triangle_negative_retained':outside,
        'sha256_third_r_values':dig.hexdigest(),
        'samples':results,
        'inference':'finite exact cross-check; universal identity proved conditionally using R330 extraction',
        'arithmetic':'integer/Fraction only; dict polynomials; signed tails preserved',
        'role':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-r',type=int,default=80)
    parser.add_argument('--out',default='R334_INTEGER_EVIDENCE.json')
    args=parser.parse_args()
    v=main(args.max_r)
    with open(args.out,'w',encoding='utf8') as f:
        json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(v,ensure_ascii=False,indent=2))
