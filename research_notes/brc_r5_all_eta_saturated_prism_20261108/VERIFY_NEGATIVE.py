#!/usr/bin/env python3
"""Exact 8-anchor G-face checker and 4D parameter samples (stdlib only).
All-real theorem follows the multi-affine same-face proof in NEGATIVE_RESIDUAL_G_CUBE.md.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json,base64,zlib
from VERIFY import verify, M, R, Z, O
ETA_MAX=F(1,30)
def source(eta,kappa,p,q):
    return (O,O,eta,(F(13,40)+eta/80)*p,
            F(9,40)*eta*kappa,(F(3,40)+F(21,80)*eta)*q,Z)
def diag(x):
    m=M(x)
    return tuple(tuple(m[i] if i==j else Z for j in range(7)) for i in range(7))
def blend(parts):
    assert sum(w for w,t in parts)==O
    x=tuple(sum(w*t[0][k] for w,t in parts) for k in range(7))
    y=tuple(sum(w*t[1][k] for w,t in parts) for k in range(7))
    Q=tuple(tuple(sum(w*t[2][i][j] for w,t in parts) for j in range(7)) for i in range(7))
    return (x,y,Q)
blob=Path(__file__).with_name("NEGATIVE_CUBE_CERTIFICATES_B64.txt").read_text().strip()
raw=json.loads(zlib.decompress(base64.b64decode(blob)).decode("utf-8"))
assert raw["eta"]=="1/30" and raw["theta"]=="0" and raw["face"]=="G"
CERT={}
for c in raw["certificates"]:
    kap,p,q=map(F,(c["kappa"],c["p"],c["q"]))
    key=(kap,p,q)
    assert key not in CERT
    x=source(ETA_MAX,*key)
    y=tuple(map(F,c["y"]))
    A=[[Z]*7 for _ in range(7)]
    for i,j,v in c["edges"]:
        assert 0<=i<7 and 0<=j<7 and A[i][j]==Z
        A[i][j]=F(v)
    t=(x,y,tuple(tuple(row) for row in A))
    verify(*t,"G")
    CERT[key]=t
assert len(CERT)==8
print("EXACT_G_FACE_NEGATIVE_CORNER_CERTIFICATES_PASS",len(CERT))
def lift(eta,kappa,p,q,s=O,g=O,h=Z):
    assert Z<=eta<=ETA_MAX and Z<=kappa<=O and Z<=p<=O and Z<=q<=O
    assert Z<=s<=g<=O and Z<=h<=O
    lam=eta/ETA_MAX
    v=[]
    for a,b,c,d in product((0,1),repeat=4):
        weight=(lam if a else O-lam)*(kappa if b else O-kappa)*(p if c else O-p)*(q if d else O-q)
        if a:
            triple=CERT[(F(b),F(c),F(d))]
        else:
            x0=source(Z,F(b),F(c),F(d))
            triple=(x0,x0,diag(x0))
        v.append((weight,triple))
    t=blend(v)
    verify(*t,"G")
    assert t[0]==source(eta,kappa,p,q)
    E1=(O,Z,Z,Z,Z,Z,Z)
    E0=(Z,)*7
    t=blend(((s,t),(g-s,(E1,E1,diag(E1))),(O-g,(E0,E0,diag(E0)))))
    verify(*t,"G")
    t=blend(((O-h,t),(h,(t[1],t[1],diag(t[1])))))
    verify(*t,"G")
    return t
n=0
for et,kap,p,q in product(map(F,("0","1/150","1/100","1/60","1/30")),
                          map(F,("0","1/5","1/2","4/5","1")),
                          map(F,("0","1/4","1/2","3/4","1")),
                          map(F,("0","1/3","2/3","1"))):
    lift(et,kap,p,q)
    n+=1
print("EXACT_4D_PARAMETER_GRID_PASS",n)
lift(F(1,50),F(3,5),F(2,3),F(1,4),F(1,3),F(3,4),F(2,5))
print("EXACT_SCALING_SOURCE_INTERPOLATION_PASS")
print("PASS_R5_NEGATIVE_RESIDUAL_G_FACE_ALL_REAL_ETA_KAPPA_PQ_CUBE")
