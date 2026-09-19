from itertools import product
from enterprise_math.predictive_quotient import predictive_block_profile, stable_predictive_partition, observation_partition
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition, refine_control_partition
from enterprise_math.brc_transport import Affine, eye

STATES = tuple(product(range(64), range(6)))  # (local mask, local phase offset delta)

def bits(m): return tuple((m >> i) & 1 for i in range(6))
def mask(s): return sum(v << i for i, v in enumerate(s))
def rot(s, k=1):
    k %= 6
    return s[k:] + s[:k]
def refl(s): return tuple(s[(-i) % 6] for i in range(6))
def align(state):
    m, delta = state
    return mask(rot(bits(m), delta))
def localize(a, delta): return mask(rot(bits(a), -delta))
def transform_abs(state, fn):
    m, d = state
    return (localize(mask(fn(bits(align(state)))), d), d)
def gauge(state):
    m,d=state
    return mask(rot(bits(m),1)), (d-1)%6
def abs_rot(state): return transform_abs(state, lambda s: rot(s,1))
def abs_ref(state): return transform_abs(state, refl)
def set0_bits(s):
    s=list(s); s[0]=1; return tuple(s)
def toggle0_bits(s):
    s=list(s); s[0]^=1; return tuple(s)
def abs_set0(state): return transform_abs(state, set0_bits)
def local_toggle0(state):
    m,d=state
    return mask(toggle0_bits(bits(m))), d

def env_obs_mask(m):
    s=bits(m)
    return (sum(s), sum(s[i]*s[(i+1)%6] for i in range(6)), sum(s[i]*s[(i+3)%6] for i in range(3)))
def obs_aligned(state): return align(state)
def obs_shape(state): return env_obs_mask(align(state))
def idx(state): return state[0]*6+state[1]
def transition(fn): return tuple(idx(fn(s)) for s in STATES)
def packet(fn, effect):
    edges=[]
    for s in STATES:
        target=fn(s)
        edges.append((idx(s),idx(target),1,Affine(eye(6),efffect(s)),1))
    return ControlPacket.from_edges(len(STATES),0,1,edges)

def test_aligned_mask_is_exact_gauge_quotient():
    assert len({obs_aligned(s) for s in STATES})==64
    assert all(obs_aligned(gauge(s))==obs_aligned(s) for s in STATES)
    actions={'G':gauge,'R':abs_rot,'J':abs_ref,'S0':abs_set0}
    assert predictive_block_profile(STATES,actions,obs_aligned,5)==(64,64,64,64,64,64)
    q=stable_predictive_partition(STATES,actions,obs_aligned)
    assert q.block_count==64 and q.stabilization_depth==0

def test_shape_to_aligned_mask_to_local_phase_ladder():
    sym={'G':gauge,'R':abs_rot,'J':abs_ref}
    absolute={**sym,'S0':abs_set0}
    local={**absolute,'L0':local_toggle0}
    assert predictive_block_profile(STATES,sym,obs_shape,5)==(13,13,13,13,13,13)
    assert predictive_block_profile(STATES,absolute,obs_shape,5)==(13,32,52,63,64,64)
    assert predictive_block_profile(STATES,local,obs_shape,5)==(13,113,353,383,384,384)
    assert stable_predictive_partition(STATES,sym,obs_shape).block_count==13
    assert stable_predictive_partition(STATES,absolute,obs_shape).block_count==64
    q=stable_predictive_partition(STATES,local,obs_shape)
    assert q.block_count==384 and q.stabilization_depth==4

def test_effect_valued_phase_offset_boundary():
    # Initial 64-class partition = globally aligned physical mask; local offset is treated as gauge.
    labels=observation_partition(STATES,obs_aligned)
    # Globally framed effect: always translate along global e1. Safe after alignment quotient.
    global_packet=packet(gauge, lambda s:(1,0,0,0,0,0))
    assert certify_control_partition(global_packet,labels)==labels
    assert len(set(refine_control_partition((global_packet,),labels)))==64
    # Local-frame effect: translate along axis indexed by local offset. Same aligned mask but distinct delta diverges.
    local_packet=packet(gauge, lambda s:tuple(1 if i==s[1] else 0 for i in range(6)))
    try:
        certify_control_partition(local_packet,labels)
    except ValueError:
        pass
    else:
        raise AssertionError('local phase-sensitive effect must reject shared-clock quotient')
    assert len(set(refine_control_partition((global_packet,local_packet),labels)))==384
