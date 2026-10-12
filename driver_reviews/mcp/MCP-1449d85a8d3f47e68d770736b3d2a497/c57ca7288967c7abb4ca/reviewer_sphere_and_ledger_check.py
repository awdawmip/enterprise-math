"""Scope-specific nonauthor review check of frozen p17/order1 evidence.

No producer/checker imports, no author execution, no research beyond the
frozen bounded child. Full sphere recursion has no nonpreferred label gate.
An alternate six-column representative checks complete coset invariance.
"""
from fractions import Fraction as Q
from decimal import Decimal
from pathlib import Path
from itertools import combinations
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'source'
DIM = 16
P = 17
BUDGET = 2331
AUTHORS = ['EM-DIRECT-E1F2B6', 'EM-DIRECT-FA0C27', 'EM-DIRECT-49ADE6',
           'EM-DVR-C1A1D9', 'EM-DVR-4C90FB', 'EM-DVR-FBF223', 'EM-T6-B4F89F']


def need(c, where):
    if not c:
        raise AssertionError(where)


def pairs(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def rat(x):
    need(type(x) is list and len(x) == 2, 'rational shape')
    need(all(type(t) is int for t in x) and x[1] > 0, 'rational integers')
    return Q(*x)


def no_duplicate(p):
    d = {}
    for k, v in p:
        need(k not in d, 'duplicate JSON key')
        d[k] = v
    return d


def load(p):
    return json.loads(p.read_bytes(), parse_float=Decimal, object_pairs_hook=no_duplicate)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q())


