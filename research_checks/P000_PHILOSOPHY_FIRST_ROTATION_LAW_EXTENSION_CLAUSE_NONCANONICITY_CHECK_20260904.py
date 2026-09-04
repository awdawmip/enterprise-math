#!/usr/bin/env python3
"""Exact finite checker for P000 Philosophy-First Q31.

The checker audits only the declared finite extension-clause language on the
frozen Q29 comparison scaffold.  It does not promote the scaffold, any
coordinate permutation, or EXP_d to native P000 structure.
"""

from collections import Counter
from itertools import permutations, product

ID = tuple(range(6))
X = tuple(product((0, 1), repeat=6))
ZERO = (0, 0, 0, 0, 0, 0)

# Candidate-blind witness universe: independent coordinate permutations on the
# two frozen three-coordinate blocks.  This is a finite comparison universe,
# not a P000 axiom or a classification of all future rotation laws.
BLOCK = tuple(permutations(range(3)))
LAWS = tuple(tuple(a) + tuple(3 + i for i in b) for a in BLOCK for b in BLOCK)


def compose(p, q):
    """Coordinate action p after q for act(p,x)[i] = x[p[i]]."""
    return tuple(q[p[i]] for i in range(6))


def power(p, n):
    out = ID
    for _ in range(n):
        out = compose(p, out)
    return out


def law_order(p):
    for n in range(1, 7):
        if power(p, n) == ID:
            return n
    raise AssertionError("law order does not divide frozen token period 6")


def act(p, x):
    return tuple(x[p[i]] for i in range(6))


def fixed_states(p):
    return sum(act(p, x) == x for x in X)


def observation(x):
    return x[:3]


def slice_fibre_constant(p):
    seen = {}
    for x in X:
        key = observation(x)
        value = observation(act(p, x))
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return len(seen) == 8


def representation_image(p):
    # T=<r | r^7=r> has normal forms e,r,...,r^6.  Because every witness
    # generator has order dividing 6, the state-map image is <p>.
    return tuple(dict.fromkeys(power(p, t) for t in range(7)))


def exp_clause(p, d):
    """EXP_d: every h in Im(rho) satisfies h^d=id."""
    return all(power(h, d) == ID for h in representation_image(p))


def conjugate(c, p):
    c_inv = next(q for q in LAWS if compose(c, q) == ID and compose(q, c) == ID)
    return compose(c, compose(p, c_inv))


