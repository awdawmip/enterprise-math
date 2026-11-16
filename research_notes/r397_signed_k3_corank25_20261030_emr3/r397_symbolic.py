#!/usr/bin/env python3
"""Exact polynomial-in-theta signed K3 BRC raw D construction at corank 25.
Reproduces K,J from R346_verify.py immutable Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1.
No universal extraction lemma is assumed. Polynomials represented as ascending integer coefficients.
"""
from __future__ import annotations
from pathlib import Path
from math import comb
from fractions import Fraction as F
import json, hashlib
from r397_exact import K,J, C
from sympy import Symbol,Poly,expand

R=25
HERE=Path(__file__).resolve().parent

def clean(it):
    xs=list(it)
    while xs and xs[-1]==0:xs.pop()
    return tuple(xs)

def add(a,b):
    return clean((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))))

def sc(a,q):return clean(v*q for v in a)

def mul(a,b):
    if not a or not b:return ()
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if y:out[i+j]+=x*y
    return clean(out)

def polys():
    S=5*R+4; P=3*R+2
    K0=[None]+[[((int(z),) if z else ()) for z in K(i)[:P+1]] for i in range(1,13)]
    assert K0[3][2]==(-8,)
    K0[3][2]=(-8,-8)
    B=[[() for _ in range(P+1)] for _ in range(S+1)]
    B[0][0]=B[0][1]=(1,)
    for s in range(1,S+1):
        for j,z in enumerate(J(s)[:P+1]):
            if z:B[s][j]=(int(z),)
        for i in range(1,min(s,12)+1):
            for j,k in enumerate(K0[i]):
                if not k:continue
                for p in range(j,P+1):
                    if B[s-i][p-j]: B[s][p]=add(B[s][p],mul(k,B[s-i][p-j]))
    def D(q,k):
        v=()
        for w in range(k+1):v=add(v,sc(B[q+w][q],(-1)**(k-w)*C(k,w)*2**(q-w)))
        return v
    M=[]
    for v in range(2*R+1):
        k=v+1;q=R+k
        val=add(mul(D(q,k),D(q+1,k+1)),sc(mul(D(q,k+1),D(q+1,k)),-1))
        M.append(sc(val,F(5)**(2*R-1-2*k)))
    out=[]
    while M:
        p=clean(M[0]);assert all(z.denominator==1 if isinstance(z,F) else True for z in p)
        out.append(tuple(int(x) for x in p))
        M=[add(M[i+1],sc(M[i],-1)) for i in range(len(M)-1)]
    tur=[]
    for j in range(1,2*R):tur.append(add(mul(out[j],out[j]),sc(mul(out[j-1],out[j+1]),-1)))
    assert len(out)==51 and len(tur)==49
    return out,tur

def eval_poly(p,x):
    v=F(0)
    for z in reversed(p):v=v*x+z
    return v

def verify():
    from r397_exact import eval_at
    polys_c,polys_t=polys()
    for th in map(F, ['0','1/2','9/10','901/1000','902/1000','1','15/8']):
        direct=eval_at(th)
        assert all(eval_poly(p,th)==d for p,d in zip(polys_c,direct['coeff']))
        assert all(eval_poly(p,th)==d for p,d in zip(polys_t,direct['turan']))
    theta=Symbol('theta')
    p=Poly(sum(z*theta**i for i,z in enumerate(polys_c[-1])),theta)
    expected=F(comb(50,25),26)
    assert expand(p.as_expr()-int(expected)*(30-16*theta)**50)==0
    rec={'schema':'EM_R397_CORANK25_SIGNED_K3_POLYNOMIALS_V1','r':R,
         'provenance':'Original signed 12 K/J branches via R346_verify.py, K3[t²]=-8(1+theta)',
         'polynomial_order':'ascending_theta_integer_coefficients',
         'C_ascending':[[str(z) for z in p] for p in polys_c],
         'T_ascending':[[str(z) for z in p] for p in polys_t],
         'top_coefficient_identity':'C50 = 4861946401452*(30-16theta)^50',
         'crosscheck_parameters':['0','1/2','9/10','901/1000','902/1000','1','15/8'],
         'crosscheck_count':(len(polys_c)+len(polys_t))*7}
    rec['polynomial_sha256']=hashlib.sha256(json.dumps({'C':rec['C_ascending'],'T':rec['T_ascending']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    output=HERE/'R397_POLYNOMIALS.json';output.write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
    print('R397_SYMBOLIC_PASS','polyhash',rec['polynomial_sha256'],'C',len(polys_c),'T',len(polys_t),'cross',rec['crosscheck_count'],flush=True)
    return polys_c,polys_t,rec
if __name__=='__main__':verify()
