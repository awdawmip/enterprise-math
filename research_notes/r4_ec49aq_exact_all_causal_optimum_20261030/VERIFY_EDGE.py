"""EC49AQ: exact certificate for all real causal policies in the 18+18-leaf auxiliary BRC model.

Run: python3 VERIFY.py --certificate EDGE_CERTIFICATES.tsv > EXACT_REPORT.json
Only Python's standard library Fraction is used. No Monte Carlo or floats.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json
import sys

ZERO, ONE = Q(0), Q(1)
ETA = Q(1, 25)
FIRST_COST = Q(43, 16)    # sum over the three conditional rows; actual cost = 43/48
SECOND_COST = Q(13, 16)
K = Q(177, 172)
ACTION_COST = (1, 1, 2, 2, 0)
ACCEPT = {(0, 1), (1, 2), (2, 0)}  # (observed action, purchased sensor z)
TARGET = Q(77, 688)


def vertices():
    """Complete vertices of product of 3 simplexes cut by first-cost equality."""
    result = set()
    for mixing_row in range(3):
        others = [w for w in range(3) if w != mixing_row]
        for i, j in product(range(5), repeat=2):
            needed = FIRST_COST - ACTION_COST[i] - ACTION_COST[j]
            for a, b in combinations(range(5), 2):
                if not min(ACTION_COST[a], ACTION_COST[b]) < needed < max(ACTION_COST[a], ACTION_COST[b]):
                    continue
                theta = (needed - ACTION_COST[b]) / Q(ACTION_COST[a] - ACTION_COST[b])
                x = [[ZERO] * 5 for _ in range(3)]
                x[others[0]][i] = ONE
                x[others[1]][j] = ONE
                x[mixing_row][a] = theta
                x[mixing_row][b] = ONE - theta
                result.add(tuple(tuple(row) for row in x))
    return sorted(result)


def support(x):
    return frozenset((w, c) for w in range(3) for c in range(5) if x[w][c] > ZERO)


def check_first_stage(x):
    assert all(sum(row, ZERO) == ONE and all(v >= ZERO for v in row) for row in x)
    assert sum((Q(ACTION_COST[c]) * x[w][c] for w, c in product(range(3), range(5))), ZERO) == FIRST_COST


def paid_cost(x):
    return sum((x[w][c] for w, c in product(range(3), range(4))), ZERO) / 3


def mix(a, b, theta):
    assert ZERO <= theta <= ONE
    return tuple(tuple((ONE - theta) * a[w][c] + theta * b[w][c] for c in range(5)) for w in range(3))


def t(w, u):
    return Q(1, 2) + (2 * u - 1) * (1 - w) * ETA


def score_fibers(x):
    """(purchased probability mass, optimal support score) indexed by (c,u)."""
    result = []
    for c, u in product(range(4), range(2)):
        q = [x[w][c] * t(w, u) / 3 for w in range(3)]
        total = sum(q, ZERO)
        support_score = sum((max(ZERO, 43 * qz - 16 * total) for qz in q), ZERO) / 172
        result.append((total, support_score))
    return result


def full_purchase_support(x):
    return sum((value for mass, value in score_fibers(x)), ZERO)


def check_witness():
    x = ((ZERO, Q(3, 16), Q(1, 4), ZERO, Q(9, 16)),
         (ONE, ZERO, ZERO, ZERO, ZERO),
         (ZERO, ONE, ZERO, ZERO, ZERO))
    check_first_stage(x)
    assert paid_cost(x) == SECOND_COST
    assert full_purchase_support(x) == TARGET
    p_sum = q_sum = alpha = beta = ZERO
    for w, u, z in product(range(3), range(2), range(3)):
        pp = t(w, u) * (Q(1, 6) if z == w else Q(1, 12))
        qq = t(w, u) / 9
        assert pp > ZERO and qq > ZERO
        p_sum += pp
        q_sum += qq
        for c in range(4):
            if (c, z) in ACCEPT:
                alpha += x[w][c] * pp
                beta += x[w][c] * qq
    assert p_sum == q_sum == ONE
    assert alpha == Q(25, 64)
    assert beta == Q(13, 48)
    assert alpha - K * beta == TARGET
    return alpha, beta


def make_certificate():
    vv = vertices()
    assert len(vv) == 168
    for x in vv:
        check_first_stage(x)
        assert len(support(x)) == 4
    costs = Counter(str(paid_cost(x)) for x in vv)
    assert costs == {
        '43/96': 24, '9/16': 24, '59/96': 24,
        '2/3': 48, '25/32': 24, '43/48': 24,
    }
    # A 1D face has 5 positive x[w,c] entries (3 row constraints + 1 cost constraint).
    edges = [(i, j) for i in range(len(vv)) for j in range(i + 1, len(vv))
             if len(support(vv[i]) | support(vv[j])) == 5]
    assert len(edges) == 924
    assert all(sum(i in (a, b) for a, b in edges) == 11 for i in range(len(vv)))

    high = [i for i, x in enumerate(vv) if paid_cost(x) > SECOND_COST]
    assert len(high) == 24 and all(paid_cost(vv[i]) == Q(43, 48) for i in high)
    crossing = [(i, j) for i, j in edges
                if (paid_cost(vv[i]) > SECOND_COST) != (paid_cost(vv[j]) > SECOND_COST)]
    high_high = [(i, j) for i, j in edges
                 if paid_cost(vv[i]) > SECOND_COST and paid_cost(vv[j]) > SECOND_COST]
    assert len(crossing) == 144 and len(high_high) == 60

    cert_rows = []
    high_values = []
    for i in high:
        value = full_purchase_support(vv[i])
        cert_rows.append(('HIGH', i, '-', '-', str(paid_cost(vv[i])), str(value)))
        high_values.append(value)
        assert value <= TARGET
    assert max(high_values) == Q(12177, 137600)

    boundary_values = []
    crossing_x = set()
    for i, j in crossing:
        # x(lambda)=(1-lambda)*v_i+lambda*v_j; c(x(lambda))=13/16
        c_i, c_j = paid_cost(vv[i]), paid_cost(vv[j])
        lam = (SECOND_COST - c_i) / (c_j - c_i)
        assert ZERO < lam < ONE
        x = mix(vv[i], vv[j], lam)
        check_first_stage(x)
        assert paid_cost(x) == SECOND_COST
        assert x not in crossing_x
        crossing_x.add(x)
        value = full_purchase_support(x)
        assert value <= TARGET
        boundary_values.append(value)
        cert_rows.append(('CUT', i, j, str(lam), str(paid_cost(x)), str(value)))
    assert len(crossing_x) == 144
    assert max(boundary_values) == TARGET
    assert sum(v == TARGET for v in boundary_values) == 24
    alpha, beta = check_witness()

    report = {
        'schema': 'EC49AQ_CAUSAL_GLOBAL_EQUALITY_CERT_V1',
        'model': 'strictly positive auxiliary 18+18-leaf BRC, hidden w erased; independent conditional sensor-purchase r(c,u)',
        'eta': str(ETA), 'first_stage_expected_cost': str(FIRST_COST / 3),
        'first_stage_conditional_row_cost_sum': str(FIRST_COST),
        'second_stage_expected_cost': str(SECOND_COST),
        'support_coefficient': str(K),
        'original_product_slice_vertices': len(vv),
        'original_polytope_edges': len(edges),
        'original_vertex_paid_cost_distribution': dict(sorted(costs.items())),
        'original_vertices_above_purchase_cut': len(high),
        'edges_with_both_endpoints_above_cut': len(high_high),
        'edges_crossing_purchase_cut': len(crossing),
        'cut_polytope_vertices_exact': len(high) + len(crossing_x),
        'high_vertex_max_full_purchase_support': str(max(high_values)),
        'boundary_vertex_max_full_purchase_support': str(max(boundary_values)),
        'boundary_vertices_attaining_maximum': sum(v == TARGET for v in boundary_values),
        'exact_global_H_max_all_real_causal_policies': str(TARGET),
        'attaining_witness_alpha': str(alpha),
        'attaining_witness_beta': str(beta),
        'method': 'convex upper envelope on truncated first-cost polytope, exact exhaustive rational vertex check',
        'calculation': 'Python stdlib Fraction only; no floats/sampling',
        'scientific_status': 'AUTHOR_PROVED_AND_EXACT_CHECKED; PORTABLE_DRAFT; UNREVIEWED; NOT_ADMITTED',
        'transfer_limit': 'positive auxiliary BRC only; native signed BRC, X6, heartbeat require typed bridge',
    }
    return report, cert_rows


def main():
    report, rows = make_certificate()
    if len(sys.argv) == 3 and sys.argv[1] == '--certificate':
        output = Path(sys.argv[2])
        data = 'kind\tv_i\tv_j\tlambda_from_i_to_j\tpaid_cost\tF\n'
        data += '\n'.join('\t'.join(map(str, row)) for row in rows) + '\n'
        output.write_text(data, encoding='utf-8')
    elif len(sys.argv) != 1:
        raise SystemExit('usage: python3 VERIFY.py [--certificate EDGE_CERTIFICATES.tsv]')
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
