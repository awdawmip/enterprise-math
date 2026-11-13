#!/usr/bin/env python3
"""PREFIX-625: sharp fixed 3-sensor two-frame tomography of original X6-BRC.
Source pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Fraction-exact tests, SymPy-exact rank certificate, native STAR source.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random
from pathlib import Path
from sympy import Matrix
import json

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
PH=tuple((a,p,s*c) for a in range(4) for c in STAR[a] for s in (-1,1) for p in near(a,s*c))
I={p:i for i,p in enumerate(PH)}
def succ(i):
    a,p,c=PH[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
    return [I[x] for x in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
E=[(i,j) for i in range(48) if abs(PH[i][2]) not in (5,6) for j in succ(i)]
assert len(PH)==48 and len(E)==96 and I[(0,1,-3)]==4

HC=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB=({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})
S=(3,4,17)

def Qstep(x,g):
    y=[F(0)]*48
    for i,j in E:
        y[i]+=(F(1) if i==4 else (g+3 if j==4 else F(2)))*x[j]
    return y

def lift(t,theta,w):
    c=[theta if i in ((t+2)%4,(t+3)%4) else F(0) for i in range(4)]
    y=[F(0)]*48
    for j,inds in enumerate(HC):
        for i in inds:y[i]+=c[j]
    for j,col in enumerate(HB):
        for i,val in col.items():y[i]+=val*w[j]
    return y

def update_w(w,g):
    return [4*(g+3)*w[3],w[0],w[1],w[2]]

def sensors(y):
    return (y[3],y[4],y[17])

def invert_pair(t,cur,nxt):
    a,b,c=cur;A,B,C=nxt
    r=t%4;w3=b/4;w2=B/4
    assert w3>0
    if r==0:
        w0=a;theta=(C-2*w0)/2;w1=(c-theta)/2
        q=(A-2*theta)/(4*w3)-3
    elif r==1:
        w0=C/2;theta=a-w0;w1=(c-theta)/2
        q=(A-2*theta)/(4*w3)-3
    elif r==2:
        w0=C/2;theta=a-w0;w1=c/2
        q=A/(4*w3)-3
    else:
        w0=a;theta=(C-2*w0)/2;w1=c/2
        q=A/(4*w3)-3
    assert theta>0 and all(x>0 for x in (w0,w1,w2,w3)) and q>=0
    w=[w0,w1,w2,w3]
    return theta,w,q,lift(t,theta,w),lift(t+1,2*theta,update_w(w,q))

# Exact affine original native kernel/intertwiner basis certificate.
for g in (F(0),F(1)):
    for j in range(5):
        theta=F(j==0)
        w=[F(k==j-1) for k in range(4)]
        for t in range(4):
            assert Qstep(lift(t,theta,w),g)==lift(t+1,2*theta,update_w(w,g))

rng=Random(625)
choices=(F(0),F(1),F(3,2),F(2),F(7,3),F(11,7),F(5))
checks=0;phase_checks=0;gate_checks=0
for trial in range(120):
    a=rng.choice(choices)
    b=rng.choice(choices)
    lam=F(rng.randrange(1,8),rng.randrange(1,6))
    n=rng.randrange(2,33)
    word=[rng.choice(choices) for _ in range(n+1)]
    d=[F(0)]*48
    for i in (4,11,14,32):d[i]=lam
    y=Qstep(Qstep(d,a),b)
    theta=4*lam
    w=[lam*(b+3),lam*(a+3),lam,lam/2]
    for t in range(n+1):
        assert y==lift(t,theta,w)
        if t<n:
            ynext=Qstep(y,word[t])
            rec_theta,rec_w,rec_gate,x0,x1=invert_pair(t,sensors(y),sensors(ynext))
            assert rec_theta==theta and rec_w==w and rec_gate==word[t]
            assert x0==y and x1==ynext
            checks+=1;phase_checks+=96;gate_checks+=1
            y=ynext;theta*=2;w=update_w(w,word[t])

# Six-dimensional time-pair differential rank certificate.
def ccoef(i,r):
    return sum(i in HC[k] for k in ((r+2)%4,(r+3)%4))
def rowcur(i,r):
    return (ccoef(i,r),)+tuple(col.get(i,0) for col in HB)+(0,)
def rownext(i,r):
    b=[col.get(i,0) for col in HB]
    # Exact derivative at next gate q=1 and sensitive coordinate w3=1.
    return (2*ccoef(i,(r+1)%4),b[1],b[2],b[3],16*b[0],4*b[0])
ranks=[];dets=[]
for r in range(4):
    M=Matrix([rowcur(i,r) for i in S]+[rownext(i,r) for i in S])
    ranks.append(M.rank());dets.append(int(M.det()))
assert ranks==[6]*4 and all(d!=0 for d in dets)

support=sorted(set(i for inds in HC for i in inds)|set(i for col in HB for i in col))
valid=0
for cand in combinations(support,3):
    if all(Matrix([rowcur(i,r) for i in cand]+[rownext(i,r) for i in cand]).rank()==6 for r in range(4)):
        valid+=1
assert len(support)==16 and valid==24

result={
    'schema':'PREFIX625_THREE_FIXED_NATIVE_PHASE_TEMPORAL_SENSORS_V1',
    'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'fixed_sensors':list(S),
    'two_consecutive_frames':True,
    'exact_two_frame_jacobian_ranks':ranks,
    'exact_two_frame_determinants':dets,
    'all_five_dimensional_state_and_one_gate_recovered':True,
    'minimum_fixed_sensor_count':3,
    'two_sensor_lower_bound':'fixed_next_gate: 4 samples cannot injectively recover 5-dimensional open reachable state by linear-rank nullity',
    'valid_triples_among_16_active_phase_positions':valid,
    'trial_count':120,'checked_pairs':checks,
    'checked_phase_coordinates':phase_checks,
    'checked_gate_inversions':gate_checks,
    'native_kernel_basis_affine_cases':40,
    'result':'ALL_ASSERTIONS_PASS',
    'review':'AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX625_three_temporal_sensors_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
