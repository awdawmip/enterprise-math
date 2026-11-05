#!/usr/bin/env python3
"""PREFIX-503 quintic W-prefix index certificate; Python 3 exact integers."""
from collections import defaultdict
from bisect import bisect_right
import json,sys
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
def row(pairs):
    vals=[];starts=[];weights=[];offsets={};s=0
    for a,w in pairs:
        if w:
            vals.append(a);starts.append(s);weights.append(w);offsets[a]=s;s+=w
    return vals,starts,weights,offsets,s
def choose(row,j):
    i=bisect_right(row[1],j)-1
    assert 0<=i<len(row[0]) and j<row[1][i]+row[2][i]
    return row[0][i],j-row[1][i]
def native_support(states):
    raw=defaultdict(set)
    for x in states:raw[x[:7]].add(x[7:])
    K={}
    for (u,v,c,d,e,V,W),cs in raw.items():
        k=u,v,abs(c),abs(d)+abs(e),W,V
        if k in K:assert K[k]==cs
        else:K[k]=cs
    return {k:tuple(sorted(s)) for k,s in K.items()}
class Index:
    def __init__(self,n,K):
        self.n=n;self.K=K;self.A=defaultdict(int);self.H={}
        self.B={};self.D={};self.C={};self.V={};self.calls=0
        qw=defaultdict(int)
        for (u,v,c,s,W,V),cs in K.items():
            self.A[u,v,c,s]+=len(cs);qw[u,v,c,s,W]+=len(cs)
        for u,v,c,s in self.A:
            m=(n-abs(u)-abs(v)-c-s)//2
            assert m>=0
            h=[0];acc=0
            for W in range(m+1):
                acc+=qw.get((u,v,c,s,W),0);h.append(acc)
            assert acc==self.A[u,v,c,s]
            self.H[u,v,c,s]=h
        for u,v,c in sorted(set(t[:3] for t in self.A)):
            L=n-abs(u)-abs(v)-c;p=[];acc=0
            for h in range(L+1):
                acc+=self.A.get((u,v,c,h),0);p.append(acc)
            self.B[u,v,c]=p
            E=lambda h:self.A.get((u,v,c,h),0)+2*(p[L]-p[h])
            r=row((d,E(abs(d))) for d in range(-L,L+1))
            if r[4]:self.D[u,v,c]=r
        groups=defaultdict(set)
        for u,v,c in self.D:groups[u,v].add(c)
        byU=defaultdict(list)
        for u,v in sorted(groups):
            L=n-abs(u)-abs(v)
            r=row((w,self.D.get((u,v,abs(w)),([],[],[],{},0))[4])
                  for w in range(-L,L+1))
            if r[4]:self.C[u,v]=r;byU[u].append((v,r[4]))
        self.V={u:row(pairs) for u,pairs in byU.items()}
        self.U=row((u,r[4]) for u,r in sorted(self.V.items()))
        self.S=self.U[4]
        self.Wwords=sum(len(h) for h in self.H.values())
        self.Qwords=len(self.A)+sum(len(p) for p in self.B.values())+sum(
            len(r[0]) for table in (self.D,self.C,self.V) for r in table.values()
        )+len(self.U[0])
    def ep(self,u,v,c,d,e):
        p=self.B[u,v,c];L=len(p)-1;h=abs(d)
        if e<0:return p[L]-p[h+abs(e)]
        if e==0:return p[L]-p[h]
        return p[L]+self.A.get((u,v,c,h),0)+p[h+e-1]-2*p[h]
    def support(self,u,v,c,s,W,V):
        self.calls+=1
        return self.K.get((u,v,c,s,W,V),())
    def rank(self,x):
        u,v,w,d,e,V,W,q,t=x;c=abs(w);s=abs(d)+abs(e)
        z=self.U[3][u]+self.V[u][3][v]+self.C[u,v][3][w]+self.D[u,v,c][3][d]
        z+=self.ep(u,v,c,d,e)+self.H[u,v,c,s][W]
        for vv in range(V):z+=len(self.support(u,v,c,s,W,vv))
        return z+self.support(u,v,c,s,W,V).index((q,t))
    def inverse(self,j):
        u,j=choose(self.U,j);v,j=choose(self.V[u],j)
        w,j=choose(self.C[u,v],j);c=abs(w)
        d,j=choose(self.D[u,v,c],j)
        R=self.n-abs(u)-abs(v)-c-abs(d)
        lo,hi=-R,R
        while lo<hi:
            mid=(lo+hi)//2
            if self.ep(u,v,c,d,mid+1)>j:hi=mid
            else:lo=mid+1
        e=lo
        assert self.ep(u,v,c,d,e)<=j<self.ep(u,v,c,d,e+1)
        j-=self.ep(u,v,c,d,e);s=abs(d)+abs(e)
        h=self.H[u,v,c,s];W=bisect_right(h,j)-1
        assert 0<=W<len(h)-1 and h[W]<=j<h[W+1]
        j-=h[W]
        m=(self.n-abs(u)-abs(v)-c-s)//2
        for V in range(2*m+1):
            cs=self.support(u,v,c,s,W,V)
            if j<len(cs):break
            j-=len(cs)
        else:raise AssertionError('V missing')
        return (u,v,w,d,e,V,W)+cs[j]
def verify(N=9):
    res={'status':'ALL_CHECKS_PASS','arithmetic':'exact Python integers',
         'frozen_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'observer':'native X6 embedded five signed axes','gates':{}}
    for g in GATES:
        states={(0,0,0,0,0,0,0,0,'N')};out=[]
        for n in range(N+1):
            I=Index(n,native_support(states))
            sorted_states=sorted(states,key=lambda x:(x[:5],x[6],x[5],x[7],x[8]))
            assert len(sorted_states)==I.S
            maxr=maxi=0
            for j,x in enumerate(sorted_states):
                I.calls=0;assert I.rank(x)==j
                maxr=max(maxr,I.calls)
                I.calls=0;assert I.inverse(j)==x
                maxi=max(maxi,I.calls)
            out.append({'n':n,'joint_states':I.S,'quartic_words':I.Qwords,
                        'W_prefix_words':I.Wwords,
                        'quintic_words':I.Qwords+I.Wwords,
                        'checked':len(sorted_states),
                        'max_rank_support_calls':maxr,
                        'max_inverse_support_calls':maxi})
            if n<N:states={advance(x,ch,g) for x in states for ch in LETTERS}
        res['gates'][g]=out
    return res
if __name__=='__main__':
    print(json.dumps(verify(int(sys.argv[1]) if len(sys.argv)>1 else 9),
                     sort_keys=True,separators=(',',':')))
