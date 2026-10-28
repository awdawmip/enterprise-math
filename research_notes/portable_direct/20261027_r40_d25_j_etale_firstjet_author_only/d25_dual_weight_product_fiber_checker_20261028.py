#!/usr/bin/env python3
"""Author-side exact enumeration for dual-weight two-arrow cyclic-gauge fibers.

Uses the already-published, pure-integer finite-field Field implementation in
this same evidence directory. Mathematical claims are separately proved in the
companion note. The checker enumerates actual ordered pairs and group actions.
"""
from collections import Counter, defaultdict
from math import gcd
from d25_restricted_gauge_galois_descent_checker_20261028 import Field
import json


def case(p, e, d):
    F = Field(p, e)
    q = F.q
    assert (q - 1) % d == 0
    H = tuple(z for z in range(1, q) if F.power(z, d) == 1)
    assert len(H) == d
    inv = {z: F.power(z, q - 2) for z in H}
    # Explicitly enumerate every two-arrow state and its H-orbit.
    unseen = {(x, y) for x in range(q) for y in range(q)}
    orbits = []
    full_gauge_actions = 0
    while unseen:
        x, y = min(unseen)
        orb = {(F.mul(z, x), F.mul(inv[z], y)) for z in H}
        full_gauge_actions += len(H)
        assert len(orb) == (d if (x, y) != (0, 0) else 1)
        assert orb <= unseen
        unseen.difference_update(orb)
        orbits.append((min(orb), orb))
    assert len(orbits) == 1 + (q*q - 1)//d

    def coset(z):
        return min(F.mul(u, z) for u in H)

    def tag(x, y):
        c = F.mul(x, y)
        if c:
            return ('both', c, coset(x))
        if x:
            return ('X_only', 0, coset(x))
        if y:
            return ('Y_only', 0, coset(y))
        return ('zero', 0, 0)

    # Completeness: tags are orbit-constant and distinguish ALL H-orbits.
    orbit_tags = []
    for rep, orb in orbits:
        assert all(tag(*v) == tag(*rep) for v in orb)
        orbit_tags.append(tag(*rep))
    assert len(set(orbit_tags)) == len(orbits)
    # Compare the (smaller) complete GL1×GL1 quotient, which forgets
    # the multiplicative source coset but retains the directed zero branches.
    def full_gauge_tag(x, y):
        c = F.mul(x, y)
        if c:
            return ('both', c)
        if x:
            return ('X_only', 0)
        if y:
            return ('Y_only', 0)
        return ('zero', 0)
    full_counts = Counter(full_gauge_tag(*rep) for rep, _ in orbits)
    assert len(full_counts) == q+2
    assert full_counts[('zero', 0)] == 1
    assert full_counts[('X_only', 0)] == (q-1)//d
    assert full_counts[('Y_only', 0)] == (q-1)//d
    assert all(full_counts[('both', c)] == (q-1)//d for c in range(1, q))
    assert len(orbits)-(q+2) == (q+1)*((q-1)//d-1)
    # Independently check the full nonzero and zero product fiber counts.
    fiber_counts = Counter(F.mul(*rep) for rep, _ in orbits)
    assert fiber_counts[0] == 1 + 2*(q-1)//d
    assert all(fiber_counts[c] == (q-1)//d for c in range(1, q))

    fixed_results = []
    Frobenius = [[F.power(z, p**j) for z in range(q)] for j in range(e)]
    for j in range(e):
        g = gcd(e, j)
        q0 = p**g
        t = gcd(d, q0-1)
        S = (q-1)//(q0-1)
        h = gcd(d, S)
        h1 = h*t//d
        assert h*t % d == 0
        M = (q-1)//d
        a = gcd(M, p**j-1)
        b = (q0-1)//t
        assert a == h1*b
        fixed_c = defaultdict(list)
        base_c = Counter()
        obstruction_by_c = defaultdict(lambda: Counter())
        coboundaries = {F.mul(F.power(z, p**j), inv[z]) for z in H}
        assert len(coboundaries) == d//t
        for rep, orb in orbits:
            x, y = rep
            c = F.mul(x, y)
            is_fixed = (Frobenius[j][x], Frobenius[j][y]) in orb
            if not is_fixed:
                continue
            fixed_c[c].append(rep)
            # Exact base-field representative test, not a proxy from c.
            base = any(Frobenius[j][u] == u and Frobenius[j][v] == v
                       for u, v in orb)
            if base:
                base_c[c] += 1
            if rep == (0, 0):
                assert base
                continue
            if x:
                zeta = F.mul(Frobenius[j][x], F.power(x, q-2))
            else:
                zeta = F.mul(y, F.power(Frobenius[j][y], q-2))
            assert zeta in H
            if x and y:
                assert F.mul(Frobenius[j][y], F.power(y,q-2)) == inv[zeta]
            cocycle_class = min(F.mul(zeta, u) for u in coboundaries)
            trivial_class = min(coboundaries)
            assert base == (cocycle_class == trivial_class)
            branch = 'both' if c else ('X_only' if x else 'Y_only')
            obstruction_by_c[(c,branch)][cocycle_class] += 1
        # Every original composite-product c in the fixed subfield has
        # a uniform Frobenius-fixed coset count. No other product can occur.
        for c in range(q):
            if Frobenius[j][c] == c:
                expected = 1+2*a if c == 0 else a
                expected_base = 1+2*b if c == 0 else b
                assert len(fixed_c[c]) == expected, (p,e,d,j,c,len(fixed_c[c]),expected)
                assert base_c[c] == expected_base
                if c:
                    assert len(obstruction_by_c[(c,'both')]) == h1
                    assert set(obstruction_by_c[(c,'both')].values()) == {b}
                else:
                    for branch in ('X_only','Y_only'):
                        assert len(obstruction_by_c[(0,branch)]) == h1
                        assert set(obstruction_by_c[(0,branch)].values()) == {b}
            else:
                assert c not in fixed_c
                assert base_c[c] == 0
        observed_fixed = sum(len(x) for x in fixed_c.values())
        observed_base = sum(base_c.values())
        expected_fixed = 1+(q0+1)*a
        expected_base = 1+(q0+1)*b
        assert observed_fixed == expected_fixed
        assert observed_base == expected_base
        assert observed_fixed-observed_base == (q0*q0-1)*(h1-1)//t
        fixed_results.append({
            'j':j,'g':g,'fixed_subfield_size':q0,'gauge_H0_size':t,
            'norm_kernel_intersection_size':h,'h1_obstruction_size':h1,
            'fixed_cosets_per_nonzero_product':a,
            'base_representable_cosets_per_nonzero_product':b,
            'zero_product_fixed_orbits':1+2*a,
            'zero_product_base_representable_orbits':1+2*b,
            'all_fixed_orbits':observed_fixed,
            'all_base_representable_orbits':observed_base,
            'non_descent_fixed_orbits':observed_fixed-observed_base,
        })
    assert sum(row['all_fixed_orbits'] for row in fixed_results) % e == 0
    # Independent traversal of sigma cycles on exact orbit tags.
    representative_by_tag = {tag(*rep):rep for rep, _ in orbits}
    unseen_tags = set(representative_by_tag)
    semilinear_cycles = 0
    while unseen_tags:
        start = min(unseen_tags)
        cur = start
        cycle = []
        while cur in unseen_tags:
            unseen_tags.remove(cur)
            cycle.append(cur)
            x, y = representative_by_tag[cur]
            cur = tag(F.power(x,p), F.power(y,p))
        assert cur == start
        assert len(cycle) <= e
        semilinear_cycles += 1
    assert semilinear_cycles == sum(row['all_fixed_orbits'] for row in fixed_results)//e
    return {'p':p,'e':e,'d':d,'q':q,'modulus':list(F.modulus),
            'raw_pairs_exhaustively_visited':q*q,
            'group_actions_used_to_construct_orbits':full_gauge_actions,
            'H_orbits':len(orbits),'full_GL1xGL1_orbits':q+2,
            'lost_orbit_distinctions_under_full_gauge':len(orbits)-(q+2),
            'group_cosets':(q-1)//d,
            'frobenius':fixed_results,
            'semilinear_orbits_by_Burnside':sum(row['all_fixed_orbits'] for row in fixed_results)//e,
            'semilinear_orbits_by_direct_cycle_traversal':semilinear_cycles,
            'pass':True}


def main():
    configs=[(2,2,3),(2,3,7),(2,4,3),(2,4,5),(2,4,15),
             (3,1,2),(3,2,2),(3,2,4),(3,2,8),(3,3,2),(3,3,13),
             (3,4,10),(3,4,20),(5,2,2),(5,2,6),(5,2,12),(5,2,24),
             (7,2,8),(7,2,48)]
    rows=[case(*config) for config in configs]
    p=373
    q=p*p
    d=p+1
    M=(q-1)//d
    t=gcd(d,p-1)
    assert t==2 and M==p-1
    assert pow(2,(p-1)//2,p)==p-1  # irreducible t^2=2
    assert pow((-2)%p,(p-1)//2,p)==p-1  # Norm(t)=-2 nonsquare
    a=gcd(M,p-1)
    b=(p-1)//t
    assert a==p-1 and b==(p-1)//2
    analytic={
       'p':p,'e':2,'d':d,'field':'F_373[t]/(t^2-2)',
       'Frobenius':'t -> -t','gauge_action':'(x,y)->(z*x,z^(-1)*y)',
       'gauge_H':'norm-one mu_374',
       'all_orbits_over_extension':1+(q*q-1)//d,
       'all_Frobenius_fixed_orbits':1+(p+1)*a,
       'base_representable_fixed_orbits':1+(p+1)*b,
       'non_descent_fixed_orbits':(p+1)*(a-b),
       'per_nonzero_base_product_fixed_orbits':a,
       'per_nonzero_base_product_representable_orbits':b,
       'per_nonzero_base_product_nondescend':a-b,
       'zero_product_fixed_orbits':1+2*a,
       'zero_product_representable_orbits':1+2*b,
       'zero_product_nondescend':2*(a-b),
       'source_example':'(t,t) with product 2 and Norm(t)=-2 nonsquare',
       'base_example':'(1,2) with product 2 and Norm(1)=1 square',
       'total_semilinear_orbits':(1+(q*q-1)//d+1+(p+1)*a)//2,
       'scope':'exact closed-form and mod-p Legendre check; no p373 full-state enumeration'
    }
    assert analytic['non_descent_fixed_orbits']==analytic['all_Frobenius_fixed_orbits']-analytic['base_representable_fixed_orbits']
    out={'title':'dual-weight two-arrow composite-product fiber and Galois descent refinement',
         'status':'AUTHOR_DERIVED_AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE',
         'method':'integer-exact finite-field enumeration of all two-arrow source states and H actions; independent orbit tags, fixed fibers, base representative and cocycle checks',
         'cases':rows,
         'total_raw_states':sum(v['raw_pairs_exhaustively_visited'] for v in rows),
         'total_explicit_H_actions':sum(v['group_actions_used_to_construct_orbits'] for v in rows),
         'analytical_p373':analytic,
         'all_checks_pass':True}
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
