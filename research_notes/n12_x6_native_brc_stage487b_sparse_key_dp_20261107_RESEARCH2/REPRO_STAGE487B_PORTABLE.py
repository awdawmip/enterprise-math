#!/usr/bin/env python3
"""Standalone executed Stage487-B sparse-fiber key BRC: support, raw mass, rank/unrank."""
from collections import defaultdict
from functools import lru_cache
from itertools import product

def edge_counts(word, alphabet):
    n=len(alphabet); idx={c:i for i,c in enumerate(alphabet)}; out=[0]*(n*n)
    for a,b in zip(word,word[1:]): out[idx[a]*n+idx[b]]+=1
    return tuple(out)

def sub(e,j):
    if e[j]<1:return None
    x=list(e);x[j]-=1;return tuple(x)

class CounterBRC:
    def __init__(self,k,u,h,alphabet,T,W,H):
        assert len(T)==2*k+2 and len(W)==k and len(H)==u
        self.k,self.u,self.h=k,u,h
        self.a=alphabet;self.d=len(alphabet);self.L=max(k+1,h-k-u-1);self.r=min(h,u)
        assert 0<=h<len(T+W+'A'+H+'A')
        self.n=self.L+k+self.r
        self.p=edge_counts(T,alphabet)
        q=edge_counts(T+W+'A'+H+'A',alphabet)
        self.q=tuple(x-y for x,y in zip(q,self.p))
        self.root=(None,self.p,self.q,None,None)
        self.s=alphabet.index(T[0]);self.A=alphabet.index('A')

    @lru_cache(None)
    def euler(self,s,t,e):
        if not any(e):return int(s==t)
        return sum(self.euler(v,t,e2) for v in range(self.d)
                   if (e2:=sub(e,s*self.d+v)) is not None)

    @lru_cache(None)
    def step(self,i,state,c):
        last,p,q,f,g=state;mul=1
        if i<self.L:
            if i==0:f=c
            else:
                p=sub(p,last*self.d+c)
                if p is None:return None
            if i==self.L-1:
                mul=self.euler(self.s,f,p)
                if not mul:return None
                p=();f=None
        elif i<self.L+self.k:
            q=sub(q,last*self.d+c)
            if q is None:return None
            if i==self.L+self.k-1:
                q=sub(q,c*self.d+self.A)
                if q is None:return None
        else:
            if i==self.L+self.k:g=c
            else:
                q=sub(q,last*self.d+c)
                if q is None:return None
            if i==self.n-1:
                q=sub(q,c*self.d+self.A)
                if q is None:return None
        return ((c,p,q,f,g),mul)

    def final_weight(self,state):
        return self.euler(self.A,state[4] if self.r else self.A,state[2])

    def count(self):
        layer={self.root:(1,1)};states=1;transitions=0
        for i in range(self.n):
            nxt=defaultdict(lambda:[0,0])
            for state,(support,mass) in layer.items():
                for c in range(self.d):
                    step=self.step(i,state,c)
                    if step is None:continue
                    trans,mul=step;transitions+=1
                    v=nxt[trans];v[0]+=support;v[1]+=mass*mul
            layer=nxt;states+=len(nxt)
        classes=raw=0
        for state,(support,mass) in layer.items():
            weight=self.final_weight(state)
            if weight:classes+=support;raw+=mass*weight
        return (classes,raw,states,transitions)

    @lru_cache(None)
    def suffix(self,i,state):
        if i==self.n:return int(self.final_weight(state)>0)
        return sum(self.suffix(i+1,x[0]) for c in range(self.d)
                   if (x:=self.step(i,state,c)) is not None)

    def unrank(self,n):
        assert 0<=n<self.suffix(0,self.root)
        state=self.root;word=[]
        for i in range(self.n):
            for c in range(self.d):
                step=self.step(i,state,c)
                if step is None:continue
                m=self.suffix(i+1,step[0])
                if n>=m:n-=m;continue
                state=step[0];word.append(self.a[c]);break
            else:raise AssertionError('unrank exhausted')
        assert n==0
        return ''.join(word)

    def rank(self,key):
        assert len(key)==self.n
        state=self.root;out=0
        for i,ch in enumerate(key):
            c=self.a.index(ch)
            for j in range(c):
                s=self.step(i,state,j)
                if s is not None:out+=self.suffix(i+1,s[0])
            s=self.step(i,state,c)
            assert s is not None
            state=s[0]
        assert self.suffix(self.n,state)>0
        return out

def run(k,u,alphabet,T,W,H,budgets):
    ans=[]
    for h in budgets:
        b=CounterBRC(k,u,h,alphabet,T,W,H)
        q,m,states,trans=b.count()
        assert q==b.suffix(0,b.root)
        for i in {0,q//2,q-1}:
            assert b.rank(b.unrank(i))==i
        ans.append((h,q,m,states,trans))
    return ans

if __name__=='__main__':
    small=run(2,2,'ABG','AABAAA','AB','AB',[0,1,2,8,9,11])
    medium=run(3,2,'ABG','AABAAAAA','ABG','AB',[0,1,8,11])
    large=run(8,6,'AB','AAABAAABAAABAAAAAA','ABAABABA','BAAABA',[0,1,3,6,20,25,26,28,32])
    assert [v[1] for v in small]==[6,12,12,12,16,16]
    assert [v[1] for v in medium]==[20,28,28,35]
    assert [v[1] for v in large]==[2300,4600,9150,15700,15700,22922,32342,58718,114296]
    assert all(v[2]==16 for v in small)
    assert all(v[2]==42 for v in medium)
    assert all(v[2]==114296 for v in large)
    print('PASS', 'small=',small, 'medium=',medium, 'large=',large)
