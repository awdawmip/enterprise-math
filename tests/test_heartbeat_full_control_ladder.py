from itertools import product
from enterprise_math.brc_control_port import ControlPacket, refine_control_partition, certify_control_partition
from enterprise_math.brc_transport import Affine, eye
from enterprise_math.predictive_quotient import observation_partition

STATES=tuple(product(range(4),range(64),range(6))) # residue, local mask, local phase offset

def bits(m): return tuple((m>>i)&1 for i in range(6))
def mask(s): return sum(v<<i for i,v in enumerate(s))
def rot(s,k=1): k%=6; return s[k:]+s[:k]
def refl(s): return tuple(s[(-i)%6] for i in range(6))
def align(m,d): return mask(rot(bits(m),d))
def localize(a,d): return mask(rot(bits(a),-d))
def env_obs(m):
    s=bits(m)
    return (sum(s),sum(s[i]*s[(i+1)%6] for i in range(6)),sum(s[i]*s[(i+3)%6] for i in range(3)))
def rgroup(r): return 0 if r in (0,3) else 1
def obs(st):
    r,m,d=st; return rgroup(r),env_obs(align(m,d))
def idx(st):
    r,m,d=st; return (r*64+m)*6+d

def transform_abs(st,fn):
    r,m,d=st; a=mask(fn(bits(align(m,d)))); return (r,localize(a,d),d)
def gauge(st):
    r,m,d=st; return (r,mask(rot(bits(m))), (d-1)%6)
def absrot(st): return transform_abs(st,lambda s:rot(s))
def absref(st): return transform_abs(st,refl)
def set0(s): s=list(s);s[0]=1;return tuple(s)
def absset0(st): return transform_abs(st,set0)
def toggle0(s): s=list(s);s[0]^=1;return tuple(s)
def localtoggle(st):
    r,m,d=st; return (r,mask(toggle0(bits(m))),d)
FM={0:1,1:0,2:3,3:2}
def micro(st):
    r,m,d=st; return (FM[r],m,d)

def packet(fn,effect):
    return ControlPacket.from_edges(len(STATES),0,1,(
        (idx(s),idx(fn(s)),1,Affine(eye(6),effect(s)),1) for s in STATES))

INITIAL=observation_partition(STATES,obs)
SAFE=packet(gauge,lambda s:((4 if rgroup(s[0])==0 else -4)*(1+(sum(bits(align(s[1],s[2])))%2)),0,0,0,0,0))
MICRO=packet(micro,lambda s:((1 if s[0] in (0,2) else -1),0,0,0,0,0))
ABS=packet(absset0,lambda s:(bits(align(s[1],s[2]))[0],0,0,0,0,0))
LOCAL=packet(localtoggle,lambda s:tuple(1 if i==s[2] else 0 for i in range(6)))
ROT=packet(absrot,lambda s:(0,0,0,0,0,0))
REF=packet(absref,lambda s:(0,0,0,0,0,0))

def classes(*packets): return len(set(refine_control_partition(packets,INITIAL)))

def test_full_typed_repair_ladder():
    assert len(set(INITIAL))==26
    assert classes(SAFE,ROT,REF)==26
    assert classes(SAFE,ROT,REF,MICRO)==52
    assert classes(SAFE,ROT,REF,ABS)==128
    assert classes(SAFE,ROT,REF,LOCAL)==768
    assert classes(SAFE,ROT,REF,MICRO,ABS)==256
    assert classes(SAFE,ROT,REF,MICRO,LOCAL)==1536

def test_external_clock_does_not_multiply_state_when_effect_is_global():
    GLOBAL=packet(gauge,lambda s:(1,0,0,0,0,0))
    aligned_labels=observation_partition(STATES,lambda s:(rgroup(s[0]),align(s[1],s[2])))
    assert len(set(aligned_labels))==128
    assert certify_control_partition(GLOBAL,aligned_labels)==aligned_labels
    local_axis=packet(gauge,lambda s:tuple(1 if i==s[2] else 0 for i in range(6)))
    try: certify_control_partition(local_axis,aligned_labels)
    except ValueError: pass
    else: raise AssertionError('local phase access must split the external-clock quotient')
    assert len(set(refine_control_partition((GLOBAL,local_axis),aligned_labels)))==768
