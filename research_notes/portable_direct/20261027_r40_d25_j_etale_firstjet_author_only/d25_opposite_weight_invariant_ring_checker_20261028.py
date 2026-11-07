#!/usr/bin/env python3
"""Author-side exact finite checks for opposite-weight cyclic gauge invariants.

No native CM/H0/B0 inputs, network, packages, or random sampling.
"""
from __future__ import annotations

import json
from pathlib import Path


def prime_field_check(p: int, d: int) -> dict:
    assert (p - 1) % d == 0 and d >= 2
    h = [z for z in range(1, p) if pow(z, d, p) == 1]
    assert len(h) == d
    generator = next(z for z in h if len({pow(z, a, p) for a in range(d)}) == d)
    unseen = {(x, y) for x in range(p) for y in range(p)}
    observed_keys = set()
    orbit_count = 0
    while unseen:
        x, y = min(unseen)
        orbit = {(z*x % p, pow(z, p - 2, p)*y % p) for z in h}
        assert orbit <= unseen
        keys = {(a*b % p, pow(a, d, p), pow(b, d, p)) for a, b in orbit}
        assert len(keys) == 1
        key = next(iter(keys))
        assert key not in observed_keys
        observed_keys.add(key)
        unseen -= orbit
        orbit_count += 1
    assert orbit_count == 1 + (p*p - 1)//d
    assert len(observed_keys) == orbit_count
    # Test invariance of *every monomial* below total degree d against a
    # generator acting on every field point; coefficients could not cancel
    # distinct characters because p does not divide d.
    tested_monomials = 0
    nonbalanced_invariant = 0
    monomial_point_evaluations = 0
    for degree in range(d):
        for a in range(degree + 1):
            b = degree-a
            mismatch_count = sum(
                (pow(x,a,p)*pow(y,b,p) -
                 pow(generator*x % p,a,p)*pow(pow(generator,p-2,p)*y % p,b,p)) % p != 0
                for x in range(p) for y in range(p)
            )
            is_invariant = mismatch_count == 0
            monomial_point_evaluations += p*p
            assert is_invariant == ((a-b) % d == 0)
            if is_invariant and a != b:
                nonbalanced_invariant += 1
            tested_monomials += 1
    assert nonbalanced_invariant == 0
    # Degree d invariants separate zero-product oriented branches.
    assert pow(1,d,p) != pow(0,d,p)
    # Every nonzero-product coset has a witness if there are multiple H cosets.
    nonzero_phase_witness = None
    if (p-1)//d > 1:
        z = next(a for a in range(1,p) if a not in h)
        assert (1*1)%p == (z*pow(z,p-2,p))%p
        assert pow(z,d,p) != 1
        nonzero_phase_witness = [[1,1],[z,pow(z,p-2,p)]]
    return {
        "p":p,"d":d,"group_order":len(h),"source_states":p*p,
        "orbits":orbit_count,"invariant_keys":len(observed_keys),
        "monomials_below_d_tested":tested_monomials,
        "monomial_point_evaluations":monomial_point_evaluations,
        "nonbalanced_invariants_below_d":nonbalanced_invariant,
        "nonzero_phase_witness":nonzero_phase_witness,
    }


def extension_check(p: int) -> dict:
    assert p % 2 == 1
    delta = next(z for z in range(2,p) if pow(z,(p-1)//2,p) == p-1)
    zero=(0,0);one=(1,0)
    def mul(z,w):
        a,b=z;c,d=w
        return ((a*c+delta*b*d)%p,(a*d+b*c)%p)
    def conjugate(z): return z[0],(-z[1])%p
    def norm(z): return mul(z,conjugate(z))[0]
    def inv(z):
        n=norm(z)
        assert n!=0
        t=pow(n,p-2,p)
        a,b=conjugate(z)
        return a*t%p,b*t%p
    field = [(a,b) for a in range(p) for b in range(p)]
    h=[z for z in field if norm(z)==1]
    assert len(h)==p+1
    unseen={(x,y) for x in field for y in field}
    keys=set(); total=0;fixed=0;base_rep=0
    while unseen:
        x,y=min(unseen)
        orbit={(mul(z,x),mul(inv(z),y)) for z in h}
        assert orbit <= unseen
        kset={(mul(a,b),norm(a),norm(b)) for a,b in orbit}
        assert len(kset)==1
        k=next(iter(kset))
        assert k not in keys
        keys.add(k)
        if (conjugate(x),conjugate(y)) in orbit:
            fixed+=1
        if any(a[1]==0 and b[1]==0 for a,b in orbit):
            base_rep+=1
        assert k[1]*k[2]%p==norm(k[0])
        unseen-=orbit
        total+=1
    q=p*p
    assert total == 1+(q*q-1)//(p+1)
    assert fixed == q
    assert base_rep == (q+1)//2
    return {
        "p":p,"extension":"F_(p^2)=F_p[t]/(t^2-delta)",
        "delta":delta,"field_cardinality":q,"norm_one_group_order":len(h),
        "ordered_states":q*q,"orbits":total,"fixed_Frobenius_orbits":fixed,
        "orbits_with_base_rep":base_rep,"fixed_without_base_rep":fixed-base_rep,
    }


def main():
    prime_configs=[(5,2),(5,4),(7,2),(7,3),(7,6),(11,2),(11,5),
                   (13,2),(13,3),(13,4),(13,6),(19,2),(19,3),(19,6)]
    primes=[prime_field_check(p,d) for p,d in prime_configs]
    ext=[extension_check(p) for p in [3,5,7]]
    p=373
    assert p%8==5 and pow(2,(p-1)//2,p)==p-1
    assert pow((-2)%p,(p-1)//2,p)==p-1
    d=p+1;q=p*p
    large={"p":p,"delta":2,"norm_one_order":d,"q":q,
           "minimal_polynomial_separating_degree":d,
           "frobenius_fixed_orbits":q,
           "fixed_orbits_with_base_rep":(q+1)//2,
           "fixed_without_base_rep":(q-1)//2,
           "t_pair_product":2,"t_pair_norm_x":p-2,
           "t_pair_has_base_rep":False,
           "large_case_method":"exact formulas and Legendre-symbol modular exponentiation, not exhaustive enumeration"}
    result={
        "status":"PASS","kind":"AUTHOR_EXACT_CHECK_ONLY_NOT_NATIVE",
        "subject":"opposite-weight invariant ring and sharp polynomial observer degree",
        "prime_cases":primes,"quadratic_extension_cases":ext,"p373_formula_case":large,
        "total_prime_state_checks":sum(v["source_states"] for v in primes),
        "total_quadratic_extension_ordered_states":sum(v["ordered_states"] for v in ext),
        "total_sub_d_monomial_tests":sum(v["monomials_below_d_tested"] for v in primes),
        "total_monomial_point_evaluations":sum(v["monomial_point_evaluations"] for v in primes),
        "limits":"Universal invariant-ring statement is proved algebraically; checks are exact finite samples only."
    }
    out=Path(__file__).with_name("d25_opposite_weight_invariant_ring_author_check_20261028.json")
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ("prime_cases","quadratic_extension_cases")},indent=2))

if __name__=="__main__": main()
