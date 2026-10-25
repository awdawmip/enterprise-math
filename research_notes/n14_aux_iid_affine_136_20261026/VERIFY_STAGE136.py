#!/usr/bin/env python3
"""Stage136 author-side exact Bellman and observer checker (finite ternary iid N14)."""
from fractions import Fraction as F
from functools import lru_cache
import json
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
N=14
K=F(840571992,1526537)
L=F(797676584,1526537)
B=(11,0,1)
D=(10,6,2)
A=(7,3,0)
alpha135=F(12235904537797579565,35205614928358539264)
V135=F(72642955720985708803,5867602488059756544)

def states(n):
    for a in range(n+1):
        for b in range(n-a+1):
            yield (n,a,b)

def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

def ratio(s):
    n,a,b=s
    return F(2**(a+b),3**a)

H={}
actions={}
strict_gaps=[]
tie_details=[]
for n in range(N,-1,-1):
    for s in states(n):
        z={'P':K*ratio(s),'Q':L}
        if n<N:
            z['C']=1+sum((P[i]*H[c] for i,c in enumerate(children(s))),F(0))
        v=min(z.values());H[s]=v
        ties=tuple(k for k,q in z.items() if q==v)
        actions[s]=ties
        if len(ties)>1:
            tie_details.append((s,ties))
        for k,q in z.items():
            if q>v:strict_gaps.append(q-v)
        if not all(q>=v for q in z.values()):raise Exception('bad min')

assert len(H)==680,len(H)
assert len(strict_gaps)==1238,len(strict_gaps)
assert set((s,t) for s,t in tie_details)=={(B,('Q','C')),(D,('P','C'))},tie_details

def policy_action(s,w,u):
    ts=actions[s]
    if len(ts)==1:return ts[0]
    if s==B:
        assert ts==('Q','C')
        return 'Q' if w else 'C'
    if s==D:
        assert ts==('P','C')
        return 'P' if u else 'C'
    raise RuntimeError((s,ts))

def moment(w,u):
    obs={}
    for n in range(N,-1,-1):
        for s in states(n):
            act=policy_action(s,w,u)
            if act=='P': obs[s]=(F(0),F(1),F(0),F(0))
            elif act=='Q':obs[s]=(F(1),F(0),F(0),F(0))
            else:
                cc=[obs[c] for c in children(s)]
                obs[s]=(
                  sum((P[i]*cc[i][0] for i in range(3)),F(0)),
                  sum((Q[i]*cc[i][1] for i in range(3)),F(0)),
                  1+sum((P[i]*cc[i][2] for i in range(3)),F(0)),
                  1+sum((Q[i]*cc[i][3] for i in range(3)),F(0)),
                )
    return obs[(0,0,0)]

M00=moment(0,0); M10=moment(1,0); M01=moment(0,1); M11=moment(1,1)
dB=tuple(x-y for x,y in zip(M10,M00))
dD=tuple(x-y for x,y in zip(M01,M00))
assert M11==tuple(M00[i]+dB[i]+dD[i] for i in range(4))
c=M00[0]-M00[1]; dw=dB[0]-dB[1]; du=dD[0]-dD[1]
w0=-c/dw
wslope=-du/dw
alpha0=M00[0]+w0*dB[0]
eta=dD[0]+wslope*dB[0]
v0=M00[2]+w0*dB[2]
vslope=dD[2]+wslope*dB[2]
qt0=M00[3]+w0*dB[3]
qtslope=dD[3]+wslope*dB[3]
print('check_bellman',len(H),len(strict_gaps),'min_strict_gap',str(min(strict_gaps)))
print('root',H[(0,0,0)],'ties',tie_details)
for name,obj in [('M00',M00),('dB',dB),('dD',dD),('w0',w0),('wslope',wslope),('alpha0',alpha0),('eta',eta),('v0',v0),('vslope',vslope),('tQ0',qt0),('tQslope',qtslope)]:print(name, obj)
print('endpoint w0,w1',w0,w0+wslope)
print('end_time_gap',v0-qt0,v0+vslope-qt0-qtslope)
print('V136',v0+vslope,'alpha136',alpha0+eta)
print('left-match',alpha0==alpha135,v0==V135)
print('slope-match',vslope==-eta*(K+L))
print('dual-match',H[(0,0,0)]==v0+(K+L)*alpha0)

assert F(0)<=w0<=1 and F(0)<=w0+wslope<=1
assert eta>0
assert v0>qt0 and v0+vslope>qt0+qtslope
assert alpha0==alpha135 and v0==V135
assert vslope==-eta*(K+L)
assert H[(0,0,0)]==v0+(K+L)*alpha0

def serialize(v):
    if isinstance(v,F):return f'{v.numerator}/{v.denominator}'
    if isinstance(v,(list,tuple)):return [serialize(x) for x in v]
    if isinstance(v,dict):return {str(k):serialize(x) for k,x in v.items()}
    return v
certificate={
 'schema':'EM_N14_STAGE136_AUTHOR_EXACT_CERT_V1','model':{'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6'],'N':14},
 'K':serialize(K),'L':serialize(L),'states':len(H),'strict_gaps':len(strict_gaps),'min_strict_gap':serialize(min(strict_gaps)),
 'ties':[{'state':list(s),'actions':list(t)} for s,t in tie_details], 'dual_root':serialize(H[(0,0,0)]),
 'M00':serialize(M00),'dB':serialize(dB),'dD':serialize(dD),'M11':serialize(M11),
 'w0':serialize(w0),'wslope':serialize(wslope),'alpha0':serialize(alpha0),'eta':serialize(eta),
 'alpha136':serialize(alpha0+eta),'V136':serialize(v0+vslope),
 'V0':serialize(v0),'time_slope':serialize(vslope),'tQ0':serialize(qt0),'tQslope':serialize(qtslope),
 'left_anchor_matched':True,'dual_bound_attained':True,'endpoint_saturates_D':True
}
with open('certificate136.json','w') as f:json.dump(certificate,f,indent=2,ensure_ascii=False)
print('PASS_STAGE136_MAIN')
