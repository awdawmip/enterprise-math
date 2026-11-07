#!/usr/bin/env python3
"""EC48Q: exact H5 k=1,l=3 two-source positive stopping-tree support check."""
from fractions import Fraction as F
from itertools import product
import json

W = ((0,0),(0,1),(1,0))
MU=F(1,24)
COSTS=(F(1,128),F(1,64),F(1,32),F(1,24))

def leaves():
    d=[]
    for h,w in enumerate(W):
        d.extend(((h,'+',None,F(1,6),F(1,12)),(h,'-',None,F(1,12),F(1,6))))
        for j,bit in enumerate(w):
            if bit:
                d.extend(((h,j,'up',F(1,32),F(1,96)),(h,j,'down',F(1,96),F(1,32))))
            else:
                d.append((h,j,'neutral',MU,MU))
    return d

LEAVES=leaves()
assert len(LEAVES)==14
assert sum((p for *_,p,q in LEAVES),F(0))==1
assert sum((q for *_,p,q in LEAVES),F(0))==1
assert all(p>0 and q>0 for *_,p,q in LEAVES)

# Under likelihood-ratio readout the payoff-optimal terminal accept decision
# for alpha-beta is accept iff P/Q>1. All stage-4 private +/- are optimally
# stopped (continuation cannot change their likelihood ratio but costs > 0).
# At each h stage 3 either stop, or continue and encode 0/1.
# At stage 4, each bit and shared j chooses stop(0)/continue(1).
# This is exhaustive for deterministic 2-register support-optimal controllers.
def payoff(actions,updates,c):
    v=-6*c     # both sources must survive neutral t1,t2 and enter t3
    for h,act in enumerate(actions):
        if act==-1: continue
        v += F(1,12)-F(2,3)*c # private + stop/accept; stage3 continued
        for j,bit in enumerate(W[h]):
            if updates[act*2+j]:
                v += (MU/F(2) if bit else F(0))-2*c*MU
    return v

def best_two(c):
    top=None; top_action=None; n=0
    for actions in product((-1,0,1),repeat=3):
        for updates in product((0,1),repeat=4):
            x=payoff(actions,updates,c); n+=1
            if top is None or x>top:
                top=x; top_action=[list(actions),list(updates)]
    early=max(-2*c,-4*c)
    return max(top,early),top_action,n,top,early

def best_full(c):
    top=None; best=None
    for choices in product((-1,0,1,2,3),repeat=3):
        val=-6*c
        for h,ch in enumerate(choices):
            if ch==-1:continue
            val += F(1,12)-F(2,3)*c
            for j,bit in enumerate(W[h]):
                if (ch>>j)&1: val+=(MU/F(2) if bit else F(0))-2*c*MU
        if top is None or val>top:
            top=val;best=choices
    return max(top,-2*c,-4*c),best

def J(o,c):return o[0]-o[1]-c*(o[2]+o[3])
def form(o):return [str(x) for x in o]

out=[]
for c in COSTS:
    two,pol,n,stage,early=best_two(c)
    full,witness=best_full(c)
    expect_full=F(7,24)-F(49,6)*c
    expect_two=F(7,24)-F(33,4)*c
    assert full==expect_full,(c,full,expect_full)
    assert two==expect_two,(c,two,expect_two)
    assert full-two==c/F(12)
    assert n==432
    out.append({'c':str(c),'n_two_state_policies':n,
                'full':str(full),'two_state':str(two), 'gap':str(full-two),
                'optimizer_two_state_example':pol,
                'optimizer_full_example':list(witness)})

# Output coordinates in lifted H5: both prefixes forced to continue;
# the 3 original h's survive at t3 and all private +/- stop at t4.
OF=(F(9,16),F(13,48),F(49,12),F(49,12))
OT=(F(9,16),F(13,48),F(33,8),F(33,8))
assert J(OF,F(1,32))==F(7,192)
assert J(OT,F(1,32))==F(13,384)
assert J(OF,F(1,32))-J(OT,F(1,32))==F(1,384)

# k=1,l=1 H5 shifted three-leaf counterexample. Full accepts on terminal
# up in b, stops on a; single register must treat a,b equally (joint LR=1).
c=F(1,32)
full_one=F(1,4)-9*c
one_state=max(-2*c,-4*c,-6*c,-8*c,F(1,4)-10*c)
assert full_one==-F(1,32)
assert one_state==-F(1,16)
assert full_one-one_state==F(1,32)
report={'experiment':'EC48Q H5 stage-two width=1, global stage-three width=3',
        'terminal_leaves':len(LEAVES),'p_total':'1','q_total':'1',
        'controller_normal_form':'3^3 x 2^4 = 432 deterministic 2-state actions; early roots checked',
        'grid':out,'witness_cost':'1/32','witness_full':form(OF),
        'witness_two_state':form(OT),
        'witness_gap':'1/384',
        'k1_l1_cost':'1/32','k1_l1_full':str(full_one),
        'k1_l1_one_state':str(one_state),'k1_l1_gap':'1/32',
        'all_exact_assertions':'PASS',
        'mathematical_scope':'finite auxiliary positive two-source BRC observation tree; no native X6 transfer',
        'proof_status':'AUTHOR_PROVED_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
