"""Exact fractions for an affine-observer no-go family in the R5 two-origin stop/continue model.

Author-side test, not native X6 or mathematical admission. See RESEARCH.md for proof.
"""
from fractions import Fraction as F
from itertools import product, permutations

ALPHA = (F(1, 4), F(1, 5))
KAPPA = (F(3, 4), F(1, 6))
KEYS = {'A': (1, F(1)), 'D': (2, F(1, 2)), 'Y': (2, F(3, 2)),
        'C': (2, F(1)), 'DH': (3, F(1, 4)), 'YH': (3, F(2)),
        'L': (3, F(1)), 'L4': (4, F(1))}
assert all((1 + k*(1-2*a))/a == F(11,2) for a,k in zip(ALPHA,KAPPA))


def flow(action):
    """Return positive Q terminal distribution for one deterministic history policy."""
    leaves = {k:F(0) for k in KEYS}
    def put(key,mass):
        leaves[key]+=mass
    for i, (a,k) in enumerate(zip(ALPHA,KAPPA)):
        origin=F(1,2)
        if action(i,'A') == 0:
            put('A',origin)
            continue
        d=y=origin*a; c=origin*(1-2*a)
        if action(i,'D'):
            put('DH',d*F(2,3))
            put('L4' if action(i,'LD') else 'L',d*F(1,3))
        else:put('D',d)
        if action(i,'Y'):
            put('YH',y*F(1,2))
            put('L4' if action(i,'LY') else 'L',y*F(1,2))
        else:put('Y',y)
        put('C',c*(1-k))
        put('L4' if action(i,'LC') else 'L',c*k)
    assert sum(leaves.values())==F(1)
    assert sum((q*KEYS[t][1] for t,q in leaves.items()),F(0))==F(1)
    assert all(q>=0 for q in leaves.values())
    return leaves


def full_policy(bits):
    names=('A','D','Y','LD','LY','LC')
    acts=[dict(zip(names,bits[i*6:(i+1)*6])) for i in (0,1)]
    return flow(lambda i,key:acts[i][key])


def lr_policy(bits):
    acts=dict(zip(('A','D','Y','L'),bits))
    return flow(lambda i,key:acts['L' if key in ('LD','LY','LC') else key])


def observe(leaves,v,w):
    r={k:F(1,2) for k in KEYS};r['DH']+=v;r['L4']+=w
    assert all(0<=x<=1 for x in r.values())
    features=({k:KEYS[k][1]*r[k] for k in KEYS},r,
              {k:KEYS[k][1]*KEYS[k][0] for k in KEYS},
              {k:KEYS[k][0] for k in KEYS})
    return tuple(sum((q*feat[k] for k,q in leaves.items()),F(0)) for feat in features)


def dot(h,x):return sum((a*b for a,b in zip(h,x)),F(0))


def det(mat):
    total=F(0)
    for p in permutations(range(4)):
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        total+=sign*__import__('functools').reduce(lambda a,b:a*b,(mat[i][p[i]] for i in range(4)),F(1))
    return total


full_flows=[full_policy(bits) for bits in product((0,1),repeat=12)]
lr_flows=[lr_policy(bits) for bits in product((0,1),repeat=4)]
assert len(full_flows)==4096 and len(lr_flows)==16
base_v,base_w=F(1,8),F(1,4)
base_h=(F(10),F(9),F(1),-F(2))
base_full_obs=[observe(f,base_v,base_w) for f in full_flows]
base_lr_obs=[observe(f,base_v,base_w) for f in lr_flows]
assert max(map(lambda o:dot(base_h,o),base_full_obs))==F(1685,192)
assert max(map(lambda o:dot(base_h,o),base_lr_obs))==F(2759,320)
assert F(1685,192)-F(2759,320)==F(37,240)

policies=[(0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0)]
for v,w in [(F(1,8),F(1,4)),(F(1,100),F(1,100)),
            (-F(1,6),F(1,5)),(F(2,5),-F(1,7)),(-F(1,8),-F(1,4))]:
    # The invertible change of the two error coordinates transports the base support direction.
    p=F(19,3)/w - F(23,12)/v
    q=F(23,12)/v - F(19,12)/w
    h=(p,q,F(1),-F(2))
    constant=(p+q-F(19))/2
    current_full=[observe(f,v,w) for f in full_flows]
    current_lr=[observe(f,v,w) for f in lr_flows]
    for f,o0,o in zip(full_flows,base_full_obs,current_full):
        assert dot(h,o)==dot(base_h,o0)+constant
    for f,o0,o in zip(lr_flows,base_lr_obs,current_lr):
        assert dot(h,o)==dot(base_h,o0)+constant
    fullsup=max(dot(h,x) for x in current_full)
    lrsup=max(dot(h,x) for x in current_lr)
    assert fullsup-lrsup==F(37,240)
    pts=[observe(lr_policy(bits),v,w) for bits in policies]
    matrix=[[pts[i+1][j]-pts[0][j] for j in range(4)] for i in range(4)]
    determinant=det(matrix)
    assert determinant==F(152361,40960000)*v*w
    # Base witness is origin0 continue, origin1 stop, all downstream continue.
    witness=observe(flow(lambda i,k: (i==0) if k=='A' else True),v,w)
    assert dot(h,witness)==fullsup
    print(f'v={v} w={w} H=({p},{q},1,-2) gap={fullsup-lrsup} '
          f'rank_det={determinant} witness_inf_dist>={(fullsup-lrsup)/sum(abs(x) for x in h)}')

for v,w in [(F(0),F(1,4)),(F(1,8),F(0)),(F(0),F(0))]:
    obs=[observe(f,v,w) for f in full_flows]
    if v==0: assert all(x[0]==x[1] for x in obs)
    if w==0: assert all(x[0]-F(1,2)==(x[1]-F(1,2))/4 for x in obs)
    print(f'BORDER v={v} w={w}: affine-rank <=3 by exact observer identity')
print('PASS_EXACT_R5_AFFINE_RESPONSE_TWO_PARAMETER_GLOBAL_NO_GO')
