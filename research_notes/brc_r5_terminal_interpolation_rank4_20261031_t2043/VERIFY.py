"""Exact Fraction verification for R5 compensated-source terminal-observer obstruction.

This program verifies a concrete rational example and two rational instances of the
small-sigma universal separator. All-real scope is proved in RESEARCH.md, not by sampling.
Only Python's standard library is needed.
"""
from fractions import Fraction as F
from itertools import product, permutations

ALPHA = (F(1, 4), F(1, 5))
KAPPA = (F(3, 4), F(1, 6))
THETA = F(11, 2)
KEY = {
    'A': (1, F(1)), 'D': (2, F(1, 2)), 'Y': (2, F(3, 2)),
    'C': (2, F(1)), 'DH': (3, F(1, 4)), 'YH': (3, F(2)),
    'L': (3, F(1)), 'L4': (4, F(1)),
}
assert all((1 + k * (1 - 2 * a)) / a == THETA
           for a, k in zip(ALPHA, KAPPA))


def observe(action, response):
    """Return (e_P,e_Q,T_P,T_Q); action(origin,key) is 0/1."""
    out = [F(0)] * 4
    masses = [F(0), F(0)]

    def terminal(q, leaf):
        time, lr = KEY[leaf]
        masses[0] += q
        masses[1] += q * lr
        features = (lr * response[leaf], response[leaf], lr * time, F(time))
        for j in range(4):
            out[j] += q * features[j]

    for i, (a, k) in enumerate(zip(ALPHA, KAPPA)):
        q = F(1, 2)
        if not action(i, 'A'):
            terminal(q, 'A')
            continue
        qd, qy, qc = q * a, q * a, q * (1 - 2 * a)
        if action(i, 'D'):
            terminal(qd * F(2, 3), 'DH')
            terminal(qd * F(1, 3), 'L4' if action(i, 'LD') else 'L')
        else:
            terminal(qd, 'D')
        if action(i, 'Y'):
            terminal(qy * F(1, 2), 'YH')
            terminal(qy * F(1, 2), 'L4' if action(i, 'LY') else 'L')
        else:
            terminal(qy, 'Y')
        terminal(qc * (1 - k), 'C')
        terminal(qc * k, 'L4' if action(i, 'LC') else 'L')
    assert masses == [F(1), F(1)], masses
    return tuple(out)


def lr_obs(bits, response):
    common = dict(zip(('A', 'D', 'Y', 'L'), bits))
    return observe(lambda i, key: common['L' if key in ('LD', 'LY', 'LC') else key], response)


def full_obs(bits, response):
    keys = ('A', 'D', 'Y', 'LD', 'LY', 'LC')
    per_origin = [dict(zip(keys, bits[i * 6: i * 6 + 6])) for i in range(2)]
    return observe(lambda i, key: per_origin[i][key], response)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def leaf_scores(h, response):
    p, q, u, v = h
    return {key: (p * lr + q) * response[key] + (u * lr + v) * time
            for key, (time, lr) in KEY.items()}


def bellman(h, response):
    z = leaf_scores(h, response)
    L = max(z['L'], z['L4'])
    D = max(z['D'], F(2, 3)*z['DH'] + F(1, 3)*L)
    Y = max(z['Y'], F(1, 2)*z['YH'] + F(1, 2)*L)
    F_i = tuple(a*(D+Y) + (1-2*a)*(1-k)*z['C']
                + (1-2*a)*k*L - z['A'] for a, k in zip(ALPHA, KAPPA))
    full = z['A'] + sum((max(F(0), x) for x in F_i), F(0))/2
    lr = z['A'] + max(F(0), F_i[0]+F_i[1])/2
    return full, lr, F_i, (L, D, Y)


def det(matrix):
    value = F(0)
    for perm in permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1,4))
        term = F(-1 if inv % 2 else 1)
        for i,j in enumerate(perm):
            term *= matrix[i][j]
        value += term
    return value


