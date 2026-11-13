#!/usr/bin/env python3
"""R684: exact V17 slot-frame lift of the R683 repeat-PASS rational kernel.
Self-contained standard-library verification, 120 starts x 64 atomic steps.
"""
from itertools import combinations, permutations
from fractions import Fraction
from collections import defaultdict
import json
from pathlib import Path

TRIADS = tuple(combinations(range(6), 3))
MATCH = (
    ((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
    ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)),
)
PASS = ((0,1), (1,2), (2,0))
BASES = (
    (-4,-3,-2,10), (-3,-2,-4,10), (-2,-4,-3,10),
    (2,4,3,-10), (3,2,4,-10), (4,3,2,-10),
)
W = (-1,1,-2,-1)
ZERO = tuple((0,0,0,0) for _ in range(4))

def c0(S, matching):
    if any((a in S) + (b in S) != 1 for a,b in matching):
        return 0
    return 1 if sum(b in S for a,b in matching)%2 == 0 else -1

C = {S: tuple(c0(S, m) for m in MATCH) for S in TRIADS}
NEIGHBORS = {S:tuple(T for T in TRIADS if len(set(S)&set(T))==2)
             for S in TRIADS}
assert len(set(C.values()))==20 and all(len(a)==9 for a in NEIGHBORS.values())

def event(u, M, e):
    a,b=PASS[e]
    v=list(u);v[a]+=1;v[b]-=1
    L=[list(row) for row in M];L[a][b]+=1
    return tuple(v),tuple(map(tuple,L))

def score(u,M,S,T):
    antisym=sum(C[S][i]*(M[i][j]-M[j][i])*C[T][j]
                for i in range(4) for j in range(4))
    return 7*(sum(u[i]*C[T][i] for i in range(4))+antisym) + sum(W[i]*C[T][i] for i in range(4))

def choose(u,M,S):
    candidates=[]
    for e,(a,b) in enumerate(PASS):
        v,L=event(u,M,e)
        scores=tuple(score(v,L,S,T) for T in NEIGHBORS[S])
        z=max(scores)
        best=tuple(T for T,q in zip(NEIGHBORS[S],scores) if q==z)
        candidates.append((z,W[a]-W[b],e,best))
    return max(candidates)

def slot_transport(F,S,T):
    """Common labels keep their slots; new label inherits the departed slot."""
    removed=tuple(set(S)-set(T)); inserted=tuple(set(T)-set(S))
    assert len(removed)==len(inserted)==1 and set(F)==set(S)
    out=tuple(inserted[0] if v==removed[0] else v for v in F)
    assert set(out)==set(T) and len(set(out))==3
    return out

def frame_quotient_signature(states):
    groups=defaultdict(set)
    for u,M,S,F in states:
        groups[(u,M,S)].add(F)
    return (len(groups),sum(len(fs)-1 for fs in groups.values()))

def propagate(bias,S0,horizon):
    states={(bias,ZERO,S0,S0):Fraction(1)}
    checkpoints={0:dict(states)}
    support_by_t={0:(1,1,0)}
    for t in range(1,horizon+1):
        new=defaultdict(Fraction)
        for (u,M,S,F),mass in states.items():
            _,_,e,options=choose(u,M,S)
            v,L=event(u,M,e)
            assert sum(v)==sum(bias)
            assert all(x>=0 for row in L for x in row)
            assert sum(map(sum,L))==t
            for T in options:
                G=slot_transport(F,S,T)
                new[(v,L,T,G)]+=mass/Fraction(len(options))
        states=dict(new)
        assert sum(states.values(),Fraction(0))==1
        q,extra=frame_quotient_signature(states)
        support_by_t[t]=(len(states),q,extra)
        if t in (12,13,14,18,19,32,64):checkpoints[t]=dict(states)
    return checkpoints,support_by_t

def fmt(S):return ''.join(map(str,S))
def compact_checkpoint(states):
    return [dict(u=list(u),counts=[M[a][b] for a,b in PASS],triad=fmt(S),
                 frame=fmt(F),mass=str(m))
            for (u,M,S,F),m in sorted(states.items())]

