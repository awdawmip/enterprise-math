from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json,math
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),(9,5,0),(10,8,2),(12,7,2),(8,5,0),(10,6,1),(7,5,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),(7,0,3),(7,1,4),(7,2,4),(7,2,5),(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3),(10,4,4),(3,0,3),(7,3,4),(9,0,2),(6,1,3),(11,6,5)}
SP.update({(5,5,0),(9,4,0),(10,4,0),(6,5,0),(9,6,1),(11,7,2),(8,6,1),(12,5,1),(10,7,2),(7,6,1),(8,4,0)})
SQ.update({(9,2,3),(5,1,3),(8,0,2),(9,4,4),(11,1,2),(4,1,3),(8,2,3),(7,0,2),(11,3,3)})
SP.add((9,7,2)) # stage82 right endpoint set deterministic P
SQ.add((8,4,4)) # stage83 right endpoint set deterministic Q
SP.add((7,4,0)) # stage84 right endpoint set deterministic P
A=(11,5,1); B=(12,0,1)
alpha0=F(5172036451545515543,14900301753911083008)
V0=F(24500207606836313729,1862537719238885376)
S=F(22822170061354427,41779200000000000)
K=F(180792,79);LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ

def child(st,i):
    n,a,b=st;return(n+1,a+(i==0),b+(i==1))
def act(st):
    if st in SP:return 'P'
    if st in SQ:return 'Q'
    n,a,b=st;t=N-n
    if 8*3**a>=9*2**(a+b+t):return 'P'
    if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
    assert n<N,st
    return 'C'

def dual(K=K, policy=act):
    lq=K;lp=F(72)+F(8,9)*K
    D={};ties=[];bad=[];pos=count=0;small=None
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b);z=policy(st)
                opts={'P':lq*F(2**(a+b),3**a),'Q':lp}
                if n<N:opts['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
                v=opts[z]
                for zz,c in opts.items():
                    if zz==z:continue
                    count+=1;d=c-v
                    if d<0:bad.append((st,z,zz,str(d)))
                    elif d==0:ties.append((st,z,zz))
                    else:
                        pos+=1
                        if small is None or d<small:small=d
                D[st]=v
    return D[(0,0,0)],ties,bad,pos,count,small

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
                eq+=q*u;p*=1-u;q*=1-u
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

def next_dual(K=K):
    vals={};cross=[];errors=[]
    for n in range(N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b);z='P' if st==A else act(st)
                opts={'P':(F(),F(2**(a+b),3**a)), 'Q':(F(72),F(8,9))}
                if n<N:opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
                vals[st]=opts[z]
                for m,v in opts.items():
                    if m==z or st in (A,B):continue
                    c0=v[0]-opts[z][0];c1=v[1]-opts[z][1]
                    if c0+c1*K<0:errors.append((st,z,m,str(c0+c1*K)))
                    if c1>0:
                        nk=-c0/c1
                        if nk<K:cross.append((nk,st,z,m))
    return max(cross),errors

def main():
    pa,qa,ha=firsthit(A);pb,qb,hb=firsthit(B)
    ra,rb=suffix(A),suffix(B)
    X=pa*ra[0];Y=qa*(1-ra[1]);E=pb*(1-rb[0]);H=qb*rb[1]
    h=(X+Y)/(E+H);eta=-X+E*h
    root,ties,bad,pos,count,gap=dual()
    f0=forward(F(),S);f1=forward(F(1),S+h)
    nxt,errs=next_dual()
    return dict(pa=pa,qa=qa,ha=ha,pb=pb,qb=qb,hb=hb,ra=ra,rb=rb,X=X,Y=Y,E=E,H=H,h=h,eta=eta,s85=S+h,root=root,ties=ties,bad=bad,pos=pos,count=count,gap=gap,f0=f0,f1=f1,nxt=nxt,errs=errs,alpha85=alpha0+eta,V85=V0-G*eta,K=K,LP=LP,G=G)
if __name__=='__main__':
    r=main();print(json.dumps({k:str(v) for k,v in r.items()},indent=2))
