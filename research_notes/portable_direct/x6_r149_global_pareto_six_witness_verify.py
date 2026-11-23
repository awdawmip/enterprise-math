"""Exact Port-10 six-pair BRC static observer Pareto and six-witness certificate.
Frozen science R121@8085ff66 / R122@0687aa24. No native dynamics claim.
Python >=3.10 standard library only; integer and Fraction arithmetic.
"""
from collections import Counter
from fractions import Fraction

PORT = 10
PARETO = (
    (1, 0, 0), (3, -7, 2), (3, -4, 1), (4, -4, 1),
    (4, -1, 0), (5, -4, 1), (5, -1, 0), (6, -4, 1),
    (6, -1, 0), (7, -1, 0), (7, 2, -1), (9, -5, 1),
)
WITNESSES = (
    (1, 0, 0), (4, -1, 0), (5, -4, 1),
    (5, -1, 0), (6, -4, 1), (9, -5, 1),
)

def population(port=PORT):
    """Sign normalized Port <= port; do NOT quotient multiples."""
    for x in range(-port, port + 1):
        for y in range(-port, port + 1):
            for z in range(-port, port + 1):
                a = (x, y, z)
                if a == (0, 0, 0):
                    continue
                if next(c for c in a if c) < 0:
                    continue
                if max(sum(max(c, 0) for c in a),
                       sum(max(-c, 0) for c in a)) <= port:
                    yield a

def gap(a):
    x, y, z = a
    h = (0, x + 3*y + 6*z, 3*x + 12*y + 30*z,
         7*x + 39*y + 126*z)
    return tuple(abs(h[j] - h[i]) for i, j in
                 ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))

def dominates(u, v):
    return all(p <= q for p, q in zip(u, v))

def score(g, B, D):
    capacities = (136 + B, 312, 136 + D, B + 176, B + D, 176 + D)
    assert all(c > 0 for c in capacities)
    return max(Fraction(x, c) for x, c in zip(g, capacities))

def main():
    pop = list(population())
    assert len(pop) == len(set(pop)) == 1935
    gaps = {a: gap(a) for a in pop}
    # Exact finite all-pairs componentwise Pareto verification.
    minimal = tuple(sorted(a for a in pop if not any(
        b != a and dominates(gaps[b], gaps[a]) for b in pop)))
    assert minimal == PARETO
    assert len(PARETO) == 12
    assert all(any(dominates(gaps[w], gaps[a]) for w in PARETO)
               for a in pop)

    high = [a for a in pop if gaps[a][1] >= 6]
    low = [a for a in pop if gaps[a][1] <= 3]
    assert len(high) == 1890 and len(low) == 45
    assert set(WITNESSES) <= set(low)
    assignment = Counter()
    for a in low:
        if a in WITNESSES:
            continue
        first = next((w for w in sorted(WITNESSES)
                      if dominates(gaps[w], gaps[a])), None)
        assert first is not None, a
        assignment[first] += 1
    assert sum(assignment.values()) == 39
    assert dict(assignment) == {
        (1, 0, 0): 16, (4, -1, 0): 18, (6, -4, 1): 5
    }
    upper = score(gaps[(1, 0, 0)], 20, 528)
    assert upper == Fraction(3, 274)
    assert Fraction(6, 312) > upper

    # Full 1935-direction independent exact rational crosschecks.
    Bvals = [Fraction(20), Fraction(41, 2), Fraction(29), Fraction(40),
             Fraction(60), Fraction(100), Fraction(135), Fraction(136),
             Fraction(1000), Fraction(99999, 7)]
    Dvals = [Fraction(528), Fraction(1057, 2), Fraction(550), Fraction(600),
             Fraction(700), Fraction(900), Fraction(1200), Fraction(1736),
             Fraction(4760), Fraction(10**6)]
    trials = 0
    for B in Bvals:
        for D in Dvals:
            full = min(score(g, B, D) for g in gaps.values())
            six = min(score(gaps[w], B, D) for w in WITNESSES)
            twelve = min(score(gaps[p], B, D) for p in PARETO)
            assert full == six == twelve, (B, D, full, six, twelve)
            trials += 1
    print("R149 GLOBAL PARETO AND SIX-WITNESS PORT-10 CERTIFICATE PASS")
    print("port_unoriented", len(pop), "global_pareto", len(PARETO))
    print("B>=20,D>=528 fixed-gap-excluded", len(high),
          "small-gap", len(low), "six_witnesses", len(WITNESSES))
    print("small-gap other 39 witness assignment", sorted(assignment.items()))
    print("monotone_upper", upper, "fixed-channel_floor", Fraction(6, 312))
    print("exact_fraction_full_population_crosschecks", trials)

if __name__ == "__main__":
    main()
