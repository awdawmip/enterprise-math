#!/usr/bin/env python3
"""R272 exact rational certificate; no dependencies beyond Python stdlib."""
from fractions import Fraction
from hashlib import sha256
import json
p=13
def val(x):
    x=Fraction(x)
    if not x:return None
    a,b=abs(x.numerator),x.denominator;n=0
    while a%p==0:a//=p;n+=1
    while b%p==0:b//=p;n-=1
    return n
def inverse(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return ((A[1][1]/d,-A[0][1]/d),(-A[1][0]/d,A[0][0]/d))
results=[]
for s in range(1,9):
    P=p**s
    q=Fraction(P,100*P+1); eps=Fraction(P,1000*P+1); h=Fraction(1,2)
    A=((q,-eps),(-eps,h)); S=inverse(A)
    assert 0<eps<q and eps<h
    assert val(q*h-eps*eps)==s
    assert val(S[0][0])==-s and val(S[0][1])==0 and val(S[1][1])==0
    assert val(S[1][1]-2)>0
    for m in range(1,7):
        U=p**(m-1); delta=Fraction(U,100*U+1)
        B=((q,-eps),(-eps,h-delta)); T=inverse(B)
        assert 0<delta<Fraction(1,100) and h-delta>eps
        assert val(delta)==m-1
        den=1-delta*S[1][1]
        assert val(den)==0
        assert T[1][1]==S[1][1]/den
        assert T[0][1]==S[0][1]+delta*S[0][1]*S[1][1]/den
        assert val(T[1][1]-S[1][1])==m-1
        results.append({"s":s,"m":m,"input_delta_valuation":val(delta),
          "observer_22_difference_valuation":val(T[1][1]-S[1][1]),
          "global_pole_s":s,"star_22_valuation":val(S[1][1])})
assert len(results)==48
data=json.dumps({"schema":"EM_R272_SPARSE_PORT_CERTIFICATE_V1","p":13,
 "tested_s_range":[1,8],"tested_m_range":[1,6],"checked_pairs":48,
 "all_checks":"PASS","exact":True,"results":results},sort_keys=True,indent=2)+"\n"
open("R272_verification.json","w",encoding="utf-8").write(data)
assert sha256(data.encode()).hexdigest()=="0e3d4911109252ff49dd5378efa12d1f051c362f7e140494b65f9252a942aa60"
print("PASS",len(results),"SHA256",sha256(data.encode()).hexdigest())
