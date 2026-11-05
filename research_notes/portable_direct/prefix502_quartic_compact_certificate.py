"""PREFIX-502 exact quartic-word rank/unrank certificate; Python 3 stdlib.
Self-contained native recurrence; no floating point.
"""
LETTERS='aAbBcCdDeE';GATES=('aab','aba')
CV=(0,1,0,2,1);CW=(0,0,1,0,1)
def advance(x,ch,g):
    y=list(x[:5]);V,W,q,t=x[5:]
    i=LETTERS.index(ch)//2;eps=1 if ch.islower() else -1
    z=int(eps*y[i]<0);y[i]+=eps
    q=max(j for j in range(4) if (g[:q]+ch).endswith(g[:j]))
    if t=='N':
        if ch in 'bB':t='B'
        elif ch in 'cC':t='C'
    return tuple(y)+(V+CV[i]*z,W+CW[i]*z,q,t)
def native_KA(states):
    raw=defaultdict(set)
    for x in states:raw[x[:7]].add(x[7:])
    K={}
    for (u,v,w,d,e,V,W),cs in raw.items():
        k=(u,v,abs(w),abs(d)+abs(e),W,V)
        if k in K:assert K[k]==cs
        else:K[k]=cs
    K={k:tuple(sorted(s)) for k,s in K.items()}
    A=defaultdict(int)
    for (u,v,c,s,W,V),cs in K.items():A[u,v,c,s]+=len(cs)
    return K,A
from bisect import bisect_right
from collections import defaultdict
import json,sys

def row(pairs):
    a=[];p=[];w=[];off={};s=0
    for x,v in pairs:
        if v:
            a.append(x);p.append(s);w.append(v);off[x]=s;s+=v
    return a,p,w,off,s

def choose(r,j):
    i=bisect_right(r[1],j)-1
    assert i>=0 and j<r[1][i]+r[2][i]
    return r[0][i],j-r[1][i]

class Index:
    def __init__(self,n,A,K):
        self.n=n;self.A=A;self.K=K
        self.B={};self.D={};self.C={};self.V={}
        for u,v,c in sorted(set(z[:3] for z in A)):
            L=n-abs(u)-abs(v)-c;P=[];s=0
            for h in range(L+1):
                s+=A.get((u,v,c,h),0);P.append(s)
            self.B[u,v,c]=P
            E=lambda h:A.get((u,v,c,h),0)+2*(P[L]-P[h])
            drow=row((d,E(abs(d))) for d in range(-L,L+1))
            if drow[4]:self.D[u,v,c]=drow
        groups=defaultdict(set)
        for u,v,c in self.D:groups[u,v].add(c)
        vgroups=defaultdict(list)
        for u,v in sorted(groups):
            lim=n-abs(u)-abs(v)
            crow=row((w,self.D.get((u,v,abs(w)),([],[],[],{},0))[4]) for w in range(-lim,lim+1))
            if crow[4]:self.C[u,v]=crow;vgroups[u].append((v,crow[4]))
        self.V={u:row(pairs) for u,pairs in vgroups.items()}
        self.U=row((u,r[4]) for u,r in sorted(self.V.items()))
        self.S=self.U[4]
    def ep(self,u,v,c,d,e):
        P=self.B[u,v,c];L=len(P)-1;h=abs(d)
        if e<0:return P[L]-P[h+abs(e)]
        if e==0:return P[L]-P[h]
        return P[L]+self.A.get((u,v,c,h),0)+P[h+e-1]-2*P[h]
    def support(self,u,v,c,s,W,V):return self.K.get((u,v,c,s,W,V),())
    def rank(self,x):
        u,v,w,d,e,V,W,q,t=x;c=abs(w);s=abs(d)+abs(e)
        z=self.U[3][u]+self.V[u][3][v]+self.C[u,v][3][w]+self.D[u,v,c][3][d]+self.ep(u,v,c,d,e)
        m=(self.n-abs(u)-abs(v)-c-s)//2
        for ww in range(W):
            for vv in range(2*m+1):z+=len(self.support(u,v,c,s,ww,vv))
        for vv in range(V):z+=len(self.support(u,v,c,s,W,vv))
        return z+self.support(u,v,c,s,W,V).index((q,t))
    def inverse(self,j):
        u,j=choose(self.U,j);v,j=choose(self.V[u],j);w,j=choose(self.C[u,v],j)
        c=abs(w);d,j=choose(self.D[u,v,c],j)
        R=self.n-abs(u)-abs(v)-c-abs(d)
        lo,hi=-R,R
        while lo<hi:
            mid=(lo+hi)//2
            if self.ep(u,v,c,d,mid+1)>j:hi=mid
            else:lo=mid+1
        e=lo;assert self.ep(u,v,c,d,e)<=j<self.ep(u,v,c,d,e+1)
        j-=self.ep(u,v,c,d,e);s=abs(d)+abs(e)
        m=(self.n-abs(u)-abs(v)-c-s)//2
        for W in range(m+1):
            k=sum(len(self.support(u,v,c,s,W,V)) for V in range(2*m+1))
            if j<k:break
            j-=k
        else:raise AssertionError('W not found')
        for V in range(2*m+1):
            cs=self.support(u,v,c,s,W,V)
            if j<len(cs):break
            j-=len(cs)
        else:raise AssertionError('V not found')
        return (u,v,w,d,e,V,W)+cs[j]
    def words(self):
        return len(self.A)+sum(len(x) for x in self.B.values())+sum(len(r[0]) for table in (self.D,self.C,self.V) for r in table.values())+len(self.U[0])

def verify(N):
    result={'status':'ALL_CHECKS_PASS','arithmetic':'exact integers','n_max':N,'results':{}}
    for g in GATES:
        states={(0,0,0,0,0,0,0,0,'N')};seq=[]
        for n in range(N+1):
            K,A=native_KA(states) # independent ten-direction native state recurrence.
            I=Index(n,A,K)
            ordered=sorted(states,key=lambda x:(x[:5],x[6],x[5],x[7],x[8]))
            assert len(ordered)==I.S
            for j,s in enumerate(ordered):
                assert I.rank(s)==j,(g,n,j,s)
                assert I.inverse(j)==s,(g,n,j,s)
            seq.append({'n':n,'joint_states':I.S,'index_words':I.words(),'quartic_group_count':len(A),'checked':len(ordered)})
            if n<N:states={advance(x,a,g) for x in states for a in LETTERS}
        result['results'][g]=seq
    return result
if __name__=='__main__':
    print(json.dumps(verify(int(sys.argv[1]) if len(sys.argv)>1 else 9),sort_keys=True,separators=(',',':')))
