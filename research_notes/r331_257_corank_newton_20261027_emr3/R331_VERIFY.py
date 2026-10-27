#!/usr/bin/env python3
"""Exact BRC signed-tail K/J -> corank Newton certificate; no floating point.
The universal degree<=r input is the rational extraction identity (4) in
R330, commit 7c73f56263c3f0515aa28e55ced2d4c703b8e086.
"""
import argparse, hashlib, json
from fractions import Fraction
from math import comb

def C(n,k): return comb(n,k) if 0<=k<=n else 0
def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:z[i+j]+=v*w
    return z
def monomial(n,coeff,degree):
    return [0]*degree+[coeff*C(n,j) for j in range(n+1)]
def K(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    a=[0]
    for j,v in enumerate(d,1):
        if v:a=add(a,monomial(i+1-j,-v,i-1))
    return a
def J(s):
    a=[0]
    for v,n in ((-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)):
        if v:a=add(a,monomial(n,v,s))
    return a
def build(R):
    b=[[1,1]]; kk=[None]+[K(i) for i in range(1,13)]
    for s in range(1,3*R+1):
        v=J(s)
        for i in range(1,min(s,12)+1):v=add(v,mul(kk[i],b[s-i]))
        b.append(v)
    return b
def check(R):
    b=build(R)
    total=(3*R+1)*(3*R+2)//2
    good=sum(q<len(row) and row[q]>0 for s,row in enumerate(b) for q in range(s+1))
    assert good==total,(good,total)
    outside=sum(x<0 for s,row in enumerate(b) for x in row[s+1:])
    h=hashlib.sha256(); samples={}
    for r in range(R+1):
        vals=[]
        for u in range(r+1):
            q=r+u
            d=sum((-1)**(u-v)*C(u,v)*2**(q-v)*b[q+v][q] for v in range(u+1))
            vals.append(Fraction(d,5**u))
        c=[]
        while vals:
            c.append(vals[0]); vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
        assert all(t>0 for t in c),(r,'nonpositive Newton coefficient')
        assert c[-1]==6**r,(r,'highest coefficient mismatch')
        for k,t in enumerate(c):h.update(f'{r},{k},{t.numerator}/{t.denominator}\n'.encode())
        if r in (17,18,19,32,64,128,R):
            samples[str(r)]={'H(0)':str(c[0]),'DeltaH(0)':str(c[1]) if r else None,'Delta^rH(0)':str(c[-1])}
    return {'status':'PASS','max_r':R,'certified_all_integer_q_ge_r_for_r':f'0..{R}',
            'positive_rational_newton_coefficients':(R+1)*(R+2)//2,
            'signed_tail_polynomials_computed_s':f'0..{3*R}',
            'in_triangle_positive':good,'outside_triangle_negative':outside,
            'highest_newton_coefficient_identity':'Delta^r H_r(0)=6^r',
            'sha256_all_newton_coefficients':h.hexdigest(),'samples':samples,
            'arithmetic':'integer and Fraction only',
            'scope':'Computer-assisted finite sign certificate + inherited exact polynomial degree bound, not native admission'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--max-r',type=int,default=256)
    ap.add_argument('--out',required=True);a=ap.parse_args()
    o=check(a.max_r)
    with open(a.out,'w') as f:json.dump(o,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(o,ensure_ascii=False,indent=2))
