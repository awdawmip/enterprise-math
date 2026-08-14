#!/usr/bin/env python3
"""R056 minimal exact Stage-C search.
Only:
  * globally exhaustive one-cell relocation for r=2..6;
  * exact bounded energy enumeration for k=2,3 with support diameter<=3.
It never opens or searches the frozen holdout.
"""
from itertools import combinations
from collections import deque
import argparse, json

DIRS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def Q(x): a,b=x; return a*a+a*b+b*b
def dL(x,y=(0,0)):
    a=x[0]-y[0]; b=x[1]-y[1]
    return max(abs(a),abs(b),abs(a+b))
def sumv(xs):
    a=b=0
    for x,y in xs: a+=x; b+=y
    return (a,b)
def H(r):
    return {(a,b) for a in range(-r,r+1) for b in range(-r,r+1) if dL((a,b))<=r}
def G(C):
    S=sumv(C); return len(C)*sum(Q(x) for x in C)-Q(S)
def connected(C):
    s=next(iter(C)); seen={s}; q=deque([s])
    while q:
        x=q.popleft()
        for d in DIRS:
            y=add(x,d)
            if y in C and y not in seen: seen.add(y); q.append(y)
    return len(seen)==len(C)
def hole_free(C):
    aa=[x[0] for x in C]; bb=[x[1] for x in C]
    amin,amax=min(aa)-1,max(aa)+1; bmin,bmax=min(bb)-1,max(bb)+1
    E={(a,b) for a in range(amin,amax+1) for b in range(bmin,bmax+1) if (a,b) not in C}
    seeds={x for x in E if x[0] in (amin,amax) or x[1] in (bmin,bmax)}
    seen=set(seeds); q=deque(seeds)
    while q:
        x=q.popleft()
        for d in DIRS:
            y=add(x,d)
            if y in E and y not in seen: seen.add(y); q.append(y)
    return seen==E
def frontier(C): return {add(x,d) for x in C for d in DIRS if add(x,d) not in C}

def m1(r):
    C=H(r); base=G(C); ans=[]
    for u in sorted(C):
        C0=C-{u}
        for v in sorted(frontier(C0)):
            if v in C: continue
            Cp=C0|{v}
            if len(Cp)!=len(C) or not connected(Cp) or not hole_free(Cp): continue
            dg=G(Cp)-base
            if dg<0:
                ans.append((dL(u,v),u,v,dg))
    if not ans: return {"r":r,"rho_1":"infinity","descent_count":0}
    rho=min(x[0] for x in ans)
    return {"r":r,"rho_1":rho,"descent_count":len(ans),"minimizer_count":sum(x[0]==rho for x in ans)}

def bounded(r,k,rho=3):
    C=H(r); pts=sorted(C); N=len(C)
    OFF=[(a,b) for a in range(-rho,rho+1) for b in range(-rho,rho+1) if dL((a,b))<=rho]
    total=neg=0; mindg=None
    for U in combinations(pts,k):
        if any(dL(U[i],U[j])>rho for i in range(k) for j in range(i)): continue
        W=[]
        for off in OFF:
            v=add(U[0],off)
            if v in C: continue
            if all(dL(v,u)<=rho for u in U[1:]): W.append(v)
        qU=sum(Q(u) for u in U); sU=sumv(U)
        for V in combinations(W,k):
            if any(dL(V[i],V[j])>rho for i in range(k) for j in range(i)): continue
            total+=1
            ds=sub(sumv(V),sU)
            dg=N*(sum(Q(v) for v in V)-qU)-Q(ds)
            mindg=dg if mindg is None else min(mindg,dg)
            neg += dg<0
    return {"r":r,"k":k,"rho_cap":rho,"candidates":total,"negative":neg,"min_DeltaG":mindg}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--r",type=int,choices=range(2,7))
    a=ap.parse_args()
    print(json.dumps({"m1":m1(a.r),"k2":bounded(a.r,2),"k3":bounded(a.r,3)},sort_keys=True))
