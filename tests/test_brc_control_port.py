from itertools import product
from fractions import Fraction as Q
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition, refine_control_partition
from enterprise_math.brc_transport import Affine, MomentState, eye
from enterprise_math.predictive_quotient import observation_partition, predictive_block_profile, stable_predictive_partition

STATES=tuple(product((0,1),repeat=6))
def encode(s): return sum(v<<i for i,v in enumerate(s))
def decode(n): return tuple((n>>i)&1 for i in range(6))
def rot(s): return s[1:]+s[:1]
def refl(s): return tuple(s[(-i)%6] for i in range(6))
def set0(s): return (1,)+s[1:]
def obs(s): return (sum(s),sum(s[i]*s[(i+1)%6] for i in range(6)),sum(s[i]*s[(i+3)%6] for i in range(3)))
def transition(fn): return tuple(encode(fn(decode(i))) for i in range(64))
def packet(fn,effect):
    edges=[]
    for i in range(64):
        s=decode(i); edges.append((i,encode(fn(s)),1,Affine(eye(6),(effect(s),0,0,0,0,0)),1))
    return ControlPacket.from_edges(64,0,1,edges)

def orbit(s):
    out=[]; t=s
    for _ in range(6): out.append(t); t=rot(t)
    t=refl(s)
    for _ in range(6): out.append(t); t=rot(t)
    return frozenset(out)

def test_mask6_orbits_and_predictive_profiles():
    orbits={min(orbit(s)):orbit(s) for s in STATES}
    assert len(orbits)==13 and sum(len(v) for v in orbits.values())==64
    assert len({obs(rep) for rep in orbits})==13
    assert all(all(obs(x)==obs(rep) for x in members) for rep,members in orbits.items())
    sym={'R':rot,'J':refl}; addressed={**sym,'S0':set0}
    assert predictive_block_profile(STATES,sym,obs,4)==(13,13,13,13,13)
    assert stable_predictive_partition(STATES,sym,obs).block_count==13
    assert predictive_block_profile(STATES,addressed,obs,5)==(13,32,52,63,64,64)
    q=stable_predictive_partition(STATES,addressed,obs)
    assert q.block_count==64 and q.stabilization_depth==4

def test_effect_valued_control_quotient_and_phase_break():
    labels=observation_partition(STATES,obs)
    rinv=packet(rot,lambda s:sum(s)%2); jinv=packet(refl,lambda s:sum(s)%2)
    assert certify_control_partition(rinv,labels)==labels
    assert certify_control_partition(jinv,labels)==labels
    assert len(set(refine_control_partition((rinv,jinv),labels)))==13
    phase=packet(rot,lambda s:s[0])
    try: certify_control_partition(phase,labels)
    except ValueError: pass
    else: raise AssertionError('phase-addressed spatial effect must split orientation-free classes')
    assert len(set(refine_control_partition((rinv,jinv,phase),labels)))==64

def test_control_packet_time_and_moment_composition():
    r=ControlPacket.deterministic(transition(rot),start=0)
    j=ControlPacket.deterministic(transition(refl),start=1)
    joined=r.then(j)
    assert joined.start==0 and joined.duration==2
    control=encode((1,0,1,0,0,0)); point=(2,-1,0,0,0,0)
    out=joined.evaluate(control,point)
    assert len(out)==1 and next(iter(out))[1]==tuple(Q(v) for v in point)
    state={control:MomentState.from_point(point)}
    after=joined.moment_action(state)
    assert len(after)==1 and next(iter(after.values()))==MomentState.from_point(point)
    try: r.then(j.at(2))
    except ValueError: pass
    else: raise AssertionError('time-port mismatch must reject')
