#!/usr/bin/env python3
"""R271 exact rational certificate; generates R271_verification.json.
Only Python standard library. No floats, remote dependencies, or random data.
"""
from fractions import Fraction
from hashlib import sha256
import json

p=13
def val(x):
    x=Fraction(x)
    if not x: return None
    u,v=abs(x.numerator),x.denominator
    n=0
    while u%p==0: u//=p; n+=1
    while v%p==0: v//=p; n-=1
    return n
def mod(x,N):
    x=Fraction(x); assert x.denominator%p
    return x.numerator*pow(x.denominator,-1,N)%N
def mat(q):
    A=((2*q,-q),(-q,2*q))
    W=((1-2*q,q),(q,1-2*q))
    S=((Fraction(2,3)/q,Fraction(1,3)/q),
       (Fraction(1,3)/q,Fraction(2,3)/q))
    assert A[0][0]*A[1][1]-A[0][1]*A[1][0]==3*q*q
    assert all(sum(A[i][k]*S[k][j] for k in range(2))==(i==j)
               for i in range(2) for j in range(2))
    return A,W,S
results=[]
for s in range(1,9):
    P=p**s
    for m in range(1,7):
        L=1+p**(m-1); M=4*P*L+1
        q0=Fraction(P,M); q1=Fraction(P*L,M)
        A0,W0,S0=mat(q0); A1,W1,S1=mat(q1)
        assert 0<q0<=q1<Fraction(1,4)
        assert all(W[i][j]>=0 for W in (W0,W1) for i in range(2) for j in range(2))
        assert all(sum(W[i])<1 for W in (W0,W1) for i in range(2))
        assert val(A0[0][0])==s and val(A1[0][0])==s
        assert val(3*q0*q0)==2*s and val(3*q1*q1)==2*s
        assert min(val(A1[i][j]-A0[i][j]) for i in range(2) for j in range(2))==s+m-1
        D=P*(S0[0][1]-S1[0][1])
        assert val(D)==m-1
        r0=mod(P*S0[0][1],p**m); r1=mod(P*S1[0][1],p**m)
        assert r0!=r1
        assert all(val(P*P*S[i][j])>=s for S in (S0,S1) for i in range(2) for j in range(2))
        results.append({"smith_exponent_s":s,"precision_digits_m":m,
          "same_input_modulus_exponent":s+m-1,
          "difference_valuation_normalized_inverse":val(D),
          "offdiag_normalized_residue_first":r0,
          "offdiag_normalized_residue_second":r1})
assert len(results)==48
out={"schema":"EM_R271_EXACT_RATIONAL_CHECK_V1",
     "model":"2 positive-rational coupled labelled ports, W=I-q[[2,-1],[-1,2]]",
     "prime":13,"tested_s_range":[1,8],"tested_m_range":[1,6],
     "checked_pairs":48,"exact":True,"all_checks":"PASS",
     "claim":"For each tested pair, inputs agree mod 13^(s+m-1), while 13^s star offdiagonal differs mod 13^m; t=2s; exact universal proof in MD.",
     "results":results}
data=json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
open("R271_verification.json","w",encoding="utf-8").write(data)
print("PASS",len(results),"SHA256",sha256(data.encode()).hexdigest())
assert sha256(data.encode()).hexdigest()=="6d9538341e683ac9be9dc811010676f6fdf0ca7a7eea9a9e9682679882877ddc"