def theorem_check():
    # Exact frame-bijection over all 20 triads x 9 neighbors x 6 frames.
    for S in TRIADS:
        frames=list(permutations(S))
        assert len(frames)==len(set(frames))==6
        for T in NEIGHBORS[S]:
            transport=[slot_transport(F,S,T) for F in frames]
            assert len(set(transport))==6
            assert set(transport)==set(permutations(T))
    # The R674 nontrivial V17 frame holonomy.
    s0=(0,1,2); f=s0
    for a,b in zip((s0,(0,1,3),(0,2,3)),((0,1,3),(0,2,3),s0)):
        f=slot_transport(f,a,b)
    assert f==(0,2,1)

    b=(-2,-4,-3,10);start=(0,2,4)
    check,support=propagate(b,start,64)
    assert sorted((fmt(S),fmt(F),str(m)) for (_,_,S,F),m in check[13].items())==[
        ('125','521','1/2'),('234','324','1/2')]
    assert len(check[19])==1
    (u19,M19,S19,F19),m19=next(iter(check[19].items()))
    assert u19==(5,1,-15,10) and (S19,F19)==((0,3,5),(0,3,5)) and m19==1
    assert [M19[a][bb] for a,bb in PASS]==[7,12,0]
    assert support[13]==(2,2,0) and support[19]==(1,1,0)

    by_time=defaultdict(lambda:[0,0,0])
    for bias in BASES:
        for S0 in TRIADS:
            cps,stats=propagate(bias,S0,64)
            for t,(n,qn,extra) in stats.items():
                by_time[t][0]+=n
                by_time[t][1]+=qn
                by_time[t][2]+=extra
    assert all(extra==0 for _,_,extra in by_time.values())
    assert [by_time[t][0] for t in (0,13,14,18,19,32,64)]==[120,122,123,123,121,121,121]
    assert [by_time[t][1] for t in (0,13,14,18,19,32,64)]==[120,122,123,123,121,121,121]
    return {
      'schema':'R684_V17_TYPED_FRAME_BRC_LIFT_CERTIFICATE_V1',
      'predecessor':'R683@1ca5b1c159efff92e6a72edc5822852d6d28453f',
      'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'model':'V23/V27 repeat PASS A,B,C; exact rational uniform ties; V17 shared-label ordered slot inheritance',
      'theorems':{
        'frame_bundle':'Each of 20 triads has 6 ordered frames; each neighbor transition induces bijection',
        'minimal_frame_states':'Six distinguishable frames for complete current-frame observer; 3 fixed binary bits',
        'nontrivial_holonomy':'012->013->023->012 transports ordered frame 012 to 021',
        'kernel_projection':'Forgetting frame is strongly lumpable for (u,M,S) observer: event scores and branch weights ignore frame'},
      'witness':{'initial_bias':list(b),'initial_triad':'024',
         'time_13':compact_checkpoint(check[13]),
         'time_19':compact_checkpoint(check[19])},
      'coverage':{'baselines':6,'triads':20,'initial_conditions':120,
         'time_horizon_inclusive':64,'frame_transports_checked':20*9*6,
         'source_R683_support_reproduced':True,
         'total_states_and_reduced_states':{
             str(t):{'frame_lift_support':by_time[t][0],
                     'projected_support':by_time[t][1],
                     'additional_frame_fibre_states':by_time[t][2]}
             for t in (0,1,12,13,14,18,19,32,64)},
         'total_extra_frame_states_over_all_0_to_64':sum(by_time[t][2] for t in range(65)),
         'all_weight_conservation_exact':True,
         'all_nonnegative_ledger_and_bias_conservation_exact':True},
      'limits':'Finite coverage uses 120 canonical-frame starts and 64-event window. Six-state lower bound spans all frame initializations; does not assert native V39 circulation or Cell/Link scheduler.'}


# R685: long-horizon *complete-frame* fibre test. All definitions above are
# inherited unchanged from immutable R684 source; no alternate dynamics.
from functools import lru_cache

@lru_cache(maxsize=500000)
def choose_fast(u,counts,S):
    # Same model, use the only three populated M entries to avoid rescoring
    # the 4x4 zero rows in the 120 x 256 exhaustive test.
    pool=[]
    for e,(a,b) in enumerate(PASS):
        v=list(u);v[a]+=1;v[b]-=1
        m=list(counts);m[e]+=1
        Om=((0,m[0],-m[2],0),(-m[0],0,m[1],0),
            (m[2],-m[1],0,0),(0,0,0,0))
        scores=[
            7*(sum(v[i]*C[T][i] for i in range(4))+
               sum(C[S][i]*Om[i][j]*C[T][j]
                   for i in range(4) for j in range(4)))+
            sum(W[i]*C[T][i] for i in range(4))
            for T in NEIGHBORS[S]
        ]
        z=max(scores)
        opts=tuple(T for T,q in zip(NEIGHBORS[S],scores) if q==z)
        pool.append((z,W[a]-W[b],e,opts))
    return max(pool)

