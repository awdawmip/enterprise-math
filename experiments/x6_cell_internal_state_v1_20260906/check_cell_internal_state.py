#!/usr/bin/env python3
"""Exact finite checks for the X6 triadic Cell-internal-state V1 model."""
from collections import Counter, defaultdict
from itertools import permutations, product

AXES=tuple(range(6))
CHANNELS=tuple(range(6))

# Full ordered signed triad frames: three distinct axes, one sign per token.
FRAMES=tuple(
    (axes,signs)
    for axes in permutations(AXES,3)
    for signs in product((-1,1),repeat=3)
)
assert len(FRAMES)==960 and len(set(FRAMES))==960


def R(frame):
    """Fixed triadic Q_S applied tokenwise: cycle axes, flip each token sign."""
    axes,signs=frame
    return ((axes[1],axes[2],axes[0]),tuple(-s for s in signs))


def cycle_class(frame):
    """Forget only the phase origin; retain cyclic orientation and signed ports."""
    reps=[]
    axes,signs=frame
    for k in range(3):
        reps.append((axes,signs))
        axes=(axes[1],axes[2],axes[0])
        signs=(signs[1],signs[2],signs[0])
    return frozenset(reps)


def unordered_signed(frame):
    axes,signs=frame
    return frozenset(zip(axes,signs))


def passage_support(frame):
    axes,_=frame
    return frozenset((axes[r],axes[(r+1)%3]) for r in range(3))


def signed_cycle_observer(frame):
    # Oriented passage support + sign on every source axis.
    axes,signs=frame
    sign_map=frozenset(zip(axes,signs))
    return (passage_support(frame),sign_map)

# Every full frame has exact C6 period; 160 C6 orbits.
seen=set(); orbit_lengths=[]
for f in FRAMES:
    if f in seen: continue
    orbit=[]; x=f
    while x not in orbit:
        orbit.append(x); seen.add(x); x=R(x)
    orbit_lengths.append(len(orbit))
assert Counter(orbit_lengths)==Counter({6:160})

# Add relation-stage bit Theta/Kappa. U^2=R and all states have exact period 12.
def U(state):
    stage,frame=state
    return ('K',frame) if stage=='T' else ('T',R(frame))

STATES=tuple((stage,f) for stage in ('T','K') for f in FRAMES)
seen=set(); c12_lengths=[]
for st in STATES:
    if st in seen: continue
    orbit=[]; x=st
    while x not in orbit:
        orbit.append(x); seen.add(x); x=U(x)
    c12_lengths.append(len(orbit))
assert len(STATES)==1920
assert Counter(c12_lengths)==Counter({12:160})

# Quotient by phase-origin only: 320 cyclic signed triad states and R descends.
classes={cycle_class(f) for f in FRAMES}
assert len(classes)==320
next_by_class=defaultdict(set)
for f in FRAMES:
    next_by_class[cycle_class(f)].add(cycle_class(R(f)))
assert all(len(v)==1 for v in next_by_class.values())

# Forget cyclic orientation too: 160 unordered signed triads. For 120 mixed-sign
# states there are two distinct possible next unordered states, so this quotient
# is not predictive/Markov safe for the signed-triad successor.
next_by_unordered=defaultdict(set)
for f in FRAMES:
    next_by_unordered[unordered_signed(f)].add(unordered_signed(R(f)))
assert len(next_by_unordered)==160
assert Counter(len(v) for v in next_by_unordered.values())==Counter({2:120,1:40})

# PF-10 channel bridge cannot be silently identified with axes. All bijections
# channel -> unsigned axis form a 720-element frame torsor.
CHANNEL_FRAMES=tuple(permutations(AXES))
assert len(CHANNEL_FRAMES)==720
phi=CHANNEL_FRAMES[0]
nontrivial=(1,0,2,3,4,5)
assert tuple(nontrivial[phi[c]] for c in CHANNELS)!=phi

# Once a channel-axis frame is chosen, positive ingress/egress occupancy only
# remembers the active 3-subset (20 possibilities); the passage support remembers
# one of the two oriented 3-cycles on that subset (40); adding spatial signs gives
# the 320 phase-origin-free signed-cycle states. Full C6 phase needs a factor 3.
occupancy={frozenset(f[0]) for f in FRAMES}
passages={passage_support(f) for f in FRAMES}
signed_cycles={signed_cycle_observer(f) for f in FRAMES}
assert len(occupancy)==20
assert len(passages)==40
assert len(signed_cycles)==320
assert len(FRAMES)==3*len(signed_cycles)

# Passage support is invariant under one R step, but it cannot recover signs or
# phase origin. This is an explicitly scoped safe observer, not full-state identity.
assert all(passage_support(R(f))==passage_support(f) for f in FRAMES)

print('PASS_X6_CELL_INTERNAL_STATE_V1')
print('ordered_signed_triad_frames',len(FRAMES))
print('triadic_C6_orbits',len(orbit_lengths))
print('decorated_stage_states',len(STATES))
print('decorated_C12_orbits',len(c12_lengths))
print('phase_origin_free_signed_cycle_states',len(classes))
print('unordered_signed_triad_states',len(next_by_unordered))
print('unordered_states_with_two_possible_successors',120)
print('axis_channel_frame_torsor_size',len(CHANNEL_FRAMES))
print('pf10_active_channel_subsets',len(occupancy))
print('pf10_oriented_passage_supports',len(passages))
print('signed_passage_states',len(signed_cycles))
