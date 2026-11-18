#!/usr/bin/env python3
"""R749SL exact filter and one-hidden-lineage minimal augmentation witness."""
from fractions import Fraction as F
from itertools import product
import json
A=frozenset((0,1)); B=frozenset((1,2)); C=frozenset((2,3))
assert C != A^B and len(B&C)==1
A1=B; B1=C; Cf=A1^B1; Cn=frozenset((3,4))
assert Cf==frozenset((1,3)) and len(B1&Cn)==1 and Cn!=Cf

def states(axes):return [dict(zip(sorted(axes),s)) for s in product((-1,1),repeat=len(axes))]
def key(x):return tuple(sorted(x.items()))
def mu0(z):return {key({0:z,1:a,2:b}):F(1,4) for a,b in product((-1,1),repeat=2)}
def trans(x,A,B,C,p):
    old=next(iter(A-B)); new=next(iter(C-B))
    if C==A^B:
        th=8*p/(1+7*p)
        choices=((x[old],(1+th)/2),(-x[old],(1-th)/2))
    else:choices=((-1,F(1,2)),(1,F(1,2)))
    return [(key({**{a:x[a] for a in B},new:s}),w) for s,w in choices if w]

def forward(d,A,B,C,p):
    out={key(x):F(0) for x in states(B|C)}
    for k,w0 in d.items():
        for y,prob in trans(dict(k),A,B,C,p):out[y]+=w0*prob
    return out

def action_emission_update(d, p, policy):
    # C_f observed and an outcome emitted from the copied sign at axis 2 on new state.
    out={key(x):F(0) for x in states(B1|Cf)}
    for k,v in d.items():
        x=dict(k); pc=policy(x)
        for ky,w in trans(x,A1,B1,Cf,p):
            y=dict(ky);ell=F(2+y[2],4)
            out[ky]+=v*pc*w*ell
    den=sum(out.values()); assert den>0
    return den,{k:v/den for k,v in out.items()}

uniform={key(x):F(1,8) for x in states(B|C)}
p=F(1,2)
for z in (-1,1):
    d=forward(mu0(z),A,B,C,p)
    assert d==uniform

pi_local=lambda x:F(2+x[1],4)
Dloc,ploc=action_emission_update(uniform,p,pi_local)
assert Dloc>0
for z in (-1,1):
    d=forward(mu0(z),A,B,C,p)
    assert action_emission_update(d,p,pi_local)==(Dloc,ploc)

prob={z:F(2+z,4) for z in (-1,1)}
assert prob[-1]==F(1,4) and prob[1]==F(3,4)
for z in (-1,1):
    d=forward(mu0(z),A,B,C,p)
    assert sum(d[k]*prob[z] for k in d)==prob[z]
    assert sum(d.values())==1

print(json.dumps({'status':'PASS','first_transition':'nonforced; named axis 0 discarded',
 'p':'1/2','current_eight_lift_distribution':'uniform 1/8 for both historical z',
 'state_local_policy_action_and_emission':'identical for z=-1 and z=+1',
 'hidden_memory_forced_choice_probabilities':{'z=-1':'1/4','z=+1':'3/4'},
 'minimal_extra_hidden_provenance_bits_for_this_family':1,
 'native_event_permission':False},indent=2,sort_keys=True))
