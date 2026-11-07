#!/usr/bin/env python3
"""R330 independent exact integer verification of the first new r=17 BRC diagonal.
Uses the raw 12-term K/J signed-tail recurrence rather than R330 rational-transform code.
"""
from math import comb
from fractions import Fraction
import json,hashlib,argparse

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
def power_one_plus_t(n):return [C(n,k) for k in range(n+1)]
def shift(a,n):return [0]*n+a
def build_K(i):
    d=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)]
    p=[0]
    for j,v in enumerate(d,1):
        if v:p=add(p,scale(power_one_plus_t(i+1-j),-v))
    return shift(p,i-1)
def build_J(s):
    parts=[(-C(3,s-1),s),(-C(6,s-1),s-1),(C(8,s-2),s-2)]
    p=[0]
    for v,e in parts:
        if v:p=add(p,scale(power_one_plus_t(e),v))
    return shift(p,s)
def compute_B(max_s):
    kernels=[None]+[build_K(i) for i in range(1,13)]
    b=[[1,1]]
    for s in range(1,max_s+1):
        poly=build_J(s)
        for i in range(1,min(s,12)+1):poly=add(poly,times(kernels[i],b[s-i]))
        b.append(poly)
    return b
def main(qmax,symbolic):
    table=json.load(open(symbolic))['results']; r=17
    assert len(table)>=r+1 and table[r]['positive']
    b=compute_B(qmax*2)
    triangle=0; negatives=0
    for s,poly in enumerate(b):
        for q in range(s+1):
            assert q<len(poly) and poly[q]>0,(s,q)
            triangle+=1
        negatives+=sum(v<0 for v in poly[s+1:])
    match=0; diff_pos=0; h=hashlib.sha256(); samples=[]
    for q in range(qmax+1):
        vals=[2**(q-u)*b[q+u][q] for u in range(q+1)]
        ds=[]
        while vals:
            ds.append(vals[0]);vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
        assert all(v>0 for v in ds),q
        diff_pos+=len(ds)
        for k,d in enumerate(ds):h.update(f'{q},{k},{d}\n'.encode())
        if q>=r:
            k=q-r
            H=Fraction(0)
            for c in table[r]['shift_coeffs']:
                H=H*k+Fraction(c)
            predicted=(5**k)*H
            assert predicted.denominator==1 and predicted.numerator==ds[k],(q,k,predicted,ds[k])
            match+=1
            if q in (17,18,19,24,32,qmax):samples.append({'q':q,'k':k,'D':str(ds[k]),'H':str(H)})
    return {'schema':'EM_R330_INDEPENDENT_INTEGER_V1','status':'PASS','max_q':qmax,'max_s':2*qmax,'triangle_positive':triangle,'newton_difference_positive':diff_pos,'r17_exact_matches':match,'domain_outside_negative_count':negatives,'newton_sha256':h.hexdigest(),'boundary_and_samples':samples,'arithmetic':'Python arbitrary precision integer and Fraction only','scope':'Finite independent check; r17 unbounded certificate is the symbolic finite polynomial positivity proof.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--q',type=int,default=64);ap.add_argument('--symbolic',required=True);ap.add_argument('--json',required=True);a=ap.parse_args()
    out=main(a.q,a.symbolic)
    with open(a.json,'w') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))
