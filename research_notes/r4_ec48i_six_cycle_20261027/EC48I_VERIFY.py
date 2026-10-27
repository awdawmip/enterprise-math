#!/usr/bin/env python3
"""EC48I: exact six-cycle seedless BRC ROC counterexample and finite sign audit.

All source-law calculations use fractions.Fraction; sign-pattern enumeration is
finite integer combinatorics. Python 3 standard library only. No native-X6 claim.
"""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import product
import json

SIGNS = ((-1, 0, 1), (-1, 1, 0), (0, -1, 1),
         (0, 1, -1), (1, -1, 0), (1, 0, -1))
P = tuple(tuple(2 + x for x in row) for row in SIGNS)
Q = tuple((2, 2, 2) for _ in SIGNS)
SP, SQ = sum(map(sum, P)), sum(map(sum, Q))
assert SP == SQ == 36
p = tuple(tuple(F(x, SP) for x in row) for row in P)
q = tuple(tuple(F(x, SQ) for x in row) for row in Q)
H, Y = len(SIGNS), 3


def sign_supports(patterns, K):
    """All optimal deterministic encoders and compulsory decoder sign masks."""
    out = {}
    for f in product(range(K), repeat=len(patterns)):
        pos, neg = [0] * K, [0] * K
        for h, m in enumerate(f):
            for y, s in enumerate(patterns[h]):
                if s == 1:
                    pos[m] |= 1 << y
                elif s == -1:
                    neg[m] |= 1 << y
        if all(not (pos[m] & neg[m]) for m in range(K)):
            start = end = True
            for h, m in enumerate(f):
                for y, s in enumerate(patterns[h]):
                    if s == 0:
                        if (pos[m] >> y) & 1:
                            start = False
                        if (neg[m] >> y) & 1:
                            end = False
            out[f] = (tuple(pos), tuple(neg), start, end)
    return out


def neighbor_ok(f, g, info):
    P0, N0 = info[f][:2]
    P1, N1 = info[g][:2]
    return all(not ((P0[k] | P1[k]) & (N0[k] | N1[k]))
               for k in range(len(P0)))


def graph_components(patterns, K):
    info = sign_supports(patterns, K)
    adj = {f: set() for f in info}
    for f in info:
        for h in range(len(f)):
            for dest in range(f[h] + 1, K):
                g = f[:h] + (dest,) + f[h + 1:]
                if g in info and neighbor_ok(f, g, info):
                    adj[f].add(g)
                    adj[g].add(f)
    comps, seen = [], set()
    for f in info:
        if f in seen:
            continue
        todo, cc = [f], []
        seen.add(f)
        while todo:
            u = todo.pop()
            cc.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        comps.append(cc)
    return info, adj, comps


def rowbits(bits):
    return tuple(int(x) for x in bits)


def four_state_policy(stage, t):
    assert 0 <= stage < 6 and F(0) <= t <= 1
    dec = [[F(x) for x in word] for word in ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1))]
    enc = [[F(int(m == target)) for m in range(4)]
           for target in (0, 1, 0, 1, 2, 2)]

    def action(step, s):
        if step == 0:
            enc[0] = [1 - s, F(0), F(0), s]
        elif step == 1:
            enc[1] = [F(0), 1 - s, F(0), s]
        elif step == 2:
            dec[0] = [s, F(0), F(1)]
        elif step == 3:
            enc[4] = [s, F(0), 1 - s, F(0)]
        elif step == 4:
            dec[1] = [s, F(1), F(0)]
        elif step == 5:
            enc[5] = [F(0), s, 1 - s, F(0)]

    for past in range(stage):
        action(past, F(1))
    action(stage, t)
    return enc, dec


