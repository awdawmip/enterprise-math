"""Independent finite check for historical FCC Johnson rho, not a native X6 benchmark.
Pinned comparison: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3.
"""
import itertools
import json

PAIRS = ((0, 5), (1, 4), (2, 3))


def rho(x):
    return tuple((x[a] - x[b]) % 2 for a, b in PAIRS) + (sum(x) % 3,)


def rho_orbit(x):
    r = rho(x)
    return tuple(sorted(r[:3])) + (r[3],)


def products(x):
    return tuple(x[a] * x[b] for a, b in PAIRS)


def q_orbit(x):
    t = products(x)
    s = sum(t)
    return tuple(sorted(s - 2 * z for z in t))


def can6(x):
    m = min(x)
    return tuple(z - m for z in x)


def wreath_actions():
    actions = set()
    for perm in itertools.permutations(range(3)):
        for swaps in itertools.product((0, 1), repeat=3):
            p = [0] * 6
            for source, (a, b) in enumerate(PAIRS):
                c, d = PAIRS[perm[source]]
                p[a], p[b] = (d, c) if swaps[source] else (c, d)
            actions.add(tuple(p))
    return sorted(actions)


def apply_perm(p, x):
    y = [0] * 6
    for i, j in enumerate(p):
        y[j] = x[i]
    return tuple(y)


def verify(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    actions = wreath_actions()
    verify(len(actions) == 48, "Wreath C2 wr S3 action count")
    image = set()
    orbit_image = set()
    comparisons = 0
    for x in itertools.product(range(-2, 3), repeat=6):
        image.add(rho(x))
        orbit_image.add(rho_orbit(x))
        for p in actions:
            verify(rho_orbit(apply_perm(p, x)) == rho_orbit(x), "Orbit invariant")
            comparisons += 1
    verify(len(image) == 24, "Exact rho image cardinality")
    verify(len(orbit_image) == 12, "Exact rho_orbit image cardinality")
    origin = (0, 0, 0, 0, 0, 0)
    displaced = (6, 0, 0, 0, 0, 0)
    verify(rho(origin) == rho(displaced), "Six-step residue collision")
    verify(rho_orbit(origin) == rho_orbit(displaced), "Orbit residue collision")
    verify(q_orbit(origin) == q_orbit(displaced), "Product-spectrum collision")
    verify(can6(origin) != can6(displaced), "Native relative coordinates differ")
    verify(all(apply_perm(p, origin) != displaced for p in actions), "Distinct carrier orbit")
    results = {
        "schema": "EM_X6_UNIT104_JOHNSON_RHO_TYPED_FINITE_CHECK_V1",
        "science_pin": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "historical_pin": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "selected_fcc_source": "research_checks/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py",
        "historical_source_git_blob_sha1": "62ea223dcbbb118186513737243ead040b77adc0",
        "carrier_group_actions": len(actions),
        "sample_states": 5 ** 6,
        "action_invariance_equalities": comparisons,
        "rho_exact_image_size": len(image),
        "rho_orbit_image_size": len(orbit_image),
        "witness_zero": origin,
        "witness_six_e0": displaced,
        "rho_witness": rho(origin),
        "q_orbit_witness": q_orbit(origin),
        "native_relative_zero": can6(origin),
        "native_relative_six_e0": can6(displaced),
        "native_squared_displacement": 36,
        "native_minimal_steps": 6,
        "native_shortest_path_words": 1,
        "status": "FINITE_EXECUTED_NOT_NATIVE_BENCHMARK_UNREVIEWED_NOT_ADMITTED"
    }
    print(json.dumps(results, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
