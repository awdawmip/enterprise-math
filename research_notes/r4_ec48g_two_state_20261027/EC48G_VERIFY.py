"""EC48G exact two-memory reconfiguration checker. Author-side only."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from random import Random
import json

def profile_capacity(sign):
    low = [tuple(int(v > 0) for v in row) for row in sign]
    high = [tuple(int(v >= 0) for v in row) for row in sign]
    return max(len(set(low)), len(set(high)))

def signatures(sign):
    tied = [h for h, row in enumerate(sign) if 0 in row]
    C = {tuple(int(v > 0) for v in row) for h, row in enumerate(sign) if h not in tied}
    D = {
        (tuple(int(v >= 0) for v in sign[h]), tuple(int(v > 0) for v in sign[h]))
        for h in tied
        if tuple(int(v >= 0) for v in sign[h]) not in C
        or tuple(int(v > 0) for v in sign[h]) not in C
    }
    return len(C), len(D)

def masks(sign, encoding, K):
    Y = len(sign[0])
    m = [[0] * Y for _ in range(K)]
    for h, row in enumerate(sign):
        for y, v in enumerate(row):
            if v:
                m[encoding[h]][y] |= 1 if v > 0 else 2
    return m

def assert_encoder_reconfiguration(sign):
    """Build valid encoder-graph path joining all tied-one and tied-zero policies."""
    H, Y = len(sign), len(sign[0])
    K = profile_capacity(sign)
    if K > 2:
        return None
    low = [tuple(int(v > 0) for v in row) for row in sign]
    high = [tuple(int(v >= 0) for v in row) for row in sign]
    low_index = {v: k for k, v in enumerate(sorted(set(low)))}
    high_index = {v: k for k, v in enumerate(sorted(set(high)))}
    f_low = [low_index[v] for v in low]
    f_high = [high_index[v] for v in high]
    adj = [set() for _ in range(H)]
    for h in range(H):
        for k in range(h + 1, H):
            if any(sign[h][y] * sign[k][y] == -1 for y in range(Y)):
                adj[h].add(k)
                adj[k].add(h)
    seen = set()
    nontrivial = []
    for h in range(H):
        if h in seen:
            continue
        pending = [h]
        comp = set()
        while pending:
            a = pending.pop()
            if a in seen:
                continue
            seen.add(a)
            comp.add(a)
            pending.extend(adj[a] - seen)
        if len(comp) >= 2:
            nontrivial.append(comp)
    assert len(nontrivial) <= 1
    if nontrivial:
        v = min(nontrivial[0])
        if f_low[v] != f_high[v]:
            assert K == 2
            f_low = [1 - x for x in f_low]
        for v in nontrivial[0]:
            assert f_low[v] == f_high[v]
    target = tuple(f_low)
    current = tuple(f_high)
    path = [current]
    for h in range(H):
        if current[h] == target[h]:
            continue
        assert not adj[h]
        nxt = current[:h] + (target[h],) + current[h + 1:]
        m1, m2 = masks(sign, current, K), masks(sign, nxt, K)
        assert all((m1[m][y] | m2[m][y]) != 3 for m in range(K) for y in range(Y))
        current = nxt
        path.append(current)
    assert current == target
    for f in path:
        assert all(bit != 3 for row in masks(sign, f, K) for bit in row)
    U_hi = [None] * K
    U_lo = [None] * K
    for h in range(H):
        for dec, f, word in ((U_hi, path[0], high[h]), (U_lo, path[-1], low[h])):
            m = f[h]
            if dec[m] is None:
                dec[m] = word
            else:
                assert dec[m] == word
    for dec in (U_hi, U_lo):
        for m in range(K):
            if dec[m] is None:
                dec[m] = (0,) * Y
    for h in range(H):
        for y in range(Y):
            if sign[h][y] == 0:
                assert U_hi[path[0][h]][y] == 1
                assert U_lo[path[-1][h]][y] == 0
    return len(path), len(nontrivial)

def source_signs(P, Q):
    H, Y = len(P), len(P[0])
    Ps, Qs = sum(map(sum, P)), sum(map(sum, Q))
    ratios = [[F(P[h][y] * Qs, Q[h][y] * Ps) for y in range(Y)] for h in range(H)]
    critical = sorted({r for row in ratios for r in row})
    mids = [critical[0] / 2] + [(a + b) / 2 for a, b in zip(critical, critical[1:])] + [critical[-1] + 1]
    cap = max(len({tuple(int(x > threshold) for x in row) for row in ratios}) for threshold in mids)
    return cap, [(r, [[(x > r) - (x < r) for x in row] for row in ratios]) for r in critical]

def explicit_example():
    P = [[1, 1], [2, 2], [2, 3]]
    Q = [[1, 1], [1, 1], [1, 1]]
    K, faces = source_signs(P, Q)
    assert K == 2
    r = F(12, 11)
    sign = next(s for x, s in faces if x == r)
    assert sign == [[-1, -1], [0, 0], [0, 1]]
    assert signatures(sign) == (1, 2)
    assert assert_encoder_reconfiguration(sign) is not None
    n = 0
    for s in (F(0), F(1, 7), F(1, 2), F(2, 3), F(1)):
        for u, v in ((F(0), s), (s, F(1))):
            w = [[F(0), F(0)], [v * u, v], [u, F(1)]]
            alpha = sum(F(P[h][y], 11) * w[h][y] for h in range(3) for y in range(2))
            beta = sum(F(Q[h][y], 6) * w[h][y] for h in range(3) for y in range(2))
            T = u + v + u * v
            assert alpha == F(3 + 2 * T, 11)
            assert beta == F(1 + T, 6)
            assert alpha - r * beta == F(1, 11)
            n += 1
    return {'P': P, 'Q': Q, 'r': str(r), 'K_hull': K, 'C': 1, 'D': 2,
            'old_signature_bank': 3, 'K_seed': 2, 'tied_q_mass_raw_interval': [0, 3],
            'exact_parameter_checks': n}

def main():
    counts = Counter()
    for H, Y in ((3, 3), (4, 2), (4, 3)):
        accepted = 0
        for flat in product((-1, 0, 1), repeat=H * Y):
            sign = [list(flat[h * Y:(h + 1) * Y]) for h in range(H)]
            counts['ternary_sign_tables'] += 1
            if profile_capacity(sign) > 2:
                continue
            accepted += 1
            _, D = signatures(sign)
            if D >= 2:
                counts['ternary_D_ge_2'] += 1
            steps, has_edge = assert_encoder_reconfiguration(sign)
            counts['ternary_eligible'] += 1
            counts['ternary_valid_path_steps'] += steps - 1
            counts['ternary_edge_component_cases'] += has_edge
        counts[f'eligible_H{H}_Y{Y}'] = accepted
    rng = Random(202610270848)
    for _ in range(1200):
        H, Y = rng.randint(3, 8), rng.randint(2, 5)
        profiles = [[rng.randint(1, 8) for _ in range(Y)] for _ in range(2)]
        choice = [rng.randrange(2) for _ in range(H)]
        Q = [[rng.randint(1, 9) for _ in range(Y)] for _ in range(H)]
        P = [[Q[h][y] * profiles[choice[h]][y] for y in range(Y)] for h in range(H)]
        K, faces = source_signs(P, Q)
        assert K <= 2
        counts['positive_rational_models'] += 1
        for _, sign in faces:
            assert profile_capacity(sign) <= K
            assert_encoder_reconfiguration(sign)
            counts['positive_rational_critical_faces'] += 1
    report = {
        'schema': 'EC48G_KHULL_LE_2_SEEDLESS_THEOREM_EXACT_VERIFY_V1',
        'status': 'PASS',
        'arithmetic': 'Python stdlib Fraction; exhaustive finite ternary sign families and seeded positive integer laws',
        'counts': dict(sorted(counts.items())),
        'witness': explicit_example(),
        'scope': 'finite two-stage binary terminal decisions; arbitrary positive rational sources; K_hull <= 2; no persistent common random seed',
        'not_proved': ['K_hull >= 3 universal equality', 'native X6 dynamics', 'independent Driver admission']
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()

