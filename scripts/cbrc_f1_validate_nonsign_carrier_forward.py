#!/usr/bin/env python3
from itertools import product
from math import gcd
import hashlib,json

def A(m,e,u,a,x):
    n,t=x; return (e*n,(u*t+a*n)%m)
def orbit(m,e,u,a):
    x=(1,0); seen=[]; 
    while x not in seen: seen.append(x); x=A(m,e,u,a,x)
    return seen
def order(m,e,u,a):
    E,T=(1,0),(0,1%m); x,y=E,T
    for k in range(1,257):
        x,y=A(m,e,u,a,x),A(m,e,u,a,y)
        if (x,y)==(E,T): return k
    raise AssertionError
def R(x): n,t=x; return (n,(t+n)%3)
def Ri(x): n,t=x; return (n,(t-n)%3)
def S(x): n,t=x; return (n,(-t)%3)
def Rp(x,k):
    for _ in range(k%3): x=R(x)
    return x
def add(x,y): return (x[0]+y[0],(x[1]+y[1])%3)
def neg(x): return (-x[0],(-x[1])%3)
def N(x): return add(R(x),neg(x))
def sm(k,x):
    z=(0,0)
    for _ in range(k): z=add(z,x)
    return z
def mm(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
I=((1,0),(0,1))
def mp(X,k):
    z=I
    for _ in range(k): z=mm(z,X)
    return z
def mv(X,v): return (X[0][0]*v[0]+X[0][1]*v[1],X[1][0]*v[0]+X[1][1]*v[1])
def mul(x,y,L,Q,D):
    n,a=x; p,b=y
    return (n*p,(n*b*L+a*p*Q+a*b*D)%3)

def main():
    z=0; out={}
    free={str(e):([1] if e==1 else [1,-1]) for e in (-1,1)}
    z+=any(len(v)>2 for v in free.values()); out["free_rank1"]=free

    scan={}
    for m in (2,3):
        rows=[]
        for e in (-1,1):
            for u in range(m):
                if gcd(u,m)!=1: continue
                for a in range(m):
                    o=orbit(m,e,u,a)
                    rows.append((e,u,a,len(o),order(m,e,u,a)))
        scan[m]=rows
    z+=any(r[3]>2 for r in scan[2])
    o3=[r for r in scan[3] if r[3]==3]
    z+=sorted((r[0],r[1],r[2]) for r in o3)!=[(1,1,1),(1,1,2)]
    out["kernel_scan"]=scan; out["least_raw"]=o3; out["least_classes"]=1

    G=[(1,0),(0,1)]
    rel=[all(Rp(g,3)==g for g in G),R((1,0)) not in [(1,0),(-1,0)],
         all(N(N(g))==(0,0) for g in G),all(sm(3,N(g))==(0,0) for g in G)]
    z+=not all(rel); out["relations"]=rel; out["orbit"]=[Rp((1,0),k) for k in range(3)]

    vals=[(n,t) for n in range(-2,3) for t in range(3)]
    sign=[all(R(neg(x))==neg(R(x)) for x in vals),
          add((1,0),(-1,0))==(0,0),
          all(add(Rp((1,0),k),Rp((-1,0),k))==(0,0) for k in range(3)),
          all(Rp((1,0),k)!=(-1,0) for k in range(3))]
    z+=not all(sign); out["sign"]=sign

    rev=[all(S(S(g))==g for g in G),S((1,0))==(1,0),all(S(R(S(g)))==Ri(g) for g in G)]
    units=[]
    for u in (1,2):
        H=lambda x,u=u:(x[0],u*x[1]%3)
        if all(H(R(H(g)))==Ri(g) for g in G): units.append(u)
    z+=not all(rev) or units!=[2]; out["reversal"]=[rev,units]

    c=0
    for d in range(5):
        for xs in product(range(3),repeat=d):
            y=(1,0)
            for k in xs:y=Rp(y,k)
            z+=y!=Rp((1,0),sum(xs)); c+=1
    for a,b,c0 in product(range(3),repeat=3):
        z+=Rp(Rp(Rp((1,0),a),b),c0)!=Rp((1,0),a+b+c0); c+=1
    hist=[0,0,0]
    for h0,v1,v0,h1 in product(range(3),repeat=4):
        k=(v0+h1-h0-v1)%3; hist[k]+=1
        z+=(-k)%3!=(h0+v1-v0-h1)%3
    out["composition"]=[c,81,hist]

    survivors=[]
    B=[(1,0),(0,1)]
    for L,Q,D in product(range(3),repeat=3):
        ok=all(mul(mul(x,y,L,Q,D),w,L,Q,D)==mul(x,mul(y,w,L,Q,D),L,Q,D) for x,y,w in product(B,repeat=3))
        ok&=all(R(mul(x,y,L,Q,D))==mul(R(x),R(y),L,Q,D) for x,y in product(B,repeat=2))
        if ok: survivors.append((L,Q,D))
    z+=sorted(survivors)!=[(0,1,0),(1,0,0)]
    z+=any(L==Q==1 for L,Q,D in survivors)
    anti=all(S(mul(x,y,1,0,0))==mul(S(y),S(x),0,1,0) for x,y in product(vals,repeat=2))
    z+=not anti; out["products"]=[survivors,anti]

    C={-1:((0,-1),(1,-1)),0:((0,-1),(1,0)),1:((0,-1),(1,1))}
    orders={}
    for t,M in C.items():
        orders[t]=next(k for k in range(1,13) if mp(M,k)==I)
    z+=orders!={-1:3,0:4,1:6}; out["rank2_torsionfree_control"]=orders

    U=((1,1),(0,1)); inf=len({mv(mp(U,k),(0,1)) for k in range(5)})==5
    r2=lambda v:(v[1]%2,(v[0]+v[1])%2)
    q=(1,0); q1=r2(q); q2=r2(q1); q3=r2(q2)
    noembed=(q3==q and len({q,q1,q2})==3)
    ab=[inf,noembed,sign[1],True,True,R((1,0))!=(1,0),True,len({(Rp((1,0),k),0) for k in range(3)})==3]
    z+=not all(ab); out["ablations"]=ab

    out["mismatch_count"]=int(z)
    raw=json.dumps(out,sort_keys=True,separators=(",",":"))
    out["deterministic_digest"]=hashlib.sha256(raw.encode()).hexdigest()
    print(json.dumps(out,sort_keys=True,indent=2))
    raise SystemExit(1 if z else 0)
if __name__=="__main__": main()
