#!/usr/bin/env python3
"""PREFIX-622: native 96-port exact tomography / missing-current-gate witness.
Frozen original X6-BRC science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python stdlib only: exact rational arithmetic, original 576 typed actions.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json
from pathlib import Path

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i];b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48));G=IX[(0,1,-3)]
H=(3,14,15);RG=2;AXIS=tuple(abs(c)-1 for a,p,c in P)
WEIGHTS=(F(1),)*4+(F(0),)*2
assert len(P)==48 and len(set(P))==48 and G==4 and sum(map(len,N))==144
assert tuple(i for i in range(48) if G in N[i])==H

def native_step(r,z):
    out=[F(0)]*96
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                wt=WEIGHTS[0]*z if (j==G and u==v==1) else WEIGHTS[AXIS[i]]
                out[2*i+u]+=wt*r[2*j+v]
    return out

def encode(r):return [r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]
def embed(v):
    r=[F(0)]*96
    for i in range(48):r[2*i]=v[i];r[2*i+1]=v[i] if i==G else F(0)
    return r

def Qstep(v,z):
    out=[F(0)]*48
    for i in range(48):
        if i==G: out[i]=WEIGHTS[AXIS[i]]*sum((v[j] for j in N[i]),F(0))
        else: out[i]=WEIGHTS[AXIS[i]]*(2*sum((v[j] for j in N[i] if j!=G),F(0))+(z+3)*v[G]*(G in N[i]))
    return out

def decode_ports(v,z=None,delta=None):
    if delta is None:
        assert z is not None and z>=0
        ell=v[3]+v[14]+v[15]-2*v[2]
        delta=F(z-1)*ell/(3*(z+3))
    out=[F(0)]*96
    for i in range(48):
        if i==G:out[2*i]=out[2*i+1]=v[i]
        else:
            e=delta if i in H else F(0)
            out[2*i]=(v[i]-e)/2
            out[2*i+1]=(v[i]+e)/2
    return out

HC=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB=({3:1,14:1,15:1},{17:2,40:2,41:2},{26:4,27:4,39:4},{4:4,5:8,29:8})
S6=(14,3,40,26,27,4)
S8=(3,4,5,14,17,26,27,40)
S14=(2,3,4,5,14,15,17,26,27,29,38,39,40,41)

def row(i,r):return [F(sum(i in HC[j] for j in ((r+2)%4,(r+3)%4)))]+[F(h.get(i,0)) for h in HB]
def solve(A,b):
    A=[list(map(F,a))+[F(y)] for a,y in zip(A,b)];pivs=[];k=0
    for j in range(5):
        p=next((i for i in range(k,len(A)) if A[i][j]),None)
        if p is None:continue
        A[k],A[p]=A[p],A[k];v=A[k][j];A[k]=[x/v for x in A[k]]
        for i in range(len(A)):
            if i!=k and A[i][j]:
                q=A[i][j];A[i]=[a-q*c for a,c in zip(A[i],A[k])]
        pivs.append(j);k+=1
    assert k==5 and all(any(a[:5]) or not a[5] for a in A)
    out=[F(0)]*5
    for i,j in enumerate(pivs):out[j]=A[i][5]
    return out

def sensor_recover(v,S,t):
    z=solve([row(i,t%4) for i in S],[v[i] for i in S]);theta=z[0]
    c=[theta if i in ((t+2)%4,(t+3)%4) else F(0) for i in range(4)]
    out=[F(0)]*48
    for j,inds in enumerate(HC):
        for i in inds:out[i]+=c[j]
    for j,h in enumerate(HB):
        for i,vv in h.items():out[i]+=vv*z[j+1]
    return out

def native_sequence(a,b,q,lam):
    d=[F(0)]*48
    for i in (4,11,14,32):d[i]=lam
    r=embed(d);v=d
    for z in (a,b)+tuple(q):
        r=native_step(r,z);v=Qstep(v,z)
        assert encode(r)==v
    return v,r

# Check no-current-gate 48-phase alias at t=3: a*g3 is compensated.
q=(F(1),F(1))
va,ra=native_sequence(F(1),F(1),q+(F(2),),F(1))
vb,rb=native_sequence(F(2),F(1),q+(F(1),),F(1))
assert va==vb and ra!=rb
La=va[3]+va[14]+va[15]-2*va[2]
assert La>0
DA=ra[2*3+1]-ra[2*3]
DB=rb[2*3+1]-rb[2*3]
assert DA==La/15 and DB==0 and (DA!=DB)
assert decode_ports(va,F(2))==ra and decode_ports(vb,F(1))==rb
assert sum(a!=b for a,b in zip(ra,rb))==6

# Four rational examples, t=0..12, exact comparisons against all 576 native actions.
cases=((F(0),F(0),F(1)),(F(1),F(2),F(3,2)),(F(7,3),F(5,2),F(13,7)),(F(2),F(1),F(7,4)))
portchecks=phasechecks=repaired=recovered=0
for a,b,lam in cases:
    for t in range(13):
        qs=tuple(F((j*j+3*j+5)%11,j%3+1) for j in range(1,t+1))
        v,r=native_sequence(a,b,qs,lam)
        z=qs[-1] if qs else b
        assert decode_ports(v,z)==r
        portchecks+=96
        for S,e in ((S6,0),(S8,1),(S14,2)):
            # test deterministic exhaustive erasure configurations for every t
            for lost in combinations(S,e):
                keep=tuple(i for i in S if i not in lost)
                vv=sensor_recover(v,keep,t)
                assert vv==v
                phasechecks+=48;recovered+=1
                assert decode_ports(vv,z)==r
                portchecks+=96
                h=3
                measured_port=r[2*h+1]
                delta=2*measured_port-vv[h]
                assert decode_ports(vv,delta=delta)==r
                repaired+=1
                ell=vv[3]+vv[14]+vv[15]-2*vv[2]
                assert ell>0 and ell-3*delta>0
                inferred=(ell+9*delta)/(ell-3*delta)
                assert inferred==z

result={
    'schema':'PREFIX622_R2_NATIVE96_SENSOR_AND_GATE_WITNESS_V1',
    'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'original_phases':48,'native_ports':96,'original_typed_actions':576,
    'witness_t':3,'witness_history_A':{'a':'1','b':'1','q':['1','1','2']},
    'witness_history_B':{'a':'2','b':'1','q':['1','1','1']},
    'witness_equal_48_phase_sums':va==vb,
    'witness_48_phase_sums':[str(v) for v in va],
    'witness_L':str(La),'witness_delta_A':str(DA),'witness_delta_B':str(DB),
    'witness_differing_port_coordinates':[i for i in range(96) if ra[i]!=rb[i]],
    'rational_parameter_sequences':len(cases)*13,
    'phase_coordinate_checks':phasechecks,
    'port_coordinate_checks':portchecks,
    'sensor_reconstruction_cases':recovered,
    'one_raw_port_bit_repairs_and_gate_inversions':repaired,
    'review':'AUTHOR_SIDE_UNREVIEWED',
    'result':'ALL_ASSERTIONS_PASS'
}
path=Path(__file__).with_name('PREFIX622_native_port_tomography_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('witness_48_phase_sums',)},ensure_ascii=False))
