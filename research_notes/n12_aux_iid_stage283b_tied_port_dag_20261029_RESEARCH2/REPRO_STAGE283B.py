#!/usr/bin/env python3
"""Stage283-B: independent exact ordered-history replay of the tied-port DAG.

All quantities are positive source masses or rational gate action probabilities.
No floating point arithmetic or imported research packages.
"""
from fractions import Fraction as F
from itertools import product

SOURCES = {
    "P": (F(1, 8), F(1, 24), F(5, 6)),
    "Q": (F(1, 12), F(1, 12), F(5, 6)),
}
TERMINAL = ("T0", "T1", "T2", "T3")


def enumerate_ordered(source, x, y):
    """List terminal (source, symbol, ordered-port-actions, exact probability) paths.

    States: initial symbol sigma, merged X, first use Y1, second use Y2.
    Action value 0 stops; 1 continues. Both Y visits use the same y but
    draw independent Bernoulli outcomes conditional on y.
    """
    assert F(0) <= x <= F(1) and F(0) <= y <= F(1)
    assert sum(SOURCES[source]) == F(1)
    paths = []

    def emit(s, hist, prob, term):
        paths.append((source, s, hist, prob, term))

    def walk(symbol, node, hist, mass):
        if node == "X":
            for action, prob in ((0, 1-x), (1, x)):
                if action == 0:
                    emit(symbol, hist+("X0",), mass*prob, "T0")
                else:
                    walk(symbol, "Y1", hist+("X1",), mass*prob)
        elif node == "Y1":
            for action, prob in ((0, 1-y), (1, y)):
                if action == 0:
                    emit(symbol, hist+("Y1_0",), mass*prob, "T1")
                else:
                    walk(symbol, "Y2", hist+("Y1_1",), mass*prob)
        elif node == "Y2":
            for action, prob in ((0, 1-y), (1, y)):
                emit(symbol, hist+(f"Y2_{action}",), mass*prob,
                     "T2" if action == 0 else "T3")
        else:
            raise AssertionError(node)

    for symbol, p_symbol in enumerate(SOURCES[source]):
        assert p_symbol > 0
        # Three distinct symbol histories merge at a common X vertex, but
        # their ordered source provenance survives in the leaf replay.
        walk(symbol, "X", (), p_symbol)
    assert len(paths) == 12
    assert sum(w for _, _, _, w, _ in paths) == F(1)
    assert len({(s, h, t) for _, s, h, _, t in paths}) == 12
    return paths


def probabilities(source, x, y):
    paths = enumerate_ordered(source, x, y)
    return tuple(sum(w for _, _, _, w, t in paths if t == term) for term in TERMINAL)


def prefix_lift(x, z, v):
    """Terminal law of a simplex point, regardless of tied-port implementability."""
    law = (1-x, x-z, z-v, v)
    assert all(w >= 0 for w in law) and sum(law) == F(1)
    return law


def cone_two_atom_witness(x, z, v):
    """Construct an exact 2-point convex mixture of tied-policy laws.

    Under 0<=z<=x<=1, z^2 <= xv, and v<=z.  For x=0 choose y=0.
    Otherwise the mixture is between y=0 and y=v/z, both with fixed x.
    """
    assert F(0) <= v <= z <= x <= F(1) and z*z <= x*v
    if z == 0:
        assert v == 0
        return ((F(1), x, F(0)),)
    y1 = v / z
    weight1 = z*z / (x*v)
    assert F(0) <= weight1 <= F(1) and F(0) <= y1 <= F(1)
    mixture = ((F(1)-weight1, x, F(0)), (weight1, x, y1))
    assert sum(w for w, _, _ in mixture) == F(1)
    assert sum(w*a for w, a, b in mixture) == x
    assert sum(w*a*b for w, a, b in mixture) == z
    assert sum(w*a*b*b for w, a, b in mixture) == v
    return mixture


def main():
    for source, masses in SOURCES.items():
        assert all(m > 0 for m in masses)
        assert sum(masses) == F(1)

    # Independent ordered-history replay of all exact rational grid pairs.
    checked = 0
    for ix, iy in product(range(17), repeat=2):
        x, y = F(ix,16), F(iy,16)
        z, v = x*y, x*y*y
        target = prefix_lift(x,z,v)
        for source in SOURCES:
            actual = probabilities(source,x,y)
            assert actual == target
            assert actual[2] == x*y*(1-y)
        assert x*v == z*z
        assert target[2] <= F(1,4)
        checked += 1

    # Observed optimum and the false independent-prefix simplex policy.
    actual = {source: probabilities(source,F(1),F(1,2)) for source in SOURCES}
    assert all(law == (F(0),F(1,2),F(1,4),F(1,4)) for law in actual.values())
    true_payoff = F(1,4)
    true_min_loss = 1-true_payoff
    relaxed = prefix_lift(F(1),F(1),F(0))
    assert relaxed == (F(0),F(0),F(1),F(0))
    assert F(1)*F(0)-F(1)*F(1) == F(-1)
    relaxed_loss = 1-relaxed[2]
    assert true_min_loss == F(3,4)
    assert relaxed_loss == F(0)
    assert true_min_loss-relaxed_loss == F(3,4)

    # Tight convex hull: every rational pair of y-coins generates a feasible
    # second-order cone point; recover it as a two-atom shared-coin mixture.
    hull_checks = 0
    for ix, ia, ib, iw in product(range(1,5), range(5), range(5), range(5)):
        x, a, b, w = F(ix,4), F(ia,4), F(ib,4), F(iw,4)
        z = x*(w*a+(1-w)*b)
        v = x*(w*a*a+(1-w)*b*b)
        witness = cone_two_atom_witness(x,z,v)
        assert sum(c for c,_,_ in witness) == F(1)
        # For any affine terminal observer, convex combinations are exact;
        # no such claim is made for pathwise correlation or future operations.
        target = prefix_lift(x,z,v)
        for source in SOURCES:
            mixed = tuple(sum(weight*component for weight, xx, yy in witness
                              for component in [probabilities(source,xx,yy)[k]])
                          for k in range(4))
            assert target == mixed
        hull_checks += 1

    # Interior convex-hull point not realizable by a single tied y coin.
    x,z,v = F(1),F(1,2),F(1,2)
    assert x*v > z*z
    witness = cone_two_atom_witness(x,z,v)
    assert witness == ((F(1,2),F(1),F(0)),(F(1,2),F(1),F(1)))
    print('SOURCE_LAWS', SOURCES)
    print('ORDERED_HISTORY_SOURCE_COUNT',len(SOURCES),'LEAF_COUNT_PER_SOURCE',12)
    print('FRACTION_GRID_POLICIES', checked, 'EACH_REPLAYED_FOR_TWO_SOURCES')
    print('OBSERVED_OPTIMAL_T2_MASS', true_payoff, 'MINIMUM_ONE_MINUS_T2', true_min_loss)
    print('RELAXED_SIMPLEX_T2_MASS', relaxed[2], 'MINIMUM_ONE_MINUS_T2', relaxed_loss)
    print('EXACT_RELAXATION_GAP', true_min_loss-relaxed_loss, 'PORT_RESIDUAL_XV_MINUS_Z2_AT_FAKE_POINT',F(-1))
    print('EXACT_CONVEX_HULL', '0<=v<=z<=x<=1, z^2<=x*v')
    print('EXACT_CONVEX_WITNESS_CASES', hull_checks)
    print('STRICT_INTERIOR_CONVEX_WITNESS', witness)
    print('STAGE283B_TIED_PORT_DAG_EXACT_PASS')

if __name__ == '__main__':
    main()
