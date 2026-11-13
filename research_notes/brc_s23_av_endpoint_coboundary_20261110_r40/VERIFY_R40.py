#!/usr/bin/env python3
"""R40 exact endpoint-coboundary batched source selector.

Self-contained; independent reference uses Euclidean floor-sum rank/select.
The R38 helper mathematics and R39 adaptive bracketing are reused in-line,
so this file can be executed from an isolated checkout.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
from collections import defaultdict
from pathlib import Path
import hashlib, json

PIN="43ec6098b1330ae86d0a7863be336c5d97f6ef34"
OUT=Path(__file__).resolve().parent

def floor(x:Q)->int:
    return x.numerator//x.denominator

def sqrt_enclose(n:int,D:int=10**65):
    k=isqrt(n*D*D)
    return Q(k,D),Q(k+1,D)

def theta_pair(p:int,q:int,root:int,scale:int):
    lo,hi=sqrt_enclose(root)
    return Q(p,q)+lo/scale,Q(p,q)+hi/scale

def fs(n:int,mod:int,a:int,b:int)->int:
    """AtCoder-style nonnegative Euclidean floor sum."""
    assert n>=0 and mod>0 and a>=0 and b>=0
    res=0
    while True:
        if a>=mod:
            res+=n*(n-1)*(a//mod)//2
            a%=mod
        if b>=mod:
            res+=n*(b//mod)
            b%=mod
        v=a*n+b
        if v<mod:return res
        n,b,mod,a=v//mod,v%mod,a,mod

def shifted_sum(L:int,J:int,z:int,theta:Q)->int:
    if L>=J:return 0
    div,rem=divmod((L-z)*theta.numerator,theta.denominator)
    return (J-L)*div+fs(J-L,theta.denominator,theta.numerator,rem)

def independent_count(a:int,b:int,w:int,L:int,J:int,theta:Q)->int:
    return shifted_sum(L,J,a,theta)-shifted_sum(L,J,b,theta)+(J-L)*(floor(a*theta)-floor(b*theta)+w)

def independent_last(arcs,L:int,J:int,theta:Q):
    out=[];calls=0
    for a,b,w in arcs:
        c=independent_count(a,b,w,L,J,theta);calls+=1
        if c==0:out.append(None);continue
        lo,hi=L,J
        while lo+1<hi:
            mid=(lo+hi)//2
            c=independent_count(a,b,w,mid,J,theta);calls+=1
            if c>0:lo=mid
            else:hi=mid
        out.append(lo)
    return out,calls

class Observer:
    def __init__(self,lo:Q,hi:Q,m:int):
        self.lo,self.hi,self.m=lo,hi,m
        self.mid=(lo+hi)/2
        assert 0<lo<=hi<1
        self.order=sorted(range(m),key=lambda z: (z*self.mid.numerator)%self.mid.denominator)
        assert self.order[0]==0
        # The floor of all differences of two historical indices must be fixed.
        for d in range(1,m):
            assert floor(d*lo)==floor(d*hi)
        self.arcs=[(a,self.order[(k+1)%m],int(k==m-1)) for k,a in enumerate(self.order)]
        # This is a stronger order check than only floor(d*theta) stability:
        # it certifies every pair's relative orbit order throughout interval.
        for k in range(m-1):
            a,b=self.order[k:k+2]
            assert floor((b-a)*lo)==floor((b-a)*hi)
        self.widths=[(b*lo-floor(b*lo)+w)-(a*lo-floor(a*lo)) for a,b,w in self.arcs]
        assert min(self.widths)>0
    def owner(self,t:int,theta:Q)->int:
        x=t*theta-floor(t*theta)
        for k,(a,b,w) in enumerate(self.arcs):
            u=a*theta-floor(a*theta)
            v=b*theta-floor(b*theta)+w
            if u<=x<v or (w and x<v-1):return k
        raise AssertionError((t,theta))

class CoboundarySelector:
    def __init__(self,obs:Observer,J:int,N:int):
        self.obs,self.J,self.N=obs,J,N
        self.memo={}
        self.P=self.obs.lo.numerator;self.Q=self.obs.lo.denominator
        self.P2=self.obs.hi.numerator;self.Q2=self.obs.hi.denominator
        self.boundary_scalar_calls=0
        self.unique_thresholds=0
        self.query_groups=0
        self.owner_count_queries=0
        self.historic_floors=[self.certified(z) for z in range(obs.m)]
        self.end_floors=[self.certified(J-1-r) for r in range(obs.m-1)]
    def certified(self,s:int)->int:
        u=(s*self.P)//self.Q;v=(s*self.P2)//self.Q2
        self.boundary_scalar_calls+=2
        assert u==v,(s,'enclosure floor changed')
        return u
    def all_counts(self,L:int)->list[int]:
        if L in self.memo:return self.memo[L]
        m=self.obs.m
        # P(z)=sum_{r=0}^{z-1} [floor((J-1-r)theta)-floor((L-1-r)theta)]
        P=[0];d=0
        for r in range(m-1):
            d+=self.end_floors[r]-self.certified(L-1-r)
            P.append(d)
        n=self.J-L
        hist=self.historic_floors
        counts=[P[b]-P[a]+n*(hist[a]-hist[b]+w) for a,b,w in self.obs.arcs]
        assert all(0<=c<=n for c in counts),(L,counts)
        assert sum(counts)==n,(L,sum(counts),n)
        self.memo[L]=counts;self.unique_thresholds+=1
        return counts
    def count_many(self,inds,L):
        assert self.J-self.N<=L<=self.J
        self.query_groups+=1;self.owner_count_queries+=len(inds)
        counts=self.all_counts(L)
        return {i:counts[i] for i in inds}
    def solve(self,inds):
        state={i:None for i in inds};pending=set(inds)
        if self.N<=max(2048,4*self.obs.m):
            cs=self.count_many(sorted(pending),self.J-self.N)
            pending=set()
            for i,c in cs.items():
                if c:state[i]=[self.J-self.N,self.J]
            expansion=0
        else:expansion=0
        old=0;H=1
        while pending:
            H=min(H,self.N);L=self.J-H
            cs=self.count_many(sorted(pending),L)
            for i,c in cs.items():
                if c:state[i]=[L,self.J-old]
            pending={i for i in pending if state[i] is None}
            expansion+=1
            if H==self.N:break
            old=H;H*=2
        brackets={i:v for i,v in state.items() if v is not None}
        rounds=0
        while True:
            groups=defaultdict(list)
            for i,(lo,hi) in brackets.items():
                if lo+1<hi:groups[(lo+hi)//2].append(i)
            if not groups:break
            for mid,ids in sorted(groups.items()):
                cs=self.count_many(ids,mid)
                for i in ids:
                    if cs[i]:brackets[i][0]=mid
                    else:brackets[i][1]=mid
            rounds+=1
        result={i:(brackets[i][0] if i in brackets else None) for i in inds}
        return result,{'expansion_rounds':expansion,'binary_rounds':rounds,'unique_thresholds':self.unique_thresholds,
                       'certified_scalar_floor_evaluations':self.boundary_scalar_calls,
                       'euclidean_floor_sum_calls':0,'owner_count_queries':self.owner_count_queries,
                       'total_request_groups':self.query_groups}


def brute(obs,J,N):
    result=[None]*obs.m
    for t in range(J-N,J):result[obs.owner(t,obs.mid)]=t
    return result

def go(label,p,q,root,scale,m,J,N,narrow_only=False):
    lo,hi=theta_pair(p,q,root,scale)
    obs=Observer(lo,hi,m)
    if narrow_only:
        step_lo=q*lo-p;step_hi=q*hi-p
        inds=[]
        for i,(a,b,w) in enumerate(obs.arcs):
            width_lo=(b*lo-floor(b*lo)+w)-(a*lo-floor(a*lo))
            width_hi=(b*hi-floor(b*hi)+w)-(a*hi-floor(a*hi))
            if width_lo<step_lo or width_hi<step_hi:inds.append(i)
        if not inds:inds=list(range(m))
    else:inds=list(range(m))
    core=CoboundarySelector(obs,J,N)
    selected,stat=core.solve(inds)
    expected,oracle_calls=independent_last([obs.arcs[i] for i in inds],J-N,J,obs.mid)
    assert all(selected[i]==expected[k] for k,i in enumerate(inds)),(label,[(i,selected[i],expected[k]) for k,i in enumerate(inds) if selected[i]!=expected[k]])
    if N<=1200:
        bt=brute(obs,J,N)
        assert all(selected[i]==bt[i] for i in inds)
    for i in inds:
        t=selected[i]
        if t is not None:
            assert obs.owner(t,lo)==i,(label,i,t,'lo')
            assert obs.owner(t,hi)==i,(label,i,t,'hi')
            assert core.all_counts(t+1)[i]==0
            assert core.all_counts(t)[i]>=1
        else:
            assert core.all_counts(J-N)[i]==0
    # Bounded remainder: for arc length lambda and endpoint separation d,
    # |C(L,J) - (J-L)*lambda| < d. A safe computable h>d/lambda
    # therefore forces a hit in every length-h suffix.
    safe_age_bounds={}
    for i in inds:
        a,b,w=obs.arcs[i];d=abs(b-a)
        low_len=min((b*lo-floor(b*lo)+w)-(a*lo-floor(a*lo)),
                    (b*hi-floor(b*hi)+w)-(a*hi-floor(a*hi)))
        assert d>=1 and low_len>0
        age=(d*low_len.denominator)//low_len.numerator+1
        safe_age_bounds[str(i)]=age
        if age<=N:
            assert core.all_counts(J-age)[i]>=1,(label,i,age)
            assert selected[i] is not None and selected[i]>=J-age,(label,i,age)
    # Final statistic includes exact-last-source verification endpoint queries.
    stat.update({'unique_thresholds':core.unique_thresholds,'certified_scalar_floor_evaluations':core.boundary_scalar_calls,
                 'euclidean_floor_sum_calls':0})
    print(label,'m',m,'selected',len(inds),'oracle sums',2*oracle_calls,
          'coboundary sums',0,'thresholds',stat['unique_thresholds'],flush=True)
    return {'case':label,'m':m,'p':p,'q':q,'root':root,'scale':scale,'J':J,'N':N,
            'selected_count':len(inds),'selected_owners':inds,'safe_age_certified_owners':sum(age<=N for age in safe_age_bounds.values()),
            'max_safe_age':max(safe_age_bounds.values()),'last_source':{str(i):selected[i] for i in inds},
            'oracle_count_calls':oracle_calls,'oracle_uncached_shifted_floor_sums':2*oracle_calls,
            **stat}

def main():
    cases=[('MIXED_257',1,3,2,10**3,257,10**9,10**8,True),
           ('NEAR_THIRD_21',1,3,2,10**7,21,10**9,10**8,False),
           ('NEAR_FIFTH_31',1,5,2,10**8,31,10**10,10**9,False),
           ('NEAR_SEVENTH_50',2,7,3,10**8,50,10**11,10**9,False),
           ('SHORT_THIRD',1,3,2,10**7,21,1183,1100,False),
           ('SHORT_FIFTH',1,5,2,10**8,31,837,600,False),
           ('STRESS_21',1,3,2,10**7,21,10**15,10**12,False),
           ('MIXED_16',1,3,2,10**3,16,10**9,10**8,True),
           ('MIXED_32',1,3,2,10**3,32,10**9,10**8,True),
           ('MIXED_128',1,3,2,10**3,128,10**9,10**8,True),
           ('MIXED_5_128',1,5,2,10**3,128,10**9,10**8,True),
           # Separate substantial historic-width change and both sides of circle.
           ('SQRT2_129',-1,1,2,1,129,10**9,10**8,False),
           ('SQRT3_72',-1,1,3,1,72,10**10,10**9,False),
           ('NEGATIVE_SOURCE_WINDOW',-1,1,2,1,16,9,50,False)]
    rows=[go(*case) for case in cases]
    path=OUT/'CERTIFICATE_R40.json'
    blob=json.dumps({'schema':'EM_R40_COBBOUNDARY_EXACT_CERT_V1','scientific_pin':PIN,'cases':rows},
                    sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    path.write_text(blob,encoding='utf-8')
    digest=hashlib.sha256(blob.encode()).hexdigest()
    print('PASS_R40_ENDPOINT_COBBOUNDARY_14_CASES',digest,flush=True)
if __name__=='__main__':main()
