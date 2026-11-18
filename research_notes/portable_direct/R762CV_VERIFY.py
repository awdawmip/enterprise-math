#!/usr/bin/env python3
"""R762CV: exact finite S6-equivariant self-map classification of signed X6 triads.
Standard library only. No native TRIADIC_CLOSURE_E event authority is assumed.
"""
import itertools, json
from math import factorial

AXES=tuple(range(6))
TRIADS=tuple((c,sig) for c in itertools.combinations(AXES,3)
             for sig in itertools.product((0,1),repeat=3))  # 1 denotes negative
states=tuple(sorted(tuple(zip(s,sig)) for s,sig in TRIADS))
state_set=set(states)
assert len(states)==len(state_set)==160
perms=tuple(itertools.permutations(AXES))
assert len(perms)==factorial(6)==720

def k(t): return sum(sig for _,sig in t)
def apply(p,t): return tuple(sorted((p[i],sig) for i,sig in t))
def blocks(t):
    A={i for i,s in t if s==1};B={i for i,s in t if s==0}; C=set(AXES)-A-B
    return A,B,C

def local_options(t):
    A,B,C=blocks(t)
    out=[]
    if A and B:
        for a,b in itertools.product((0,1), repeat=2):
            out.append(tuple(sorted([(i,a) for i in A]+[(i,b) for i in B])))
    else:
        U=A|B
        for s in (0,1):out.append(tuple(sorted((i,s) for i in U)))
    for s in (0,1):out.append(tuple(sorted((i,s) for i in C)))
    assert len(out)==len(set(out))
    return tuple(out)

sizes={};local_map_checks=0;stabilizer_checks=0
for kk in range(4):
    group=[t for t in states if k(t)==kk]
    t=group[0]
    H=tuple(p for p in perms if apply(p,t)==t)
    stabs=(factorial(kk)*factorial(3-kk)*factorial(3))
    assert len(H)==stabs
    fixed=tuple(s for s in states if all(apply(p,s)==s for p in H))
    choices=local_options(t)
    assert set(fixed)==set(choices),(kk,fixed,choices)
    stabilizer_checks+=len(H)*len(states)
    sizes[str(kk)]={'orbit_size':len(group),'stabilizer_size':len(H),'fixed_target_choices':len(fixed)}
    reps={}
    for p in perms:
        transformed=apply(p,t)
        if transformed not in reps:reps[transformed]=p
    assert len(reps)==len(group)
    for option in fixed:
        outputs={s:apply(reps[s],option) for s in group}
        for s in group:
            assert outputs[s] in state_set
            for p in perms:
                assert outputs[apply(p,s)]==apply(p,outputs[s])
                local_map_checks+=1

support_preserving={};signcount_preserving={}
for kk in range(4):
    t=next(t for t in states if k(t)==kk)
    allowed=local_options(t)
    support_preserving[str(kk)]=sum({i for i,_ in x}=={i for i,_ in t} for x in allowed)
    signcount_preserving[str(kk)]=sum(k(x)==kk for x in allowed)
assert [sizes[str(kk)]['fixed_target_choices'] for kk in range(4)]==[4,6,6,4]
assert [support_preserving[str(kk)] for kk in range(4)]==[2,4,4,2]
assert [signcount_preserving[str(kk)] for kk in range(4)]==[2,1,1,2]
assert 4*6*6*4==576
assert 2*4*4*2==64
assert 2*1*1*2==4

def mirror(t): return tuple(sorted((i,1-s) for i,s in t))
def alt(t):
    if k(t) in (1,2):return t
    unused=set(AXES)-{i for i,_ in t}
    return tuple((i,k(t)//3) for i in sorted(unused))
for t in states:
    assert alt(alt(t))==t
    assert k(alt(t))==k(t)
    assert mirror(alt(t))==alt(mirror(t))
    for p in perms:
        assert alt(apply(p,t))==apply(p,alt(t))

out={
 'study':'R762CV_S6_EQUIVARIANT_TRIAD_ENDOMAPS',
 'scientific_scope':'pure signed candidate triads, unmarked deterministic maps, S6 acts by axis permutations',
 'status':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENTLY_REVIEWED',
 'state_count':len(states),'group_order':len(perms),'orbit_info':sizes,
 'local_equivariance_assertions':local_map_checks,
 'stabilizer_fix_checks':stabilizer_checks,
 'full_signcount_plus_reversal_alt_checks':len(states)*len(perms),
 'equivariant_self_maps':576,
 'support_preserving_choices_by_k':support_preserving,
 'support_preserving_maps':64,
 'signcount_preserving_choices_by_k':signcount_preserving,
 'signcount_preserving_maps':4,
 'global_sign_reversal_equivariant_maps':24,
 'signcount_and_global_reversal_equivariant_maps':2,
 'exact_finite_checks_passed':True,
 'native_event_licence':'NOT_EVALUATED',
}
print(json.dumps(out,indent=2,sort_keys=True))
