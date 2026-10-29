"""Exact rational certificate: perturbing one double-collision LR fiber.
Auxiliary finite dual-law stopping model; no native X6 computation.
"""
from fractions import Fraction as F

EPS = F(1, 1000)
ETA = F(1, 1000)
roots = {'A': (F(1, 3), F(2, 3)), 'B': (F(2, 3), F(1, 3))}
y = {'A': (F(1, 2), F(1, 4)), 'B': (F(1, 4), F(1, 2))}
z = {('A', 1): (F(1, 2), F(1, 4)),
     ('B', 1): (F(2, 3), F(1, 3)),
     ('A', 0): (F(1, 2), F(2, 5)),
     ('B', 0): (F(1, 2), F(3, 5))}

mass = {}
for s, (p, q) in roots.items():
    mass[(s,)] = p, q
    for yy in (0, 1):
        py, qy = y[s]
        p2 = p * (py if yy else 1-py)
        q2 = q * (qy if yy else 1-qy)
        mass[(s, yy)] = p2, q2
        for zz in (0, 1):
            pz, qz = z[s, yy]
            mass[(s, yy, zz)] = (p2*(pz if zz else 1-pz),
                                 q2*(qz if zz else 1-qz))

leaves = tuple((h, mass[h]) for h in mass if len(h) == 3)
full_keys = tuple(sorted(mass, key=str))
lr_key = lambda h: (len(h), mass[h][0] / mass[h][1])
lr_keys = tuple(sorted(set(map(lr_key, mass))))
assert len(full_keys) == 14 and len(lr_keys) == 12
assert all(p > 0 and q > 0 for p, q in mass.values())
assert all(0 < a < 1 and 0 < b < 1 for a, b in list(y.values())+list(z.values()))
assert sum(p for h, (p, q) in leaves) == sum(q for h, (p, q) in leaves) == 1
assert lr_key(('A', 1)) == lr_key(('B', 1)) == (2, F(1))
assert lr_key(('A', 1, 1)) == lr_key(('B', 1, 1)) == (3, F(2))
assert z[('A', 1)] != z[('B', 1)]
assert mass[('A', 1)] == mass[('B', 1)] == (F(1, 6), F(1, 6))


def errors(t, h):
    lr = mass[h][0]/mass[h][1]
    dp = (int(h == ('A', 1)) - int(h == ('B', 1))) if t == 2 else 0
    dq = (int(h == ('A', 1, 1)) - int(h == ('B', 1, 1))) if t == 3 else 0
    return (F(1, 5)+F(t, 20)+F(t+1, 100)/lr+EPS*dp,
            F(2, 5)-F(t, 30)+F(t+2, 200)*lr+ETA*dq)

assert all(0 < rate < 1 for h in mass
           for t in ([len(h)] if len(h) < 3 else [3, 4])
           for rate in errors(t, h))

# Each natural leaf is counted under its original P/Q mass.
def observation(mask, keys, lr=False):
    flags = {key: (mask >> i) & 1 for i, key in enumerate(keys)}
    ep = eq = tp = tq = F(0)
    for (s, yy, zz), (p, q) in leaves:
        path = ((s,), (s, yy), (s, yy, zz))
        t, h = 4, path[-1]
        for stage, prefix in enumerate(path, start=1):
            k = lr_key(prefix) if lr else prefix
            if flags[k]:
                t, h = stage, prefix
                break
        a, b = errors(t, h)
        ep += p*a
        eq += q*b
        tp += p*t
        tq += q*t
    return ep, eq, tp, tq


def score(o):
    ep, eq, tp, tq = o
    return 10000*ep - 499*tp - 99*tq

