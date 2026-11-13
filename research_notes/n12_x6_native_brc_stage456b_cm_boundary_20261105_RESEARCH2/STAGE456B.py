"""Stage456-B: c=m boundary extension for binary BRC grouped support.

Native X6 ordered paths restricted to A=+E1, B=-E1 at input,
A endpoints, isolated B. Future probes: both sources can APPEND in 12
native signed directions; P has zero POP, Q POP only down to length >=m.
This script counts source-distinct histories by exact integer arithmetic.
"""
from collections import defaultdict
from functools import lru_cache
import json
import random

@lru_cache(None)
def prefix(m,kp,kq,d):
    """(bq, q_m) -> multiplicity of ordered P/Q prefixes of length m.
    P_1=P_m=Q_1=A, both isolated B, exact B counts in P and Q prefix,
    and exactly d mismatching paired positions.
    """
    cur={(0,0,0,0,0):1}  # bp,bq,mismatch,last_p,last_q
    for i in range(1,m+1):
        nxt=defaultdict(int)
        for (bp,bq,mis,lp,lq),v in cur.items():
            for p in (0,1):
                if (i==1 or i==m) and p:continue
                if i>1 and lp and p:continue
                for q in (0,1):
                    if i==1 and q:continue
                    if i>1 and lq and q:continue
                    pp,qq,dd=bp+p,bq+q,mis+(p!=q)
                    if pp<=kp and qq<=kq and dd<=d:
                        nxt[pp,qq,dd,p,q]+=v
        cur=nxt
    out=defaultdict(int)
    for (bp,bq,dd,lp,lq),v in cur.items():
        if bp==kp and dd==d:out[bq,lq]+=v
    return dict(out)

@lru_cache(None)
def gap(g,left,right,kq):
    """Q-only gap mass by #B with exact endpoint adjacency."""
    if g==0:return {0:1}
    states={(left,0):1}
    for _ in range(g):
        nxt=defaultdict(int)
        for (last,b),v in states.items():
            for q in (0,1):
                if last and q:continue
                if b+q<=kq:nxt[q,b+q]+=v
        states=nxt
    out=defaultdict(int)
    for (last,b),v in states.items():
        if not(last and right):out[b]+=v
    return dict(out)

@lru_cache(None)
def visible_summaries(m,n,t,u):
    """C(sigma) for distinct visible repair keys, without listing keys."""
    visible=sorted(set([m] if u==m else []).union(i for i in range(m+1,n+1) if i<=t or i>=u))
    # v (# visible B for i>m), q_m, q_{m+1}, q_t, q_u, prev_index,prev_letter
    states={(0,-1,-1,-1,-1,-1,-1):1}
    for i in visible:
        nxt=defaultdict(int)
        for (v,qm,qfirst,qt,qu,prev,last),multiplicity in states.items():
            for q in ((0,) if i==n else (0,1)):
                if prev==i-1 and last and q:continue
                nxt[(v+(q if i>m else 0),
                     q if i==m else qm,
                     q if i==m+1 else qfirst,
                     q if i==t and t>m else qt,
                     q if i==u and u>m else qu,
                     i,q)]+=multiplicity
        states=nxt
    # discard final index and letter; other summaries encode all needed boundary data
    grouped=defaultdict(int)
    for (v,qm,qfirst,qt,qu,_,_),count in states.items():
        grouped[v,qm,qfirst,qt,qu]+=count
    return dict(grouped)

def grouped(m,n,kp,kq,d,pq,rp):
    assert 2<=m<n and 0<=pq<=n-m and rp>=0
    u=n-pq # c=m iff minimal Q length >=m
    t=min(n,m+rp)
    g=max(0,u-t-1)
    P=prefix(m,kp,kq,d)
    C=visible_summaries(m,n,t,u)
    qf=0;pop=0;nonzero_summaries=0
    for (v,qm,qfirst,qt,qu),number_keys in C.items():
        mass=0
        for (bq,lastq),num_pre in P.items():
            if qm!=-1 and qm!=lastq:continue
            # when first post-m Q is visible, enforce Q_m -> Q_{m+1}
            if qfirst!=-1 and lastq and qfirst:continue
            # only possible hidden gap when t=m is immediately after Q_m
            if g:
                left=qt if t>m else lastq
                right=qu
                w=gap(g,left,right,kq).get(kq-bq-v,0)
            else:
                w=int(kq==bq+v)
            mass+=num_pre*w
        if mass:
            nonzero_summaries+=1
            qf+=number_keys
            pop+=number_keys*mass
    return dict(qF=str(qf),population=str(pop),summaries=nonzero_summaries,
                C_states=len(C),prefix_states=len(P),c=m,t=t,u=u,g=g)

def words(n,k):
    out=[]
    def visit(s,b):
        if len(s)==n:
            if b==k:out.append(s)
            return
        for a in (0,1):
            if a and (len(s)==0 or len(s)==n-1 or s[-1]):continue
            if b+a<=k:visit(s+(a,),b+a)
    visit((),0)
    return out

def brute(m,n,kp,kq,d,pq,rp):
    u=n-pq;t=min(n,m+rp)
    S=sorted(set([m] if u==m else []).union(i for i in range(m+1,n+1) if i<=t or i>=u))
    classes=defaultdict(int)
    for p in words(m,kp):
        for q in words(n,kq):
            if sum(a!=b for a,b in zip(p,q))!=d:continue
            key=tuple(q[i-1] for i in S)
            classes[key]+=1
    return str(len(classes)),str(sum(classes.values()))

def main():
    rand=random.Random(456)
    checked=nonempty=0;totalhist=totalclasses=0
    special=[]
    for _ in range(1600):
        m=rand.randint(2,9);n=rand.randint(m+1,min(13,m+5))
        kp=rand.randint(0,min(2,(m-2)//2))
        kq=rand.randint(0,min(3,(n-2)//2))
        d=rand.randint(0,min(m,4))
        pq=rand.randint(0,n-m) # exactly c=m
        rp=rand.randint(0,n-m+2)
        x=m,n,kp,kq,d,pq,rp
        g=grouped(*x);b=brute(*x)
        if (g['qF'],g['population'])!=b:
            raise AssertionError((x,g,b))
        checked+=1
        nonempty+=int(int(g['population'])>0)
        totalhist+=int(g['population']);totalclasses+=int(g['qF'])
        if len(special)<7 and g['g']>0 and g['population']!='0' and rp==0:
            special.append(dict(parameters=x,result=g))
    large=[]
    for x in [
        (64,80,15,17,1,0,0),
        (64,80,15,17,1,5,0),
        (64,80,15,17,1,5,3),
        (64,80,15,17,1,16,0),
        (92,126,20,25,3,12,7)]:
        large.append({'parameters':x,'result':grouped(*x)})
    print(json.dumps({'marker':'STAGE456B_CM_BOUNDARY_GROUPED_DP_PASS',
        'model':'P_POP=0, Q_POP<=n-m, binary isolated initial defects, full native 12-direction future append',
        'oracle':{'cases':checked,'nonempty':nonempty,'population_sum':str(totalhist),
            'class_count_sum':str(totalclasses)},'edge_examples':special,
        'large':large},indent=2))
if __name__=='__main__':main()