def roc_and_check(enc, dec, ratio, expected=None):
    K = len(dec)
    assert all(len(row) == K and sum(row) == 1 and all(F(0) <= v <= 1 for v in row)
               for row in enc)
    assert all(len(row) == Y and all(F(0) <= v <= 1 for v in row)
               for row in dec)
    alpha = beta = F(0)
    for h in range(H):
        for y in range(Y):
            w = sum(enc[h][m] * dec[m][y] for m in range(K))
            assert F(0) <= w <= 1
            if p[h][y] > ratio * q[h][y]:
                assert w == 1
            elif p[h][y] < ratio * q[h][y]:
                assert w == 0
            alpha += p[h][y] * w
            beta += q[h][y] * w
    support = sum(max(p[h][y] - ratio * q[h][y], F(0))
                  for h in range(H) for y in range(Y))
    assert alpha - ratio * beta == support
    if expected is not None:
        assert (alpha, beta) == expected, ((alpha, beta), expected)
    return alpha, beta


def check_nonmiddle_faces():
    result = {}
    for r, case in ((F(1, 2), 'low'), (F(3, 2), 'high')):
        points = []
        for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            dec = []
            for j in range(3):
                dec.append([t if y == j else F(1 if case == 'low' else 0)
                            for y in range(Y)])
            enc = [[F(int(j == (row.index(-1) if case == 'low' else row.index(1))))
                    for j in range(3)] for row in SIGNS]
            alpha, beta = roc_and_check(enc, dec, r)
            points.append((str(alpha), str(beta)))
        result[str(r)] = points
    return result


def check_abstract_sign_patterns():
    """Exact finite audit of ALL subsets of distinct ternary Y=3 rows.

    Enumerate each subset once. Prune if >3 lower or upper binary words;
    every K_hull<=3 critical face must pass these necessary chamber bounds.
    """
    types = tuple(product((-1, 0, 1), repeat=3))
    lower = tuple(sum((s == 1) << y for y, s in enumerate(row)) for row in types)
    upper = tuple(sum((s >= 0) << y for y, s in enumerate(row)) for row in types)
    counts = Counter()
    failures = []

    def rec(i, chosen, lowset, upset):
        if i == len(types):
            n = len(chosen)
            counts['subsets_n' + str(n)] += 1
            if n >= 4 and max(lowset.bit_count(), upset.bit_count()) == 3:
                # A subset with no ties cannot be critical and needs no test.
                if not any(0 in types[j] for j in chosen):
                    return
                patterns = tuple(types[j] for j in chosen)
                info = sign_supports(patterns, 3)
                starts = [f for f, data in info.items() if data[2]]
                ends = set(f for f, data in info.items() if data[3])
                assert starts and ends
                seen = set(starts)
                todo = deque(starts)
                success = bool(ends.intersection(starts))
                while todo and not success:
                    f = todo.popleft()
                    for h in range(n):
                        for new in range(3):
                            if new == f[h]:
                                continue
                            g = f[:h] + (new,) + f[h + 1:]
                            if g in info and g not in seen and neighbor_ok(f, g, info):
                                if g in ends:
                                    success = True
                                    break
                                seen.add(g)
                                todo.append(g)
                        if success:
                            break
                counts['tested'] += 1
                if not success:
                    failures.append(chosen)
            return
        rec(i + 1, chosen, lowset, upset)
        nl = lowset | (1 << lower[i])
        nu = upset | (1 << upper[i])
        if nl.bit_count() <= 3 and nu.bit_count() <= 3:
            rec(i + 1, chosen + (i,), nl, nu)

    rec(0, (), 0, 0)
    assert counts['tested'] == 13570
    assert failures == [(5, 7, 11, 15, 19, 21)], failures
    return {'distinct_type_subsets_by_size': dict(sorted(
                ((int(k[len('subsets_n'):]), v) for k, v in counts.items()
                 if k.startswith('subsets_n')))),
            'tested_three_decoder_nontrivial_subsets': counts['tested'],
            'no_extreme_to_extreme_path_count': len(failures),
            'unique_obstruction_row_type_indices': list(failures[0]),
            'row_type_enumeration_order': 'itertools.product((-1,0,1),repeat=3)'}


