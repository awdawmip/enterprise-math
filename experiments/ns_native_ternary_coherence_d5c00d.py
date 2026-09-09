#!/usr/bin/env python3
"""Exact finite X6 coherence diagnostics, not a native fluid or NS solver.

Only signed integer coordinates are used. The ternary packet model and its
additive first moment are explicitly additional *test-model* assumptions;
they do not define P000 primitive force quanta or TRIADIC_CLOSURE_E.
Run: python ns_native_ternary_coherence_d5c00d.py --output results.json
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path

D = 6
Vec = tuple[int, ...]
Config = tuple[int, int, int]
Port = tuple[int, int, int, int]  # spectator axis/sign, old pair, selected pair
ZERO = (0,) * D

def unit(i: int, sign: int = 1) -> Vec:
    if not 0 <= i < D or sign not in (-1, 1):
        raise ValueError('Invalid signed axis')
    return tuple(sign if j == i else 0 for j in range(D))

def add(x: Vec, y: Vec) -> Vec:
    return tuple(a + b for a, b in zip(x, y))

def scale(n: int, x: Vec) -> Vec:
    return tuple(n * a for a in x)

# Channels 2*i and 2*i+1 represent -e_i and +e_i.
DIRS = tuple(unit(i, s) for i in range(D) for s in (-1, 1))

def moment(c: Config) -> Vec:
    return tuple(sum(DIRS[a][i] for a in c) for i in range(D))

def C(j: int, sign: int, pair_axis: int) -> Config:
    return tuple(sorted((2*j + (sign == 1), 2*pair_axis, 2*pair_axis+1)))

def act_vec(p: tuple[int, ...], x: Vec) -> Vec:
    out = [0]*D
    for i, a in enumerate(x):
        out[p[i]] = a
    return tuple(out)

def act_config(p: tuple[int, ...], c: Config) -> Config:
    return tuple(sorted(2*p[a//2] + a % 2 for a in c))

def slot_data(c: Config) -> tuple[int, int, int] | None:
    P = moment(c)
    if sum(map(abs, P)) != 1:
        return None
    j = next(i for i, x in enumerate(P) if x)
    counts = Counter(c)
    l = next(i for i in range(D) if counts[2*i] and counts[2*i+1])
    assert c == C(j, P[j], l)
    return j, P[j], l

def bare_map(c: Config, collapse_positive: bool, collapse_negative: bool) -> Config:
    data = slot_data(c)
    if data is None:
        return c
    j, sign, l = data
    collapse = collapse_positive if sign == 1 else collapse_negative
    return C(j, sign, j if collapse else l)

def port_update(a: Port) -> Port:
    j, sign, l, m = a
    if len({j, l, m}) != 3 or sign not in (-1, 1):
        raise ValueError('Port axes must be distinct, sign must be +/-1')
    return j, sign, m, l

def act_port(p: tuple[int, ...], a: Port) -> Port:
    j, sign, l, m = a
    return p[j], sign, p[l], p[m]

def port_observe(a: Port) -> Config:
    j, sign, l, _ = a
    return C(j, sign, l)

def spatial_lift(triad: tuple[int, int, int], bits: tuple[int, int, int]):
    """A relational triangle lifted into six primitive spatial steps.

    Nodes are e_i, e_j, e_k. Each composite leg e_b-e_a has two
    orderings. Nothing here asserts force balance, scattering or viscosity.
    """
    if len(set(triad)) != 3 or any(b not in (0, 1) for b in bits):
        raise ValueError('Need three distinct axes and three binary path flags')
    steps: list[Vec] = []
    for a, b, flag in zip(triad, triad[1:] + triad[:1], bits):
        leg = (unit(a, -1), unit(b))
        steps.extend(leg if flag == 0 else reversed(leg))
    vertices = [unit(triad[0])]
    for v in steps:
        vertices.append(add(vertices[-1], v))
    assert vertices[-1] == vertices[0]
    return tuple(steps), tuple(vertices)

def run_checks() -> dict:
    configs = list(combinations_with_replacement(range(2*D), 3))
    fibers: dict[Vec, list[Config]] = defaultdict(list)
    for c in configs:
        P = moment(c)
        fibers[P].append(c)
        counts = Counter(c)
        pairs = sum(min(counts[2*i], counts[2*i+1]) for i in range(D))
        assert 3 == sum(map(abs, P)) + 2*pairs
        assert sum(map(abs, P)) in (1, 3)
    assert ZERO not in fibers
    hist = Counter(len(v) for v in fibers.values())
    assert (len(configs), len(fibers), hist) == (364, 304, Counter({1:292, 6:12}))
    for P, fs in fibers.items():
        if len(fs) == 1:
            assert sum(map(abs, P)) == 3
        else:
            j = next(i for i, a in enumerate(P) if a)
            assert set(fs) == {C(j, P[j], l) for l in range(D)}

    # Exhaust *all* 6^6 deterministic maps of one moment fiber. Adjacent
    # transpositions of axes 1..5 generate its full S5 stabilizer.
    stabilizer_generators = []
    for i in range(1, 5):
        p = list(range(D)); p[i], p[i+1] = p[i+1], p[i]
        stabilizer_generators.append(tuple(p))
    admissible_maps = []
    for f in product(range(D), repeat=D):
        if all(f[p[l]] == p[f[l]] for p in stabilizer_generators for l in range(D)):
            admissible_maps.append(f)
    assert set(admissible_maps) == {(0,)*D, tuple(range(D))}

    perms = list(permutations(range(D)))
    maps = {(pos, neg): {c: bare_map(c, pos, neg) for c in configs}
            for pos, neg in product((False, True), repeat=2)}
    global_checks = 0
    for p in perms:
        transformed = {c: act_config(p, c) for c in configs}
        for tab in maps.values():
            for c in configs:
                assert tab[transformed[c]] == transformed[tab[c]]
                global_checks += 1
    bijective = [key for key, tab in maps.items() if len(set(tab.values())) == len(configs)]
    assert bijective == [(False, False)]

    ports: list[Port] = [(j, s, l, m) for j, l, m in permutations(range(D), 3)
                        for s in (-1, 1)]
    port_covariance_checks = 0
    for a in ports:
        b = port_update(a)
        assert port_update(b) == a
        assert moment(port_observe(a)) == moment(port_observe(b))
        assert port_observe(a) != port_observe(b)
        for p in perms:
            assert port_update(act_port(p, a)) == act_port(p, b)
            port_covariance_checks += 1
    a, b = (0, 1, 1, 2), (0, 1, 1, 3)
    assert port_observe(a) == port_observe(b)
    assert port_observe(port_update(a)) != port_observe(port_update(b))
    fixed_axes = [p for p in perms if p[0] == 0 and p[1] == 1]
    new_axes_orbit = {p[2] for p in fixed_axes}
    assert len(fixed_axes) == 24 and new_axes_orbit == {2, 3, 4, 5}
    assert not any(all(p[m] == m for p in fixed_axes) for m in new_axes_orbit)

    # Any word using three axes and returning has at least 2 steps per axis.
    # Independently enumerate all words of lengths 1..5 on one 3-axis alphabet.
    alphabet = DIRS[:6]
    short_tested, short_closed_three_axes = 0, 0
    for length in range(1, 6):
        for word in product(range(6), repeat=length):
            short_tested += 1
            used = {a//2 for a in word}
            endpoint = tuple(sum(alphabet[a][i] for a in word) for i in range(D))
            if len(used) == 3 and endpoint == ZERO:
                short_closed_three_axes += 1
    assert short_closed_three_axes == 0
    minimal_six_words = set(permutations(range(6)))
    assert len(minimal_six_words) == 720

    lifts, simple, lift_generator_checks, flux_tests = 0, 0, 0, 0
    path_reversal_checks, anchor_checks = 0, 0
    anchors = (ZERO, (3,-2,0,1,0,-4), (-1,0,5,-2,2,0))
    all_generators = []
    for i in range(5):
        p = list(range(D)); p[i], p[i+1] = p[i+1], p[i]
        all_generators.append(tuple(p))
    for triad in permutations(range(D), 3):
        for flags in product((0, 1), repeat=3):
            steps, vertices = spatial_lift(triad, flags)
            lifts += 1
            rs, rv = spatial_lift((triad[0], triad[2], triad[1]), tuple(reversed(flags)))
            assert rs == tuple(scale(-1, v) for v in reversed(steps))
            assert rv == tuple(reversed(vertices))
            path_reversal_checks += 1
            for anchor in anchors:
                moved = tuple(add(anchor, v) for v in vertices)
                assert moved[0] == moved[-1]
                assert tuple(add(moved[i+1], scale(-1, moved[i])) for i in range(6)) == steps
                anchor_checks += 1
            assert all(v in DIRS for v in steps)
            assert len({i for v in steps for i, a in enumerate(v) if a}) == 3
            assert all(vertices[2*i] == unit(triad[i]) for i in range(3))
            if len(set(vertices[:-1])) == 6:
                simple += 1
            for p in all_generators:
                ss, vv = spatial_lift(tuple(p[i] for i in triad), flags)
                assert ss == tuple(act_vec(p, v) for v in steps)
                assert vv == tuple(act_vec(p, v) for v in vertices)
                lift_generator_checks += 1
            # Integer flow incidence has zero boundary; no momentum/force
            # interpretation is attached to this particle-count identity.
            flow = Counter(zip(vertices[:-1], vertices[1:]))
            boundary: Counter = Counter()
            for (tail, head), q in flow.items():
                boundary[tail] -= q; boundary[head] += q
            assert all(q == 0 for q in boundary.values())
            flux_tests += 1
    assert (lifts, simple) == (960, 480)

    return {
        'schema': 'EM_NATIVE_TERNARY_COHERENCE_RESULTS_V1',
        'event_id': 'NS-NATIVE-TERNARY-COHERENCE-20260909-D5C00D-09',
        'status': 'EXACT_FINITE_CHECKS_WITH_ORDINARY_PROOFS_NOT_FLUID_DYNAMICS',
        'native_coordinate_source': 'awdawmip/enterprise-math@e16c5a875d4098f260f3d17283368b20b02c774c',
        'ternary': {'multisets': len(configs), 'moment_fibers': len(fibers),
                    'singleton_fibers': hist[1], 'six_state_fibers': hist[6],
                    'zero_moment_configurations': 0, 'fiber_maps_exhausted': D**D,
                    'equivariant_fiber_maps': admissible_maps,
                    'global_S6_equivariant_maps': len(maps),
                    'global_equivariance_equalities_checked': global_checks,
                    'bijective_maps': 1},
        'port_repair': {'decorated_states': len(ports), 'involution': True,
                        'S6_covariance_equalities_checked': port_covariance_checks,
                        'moment_conserved': True, 'bare_observer_descent': False,
                        'new_axis_orbit_size': len(new_axes_orbit),
                        'minimum_deterministic_selector_fiber_size': 4},
        'spatial_lift': {'short_words_tested': short_tested,
                         'closed_three_axis_words_below_six': short_closed_three_axes,
                         'minimal_six_step_words_for_fixed_three_axes': len(minimal_six_words),
                         'oriented_lifts_checked': lifts, 'simple_lifts': simple,
                         'S6_generator_covariance_equalities_checked': lift_generator_checks,
                         'source_free_integer_flow_checks': flux_tests,
                         'path_reversal_identities_checked': path_reversal_checks,
                         'anchor_translation_identities_checked': anchor_checks},
        'nonclaims': ['P000 force closure is not identified with additive moment zero',
                      'No native fluid update, viscosity, instability, or NS theorem',
                      'Port swap and spatial circulation are diagnostic interfaces, not selected physics',
                      'No independent review or Lean verification',
                      'No proof of historical novelty']}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    data = run_checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
