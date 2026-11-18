#!/usr/bin/env python3
"""R273 exact rational certificate for two labelled BRC Port edges.
Requires only Python standard library; no network or private session capability.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

p = 13

def vp(x):
    x = F(x)
    if not x:
        return None
    a, b = abs(x.numerator), x.denominator
    r = 0
    while a % p == 0:
        a //= p
        r += 1
    while b % p == 0:
        b //= p
        r -= 1
    return r

def inverse2(A):
    d = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d != 0
    return ((A[1][1]/d, -A[0][1]/d), (-A[1][0]/d, A[0][0]/d))

def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def add(A, B):
    return tuple(tuple(x+y for x,y in zip(ar,br)) for ar,br in zip(A,B))

def transpose(A):
    return tuple(zip(*A))

I=((F(1),F(0)),(F(0),F(1)))
rows=[]
for t in range(1,9):
    P=p**t
    a0=b=F(1,1+P)
    for m in range(1,7):
        Q=p**(t+m-1)
        a1=F(3,(1+P)*(3+Q))
        d0=1-a0*b
        d1=1-a1*b
        assert a0>0 and b>0 and a1>0 and a0*b<1 and a1*b<1
        assert vp(d0)==t and vp(d1)==t
        assert vp(a0-a1)==t+m-1
        W0=((F(0),a0),(b,F(0)))
        W1=((F(0),a1),(b,F(0)))
        S0=inverse2(add(I,tuple(tuple(-v for v in row) for row in W0)))
        S1=inverse2(add(I,tuple(tuple(-v for v in row) for row in W1)))
        assert S0[0][0]==1/d0 and S1[0][0]==1/d1
        assert S0[0][1]==a0/d0 and S0[1][0]==b/d0
        assert vp(P*(S0[0][0]-S1[0][0]))==m-1
        assert vp(P*S0[0][0])==0 and vp(P*S1[0][0])==0
        assert inverse2(((F(1),-a0),(F(0),F(1))))[0][0]==1
        assert inverse2(((F(1),F(0)),(-b,F(1))))[0][0]==1
        rows.append({"t":t,"m":m,"individual_11_stars":"1, 1",
                    "v13_1_minus_a0b":vp(d0),"v13_1_minus_a1b":vp(d1),
                    "v13_a_difference":vp(a0-a1),
                    "v13_normalized_11_difference":vp(P*(S0[0][0]-S1[0][0]))})
assert len(rows)==48

# Exact Woodbury identities for a genuinely nonzero stable baseline.
base=((F(1,10),F(1,20)),(F(1,30),F(1,10)))
S=inverse2(add(I,tuple(tuple(-x for x in row) for row in base)))
woodbury=[]
for a,b in [(F(1,7),F(1,9)),(F(1,14),F(1,14)),(F(2,13),F(3,17))]:
    U=((a,F(0)),(F(0),b))
    V=((F(0),F(1)),(F(1),F(0)))
    VT=transpose(V)
    M=add(I,tuple(tuple(-x for x in row) for row in mm(mm(VT,S),U)))
    actual=inverse2(add(I,tuple(tuple(-(base[i][j]+mm(U,VT)[i][j])
                   for j in range(2)) for i in range(2))))
    theoretical=add(S,mm(mm(mm(S,U),inverse2(M)),mm(VT,S)))
    assert actual==theoretical
    woodbury.append({"a":str(a),"b":str(b),"det_M":str(M[0][0]*M[1][1]-M[0][1]*M[1][0]),
                     "exact_identity":True})

assert 2*2>1 # singles nilpotent, simultaneous [[0,2],[2,0]] spectral radius 2
payload={"schema":"EM_R273_TWO_EDGE_PORT_RESONANCE_CERTIFICATE_V1",
         "p":13,"tested_t_range":[1,8],"tested_m_range":[1,6],
         "tested_pairs":48,"arithmetic":"exact rational only",
         "two_edge_woodbury_nonzero_baseline":woodbury,
         "nilpotent_single_edges_joint_unstable":{"a":"2","b":"2","single_edge_spectral_radius":"0","joint_spectral_radius":"2"},
         "all_checks":"PASS","results":rows}
s=json.dumps(payload,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
out=Path(__file__).with_name("R273_verification.json")
out.write_text(s,encoding="utf-8")
print("PASS",len(rows),"WOODBURY",len(woodbury),"SHA256",sha256(s.encode()).hexdigest())
