#!/usr/bin/env python3
"""R34: no-stepwise-cut initialization for S23/AV, exact Farey last-survivor rank/select.

Research tool: fixed frozen rational enclosure and m=128; stage generation, arc counting,
last-survivor selection, boundary risk checks. No loop over n=129..389 in the compiler.
The optional independent regression intentionally does perform direct geometric checks.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json

D=10**24
TLO=262204504569236716045286
THI=TLO+1
LO=F(TLO,D);HI=F(THI,D);MID=(LO+HI)/2
P=MID.numerator;Q=MID.denominator
M=128;END=389
ORDER=sorted(range(M),key=lambda s:(s*P)%Q)
ARCS=[(s,ORDER[(k+1)%M]) for k,s in enumerate(ORDER)]

def fs(n,mod,a,b):
    assert n>=0 and mod>0 and a>=0 and b>=0
    out=0
    while True:
        if a>=mod: out+=n*(n-1)*(a//mod)//2;a%=mod
        if b>=mod: out+=n*(b//mod);b%=mod
        x=a*n+b
        if x<mod:return out
        n=x//mod;b=x%mod;mod,a=a,mod

def shifted(l,r,s):
    k=r-l
    if k<=0:return 0
    q,b=divmod((l-s)*P,Q)
    return k*q+fs(k,Q,P,b)

def below(s,l,r):
    return shifted(l,r,0)-shifted(l,r,s)-(r-l)*((s*P)//Q)

def count(s,e,l,r):
    if l>=r:return 0
    t=below(e,l,r)-below(s,l,r)
    if (s*P)%Q>(e*P)%Q:t+=r-l
    assert 0<=t<=r-l,(s,e,l,r,t)
    return t

def farey(n):
    # Valid only when the frozen interval avoids all rationals of order < n.
    a,i,c,j=0,1,1,1
    while i+j<=n-1:
        d=P*i-Q*a;f=Q*c-P*j
        assert d>0 and f>0
        if d>f:
            k=min((d-1)//f,(n-1-i)//j)
            assert k>0;a+=k*c;i+=k*j
        else:
            k=min((f-1)//d,(n-1-j)//i)
            assert k>0;c+=k*a;j+=k*i
    assert i*c-a*j==1 and i+j>=n and i<n and j<n
    assert a*D<i*TLO and c*D>j*THI
    return a,i,c,j

def amplitude(a,i,c,j):
    # max(u,v) selected uniformly on theta enclosure; output w-max(u,v)
    # u=i theta-a and v=c-j theta
    u=(-a,i);v=(c,-j);w=(c-a,i-j)
    ulo=u[0]*D+u[1]*TLO;uhi=u[0]*D+u[1]*THI
    vlo=v[0]*D+v[1]*TLO;vhi=v[0]*D+v[1]*THI
    if ulo>vhi:return w[0]-u[0],w[1]-u[1]
    if vlo>uhi:return w[0]-v[0],w[1]-v[1]
    raise AssertionError(('ambiguous winner',i,j))

def risk_oracle(n):
    a,i,c,j=farey(n)
    ranges=[(0,n-i,(-a,i)),(n-i,j,(c-a,i-j)),(j,n,(c,-j))]
    A,B=1,0
    for s,e in ARCS:
        candidates=[coef for l,r,coef in ranges if count(s,e,l,r)>0]
        assert candidates
        low=max(candidates,key=lambda z:z[0]*D+z[1]*TLO)
        high=max(candidates,key=lambda z:z[0]*D+z[1]*THI)
        assert low==high,('enclosure winner',n,s,e)
        A-=low[0];B-=low[1]
    assert 0<=A*D+B*TLO<=D and 0<=A*D+B*THI<=D
    return A,B

def last(s,e,l,r):
    if l>=r or count(s,e,l,r)==0:return None
    lo,hi=l,r-1
    while lo<hi:
        mid=(lo+hi+1)//2
        if count(s,e,mid,r)>0:lo=mid
        else:hi=mid-1
    assert count(s,e,lo,lo+1)==1
    return lo

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]

def compile_prefix():
    pos=M;value=(0,0);events={};regimes=[];oracle_queries=0
    assert risk_oracle(M)==value;oracle_queries+=1
    while pos<=END:
        a,i,c,j=farey(pos)
        nend=min(i+j,END)
        gap=amplitude(a,i,c,j)
        # At regime start, the surviving w-source interval is [pos-i,j).
        # Search each historical fibre for its final w source by rank/select.
        selections=[]
        for s,e in ARCS:
            t=last(s,e,pos-i,j)
            if t is None:continue
            n=i+t+1
            assert pos<n<=i+j
            if n<=nend:
                assert n not in events
                events[n]=gap;selections.append((n,t,s,e))
        # Only 1 independent exact point-query at each new Farey bracket boundary.
        endvalue=add(value,(len(selections)*gap[0],len(selections)*gap[1]))
        assert risk_oracle(nend)==endvalue,(pos,nend,risk_oracle(nend),endvalue)
        oracle_queries+=1
        regimes.append(dict(start=pos,end=nend,lower=f'{a}/{i}',upper=f'{c}/{j}',
                            w_sources=len(selections),amplitude=list(gap),
                            first_event=min((e[0] for e in selections),default=None),
                            last_event=max((e[0] for e in selections),default=None)))
        if nend==END:
            value=endvalue;break
        nextvalue=risk_oracle(nend+1);oracle_queries+=1
        delta=sub(nextvalue,endvalue)
        assert delta[0]*D+delta[1]*TLO>=0 and delta[0]*D+delta[1]*THI>=0
        if delta!=(0,0):
            assert nend+1 not in events
            events[nend+1]=delta
        value=nextvalue;pos=nend+1
    assert len(events)==225,(len(events),regimes)
    assert len(regimes)==3
    # Translate sparse single events to maximal constant-increment runs without a per-cut sweep.
    items=sorted(events.items());segments=[];cursor=M+1
    for n,d in items:
        if cursor<n:
            if segments and segments[-1][1]+1==cursor and segments[-1][2]==(0,0):
                segments[-1]=(segments[-1][0],n-1,(0,0))
            else:segments.append((cursor,n-1,(0,0)))
        if segments and segments[-1][1]+1==n and segments[-1][2]==d:
            segments[-1]=(segments[-1][0],n,d)
        else:segments.append((n,n,d))
        cursor=n+1
    if cursor<=END:segments.append((cursor,END,(0,0)))
    assert segments==[(129,164,(16,-61)),(165,292,(-43,164)),(293,328,(0,0)),(329,389,(-43,164))],segments
    checksum=(0,0)
    for l,r,d in segments:checksum=add(checksum,((r-l+1)*d[0],(r-l+1)*d[1]))
    assert checksum==risk_oracle(END)
    return segments,regimes,checksum,oracle_queries,events

def independent_geometry(n):
    phases=sorted(range(n),key=lambda z:(z*P)%Q)
    starts=[z for z,t in enumerate(phases) if t<M]
    maxgaps=[]
    for k,st in enumerate(starts):
        stop=starts[(k+1)%M]
        if stop<=st:stop+=n
        biggest=F(0)
        for z in range(st,stop):
            x,y=phases[z%n],phases[(z+1)%n]
            gap=F(((y-x)*P)%Q,Q)
            biggest=max(biggest,gap)
        maxgaps.append(biggest)
    assert len(maxgaps)==M
    return 1-sum(maxgaps)

def main():
    segs,regimes,lastvalue,q,events=compile_prefix()
    # Independent direct partition reconstruction, at every early-prefix position,
    # for verification only (not part of source-select generator).
    cur=(0,0)
    for n in range(M+1,END+1):
        if n in events:cur=add(cur,events[n])
        assert cur[0]+cur[1]*MID==independent_geometry(n),n
    assert cur==lastvalue
    p=Path(__file__).resolve().parent
    with (p/'PREFIX_R34.tsv').open('w') as f:
        f.write('n_start\tn_end\tdelta_A\tdelta_B\n')
        for l,r,ab in segs:f.write(f'{l}\t{r}\t{ab[0]}\t{ab[1]}\n')
    (p/'CERTIFICATE_R34.json').write_text(json.dumps({
        'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'theta_interval':{'lo':str(LO),'hi':str(HI)},
        'historical_arcs':M,'endpoint':END,
        'regimes':regimes,'positive_events':len(events),
        'rank_select_oracle_queries':q,'prefix_segments':[
            dict(n_start=l,n_end=r,delta_A=ab[0],delta_B=ab[1]) for l,r,ab in segs],
        'final_risk_affine':list(lastvalue),
        'independent_direct_phase_checks':END-M,
        'generator_loop_over_insertion_n':False
    },ensure_ascii=False,indent=2)+'\n')
    print('CERTIFIED regimes',len(regimes),'risk oracle calls',q,'positive events',len(events))
    for z in regimes:print('REGIME',z)
    print('PREFIX EXACT SEGMENTS',segs)
    print('R_389',lastvalue)
    print('PASS_R34_SOURCE_SELECTED_PREFIX_WITH_261_INDEPENDENT_PHASE_CHECKS')

if __name__=='__main__':main()
