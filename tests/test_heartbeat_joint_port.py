from itertools import product
from fractions import Fraction as Q
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition, refine_control_partition
from enterprise_math.brc_transport import Affine, eye

STATES=tuple(product(range(4),range(64)))
def idx(r,m): return 64*r+m
def bits(m): return tuple((m>>i)&1 for i in range(6))
def mask(s): return sum(v<<i for i,v in enumerate(s))
def rot(s): return s[1:]+s[:1]
def set0(s): return (1,)+s[1:]
def env_obs(s): return (sum(s),sum(s[i]*s[(i+1)%6] for i in range(6)),sum(s[i]*s[(i+3)%6] for i in range(3)))
def rgroup(r): return 0 if r in (0,3) else 1
_env_ids={}
ENV_LABEL=[]
for m in range(64):
    o=env_obs(bits(m)); _env_ids.setdefault(o,len(_env_ids)); ENV_LABEL.append(_env_ids[o])
INITIAL=tuple(rgroup(r)*13+ENV_LABEL[m] for r,m in STATES)

def packet(trans,effect):
    edges=[]
    for r,m in STATES:
        rr,mm=trans(r,m)
        edges.append((idx(r,m),idx(rr,mm),1,Affine(eye(6),(effect(r,m),0,0,0,0,0)),1))
    return ControlPacket.from_edges(256,0,1,edges)

SAFE=packet(lambda r,m:(r,mask(rot(bits(m)))), lambda r,m:(4 if rgroup(r)==0 else -4)*(1+(sum(bits(m))%2)))
MICRO=packet(lambda r,m:({0:1,1:0,2:3,3:2}[r],m), lambda r,m:1 if r%2==0 else -1)
PHASE=packet(lambda r,m:(r,mask(set0(bits(m)))), lambda r,m:bits(m)[0])

def test_joint_class_ladder():
    assert len(set(INITIAL))==26
    assert certify_control_partition(SAFE,INITIAL)==INITIAL
    assert len(set(refine_control_partition((SAFE,),INITIAL)))==26
    assert len(set(refine_control_partition((SAFE,MICRO),INITIAL)))==52
    assert len(set(refine_control_partition((SAFE,PHASE),INITIAL)))==128
    assert len(set(refine_control_partition((SAFE,MICRO,PHASE),INITIAL)))==256

def effect(r,m): return (4 if rgroup(r)==0 else -4)*(1+(sum(bits(m))%2))
def test_same_marginals_different_joint_coupling():
    empty=0; one=1
    A=[(0,empty,Q(1,2)),(1,one,Q(1,2))]
    B=[(0,one,Q(1,2)),(1,empty,Q(1,2))]
    assert sorted((r,w) for r,m,w in A)==sorted((r,w) for r,m,w in B)
    assert sorted((m,w) for r,m,w in A)==sorted((m,w) for r,m,w in B)
    meanA=sum(w*effect(r,m) for r,m,w in A)
    meanB=sum(w*effect(r,m) for r,m,w in B)
    assert meanA==-2 and meanB==2

def test_factor_sizes_explain_safe_ladder():
    assert len(_env_ids)==13
    assert 2*13==26 and 4*13==52 and 2*64==128 and 4*64==256
