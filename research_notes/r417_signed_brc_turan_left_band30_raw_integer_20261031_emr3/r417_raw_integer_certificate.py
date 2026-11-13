#!/usr/bin/env python3
"""R417: pure-stdlib exact polynomial positive coefficient certificate for s=30."""
import json
from math import comb
from pathlib import Path

S=30

def add(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def scale(a,n):return [n*x for x in a]
def sub(a,b):return add(a,scale(b,-1))
def product(items):
    v=[1]
    for item in items:v=mul(v,item)
    return v
def ev(a,x):
    y=0
    for v in reversed(a):y=y*x+v
    return y
def cat(n):return comb(2*n,n)//(n+1)
def raw_delta(r,q):
    acc=0
    for a in range(2*q+1):
        for b in (0,1):
            v=r-a-b
            if v>=0 and v%2==0 and v//2<=r-q:
                acc+=(-1)**b*comb(2*q,a)*comb(r-q,v//2)
    return acc

def certificate(eps):
    m0=16 if eps==0 else 15
    dmax=14 if eps==0 else 15
    b0=m0-1+eps; r0=2*m0+eps
    # b=b0+x; T is product of all Cat-ratio denominators.
    den=[ [2*(2*(b0-a)-1),4] for a in range(dmax)]
    numer=[[b0-a+1,1] for a in range(dmax)]
    T=product(den)
    N={}
    for q in (S-1,S,S+1):
        Nq=[0]
        for j in range(q):
            if (eps-q+j)%2: continue
            d=(q-j-2+eps)//2
            part=product(numer[:d]+den[d:])
            Nq=add(Nq,scale(part,comb(q-1,j)*(2**(q-1-j))))
        N[q]=Nq
    lnum=scale(mul([r0+S+1,2],[r0-S,2]),2*S*(2*S-1))
    lden=scale(mul([r0+S,2],[r0-S+1,2]),(2*S+2)*(2*S+1))
    A=sub(mul(lden,mul(N[S],N[S])),mul(lnum,mul(N[S-1],N[S+1])))
    B=mul(lden,mul(T,T))
    assert len(A)==len(B)==2*dmax+3 and min(A)>0 and min(B)>0
    # The signed raw coefficient model is verified directly, independently
    # of any original/previous symbolic generator.
    for x in range(2+2*dmax+1):
        r=r0+2*x;m=m0+x; C=cat(m-1+eps)
        hs=[comb(r+q,2*q)*raw_delta(r,q) for q in (29,30,31)]
        D=hs[1]*hs[1]-hs[0]*hs[2]
        assert ev(B,x)*D==ev(A,x)*(comb(r+S,2*S)*C)**2 and D>0
    return {'epsilon':eps,'r0':r0,'T_degree':dmax,'A_degree':len(A)-1,'B_degree':len(B)-1,
        'A_coefficients_ascending':[str(z) for z in A],
        'B_coefficients_ascending':[str(z) for z in B],
        'A_min':str(min(A)),'B_min':str(min(B)),
        'turan_integer_checks':2+2*dmax+1}

def main():
    rows=[certificate(i) for i in (0,1)]
    p=Path(__file__).parent/'R417_RAW_EVIDENCE.json'
    p.write_text(json.dumps({'schema':'EM_R417_RAW_INTEGER_CERTIFICATE_V1',
        'claim':'D(r,30)>0 for all integers r>=31', 'results':rows},indent=2)+'\n')
    print('R417_RAW_STDLIB_PASS',len(rows),sum(len(r['A_coefficients_ascending']) for r in rows),
          sum(len(r['B_coefficients_ascending']) for r in rows),sum(r['turan_integer_checks'] for r in rows))
    for r in rows:print('PARITY',r['epsilon'],'degrees',r['A_degree'],r['B_degree'],'min',r['A_min'],r['B_min'])
if __name__=='__main__':main()
