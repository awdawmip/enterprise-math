#!/usr/bin/env python3
"""Exact, reproducible tests; select --backend pinned or repository explicitly."""
from __future__ import annotations
import argparse
from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations, product, permutations
import json
from pathlib import Path
import random
import factor_atoms as fa


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", required=True, choices=("pinned", "repository"))
    parser.add_argument("--output", default="verification.json")
    args = parser.parse_args()
    fa.select_backend(args.backend)
    if args.backend == "pinned":
        import pinned_resultant_kernel as rg
    else:
        import brc_newton_resultant_event_generator_check as rg
    from atom_events import event_guard, specialize
    K = fa.K
    one = fa.ONE
    def poly(*c): return tuple(Q(x) for x in c)
    def linear(r): return (-Q(r), Q(1))
    def mul(*fs):
        ans = one
        for f in fs: ans = K._p_mul(ans, f)
        return ans
    def expand(fs, ws=None):
        ws = tuple(1 for _ in fs) if ws is None else tuple(ws)
        return mul(*(fa.ppow(f, w) for f, w in zip(fs, ws)))
    def mobius(fs, l, r):
        total = terms = 0
        for size in range(1, len(fs) + 1):
            for indices in combinations(range(len(fs)), size):
                g = fs[indices[0]]
                for i in indices[1:]: g = K._p_gcd(g, fs[i])
                total += (-1 if size % 2 == 0 else 1) * fa.root_count(g, l, r)
                terms += 1
        return total, terms
    def direct_multiplicity(f, l, r):
        # Reuse the predecessor's independent successive-derivative gcd oracle.
        total = fa.root_count(f, l, r)
        common = derivative = f
        for _ in range(1, len(f) - 1):
            derivative = K._p_derivative(derivative)
            common = K._p_gcd(common, derivative)
            if len(common) <= 1: break
            total += fa.root_count(common, l, r)
        return total
    def check_cert(fs):
        c = fa.compile_atoms(fs)
        assert fa.verify_certificate(fs, c)
        assert len(c.atoms) <= c.total_input_degree
        assert c.refinement_gcd_calls <= c.squarefree_layers * c.total_input_degree
        return c
    out = {"status": "PASS", "backend": fa.BACKEND,
           "source_commit": "dc86d1d26a1374fc15cfb85c8db10f8bfbef849b",
           "full_package_or_CI_executed": args.backend == "repository"}
    # Baseline library and intervals are inherited from #1238, not new data.
    x, a, b, c = (linear(r) for r in (0, 1, 2, 3))
    library = (mul(x, a), mul(x, b), mul(x, c), mul(a, b),
               poly(-2, 0, 1), poly(1, 0, 1), poly(-1, -1, 1), linear(-1), linear(Q(5, 2)))
    intervals = ((Q(-2), Q(4)), (Q(0), Q(2)), (Q(-1,2), Q(3,2)),
                 (Q(1), Q(3)), (Q(-3,2), Q(1,2)))
    baseline_samples = baseline_terms = activation_queries = 0
    for size in range(1, 5):
        for fs in combinations(library, size):
            cert = check_cert(fs)
            expanded = expand(fs)
            for l, r in intervals:
                counts = fa.atom_counts(cert, l, r)
                observed = fa.observe(cert, counts, (1,) * size)
                actual = fa.root_count(expanded, l, r)
                mt, terms = mobius(fs, l, r)
                assert observed[1] == actual == mt
                assert observed[2] == sum(fa.root_count(f, l, r) for f in fs)
                assert fa.failing_factors(cert, counts) == tuple(i for i, f in enumerate(fs) if fa.root_count(f, l, r))
                baseline_samples += 1
                baseline_terms += terms
                # All deletion/activation contexts, with expanded Sturm oracle.
                for ws in product((0, 1), repeat=size):
                    assert fa.observe(cert, counts, ws)[1] == fa.root_count(expand(fs, ws), l, r)
                    activation_queries += 1
    out.update(baseline_interval_samples=baseline_samples, old_mobius_subset_terms=baseline_terms,
               activation_queries=activation_queries)
    # Independent known-root catalog: exact interval counts are supplied by hand.
    primitives = (linear(-1), x, a, poly(-2,0,1), poly(1,0,1))
    known_intervals = ((-2, 2), (0, 1), (1, 2), (-2, 0), (0, 2))
    primitive_counts = ((1,1,1,2,0), (0,0,0,0,0), (0,0,0,1,0),
                        (1,0,0,1,0), (0,0,1,1,0))
    rng = random.Random(0x6F42A1)
    random_queries = permutation_checks = 0
    max_atoms = 0
    for trial in range(100):
        n = rng.randrange(1, 5)
        profiles = tuple(tuple(rng.randrange(3) for _ in range(n)) for _ in primitives)
        fs = tuple(K._p_scale(mul(*(fa.ppow(p, v[i]) for p, v in zip(primitives, profiles))),
                             Q((-1) ** i * (i + 1), i + 2)) for i in range(n))
        cert = check_cert(fs)
        max_atoms = max(max_atoms, len(cert.atoms))
        expected_atoms = {}
        for p, v in zip(primitives, profiles):
            if any(v): expected_atoms[v] = mul(expected_atoms.get(v, one), p)
        assert {a.profile: a.polynomial for a in cert.atoms} == expected_atoms
        for (l, r), native_counts in zip(known_intervals, primitive_counts):
            counts = fa.atom_counts(cert, l, r)
            for _ in range(4):
                ws = tuple(rng.randrange(3) for _ in range(n))
                powers = [sum(w*v for w,v in zip(ws, vs)) for vs in profiles]
                distinct = sum(q for q,e in zip(native_counts,powers) if e)
                multiplicity = sum(q*e for q,e in zip(native_counts,powers))
                assert fa.observe(cert, counts, ws) == (distinct == 0, distinct, multiplicity)
                random_queries += 1
            # Reconstruct the complete support histogram from all activation queries.
            hist = fa.support_histogram(cert, counts)
            full = (1 << n) - 1
            union = {mask: fa.observe(cert, counts, tuple(int(bool(mask & (1<<i))) for i in range(n)))[1]
                     for mask in range(1 << n)}
            subset_mass = {mask: union[full] - union[full ^ mask] for mask in range(1 << n)}
            for mask in range(1, 1 << n):
                recovered = sum((-1)**(mask.bit_count()-s.bit_count()) * subset_mass[s]
                                for s in range(1 << n) if s & mask == s)
                assert recovered == hist.get(mask, 0)
        order = tuple(reversed(range(n)))
        rev = check_cert(tuple(fs[i] for i in order))
        reverse_atoms = {tuple(a.profile[i] for i in order): a.polynomial for a in rev.atoms}
        assert reverse_atoms == {a.profile: a.polynomial for a in cert.atoms}
        permutation_checks += 1
    out.update(known_root_weighted_queries=random_queries, factor_permutation_checks=permutation_checks,
               support_histogram_inversions=100*len(known_intervals), maximum_random_atoms=max_atoms)
    # Repeated/coincident factors, with an independent derivative-chain multiplicity check.
    multiplicity_checks = 0
    for i, j in product(range(1, 4), repeat=2):
        fs = (mul(fa.ppow(x, i), fa.ppow(a, j)),
              mul(fa.ppow(x, j), fa.ppow(a, i)), poly(-3))
        cert = check_cert(fs)
        for ws in ((1,1,1), (2,1,0), (0,2,1)):
            for l,r in ((-1,2), (0,2), (-1,1)):
                counts = fa.atom_counts(cert,l,r)
                observed = fa.observe(cert,counts,ws)
                assert observed[2] == direct_multiplicity(expand(fs,ws),l,r)
                multiplicity_checks += 1
    out["independent_multiplicity_checks"] = multiplicity_checks
    # Observer counterexamples: final counts and singleton counts are insufficient.
    fsA = (mul(x,a), mul(x,b), mul(a,b))
    fsB = (mul(x,a), mul(x,b), mul(x,b))
    ca, cb = check_cert(fsA), check_cert(fsB)
    na, nb = fa.atom_counts(ca,-1,3), fa.atom_counts(cb,-1,3)
    assert fa.observe(ca,na,(1,1,1))[1] == fa.observe(cb,nb,(1,1,1))[1] == 3
    assert all(fa.root_count(f,-1,3) == 2 for f in fsA+fsB)
    assert fa.observe(ca,na,(0,1,1))[1] == 3
    assert fa.observe(cb,nb,(0,1,1))[1] == 2
    # Fixed-I support-count equivalence cannot survive a new factor insertion.
    assert fa.root_count(x,-1,2) == fa.root_count(a,-1,2) == 1
    assert fa.root_count(mul(x,x),-1,2) == 1
    assert fa.root_count(mul(a,x),-1,2) == 2
    val = check_cert((mul(x,fa.ppow(a,2)),mul(fa.ppow(x,2),a)))
    assert {v.profile for v in val.atoms} == {(1,2),(2,1)}
    out["observer_boundary_witnesses"] = 3
    # Full valuation profiles need not be minimal for a restricted count lease.
    ma = check_cert((mul(x,fa.ppow(a,3)),mul(fa.ppow(x,3),a)))
    mb = check_cert((mul(fa.ppow(x,2),fa.ppow(a,2)),)*2)
    qa,qb = fa.atom_counts(ma,-1,2),fa.atom_counts(mb,-1,2)
    assert len(ma.atoms) == 2 and len(mb.atoms) == 1
    assert fa.minimal_count_signature(ma,qa) == fa.minimal_count_signature(mb,qb)
    for ws in product(range(4),repeat=2):
        assert fa.observe(ma,qa,ws) == fa.observe(mb,qb,ws)
    assert fa.observe(ma,fa.atom_counts(ma,-1,Q(1,2)),(1,0))[2] != fa.observe(mb,fa.atom_counts(mb,-1,Q(1,2)),(1,0))[2]
    out["strict_observer_signature_coarsening_queries"] = 16
    # Functorial monomial transport, independent fresh-gcd compiler comparison.
    transport_checks = associativity_checks = 0
    for trial in range(60):
        fs = tuple(rng.choice(library[:5]) for _ in range(3))
        cert = check_cert(fs)
        counts = fa.atom_counts(cert,-2,4)
        B = tuple(tuple(rng.randrange(2) for _ in fs) for _ in range(2))
        C = tuple(tuple(rng.randrange(2) for _ in B) for _ in range(2))
        hs = tuple(expand(fs,column) for column in B)
        pushed,pc = fa.monomial_pushforward(cert,B,counts)
        fresh = check_cert(hs)
        assert pushed.atoms == fresh.atoms and pushed.scalars == fresh.scalars
        assert fa.verify_certificate(hs,pushed)
        assert pc == fa.atom_counts(fresh,-2,4)
        transport_checks += 1
        twice,tc = fa.monomial_pushforward(pushed,C,pc)
        BC = tuple(tuple(sum(B[j][i]*column[j] for j in range(len(B))) for i in range(len(fs))) for column in C)
        once,oc = fa.monomial_pushforward(cert,BC,counts)
        assert (twice.atoms,twice.scalars,tc) == (once.atoms,once.scalars,oc)
        for ws in product((0,1,2),repeat=2):
            assert fa.observe(twice,tc,ws) == fa.observe(once,oc,ws)
        associativity_checks += 1
    # Include empty source/target and total deletion in the transport contract.
    for fs,cols in (((),((),())), ((x,a),()), ((x,a),((0,0),))):
        source = check_cert(fs)
        carried,_ = fa.monomial_pushforward(source,cols)
        assert fa.verify_certificate(tuple(expand(fs,col) for col in cols),carried)
        transport_checks += 1
    out.update(monomial_transport_checks=transport_checks,monomial_associativity_checks=associativity_checks)
    # High-factor-count compression: no subset oracle is invoked here.
    fs = tuple((mul(x,a),mul(x,b),mul(a,b))[i % 3] for i in range(80))
    large = check_cert(fs)
    assert len(large.atoms) == 3
    assert fa.observe(large,fa.atom_counts(large,-1,3),(1,)*80)[1] == 3
    out["large_factor_witness"] = {"factor_count":80,"input_degree":160,"atom_count":3,
        "refinement_gcd_calls":large.refinement_gcd_calls,
        "avoided_nonempty_subsets": str((1<<80)-1), "subset_oracle_run":False}
    # Permanent shared factor: old cross resultant is identically zero.
    xt = ((Q(0),Q(-1)),rg.ONE)
    xm1 = ((Q(-1),),rg.ONE)
    xp1 = ((Q(1),),rg.ONE)
    F1,F2 = rg.x_mul(xt,xm1),rg.x_mul(xt,xp1)
    assert rg.sylvester_resultant(F1,F2) == rg.ZERO
    guard, slots = event_guard((xt,xm1,xp1),-2,2,rg)
    assert guard == poly(4,0,-5,0,1)
    param_queries = 0
    for raw in range(-12,13):
        t = Q(raw,4)
        fs = (specialize(F1,t,rg),specialize(F2,t,rg))
        cert = check_cert(fs)
        counts = fa.atom_counts(cert,-2,2)
        expected = len({z for z in (t,Q(-1),Q(1)) if -2<z<2})
        assert fa.observe(cert,counts,(1,1))[1] == expected
        if rg.t_eval(guard,t):
            assert len(cert.atoms) == 3
            assert {a.profile for a in cert.atoms} == {(1,0),(0,1),(1,1)}
        for ws in product((0,1,2),repeat=2):
            assert fa.observe(cert,counts,ws)[1] == fa.root_count(expand(fs,ws),-2,2)
            assert fa.observe(cert,counts,ws)[2] == direct_multiplicity(expand(fs,ws),-2,2)
            param_queries += 1
    out["parameter_guard"] = {"ascending_coefficients":[4,0,-5,0,1],"resultant_endpoint_slots":slots,
                              "parameter_specializations":25,"weighted_observer_queries":param_queries,
                              "old_cross_resultant":"IDENTICALLY_ZERO"}
    # Hard refusal and corruption tests.
    refusals = corruptions = 0
    def refuses(fn):
        nonlocal refusals
        try: fn()
        except (ValueError,TypeError): refusals += 1; return
        raise AssertionError("invalid input unexpectedly accepted")
    for fs in (((0,),), ((),), ((0.5,1),), ((True,1),)):
        refuses(lambda fs=fs: fa.compile_atoms(fs))
    empty = check_cert(())
    assert fa.observe(empty,fa.atom_counts(empty,-1,1),()) == (True,0,0)
    constant = check_cert((poly(-2),poly(3)))
    assert not constant.atoms
    refuses(lambda: fa.atom_counts(empty,1,0))
    refuses(lambda: fa.atom_counts(empty,0.1,1))
    refuses(lambda: fa.observe(ca,na,(1,-1,0)))
    refuses(lambda: fa.monomial_pushforward(ca,((1,-1,0),)))
    refuses(lambda: fa.monomial_pushforward(ca,((1,0),)))
    refuses(lambda: event_guard((xt,xt),-2,2,rg))
    refuses(lambda: event_guard((rg.x_mul(xt,xt),),-2,2,rg))
    refuses(lambda: event_guard((xp1,),-1,2,rg))
    original = check_cert((mul(x,a),mul(x,b)))
    alterations = (
        replace(original,scalars=(Q(2),Q(1))),
        replace(original,atoms=original.atoms[:-1]),
        replace(original,atoms=original.atoms+(original.atoms[0],)),
        replace(original,atoms=(replace(original.atoms[0],profile=(0,0)),)+original.atoms[1:]),
        replace(original,atoms=(replace(original.atoms[0],polynomial=fa.ppow(original.atoms[0].polynomial,2)),)+original.atoms[1:]),
    )
    for damaged in alterations:
        assert not fa.verify_certificate((mul(x,a),mul(x,b)),damaged)
        corruptions += 1
    out.update(invalid_input_refusals=refusals,corrupt_certificate_refusals=corruptions)
    output = Path(args.output)
    output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__ == "__main__":
    main()
