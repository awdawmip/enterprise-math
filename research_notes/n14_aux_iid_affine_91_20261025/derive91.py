#!/usr/bin/env python3
"""Stage91 exact rational Bellman and ordered-prefix audit, auxiliary iid N=14.
Source action prior: derive90.py@stage90; independent Research Driver review NOT claimed.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import json
import derive90 as old

N=old.N;P=old.P;Q=old.Q
A=(6,0,2);B=old.B
alpha0=F(5172392575267656743,14900301753911083008)
V0=F(24307271485812814529,1862537719238885376)
S=F(29733408254700427,41779200000000000)
K=F(4256337294,2241499);LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ

def child(st,i):return old.child(st,i)
def act(st):
    if st==old.A:return 'Q' # stage90 endpoint
    return old.act(st)

def dual(k=K,policy=act):
    lq=k;lp=F(72)+F(8,9)*k
    D={};ties=[];bad=[];pos=total=0;mingap=None
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b);z=policy(st)
                opts={'P':lq*F(2**(a+b),3**a),'Q':lp}
                if n<N:opts['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
                v=opts[z]
                for alt,w in opts.items():
                    if alt==z:continue
                    total+=1;d=w-v
                    if d<0:bad.append((st,z,alt,str(d)))
                    elif d==0:ties.append((st,z,alt))
                    else:
                        pos+=1
                        mingap=d if mingap is None or d<mingap else mingap
                D[st]=v
    return D[(0,0,0)],ties,bad,pos,total,mingap

def firsthit(st):
    cur={(0,0):(F(1),F(1),1)}
    for n in range(st[0]):
        nxt=defaultdict(lambda:(F(),F(),0))
        for (a,b),(p,q,k) in cur.items():
            if act((n,a,b))!='C':continue
            for i in range(3):
                idx=(a+(i==0),b+(i==1));x,y,l=nxt[idx]
                nxt[idx]=(x+p*P[i],y+q*Q[i],l+k)
        cur=dict(nxt)
    return cur.get(st[1:],(F(),F(),0))

@lru_cache(None)
def suffix(st):
    z=act(st)
    if z=='P':return F(),F(1),F(),F()
    if z=='Q':return F(1),F(),F(),F()
    kids=[suffix(child(st,i)) for i in range(3)]
    return (sum((P[i]*kids[i][0] for i in range(3)),F()),
            sum((Q[i]*kids[i][1] for i in range(3)),F()),
            F(1)+sum((P[i]*kids[i][2] for i in range(3)),F()),
            F(1)+sum((Q[i]*kids[i][3] for i in range(3)),F()))

def forward(u,s):
    cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
    for n in range(N+1):
        nxt=defaultdict(lambda:(F(),F()))
        for (a,b),(p,q) in cur.items():
            st=(n,a,b)
            if st==A:
                ep+=p*u;p*=1-u;q*=1-u
            elif st==B:
                ep+=p*s;p*=1-s;q*=1-s
            else:
                z=act(st)
                if z=='P':eq+=q;continue
                if z=='Q':ep+=p;continue
            assert n<N,st
            tp+=p;tq+=q
            for i in range(3):
                idx=(a+(i==0),b+(i==1));x,y=nxt[idx]
                nxt[idx]=(x+p*P[i],y+q*Q[i])
        cur=dict(nxt)
    assert not cur
    return ep,eq,tp,tq

def next_dual(k=K):
    coeff={};cross=[];err=[]
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b);z='Q' if st==A else act(st)
                opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
                if n<N:opts['C']=(F(1)+sum((P[i]*coeff[child(st,i)][0] for i in range(3)),F()),sum((P[i]*coeff[child(st,i)][1] for i in range(3)),F()))
                coeff[st]=opts[z]
                for alt,w in opts.items():
                    if alt==z or st in (A,B):continue
                    c0=w[0]-opts[z][0];c1=w[1]-opts[z][1]
                    if c0+c1*k<0:err.append((st,z,alt,str(c0+c1*k)))
                    if c1>0:
                        kk=-c0/c1
                        if kk<k:cross.append((kk,st,z,alt))
    return max(cross) if cross else None,err

def main():
    pa,qa,ha=firsthit(A);pb,qb,hb=firsthit(B)
    ra,rb=suffix(A),suffix(B)
    X=pa*(1-ra[0]);Y=qa*ra[1]
    E=pb*(1-rb[0]);H=qb*rb[1]
    h=-(X+Y)/(E+H)
    eta=X+E*h
    root,ties,bad,pos,count,gap=dual()
    f0=forward(F(),S);f1=forward(F(1),S+h)
    nxt,errs=next_dual()
    return dict(pa=pa,qa=qa,ha=ha,pb=pb,qb=qb,hb=hb,ra=ra,rb=rb,X=X,Y=Y,E=E,H=H,h=h,eta=eta,s91=S+h,root=root,ties=ties,bad=bad,pos=pos,count=count,gap=gap,f0=f0,f1=f1,nxt=nxt,errs=errs,alpha91=alpha0+eta,V91=V0-G*eta,K=K,LP=LP,G=G)

if __name__=='__main__':
    r=main();print(json.dumps({k:str(v) for k,v in r.items()},indent=2))
