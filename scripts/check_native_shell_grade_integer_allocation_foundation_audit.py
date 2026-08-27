#!/usr/bin/env python3
from __future__ import annotations
import json
from itertools import permutations

AXES=(0,1,2)
FRAMES=tuple(permutations(AXES))
MAX_SHELL=64

def shell(n):
    return [(a,b,c) for a in range(n+1) for b in range(n+1) for c in range(n+1)
            if a+b+c==n and min(a,b,c)==0]

def start(n):
    return 1+3*n*(n-1)//2

def pos(f,x,n):
    i,j,k=f
    for t in range(n):
        y=[0,0,0]; y[i],y[j]=n-t,t
        if tuple(y)==x: return t
    for t in range(n):
        y=[0,0,0]; y[j],y[k]=n-t,t
        if tuple(y)==x: return n+t
    for t in range(n):
        y=[0,0,0]; y[i],y[k]=t,n-t
        if tuple(y)==x: return 2*n+t
    raise AssertionError((f,x,n))

def label(f,x,n):
    return start(n)+pos(f,x,n)

def act(g,x):
    y=[0,0,0]
    for old,new in enumerate(g): y[new]=x[old]
    return tuple(y)

def main():
    states=bij=eq=bal=0
    for n in range(1,MAX_SHELL+1):
        A=shell(n); assert len(A)==3*n; states+=len(A)
        assert start(n+1)==start(n)+3*n
        for f in FRAMES:
            assert sorted(pos(f,x,n) for x in A)==list(range(3*n))
            assert sorted(label(f,x,n) for x in A)==list(range(start(n),start(n)+3*n))
            bij+=1
        for g in FRAMES:
            for f in FRAMES:
                gf=tuple(g[i] for i in f)
                for x in A:
                    gx=act(g,x)
                    assert pos(gf,gx,n)==pos(f,x,n)
                    assert label(gf,gx,n)==label(f,x,n)
                    eq+=1
        x=(n,0,0)
        assert label((0,1,2),x,n)!=label((1,2,0),x,n)
        if n%2==0:
            m=n//2
            O=[(m,m,0),(0,m,m),(m,0,m)]
            want=sorted((6*m*m-2*m+1,6*m*m+1,6*m*m+2*m+1))
            for f in FRAMES:
                assert sorted(label(f,x,n) for x in O)==want
                bal+=1
    out={
      "schema":"ENTERPRISE_MATH_NSIA_TORSOR_REGRESSION_V1",
      "max_shell":MAX_SHELL,"frames":6,"group_elements":6,
      "shell_states_checked":states,"shell_frame_bijection_checks":bij,
      "equivariance_point_checks":eq,"even_balance_packet_frame_checks":bal,
      "verdict":"PASS","proof_status":"REGRESSION_ONLY_GENERAL_PROOF_IN_RETURN"}
    print(json.dumps(out,sort_keys=True))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
