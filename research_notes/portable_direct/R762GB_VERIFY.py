#!/usr/bin/env python3
"""R762GB, exact finite S6/K4 S4/marked S3 signed-orbit marginal checker."""
import itertools as it
import json
from collections import Counter
from math import comb

AXES=tuple(range(6))
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}

def c3(c):
    c=tuple(c)
    j=c.index(min(c))
    return c[j:]+c[:j]

def cycles(triples):
    return sorted(set(c3(z) for t in triples for z in (t,(t[0],t[2],t[1]))))

def all_triples():
    return list(it.combinations(AXES,3))

def stars():
    return [tuple(i for i,e in enumerate(EDGES) if v in e) for v in range(4)]

def k4_group():
    out=[]
    for q in it.permutations(range(4)):
        out.append(tuple(EDGE_INDEX[tuple(sorted((q[u],q[v])))] for u,v in EDGES))
    return out

def states(C):
    return {(c,signs) for c in C for signs in it.product((-1,1),repeat=3)}

def transport(y,p):
    c,signs=y
    d={p[i]:s for i,s in zip(c,signs)}
    t=c3(tuple(p[i] for i in c))
    return (t,tuple(d[i] for i in t))

def make_orbits(Y,G):
    remain=set(Y)
    out=[]
    while remain:
        x=next(iter(remain))
        orb={transport(x,p) for p in G}
        assert orb.issubset(Y), 'group action not closed'
        out.append(orb)
        remain-=orb
    return sorted(out,key=lambda o:(len(o), sorted(o)[0]))

def audit(name,C,G,expected_orbit_sizes):
    X=set(C)
    Y=states(C)
    O=make_orbits(Y,G)
    assert sorted(len(o) for o in O)==sorted(expected_orbit_sizes)
    assert len(set.union(*O))==len(Y)==8*len(X)
    orbit_fibres=[]
    for orb in O:
        count=Counter(x[0] for x in orb)
        assert set(count)==X
        assert len(set(count.values()))==1
        orbit_fibres.append(next(iter(count.values())))
    masks=0
    for mask in range(1,1<<len(O)):
        permitted=set().union(*(O[i] for i in range(len(O)) if mask&(1<<i)))
        F=Counter(x[0] for x in permitted)
        assert set(F)==X and len(set(F.values()))==1
        assert len(permitted)==len(X)*F[next(iter(X))]
        masks+=1
    return {
        'group':name,'cycles':len(X),'signed_states':len(Y),
        'group_order':len(G),'orbits':len(O),'orbit_sizes':sorted(len(o) for o in O),
        'orbit_fibre_sizes_per_oriented_cycle':sorted(orbit_fibres),
        'nonempty_invariant_boolean_gates_exhausted':masks,
        'all_masks_have_exact_uniform_oriented_marginal':True,
    }

def main():
    S6=list(it.permutations(range(6)))
    K4=k4_group()
    ST=stars()
    MARKED=[s for i,s in enumerate(ST) if i!=0]
    Ex=set(ST[0])
    K3=[p for p in K4 if {p[i] for i in Ex}==Ex]
    assert len(K4)==24 and len(K3)==6
    res=[
        audit('S6-full',cycles(all_triples()),S6,[40,120,120,40]),
        audit('K4-fixed-frame-S4',cycles(ST),K4,[8,24,24,8]),
        audit('K4-marked-three-STAR-S3',cycles(MARKED),K3,[6]*8),
    ]
    fullC=set(cycles(all_triples()))
    frames={frozenset(tuple(sorted(p[i] for i in s)) for s in ST) for p in S6}
    assert len(frames)==30
    fcount=Counter(c for F in frames for c in cycles(sorted(F)))
    assert set(fcount)==fullC and set(fcount.values())=={6}
    marked=set()
    for F in frames:
        for excluded in F:
            marked.add((F,excluded))
    assert len(marked)==120
    mcount=Counter(c for F,excluded in marked for c in cycles(sorted(F-{excluded})))
    assert set(mcount)==fullC and set(mcount.values())=={18}
    # Candidate signed-coordinate update counterexample (not native permission).
    g=(0,1,2)
    i=g[0]
    z={j:int(j==i) for j in AXES}
    def signed_step(y):
        c,s=y
        d={k:0 for k in AXES}
        for j,v in z.items():
            d[c[(c.index(j)+1)%3] if j in c else j] = v
        for j,sign in zip(c,s):d[j]*=sign
        return tuple(d[j] for j in AXES)
    target=g[1]
    s=tuple(-1 if j==target else 1 for j in g)
    plus=signed_step((g,(1,1,1)))
    minus=signed_step((g,s))
    assert plus!=minus
    out={
        'schema':'R762GB_SIGNED_GATE_MARGINAL_AUDIT_V1','status':'PASS',
        'precision':'INTEGER_EXACT','groups':res,
        'frame_count':len(frames),'frame_cycles_per_orientation':6,
        'marked_frame_count':len(marked),'marked_cycles_per_orientation':18,
        'counterexample':{'oriented_cycle':g,'input_cell':z,'all_plus_output':plus,
          'one_output_sign_flipped':minus,'scope':'candidate signed permutation map, not proven native Cell/Link/Port permission'},
        'mathematical_scope':'fixed independent invariant one-step gates and weights on signed BRC labels; projection discards signs, retains g; repeated independent steps use same kernel',
        'review':'NOT_REVIEWED'
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
