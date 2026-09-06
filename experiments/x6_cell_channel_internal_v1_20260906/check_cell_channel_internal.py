#!/usr/bin/env python3
from itertools import permutations, combinations, product

CHANNELS=tuple(range(6))
SIGNS=(-1,1)


def update_frame(frame):
    (c0,s0),(c1,s1),(c2,s2)=frame
    return ((c1,-s0),(c2,-s1),(c0,-s2))


def cyclic_rots(chs):
    chs=tuple(chs)
    return tuple(chs[i:]+chs[:i] for i in range(3))


def canonical_cycle(chs):
    return min(cyclic_rots(tuple(chs)))


def kernel_key(frame):
    chs=tuple(c for c,_ in frame)
    cyc=canonical_cycle(chs)
    sig=dict(frame)
    return (cyc,tuple(sig[c] for c in cyc))


frames=tuple(
    tuple(zip(chs,signs))
    for chs in permutations(CHANNELS,3)
    for signs in product(SIGNS,repeat=3)
)
assert len(frames)==960 and len(set(frames))==960

# R^3 flips all polarities while preserving the channel anchor; R^6=id.
for f in frames:
    x=f
    for _ in range(3): x=update_frame(x)
    assert x==tuple((c,-s) for c,s in f)
    for _ in range(3): x=update_frame(x)
    assert x==f

# Exact C6 orbit partition.
seen=set(); frame_orbits=[]
for f in frames:
    if f in seen: continue
    orb=[]; x=f
    while x not in orb:
        orb.append(x); seen.add(x); x=update_frame(x)
    assert len(orb)==6
    frame_orbits.append(tuple(orb))
assert len(frame_orbits)==160

# 40 oriented channel 3-cycles, 320 signed kernels, 160 static signed supports.
cycles={canonical_cycle(chs) for chs in permutations(CHANNELS,3)}
assert len(cycles)==40
kernels={kernel_key(f) for f in frames}
assert len(kernels)==320
supports={frozenset(f) for f in frames}
assert len(supports)==160
unsigned_supports={frozenset(c for c,_ in f) for f in frames}
assert len(unsigned_supports)==20

# Event parity doubles 960 frames into 160 exact C12 interaction cycles.
def event_step(state):
    f,parity=state
    if parity==0: return (f,1)
    return (update_frame(f),0)

event_states={(f,p) for f in frames for p in (0,1)}
assert len(event_states)==1920
seen=set(); event_orbits=[]
for st in event_states:
    if st in seen: continue
    orb=[]; x=st
    while x not in orb:
        orb.append(x); seen.add(x); x=event_step(x)
    assert len(orb)==12
    event_orbits.append(tuple(orb))
assert len(event_orbits)==160

# Six PF-10 channel labels cannot encode twelve signed X6 sides without polarity.
half_ports={(c,s) for c in CHANNELS for s in SIGNS}
assert len(half_ports)==12
coarse={p:p[0] for p in half_ports}
assert len(set(coarse.values()))==6
for c in CHANNELS:
    assert coarse[(c,1)]==coarse[(c,-1)]

# Signed support alone is non-Markov for 120 mixed-polarity supports when chirality is erased.
def frame_from_support_cycle(supp,cyc):
    sig=dict(supp)
    return tuple((c,sig[c]) for c in cyc)

ambiguous=0; coherent=0
for supp in supports:
    chset={c for c,_ in supp}
    options=[cyc for cyc in cycles if set(cyc)==chset]
    assert len(options)==2
    nxt={frozenset(update_frame(frame_from_support_cycle(supp,cyc))) for cyc in options}
    if len(nxt)==2: ambiguous+=1
    else: coherent+=1
assert (ambiguous,coherent)==(120,40)

# Contextual INNER/OUTER split on all 20 axis triads x 8 sign sheets.
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

context_cases=0
for S in combinations(range(6),3):
    for signs in product(SIGNS,repeat=3):
        starts=[unit(i,s) for i,s in zip(S,signs)]
        targets=[q_on_selected(S,a) for a in starts]
        inner=[ZERO,ZERO,ZERO]
        outer=[add(a,b) for a,b in zip(starts,targets)]
        assert inner[0]==inner[1]==inner[2]==ZERO
        assert all(m!=ZERO for m in outer)
        assert len(set(outer))==3
        context_cases+=1
assert context_cases==160

print('PASS_X6_CELL_CHANNEL_INTERNAL_V1')
print('axis_channel_frames',720)
print('signed_half_ports',12)
print('full_ordered_signed_triad_frames',len(frames))
print('triadic_C6_frame_orbits',len(frame_orbits))
print('oriented_channel_3cycles',len(cycles))
print('signed_predictive_kernels',len(kernels))
print('static_signed_supports',len(supports))
print('local_event_states',len(event_states))
print('local_C12_interaction_cycles',len(event_orbits))
print('signed_support_chirality_ambiguous',ambiguous)
print('signed_support_chirality_coherent',coherent)
print('contextual_inner_outer_cases',context_cases)
print('context_free_endpoint_branch_selector_sufficient',False)
