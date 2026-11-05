#!/usr/bin/env python3
"""Stage460-B: positive source-distinct BRC support/mass, rank/unrank.
Two native X6 A/B source histories with isolated interior B, fixed A endpoints;
P and Q may each POP at most twice, no APPEND. Integer semiring N = BRC
positive source population; supports are its nonzero projection. No analytic
propagator, angle, phase or physical residual calculation is performed.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json

A, B = 0, 1


def words(n, k):
    return [tuple(B if j in js else A for j in range(1, n+1))
            for js in combinations(range(2,n), k)
            if all(v > u+1 for u,v in zip(js,js[1:]))]


def observer(p,q):
    # Six signed spatial axes; two of the twelve directions used initially.
    def local(w):
        endpoint = (sum(1 if x==A else -1 for x in w),0,0,0,0,0)
        edges = [0]*144
        for a,b in zip(w,w[1:]):
            # A=+E1 -> direction slot 0; B=-E1 -> slot 6.
            edges[(0 if a==A else 6)*12+(0 if b==A else 6)]+=1
        return len(w),endpoint,tuple(edges)
    return local(p),local(q),sum(a==b for a,b in zip(p,q))


def pop_grid(p,q):
    # All labeled POP-prefix interleavings are represented by this commuting grid.
    return tuple(observer(p[:len(p)-a],q[:len(q)-b])
                 for a in range(0,min(2,len(p))+1)
                 for b in range(0,min(2,len(q))+1))


class Counter:
    def __init__(self,m,n,kp,kq,d):
        assert 2 <= m < n and min(kp,kq,d) >= 0
        self.m,self.n,self.kp,self.kq,self.d=m,n,kp,kq,d
        self.ps=tuple(i for i in (m-2,m-1) if 1<=i<m)
        self.qs=tuple(sorted(set(i for i in (m-1,m,n-2,n-1) if 1<=i<n)))
        self.coords=tuple(('P',i) for i in self.ps)+tuple(('Q',i) for i in self.qs)
        self._mass_calls=0

    def key(self,p,q):
        return tuple((p if s=='P' else q)[i-1] for s,i in self.coords)

    @lru_cache(None)
    def mass(self,key):
        """DP through original paired prefix and Q-only suffix; no raw histories.
        Unit BRC mass per pair; alternative histories add, sequential edges multiply.
        Boundary last letters and mismatch counter retained until safe quotient.
        """
        assert len(key)==len(self.coords)
        self._mass_calls+=1
        fixedp={i:z for (s,i),z in zip(self.coords,key) if s=='P'}
        fixedq={i:z for (s,i),z in zip(self.coords,key) if s=='Q'}
        # State: P defects, Q defects, mismatches, prevP, prevQ, positive mass.
        states={(0,0,0,A,A):1}
        for i in range(1,self.n+1):
            nxt=defaultdict(int)
            pvals=(A,B) if i<self.m else (A,) if i==self.m else (None,)
            qvals=(A,B) if 1<i<self.n else (A,)
            if i==1: pvals=(A,)
            if i in fixedp: pvals=tuple(x for x in pvals if x==fixedp[i])
            if i in fixedq: qvals=tuple(x for x in qvals if x==fixedq[i])
            for (a,b,h,lp,lq),mass in states.items():
                for p in pvals:
                    if p is not None and lp==B and p==B and i>1: continue
                    x=a+int(p==B)
                    if x>self.kp:continue
                    for q in qvals:
                        if lq==B and q==B and i>1:continue
                        y=b+int(q==B)
                        hh=h+int(i<=self.m and p!=q)
                        if y<=self.kq and hh<=self.d:
                            nxt[(x,y,hh,p if p is not None else lp,q)]+=mass
            states=nxt
        return sum(v for (a,b,h,_,_),v in states.items()
                   if a==self.kp and b==self.kq and h==self.d)

    @lru_cache(None)
    def _subtree(self,prefix):
        if len(prefix)==len(self.coords):
            z=self.mass(prefix)
            return (int(z>0),z)
        u=self._subtree(prefix+(A,));v=self._subtree(prefix+(B,))
        return u[0]+v[0],u[1]+v[1]

    def total(self):return self._subtree(())

    def rank(self,key):
        if len(key)!=len(self.coords) or any(x not in (A,B) for x in key):
            raise ValueError('key length/letters')
        r=0;prefix=()
        for x in key:
            if x==B:r+=self._subtree(prefix+(A,))[0]
            prefix=prefix+(x,)
        if self.mass(key)==0:raise ValueError('key unsupported')
        return r

    def unrank(self,r):
        q=self.total()[0]
        if not 0<=r<q:raise ValueError('rank outside support')
        prefix=()
        for _ in self.coords:
            count=self._subtree(prefix+(A,))[0]
            if r<count: prefix=prefix+(A,)
            else: prefix=prefix+(B,);r-=count
        assert r==0 and self.mass(prefix)>0
        return prefix


def validate():
    runs=nonempty=histories=classchecks=rankchecks=pairchecks=0
    pop_to_empty=0; boundaries=set()
    for m in range(2,8):
      for n in range(m+1,min(m+5,10)):
        for kp in range((m-1)//2+1):
          for kq in range((n-1)//2+1):
            wp,wq=words(m,kp),words(n,kq)
            fibers=defaultdict(list)
            for p in wp:
              for q in wq:
                d=sum(a!=b for a,b in zip(p,q))
                fibers[d].append((p,q))
            for d in range(m+1):
                runs+=1
                C=Counter(m,n,kp,kq,d)
                population=fibers[d]
                qF,raw=C.total()
                assert raw==len(population),(m,n,kp,kq,d,raw,len(population))
                if not raw:continue
                nonempty+=1;histories+=raw
                if m==2:pop_to_empty+=1
                boundaries.add(n-m)
                bykey=defaultdict(list)
                for p,q in population:bykey[C.key(p,q)].append((p,q))
                assert qF==len(bykey),(m,n,kp,kq,d,qF,len(bykey))
                keys=sorted(bykey)
                for ix,key in enumerate(keys):
                    classchecks+=1;rankchecks+=1
                    assert C.mass(key)==len(bykey[key])
                    assert C.rank(key)==ix and C.unrank(ix)==key
                # Independent future observation oracle on full (up to 3x3) POP grid.
                sig_to_key={};key_to_sig={}
                for p,q in population:
                    k=C.key(p,q);s=pop_grid(p,q)
                    if k in key_to_sig:assert key_to_sig[k]==s
                    if s in sig_to_key:assert sig_to_key[s]==k
                    sig_to_key[s]=k;key_to_sig[k]=s
                    pairchecks+=1
    large=[]
    for m,n,kp,kq,d in [(64,80,15,17,1),(92,126,20,25,3),(8,9,1,2,1)]:
        C=Counter(m,n,kp,kq,d)
        q,pop=C.total()
        roundtrips=[]
        for r in sorted(set(x for x in (0,q//2,q-1) if 0<=x<q)):
            key=C.unrank(r)
            assert C.rank(key)==r
            roundtrips.append(r)
        large.append(dict(params=[m,n,kp,kq,d],classes=q,population=str(pop),
                          key_length=len(C.coords),mass_leaf_calls=C._mass_calls,
                          rank_roundtrips=roundtrips))
    return dict(marker='STAGE460B_TWO_TWO_POP_ONLY_GROUPED_EXACT_PASS',
                parameter_fibers=runs,nonempty_fibers=nonempty,
                original_histories_compared=histories,positive_classes=classchecks,
                rank_unrank_checks=rankchecks,full_future_signatures_compared=pairchecks,
                pop_to_empty_nonempty_fibers=pop_to_empty,n_minus_m_cases=sorted(boundaries),
                future_grid_max_states=9,large=large,
                full_future_operations='both sources up to 2 POP each, no APPEND',
                carrier='source-distinct positive integer BRC mass, Boolean support by >0',
                scientific_pins={'GLOBAL':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
                                 'EM':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419'})

if __name__=='__main__': print(json.dumps(validate(),ensure_ascii=False,indent=2))