def evolve_fast(dist):
    nd=defaultdict(Fraction)
    for (u,m,S,F),mass in dist.items():
        _,_,e,options=choose_fast(u,m,S)
        a,b=PASS[e]
        v=list(u);v[a]+=1;v[b]-=1
        counts=list(m);counts[e]+=1
        for T in options:
            G=slot_transport(F,S,T)
            nd[(tuple(v),tuple(counts),T,G)]+=mass/len(options)
    return dict(nd)

def fibre_collisions(dist,t,bias):
    assert sum(dist.values(),Fraction(0))==1
    groups=defaultdict(set)
    for (u,m,S,F),mass in dist.items():
        assert mass>0 and sum(m)==t and all(x>=0 for x in m)
        assert sum(u)==sum(bias) and set(F)==set(S)
        assert u==(bias[0]+m[0]-m[2],bias[1]-m[0]+m[1],
                   bias[2]-m[1]+m[2],bias[3])
        groups[(u,m,S)].add(F)
    return [(key,tuple(sorted(fs))) for key,fs in groups.items() if len(fs)>1]

def r685_verify():
    horizon=256
    collisions=[]
    for bias in BASES:
        for initial_triad in TRIADS:
            dist={(bias,(0,0,0),initial_triad,initial_triad):Fraction(1)}
            for t in range(horizon+1):
                hit=fibre_collisions(dist,t,bias)
                if hit:
                    collisions.append((bias,initial_triad,t,hit))
                    break
                if t<horizon:
                    dist=evolve_fast(dist)
    witness_bias=(-2,-4,-3,10)
    witness_triad=(0,3,5)
    assert len(collisions)==1 and collisions[0][:3]==(
        witness_bias,witness_triad,227),collisions
    dist={(witness_bias,(0,0,0),witness_triad,witness_triad):Fraction(1)}
    checkpoint={}
    for t in range(228):
        if t in (211,212,223,224,225,226,227):
            checkpoint[str(t)]=[
                dict(u=list(u),counts=list(m),S=''.join(map(str,S)),
                     F=''.join(map(str,F)),mass=str(mass))
                for (u,m,S,F),mass in sorted(dist.items())
            ]
        if t<227:dist=evolve_fast(dist)
    key=((4,4,-17,10),(75,83,69),(0,2,5))
    fmass={''.join(map(str,F)):mass
           for (u,m,S,F),mass in dist.items() if (u,m,S)==key}
    assert fmass=={'250':Fraction(1,4),'025':Fraction(1,2)}
    assert len(dist)==3 and sum(fmass.values())==Fraction(3,4)
    report={
      'schema':'R685_LONG_HORIZON_HIDDEN_FRAME_FIBRE_V1',
      'date':'2026-11-10',
      'science_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'predecessor':'R684@ddd775c737dc2f1e11b2992356981d59ff74becd',
      'verified_scope':{'baseline_biases':6,'initial_triads':20,
          'canonical_frame_starts':120,'time_horizon':256,
          'number_of_initial_conditions_with_frame_collision':1,
          'first_collision_in_declared_initial_ensemble':227},
      'witness':{'initial_bias':list(witness_bias),'S0':'035','F0':'035',
          'first_split':212,'collision_time':227,
          'field':{'u':[4,4,-17,10],'counts':[75,83,69],'S':'025'},
          'frame_mass':{'250':'1/4','025':'1/2'},
          'field_total_mass':'3/4',
          'conditional_frame_mass':{'250':'1/3','025':'2/3'},
          'all_states_at_selected_steps':checkpoint},
      'exact_checks':{'Fraction_total_mass_1':True,'M_nonnegative':True,
          'sum_M_equals_time':True,'bias_from_counts':True,
          'all_starts_checked':True},
      'finite_scope_note':'Earliest only for 120 sorted-frame starts and the t<=256 scan; not a universal initial-state lower bound.'
    }
    Path(__file__).with_name('R685_EVIDENCE.json').write_text(
      json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('R685_HIDDEN_FRAME_FIBRE_T227_EXACT_PASS')
    print('120 starts; first collision at 227; 250:1/4, 025:1/2')

if __name__=='__main__':
    r685_verify()
