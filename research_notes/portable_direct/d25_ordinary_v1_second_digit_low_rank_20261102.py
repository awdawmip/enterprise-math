#!/usr/bin/env python3
"""Original D25 ordinary v1 second digit via source rectangles. Exact p-local units."""
import json
from pathlib import Path
MODELS=(("W216",(2,3),216,6,3),("S2304",(4,),2304,8,4))
def low(p,js,base):
    M=p*p;f=[1]*(max(js)*p);val=[0]*len(f)
    for n in range(1,len(f)):
        z=n;t=0
        while z%p==0:z//=p;t+=1
        f[n]=f[n-1]*z%M;val[n]=val[n-1]+t
    U=[];V=[];d=sum(js)
    for n in range(p):
        v=sum(val[j*n] for j in js)-d*val[n]
        u=pow(base,-n,M)*pow(f[n],-d,M)%M
        for j in js:u=u*f[j*n]%M
        U.append(u);V.append(v)
    H=[0]*p
    for i in range(1,p):H[i]=(H[i-1]+pow(i,-1,p))%p
    return U,V,H,(pow(base,p-1,M)-1)//p
def predict(p,js,base,lam,jstar):
    M=p*p;U,V,H,q=low(p,js,base)
    h=(p-1)//jstar; mid=(p-1)//2;I0=list(range(h+1));I1=list(range(h+1,mid+1))
    A=[a for a in I0 if (jstar*a+1)%p]
    def C(b):return (sum(j*H[j*b%p] for j in js)-sum(js)*H[b]-q)%p
    def rect(A,B,gamma):
        A0=sum(gamma(a)*U[a] for a in A)%M
        A1=sum(a*gamma(a)*U[a] for a in A)%p
        B0=sum((lam*b+1)*U[b] for b in B)%M
        Bplain=sum(U[b] for b in B)%p
        Bharm=sum((lam*b+1)*U[b]*C(b) for b in B)%p
        return (A0*B0+p*A1*(lam*Bplain+Bharm))%M,len(A)*len(B)
    L,lcount=rect(A,I1,lambda a:jstar*a+1)
    R,rcount=rect(I1,I0,lambda a:1)
    return L,R,(L+R)%M,lcount+rcount
def independent(p,js,lam):
    M=p**3;val=0;u=1;answer=0;count=0
    den=36 if len(js)==2 else 288
    h=(p-1)//max(js);H=(p-1)//2
    for k in range(p*p):
        a,b=divmod(k,p)
        selected=(a<=h and h<b<=H and (max(js)*a+1)%p!=0) or (h<a<=H and b<=h)
        if selected:
            assert val==1,(p,js,k,val)
            answer=(answer+(lam*k+1)*u)%M
            count+=1
        if k==p*p-1:break
        d=k+1;z=d;shift=0
        while z%p==0:z//=p;shift+=1
        dv=-3*shift;prod=1
        nums=(2*k+1,3*k+1,3*k+2) if len(js)==2 else (2*k+1,4*k+1,4*k+3)
        for t in nums:
            while t%p==0:t//=p;dv+=1
            prod=prod*t%M
        val+=dv;u=u*prod*pow(z,-3,M)*pow(den,-1,M)%M
        assert val>=0
    return answer%(p*p),count
if __name__=="__main__":
    rows=[];count=0
    for p in (5,7,11,13,19,23,37,43,61,67,109,139,373):
        for name,js,base,lam,jstar in MODELS:
            L,R,T,n=predict(p,js,base,lam,jstar)
            D,nd=independent(p,js,lam)
            assert (T,n)==(D,nd)
            count+=n;rows.append((p,name,L,R,T))
    w,s=[next(r for r in rows if r[0]==373 and r[1]==label) for label in ("W216","S2304")]
    assert w[4]//373==111 and s[4]//373==201
    assert (w[4]//373-2*(s[4]//373))%373==82
    print(json.dumps({"verified_positions":count,"p373_W":w,"p373_S":s,"signed_digit":82}))