def det(a):
    # Fraction-preserving row elimination, independent of producer Bareiss.
    a = [[Q(x) for x in row] for row in a]
    n = len(a)
    out = Q(1)
    for k in range(n):
        pivot = next((j for j in range(k, n) if a[j][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            out = -out
        q = a[k][k]
        out *= q
        for j in range(k+1, n):
            scale = a[j][k]/q
            a[j] = [v-scale*w for v, w in zip(a[j], a[k])]
    return out


def gs(rows):
    orthogonal, norms, coefficients = [], [], []
    for row in rows:
        original = list(map(Q, row))
        v = original[:]
        coeff = []
        for b, n in zip(orthogonal, norms):
            t = dot(original, b)/n
            coeff.append(t)
            v = [x-t*y for x, y in zip(v, b)]
        n = dot(v, v)
        need(n > 0, 'nonsingular GS')
        orthogonal.append(v)
        norms.append(n)
        coefficients.append(coeff)
    for i in range(DIM):
        for j in range(i):
            need(dot(orthogonal[i], orthogonal[j]) == 0, 'GS orthogonality')
        rebuilt = [orthogonal[i][s] + sum(coefficients[i][j]*orthogonal[j][s]
                                            for j in range(i)) for s in range(DIM)]
        need(rebuilt == rows[i], 'exact GS row reconstruction')
    return orthogonal, norms, coefficients


def residues(u, m=None):
    return [(sum(u[s-1]*pow(s, -k, P**k) for s in range(1, DIM+1))
              + (0 if m is None else pow(m, -k, P**k))) % P**k
            for k in range(1, 7)]


def alternative_rep(r):
    # Use columns 11..16, unlike the producer's 1..6 construction.
    m = P**6
    a = [[pow(s, -k, m) for s in range(11, 17)] + [-pow(P+r, -k, m) % m]
         for k in range(1, 7)]
    for k in range(6):
        j = next(i for i in range(k, 6) if a[i][k] % P)
        a[k], a[j] = a[j], a[k]
        inv = pow(a[k][k], -1, m)
        a[k] = [(v*inv) % m for v in a[k]]
        for i in range(6):
            if i == k:
                continue
            scale = a[i][k]
            a[i] = [(v-scale*w) % m for v, w in zip(a[i], a[k])]
    u = [0]*10 + [row[-1] for row in a]
    need(residues(u, P+r) == [0]*6, 'alternate representative original mixed rows')
    return u


def bracket(c):
    t = -c
    lo = t.numerator // t.denominator
    return [lo] if t.denominator == 1 else [lo, lo+1]


def pref(c):
    b = bracket(c)
    return (b[0], None) if len(b) == 1 else tuple(sorted(b, key=lambda z:(abs(z+c), z)))


def factors(m):
    return [q for q in range(2, m+1)
            if m % q == 0 and all(q % d for d in range(2, q))]


def direct_sphere(r, basis, stars, D, mu, oldrep):
    radius = (2043-17*r)**2 + BUDGET**2
    u0 = alternative_rep(r)
    need(residues([a-b for a, b in zip(u0, oldrep)]) == [0]*6,
         'two representatives differ in full mixed kernel')
    w = [(P*(s+1)-1)*v for s, v in enumerate(u0)]
    h = [dot(w, v)/d for v, d in zip(stars, D)]
    need(sum(d*x*x for d, x in zip(D, h)) == dot(w,w), 'alternate offset full GS identity')
    z = [0]*DIM
    trace, leaves = [], []

    def visit(i, spent):
        if i < 0:
            u = [u0[s]+sum(z[j]*basis[j][s] for j in range(DIM)) for s in range(DIM)]
            weighted = [(P*(s+1)-1)*v for s,v in enumerate(u)]
            need(dot(weighted, weighted) == spent and residues(u,P+r) == [0]*6,
                 'direct sphere leaf invariant')
            leaves.append(dict(q0=u, squared_norm=pairs(spent)))
            return
        c = h[i]+sum(mu[j][i]*z[j] for j in range(i+1,DIM))
        choices = bracket(c)
        for t in choices:
            total = spent+D[i]*(t+c)**2
            keep = total <= radius
            trace.append(dict(i=i, higher_coefficients=z[i+1:], center=pairs(c),
                              bracket_choices=choices, chosen=t, prior_norm=pairs(spent),
                              norm=pairs(total), admitted=keep))
            if keep:
                z[i] = t
                visit(i-1, total)
    visit(DIM-1,Q())
    need(not leaves, 'full necessary sphere has a survivor')
    return dict(r=r, radius_squared=radius, alternate_q0=u0,
                alternate_original_mixed_residues=residues(u0,P+r),
                alternate_affine_h=[pairs(x) for x in h],
                tested_coordinate_choices=len(trace),
                pruned_choices=sum(not x['admitted'] for x in trace),
                sphere_leaves=leaves, trace=trace)


def main():
    cert = load(SRC/'p17_q0_certificate.json')
    ledger = load(ROOT/'checks/UNPACKED_LEDGER.json')
    bound = load(SRC/'P17_ORDER1_BRANCH_BOUND_RESULTS.json')
    B = cert['unweighted_basis']
    W = cert['weighted_basis']
    need(len(B) == DIM and all(len(r) == DIM for r in B), 'all 16 coordinates')
    need(all(type(v) is int for r in B for v in r), 'integer basis')
    need(W == [[(P*(s+1)-1)*v for s,v in enumerate(row)] for row in B], 'weights')
    determinant = det(B)
    need(abs(determinant) == P**21, 'exact kernel-index determinant')
    need(all(residues(row) == [0]*6 for row in B), 'basis mixed-congruence membership')
    unit_minor = det([[pow(s,-k,P) for s in range(1,7)] for k in range(1,7)])
    alternate_minor = det([[pow(s,-k,P) for s in range(11,17)] for k in range(1,7)])
    need(unit_minor.denominator == alternate_minor.denominator == 1 and
         int(unit_minor) % P != 0 and int(alternate_minor) % P != 0, 'two unit minors')
    stars, D, mu = gs(W)
    need(D == [rat(x) for x in cert['gram_schmidt_squared']], 'all exact frozen GS norms')
    max_radius = 2026**2+BUDGET**2
    need(min(D) > max_radius and 3*min(D) > 4*max_radius, 'sphere and label coverage bounds')
    need([row['r'] for row in ledger['rows']] == list(range(1,17)), 'complete ordered row domain')
    counts, check_rows, actual = [], [], []
    path_count = step_count = 0
    for row in ledger['rows']:
        r = row['r']
        f = factors(P+r)
        need(row['cofactor'] == P+r and row['prime_divisors'] == f, 'row arithmetic domain')
        if max(f) > P:
            need(row['status'] == 'OUTSIDE_MAXIMAL_P17_DOMAIN' and
                 row['affine_paths_evaluated'] == 0 and row['relaxed_class_empty_claim'] is False,
                 'outside is not relaxed EMPTY')
            check_rows.append(dict(r=r,status='OUTSIDE_MAXIMAL_P17_DOMAIN',prime_divisors=f))
            continue
        actual.append(r)
        radius = (2043-17*r)**2+BUDGET**2
        labels = [[]] + [[i] for i,d in enumerate(D) if d <= 4*radius]
        labels += [list(ij) for ij in combinations(range(DIM),2) if sum(D[i] for i in ij) <= 4*radius]
        need(row['allowed_nonpreferred_sets'] == labels, 'complete independently derived labels')
        need(row['R2'] == radius and row['q1_cost'] == P*(P+r)-1, 'original side budgets')
        saved = bound['classes'][r-1]
        need(saved['weighted_leaf_bound'] == len(labels), 'frozen branch bound label count')
        u0 = row['particular_q0']
        need(residues(u0,P+r) == row['particular_mixed_residues'] == [0]*6, 'saved offset original mixed rows')
        w = [(P*(s+1)-1)*v for s,v in enumerate(u0)]
        h = [dot(w,v)/d for v,d in zip(stars,D)]
        need([pairs(x) for x in h] == row['affine_h_coordinates'], 'all saved affine h')
        need(sum(d*x*x for d,x in zip(D,h)) == dot(w,w), 'saved offset full GS identity')
        need(len(row['paths']) == len(labels), 'one saved trace for every eligible label')
        decisions = 0
        for label,path in zip(labels,row['paths']):
            need(path['nonpreferred_indices'] == label, 'ordered exhaustive path labels')
            z = [0]*DIM
            spent = Q()
            steps = path['steps']
            for t,step in enumerate(steps):
                i = DIM-1-t
                c = h[i]+sum(mu[j][i]*z[j] for j in range(i+1,DIM))
                preferred,other = pref(c)
                chosen = other if i in label else preferred
                need(chosen is not None, 'distinct chosen branch')
                need(step['i'] == i and rat(step['center']) == c and
                     step['preferred'] == preferred and step['other'] == other and
                     step['chosen'] == chosen and step['nonpreferred'] is (i in label), 'saved exact integer decision')
                q = D[i]*(chosen+c)**2
                if i in label:
                    need(q >= D[i]/4, 'nonpreferred branch lower cost')
                spent += q
                need(rat(step['contribution']) == q and rat(step['partial_norm_squared']) == spent,
                     'every saved rational pruning contribution')
                z[i] = chosen
                need(t == len(steps)-1 or spent <= radius, 'no computation past prior strict prune')
            need(steps and spent > radius and path['status'] == 'EXACT_NORM_PRUNED' and
                 path['stopping_index'] == steps[-1]['i'] and
                 path['coordinate_decisions'] == len(steps) and rat(path['partial_norm_squared']) == spent,
                 'strict final pruning certificate')
            decisions += len(steps)
        need(row['affine_paths_evaluated'] == len(labels) and row['coordinate_decisions'] == decisions and
             row['local_survivor_count'] == 0 and row['status'] == 'EMPTY_BY_COMPLETE_EXACT_SEARCH', 'row conclusion')
        path_count += len(labels)
        step_count += decisions
        counts.append(dict(r=r,eligible_labels=len(labels),saved_decisions=decisions))
        check_rows.append(direct_sphere(r,B,stars,D,mu,u0))
    need(actual == [1,3,4,5,7,8,9,10,11,13,15,16], 'exact maximal-p17 admissible domain')
    need(path_count == ledger['affine_paths_evaluated'] == 299 and
         step_count == ledger['coordinate_decisions'] == 1490 and ledger['local_survivor_count'] == 0,
         'counts derived after actual arithmetic audit')
    need(ledger['p17_higher_orders_claim'] is False and ledger['global_T6_completion_claim'] is False and
         ledger['p19_campaign_replayed'] is False, 'bounded claim scope')
    out = dict(schema='T6_NONAUTHOR_DRIVER_FROZEN_REVIEW_CHECK_V1',status='PASS',
               reviewer_id='EM-DVR-4CF7AF', reviewer_contribution_ids=['EM-DVR-4CF7AF'],
               retained_result_author_ids=AUTHORS, context='SHARED_TRUSTED_OWNER_NONBLIND_DIRECTED_SOURCE_EXPOSURE',
               result_id='RR-81586AD70E1CEA1B7140', result_sha256=hashlib.sha256((SRC/'RR-81586AD70E1CEA1B7140.json').read_bytes()).hexdigest(),
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               basis_determinant=pairs(determinant),kernel_index=P**21,
               first_minor_residue=int(unit_minor)%P,alternate_minor_residue=int(alternate_minor)%P,
               min_GS_norm=pairs(min(D)),max_radius_squared=max_radius,
               floor_ceil_margin=pairs(min(D)-max_radius),at_most_two_nonpreferred_margin=pairs(3*min(D)-4*max_radius),
               saved_label_paths_independently_derived_and_arithmetic_checked=path_count,
               saved_coordinate_decisions_arithmetic_checked=step_count,
               per_class_saved_coverage=counts,
               full_sphere_strategy='ALL_FLOOR_CEIL_BRANCHES_NO_LABEL_GATE_ALTERNATE_COLUMNS_11_TO_16_REPRESENTATIVES',
               direct_sphere_coordinate_choices=sum(x.get('tested_coordinate_choices',0) for x in check_rows),
               direct_sphere_complete_leaves=0,rows=check_rows,
               closed_scope='ONLY_MAXIMAL_P17_TOTAL_VERTICAL_ORDER1_WITH_ORIGINAL_SEPARATE_BUDGETS_2331',
               p19_or_order0_reverified=False,higher_orders_or_global_threshold_claim=False,
               formal_kernel_check=False)
    p = ROOT/'checks/REVIEWER_EXACT_CHECK_RECEIPT.json'
    need(not p.exists(), 'immutable local receipt already exists')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','basis_determinant','first_minor_residue','alternate_minor_residue',
          'saved_label_paths_independently_derived_and_arithmetic_checked','saved_coordinate_decisions_arithmetic_checked',
          'direct_sphere_coordinate_choices','direct_sphere_complete_leaves','script_sha256']}))


if __name__ == '__main__':
    main()
