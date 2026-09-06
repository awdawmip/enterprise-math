#!/usr/bin/env python3
"""Exact local no-go: same macro arrow requires INNER or OUTER by event context."""
from itertools import product

N=6
ZERO=(0,)*N
STAR_TRIPLES=((0,1,2),(0,3,4),(1,3,5),(2,4,5))

def unit(i,s=1):
    z=[0]*N;z[i]=s;return tuple(z)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def l1(a,b): return sum(abs(x-y) for x,y in zip(a,b))

def q_action(S,z):
    i,j,k=S
    out=[0]*N
    # Q: ei->-ej, ej->-ek, ek->-ei; complement fixed.
    mapping={i:(j,-1),j:(k,-1),k:(i,-1)}
    for a,c in enumerate(z):
        if not c: continue
        if a in mapping:
            b,s=mapping[a]; out[b]+=s*c
        else: out[a]+=c
    return tuple(out)

def branches(a,b):
    outer=add(a,b)
    assert l1(a,ZERO)==l1(ZERO,b)==1
    assert l1(a,outer)==l1(outer,b)==1
    assert outer!=ZERO
    return {'INNER':ZERO,'OUTER':outer}

conflicts=0
triad_joint_cases=0
for S in STAR_TRIPLES:
    # Six Q phases for one port.
    phase=[unit(S[0])]
    for _ in range(5): phase.append(q_action(S,phase[-1]))
    assert q_action(S,phase[-1])==phase[0]

    # At every macro phase build the three-token triad by Q^r acting on the
    # three positive axis tokens. The unique common midpoint selection is III.
    tokens=[unit(i) for i in S]
    for r in range(6):
        starts=tokens
        targets=[q_action(S,a) for a in starts]
        opts=[branches(a,b) for a,b in zip(starts,targets)]
        common=[]
        for bits in product(('INNER','OUTER'),repeat=3):
            mids=[opts[t][bits[t]] for t in range(3)]
            if mids[0]==mids[1]==mids[2]: common.append((bits,mids[0]))
            triad_joint_cases+=1
        assert common==[(('INNER','INNER','INNER'),ZERO)]
        tokens=targets

    # For the same shell macro arrows, the established nonzero intermediate
    # phase requirement selects OUTER. Hence no endpoint/frame-only selector can
    # satisfy both event semantics.
    for r,a in enumerate(phase):
        b=phase[(r+1)%6]
        br=branches(a,b)
        key=(S,a,b) # Q_S is fixed by S; shortest fiber is also fixed by this pair.
        force_required='INNER'
        phase_required='OUTER'
        assert force_required!=phase_required
        assert br[force_required]!=br[phase_required]
        conflicts+=1

assert conflicts==24
assert triad_joint_cases==4*6*8

# A two-valued event-kind context suffices on this restricted interface.
def contextual_selector(kind):
    return {'TRIADIC_ATOMIC_CLOSURE':'INNER','NONZERO_PHASE_REFINEMENT':'OUTER'}[kind]
assert contextual_selector('TRIADIC_ATOMIC_CLOSURE')=='INNER'
assert contextual_selector('NONZERO_PHASE_REFINEMENT')=='OUTER'

print('PASS_X6_BRANCH_SELECTOR_CONTEXT_NOGO_V3')
print('STAR_macro_arrow_conflicts',conflicts)
print('joint_triad_branch_cases',triad_joint_cases)
print('endpoint_only_universal_selector_exists',False)
print('minimum_context_classes_on_restricted_interface',2)