# Exhaust all deterministic policies: multilinearity then covers real hazards.
# Validate the exact full observation gauge and the perturbed residue.
LR_MAX = None
FULL_MAX = None
LR_arg = FULL_arg = None
for is_lr, keys in ((True, lr_keys), (False, full_keys)):
    maximum = None
    maximizer = None
    for mask in range(1 << len(keys)):
        o = observation(mask, keys, lr=is_lr)
        ep, eq, tp, tq = o
        qres = eq - F(41, 100)-tp/F(200)+tq/F(30)
        assert abs(qres) <= ETA/F(10)
        residue = ep-F(21, 100)-tp/F(20)-tq/F(100)
        assert abs(residue) <= F(1, 6)*EPS
        val = score(o)
        if maximum is None or val > maximum:
            maximum = val
            maximizer = mask
    if is_lr:
        LR_MAX, LR_arg = maximum, maximizer
    else:
        FULL_MAX, FULL_arg = maximum, maximizer

witness_mask = 1 << full_keys.index(('A', 1))
witness = observation(witness_mask, full_keys)
assert witness == (F(2581, 6000), F(551, 1800), F(11, 3), F(11, 3)), witness
assert score(witness) == 2109
assert LR_MAX == 2108, LR_MAX
assert FULL_MAX == 2109, FULL_MAX
assert observation(0, lr_keys, lr=True) == (F(45, 100), F(89, 300), F(4), F(4))
assert score(observation(0, lr_keys, lr=True)) == 2108
def rank(rows):
    pivot_rows = []
    for vec in rows:
        a = list(vec)
        for k, row in pivot_rows:
            c = a[k]
            if c:
                a = [v - c*r for v, r in zip(a, row)]
        nonzero = [i for i, x in enumerate(a) if x]
        if nonzero:
            k = nonzero[0]
            pivot_rows.append((k, [v/a[k] for v in a]))
            pivot_rows.sort(key=lambda pair: pair[0])
    return len(pivot_rows)

def det4(rows):
    a = [list(row) for row in rows]
    out = F(1)
    for k in range(4):
        p = next(i for i in range(k, 4) if a[i][k])
        if p != k:
            a[k], a[p] = a[p], a[k]
            out = -out
        pivot = a[k][k]
        out *= pivot
        for i in range(k+1, 4):
            ratio = a[i][k]/pivot
            for j in range(k, 4):
                a[i][j] -= ratio*a[k][j]
    return out

for is_lr, keys in ((True, lr_keys), (False, full_keys)):
    base = observation(0, keys, lr=is_lr)
    basis = []
    for mask in range(1, 1 << len(keys)):
        vec = tuple(u-v for u, v in zip(observation(mask, keys, lr=is_lr), base))
        if rank([v for _, v in basis] + [vec]) > len(basis):
            basis.append((mask, vec))
            if len(basis) == 4:
                break
    assert len(basis) == 4, basis
    determinant = det4([vec for _, vec in basis])
    assert determinant != 0
    expected_masks = [1, 2, 9, 512] if is_lr else [1, 2, 8, 32]
    expected_det = -F(1, 144000000) if is_lr else F(1, 8640000000)
    assert [m for m, _ in basis] == expected_masks
    assert determinant == expected_det
    print(('LR' if is_lr else 'FULL')+'_AFFINE_RANK', len(basis), 'WITNESS_MASKS', [m for m, _ in basis], 'DET', determinant, 'DET_DIV_EPS_ETA', determinant/(EPS*ETA))

print('FREEZE EPS', EPS, 'ETA', ETA)
print('FULL_KEYS', len(full_keys), 'DETERMINISTIC', 1 << len(full_keys), 'ORDER', full_keys)
print('LR_KEYS', len(lr_keys), 'DETERMINISTIC', 1 << len(lr_keys), 'ORDER', lr_keys)
print('FIRST_COLLISION', mass[('A', 1)], mass[('B', 1)], lr_key(('A', 1)))
print('SECOND_COLLISION', lr_key(('A', 1, 1)), lr_key(('B', 1, 1)))
print('FULL_WITNESS', tuple(map(str, witness)))
print('LR_SUPPORT_MAX', LR_MAX, 'FULL_SUPPORT_MAX', FULL_MAX, 'GAP', FULL_MAX-LR_MAX)
print('LINF_DISTANCE_LOWER_BOUND', F(1, 10598))
print('PASS_EXACT_R5_DOUBLE_COLLISION_FULL_RANK_PERTURBATION')
