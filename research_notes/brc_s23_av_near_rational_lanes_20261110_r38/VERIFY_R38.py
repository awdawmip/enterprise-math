#!/usr/bin/env python3
"""R38: certified q-lane last-source selection for a near-rational rotation.

Exact Fraction endpoints; independent floor-sum rank/select oracle and tiny
brute-force tests.  The statement is confined to an auxiliary circle observer.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt, gcd
from pathlib import Path
import json, hashlib, time

OUT=Path(__file__).resolve().parent
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def floor(z:F)->int:return z.numerator//z.denominator

def ceil(z:F)->int:return -floor(-z)

def root_interval(n:int,D:int=10**65):
    a=isqrt(n*D*D)
    return F(a,D),F(a+1,D)

def theta_pair(p,q,root,scale):
    a,b=root_interval(root)
    return F(p,q)+a/scale,F(p,q)+b/scale

def floor_sum(n,mod,a,b):
    assert n>=0 and mod>0 and a>=0 and b>=0
    ans=0
    while True:
        if a>=mod: ans+=n*(n-1)*(a//mod)//2;a%=mod
        if b>=mod: ans+=n*(b//mod);b%=mod
        z=a*n+b
        if z<mod:return ans
        n,b,mod,a=z//mod,z%mod,a,mod

def shifted(l,r,s,P,Q):
    if l>=r:return 0
    n=r-l
    div,rem=divmod((l-s)*P,Q)
    return n*div+floor_sum(n,Q,P,rem)

def below(s,l,r,P,Q):
    return shifted(l,r,0,P,Q)-shifted(l,r,s,P,Q)-(r-l)*floor(F(s*P,Q))

def arc_count(s,e,l,r,P,Q):
    if l>=r:return 0
    z=below(e,l,r,P,Q)-below(s,l,r,P,Q)
    if (s*P)%Q>(e*P)%Q:z+=r-l
    assert 0<=z<=r-l,(s,e,l,r,z)
    return z

def oracle_tau(arcs,l,r,P,Q):
    ans=[];calls=0
    for s,e,_ in arcs:
        c=arc_count(s,e,l,r,P,Q);calls+=1
        if not c: ans.append(None);continue
        a,b=l,r
        while a+1<b:
            mid=(a+b)//2
            c=arc_count(s,e,mid,r,P,Q);calls+=1
            if c:a=mid
            else:b=mid
        ans.append(a)
    return ans,calls

class ArcModel:
    def __init__(self,lo,hi,m):
        self.lo,self.hi,self.m=lo,hi,m
        mid=(lo+hi)/2
        self.P,self.Q=mid.numerator,mid.denominator
        self.order=sorted(range(m),key=lambda s: (s*self.P)%self.Q)
        for d in range(1,m):
            assert floor(d*lo)==floor(d*hi),'history ordering not certified'
        self.arcs=[]
        for k,s in enumerate(self.order):
            e=self.order[(k+1)%m]
            wrap=int(k==m-1)
            self.arcs.append((s,e,wrap))
        assert self.order[0]==0

    def unwrap(self,s,e,wrap,theta):
        a=s*theta-floor(s*theta)
        b=e*theta-floor(e*theta)+wrap
        assert 0<b-a<=1
        return a,b

    def min_width_bound(self,p,q):
        sm_lo=q*self.lo-p;sm_hi=q*self.hi-p
        assert 0<sm_lo<=sm_hi<1
        tight=[]
        for k,(s,e,w) in enumerate(self.arcs):
            alo,blo=self.unwrap(s,e,w,self.lo)
            ahi,bhi=self.unwrap(s,e,w,self.hi)
            if blo-alo<sm_lo or bhi-ahi<sm_hi:tight.append(k)
        return len(tight)==0,tight

    def locate(self,t,theta):
        x=t*theta-floor(t*theta)
        for k,(s,e,w) in enumerate(self.arcs):
            a,b=self.unwrap(s,e,w,theta)
            shift=floor(x-a)
            if a+shift<=x<b+shift:return k
        raise AssertionError('source owner missing')

def candidate(mdl,p,q,kmin,kmax,r,theta,arc):
    s0,e0,w=arc
    a,b=mdl.unwrap(s0,e0,w,theta)
    step=q*theta-p
    assert step>0 and b-a>=step
    ymax=r*theta+step*kmax
    h=floor(ymax-a)
    if ymax<b+h: k=kmax;mode='newest'
    else: k=ceil((b+h-r*theta)/step)-1;mode='predecessor'
    assert k<=kmax
    assert a+h<=r*theta+step*k<b+h
    if k<kmin:return None,h,mode
    return r+q*k,h,mode

def floor_sum_interval_stable(mdl,s,l,r):
    """Certify every floor((t-s)*theta) fixed on [lo,hi]."""
    assert l>=s
    L=shifted(l,r,s,mdl.lo.numerator,mdl.lo.denominator)
    U=shifted(l,r,s,mdl.hi.numerator,mdl.hi.denominator)
    assert L==U,('uncertified long-range floors',s,l,r)
    return 2

def single_arc_oracle_certified(mdl,arc,j,N):
    """Narrow-arc fallback at midpoint, with entire enclosure certificate."""
    s,e,w=arc
    idx_list,calls=oracle_tau([arc],j-N,j,mdl.P,mdl.Q)
    t=idx_list[0]
    a=j-N if t is None else t+1
    checked=0
    for boundary in (0,s,e):
        checked+=floor_sum_interval_stable(mdl,boundary,a,j)
    for theta in (mdl.lo,mdl.hi):
        assert arc_count(s,e,a,j,theta.numerator,theta.denominator)==0
        if t is not None: assert mdl.locate(t,theta)==mdl.arcs.index(arc)
    return t,calls,checked

def lane_selector(mdl,p,q,j,N):
    _,tight=mdl.min_width_bound(p,q)
    narrow=set(tight)
    selected=[];checks=0;fallback_calls=0;floor_cert_checks=0
    lane_cases=[]
    for idx,arc in enumerate(mdl.arcs):
        if idx in narrow:
            t,calls,fc=single_arc_oracle_certified(mdl,arc,j,N)
            selected.append(t);fallback_calls+=calls;floor_cert_checks+=fc
            lane_cases.append(None)
            continue
        lane_winners=[]
        for r in range(q):
            kmin=ceil(F(j-N-r,q));kmax=floor(F(j-1-r,q))
            if kmin>kmax:continue
            a,ha,ma=candidate(mdl,p,q,kmin,kmax,r,mdl.lo,arc)
            b,hb,mb=candidate(mdl,p,q,kmin,kmax,r,mdl.hi,arc)
            assert (a,ha,ma)==(b,hb,mb),('unstable lane',idx,r,a,b,ha,hb,ma,mb)
            checks+=2
            if a is not None:
                assert mdl.locate(a,mdl.lo)==idx,(idx,r,a,'lo')
                assert mdl.locate(a,mdl.hi)==idx,(idx,r,a,'hi')
                lane_winners.append(a)
        selected.append(max(lane_winners) if lane_winners else None)
        lane_cases.append(lane_winners)
    return selected,{'status':'CERTIFIED_HYBRID' if narrow else 'CERTIFIED_ALL_LANES',
                     'lane_candidates':q*(mdl.m-len(narrow)),
                     'narrow_arc_count':len(narrow),
                     'fallback_floor_sum_count_calls':fallback_calls,
                     'fallback_floor_stability_endpoint_evaluations':floor_cert_checks,
                     'fraction_endpoint_candidate_checks':checks,
                     'last_by_arc':selected,'per_arc_lane_hits':list(map(lambda x:None if x is None else len(x),lane_cases))}

def brute_tau(mdl,j,N,theta):
    ans=[None]*mdl.m
    for t in range(j-N,j):ans[mdl.locate(t,theta)]=t
    return ans

def do_case(label,p,q,root,scale,m,j,N):
    lo,hi=theta_pair(p,q,root,scale);mdl=ArcModel(lo,hi,m)
    start=time.perf_counter()
    got,cert=lane_selector(mdl,p,q,j,N)
    want,calls=oracle_tau(mdl.arcs,j-N,j,mdl.P,mdl.Q)
    assert got==want,[(i,a,b) for i,(a,b) in enumerate(zip(got,want)) if a!=b]
    if N<=1500:
        middle=F(mdl.P,mdl.Q)
        assert got==brute_tau(mdl,j,N,middle)
    for k,t in enumerate(got):
        if t is not None:
            assert j-N<=t<j and mdl.locate(t,lo)==k and mdl.locate(t,hi)==k
    return {'case':label,'m':m,'j':j,'N':N,'p':p,'q':q,'root':root,'scale':scale,
            'theta_enclosure':[str(lo),str(hi)],'min_gap_at_lo':str(min(mdl.unwrap(*arc,lo)[1]-mdl.unwrap(*arc,lo)[0] for arc in mdl.arcs)),
            's_at_hi':str(q*hi-p),'lane_candidate_budget':cert['lane_candidates'],'narrow_arc_count':cert['narrow_arc_count'],
            'fallback_floor_sum_count_calls':cert['fallback_floor_sum_count_calls'],
            'fallback_floor_stability_endpoint_evaluations':cert['fallback_floor_stability_endpoint_evaluations'],
            'reference_floor_sum_count_calls':calls,
            'candidate_endpoints_verified':cert['fraction_endpoint_candidate_checks'],
            'selected_owner_count':sum(x is not None for x in got),'last_source_by_historical_arc':got,
            'elapsed_seconds_diagnostic':round(time.perf_counter()-start,4)}

def main():
    cases=[('NEAR_THIRD_R37',1,3,2,10**7,21,10**9,10**8),
           ('NEAR_FIFTH',1,5,2,10**8,31,10**10,10**9),
           ('NEAR_SEVENTH',2,7,3,10**8,50,10**11,10**9),
           ('NEAR_THIRD_SMALL',1,3,2,10**7,21,1183,1100),
           ('NEAR_FIFTH_SHORT',1,5,2,10**8,31,837,600),
           ('NEAR_THIRD_WIDE',1,3,2,10**3,257,10**9,10**8)]
    rows=[]
    for C in cases:
        d=do_case(*C);rows.append(d)
        print(d['case'],d['m'],'HYBRID' if d['narrow_arc_count'] else 'FULL_LANES',
              'lanes',d.get('lane_candidate_budget'), 'oracle',d.get('reference_floor_sum_count_calls'))
    assert rows[-1]['narrow_arc_count']>0
    assert sum('last_source_by_historical_arc' in x for x in rows)==6
    stress=do_case('NEAR_THIRD_LARGE_HORIZON',1,3,2,10**7,21,10**15,10**12)
    rows.append(stress);print(stress['case'],'CERTIFIED lanes',stress.get('lane_candidate_budget'),'oracle',stress.get('reference_floor_sum_count_calls'))
    assert len(stress['last_source_by_historical_arc'])==21
    obj={'schema':'EM_R38_NEAR_RATIONAL_LANE_SELECT_CERT_V1',
         'scientific_pin':PIN,
         'scope':'external auxiliary irrational-rotation observer; no native X6 dynamics transfer',
         'certificate_type':'exact interval endpoint checks plus independent rational-midpoint floor-sum selection',
         'cases':rows}
    dest=OUT/'CERTIFICATE_R38.json'
    dest.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('PASS_R38_EXACT_Q_LANE_LAST_SOURCE_AND_INDEPENDENT_FLOOR_SUM_REFERENCE',
          'cases',len(rows),'SHA256',hashlib.sha256(dest.read_bytes()).hexdigest())

if __name__=='__main__':main()
