#!/usr/bin/env python3
"""R5: exact rational Blackwell witness checker (Python stdlib only).
Read CERTIFICATES_ZLIB_B64.txt: base64(zlib(UTF-8 JSON)) lossless.
This checks all 43 rational anchor certificates. See RESEARCH.md
for the all-real same-face convex interpolation proof.
"""
from fractions import Fraction as F
from pathlib import Path
import base64, json, zlib

O=F(1)
Z=F(0)
R=tuple(map(F,("1/10","1/2","3/4","1","5/4","3/2","19/10")))

def M(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,
            (g-a)/2,
            O-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,
            F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def T(x):
    g,a,b,u,v,w,z=x
    return (O+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            O+g+(a+b)/2+u+v+w)

def lawful(x):
    g,a,b,u,v,w,z=x
    return (Z<=a<=g<=O and Z<=b<=g and
            Z<=u<=F(13,40)*a+b/80 and
            Z<=w<=F(3,40)*a+F(21,80)*b and
            Z<=z<=a/10 and Z<=v-z<=F(9,40)*b)

def source(eta,theta,p,q):
    u=(F(13,40)+eta/80)*p
    w=(F(3,40)+F(21,80)*eta)*q
    z=theta/10
    return (O,O,eta,u,F(9,40)*eta+z,w,z)

def verify(x,y,Q,face):
    assert lawful(x) and lawful(y),("lawful",x,y)
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6]),("seedless",y)
    if face=="G":
        assert y[2]==Z and y[4]==y[6]
    else:
        assert face=="F" and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
    assert len(Q)==7 and all(len(row)==7 for row in Q)
    assert all(a>=0 for row in Q for a in row),("negative edge",)
    mx,my=M(x),M(y)
    assert sum(mx)==sum(my)==O
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*my[i] for i in range(7))==O
    for i in range(7):
        assert sum(Q[i])==my[i],("row",i)
    for j in range(7):
        assert sum(Q[i][j] for i in range(7))==mx[j],("Q column",j)
        assert sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j],("P column",j)
    assert T(x)==T(y),("stop times",)
    # Extreme declarations span all possible d in [0,1]^7 by linearity.
    for j in range(7):
        d=[Z]*7
        d[j]=O
        dp=[sum(Q[i][k]*d[k] for k in range(7))/my[i] if my[i] else Z for i in range(7)]
        assert all(Z<=a<=O for a in dp)
        assert sum(my[i]*dp[i] for i in range(7))==mx[j]
        assert sum(R[i]*my[i]*dp[i] for i in range(7))==R[j]*mx[j]

def run():
    encoded=Path(__file__).with_name("CERTIFICATES_ZLIB_B64.txt").read_text().strip()
    raw=json.loads(zlib.decompress(base64.b64decode(encoded)).decode("utf-8"))
    assert tuple(map(F,raw["likelihoods"]))==R
    seen={}
    for c in raw["certificates"]:
        key=(F(c["eta"]),F(c["theta"]),F(c["p"]),F(c["q"]),c["face"])
        assert key not in seen
        x=source(*key[:4])
        y=tuple(map(F,c["y"]))
        Q=[[Z]*7 for _ in range(7)]
        for i,j,v in c["edges"]:
            assert 0<=i<7 and 0<=j<7 and Q[i][j]==Z
            Q[i][j]=F(v)
        verify(x,y,Q,key[-1])
        seen[key]=(x,y,Q)
    assert len(seen)==43
    print("EXACT_ANCHOR_CERTIFICATES_PASS",len(seen))
    # A nontrivial convex test between two different eta anchors on F.
    key1=(F(1,30),Z,Z,O,"F")
    key2=(F(46,705),Z,Z,O,"F")
    A,B=seen[key1],seen[key2]
    weight=F(2,7)
    blend=lambda a,b: (O-weight)*a+weight*b
    x=tuple(blend(A[0][k],B[0][k]) for k in range(7))
    y=tuple(blend(A[1][k],B[1][k]) for k in range(7))
    Q=[[blend(A[2][i][j],B[2][i][j]) for j in range(7)] for i in range(7)]
    verify(x,y,Q,"F")
    assert x==source(blend(key1[0],key2[0]),Z,Z,O)
    print("SAME_FACE_INTERPOLATION_EXACT_PASS")
    print("PASS_R5_ALL_ETA_RATIONAL_ANCHORS_BLACKWELL")
if __name__=="__main__":
    run()
