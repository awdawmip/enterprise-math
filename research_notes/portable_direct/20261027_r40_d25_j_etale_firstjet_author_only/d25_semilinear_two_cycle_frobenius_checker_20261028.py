#!/usr/bin/env python3
"""Exact exhaustive GF(4) two-cycle gauge/Galois orbit certificate.
Uses standard-library integers only; auxiliary finite-field model, not native CM.
"""
import json
from collections import Counter
from datetime import datetime, timezone


def mul(a, b):
    z = 0
    for i in range(2):
        if (b >> i) & 1:
            z ^= a << i
    if z & 4: z ^= 0b111   # x^2 = x + 1 over F2
    return z


def add(a, b): return a ^ b

def sigma(a): return mul(a, a)

def vadd(u, v): return (u[0] ^ v[0], u[1] ^ v[1])

def smul(a, v): return (mul(a, v[0]), mul(a, v[1]))

def apply(M, v): return (mul(M[0], v[0]) ^ mul(M[1], v[1]), mul(M[2], v[0]) ^ mul(M[3], v[1]))

def mmul(A, B): return (mul(A[0],B[0])^mul(A[1],B[2]),mul(A[0],B[1])^mul(A[1],B[3]),mul(A[2],B[0])^mul(A[3],B[2]),mul(A[2],B[1])^mul(A[3],B[3]))

def inv(M):
    det = mul(M[0], M[3]) ^ mul(M[1], M[2])
    if det == 0: raise ValueError("singular")
    idet = next(t for t in range(1,4) if mul(det,t)==1)
    return tuple(mul(idet,x) for x in (M[3],M[1],M[2],M[0]))

VECTORS = tuple((x,y) for x in range(4) for y in range(4))

def subspace(*basis):
    return tuple(sorted({vadd(smul(a,basis[0]) if len(basis)>0 else (0,0), smul(b,basis[1]) if len(basis)>1 else (0,0)) for a in range(4) for b in range(4)}))


def get_subspaces():
    ss = {subspace()}
    ss.update(subspace(v) for v in VECTORS)
    ss.update(subspace(v,w) for v in VECTORS for w in VECTORS)
    assert len(ss) == 7
    return sorted(ss)

SUBSPACES = get_subspaces()
SDIM = {S:{1:0,4:1,16:2}[len(S)] for S in SUBSPACES}
GL = tuple(M for M in __import__('itertools').product(range(4),repeat=4) if (mul(M[0],M[3])^mul(M[1],M[2])) != 0)
assert len(GL) == 180


def rank(M):
    return {1:0,4:1,16:2}[len({apply(M,v) for v in VECTORS})]


def admissible():
    mat = tuple(__import__('itertools').product(range(4),repeat=4))
    return [(S,D,T) for S in SUBSPACES for D in SUBSPACES for T in mat
            if all(apply(T,v)==(0,0) for v in S) and all(apply(T,v) in D for v in VECTORS)]


def core(t):
    S,D,T=t
    return 2-SDIM[S]+SDIM[D]-rank(T)


def conjugate(g,t):
    S,D,T=t
    gi=inv(g)
    return (tuple(sorted(apply(g,v) for v in S)),tuple(sorted(apply(g,v) for v in D)),mmul(mmul(g,T),gi))


def frob(t):
    S,D,T=t
    return (tuple(sorted((sigma(x),sigma(y)) for x,y in S)),tuple(sorted((sigma(x),sigma(y)) for x,y in D)),tuple(map(sigma,T)))


def check():
    assert [sigma(x) for x in range(4)] == [0,1,3,2]
    for a in range(4):
        for b in range(4):
            assert mul(a,b) in range(4)
            assert sigma(mul(a,b)) == mul(sigma(a),sigma(b))
    states=admissible(); stset=set(states)
    assert len(states) == 529
    assert 3 + ((4-1)+(2-1))//2 == 5 # n=1, m=1, q=4
    assert 4 + ((4-1)+(2-1))//2 == 6 # n=1, m>=2, q=4
    assert set(core(x) for x in states)==set(range(5))
    orbit_id={}; orbits=[]; checks=0
    for t in states:
        if t in orbit_id: continue
        orbit={conjugate(g,t) for g in GL}
        assert orbit <= stset
        assert all(core(x)==core(t) for x in orbit)
        idx=len(orbits)
        for x in orbit:
            assert x not in orbit_id
            orbit_id[x]=idx
        orbits.append((core(t),orbit))
        checks+=len(GL)
    assert len(orbit_id)==len(states)
    ordinary=Counter(d for d,orb in orbits)
    assert [ordinary[i] for i in range(5)]==[1,6,27,6,1], ordinary
    galmap=[]
    for d,orb in orbits:
        j=orbit_id[frob(next(iter(orb)))]
        assert orbits[j][0]==d
        assert all(orbit_id[frob(t)]==j for t in orb)
        galmap.append(j)
    assert all(galmap[galmap[i]]==i for i in range(len(orbits)))
    fixed=Counter(orbits[i][0] for i,j in enumerate(galmap) if i==j)
    semilinear=[(ordinary[d]+fixed[d])//2 for d in range(5)]
    assert all((ordinary[d]+fixed[d])%2==0 for d in range(5))
    # Independent direct construction using full GL2(4) x Gal(4/2) orbit action
    directly_seen=set(); direct=Counter(); group_actions=0
    for t in states:
        if t in directly_seen: continue
        orbit={conjugate(g,s) for g in GL for s in (t,frob(t))}
        assert orbit <= stset
        assert all(core(x)==core(t) for x in orbit)
        assert not orbit & directly_seen
        directly_seen.update(orbit); direct[core(t)]+=1
        group_actions+=2*len(GL)
    assert directly_seen==stset
    assert [direct[i] for i in range(5)]==semilinear
    # Signed-orientation p=373 witness in F_373[t]/(t^2-2).
    p=373
    assert pow(2,(p-1)//2,p)==p-1
    assert (p-2)%p==371
    assert (0,1)!=(0,p-1) # witness is t vs -t in (constant,t) coordinates
    out={
       'schema':'EM_AUTHOR_EXACT_GF4_SEMILINEAR_TWO_CYCLE_V1',
       'field':'F_4=F_2[z]/(z^2+z+1)', 'base_field':'F_2',
       'dimensions':'W=F_4^2; V=F_4^m; m>=0',
       'candidate_subspaces':len(SUBSPACES),
       'admissible_triples':len(states),
       'gl2_order':len(GL),
       'ordinary_orbits_by_core_dim':[ordinary[i] for i in range(5)],
       'frobenius_fixed_ordinary_orbits_by_core_dim':[fixed[i] for i in range(5)],
       'semilinear_orbits_by_core_dim':semilinear,
       'ordinary_total':len(orbits), 'semilinear_total':sum(semilinear),
       'ordinary_cumulative_orbits':[sum(ordinary[i] for i in range(min(m,4)+1)) for m in range(7)],
       'semilinear_cumulative_orbits':[sum(semilinear[i] for i in range(min(m,4)+1)) for m in range(7)],
       'explicit_ordinary_action_checks':checks,
       'explicit_semilinear_action_checks':group_actions,
       'p373_frobenius_conjugation':'t -> -t, t^2=2, trace(t)=0, norm(t)=371 mod373',
       'status':'PASS',
       'scope':'AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE'
    }
    return out


if __name__=='__main__':
    print(json.dumps(check(),indent=2,ensure_ascii=False,sort_keys=True))