# One common, strictly interior Bernoulli terminal-error response for both policies.
response = {key: F(1, 2) for key in KEY}
response['DH'], response['L4'] = F(5, 8), F(3, 4)
assert all(0 < x < 1 for x in response.values())
assert 2*response['C']-response['A']-response['L'] == 0

H = (F(10), F(9), F(1), F(-2))
all_lr = [lr_obs(a, response) for a in product((0, 1), repeat=4)]
all_full = [full_obs(a, response) for a in product((0, 1), repeat=12)]
max_full = max(dot(H, z) for z in all_full)
max_lr = max(dot(H, z) for z in all_lr)
full_b, lr_b, advantages, downstream = bellman(H, response)
assert (max_full, max_lr) == (full_b, lr_b)
assert advantages == (F(53, 96), -F(37, 120))
assert (max_full, max_lr) == (F(1685, 192), F(2759, 320))
assert max_full - max_lr == F(37, 240)

# FULL chooses A=CONTINUE for origin 0, A=STOP for origin 1;
# D=Y=L=CONTINUE on all reached branches.
full_witness = observe(lambda i, key: i == 0 if key == 'A' else True, response)
assert full_witness == (F(221, 384), F(7, 12), F(107, 48), F(107, 48))
assert dot(H, full_witness) == max_full

# Four affinely independent LR differences: A-stop and four A-continue policies.
policies = [(0,0,0,0), (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,1,0,0)]
points = [lr_obs(b, response) for b in policies]
mat = [[points[i+1][j] - points[0][j] for j in range(4)] for i in range(4)]
det_exact = det(mat)
assert det_exact == F(152361, 1310720000)
assert len(set(all_lr)) == 9
assert len(all_full) == 4096 and len(all_lr) == 16

# Test the separate all-real symbolic separator formula at two rational choices.
for rC, predicted in ((F(3, 4), F(1, 2304)), (F(3, 8), F(1, 4608))):
    r = dict(response)
    r['C'] = rC
    gamma = 2*r['C'] - r['A'] - r['L']
    xi = r['D'] + r['YH']/2 - F(3,2)*r['L'] - (THETA+2)*(r['C']-r['L'])
    sigma = F(1, 64)
    total_alpha = sum(ALPHA)
    bound = THETA + F(7,2) + 4/total_alpha
    assert sigma < min(F(1,2), THETA/(2*bound))
    time_parameter = THETA - sigma*(xi + 2*gamma/total_alpha)
    h=(F(0), sigma, 2*(time_parameter+1), -(2*time_parameter+3))
    full_support, lr_support, F_i, _ = bellman(h, r)
    calculated = full_support-lr_support
    universal = sigma*abs(gamma)*abs(ALPHA[0]-ALPHA[1])/(2*total_alpha)
    assert calculated == universal == predicted
    # Checking the model's actual finite deterministic maximizers.
    assert full_support == max(dot(h,z) for z in (full_obs(a,r) for a in product((0,1),repeat=12)))
    assert lr_support == max(dot(h,z) for z in (lr_obs(a,r) for a in product((0,1),repeat=4)))

print('PARAMETERS alpha=(1/4,1/5) kappa=(3/4,1/6) theta=11/2')
print('ERROR response: 1/2 except r(DH)=5/8, r(L4)=3/4; gamma=0')
print('POLICIES exact FULL=4096 LR=16 distinct_LR=9')
print(f'SUPPORT H=(10,9,1,-2) FULL={max_full} LR={max_lr} GAP={max_full-max_lr}')
print(f'SOURCE_ADVANTAGES F0={advantages[0]} F1={advantages[1]}')
print(f'FULL_WITNESS {full_witness}')
print(f'FOUR_RANK_DET {det_exact}  symbolic=152361*v*w/40960000')
print(f'INF_DISTANCE_LOWER_BOUND {(max_full-max_lr)/sum(map(abs,H))}')
print('SMALL_SIGMA_EXACT_CASES gamma=1/2 gap=1/2304; gamma=-1/4 gap=1/4608')
print('PASS_EXACT_R5_TERMINAL_GAMMA_NECESSARY_NOT_SUFFICIENT_RANK4')
