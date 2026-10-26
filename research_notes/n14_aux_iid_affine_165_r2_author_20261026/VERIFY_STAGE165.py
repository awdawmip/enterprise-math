#!/usr/bin/env python3
"""Stage165 finite-N ternary iid exact author verifier.

Checks rational Bellman lower bound, two tie-cone affine observer map and
primal interval using a count-state suffix recurrence plus literal ordered
prefix integer DFS. External auxiliary model only; no native P000 transfer.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json
N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(13623672285,49693891)
L=F(40009085000,149081673)
R=(10,0,1)
Y=(10,7,3)
ACTS='PQC'
TIES={R:('Q','C'),Y:('P','C')}
fmt=lambda v: str(v.numerator)+('/'+str(v.denominator) if v.denominator!=1 else '')

def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return (s[0]+1,s[1]+(i==0),s[2]+(i==1))
@lru_cache(None)
def bell(s):
    opts=[K*ratio(s),L]
    if s[0]<N: opts.append(F(1)+sum(P[i]*bell(child(s,i))[0] for i in range(3)))
    return min(opts),tuple(opts)
strict={};ties={};gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=n,a,b;m,opts=bell(s)
            win=tuple(ACTS[i] for i,c in enumerate(opts) if c==m)
            if len(win)>1: ties[s]=win
            else:strict[s]=win[0]
            gaps.extend(c-m for c in opts if c>m)
assert len(strict)+len(ties)==680
assert ties==TIES, ('unexpected tie set',ties)
assert len(gaps)==1238 and min(gaps)==F(8257109179793,821825520500736)
# r=Pr[Q-at-R], y=Pr[P-at-Y]
def act(s,r,y):
    if s==R:return 'Q' if r else 'C'
    if s==Y:return 'P' if y else 'C'
    return strict[s]

def suffix(r,y):
    @lru_cache(None)
    def rec(s):
        z=act(s,r,y)
        if z=='P':return F(0),F(1),F(0),F(0)
        if z=='Q':return F(1),F(0),F(0),F(0)
        vals=[rec(child(s,i)) for i in range(3)]
        return (sum(P[i]*vals[i][0] for i in range(3)),
                sum(Q[i]*vals[i][1] for i in range(3)),
                1+sum(P[i]*vals[i][2] for i in range(3)),
                1+sum(Q[i]*vals[i][3] for i in range(3)))
    return rec((0,0,0))

def ordered_dfs(r,y):
    pn=(3,1,20);qn=(1,1,10)
    acc=defaultdict(int);hits={R:[0,F(0),F(0)],Y:[0,F(0),F(0)]}
    nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;s=n,a,b
        if s in hits:
            h=hits[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
        z=act(s,r,y)
        if z=='C':
            for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q
            acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if z=='P':acc[n,'eq']+=q
            else:acc[n,'ep']+=p
    walk(0,0,0,1,1)
    tot=lambda kind,b:sum((F(acc[n,kind],b**n) for n in range(N+1)),F(0))
    assert tot('ap',24)==tot('aq',12)==1
    return (tot('ep',24),tot('eq',12),tot('tp',24),tot('tq',12)),hits,nodes

corners={};nodes={};hits_ref=None
for r in (0,1):
    for y in (0,1):
        d=suffix(r,y)
        e,h,n=ordered_dfs(r,y)
        assert d==e,(r,y,d,e)
        corners[r,y]=e
        nodes[f'{r}{y}']=n
        if hits_ref is None:hits_ref=h
        else:assert h==hits_ref
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0]
dR=sub(corners[1,0],base)
dY=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dY)
assert mixed==(F(0),)*4
assert Y[0]==R[0] and Y[1]!=R[1]
assert hits_ref[R][0]>0 and hits_ref[Y][0]>0
D=lambda z:z[0]-z[1]
D0,Dr,Dy=map(D,(base,dR,dY))
assert Dr!=0
r0=-D0/Dr;rslope=-Dy/Dr
vec=lambda y:tuple(base[i]+(r0+rslope*y)*dR[i]+y*dY[i] for i in range(4))
ALPHA164=F(62947091618416625195,180720939287325966336)
V164=F(2138584004831606037541,180720939287325966336)
R164=F(257914391728953,844544000000000)
left=vec(F(0))
assert r0==R164,('R coin inherited Stage163',r0,R164)
assert left[0]==left[1]==ALPHA164 and left[2]==V164,('Stage163 left anchor',left)
interval=[F(0),F(1)]
if rslope>0: interval=[max(interval[0],-r0/rslope),min(interval[1],(1-r0)/rslope)]
elif rslope<0: interval=[max(interval[0],(1-r0)/rslope),min(interval[1],-r0/rslope)]
a,b=interval
assert a==0 and b>0
alpha_deriv=(vec(F(1))[0]-left[0])
assert alpha_deriv!=0
right_point=b if alpha_deriv>0 else a
assert right_point>0,('no increasing error in y',rslope,alpha_deriv)
right=vec(right_point)
assert right[0]==right[1]>left[0] and right[2]<left[2]
H=bell((0,0,0))[0]
for pt in (left,right):
    assert pt[2]>pt[3],('P-time not dominant',pt)
    assert pt[2]+K*pt[1]+L*pt[0]==H,('dual equality',pt)
assert right[2]-left[2]==-(K+L)*(right[0]-left[0])
certificate={
    'status':'AUTHOR_EXACT_NOT_ADMITTED_STAGE165',
    'model':{'N':14,'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6'],'scope':'EXTERNAL_N14_IID_FULL_ORDERED_HISTORY'},
    'upstream':{'stage164_source_commit':'c085c64c14515b4d2fc3cbfb33751d4e1171530c','stage164_certificate':'certificate165.json'},
    'dual':{'K':fmt(K),'L':fmt(L),'H':fmt(H),'states':680,'ties':{str(k):list(v) for k,v in ties.items()},'strict_gaps':len(gaps),'min_strict_gap':fmt(min(gaps))},
    'first_hits':{str(s):{'count':h[0],'P_mass':fmt(h[1]),'Q_mass':fmt(h[2])} for s,h in hits_ref.items()},
    'dfs_nodes':nodes,
    'corners':{f'{r}{y}':[fmt(v) for v in corners[r,y]] for (r,y) in corners},
    'M00':[fmt(v) for v in base],
    'dR':[fmt(v) for v in dR],
    'dY':[fmt(v) for v in dY],
    'mixed':[fmt(v) for v in mixed],
    'error_balance':{'D0':fmt(D0),'Dr':fmt(Dr),'Dy':fmt(Dy),'r0':fmt(r0),'r_slope':fmt(rslope),'y_endpoint':fmt(right_point),'r_endpoint':fmt(r0+rslope*right_point),'alpha_derivative':fmt(alpha_deriv)},
    'left':{'alpha':fmt(left[0]),'V':fmt(left[2]),'time_gap':fmt(left[2]-left[3])},
    'right':{'alpha':fmt(right[0]),'V':fmt(right[2]),'time_gap':fmt(right[2]-right[3])},
    'width':fmt(right[0]-left[0]),'slope':fmt(K+L),
    'scope':'Stage165 author exact finite N14 external model. No native P000/X6 transfer, independent Driver review, or formal Source acceptance.'
}
for k,v in certificate.items():
    if k in {'corners','first_hits'}:continue
    print(k,v)
if __name__=='__main__':
    p=Path(__file__).with_name('certificate164.json')
    p.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS Stage165 full real interval; certificate:',p)
