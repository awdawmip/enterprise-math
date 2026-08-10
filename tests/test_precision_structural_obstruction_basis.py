import unittest

from enterprise_math.precision_structural_obstruction_basis import (
    blocker_duality_holds,
    canonical_cut_kill_identity,
    carrier_bases_from_cuts,
    joint_adequacy_cuts,
    minimal_adequate_instruction_sets,
    minimal_failure_cuts,
    minimal_transversals,
    sperner_cut_bound,
)


def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0]))


def block_map(P):
    return {x: i for i, B in enumerate(P) for x in B}


def stable_unary(P, f):
    bm = block_map(P)
    for B in P:
        if len({bm[f[x]] for x in B}) != 1:
            return False
    return True


def refine_once(P, funcs):
    bm = block_map(P)
    out = []
    for B in P:
        groups = {}
        for x in B:
            sig = (bm[x],) + tuple(bm[f[x]] for f in funcs)
            groups.setdefault(sig, []).append(x)
        out.extend(groups.values())
    return canon(out)


def compile_unary(P0, funcs):
    P = P0
    while True:
        Q = refine_once(P, funcs)
        if Q == P:
            return P
        P = Q


def transformation_closure(gens, size):
    identity = tuple(range(size))
    closure = {identity, *gens}
    changed = True
    while changed:
        changed = False
        cur = tuple(closure)
        for a in cur:
            for b in cur:
                c = tuple(a[b[x]] for x in range(size))
                if c not in closure:
                    closure.add(c)
                    changed = True
    return closure


class StructuralObstructionBasisTests(unittest.TestCase):
    def test_minimal_cut_has_exact_canonical_kill_set(self):
        # 4-state operation ping-pong witness from Supplement 14.
        f = (0, 0, 0, 1)
        g = (0, 0, 3, 0)
        generators = ("f", "g")
        fmap = {"f": f, "g": g}
        P0 = canon([{0, 2, 3}, {1}])
        full = compile_unary(P0, [f, g])

        def compile_retained(retained):
            return compile_unary(P0, [fmap[name] for name in generators if name in retained])

        def adequate(retained):
            return compile_retained(retained) == full

        cuts = minimal_failure_cuts(generators, adequate)
        self.assertEqual(set(cuts), {frozenset({"f"}), frozenset({"g"})})
        for cut in cuts:
            self.assertTrue(
                canonical_cut_kill_identity(
                    generators,
                    cut,
                    compile_retained,
                    lambda name, world: stable_unary(world, fmap[name]),
                )
            )

    def test_carrier_bases_are_minimal_transversals(self):
        generators = (0, 1, 2)
        cuts = (frozenset({0, 1}), frozenset({1, 2}))
        bases = carrier_bases_from_cuts(generators, cuts)
        self.assertEqual(
            set(bases),
            {frozenset({1}), frozenset({0, 2})},
        )
        self.assertTrue(blocker_duality_holds(generators, cuts))

    def test_joint_cuts_are_minimal_union_of_carrier_and_semantic_cuts(self):
        # P0 = {{0,2},{1}}. g1 is carrier-essential; g2 is additionally
        # semantic-essential on the final discrete quotient.
        g0 = (0, 0, 0)
        g1 = (0, 0, 1)
        g2 = (0, 0, 2)
        funcs = (g0, g1, g2)
        generators = (0, 1, 2)
        P0 = canon([{0, 2}, {1}])
        Q = compile_unary(P0, funcs)
        self.assertEqual(Q, canon([{0}, {1}, {2}]))
        required = set(funcs)

        def carrier_ok(retained):
            return compile_unary(P0, [funcs[i] for i in generators if i in retained]) == Q

        def semantic_ok(retained):
            closure = transformation_closure(
                [funcs[i] for i in generators if i in retained], 3
            )
            return required.issubset(closure)

        carrier_cuts = minimal_failure_cuts(generators, carrier_ok)
        semantic_cuts = minimal_failure_cuts(generators, semantic_ok)
        joint = joint_adequacy_cuts(generators, carrier_ok, semantic_ok)
        bases = minimal_adequate_instruction_sets(generators, carrier_ok, semantic_ok)

        self.assertEqual(set(carrier_cuts), {frozenset({1})})
        self.assertEqual(set(semantic_cuts), {frozenset({1}), frozenset({2})})
        self.assertEqual(set(joint), {frozenset({1}), frozenset({2})})
        self.assertEqual(set(bases), {frozenset({1, 2})})

    def test_empty_or_dominated_cut_handling(self):
        generators = (0, 1, 2)
        cuts = (frozenset({0}), frozenset({0, 1}), frozenset({2}))
        bases = minimal_transversals(generators, cuts)
        self.assertEqual(set(bases), {frozenset({0, 2})})

    def test_sperner_antichain_bound(self):
        self.assertEqual(sperner_cut_bound(0), 1)
        self.assertEqual(sperner_cut_bound(1), 1)
        self.assertEqual(sperner_cut_bound(4), 6)
        self.assertEqual(sperner_cut_bound(6), 20)


if __name__ == "__main__":
    unittest.main()
