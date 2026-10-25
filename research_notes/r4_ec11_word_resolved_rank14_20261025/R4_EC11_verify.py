#!/usr/bin/env python3
"""R4-EC11: exact labelled Hankel rank and split-obstruction certificates.
Python 3 + SymPy. No floating point, randomness or external network.
"""
from collections import deque
from sympy import Matrix, Symbol, simplify, isprime

z = Symbol("z", nonzero=True)
p = 1000003
assert isprime(p)
rules = {
  0: {0:(2,-1,-1), 1:(2,1,-1)},
  1: {0:(0,-1,-1), 1:(0,1,-1)},
  2: {0:(1,1,1), 1:(2,1,-1)},
}

def step(s,a):
    q,r,e,t = s
    qp,eta,b = rules[q][a]
    rp = 2 if r==2 else (0 if a==1 else (1 if r==0 else 2))
    ep = eta*e
    return qp,rp,ep,t+ep*b

def run(w):
    s=(0,0,1,0)
    for a in w:
        s=step(s,int(a))
    return s

# BFS gives one genuinely reachable path for every fine oriented state.
todo=deque([("",(0,0,1,0))])
seen={}
while todo:
    w,s=todo.popleft()
    if s[:3] in seen: continue
    seen[s[:3]]=w
    for a in (0,1):
        todo.append((w+str(a),step(s,a)))
assert len(seen)==14
states=sorted(seen)
I={s:i for i,s in enumerate(states)}
channels=[(q,c,e) for q in range(3) for c in range(2) for e in (-1,1)]
B={}
for a in (0,1):
    M=Matrix.zeros(14,14)
    for j,s in enumerate(states):
        dest=step((*s,0),a)
        M[I[dest[:3]],j]+=z**dest[3]
    B[a]=M
C=Matrix.zeros(12,14)
for j,(q,r,e) in enumerate(states):
    C[channels.index((q,int(r==2),e)),j]=1
suffix_rows=[channels.index((1,0,e)) for e in (-1,1)]
O=C.col_join((C*B[0])[suffix_rows,:])
R=Matrix.zeros(14,14)
for j,s in enumerate(states):
    dest=run(seen[s])
    assert dest[:3]==s
    R[I[s],j]=z**dest[3]
assert simplify(O.det()-1)==0
assert simplify(R.det()-z**3)==0

rows=[("",c) for c in channels]+[("0",(1,0,e)) for e in (-1,1)]
H=Matrix.zeros(14,14)
for j,s in enumerate(states):
    for i,(suffix,chan) in enumerate(rows):
        q,r,e,t=run(seen[s]+suffix)
        if (q,int(r==2),e)==chan:
            H[i,j]=z**t
assert H==O*R
assert simplify(H.det()-z**3)==0

# Evaluation at z=2 in F_p, another independent exact certificate.
def advance(v,a):
    out=[0]*14
    for i,s in enumerate(states):
        dest=step((*s,0),a)
        j=I[dest[:3]]
        out[j]=(out[j]+v[i]*pow(2,dest[3],p))%p
    return out
def det_mod(A):
    A=[list(r) for r in A]
    d=1
    for j in range(14):
        k=next((k for k in range(j,14) if A[k][j]%p),None)
        if k is None:return 0
        if k!=j:
            A[k],A[j]=A[j],A[k]
            d=-d%p
        pivot=A[j][j]%p
        d=d*pivot%p
        inv=pow(pivot,-1,p)
        for i in range(j+1,14):
            fac=A[i][j]*inv%p
            for k in range(j,14):
                A[i][k]=(A[i][k]-fac*A[j][k])%p
    return d

v=[int(s==(0,0,1)) for s in states]
orbit=[]
for _ in range(13):
    orbit.append(v)
    v0,v1=advance(v,0),advance(v,1)
    v=[(a+b)%p for a,b in zip(v0,v1)]
det=det_mod(list(map(list,zip(*orbit,advance(orbit[0],0)))))
assert det==520642,det
print("PASS: 14 fine oriented states reached")
print("PASS: det(O)=1, det(R)=z^3, det(labelled Hankel)=z^3")
print("PASS: det([v,Tv,...,T^12v,T0v]) @z=2 modulo 1000003 =",det)
for s in states:
    print(s,repr(seen[s]),"t=",run(seen[s])[3])
