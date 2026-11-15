#!/usr/bin/env python3
"""Exact six-shift phase-decoder proof certificate; Python standard library only."""
from fractions import Fraction as Q
from math import factorial
import json
S=(1,1,2,3,6)
H=(Q(1,6),Q(1,2),-Q(115,36),Q(115,6),-Q(16315,108))
P=tuple(Q(x,36) for x in (455,-295,-25,185,-25,-295))
def count(N=600):
    a=[1]+[0]*(N-1);b=[0]*N
    for j,w in enumerate(S):
        for k in range(w,N):
            a[k]+=a[k-w];b[k]+=b[k-w]+(a[k-w] if j==0 else 0)
    c=[0];t=[0]
    for k in range(N):c.append(c[-1]+a[k]);t.append(t[-1]+b[k])
    return c,t

def add(a,b):return [(a[k] if k<len(a) else 0)+(b[k] if k<len(b) else 0) for k in range(max(len(a),len(b)))]
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def scale(a,z):return [x*z for x in a]
def power(a,n):
    q=[Q(1)]
    for _ in range(n):q=mul(q,a)
    return q
def interp(v):
    d=list(map(Q,v));q=[Q(0)]
    for k in range(len(v)):
        B=[Q(1)]
        for j in range(k):B=mul(B,[-Q(j),Q(1)])
        q=add(q,scale(B,d[0]/factorial(k)))
        d=[d[i+1]-d[i] for i in range(len(d)-1)]
    return q

def residual(r,c,t):return Q(r**3*t[r],c[r])-sum(h*r**(4-i) for i,h in enumerate(H))

def run():
    c,t=count()
    # Independent enumeration of the first 24 cutoff levels.
    def brute(j,b,u):
        if j==len(S):return 1,u
        C=T=0
        for k in range(b//S[j]+1):
            x,y=brute(j+1,b-k*S[j],u+(k if j==0 else 0));C+=x;T+=y
        return C,T
    for r in range(1,25):assert (c[r],t[r])==brute(0,r-1,0)
    pos=[]
    for a in range(6):
        r=next(x for x in range(512,518) if x%6==a)
        cp=interp([c[r+6*n] for n in range(6)]);tp=interp([t[r+6*n] for n in range(7)])
        assert all(sum(x*n**k for k,x in enumerate(cp))==c[r+6*n] for n in range(10))
        assert all(sum(x*n**k for k,x in enumerate(tp))==t[r+6*n] for n in range(10))
        assert len(cp)==6 and len(tp)==7
        R=[Q(r),Q(6)]; hp=[P[a]]
        for j,h in enumerate(H):hp=add(hp,scale(power(R,4-j),h))
        np=add(mul(power(R,3),tp),scale(mul(cp,hp),-1))
        up=add(scale(cp,Q(35,12)),scale(np,-1))
        while np[-1]==0:np.pop()
        while up[-1]==0:up.pop()
        assert len(np)==5 and len(up)==6 and min(cp+np+up)>0
        pos.append({'phase':a,'first_r':r,'min_C':str(min(cp)),'min_N':str(min(np)),'min_U':str(min(up))})
    out=[]
    for h in range(6):
        signatures=[(P[a],P[(a+h)%6]) for a in range(6)]
        fibers={}
        for a,v in enumerate(signatures):fibers.setdefault(v,[]).append(a)
        distinct=list(fibers)
        sep=min(max(abs(x[i]-y[i]) for i in (0,1)) for x in distinct for y in distinct if x!=y)
        assert sep>=Q(35,6)
        wrong=[];ties=[];gaps=[]
        def dist(r):
            Y=(residual(r,c,t),residual(r+h,c,t))
            return {v:max(abs(Y[i]-v[i]) for i in (0,1)) for v in distinct}
        for r in range(1,512):
            d=dist(r);win=min(d,key=d.get)
            if sum(v==d[win] for v in d.values())>1:ties.append(r)
            if win!=signatures[r%6]:wrong.append(r)
        assert wrong and not ties
        tau=wrong[-1]+1
        for r in range(tau,512):
            d=dist(r);true=d[signatures[r%6]]
            gap=min(x-true for v,x in d.items() if v!=signatures[r%6]);assert gap>0
            gaps.append((gap,r))
        r=tau-1;d=dist(r);win=min(d,key=d.get)
        assert win!=signatures[r%6]
        out.append({'shift':h,'classes':list(fibers.values()),'states':len(fibers),'separation':str(sep),
            'threshold':tau,'checked_bridge':[tau,511], 'min_bridge_margin':str(min(gaps)[0]),
            'min_bridge_at_r':min(gaps)[1],'witness':{'r':r,'true_phase':r%6,'winner_class':fibers[win],
            'true_distance':str(d[signatures[r%6]]),'wrong_distance':str(d[win])},'wrong_below_512':len(wrong)})
    assert [(v['states'],v['threshold']) for v in out]==[(4,477),(6,398),(6,384),(4,204),(6,380),(6,393)]
    return {'status':'PASS','model':list(S),'marked_index':0,'strict_prefix':'sum(s_i*k_i)<=r-1',
        'smooth_H':[str(v) for v in H],'periodic_P':[str(v) for v in P],
        'global_bound':'for all r>=512, 0<R(r)-P(r)<35/12 by six positive coefficient certificates',
        'global_certificates':pos,'independent_brute_levels':24,
        'exact_finite_distances':6*511,'results':out,'math_review':'AUTHOR_EXACT_NOT_REVIEWED',
        'prior_pin':'R749SQR@833a27613a2580f1e7b9ec4f6663ddbe9aa22aa2'}
if __name__=='__main__':print(json.dumps(run(),indent=2,ensure_ascii=False))
