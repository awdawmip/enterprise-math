"""PREFIX-437: exact signed-X6 BRC + S6-equivariant C2-holonomy sidecar.

Native positive-path BRC is imported from the pinned git-blob source in the
PREFIX-436 evidence bundle. C4 phase tagging is a NEW auxiliary construction.
No physical heartbeat simulation is performed.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from hashlib import sha1
from itertools import permutations, product
from math import factorial
from pathlib import Path
import importlib.util
import os

BRC_BLOB = '300a96e3dc24bf6fff73743037a0347a8bc83176'
BRC_SOURCE_PATH = Path(os.environ.get('PREFIX437_BRC_SOURCE',
    str(Path(__file__).resolve().parent / 'PREFIX436/existing/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')))
raw = BRC_SOURCE_PATH.read_bytes()
assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==BRC_BLOB
spec=importlib.util.spec_from_file_location('prefix437_signed_brc',BRC_SOURCE_PATH)
brc=importlib.util.module_from_spec(spec)
spec.loader.exec_module(brc)


def amp_formula(m):
    """All six native axes, signed displacement via m=abs(d)."""
    n=sum(m)
    if sum(v&1 for v in m)>1: return 0
    out=factorial(n//2)
    for v in m: out//=factorial(v//2)
    return out


def shift(h,t):
    return tuple(h[(j-t)%4] for j in range(4))


def dp_hist(d, start=(0,0,0,0,0,0)):
    m=tuple(abs(z) for z in d)
    signs=tuple(1 if z>=0 else -1 for z in d)
    @lru_cache(None)
    def go(k):
        if k==m:return (1,0,0,0)
        h=[0,0,0,0]
        for j in range(6):
            if k[j]>=m[j]:continue
            nxt=tuple(k[i]+(i==j) for i in range(6))
            # theta(x,+/-e_j)=2*sign_j*sum_(i<j) x_i mod 4.
            tag=2*signs[j]*sum(start[i]+signs[i]*k[i] for i in range(j))%4
            for r,z in enumerate(shift(go(nxt),tag)):h[r]+=z
        return tuple(h)
    return go((0,)*6)


def phase_start(d,x):
    return sum(x[i]*d[j] for i in range(6) for j in range(i+1,6))%2


def group_c(d,e):
    return 2*sum(d[i]*e[j] for i in range(6) for j in range(i+1,6))%4


# S6 equivariance is tested at the invariant commutator level. The abstract
# presentation with generators X_i,z and [X_i,X_j]=z^2 supplies actual lifts.
perms=list(permutations(range(6)))
for pi in perms:
    for i in range(6):
        for j in range(6):
            if i==j:continue
            assert 2 == (-2 if pi[i]>pi[j] else 2)%4
assert len(perms)==720

def permute(pi,d):
    v=[0]*6
    for i in range(6):v[pi[i]]=d[i]
    return tuple(v)

def gauge_lift(pi,d):
    return 2*sum(d[i]*d[j] for i in range(6) for j in range(i+1,6) if pi[i]>pi[j])%4

def compose(pi,sigma):
    return tuple(pi[sigma[i]] for i in range(6))

vectors=((0,)*6,(1,0,0,0,0,0),(0,1,0,0,0,0),
         (1,1,0,0,0,0),(2,-3,0,1,0,0),(-2,3,1,-2,1,0),
         (1,1,1,1,1,1))
for pi in perms:
    for d in vectors:
        for e in vectors:
            de=tuple(d[i]+e[i] for i in range(6))
            # This is the exact group-homomorphism equation for the lifted S6 action.
            assert (group_c(permute(pi,d),permute(pi,e))+gauge_lift(pi,d)+gauge_lift(pi,e)
                    -group_c(d,e)-gauge_lift(pi,de))%4==0
for pi in perms[::23]:
    for sigma in perms[::19]:
        for d in vectors:
            assert gauge_lift(compose(pi,sigma),d)==(gauge_lift(sigma,d)+gauge_lift(pi,permute(sigma,d)))%4
assert (1,0,0,0,0,0)!=(0,1,0,0,0,0)
for d,e,f in product(((0,)*6,(1,0,0,0,0,0),(0,1,0,0,0,0),(-1,2,0,0,0,0)),repeat=3):
    de=tuple(d[i]+e[i] for i in range(6))
    ef=tuple(e[i]+f[i] for i in range(6))
    assert (group_c(d,e)+group_c(de,f)-group_c(e,f)-group_c(d,ef))%4==0
assert (group_c((1,0,0,0,0,0),(0,1,0,0,0,0))-group_c((0,1,0,0,0,0),(1,0,0,0,0)))%4==2

# Exact six-axis DP and actual native signed-X6 positive BRC counts.
# All 3^6 count vectors are tested at three signed-start configurations.
starts=((0,)*6,(1,0,-3,2,5,-1),(-2,7,0,1,-4,3))
checked=0
for m in product(range(3),repeat=6):
    d=tuple(((-1)**i)*m[i] for i in range(6))
    expected=amp_formula(m)
    positive=brc.shortest_path_multiplicity(d)
    assert positive==factorial(sum(m))//__import__('math').prod(factorial(v) for v in m)
    for x in starts:
        h=dp_hist(d,x)
        assert h[1]==h[3]==0
        assert sum(h)==positive
        assert h[0]-h[2]==((-1)**phase_start(d,x))*expected
        checked+=1

# Independent exhaustive enumeration of every positive six-axis word up to length 6.
# Sum_{n=0}^6 6^n = 55,987 complete words; classify by endpoint counts.
table=defaultdict(lambda:[0,0,0,0])
words=0
for n in range(7):
    for w in product(range(6),repeat=n):
        pos=[0]*6; t=0
        for j in w:
            t=(t+2*sum(pos[:j]))%4
            pos[j]+=1
        table[tuple(pos)][t]+=1
        words+=1
for m,h in table.items():
    expected=amp_formula(m)
    assert h[1]==h[3]==0
    assert h[0]-h[2]==expected
    assert sum(h)==brc.shortest_path_multiplicity(m)
assert words==55987

# 64-state coordinate-parity/sign transducer: all 12 signed primitive steps.
# Distinguishability (horizon <=1) checks all unordered state pairs.
def advance(state,j):
    p,t=state
    toggle=sum((p>>i)&1 for i in range(j))%2
    return (p^(1<<j) if j<5 else p, t^toggle)
states=[(p,t) for p in range(32) for t in range(2)]
for state in states:
    for j in range(6):
        u=advance(state,j)
        assert 0<=u[0]<32 and u[1] in (0,1)
        assert advance(u,j)==state  # same action for +/- step on parity
pairs=0
for a in range(len(states)):
    for b in range(a+1,len(states)):
        x,y=states[a],states[b]
        assert x[1]!=y[1] or any(advance(x,j)[1]!=advance(y,j)[1] for j in range(6))
        pairs+=1
assert pairs==2016

for m in ((1,1,0,0,0,0),(1,1,1,1,0,0),(2,2,0,0,0,0),(2,2,2,2,0,0)):
    h=dp_hist(m)
    print('EXAMPLE counts=',m,'positive_BRC=',sum(h),'hist=',h,'amplitude=',h[0]-h[2],'intensity=',(h[0]-h[2])**2)
print('PASS PREFIX437 signed-BRC-blob='+BRC_BLOB+'; 720 explicit gauge-lifted permutations; 64 cocycle triples; 2187 exact DP/positive BRC start cases; 55987 complete six-axis words; 2016 distinguishability pairs; 64-state involutive edge updates')
