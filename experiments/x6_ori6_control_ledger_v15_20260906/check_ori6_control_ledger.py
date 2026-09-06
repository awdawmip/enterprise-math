#!/usr/bin/env python3
from itertools import product

STATES=tuple((r,e) for r in range(6) for e in (-1,1))


def step(state,u):
    r,e=state
    return ((r+e)%6, (-e if u else e))


def run(state,controls):
    out=state
    for u in controls: out=step(out,u)
    return out

# Exact ledger/chirality and phase-integral formulas on all binary words to length 10.
for n in range(11):
    for controls in product((0,1),repeat=n):
        for r0,e0 in ((0,1),(2,-1),(5,1)):
            r,e=run((r0,e0),controls)
            chi=sum(controls)%2
            assert e==e0*((-1)**chi)
            running=0
            prefix_chi=0
            for u in controls:
                running += e0*((-1)**prefix_chi)
                prefix_chi ^= u
            assert r==(r0+running)%6

# Current event kind has same immediate phase target, different hidden chirality.
for s in STATES:
    a=step(s,0); b=step(s,1)
    assert a[0]==b[0]
    assert a[1]==-b[1]

# Phase translation and chirality relabeling symmetries.
def T(k,s):
    r,e=s; return ((r+k)%6,e)

def C(s):
    r,e=s; return ((-r)%6,-e)

for s in STATES:
    for u in (0,1):
        for k in range(6):
            assert step(T(k,s),u)==T(k,step(s,u))
        assert step(C(s),u)==C(step(s,u))

# Enumerate all state-dependent binary selectors and keep those invariant under
# all phase translations and chirality relabeling. There should be exactly two.
symmetric=[]
for bits in product((0,1),repeat=len(STATES)):
    sigma=dict(zip(STATES,bits))
    ok=True
    for s in STATES:
        for k in range(6):
            if sigma[T(k,s)]!=sigma[s]: ok=False; break
        if not ok: break
        if sigma[C(s)]!=sigma[s]: ok=False; break
    if ok: symmetric.append(bits)
assert len(symmetric)==2
assert {sum(bits) for bits in symmetric}=={0,12}

# Both homogeneous laws are reversible/bijective, so reversibility does not select.
for u in (0,1):
    images={step(s,u) for s in STATES}
    assert len(images)==12

# Final orientation charge only needs parity, not full event word.
assert run((0,1),(1,1))==run((0,1),())  # same local state after B^2
assert (1,1)!=( )  # but histories differ

print('PASS_X6_ORI6_CONTROL_LEDGER_V15')
print('local_states',len(STATES))
print('symmetric_deterministic_trigger_laws',len(symmetric))
print('homogeneous_laws',('ALWAYS_ADVANCE','ALWAYS_PHASE_REVERSAL'))
print('reversibility_selects_unique_trigger',False)
print('minimal_event_control_cardinality',2)
print('control_parity_equals_local_Ori6_ledger',True)
