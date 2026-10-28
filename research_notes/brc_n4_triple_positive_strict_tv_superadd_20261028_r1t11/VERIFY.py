#!/usr/bin/env python3
"""Exact rational BRC N=4 two-law triple-positive TV superadditivity certificate.
Every assertion uses fractions.Fraction; no floating point or solver dependence.
This is an external finite sequential P/Q model, not Heartbeat native X6.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

Z,O=F(0),F(1)
ACT=('P','Q','C')
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
   2:{'AU':(F(1,6),O,'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),O,'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
    N[t]={}
    for pa,(q,r,_) in N[t-1].items():
        e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[pa] if t==3
           else Z if pa=='AV0' else F(3,50) if pa=='AV1' else F(1,20))
        for j,s in enumerate((-1,1)):
            N[t][pa+str(j)]=(q/2,r*(1+s*e),pa)
for t in N:
    assert len(N[t])==2**t and all(q>0 and r>0 for q,r,_ in N[t].values())
    assert sum((q for q,r,p in N[t].values()),Z)==sum((q*r for q,r,p in N[t].values()),Z)==O
    if t>1:
        for pa,(q,r,_) in N[t-1].items():
            children=[(qc,rc) for qc,rc,p in N[t].values() if p==pa]
            assert len(children)==2 and sum((v for v,_ in children),Z)==q
            assert sum((v*w for v,w in children),Z)==q*r

F0={(1,h):(Z,Z,O) for h in N[1]}
F0.update({(2,'AU'):(F(1,2),F(1,6),F(1,3)),(2,'AV'):(Z,Z,O),
           (2,'BU'):(Z,F(1,2),F(1,2)),(2,'BV'):(O,Z,Z)})
T3={'AU0':(Z,O,Z),'AU1':(O,Z,Z),'AV0':(Z,F(1,2),F(1,2)),
    'AV1':(Z,Z,O),'BU0':(Z,Z,O),'BU1':(Z,O,Z)}
F0.update({(3,h):T3.get(h,(O,Z,Z)) for h in N[3]})
F0.update({(4,h):((Z,O,Z) if r<F(2501,10000) else (O,Z,Z))
           for h,(q,r,p) in N[4].items()})

def full(e):
    assert Z<=e<=F(1,2)
    a=dict(F0);a[2,'BU']=(Z,F(1,2)-e,F(1,2)+e)
    return a

def law(actions):
    out=[Z]*16
    for leaf,(q,r,p) in N[4].items():
        alive=O
        for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
            u=actions[t,h]
            assert len(u)==3 and all(z>=0 for z in u) and sum(u,Z)==O
            assert t<4 or u[2]==Z
            j=2*(t-1)
            out[j]+=q*alive*u[0];out[j+1]+=q*alive*u[1]
            out[8+j]+=q*r*alive*u[0];out[9+j]+=q*r*alive*u[1]
            alive*=u[2]
        assert alive==Z
    assert sum(out[:8],Z)==sum(out[8:],Z)==O
    return out

def tv(a,b):
    return (sum((abs(x-y) for x,y in zip(a[:8],b[:8])),Z)/2,
            sum((abs(x-y) for x,y in zip(a[8:],b[8:])),Z)/2)

# Raw certification values x_t,h,a represent conditional occupation on labeled histories,
# not Q-multiplied flows; each stage's incoming mass is parent's continue occupancy.
def load():
    groups={};name=None
    for raw in Path(__file__).with_name('CERTIFICATES.txt').read_text(encoding='utf-8').splitlines():
        line=raw.strip()
        if not line or line.startswith('#'):continue
        if line.startswith('['):
            assert line.endswith(']');name=line[1:-1].split()[0];assert name not in groups
            groups[name]={};continue
        lhs,val=line.split('=');t,h,a=lhs.split('.');k=(int(t),h,a)
        assert k not in groups[name] and k[1] in N[k[0]] and k[2] in ACT
        groups[name][k]=F(val)
    assert set(groups)=={'S3_ZERO','S3_THRESHOLD','S3_HALF','S2_WITNESS','S23_WITNESS'}
    return groups

frozen=load()

def check_flow(X,mode,e,expect):
    # Automatically complete omitted zero occupancies and normalize a shared
    # behavior at zero-reached histories to an already reached fiber member.
    x={(t,h,k):X.get((t,h,k),Z) for t in N for h in N[t]
       for k in (ACT if t<4 else ('P','Q'))}
    assert all(v>=Z for v in x.values())
    incoming={}
    for t in N:
        for h in N[t]:
            s=O if t==1 else x[t-1,N[t][h][2],'C']
            incoming[t,h]=s
            assert sum((x[t,h,k] for k in (ACT if t<4 else ('P','Q'))),Z)==s
    must={4}|({2} if mode in ('S2','S23') else set())|({3} if mode in ('S3','S23') else set())
    compressed={}
    for t in must:
        by=defaultdict(list)
        for h,(q,r,p) in N[t].items():by[r].append(h)
        for r,histories in by.items():
            for h in histories:
                for k in (ACT if t<4 else ('P','Q')):
                    for g in histories:
                        assert x[t,h,k]*incoming[t,g]==x[t,g,k]*incoming[t,h]
            reached=next((h for h in histories if incoming[t,h]>0),None)
            if reached is not None:
                v=tuple(x[t,reached,k]/incoming[t,reached] for k in (ACT if t<4 else ('P','Q')))
                compressed[t,r]=v if t<4 else v+(Z,)
    policy={}
    for t in N:
        for h,(q,r,p) in N[t].items():
            if (t,r) in compressed:row=compressed[t,r]
            elif incoming[t,h]>0:
                row=tuple(x[t,h,k]/incoming[t,h] for k in (ACT if t<4 else ('P','Q')))
                if t==4:row=row+(Z,)
            else:row=(Z,Z,O) if t<4 else (O,Z,Z)
            policy[t,h]=row
            assert min(row)>=0 and sum(row,Z)==O
    out=law(policy)
    linear=[Z]*16
    for (t,h,k),z in x.items():
        if k=='C':continue
        q,r,p=N[t][h];j=2*(t-1)+(k=='Q')
        linear[j]+=q*z;linear[8+j]+=q*r*z
    assert out==linear
    dist=tv(out,law(full(e)))
    assert dist==expect, (mode,e,dist,expect)
    return x,out

# All terminal (t,label) scores are normalized signed two-law observers.
W2q=list(map(F,['0','0','25/253','25/253','25/253','25/253','25/253','-25/253']))
W2p=list(map(F,['0','0','-203/506','-203/506','-197/506','-197/506','-197/506','203/506']))
W23q=list(map(F,['0','0','1293/13085','1293/13085','3736/39255','3736/39255','3871/39255','-1293/13085']))
W23p=list(map(F,['0','0','-10499/26170','-10499/26170','-30353/78510','-30353/78510','-30503/78510','10499/26170']))
W3q=list(map(F,['1/10','1/10','751/7750','374/3875','374/3875','374/3875','1/10','-1/10']))
W3p=list(map(F,['2/5','2/5','-1544/3875','-617/1550','-617/1550','-617/1550','-2/5','2/5']))
WEIGHTS={'S2':W2q+W2p,'S3':W3q+W3p,'S23':W23q+W23p}
for w in WEIGHTS.values():
    assert max(w[:8])-min(w[:8])+max(w[8:])-min(w[8:])==O

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)

def bellman(W,mode):
    """Global linear minimum for every REAL randomized policy, via multi-affine vertices.
    S2/S23: exhaustive 3^2*3^3=243 stage1 and shared-stage2 prefix choices;
    terminal decisions are independently optimized (a LOWER relaxation, hence safe).
    S3: direct backward stochastic DP, t3 siblings share one action.
    """
    wq,wp=W[:8],W[8:]
    def c(t,h,k):
        r=N[t][h][1];j=2*(t-1)+(k=='Q')
        return wq[j]+r*wp[j]
    def tail(h):
        return sum((min(c(4,h+str(j),'P'),c(4,h+str(j),'Q'))/2 for j in (0,1)),Z)
    if mode=='S3':
        def v3(pa):
            if pa in ('AV','BV'):
                return min(sum((c(3,pa+str(j),k) if k!='C' else tail(pa+str(j))) for j in (0,1))/2
                           for k in ACT)
            return sum((min(c(3,pa+str(j),'P'),c(3,pa+str(j),'Q'),tail(pa+str(j)))
                        for j in (0,1)),Z)/2
        def v2(h):return min(c(2,h,'P'),c(2,h,'Q'),v3(h))
        def v1(h):
            ch=('AU','AV') if h=='A' else ('BU','BV')
            cont=sum((N[2][k][0]/N[1][h][0]*v2(k) for k in ch),Z)
            return min(c(1,h,'P'),c(1,h,'Q'),cont)
        return sum((N[1][h][0]*v1(h) for h in N[1]),Z),1
    best=None;count=0
    for first in product(ACT,repeat=2):
        t1=dict(zip(('A','B'),first))
        for second in product(ACT,repeat=3):
            count+=1;t2=dict(zip(('U','AV','BV'),second))
            cost=Z;reached=[]
            for h,(q,r,p) in N[1].items():
                if t1[h]!='C':cost+=q*c(1,h,t1[h])
            for h,(q,r,pa) in N[2].items():
                if t1[pa]!='C':continue
                act=t2['U' if h in ('AU','BU') else h]
                if act!='C':cost+=q*c(2,h,act)
                else:
                    reached.extend((q3,r3,h3) for h3,(q3,r3,parent) in N[3].items() if parent==h)
            if mode=='S2':
                for q,r,h in reached:
                    cost+=q*min(c(3,h,'P'),c(3,h,'Q'),tail(h))
            else:
                by=defaultdict(list)
                for q,r,h in reached:by[r].append((q,h))
                for r,pairs in by.items():
                    cost+=min(*(sum((q*(tail(h) if act=='C' else c(3,h,act)) for q,h in pairs),Z)
                                for act in ACT))
            best=cost if best is None else min(best,cost)
    assert count==243
    return best,count

expected_min={'S2':-F(153,506),'S3':-F(4747,15500),'S23':-F(7913,26170)}
results={}
for mode in ('S2','S3','S23'):
    got,n=bellman(WEIGHTS[mode],mode)
    assert got==expected_min[mode],(mode,got)
    results[mode]={'bellman_min':str(got),'prefix_cases':n}

e0=Z;ecrit=F(255,572);half=F(1,2);ew=F(9,20)
assert e0<ecrit<ew<half
x0,law0=check_flow(frozen['S3_ZERO'],'S3',e0,(Z,Z))
xc,lawc=check_flow(frozen['S3_THRESHOLD'],'S3',ecrit,(Z,Z))
xh,lawh=check_flow(frozen['S3_HALF'],'S3',half,(F(1,4000),F(1,4000)))
x2,law2=check_flow(frozen['S2_WITNESS'],'S2',ew,(F(37,30360),F(37,30360)))
x23,law23=check_flow(frozen['S23_WITNESS'],'S23',ew,(F(12907,9421200),F(12907,9421200)))

# Convex interpolation stays REAL S3 behavior, as incoming rates agree at
# all constrained same-LR groups. The target full-law is affine in epsilon.
def blend(a,b,t):return {k:(O-t)*v+t*b[k] for k,v in a.items()}
beta=(ew-ecrit)/(half-ecrit)
x3,law3=check_flow(blend(xc,xh,beta),'S3',ew,(F(3,155000),F(3,155000)))

Y=law(full(ew));d2=F(37,30360);d3=F(3,155000);d23=F(12907,9421200)
for mode,dist in [('S2',d2),('S3',d3),('S23',d23)]:
    low=expected_min[mode]-dot(WEIGHTS[mode],Y)
    assert low==dist,(mode,low,dist)
# Global S3 lower is max(0, minimum - W3*target); exact affine identity.
for ee in (e0,ecrit,F(1,4),ew,half):
    dual=expected_min['S3']-dot(WEIGHTS['S3'],law(full(ee)))
    assert max(Z,dual)==max(Z,F(143,31000)*(ee-ecrit))
assert expected_min['S3']-dot(WEIGHTS['S3'],law(full(ecrit)))==Z
assert expected_min['S3']-dot(WEIGHTS['S3'],law(full(half)))==F(1,4000)
# Lower dual holds for ALL e; exact S3 witnesses at e0,ecrit,1/2 and convex
# linearity upper yield the equality for every real e in [0,1/2].
gap=d23-d2-d3
assert gap==F(243712321,1847261790000)>0
out={
 'status':'PASS_EXACT_N4_TRIPLE_POSITIVE_STRICT_SUPERADD',
 'model':'external strictly-positive N4 two-law BRC labeled tree, 16 time-decision outputs',
 'epsilon_witness':'9/20',
 'd2':str(d2),'d3':str(d3),'d23':str(d23),
 'superadditivity_gap':str(gap),
 's3_phase':'d3(e)=143/31000 * max(0,e-255/572), 0<=e<=1/2',
 's3_threshold':str(ecrit),
 'S3_witness_mixing_weight':str(beta),
 'target_Q':[str(z) for z in Y[:8]],'target_P':[str(z) for z in Y[8:]],
 'witness_TV':{k: str(v) for k,v in [('S2',d2),('S3',d3),('S23',d23)]},
 'certificate_counts':{k:len(v) for k,v in frozen.items()},
 'global_full_behavior_bellman':results,
 'verification':'Python standard-library Fraction, exact, no LP or floating dependency',
 'mathematical_status':'AUTHOR_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED',
 'X6_native_correspondence':'NOT_PROVED',
}
if __name__=='__main__':
    print(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True))
    print(out['status'])