def run():
    ratios = sorted({p[h][y] / q[h][y] for h in range(H) for y in range(Y)})
    assert ratios == [F(1, 2), F(1), F(3, 2)]
    kh_chambers = []
    for lam in [F(1, 4), F(3, 4), F(5, 4), F(2)]:
        words = {tuple(int(p[h][y] > lam * q[h][y]) for y in range(Y))
                 for h in range(H)}
        kh_chambers.append(len(words))
    assert kh_chambers == [1, 3, 3, 1]
    compat = []
    for i in range(H):
        for j in range(i + 1, H):
            if not any(SIGNS[i][y] * SIGNS[j][y] == -1 for y in range(Y)):
                compat.append((i, j))
    assert compat == [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
    for K, count, edge_count, ncomp in ((3, 12, 0, 12), (4, 264, 576, 1)):
        info, adj, comps = graph_components(SIGNS, K)
        assert len(info) == count and sum(map(len, adj.values())) // 2 == edge_count
        assert len(comps) == ncomp
        if K == 3:
            lo = Counter()
            hi = Counter()
            for f, data in info.items():
                # There are no free tied decoder bits for any optimal K=3 encoding.
                lower = upper = F(0)
                for h, m in enumerate(f):
                    for y, sign in enumerate(SIGNS[h]):
                        if sign == 0:
                            if data[0][m] & (1 << y):
                                lower += q[h][y]
                                upper += q[h][y]
                            elif not (data[1][m] & (1 << y)):
                                upper += q[h][y]
                lo[str(lower)] += 1
                hi[str(upper)] += 1
                assert lower == upper
            assert lo == {'0': 6, '1/3': 6}
    middle_points = []
    for phase in range(6):
        for t in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            enc, dec = four_state_policy(phase, t)
            z = (phase + t) / 18
            pair = roc_and_check(enc, dec, F(1),
                                 (F(1, 2) + z, F(1, 3) + z))
            middle_points.append((str(pair[0]), str(pair[1])))
    # Independent linearity certificate: in each phase only ONE encoder row
    # or decoder row varies linearly, with the counterpart held fixed; ROC is
    # affine in t on the complete closed interval [0,1]. Endpoint formulas
    # therefore establish continuous full-face coverage, not just samples.
    for phase in range(6):
        a0, b0 = roc_and_check(*four_state_policy(phase, F(0)), F(1))
        a1, b1 = roc_and_check(*four_state_policy(phase, F(1)), F(1))
        assert (a0, b0) == (F(1, 2) + F(phase, 18),
                            F(1, 3) + F(phase, 18))
        assert (a1 - a0, b1 - b0) == (F(1, 18), F(1, 18))
    other = check_nonmiddle_faces()
    abstract = check_abstract_sign_patterns()
    report = {
        'scope': 'finite strictly positive two-stage BRC terminal ROC; no persistent common seed; not X6',
        'P_raw': P, 'Q_raw': Q, 'P_total': SP, 'Q_total': SQ,
        'critical_ratios': [str(x) for x in ratios],
        'strict_chamber_signature_counts': kh_chambers,
        'K_hull': 3, 'K_seed': 4,
        'critical_r': '1', 'face_support_alpha_minus_beta': '1/6',
        'full_face_beta_interval': ['1/3', '2/3'],
        'unreachable_at_K3': {'alpha': '2/3', 'beta': '1/2'},
        'compatible_history_edges': compat,
        'optimal_encoder_enumeration': {
            'K3': {'tested': 3**6, 'optimal': 12, 'edges': 0, 'components': 12,
                   'face_tied_mass_component_intervals': {'[0,0]': 6, '[1/3,1/3]': 6}},
            'K4': {'tested': 4**6, 'optimal': 264, 'edges': 576, 'components': 1}},
        'four_state_six_phases': 6,
        'tie_mass_phase_boundaries': [str(F(i, 18)) for i in range(7)],
        'exact_fraction_sample_checks_middle': len(middle_points),
        'exact_fraction_sample_checks_other_critical_faces': other,
        'abstract_exhaustive_audit': abstract,
        'mathematical_status': 'author-side direct combinatorial proof, finite exact checks, pending independent review'
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    run()
