#!/usr/bin/env python3
"""PREFIX-544 exact composition certificate; uses PREFIX543 native transition source.
Run alongside PREFIX543_boundary_moment_certificate.py. Scientific pin f42f2906...
"""
from collections import defaultdict
import json
from PREFIX543_boundary_moment_certificate import P,NX,T,sig,tau,ep,raw

def gate(b,j,c):return int(b==c==1 and j==T)
def add(F,r):
    W=defaultdict(int)
    for (i,b,p,h),v in F.items():
        for j in NX[i]:
            for c in (0,1):W[j,c,p+tau(r,i,j),h+gate(b,j,c)]+=v
    return dict(W)
def flatten(F):
    A=defaultdict(int)
    for (_,_,p,h),v in F.items():A[p,h]+=v
    return dict(A)
def suffixes(r,D):
    B=[[[{(0,0):1} for _ in (0,1)] for _ in P]]
    for _ in range(D):
        W=[]
        for i in range(48):
            row=[]
            for b in (0,1):
                h=defaultdict(int)
                for j in NX[i]:
                    for c in (0,1):
                        for (p,k),v in B[-1][j][c].items():
                            h[p+tau(r,i,j),k+gate(b,j,c)]+=v
                row.append(dict(h))
            W.append(row)
        B.append(W)
    return B
def glue(F,B):
    H=defaultdict(int)
    for (i,b,p,h),v in F.items():
        for (x,y),w in B[i][b].items():H[p+x,h+y]+=v*w
    return dict(H)
def delta(r,a,u,v):
    z=abs(sig(u)-r)-abs(sig(v)-r)+abs(sig(v)-a)-abs(sig(u)-a)
    assert z%2==0
    return z//2

def run(D=10):
    assert len(P)==48 and sum(map(len,NX))==144 and T not in NX[T]
    Bs={r:suffixes(r,D) for r in (-1,0,1)}
    split=raw_checks=rebases=0
    for s in range(48):
        r=sig(s)
        for b0 in (0,1):
            F=[{(s,b0,0,0):1}]
            for d in range(D):F.append(add(F[-1],r))
            independently=raw(s,min(D,6),b0)
            for d,H in enumerate(independently):
                assert flatten(F[d])==H
                raw_checks+=1
            for m in range(D+1):
                for n in range(D-m+1):
                    assert glue(F[m],Bs[r][n])==flatten(F[m+n])
                    split+=1
    for u in range(48):
        a=sig(u)
        for r in (-1,0,1):
            words=[(u,0,0)]
            for n in range(6):
                for v,x,y in words:
                    assert x-y==delta(r,a,u,v)
                    rebases+=1
                if n<5:words=[(j,x+tau(r,v,j),y+tau(a,v,j)) for v,x,y in words for j in NX[v]]
    ix={p:i for i,p in enumerate(P)}
    s=ix[(0,3,-6)]; i=ix[(0,-6,1)]
    assert i in NX[s] and T in NX[i] and tau(sig(s),s,i)==0
    assert tau(sig(s),i,T)==1 and gate(0,T,1)==0 and gate(1,T,1)==1
    s=ix[(0,6,-3)]; i=ix[(0,-3,1)]; j=ix[(2,-3,2)]
    assert i in NX[s] and j in NX[s] and tau(sig(s),s,i)==tau(sig(s),s,j)==0
    assert P[NX[i][0]]==(0,1,-6) and P[NX[j][0]]==(2,2,-5)
    assert tau(sig(s),i,NX[i][0])==1 and tau(sig(s),j,NX[j][0])==0
    assert tau(sig(i),i,NX[i][0])==0 and delta(sig(s),sig(i),i,NX[i][0])==1
    return dict(status='ALL_CHECKS_PASS',max_total_depth=D,phases=48,port_states=96,
        root_sign_parameters=3,split_equalities=split,independent_native_endpoint_crosschecks=raw_checks,
        root_rebase_equalities=rebases,witnesses=['last bit changes gate on same target suffix',
        'terminal phase changes first-axis BRC under successor-slot-0',
        'local suffix BRC 0 rebases to global BRC 1'])
if __name__=='__main__':
    import sys
    print(json.dumps(run(int(sys.argv[1]) if len(sys.argv)>1 else 10),indent=2))
