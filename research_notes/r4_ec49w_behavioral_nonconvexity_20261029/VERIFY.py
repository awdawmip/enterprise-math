#!/usr/bin/env python3
"""EC49W exact auxiliary BRC calculation; Python stdlib only.
This exhausts the proved 144-vertex always-buy-S slice, not all behavioral policies.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

W = (0, 1, 2)
U = (0, 1)
Z = (0, 1, 2)
SIGMA = (1, 0, -1)
ETA = F(1, 200)
CODES = (('A', 0), ('A', 1), ('B', 0), ('B', 1))


def leaf(source, w, u, z):
    mass = (F(1, 6) if z == w else F(1, 12)) if source == 'P' else F(1, 9)
    return mass * (F(1, 2) + (2 * u - 1) * ETA * SIGMA[w])


def plus(x):
    return max(F(0), x)


def formatted(x):
    return str(x)


def make_vertex(stop_w, b_w, a_labels, b_label):
    p = {(w, c): F(0) for w in W for c in CODES}
    stops = {}
    for w in W:
        stops[w] = F(3, 8) if w == stop_w else F(0)
        b = F(1, 16) if w == b_w else F(0)
        p[w, ('A', a_labels[w])] = 1 - stops[w] - b
        p[w, ('B', b_label)] = b
    return p, stops


def observe(p, terminal='optimized'):
    a = b = F(0)
    independent_masks = 0
    for c in CODES:
        for u in U:
            d_by_z = [sum(p[w, c] * (leaf('P', w, u, z) - leaf('Q', w, u, z))
                          for w in W) for z in Z]
            max_d = sum(plus(v) for v in d_by_z)
            # Independent eight-mask check of the positive-part optimizer.
            masks = [sum(d_by_z[z] * bits[z] for z in Z)
                     for bits in product((0, 1), repeat=3)]
            assert max(masks) == max_d
            independent_masks += len(masks)
            for z, d in zip(Z, d_by_z):
                if d > 0:
                    a += sum(p[w, c] * leaf('P', w, u, z) for w in W)
                    b += sum(p[w, c] * leaf('Q', w, u, z) for w in W)
    return a, b, independent_masks


def costs(p, stops):
    c1 = sum((1 if c[0] == 'A' else 2) * p[w, c]
             for w in W for c in CODES) / 3
    c2 = sum(p.values()) / 3
    assert c2 == 1 - sum(stops.values()) / 3
    return c1, c2


def pure_prefix_J(pre):
    p = {(w, c): F(1) if pre[w] == c else F(0) for w in W for c in CODES}
    st = {w: F(1) if pre[w] is None else F(0) for w in W}
    a, b, _ = observe(p)
    c1, c2 = costs(p, st)
    return a - b - (c1 - c2) / 6


def main():
    for source in ('P', 'Q'):
        atoms = [leaf(source, w, u, z) for w in W for u in U for z in Z]
        assert len(atoms) == 18 and all(x > 0 for x in atoms) and sum(atoms) == 1
    # Strict singleton/pair sign incompatibility for both U observations.
    assert all(2 * (F(1, 2) + (2*u-1)*ETA*SIGMA[i])
               > F(1, 2) + (2*u-1)*ETA*SIGMA[j]
               for i in W for j in W if i != j for u in U)

    rows = []
    for sw, bw in product(W, repeat=2):
        for labels in product((0, 1), repeat=3):
            for b_label in (0, 1):
                p, stops = make_vertex(sw, bw, labels, b_label)
                c1, c2 = costs(p, stops)
                assert (c1, c2) == (F(43, 48), F(7, 8))
                a, b, mask_count = observe(p)
                rows.append((a-b, a, b, sw, bw, labels, b_label))
    assert len(rows) == 144
    optimum = max(r[0] for r in rows)
    assert optimum == F(59, 576), (optimum, F(59, 576))
    winners = [r for r in rows if r[0] == optimum]
    witness = [r for r in rows if (r[3], r[4], r[5], r[6]) == (2, 2, (0, 1, 0), 0)][0]
    assert witness[:3] == (F(59, 576), F(109, 192), F(67, 144))

    raw_codes = (None,) + CODES
    pure = [(pure_prefix_J(p), p) for p in product(raw_codes, repeat=3)]
    assert len(pure) == 125
    pure_max = max(v for v, _ in pure)
    assert pure_max == F(1, 9)
    for v, p in pure:
        if v == pure_max:
            a0 = [w for w in W if p[w] == ('A', 0)]
            a1 = [w for w in W if p[w] == ('A', 1)]
            b_codes = [w for w in W if p[w] in (('B', 0), ('B', 1))]
            assert 1 <= len(a0) <= 2 and 1 <= len(a1) <= 2 and len(b_codes) <= 1
            assert not (None in p and b_codes)

    # Existing EC49V convexified external-seed witness; joint outcomes are linear in a shared seed.
    mixed = [(F(3, 8), (None, ('A', 0), ('A', 1))),
             (F(9, 16), (('A', 0), ('A', 0), ('A', 1))),
             (F(1, 16), (('A', 0), ('A', 1), ('B', 0)))]
    assert sum(x for x, _ in mixed) == 1
    c1_mix = c2_mix = d_mix = F(0)
    for weight, prefix in mixed:
        p = {(w, c): F(1) if prefix[w] == c else F(0) for w in W for c in CODES}
        st = {w: F(1) if prefix[w] is None else F(0) for w in W}
        cost1, cost2 = costs(p, st)
        aa, bb, _ = observe(p)
        c1_mix += weight * cost1
        c2_mix += weight * cost2
        d_mix += weight * (aa-bb)
    assert (c1_mix, c2_mix, d_mix) == (F(43,48),F(7,8),F(11,96))

    report = {
        'schema': 'EC49W_EXACT_144_VERTEX_ALWAYS_S_AND_NONCONVEXITY_V1',
        'status': 'AUTHOR_PROVED_EXACT_FRACTION_PASS_UNREVIEWED_NOT_ADMITTED',
        'source_atoms_per_source': 18,
        'eta': formatted(ETA),
        'always_S_cost_section': {'C1': '43/48', 'C2': '7/8', 'vertex_count': len(rows),
                                   'terminal_masks_independently_compared_per_vertex': mask_count,
                                   'optimal_discrimination': formatted(optimum),
                                   'number_of_tied_vertices': len(winners),
                                   'explicit_witness_acceptance': {'P': formatted(witness[1]), 'Q': formatted(witness[2])}},
        'all_pure_prefixes_J_checked': len(pure),
        'pure_J_max': formatted(pure_max),
        'pure_J_equality_prefix_count': sum(v == pure_max for v,_ in pure),
        'shared_seed_convexified_point': {'C1': formatted(c1_mix),'C2':formatted(c2_mix),
                                         'discrimination': formatted(d_mix)},
        'all_behavioral_fixed_cost_optimum': 'OPEN: rigorously in [59/576,11/96) by analytic non-attainment proof',
        'proof_boundary': 'All-real non-attainment is analytic; 144-point check is exhaustive only for always-S subclass.'
    }
    output = Path(__file__).with_name('EXACT_REPORT.json')
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print('PASS EC49W: 144 always-S vertices; optimum 59/576;',
          'J max 1/9 over 125 pure prefixes;',len(winners),'optimal vertex witnesses')
    print('PASS convexified point: C1=43/48,C2=7/8,delta=11/96')
    print(output.read_text(encoding='utf-8'))


if __name__ == '__main__':
    main()
