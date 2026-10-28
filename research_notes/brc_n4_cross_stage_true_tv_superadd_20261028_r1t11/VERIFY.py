#!/usr/bin/env python3
"""Exact Fraction verification of an N4 dual-law true TV superadditivity witness.
Uses only Python stdlib and CERTIFICATES.txt. Does not need SciPy or GitHub auth.
External finite BRC tree; does not grant P000-native X6 or formal Result status.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

Z, O = F(0), F(1)
N={1:{'A':(F(1,2),F(1,2),None),'B':(F(1,2),F(3,2),None)},
   2:{'AU':(F(1,6),O,'A'),'AV':(F(1,3),F(1,4),'A'),
      'BU':(F(1,4),O,'B'),'BV':(F(1,4),F(2),'B')}}
for t in (3,4):
    N[t]={}
    for pa,(q,r,_) in N[t-1].items():
        eps=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[pa] if t==3
             else Z if pa=='AV0' else F(3,50) if pa=='AV1' else F(1,20))
        for j,sign in enumerate((-1,1)):
            N[t][pa+str(j)]=(q/2,r*(1+sign*eps),pa)
for t,nodes in N.items():
    assert len(nodes)==2**t
    assert all(q>0 and r>0 for q,r,_ in nodes.values())
    assert sum((q for q,r,_ in nodes.values()),Z)==O
    assert sum((q*r for q,r,_ in nodes.values()),Z)==O
    if t<4:
        for h,(q,r,_) in nodes.items():
            ch=[(qc,rc) for c,(qc,rc,p) in N[t+1].items() if p==h]
            assert len(ch)==2
            assert sum((qc for qc,rc in ch),Z)==q
            assert sum((qc*rc for qc,rc in ch),Z)==q*r
groups={t:defaultdict(list) for t in (2,3,4)}
for t in groups:
    for h,(q,r,p) in N[t].items():groups[t][r].append(h)

def baseline(t,h):
    r=N[t][h][1]
    if t==2:
        return {'AU':(O,Z,Z),'AV':(Z,Z,O),'BU':(Z,Z,O),'BV':(O,Z,Z)}[h]
    if t==3:
        if h in ('AV0','AV1','BU0'):return Z,Z,O
        if h=='BU1':return Z,O,Z
        return O,Z,Z
    return (Z,O,Z) if 100*r<F(2501,100) else (O,Z,Z)

full={(t,h):baseline(t,h) for t in (2,3,4) for h in N[t]}
full.update({(2,'AU'):(F(1,2),F(1,6),F(1,3)),
             (2,'BU'):(Z,F(1,2),F(1,2)),
             (3,'AU0'):(Z,O,Z),(3,'AV0'):(Z,F(1,2),F(1,2))})
assert all(sum(p,Z)==O and min(p)>=Z for p in full.values())
def law(actions):
    out=[Z]*16
    for leaf,(q,r,_) in N[4].items():
        alive=O
        for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
            p=(Z,Z,O) if t==1 else actions[t,h]
            assert len(p)==3 and min(p)>=Z and sum(p,Z)==O
            assert t!=4 or p[2]==Z
            j=2*(t-1)
            out[j]+=q*alive*p[0];out[j+1]+=q*alive*p[1]
            out[8+j]+=q*r*alive*p[0];out[8+j+1]+=q*r*alive*p[1]
            alive*=p[2]
        assert alive==Z
    assert sum(out[:8],Z)==sum(out[8:],Z)==O
    return out
T=law(full)
assert T==list(map(F,('0','0','1/3','11/72','1/36','25/144','1/12','11/48',
                      '0','0','7/12','11/72','11/360','19/120','53/2400','127/2400')))
def tv(a,b):
    return (sum((abs(a[i]-b[i]) for i in range(8)),Z)/2,
            sum((abs(a[8+i]-b[8+i]) for i in range(8)),Z)/2)

# Parse the completely explicit sparse rational occupation certificates.
text=Path(__file__).with_name('CERTIFICATES.txt').read_text(encoding='utf-8')
ledger,weights={},{}
scope=None
for raw in text.splitlines():
    line=raw.strip()
    if line in ('[S2]','[S3]','[S23]'):
        scope=line[1:-1];ledger[scope]={}
    elif scope and line.startswith('W='):
        weights[scope]=list(map(F,line[2:].split()))
    elif scope and line and line[0]=='2' or scope and line and line[0]=='3' or scope and line and line[0]=='4':
        for item in line.split(';'):
            key,v=item.split('=')
            head,a=key.split('.')
            t,h=int(head[0]),head[1:]
            assert (t,h,a) not in ledger[scope]
            ledger[scope][t,h,a]=F(v)

def primal(which):
    x={(t,h,a):Z for t in (2,3,4) for h in N[t]
       for a in ('P','Q','C') if t<4 or a!='C'}
    for k,v in ledger[which].items():
        assert k in x and v>0
        x[k]=v
    arrive={}
    for t in (2,3,4):
        for h in N[t]:
            arrive[t,h]=O if t==2 else x[t-1,N[t][h][2],'C']
            assert sum((x[t,h,a] for a in ('P','Q','C') if (t,h,a) in x),Z)==arrive[t,h]
    # All action probabilities on equal (time,LR) fibers are identical
    # where that time is compressed. At t4 use the common LR terminal rule.
    times={'S2':{2,4},'S3':{3,4},'S23':{2,3,4}}[which]
    for t in times:
        for r,hs in groups[t].items():
            for h in hs[1:]:
                for a in ('P','Q','C'):
                    if (t,h,a) not in x:continue
                    base=hs[0]
                    assert x[t,h,a]*arrive[t,base]==x[t,base,a]*arrive[t,h]
    action={}
    for (t,h),s in arrive.items():
        if s==0:
            action[t,h]=(Z,Z,O) if t<4 else (O,Z,Z)
        else:
            action[t,h]=tuple([x[t,h,a]/s for a in ('P','Q')]+
                               ([x[t,h,'C']/s] if t<4 else [Z]))
    v=law(action)
    linear=[Z]*16
    for (t,h,a),val in x.items():
        if a=='C':continue
        q,r,_=N[t][h];j=2*(t-1)+(a=='Q')
        linear[j]+=q*val;linear[8+j]+=q*r*val
    assert v==linear
    return tv(v,T),sum(z>0 for z in x.values())

# Global exact Bellman lower bound. Includes unrestricted t1 STOP/CONTINUE.
# For linear score, each action-simplex variable occurs at most once along
# a path, so multi-affinity proves the minimum is attained at a vertex.
def bellman(w,mode):
    wq,wp=w[:8],w[8:]
    def c(t,r,a):return wq[2*(t-1)+a]+r*wp[2*(t-1)+a]
    next3={}
    for h,(q,r,_) in N[3].items():
        next3[h]=sum((qc/q*min(c(4,rr,0),c(4,rr,1))
                     for leaf,(qc,rr,p) in N[4].items() if p==h),Z)
    best=None;count=0
    for a in product(range(3),repeat=2):
        first=dict(zip(('A','B'),a))
        for b in product(range(3),repeat=3):
            count+=1;second=dict(zip(('U','AV','BV'),b))
            value=Z;reached=[]
            for h,(q,r,_) in N[1].items():
                if first[h]!=2:value+=q*c(1,r,first[h])
            for h,(q,r,parent) in N[2].items():
                if first[parent]!=2:continue
                choice=second['U' if h in ('AU','BU') else h]
                if choice!=2:value+=q*c(2,r,choice)
                else:
                    reached.extend((q3,r3,h3) for h3,(q3,r3,p) in N[3].items() if p==h)
            if mode=='S2':
                for q,r,h in reached:
                    value+=q*min(c(3,r,0),c(3,r,1),next3[h])
            else:
                buckets=defaultdict(list)
                for q,r,h in reached:buckets[r].append((q,h))
                for r,items in buckets.items():
                    value+=min(sum((q*c(3,r,0) for q,h in items),Z),
                               sum((q*c(3,r,1) for q,h in items),Z),
                               sum((q*next3[h] for q,h in items),Z))
            if best is None or value<best:best=value
    assert count==243
    return best

expected={'S2':F(1,3036),'S3':Z,'S23':F(1037,1884240)}
checks={}
for name in ('S2','S3','S23'):
    d,n=primal(name)
    assert d==(expected[name],expected[name])
    checks[name]={'TV_Q':str(d[0]),'TV_P':str(d[1]),'nonzero_occupancies':n}
for name,least,score in [('S2',-F(153,506),-F(919,3036)),
                         ('S23',-F(7913,26170),-F(570773,1884240))]:
    w=weights[name]
    assert len(w)==16 and max(w[:8])-min(w[:8])+max(w[8:])-min(w[8:])==O
    assert bellman(w,name)==least
    assert sum((a*b for a,b in zip(w,T)),Z)==score
    assert least-score==expected[name]
    checks[name]['all_randomization_bellman_min']=str(least)
gap=expected['S23']-expected['S2']-expected['S3']
assert gap==F(105341,476712720)>0

# Genuine change at t2 AU: STOP P up, CONTINUE down, preserving positive mass.
eps=F(1,10000)
actions=dict(full)
actions[2,'AU']=(F(1,2)+eps,F(1,6),F(1,3)-eps)
assert tv(law(actions),T)==(eps/6,eps/6)
# Distance to any nonempty set is 1-Lipschitz under max two-law TV:
# G(F_eps) >= G(F)-3*(eps/6)>0 for the entire epsilon interval.
floor=gap-eps/2
assert floor==F(20376341,119178180000)>0
print(json.dumps({
 'status':'PASS_EXACT_FRACTION_N4_TRUE_TV_SUPERADDITIVITY',
 'scope':'finite positive two-law N4 tree, full (T,D) 16-cell observer',
 'd2':str(expected['S2']),'d3':str(expected['S3']),
 'd23':str(expected['S23']),'strict_gap':str(gap),
 'Q_target':[str(x) for x in T[:8]],'P_target':[str(x) for x in T[8:]],
 'checks':checks,'t2_perturbation_max':str(eps),
 'robust_superadditivity_lower':str(floor),
 'review':'AUTHOR_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED',
},ensure_ascii=False,indent=2,sort_keys=True))
