"""Finite witnesses for the stacking, rigid-grid and marked orbit calculations."""
import json
from collections import Counter
from itertools import product


# Lexicographic residues (x,y,z). Bit j of each octal digit lifts coordinate j.
LIFT = "7323716570015730644422032404173106142611737750426510430052044560"


def rigid_transversal():
    m = 4
    residues = list(product(range(m), repeat=3))
    assert len(LIFT) == len(residues)
    points = [tuple(v[j] + m * ((int(mask) >> j) & 1) for j in range(3))
              for v, mask in zip(residues, LIFT)]
    recovered = {tuple(t % m for t in point) for point in points}
    assert recovered == set(residues)
    differences = Counter(tuple(b - a for a, b in zip(p, q))
                          for p in points[1:] for q in points[1:])
    required = sorted(d for d in product(range(-m, m + 1), repeat=3) if any(x % m for x in d))
    multiplicities = Counter(differences[d] for d in required)
    assert len(required) == 702 and min(multiplicities) > 0
    # The bound for m=2 uses unordered pairs, with d and -d represented together.
    assert (2**3 - 1) * (2**3 - 2) // 2 < (5**3 - 27) // 2
    return {"modulus": m, "octal_lift_word": LIFT, "required_oriented_differences": len(required),
            "multiplicity_histogram": dict(sorted(multiplicities.items())),
            "excluded_modulus_2": {"available_unordered_pairs": 21, "required_up_to_sign": 49}}


def orbit_tally(word):
    n = len(word)
    marked = [1 - bit + word[j - 1] for j, bit in enumerate(word)]
    holes, doubles = marked.count(0), marked.count(2)
    assert holes == doubles and holes * 2 == sum(abs(k - 1) for k in marked)
    edit = min(word.count(0), word.count(1))
    return holes, edit


def single_orbit(n):
    h = n // 2
    observed = Counter(orbit_tally(w) for w in product((0, 1), repeat=n))
    expected = {(0, 0)} | {(j, e) for j in range(1, h + 1) for e in range(j, h + 1)}
    assert set(observed) == expected
    assert orbit_tally([1] * h + [0] * (n - h)) == ((1, h) if n > 1 else (0, 0))
    return observed


def quotient_profiles():
    tested = 0
    for n in range(1, 18):
        atom = single_orbit(n)
        profile = {(0, 0)}
        for c in range(1, 8):
            profile = {(a + j, b + e) for a, b in profile for j, e in atom}
            h = n // 2
            expected = {(j, e) for j in range(h * c + 1) for e in range(j, h * min(j, c) + 1)}
            assert expected == profile
            tested += 1
    return {"single_orbit_lengths": [1, 17], "aggregate_cases": tested,
            "literal_binary_words": sum(2**n for n in range(1, 18)),
            "order_9_3_orbits_distance_ranges": [
                [j, j, 4 * min(j, 3)] for j in range(13)]}


def stacking():
    # 0,1,3 is a (7,3,1) difference set; its complement also has full differences.
    q = 7
    partition = ({0, 1, 3}, {2, 4, 5, 6})
    assert all({(b - a) % q for a in e for b in e} == set(range(q)) for e in partition)
    # Genuine joint restrictions on phase lifts. For H=Z/4 use F1={0}, F2={1}.
    # Then A=H is the only common solution, and adjacent phases must agree.
    def lift_ok(phases):
        for x in range(4):
            counts = Counter((phases[(x - f) % 4] + e) % q
                             for f, sector in enumerate(partition) for e in sector)
            if any(counts[y] != 1 for y in range(q)):
                return False
        return True
    surviving = [p for p in product(range(q), repeat=4) if lift_ok(p)]
    assert surviving == [(t,) * 4 for t in range(q)]
    return {"prime": q, "common_solutions": 1, "phase_functions_tested": q**4,
            "valid_stacked_phase_lifts": len(surviving)}


def macro_counterexample():
    # Two length-three rows downstairs. U is injective after dividing by w.
    G = list(product(range(6), range(2)))
    B = {(x, y) for x, y in G if x % 2 == 0}
    U = [(0, 0), (1, 0)]
    def multiplicity(V):
        return [sum(((x - u) % 6, (y - v) % 2) in V for u, v in U) for x, y in G]
    assert multiplicity(B) == [1] * 12
    sites = list(product(range(3), range(2)))
    errors = []
    for word in product((0, 1), repeat=6):
        lookup = dict(zip(sites, word))
        V = {(x, y) for x, y in G if lookup[x % 3, y]}
        assert len(B ^ V) == 6
        errors.append(sum(abs(k - 1) for k in multiplicity(V)))
    assert len(errors) == 64 and min(errors) == 4
    return {"group": "Z/6 x Z/2", "w": [3, 0], "U": U, "upstairs_exact": True,
            "invariant_repairs_tested": len(errors), "best_macro_L1_error": min(errors),
            "marked_edit_distance": 6, "cardinality_preserving_repair_exists": len(B) % 2 == 0}



if __name__ == "__main__":
    print(json.dumps({"external_source_commit": "adc7f1241b42e322a6451854ab7e4b4c146bf78a",
                      "section_06_git_blob": "f3d57d950997466dc1ab6899242f46b08b2c64c7",
                      "section_07_git_blob": "bce164066c28e456fd0584cee14df92a22ac96c4",
                      "rigid_transversal": rigid_transversal(), "finite_quotients": quotient_profiles(),
                      "finite_stacking": stacking(), "macro_boundary": macro_counterexample()},
                     sort_keys=True, indent=2))
