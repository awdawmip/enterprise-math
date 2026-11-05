#!/usr/bin/env python3
"""PREFIX-510: exact t=N W-prefix for restricted native X6 BRC observer.
Exhaustive DP on signed native directions a/A,d/D,e/E only (the t=N subset).
This tests an exact combinatorial BRC cancellation observable; NO physical evolution,
pi/trigonometric or classical rotation computations are performed.
"""
from collections import defaultdict
import json, hashlib, time

GATES={'aab':(0,0,1), 'aba':(0,1,0)}
NATIVE=((0,1,0),(0,-1,4),(1,1,4),(1,-1,4),(2,1,4),(2,-1,4))

def terminal(seq,gate):
    for k in range(min(len(seq),len(gate)),0,-1):
        if tuple(seq[-k:])==gate[:k]:return k
    return 0

def exact_controls(g,n,ya,yd,ye,V,W):
    S=abs(yd)+abs(ye)
    if n<0 or n<abs(ya)+S or (n-abs(ya)-S)%2 or W<0:return set()
    m=(n-abs(ya)-S)//2
    if V<W or (V-W)%2:return set()
    e=W; d=(V-W)//2
    if d<0 or d+e>m:return set()
    pa=m-d-e
    Aplus=pa+max(ya,0)
    X=pa+max(-ya,0)+2*(d+e)+S
    gate=g
    out=set()
    if X>0 or n==0:out.add(0)
    if Aplus>=1:
        if gate=='aba' or X>0 or Aplus==1:out.add(1)
    if gate=='aab' and Aplus>=2:out.add(2)
    return out

def N_j(L,a,j):
    return max(0,min(L+1,L+a-j+1))

def W_mass(g,n,ya,yd,ye,W):
    S=abs(yd)+abs(ye)
    if n<0 or n<abs(ya)+S or (n-abs(ya)-S)%2:return 0
    m=(n-abs(ya)-S)//2
    if W<0 or W>m:return 0
    L=m-W;a=max(0,ya)
    k=L+1+N_j(L,a,1)+(N_j(L,a,2) if g=='aab' else 0)
    # Sole no-x observer: every native step is positive a (n=ya>0).
    if m==0 and S==0 and ya>0:
        k-=1+(int(g=='aab' and ya>=2))
    return k

def W_prefix(g,n,ya,yd,ye,j):
    S=abs(yd)+abs(ye)
    if n<0 or n<abs(ya)+S or (n-abs(ya)-S)%2:return 0
    m=(n-abs(ya)-S)//2
    j=max(0,min(j,m+1));a=max(0,ya)
    triangle=j*(j-1)//2
    if g=='aba':
        out=j*(2*m+1+(a>=1))-2*triangle
    else:
        if a>=2:out=3*j*(m+1)-3*triangle
        elif a==1:out=j*(3*m+2)-3*triangle
        else:out=3*j*m-3*triangle+int(j==m+1)
    if j>=1 and m==0 and S==0 and ya>0:
        out-=1+int(g=='aab' and ya>=2)
    return out

def native_DP(nmax,g):
    # DP holds only the first-source N paths: no native b/B,c/C directions.
    # state: (ya,yd,ye,V,W,q), path multiplicity discarded intentionally.
    gate=GATES[g]; st={(0,0,0,0,0,0)}
    for n in range(nmax+1):
        byrow=defaultdict(set)
        for ya,yd,ye,V,W,q in st:
            byrow[(ya,yd,ye,V,W)].add(q)
        yield n,byrow
        ns=set()
        for ya,yd,ye,V,W,q in st:
            y=(ya,yd,ye)
            for axis,sgn,col in NATIVE:
                zz=list(y);cancel=(zz[axis]*sgn<0);zz[axis]+=sgn
                vv=V+(2 if axis==1 else 1 if axis==2 else 0)*int(cancel)
                ww=W+int(cancel and axis==2)
                qq=terminal(gate[:q]+(col,),gate)
                ns.add((*zz,vv,ww,qq))
        st=ns

def run(nmax=12):
    t=time.time(); totals={}; checked=0; rows=0; prefixes=0; anomalies=[]
    for g in GATES:
        entry={}
        for n,dp in native_DP(nmax,g):
            observed=defaultdict(lambda:defaultdict(set))
            for (ya,yd,ye,V,W),qset in dp.items():
                predicted=exact_controls(g,n,ya,yd,ye,V,W)
                assert predicted==qset, (g,n,(ya,yd,ye,V,W),qset,predicted)
                checked+=1
                observed[(ya,yd,ye)][W].update((V,q) for q in qset)
            for y,rows_by_w in observed.items():
                ya,yd,ye=y; S=abs(yd)+abs(ye);m=(n-abs(ya)-S)//2
                assert m>=0
                for w in range(m+1):
                    k=len(rows_by_w.get(w,set()))
                    assert k==W_mass(g,n,*y,w),(g,n,y,w,k,W_mass(g,n,*y,w))
                    rows+=1
                for j in range(m+2):
                    actual=sum(len(rows_by_w.get(w,set())) for w in range(j))
                    formula=W_prefix(g,n,*y,j)
                    assert actual==formula,(g,n,y,j,actual,formula)
                    prefixes+=1
            entry[str(n)]={'native_no_source_states':sum(len(v) for v in dp.values()),
                           'nonempty_yVW_rows':len(dp),'signed_y_keys':len(observed)}
        totals[g]=entry
    for m in range(0,50):
        for ya in (-5,-2,-1,0,1,2,5):
            for yd,ye in ((0,0),(1,0),(-2,1),(2,3)):
                n=abs(ya)+abs(yd)+abs(ye)+2*m
                for g in GATES:
                    direct=sum(W_mass(g,n,ya,yd,ye,w) for w in range(m+1))
                    assert W_prefix(g,n,ya,yd,ye,m+1)==direct
    result={'status':'ALL_CHECKS_PASS','scope':'native X6 five-axis subfamily, t=N no-source observer, exactly six a/A/d/D/e/E signed primitive steps',
            'full_native_DP_n_range':[0,nmax],'gate_stats':totals,'verified_point_support_rows':checked,
            'verified_W_row_masses':rows,'verified_W_prefix_sums':prefixes,
            'additional_m_values':50,'integer_semantics':'arbitrary precision Python integer; exact no tolerance',
            'elapsed_seconds_descriptive':round(time.time()-t,3)}
    return result
if __name__=='__main__':
    r=run(); print(json.dumps(r,ensure_ascii=False,indent=2))
