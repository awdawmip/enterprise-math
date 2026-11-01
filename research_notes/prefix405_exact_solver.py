#!/usr/bin/env python3
"""PREFIX-405: exact rational, replayable all-six-band phase-fiber feasibility.

External static five-Port complex-amplitude model only. No native P000/BRC arithmetic.
The branch-and-bound algorithm is sound at every step, terminates for every NO
and for every record with a strictly feasible source; boundary-only YES may UNKNOWN.
"""
from __future__ import annotations
from collections import deque
from fractions import Fraction as Q
from math import isqrt
import json

C = tuple[Q, Q]

def c(r=0, i=0) -> C:
    return (Q(r), Q(i))
def add(x: C, y: C) -> C:
    return (x[0]+y[0], x[1]+y[1])
def neg(x: C) -> C:
    return (-x[0], -x[1])
def sub(x: C, y: C) -> C:
    return add(x, neg(y))
def mul(x: C, y: C) -> C:
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def div(x: C, y: C) -> C:
    t=y[0]*y[0]+y[1]*y[1]
    assert t > 0
    return ((x[0]*y[0]+x[1]*y[1])/t,
            (x[1]*y[0]-x[0]*y[1])/t)
def sqabs(x: C) -> Q:
    return x[0]**2+x[1]**2
def l1(x: C) -> Q:
    return abs(x[0])+abs(x[1])
def times_i(x: C) -> C:
    return (-x[1], x[0])

a4=c(Q(5,2), Q(9,2)); b4=c(Q(3,2), Q(7,2)); c4=c(0,4)
a5=c(Q(11,4), Q(15,8)); b5=a5; c5=c(Q(5,4),Q(9,4))
# Measurement order is preserved (I2, Cu, I3, Cv, I4, I5).
OBS={
    'I2':(c(),c(1),c()),
    'Cu':(c(1),c(1),c()),
    'I3':(c(),c(),c(1)),
    'Cv':(c(1),c(),c(1)),
    'I4':(a4,b4,c4),
    'I5':(a5,b5,c5),
}
ORDER=tuple(OBS)
BANDS= dict[str, tuple[Q,Q]]
BOX=tuple[tuple[Q,Q],tuple[Q,Q],tuple[Q,Q],tuple[Q,Q]]

def calc(u:C,v:C) -> dict[str,Q]:
    return {k:sqabs(add(add(a,mul(b,u)),mul(d,v))) for k,(a,b,d) in OBS.items()}
