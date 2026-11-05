#!/usr/bin/env python3
"""PREFIX-508: exact constant-template mod-six source-row compiler.
Only integer BRC occupancy and ordered native colors are used. No floats, pi,
trig, generic PDE/rotation solver or external libraries.
"""
from __future__ import annotations
from itertools import product
from collections import defaultdict
import json, random, time

COLORS = tuple(range(5))
GATES = {"aab":(0,0,1), "aba":(0,1,0)}
SRC = {1:"B",2:"B",3:"C"}
SUFFIXES = {z: list(product(COLORS, repeat=z)) for z in range(4)}

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

def terminal(s,gate):
    # n>=3: terminal gate prefix depends only on the last three colors
    for k in range(min(len(s),len(gate)),0,-1):
        if tuple(s[-k:]) == gate[:k]:return k
    return 0

def add_linear_bounds(low,high,a,b):
    # enforce a*t+b>=0 on integer t
    if a>0:low=max(low,ceildiv(-b,a))
    elif a<0:high=min(high,(-b)//a) # floor(b/-a) equivalent to floor((-b)/a)
    elif b<0:return (1,0)
    return low,high

def compile_row(g,n,y,W):
    """Dict (q,tag,r) -> disjoint intervals [t0,t1], V=6*t+r."""
    gate=GATES[g]
    if len(y)!=5: raise ValueError("five-axis restricted X6 chart")
    mass=sum(map(abs,y))
    if n<0 or (n-mass)%2 or n<mass or W<0:return {}
    m=(n-mass)//2
    ya,yb,yc,yd,ye=y
    ap=max(ya,0); am=max(-ya,0);bp=max(yb,0);bm=max(-yb,0); S=abs(yd)+abs(ye)
    ell=min(3,n)
    raw=defaultdict(list)
    for s in SUFFIXES[ell]:
        counts=[s.count(c) for c in COLORS]
        ua,ub,uB,uc,ux=counts
        sb=ub+uB;sc=uc
        q=terminal(s,gate)
        first=next((SRC[c] for c in s if c in SRC),"N")
        A=max(0,ua-ap)
        K=ux-am-S
        # SOURCE_FIRST_IN_PREFIX: freely permute prefix to place a desired source first.
        if n>ell:
            for tag in ("B","C"):
                B=max(0,ub-bp,uB-bm)
                C=max(0,ceildiv(uc-abs(yc),2))
                if tag=="B": B=max(B,ceildiv(sb+1-abs(yb),2))
                else: C=max(C,ceildiv(sc+1-abs(yc),2))
                if W<C: continue
                for r in range(6):
                    low=0; high=(2*m-r)//6
                    if high<0:continue
                    # L={0,V+W-m+A,ceil((V+W-m+K)/3)}
                    # U={V-B,floor((V+W-B-C)/2)}
                    lower=[(0,0),(6,r+W-m+A),(2,ceildiv(r+W-m+K,3))]
                    upper=[(6,r-B),(3,(r+W-B-C)//2)]
                    for aa,bb in lower:
                        for cc,dd in upper:
                            low,high=add_linear_bounds(low,high,cc-aa,dd-bb)
                    if low<=high:raw[q,tag,r].append((low,high))
        # SOURCE_FIRST_IN_SUFFIX: prefix source-free, exact B/c total counts.
        if yb != ub-uB or sc<abs(yc) or (sc-abs(yc))%2:continue
        Bfix=(sb-abs(yb))//2
        Cfix=(sc-abs(yc))//2
        if Bfix<0 or Cfix<0 or W<Cfix:continue
        low_V=max(W+Bfix-Cfix, 2*(ux-am-S-m)-W+3*(Cfix+Bfix))
        high_V=2*m-W-Cfix-Bfix-2*A
        for r in range(6):
            if (r+W-Cfix-Bfix)%2:continue
            low=max(0,ceildiv(low_V-r,6))
            high=min((2*m-r)//6,(high_V-r)//6)
            if low<=high: raw[q,first,r].append((low,high))
    merged={}
    for key,vals in raw.items():
        vals.sort(); out=[]
        for lo,hi in vals:
            if out and lo<=out[-1][1]+1:out[-1]=(out[-1][0],max(out[-1][1],hi))
            else:out.append((lo,hi))
        merged[key]=out
    return merged

def supported_from_compiler(comp,V):
    r=V%6;t=(V-r)//6
    return {(q,tag) for (q,tag,rr), intervals in comp.items() if r==rr and any(lo<=t<=hi for lo,hi in intervals)}

def sum_moment(comp,L,H,tag=None):
    """Inclusive integer range; return (F=sum support sizes,T=sum (V+1)k)."""
    if H<L:return (0,0)
    F=T=0
    for (q,tt,r), intervals in comp.items():
        if tag is not None and tt!=tag:continue
        tl=ceildiv(L-r,6);th=(H-r)//6
        for a,b in intervals:
            lo=max(a,tl);hi=min(b,th)
            if lo>hi:continue
            count=hi-lo+1
            F+=count
            T+=count*(3*(lo+hi)+r+1)
    return F,T

def occupancy_observe(cnt):
    y=tuple(cnt[2*i]-cnt[2*i+1] for i in range(5))
    p=[min(cnt[2*i],cnt[2*i+1]) for i in range(5)]
    return y,p[1]+2*p[3]+p[4],p[2]+p[4]

def native_baseline(n,g):
    """Independent ordered-word dynamic programming; actual primitive steps.
       (counts10,q,t) is retained and no observer collapse occurs until final readout.
    """
    gate=GATES[g]; initial=((0,)*10,0,"N")
    states={initial}
    cmap=(0,4,1,2,3,3,4,4,4,4)
    for _ in range(n):
        new=set()
        for counts,q,t in states:
            for i,col in enumerate(cmap):
                c=tuple(x+(j==i) for j,x in enumerate(counts))
                seq=gate[:q]+(col,)
                nq=terminal(seq,gate)
                nt=t if t!="N" else SRC.get(col,"N")
                new.add((c,nq,nt))
        states=new
    rows=defaultdict(lambda:defaultdict(set))
    for counts,q,t in states:
        y,V,W=occupancy_observe(counts)
        rows[y,W][V].add((q,t))
    return rows,len(states)

def independent_occ_baseline(n,g):
    """Separate 10-direction occupancy enumerator + 5-color suffix lifting.
       Used for long probes without DP ordered-state explosion.
    """
    gate=GATES[g]
    def comp(total,k):
        if k==1:yield (total,);return
        for z in range(total+1):
            for rest in comp(total-z,k-1):yield (z,)+rest
    rows=defaultdict(lambda:defaultdict(set))
    for cnt in comp(n,10):
        y,V,W=occupancy_observe(cnt)
        K=(cnt[0],cnt[2],cnt[3],cnt[4]+cnt[5],cnt[1]+sum(cnt[6:]))
        ell=min(3,n)
        for s in SUFFIXES[ell]:
            used=tuple(s.count(c) for c in range(5))
            if any(used[c]>K[c] for c in range(5)):continue
            rem=tuple(K[c]-used[c] for c in range(5))
            q=terminal(s,gate)
            Bs=rem[1]+rem[2]
            Cs=rem[3]
            if Bs:rows[y,W][V].add((q,"B"))
            if Cs:rows[y,W][V].add((q,"C"))
            if Bs==Cs==0:
                first=next((SRC[c] for c in s if c in SRC),"N")
                rows[y,W][V].add((q,first))
    return rows

def run():
    began=time.perf_counter()
    summary={"certificate":"PREFIX508_EXPLICIT_MOD6_COMPILER","status":"ALL_CHECKS_PASS", "scope":"native ten-direction DP, exact integer computations, fixed-gate X6 five-axis subfamily", "gates":{},"large_probe":[],"hole":{}}
    # Independent ordered-source DP, full rows n=0..6 and deterministic sample at n=7..9
    for g in GATES:
        details=[]
        for n in range(10):
            native,numstates=native_baseline(n,g)
            keys=sorted(native)
            samples=keys if n<=6 else keys[::max(1,len(keys)//180)]
            checked=0;intervals=0
            for y,W in samples:
                exact=native[y,W]
                compiler=compile_row(g,n,y,W)
                for V in range(n+1):
                    wanted=exact.get(V,set())
                    actual=supported_from_compiler(compiler,V)
                    if actual!=wanted:
                        raise AssertionError({"gate":g,"n":n,"y":y,"W":W,"V":V,"expected":sorted(wanted),"actual":sorted(actual)})
                    checked+=1
                # All interval moments, incl beyond valid range and empty spans
                for L in range(-2,n+2):
                    for H in range(L,n+2):
                        expF=sum(len(exact.get(v,())) for v in range(L,H+1))
                        expT=sum((v+1)*len(exact.get(v,())) for v in range(L,H+1))
                        F,T=sum_moment(compiler,L,H)
                        if (F,T)!=(expF,expT):raise AssertionError((g,n,y,W,L,H,F,T,expF,expT))
                        intervals+=1
            details.append({"n":n,"native_occupancy_controller_states":numstates,"total_rows":len(keys),"tested_rows":len(samples),"V_memberships_checked":checked,"interval_moments_checked":intervals})
        summary["gates"][g]=details
    # Large n probe: independently compute BRC row by explicit occupancy enumerations of d,e
    rng=random.Random(508)
    for g in GATES:
        for n in [9,17,32,64,127]:
            for j in range(6):
                # sample an achievable source row: build random signed direction occupancies
                counts=[0]*10
                for _ in range(n):counts[rng.randrange(10)]+=1
                y,V,W=occupancy_observe(counts)
                compiler=compile_row(g,n,y,W)
                # reference enumerator samples all nonnegative (d,e) for chosen V and W,
                # then builds explicit 5-color suffix supports independently.
                m=(n-sum(map(abs,y)))//2
                ref=set()
                for e in range(min(m,W)+1):
                    dmax=m-e
                    for d in range(dmax+1):
                        p=[m-V-W+d+e,V-2*d-e,W-e,d,e]
                        if any(q<0 for q in p):continue
                        ya,yb,yc,yd,ye=y
                        k=(p[0]+max(ya,0),p[1]+max(yb,0),p[1]+max(-yb,0),2*p[2]+abs(yc),p[0]+max(-ya,0)+2*d+2*e+abs(yd)+abs(ye))
                        for s in SUFFIXES[3]:
                            used=[s.count(c) for c in COLORS]
                            if any(used[i]>k[i] for i in COLORS):continue
                            rem=[k[i]-used[i] for i in COLORS]
                            q=terminal(s,GATES[g])
                            if rem[1]+rem[2]:ref.add((q,"B"))
                            if rem[3]:ref.add((q,"C"))
                            if not (rem[1]+rem[2]+rem[3]):ref.add((q,next((SRC[c] for c in s if c in SRC),"N")))
                got=supported_from_compiler(compiler,V)
                if ref!=got:raise AssertionError((g,n,y,V,W,ref,got))
                summary["large_probe"].append({"gate":g,"n":n,"y":list(y),"V":V,"W":W,"states":len(got)})
    # BRC hole from PREFIX-507
    for g in GATES:
        comp=compile_row(g,2,(0,0,0,0,0),0)
        occupied=[v for v in range(3) if (0,"N") in supported_from_compiler(comp,v)]
        assert occupied==[0,2]
        summary["hole"][g]=occupied
    summary["elapsed_seconds"]=round(time.perf_counter()-began,3)
    return summary

if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,separators=(',',':')))
