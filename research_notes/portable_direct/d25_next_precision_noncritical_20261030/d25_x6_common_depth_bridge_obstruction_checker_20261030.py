#!/usr/bin/env python3
"""Author-side exact integer checks for an X6 affine quotient/transport obstruction.

No claim is made that any of these affine maps is the native Heartbeat update.
All arithmetic is integer/exact; no external packages or randomness.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

N = 6
DELTA = (1,)*N


def I6():
    return tuple(tuple(int(i == j) for j in range(N)) for i in range(N))


def matvec(A, z):
    return tuple(sum(A[i][j]*z[j] for j in range(N)) for i in range(N))


def plus(z, w):
    return tuple(a+b for a,b in zip(z,w))


def rel(z):
    return tuple(z[i]-z[5] for i in range(5))


def gauge(z):
    return (rel(z), z[5])


def ungauge(q, h):
    return tuple(v+h for v in q)+(h,)


def mat_derivation(A, b):
    AD = matvec(A, DELTA)
    C = rel(AD)
    # R(q)=(q1,...,q5,0), D(v)=(v_i-v_6)_{i<6}
    M = tuple(tuple(rel(matvec(A, tuple(int(k==j) for k in range(6))))[i] for j in range(5)) for i in range(5))
    H = tuple(A[5][j] for j in range(5))
    k = AD[5]
    return {"C": C, "M": M, "H": H, "k": k, "Db": rel(b), "b6": b[5]}


def update_qh(D, q, h):
    q2 = tuple(sum(D['M'][i][j]*q[j] for j in range(5))+D['C'][i]*h+D['Db'][i] for i in range(5))
    h2 = sum(D['H'][j]*q[j] for j in range(5))+D['k']*h+D['b6']
    return (q2,h2)


def update(A,b,z):
    return plus(matvec(A,z),b)


def finite_branches(A,b,sources,weights,H):
    # Every source occurrence remains independently weighted, even when states or outputs coincide.
    traces = {}
    for s in sources:
        z = s
        tt = []
        for _ in range(H+1):
            tt.append(rel(z))
            z = update(A,b,z)
        traces[s] = tuple(tt)
    masses = Counter()
    for s in sources:
        masses[traces[s]] += weights[s]
    return masses,traces


def ring_case(p,L,e,d,lam):
    mod=p**L
    units=[x for x in range(mod) if x%p]
    def P(x):return (x+p**e*lam*pow(x,d,mod))%mod
    mapped=[P(x) for x in units]
    assert len(set(mapped))==len(units) and set(mapped)==set(units)
    assert all(P(x)!=x for x in units)
    cycles=[]
    left=set(units)
    while left:
        s=min(left); x=s; c=[]
        while x not in c:
            assert x in left
            c.append(x);left.remove(x)
            x=P(x)
        assert x==s
        cycles.append(len(c))
    # For every nonzero constant integer translation v in Z6, a period m forbids
    # E(P^m(x))=E(x)+m*v by torsion-free cancellation. The checker records m.
    return {"p":p,"L":L,"e":e,"d":d,"lambda":lam,"source_count":len(units),
            "period_spectrum":dict(sorted(Counter(cycles).items())),
            "first_source_1":1,"first_update":P(1)}


def main():
    identity=I6()
    shear=[list(r) for r in identity]
    shear[0][1] += 1
    shear=tuple(tuple(r) for r in shear)
    preserve=[list(r) for r in identity]
    preserve[0][1]+=1; preserve[0][2]-=1
    preserve=tuple(tuple(r) for r in preserve)
    swap=[list(r) for r in identity]
    swap[0],swap[5]=swap[5],swap[0]
    swap=tuple(tuple(r) for r in swap)
    negate=tuple(tuple(-v for v in r) for r in identity)
    cases={"identity":identity,"shear":shear,"balanced_shear":preserve,"swap_first_last":swap,"negation":negate}
    b=(2,-1,0,3,0,-2)
    chart_states=list(itertools.product((-1,0,1), repeat=N))
    chart_count=0; derived_count=0; fiber_pairs=0
    summary={}
    for name,A in cases.items():
        D=mat_derivation(A,b)
        safe=all(x==0 for x in D['C'])
        assert safe == (name!="shear")
        assert ungauge(*gauge((3,-1,2,0,-2,4)))==(3,-1,2,0,-2,4)
        for z in chart_states:
            q,h=gauge(z)
            assert ungauge(q,h)==z
            assert update_qh(D,q,h) == gauge(update(A,b,z))
            derived_count+=1
            # Test one representative within the same q-fiber shifted by nonzero depth.
            for k in (-2,-1,1,2):
                y=plus(z,tuple(k*di for di in DELTA))
                assert rel(z)==rel(y)
                is_same=(rel(update(A,b,z))==rel(update(A,b,y)))
                assert is_same==safe
                fiber_pairs+=1
        summary[name]={"C":list(D['C']),"A_delta":list(matvec(A,DELTA)),
                       "global_relative_quotient_descends":safe,
                       "observed_depth_pair_split":not safe}
        chart_count+=len(chart_states)
    # Source population, weights, exact trajectory-class multiplicity; no Boolean collapse.
    zero=(0,)*6; e1=(1,0,0,0,0,0)
    sources=[zero,DELTA,e1,plus(e1,tuple(2*a for a in DELTA)),tuple(-2*a for a in DELTA)]
    weights=dict(zip(sources,(1,2,3,4,5)))
    assert len(set(sources))==5
    mass_id,tr_id=finite_branches(identity,(0,)*6,sources,weights,3)
    mass_shear,tr_shear=finite_branches(shear,(0,)*6,sources,weights,3)
    id_sorted=sorted(mass_id.values())
    shear_sorted=sorted(mass_shear.values())
    assert id_sorted==[7,8], id_sorted
    assert sum(mass_shear.values())==15
    assert tr_shear[zero]!=tr_shear[DELTA]
    assert tr_id[zero]==tr_id[DELTA]
    # Time-zero fibers are [8,7]; under shear some split at time 1.
    time0=Counter()
    time1=Counter()
    for s in sources:
        time0[tr_shear[s][0]]+=weights[s]
        time1[tr_shear[s][:2]]+=weights[s]
    assert sorted(time0.values())==[7,8]
    assert sorted(time1.values())==[1,2,3,4,5]
    # Check finite modular reversible auxiliary maps: all cycles nontrivial.
    rings=[ring_case(p,L,e,d,lam) for p,L,e,d,lam in
           [(3,3,1,2,1),(5,3,1,2,1),(5,4,2,4,2),(7,3,1,6,3)]]
    for r in rings:
        assert min(map(int,r['period_spectrum']))>1
    out={"schema":"D25_X6_AFFINE_QUOTIENT_OBSTRUCTION_AUTHOR_CHECK_V1",
         "date":"2026-10-30", "status":"PASS", "mode":"EXACT_INTEGER_AUTHOR_ONLY",
         "chart_points_checked_per_map":len(chart_states),"affine_maps":summary,
         "coordinate_reconstruction_checks":derived_count,
         "same_relative_fiber_one_step_pair_checks":fiber_pairs,
         "weighted_source_multiplicity":{"source_occurrences":len(sources),
            "source_total_weight":sum(weights.values()),
            "identity_horizon3_fiber_masses":id_sorted,
            "shear_time0_fiber_masses":sorted(time0.values()),
            "shear_time01_fiber_masses":sorted(time1.values()),
            "shear_horizon3_fiber_masses":shear_sorted},
         "ring_period_checks":rings,
         "scope":"finite illustrations of the algebraic bridge theorem, not an all-X6 native dynamics experiment"}
    target=Path(__file__).with_name("d25_x6_common_depth_bridge_obstruction_author_check_20261030.json")
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":out['status'],"checks":derived_count+fiber_pairs,
                      "weighted_time01":sorted(time1.values()),
                      "ring_cycle_examples":rings},ensure_ascii=False))

if __name__ == '__main__':
    main()