def main():
    assert len(LAWS) == 36
    assert len(set(LAWS)) == 36

    # Every witness is a legal Q29-style active equivalence comparison law.
    for p in LAWS:
        assert len(set(act(p, x) for x in X)) == 64
        assert act(p, ZERO) == ZERO
        assert slice_fibre_constant(p)
        assert power(p, 7) == p

    orders = Counter(law_order(p) for p in LAWS)
    assert orders == Counter({1: 1, 2: 15, 3: 8, 6: 12})

    fixed_hist = Counter((law_order(p), fixed_states(p)) for p in LAWS)
    assert fixed_hist == Counter({
        (1, 64): 1,
        (2, 16): 9,
        (2, 32): 6,
        (3, 4): 4,
        (3, 16): 4,
        (6, 8): 12,
    })

    # The declared divisor-exponent atom family is generated from divisors of
    # the frozen token period 6 rather than from names/action tables of targets.
    divisors = (1, 2, 3, 6)
    truth = {d: tuple(p for p in LAWS if exp_clause(p, d)) for d in divisors}
    assert {d: len(v) for d, v in truth.items()} == {1: 1, 2: 16, 3: 9, 6: 36}

    E2 = (1, 0, 2, 4, 3, 5)
    E3 = (1, 2, 0, 4, 5, 3)
    E6 = (1, 0, 2, 4, 5, 3)
    assert E2 in LAWS and E3 in LAWS and E6 in LAWS
    assert (law_order(E2), fixed_states(E2)) == (2, 16)
    assert (law_order(E3), fixed_states(E3)) == (3, 4)
    assert (law_order(E6), fixed_states(E6)) == (6, 8)

    # Parent-pair discrimination.
    assert exp_clause(E2, 2) and not exp_clause(E2, 3)
    assert exp_clause(E3, 3) and not exp_clause(E3, 2)

    # Incomparability and non-complementarity.
    assert not set(truth[2]).issubset(set(truth[3]))  # E2 witness
    assert not set(truth[3]).issubset(set(truth[2]))  # E3 witness
    assert not exp_clause(E6, 2) and not exp_clause(E6, 3)
    assert len(set(truth[2]) & set(truth[3])) == 1
    assert sum((not exp_clause(p, 2)) and (not exp_clause(p, 3)) for p in LAWS) == 12

    # On nontrivial active witnesses the two retained families are disjoint.
    nontrivial = tuple(p for p in LAWS if p != ID)
    exp2_nontrivial = tuple(p for p in nontrivial if exp_clause(p, 2))
    exp3_nontrivial = tuple(p for p in nontrivial if exp_clause(p, 3))
    assert len(exp2_nontrivial) == 15
    assert len(exp3_nontrivial) == 8
    assert set(exp2_nontrivial).isdisjoint(exp3_nontrivial)

    # Complete the declared positive-conjunctive language L_wedge generated
    # by the four divisor atoms.  Clauses are semantically equivalent exactly
    # when they have the same truth set on this structurally defined universe.
    formulas = []
    for mask in range(1 << len(divisors)):
        atoms = tuple(d for i, d in enumerate(divisors) if (mask >> i) & 1)
        truth_set = frozenset(
            p for p in LAWS if all(exp_clause(p, d) for d in atoms)
        )
        formulas.append((atoms, truth_set))

    semantic_classes = {}
    for atoms, truth_set in formulas:
        semantic_classes.setdefault(truth_set, []).append(atoms)
    assert len(formulas) == 16
    assert len(semantic_classes) == 4
    assert sorted(len(k) for k in semantic_classes) == [1, 9, 16, 36]

    # Exactly two semantic classes discriminate the decisive Q29 pair.  Their
    # one-atom minimal representatives are EXP_2 and EXP_3.
    discriminator_classes = {
        truth_set
        for truth_set in semantic_classes
        if ((E2 in truth_set) != (E3 in truth_set))
    }
    assert len(discriminator_classes) == 2
    assert frozenset(truth[2]) in discriminator_classes
    assert frozenset(truth[3]) in discriminator_classes
    assert semantic_classes[frozenset(truth[2])] == [(2,), (2, 6)]
    assert semantic_classes[frozenset(truth[3])] == [(3,), (3, 6)]

    # Deletion-minimality: deleting the sole atom from each minimal
    # representative gives the empty conjunction, which admits both E2/E3.
    empty_truth = next(ts for atoms, ts in formulas if atoms == ())
    assert E2 in empty_truth and E3 in empty_truth
    assert len((2,)) == 1 and len((3,)) == 1

    # Typed-law equivalence invariance: EXP_d is invariant under every
    # block-preserving conjugacy available in the witness universe.
    conjugacy_checks = 0
    for c in LAWS:
        for p in LAWS:
            q = conjugate(c, p)
            assert q in LAWS
            for d in divisors:
                assert exp_clause(p, d) == exp_clause(q, d)
                conjugacy_checks += 1
    assert conjugacy_checks == 36 * 36 * 4

    print(
        "PASS P000_Q31_ROTATION_EXTENSION_NONCANONICITY "
        "laws=36 nontrivial=35 order1=1 order2=15 order3=8 order6=12 "
        "exp1=1 exp2=16 exp3=9 exp6=36 "
        "exp2_nontrivial=15 exp3_nontrivial=8 intersection=1 neither=12 "
        "e2=EXP2_NOT_EXP3 e3=EXP3_NOT_EXP2 e6=NEITHER "
        "formulas=16 semantic_classes=4 minimal_parent_discriminators=2 "
        "conjugacy_checks=5184 "
        "terminal=NO_CANONICAL_MINIMAL_ROTATION_EXTENSION_CLAUSE_ON_DECLARED_LANGUAGE"
    )


if __name__ == "__main__":
    main()