def sqrt_bounds(q:Q,den:int=1000) -> tuple[Q,Q]:
    """Exact rational floor/ceiling enclosing sqrt(q), q>=0."""
    assert q>=0 and den>=1
    n=isqrt((q.numerator*den*den)//q.denominator)
    lo=Q(n,den)
    hi=lo if lo*lo==q else Q(n+1,den)
    assert lo*lo<=q<=hi*hi
    return (lo,hi)

def axis_bounds(qband: tuple[Q,Q], pband:tuple[Q,Q],R:Q,
                den:int) -> list[tuple[tuple[Q,Q],tuple[Q,Q]]]:
    """Every z with |z|^2 in qband and |1+z|^2 in pband lies
    in the returned exact rational x/y rectangles; split Im-sign.
    The rectangles may be strict supersets of the feasible set.
    """
    qlo,qhi=qband; plo,phi=pband
    if qhi<0 or plo>phi or qlo>qhi: return []
    xlo=max(-R,(plo-1-qhi)/2)
    xhi=min( R,(phi-1-max(0,qlo))/2)  # q>=0 tightens upper x bound
    # Lower x bound must also tighten q>=0, which is already qhi>=0.
    if xlo>xhi: return []
    max_x2=max(xlo*xlo,xhi*xhi)
    min_x2=Q(0) if xlo<=0<=xhi else min(xlo*xlo,xhi*xhi)
    yl2=max(Q(0),max(Q(0),qlo)-max_x2)
    yh2=qhi-min_x2
    if yh2<yl2: return []
    yl=sqrt_bounds(yl2,den)[0]
    yh=sqrt_bounds(yh2,den)[1]
    if yl>yh: return []
    if yl==0:
        return [((xlo,xhi),(-yh,yh))]
    return [((xlo,xhi),(-yh,-yl)),((xlo,xhi),(yl,yh))]

def initial_boxes(bands:BANDS,den:int=1000) -> list[BOX]:
    assert set(bands)==set(ORDER)
    if any(lo>hi for lo,hi in bands.values()):return []
    q2=bands['I2'][1];q3=bands['I3'][1]
    if q2<0 or q3<0:return []
    R=Q(1)+max(q2,q3)
    U=axis_bounds(bands['I2'],bands['Cu'],R,den)
    V=axis_bounds(bands['I3'],bands['Cv'],R,den)
    return [(u[0],u[1],v[0],v[1]) for u in U for v in V]

def center(box:BOX) -> tuple[Q,Q,Q,Q]:
    return tuple((l+h)/2 for l,h in box) # type: ignore

def enclose(box:BOX,name:str) -> tuple[Q,Q]:
    a,b,d=OBS[name]
    xs=center(box);u=c(xs[0],xs[1]);v=c(xs[2],xs[3])
    w=add(add(a,mul(b,u)),mul(d,v))
    radii=[(hi-lo)/2 for lo,hi in box]
    coeff=(b,times_i(b),d,times_i(d))
    D=sum((l1(k)*r for k,r in zip(coeff,radii)),Q(0))
    U=l1(w)
    E=2*U*D+D*D
    w2=sqabs(w)
    return (max(Q(0),w2-E),w2+E)

def reject(box:BOX,bands:BANDS) -> str|None:
    for name in ORDER:
        l,h=enclose(box,name)
        lo,hi=bands[name]
        if h<lo or hi<l: return name
    return None

def center_works(box:BOX,bands:BANDS) -> bool:
    z=center(box);vals=calc(c(z[0],z[1]),c(z[2],z[3]))
    return all(bands[k][0]<=vals[k]<=bands[k][1] for k in ORDER)

def split(box:BOX,axis:int) -> tuple[BOX,BOX]:
    lo,hi=box[axis]; m=(lo+hi)/2
    assert lo<hi
    a=list(box); b=list(box)
    a[axis]=(lo,m);b[axis]=(m,hi)
    return (tuple(a),tuple(b))  # type: ignore

def solve(bands:BANDS,budget:int=5000,den:int=1000):
    roots=initial_boxes(bands,den)
    if not roots:return {'status':'NO','roots':0,'nodes':{},'tested':0,'den':den}
    jobs=deque((str(i),box) for i,box in enumerate(roots))
    nodes={};tested=0
    while jobs and tested<budget:
        path,box=jobs.popleft();tested+=1
        denied=reject(box,bands)
        if denied is not None:
            nodes[path]={'kind':'exclude','by':denied}
            continue
        if center_works(box,bands):
            z=center(box)
            return {'status':'YES','u':c(z[0],z[1]),'v':c(z[2],z[3]),'tested':tested,'nodes':nodes}
        widths=[hi-lo for lo,hi in box]
        axis=max(range(4),key=lambda j:widths[j])
        if widths[axis]==0: # exact point would have been excluded or accepted
            raise AssertionError('non-feasible exact point not excluded')
        nodes[path]={'kind':'split','axis':axis}
        left,right=split(box,axis)
        jobs.append((path+'0',left));jobs.append((path+'1',right))
    if jobs:return {'status':'UNKNOWN','tested':tested,'pending':len(jobs)}
    return {'status':'NO','roots':len(roots),'nodes':nodes,'tested':tested,'den':den}

def verify_no_certificate(bands:BANDS,certificate:dict)->bool:
    assert certificate['status']=='NO'
    roots=initial_boxes(bands,certificate['den'])
    assert len(roots)==certificate['roots']
    nodes=certificate['nodes']
    visited=set()
    def walk(path:str,box:BOX):
        assert path not in visited and path in nodes
        visited.add(path)
        node=nodes[path]
        if node['kind']=='exclude':
            assert node['by'] in ORDER
            vl,vh=enclose(box,node['by']);ql,qh=bands[node['by']]
            assert vh<ql or qh<vl
            return
        assert node['kind']=='split'
        axis=node['axis']; assert axis in range(4)
        left,right=split(box,axis)
        walk(path+'0',left);walk(path+'1',right)
    for j,box in enumerate(roots):walk(str(j),box)
    assert visited==set(nodes)
    return True

# Original A[0:3] source reconstruction and full port check.
A=[
    [c(4),c(4),c()],
    [c(),c(-4),c(4)],
    [c(-5,3),c(),c(-3,1)],
    [c(-2,-2),c(4,4),c(2,2)],
    [c(-2),c(),c(5,2)],
]
def reconstruct(u:C,v:C) -> list[C]:
    M=[A[i][:]+[w] for i,w in enumerate([c(1),u,v])]
    for k in range(3):
        piv=next(i for i in range(k,3) if M[i][k] != c())
        M[k],M[piv]=M[piv],M[k]
        w=M[k][k]
        M[k]=[div(x,w) for x in M[k]]
        for i in range(3):
            if i==k:continue
            f=M[i][k]
            M[i]=[sub(s,mul(f,t)) for s,t in zip(M[i],M[k])]
    return [M[i][3] for i in range(3)]
def ports(Y:list[C]) -> list[Q]:
    return [sqabs(sum_complex(mul(a,b) for a,b in zip(row,Y))) for row in A]
def sum_complex(z) -> C:
    out=c()
    for v in z:out=add(out,v)
    return out

def J(lo,hi):return (Q(lo),Q(hi))
def sample_bands(i4lo:Q,i4hi:Q) -> BANDS:
    eps=Q(1,10000)
    return {
       'I2':(1-eps,1+eps),
       'Cu':(2-eps,2+eps),
       'I3':(Q(0),eps),
       'Cv':(1-eps,1+eps),
       'I4':(Q(i4lo),Q(i4hi)),
       'I5':(Q(22),Q(23)),
    }
def clean_dict(o):
    if isinstance(o,Q):return f'{o.numerator}/{o.denominator}'
    if isinstance(o,tuple):return [clean_dict(x) for x in o]
    if isinstance(o,list):return [clean_dict(x) for x in o]
    if isinstance(o,dict):return {k:clean_dict(v) for k,v in o.items()}
    return o

def tests():
    plus=calc(c(0,1),c()); minus=calc(c(0,-1),c())
    assert plus=={'I2':1,'Cu':2,'I3':0,'Cv':1,'I4':37,'I5':Q(709,32)}
    assert minus=={**plus,'I4':Q(45)}
    Aplus=reconstruct(c(0,1),c());Aminus=reconstruct(c(0,-1),c())
    assert ports(Aplus)==[1,1,0,37,Q(709,32)]
    assert ports(Aminus)==[1,1,0,45,Q(709,32)]
    no=sample_bands(40,42)
    rno=solve(no,budget=5000)
    assert rno['status']=='NO',rno
    assert verify_no_certificate(no,rno)
    assert rno['roots']==2 and rno['tested']==2,rno
    assert [rno['nodes'][str(i)]['by'] for i in range(2)]==['I4','I4']
    yesp=solve(sample_bands(36,38),budget=5000)
    yesm=solve(sample_bands(44,46),budget=5000)
    assert yesp['status']=='YES' and yesm['status']=='YES',(yesp,yesm)
    for r,band in [(yesp,sample_bands(36,38)),(yesm,sample_bands(44,46))]:
        vals=calc(r['u'],r['v']); assert all(band[k][0]<=vals[k]<=band[k][1] for k in ORDER)
        Y=reconstruct(r['u'],r['v'])
        measured=ports(Y)
        assert measured==[1,vals['I2'],vals['I3'],vals['I4'],vals['I5']]
    original_no={
       'I2':J(0,Q(1,1000000)), 'Cu':J(Q(99,100),Q(101,100)),
       'I3':J(0,Q(1,1000000)), 'Cv':J(Q(99,100),Q(101,100)),
       'I4':J(0,1),'I5':J(10,12)
    }
    rn=solve(original_no,budget=5000)
    assert rn['status']=='NO' and verify_no_certificate(original_no,rn),rn
    # Explicit algebraic robust exclusion on the noisy midpoint.
    delta=Q(459,10000)
    ep=2*7*delta+delta**2;em=2*9*delta+delta**2
    gap=min(Q(40)-(Q(37)+ep),(Q(45)-em)-Q(42))
    assert ep==Q(64470681,100000000)
    assert em==Q(82830681,100000000)
    assert gap==Q(217169319,100000000)
    # Check rational imaginary axis hull enclosing all admissible points.
    eps=Q(1,10000)
    assert Q(9999,10000)-eps**2>Q(999,1000)**2
    assert Q(10001,10000)<Q(1001,1000)**2
    return {
       'status':'PASS_PREFIX405_COMPLETE_NO_SEMIDECISION_AND_ROBUST_NONCONVEXITY',
       'noisy_midpoint':rno,
       'positive_branch':{'status':yesp['status'],'u':yesp['u'],'v':yesp['v'],'Y':reconstruct(yesp['u'],yesp['v'])},
       'negative_branch':{'status':yesm['status'],'u':yesm['u'],'v':yesm['v'],'Y':reconstruct(yesm['u'],yesm['v'])},
       'legacy_far_no':{'status':rn['status'],'checked':rn['tested'],'nodes':len(rn['nodes'])},
       'gap':gap,'E_plus':ep,'E_minus':em,
       'model':'external auxiliary static normalized I1=1',
       'witness_branches':2,
       'no_certificate_replayed':True,
    }
if __name__=='__main__':
    print(json.dumps(clean_dict(tests()),ensure_ascii=False,sort_keys=True,indent=2))
