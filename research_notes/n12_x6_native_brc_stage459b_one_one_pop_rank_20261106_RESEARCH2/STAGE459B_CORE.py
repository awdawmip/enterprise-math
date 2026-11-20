#!/usr/bin/env python3
"""Stage459-B: exact two-source X6 observer quotient / positive BRC counting.

Frozen model: A=+E1, B=-E1, isolated interior B defects, each word starts/ends A.
P and Q can each POP once; P APPEND budget r>=0, Q APPEND arbitrary finite
budget (does not expose additional original P). Native APPEND letters: all 12.
Initial observer: lengths, Z^6 endpoint, directed 12x12 adjacency and overlap K.
This code counts positive source-distinct original histories using exact integers.
No physical heartbeat evolution, phase amplitude, or classical trig is computed.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
import json, sys

A, B = 0, 1


def words(n, k):
    if n < 2: return []
    return [tuple(B if i in places else A for i in range(1, n+1))
            for places in combinations(range(2,n), k)
            if all(y>x+1 for x,y in zip(places, places[1:]))]


def fiber_histories(m,n,kp,kq,d):
    return [(p,q) for p in words(m,kp) for q in words(n,kq)
            if sum(x!=y for x,y in zip(p,q))==d]

class Counter:
    def __init__(self,m,n,kp,kq,d,r):
        assert 2<=m<n and 0<=r and kp>=0 and kq>=0 and d>=0
        self.m,self.n,self.kp,self.kq,self.d,self.r=m,n,kp,kq,d,r
        self.t=min(n,m+r)
        self.positions=tuple(sorted(set(range(m,self.t+1))|{n-1}))
        self.g=max(0,n-2-self.t)
        self._T={ (u,qm):self._prefix(u,qm) for u in (A,B) for qm in (A,B)}

    def _prefix(self,u,qm):
        """Hidden P/Q paired prefix through m-1, with P(m-1)=u and Qm=qm.
        Return (Q-count-j,Q-end-predecessor)->source population. Mismatch m
        against fixed Pm=A is handled here; Pm=A adds no defect.
        """
        m,kp,kq,d=self.m,self.kp,self.kq,self.d
        need=d-int(qm==B)
        if need<0 or (m==2 and u!=A): return {}
        D={(0,0,0,A,A):1}
        for i in range(1,m):
            E=defaultdict(int)
            for (bp,bq,h,lp,lq),mass in D.items():
                for p in (A,B):
                    if (i==1 or i==m-1) and p!=(A if i==1 else u): continue
                    if i>1 and lp==B and p==B: continue
                    for q in (A,B):
                        if i==1 and q!=A: continue
                        if i>1 and lq==B and q==B: continue
                        bp2,bq2,h2=bp+p,bq+q,h+int(p!=q)
                        if bp2<=kp and bq2<=kq and h2<=need:
                            E[bp2,bq2,h2,p,q]+=mass
            D=E
        out=defaultdict(int)
        for (bp,bq,h,lp,lq),mass in D.items():
            if bp==kp and h==need and (lq!=B or qm!=B):out[(bq,lq)]+=mass
        return dict(out)

    @lru_cache(None)
    def _gap(self,g,left,right,bs):
        """Count admissible B-isolated hidden Q-gap with both fixed neighbors."""
        if bs<0 or bs>g:return 0
        D={(0,left):1}
        for _ in range(g):
            E=defaultdict(int)
            for (j,p),mass in D.items():
                for z in (A,B):
                    if p==B and z==B:continue
                    if j+z<=bs:E[(j+z,z)]+=mass
            D=E
        return sum(mass for (j,p),mass in D.items()
                   if j==bs and not(p==B and right==B))

    @lru_cache(None)
    def mass(self,u,qm,qt,qn1,v):
        # Need Q_{n-1}; it can also be inside the visible interval m..t.
        total=0
        for (j,lq),a in self._T[(u,qm)].items():
            bs=self.kq-j-v
            if self.n-1>self.t:
                g=self.n-2-self.t
                z=self._gap(g,qt,qn1,bs)
            else:
                z=int(bs==0)
            total+=a*z
        return total

    @lru_cache(None)
    def _suffix(self,u,idx,qm,qt,qn1,v,last,last_idx):
        """(supported key count,total raw history mass) over visible suffix."""
        if idx==len(self.positions):
            mass=self.mass(u,qm,qt,qn1,v)
            return (int(mass>0),mass)
        i=self.positions[idx]
        classes=raw=0
        for z in ((A,) if i==self.n else (A,B)):
            if last_idx==i-1 and last==B and z==B: continue
            q_m=z if i==self.m else qm
            q_t=z if i==self.t else qt
            q_n1=z if i==self.n-1 else qn1
            c,w=self._suffix(u,idx+1,q_m,q_t,q_n1,v+z,z,i)
            classes+=c;raw+=w
        return classes,raw

    def total(self):
        vals=[self._suffix(u,0,A,A,A,0,A,-100) for u in (A,B)]
        return tuple(sum(v[i] for v in vals) for i in (0,1))

    def key(self,p,q):
        return (p[self.m-2],)+tuple(q[i-1] for i in self.positions)

    def rank(self,key):
        if len(key)!=1+len(self.positions) or any(x not in (A,B) for x in key):
            raise ValueError('key format')
        target_u=key[0];rank=0
        for u in (A,B):
            if u==target_u: break
            rank+=self._suffix(u,0,A,A,A,0,A,-100)[0]
        qm=qt=qn1=A;v=0;last=A;last_i=-100
        for idx,(i,z) in enumerate(zip(self.positions,key[1:])):
            cand=(A,) if i==self.n else (A,B)
            for smaller in cand:
                if smaller>=z: break
                if last_i==i-1 and last==B and smaller==B:continue
                rq=smaller if i==self.m else qm
                rt=smaller if i==self.t else qt
                rn=smaller if i==self.n-1 else qn1
                rank+=self._suffix(target_u,idx+1,rq,rt,rn,v+smaller,smaller,i)[0]
            if z not in cand or (last_i==i-1 and last==B and z==B):raise ValueError('invalid key')
            qm=z if i==self.m else qm
            qt=z if i==self.t else qt
            qn1=z if i==self.n-1 else qn1
            v+=z;last=z;last_i=i
        if self.mass(target_u,qm,qt,qn1,v)==0:raise ValueError('unsupported key')
        return rank

    def unrank(self,rank):
        total=self.total()[0]
        if not 0<=rank<total:raise ValueError('rank out of range')
        for u in (A,B):
            c=self._suffix(u,0,A,A,A,0,A,-100)[0]
            if rank<c:break
            rank-=c
        key=[u];qm=qt=qn1=A;v=0;last=A;last_i=-100
        for idx,i in enumerate(self.positions):
            for z in ((A,) if i==self.n else (A,B)):
                if last_i==i-1 and last==B and z==B:continue
                rq=z if i==self.m else qm
                rt=z if i==self.t else qt
                rn=z if i==self.n-1 else qn1
                c=self._suffix(u,idx+1,rq,rt,rn,v+z,z,i)[0]
                if rank>=c:
                    rank-=c;continue
                key.append(z);qm,qt,qn1,v,last,last_i=rq,rt,rn,v+z,z,i
                break
            else:raise AssertionError('unrank branch missing')
        assert rank==0
        return tuple(key)


