#!/usr/bin/env python3
"""PREFIX-624: native 96-port reconstruction from two consecutive 48-phase frames.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact stdlib Fraction computation; original 576 typed actions.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48))
G=IX[(0,1,-3)]
H=(3,14,15)
AXIS=tuple(abs(c)-1 for a,p,c in P)
W=(F(1),)*4+(F(0),)*2
assert len(P)==48 and len(set(P))==48 and G==4 and sum(map(len,N))==144
assert tuple(i for i in range(48) if G in N[i])==H

def native_step(r,z):
    out=[F(0)]*96
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                wt=z if j==G and u==v==1 else W[AXIS[i]]
                out[2*i+u]+=wt*r[2*j+v]
    return out

def encode(r):
    return [r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]

def embed(v):
    r=[F(0)]*96
    for i in range(48):
        r[2*i]=v[i]
        if i==G:r[2*i+1]=v[i]
    return r

def Qstep(v,z):
    out=[F(0)]*48
    for i in range(48):
        if i==G:
            out[i]=W[AXIS[i]]*sum((v[j] for j in N[i]),F(0))
        else:
            out[i]=W[AXIS[i]]*(
                2*sum((v[j] for j in N[i] if j!=G),F(0))
                +(z+3)*v[G]*(G in N[i]))
    return out

def ell(v):
    return v[3]+v[14]+v[15]-2*v[2]

def infer_gate(prev,cur):
    assert prev[G]>0
    z=ell(cur)/(3*prev[G])-3
    assert z>=0
    return z

def infer_ports(prev,cur):
    delta=ell(cur)/3-4*prev[G]
    out=[F(0)]*96
    for i in range(48):
        if i==G:
            out[2*i]=out[2*i+1]=cur[i]
        else:
            e=delta if i in H else F(0)
            out[2*i]=(cur[i]-e)/2
            out[2*i+1]=(cur[i]+e)/2
    assert all(x>=0 for x in out)
    return out

def all_actions(z):
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                wt=z if j==G and u==v==1 else W[AXIS[i]]
                yield (2*i+u,2*j+v,wt,(i,j,u,v))

def action_tensor(state,z):
    return [wt*state[src] for dst,src,wt,label in all_actions(z)]

def summed_actions(state,z):
    out=[F(0)]*96
    for dst,src,wt,label in all_actions(z):
        out[dst]+=wt*state[src]
    return out

# Exact 48-basis certificate for each of z=0,1; Q(z) is affine in z.
for z in (F(0),F(1)):
    coeff=[]
    for j in range(48):
        e=[F(0)]*48;e[j]=F(1)
        coeff.append(ell(Qstep(e,z)))
    assert coeff==[F(3*(z+3)) if j==G else F(0) for j in range(48)]

# Native Q(0) support certificate for all lengths modulo four.
paths=((4,), (11,4), (32,26,4), (14,40,26,4), (4,14,40,26,4))
for p in paths:
    for src,dst in zip(p,p[1:]):
        e=[F(0)]*48;e[src]=F(1)
        assert Qstep(e,F(0))[dst]>0

rng=Random(624)
all_gate_sets=[[],[F(0)]*18,[F(1)]*18,[F(2),F(0),F(3,7),F(1,2),F(5,3)]*4]
choices=(F(0),F(1),F(2),F(5,3),F(7,4),F(11,5))
for _ in range(120):
    all_gate_sets.append([rng.choice(choices) for _ in range(rng.randrange(1,29))])

frame_checks=0; action_checks=0; gate_checks=0
for gates in all_gate_sets:
    d=[F(0)]*48
    for i in (4,11,14,32):d[i]=F(1)
    v=d;r=embed(v)
    for z in gates:
        nxt=Qstep(v,z)
        nxt_r=native_step(r,z)
        assert nxt==encode(nxt_r)
        assert infer_gate(v,nxt)==z
        assert infer_ports(v,nxt)==nxt_r
        assert summed_actions(r,z)==nxt_r
        assert action_tensor(r,infer_gate(v,nxt))==action_tensor(r,z)
        frame_checks+=96;gate_checks+=1;action_checks+=576
        v,r=nxt,nxt_r

history_A=(F(1),F(1),F(1),F(1),F(2))
history_B=(F(2),F(1),F(1),F(1),F(1))
def native_history(h):
    d=[F(0)]*48
    for i in (4,11,14,32):d[i]=F(1)
    v=d;r=embed(v);seq=[(v,r)]
    for z in h:
        v=Qstep(v,z);r=native_step(r,z);seq.append((v,r))
    return seq
hist_a=native_history(history_A)
hist_b=native_history(history_B)
assert hist_a[5][0]==hist_b[5][0] and hist_a[5][1]!=hist_b[5][1]
assert hist_a[4][0]!=hist_b[4][0]
assert infer_ports(hist_a[4][0],hist_a[5][0])==hist_a[5][1]
assert infer_ports(hist_b[4][0],hist_b[5][0])==hist_b[5][1]
assert infer_gate(hist_a[4][0],hist_a[5][0])==F(2)
assert infer_gate(hist_b[4][0],hist_b[5][0])==F(1)
assert hist_a[5][1][29]-hist_a[5][1][28]==16
assert hist_b[5][1][29]-hist_b[5][1][28]==0

result={
    'schema':'PREFIX624_NATIVE96_TWO_FRAME_PHASE_OBSERVER_V1',
    'date':'2026-11-09',
    'source_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'native_phases':48,'native_ports':96,'labelled_actions':576,
    'gate_sequence_count':len(all_gate_sets),
    'gate_steps_exactly_checked':gate_checks,
    'port_coordinates_exactly_checked':frame_checks,
    'labelled_flow_coordinates_exactly_checked':action_checks,
    'universal_dual_basis_checks':96,
    'universal_dual_relation':'ell(Q(z)v)=3(z+3)*v[4]',
    'lagged_residual':'delta_m=ell(v_m)/3-4*v_(m-1)[4]',
    'recovered_gate':'z_m=ell(v_m)/(3*v_(m-1)[4])-3',
    'positive_support_paths':[list(p) for p in paths],
    'collision_time5_same_phase':True,
    'collision_time4_different_phase':True,
    'collision_delta_5_values':['16','0'],
    'single_frame_fails_for_current_ports':True,
    'two_frames_recover_current_ports_and_gate':True,
    'role':'AUTHOR_SIDE_UNREVIEWED','result':'ALL_ASSERTIONS_PASS'
}
Path(__file__).with_name('PREFIX624_two_frame_native_decoder_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
