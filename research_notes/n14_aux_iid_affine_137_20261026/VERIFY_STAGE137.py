#!/usr/bin/env python3
"""Stage137 exact Bellman+4-observer finite-N author verifier; Python 3 stdlib only."""
from fractions import Fraction as F
from pathlib import Path
import json

P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
N=14; K=F(214326,401); L=F(203912,401)
B=(11,0,1); G=(13,6,4)
alpha136=F(12235904656867465565,35205614928358539264)
V136=F(72642934423754220803,5867602488059756544)
w136=F(3409636967625767,7403520000000000)

def states(n):
    for a in range(n+1):
        for b in range(n-a+1):
            yield (n,a,b)

def children(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

H={}; moves={}; gaps=[]; ties=[]
for n in range(N,-1,-1):
    for s in states(n):
        n,a,b=s
        r=F(2**(a+b),3**a)
        cost={'P':K*r,'Q':L}
        if n<N:
            cost['C']=1+sum((P[i]*H[t] for i,t in enumerate(children(s))),F(0))
        minimum=min(cost.values())
        H[s]=minimum
        moves[s]=tuple(x for x,c in cost.items() if c==minimum)
        if len(moves[s])>1:ties.append((s,moves[s]))
        gaps.extend(c-minimum for c in cost.values() if c>minimum)
assert len(H)==680 and len(gaps)==1238
assert set(ties)=={(B,('Q','C')),(G,('Q','C'))}
assert min(gaps)==F(1,173232)
assert H[(0,0,0)]==F(2744968460634070393271,7322329660929343488)

def moment(w,z):
    out={}
    for n in range(N,-1,-1):
        for s in states(n):
            a=moves[s][0] if len(moves[s])==1 else (('Q' if w else 'C') if s==B else ('C' if z else 'Q'))
            if a=='P':out[s]=(F(0),F(1),F(0),F(0))
            elif a=='Q':out[s]=(F(1),F(0),F(0),F(0))
            else:
                child=[out[t] for t in children(s)]
                out[s]=(
                    sum((P[i]*child[i][0] for i in range(3)),F(0)),
                    sum((Q[i]*child[i][1] for i in range(3)),F(0)),
                    1+sum((P[i]*child[i][2] for i in range(3)),F(0)),
                    1+sum((Q[i]*child[i][3] for i in range(3)),F(0)))
    return out[(0,0,0)]

M00=moment(0,0); M10=moment(1,0)
M01=moment(0,1); M11=moment(1,1)
dB=tuple(x-y for x,y in zip(M10,M00))
dG=tuple(x-y for x,y in zip(M01,M00))
assert M11==tuple(M00[i]+dB[i]+dG[i] for i in range(4))
c=M00[0]-M00[1]
dw=dB[0]-dB[1]
dz=dG[0]-dG[1]
w0=-c/dw
wz=-dz/dw
a0=M00[0]+w0*dB[0]
eta=dG[0]+wz*dB[0]
v0=M00[2]+w0*dB[2]
dv=dG[2]+wz*dB[2]
q0=M00[3]+w0*dB[3]
dq=dG[3]+wz*dB[3]
assert a0==alpha136 and v0==V136 and w0==w136
assert w0==F(3409636967625767,7403520000000000)
assert wz==F(186571,46272000000)
assert F(0)<w0<w0+wz<F(1)
assert eta==F(121452875,412565799941701632)
assert a0+eta==F(36707714001694332695,105616844785075617792)
assert v0+dv==F(653786393599537203227,52808422392537808896)
assert dv==-(K+L)*eta
assert v0>q0 and v0+dv>q0+dq
assert H[(0,0,0)]==v0+(K+L)*a0

def fmt(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [fmt(y) for y in x]
    return x

cert={
'schema':'EM_N14_STAGE137_AUTHOR_EXACT_CERT_V1',
'model':{'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6'],'N':14},
'K':str(K),'L':str(L),'states':len(H),'strict_gaps':len(gaps),
'min_positive_gap':str(min(gaps)), 'root':str(H[(0,0,0)]),
'ties':[{'state':list(s),'actions':list(a)} for s,a in ties],
'M00':fmt(M00),'dB':fmt(dB),'dG':fmt(dG),'M11':fmt(M11),
'w0':str(w0),'wz':str(wz),'w1':str(w0+wz),
'alpha136':str(a0),'eta137':str(eta),'alpha137':str(a0+eta),
'V136':str(v0),'time_slope':str(dv),'V137':str(v0+dv),
'time_gap0':str(v0-q0),'time_gap1':str(v0+dv-q0-dq),
'sharpness_argument':'Strict-dual-gaps, tie-mass-averaging, disjoint cones; positive eta and z<=1.'
}
target=Path(__file__).with_name('certificate137.json')
target.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS_STAGE137_MAIN',len(H),'states',len(gaps),'strict_gaps')
print('exact_alpha137',a0+eta,'exact_V137',v0+dv,'eta',eta)
