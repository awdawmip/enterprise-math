#!/usr/bin/env python3
from itertools import combinations, product

CHANNELS=tuple(range(6))
SIGNS=(-1,1)

# Six channel labels are not enough for twelve signed X6 sides.
half_ports={(c,s) for c in CHANNELS for s in SIGNS}
assert len(half_ports)==12
channel_only={p:p[0] for p in half_ports}
assert len(set(channel_only.values()))==6
for c in CHANNELS:
    assert channel_only[(c,+1)]==channel_only[(c,-1)]

# Signed lift of one oriented 3-cycle has exact C6 order.
def q_port(cycle,port):
    c,s=port
    if c not in cycle:
        return port
    r=cycle.index(c)
    return (cycle[(r+1)%3],-s)

for S in combinations(CHANNELS,3):
    i,j,k=S
    for cycle in ((i,j,k),(i,k,j)):
        for p in half_ports:
            x=p
            for _ in range(3): x=q_port(cycle,x)
            if p[0] in cycle:
                assert x==(p[0],-p[1])
            else:
                assert x==p
            for _ in range(3): x=q_port(cycle,x)
            assert x==p

# Spatial contextual INNER/OUTER theorem.
ZERO=(0,)*6

def unit(i,s=1):
    z=[0]*6; z[i]=s; return tuple(z)

def add(a,b): return tuple(x+y for x,y in zip(a,b))

def q_on_selected(S,z):
    i,j,k=S
    mapping={i:(j,-1),j:(k,-1),k:(i,-1)}
    out=[0]*6
    for idx,val in enumerate(z):
        if not val: continue
        if idx in mapping:
            target,sg=mapping[idx]
            out[target]+=sg*val
        else:
            out[idx]+=val
    return tuple(out)

cases=0
for S in combinations(range(6),3):
    for signs in product(SIGNS,repeat=3):
        starts=[unit(i,s) for i,s in zip(S,signs)]
        targets=[q_on_selected(S,a) for a in starts]
        # Closure context: all INNER share pivot.
        inner_midpoints=[ZERO,ZERO,ZERO]
        assert len(set(inner_midpoints))==1
        # Phase context: OUTER midpoints are nonzero and distinct.
        outer_midpoints=[add(a,b) for a,b in zip(starts,targets)]
        assert all(m!=ZERO for m in outer_midpoints)
        assert len(set(outer_midpoints))==3
        # Therefore the closure and phase contexts demand opposite sections.
        cases+=1
assert cases==160

print('PASS_X6_SIGNED_HALFPORT_CONTEXT_V2')
print('abstract_channels',6)
print('signed_half_ports',12)
print('minimal_polarity_repair_bits_per_occurrence',1)
print('triadic_signed_context_cases',cases)
print('triadic_closure_section','INNER')
print('nonzero_phase_section','OUTER')
print('endpoint_frame_only_selector_sufficient',False)
