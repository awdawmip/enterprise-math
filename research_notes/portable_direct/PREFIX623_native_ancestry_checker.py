#!/usr/bin/env python3
"""PREFIX-623: native 96-port typed-path ancestry fiber and sharp one-scalar repair.
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


# PREFIX-623: full original typed 576-action ancestry flow, no new transport model.
# The two full six-step histories share exactly the same original input E(d).
a=(F(1),F(1),(F(1),F(1),F(2),F(1)))
b=(F(2),F(1),(F(1),F(1),F(1),F(1)))
def native_trace(a,b,q):
    d=[F(0)]*48
    for k in (4,11,14,32):d[k]=F(1)
    r=embed(d);states=[r]
    for gate in (a,b)+tuple(q):
        r=native_step(r,gate);states.append(r)
    return states
ta=native_trace(*a)
tb=native_trace(*b)
assert len(ta)==len(tb)==7
pA,pB=ta[5],tb[5]
terminalA,terminalB=ta[6],tb[6]
assert encode(pA)==encode(pB) and pA!=pB
assert terminalA==terminalB and encode(terminalA)==encode(terminalB)
h=[F(0)]*96
for j in H:
    h[2*j]=F(-1)
    h[2*j+1]=F(1)
assert [u-v for u,v in zip(pA,pB)]==[8*k for k in h]
# Native A(g) is affine in g. A(0)h=A(1)h=0 proves all g.
assert native_step(h,F(0))==[F(0)]*96
assert native_step(h,F(1))==[F(0)]*96
assert all(native_step(h,g)==[F(0)]*96 for g in (F(2),F(7,3)))
assert all(native_step(terminalA,g)==native_step(terminalB,g) for g in (F(0),F(1),F(2),F(7,3)))

# Preserve the typed action labels BEFORE destination summation.
def actions(s):
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                w=WEIGHTS[0]*s if j==G and u==v==1 else WEIGHTS[AXIS[i]]
                yield (2*i+u,2*j+v,w,(i,j,u,v))
listA=[w*pA[src] for dest,src,w,label in actions(F(1))]
listB=[w*pB[src] for dest,src,w,label in actions(F(1))]
assert len(listA)==len(listB)==576
typed_difference_count=sum(x!=y for x,y in zip(listA,listB))
assert typed_difference_count==12

source=29  # phase 14, bit 1; a positive source under six native actions.
outgoing=[(dest,w) for dest,src,w,label in actions(F(1)) if src==source and w]
assert len(outgoing)==6 and all(w==1 for dest,w in outgoing)
assert (pA[source],pB[source])==(F(48),F(40))
flowA=sum((w*pA[source] for dest,w in outgoing),F(0))
flowB=sum((w*pB[source] for dest,w in outgoing),F(0))
assert (flowA,flowB)==(F(288),F(240))
tagA=[F(0)]*96;tagB=[F(0)]*96
for dest,w in outgoing:
    tagA[dest]+=w*pA[source]
    tagB[dest]+=w*pB[source]
assert sorted(j for j in range(96) if tagA[j]!=tagB[j])==[34,35,80,81,82,83]
assert sum(tagA)==flowA and sum(tagB)==flowB

# All 576 source-labelled flows are reconstructed from predecessor phase v
# plus one bit-imbalance delta, at a known subsequent gate.
v=encode(pA)
deltaA=pA[29]-pA[28]
deltaB=pB[29]-pB[28]
assert deltaA==16 and deltaB==0
def decoder(v,delta):
    ans=[F(0)]*96
    for i in range(48):
        if i==G:
            ans[2*i]=ans[2*i+1]=v[i]
        else:
            e=delta if i in H else F(0)
            ans[2*i]=(v[i]-e)/2
            ans[2*i+1]=(v[i]+e)/2
    return ans
assert decoder(v,deltaA)==pA
assert decoder(v,deltaB)==pB
for r,actions_expected in ((decoder(v,deltaA),listA),(decoder(v,deltaB),listB)):
    assert [w*r[src] for dest,src,w,label in actions(F(1))]==actions_expected
    recomposed=[F(0)]*96
    for dest,src,w,label in actions(F(1)):
        recomposed[dest]+=w*r[src]
    assert recomposed==terminalA==terminalB

result={
  "schema":"PREFIX623_NATIVE96_TAGGED_ANCESTRY_FIBER_V1",
  "date":"2026-11-09",
  "frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
  "phase_count":48,"port_count":96,"labelled_action_count":576,
  "history_A_gates":list(map(str,(a[0],a[1])+a[2])),
  "history_B_gates":list(map(str,(b[0],b[1])+b[2])),
  "preceding_phase_equal":encode(pA)==encode(pB),
  "preceding_port_equal":pA==pB,
  "terminal_port_equal":terminalA==terminalB,
  "universal_kernel_h_nonzero_count":sum(k!=0 for k in h),
  "universal_kernel_verified_affine_endpoints":["0","1"],
  "preceding_source_port":source,
  "preceding_source_masses":[str(pA[source]),str(pB[source])],
  "positive_outgoing_label_count_from_source":len(outgoing),
  "source_tagged_flow_total_masses":[str(flowA),str(flowB)],
  "different_labelled_action_coordinates":typed_difference_count,
  "tagged_terminal_port_difference_coordinates":[j for j in range(96) if tagA[j]!=tagB[j]],
  "tagged_terminal_port_difference_values":{str(j):[str(tagA[j]),str(tagB[j])] for j in range(96) if tagA[j]!=tagB[j]},
  "delta_repair_values":[str(deltaA),str(deltaB)],
  "full_576_labelled_actions_recovered_from_one_scalar":True,
  "one_scalar_lower_bound_witness":True,
  "shared_future_gates_tested":["0","1","2","7/3"],
  "full_terminal_ports":[str(z) for z in terminalA],
  "review":"AUTHOR_SIDE_UNREVIEWED",
  "result":"ALL_ASSERTIONS_PASS"
}
Path(__file__).with_name("PREFIX623_native_ancestry_results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\\n")
print(json.dumps({k:v for k,v in result.items() if k not in ("full_terminal_ports","tagged_terminal_port_difference_values")},ensure_ascii=False))
