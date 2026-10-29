"""Exact all-signed/full-image certificate for the two-collision auxiliary stopping tree.
Uses only Python's standard library, with exact fractions and exhaustive binary corners.
"""
from fractions import Fraction as F
from itertools import product

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
        p2, q2 = p * (py if yy else 1-py), q * (qy if yy else 1-qy)
        mass[(s, yy)] = p2, q2
        for zz in (0, 1):
            pz, qz = z[s, yy]
            mass[(s, yy, zz)] = (p2 * (pz if zz else 1-pz),
                                 q2 * (qz if zz else 1-qz))

leaves = tuple((h, m) for h, m in mass.items() if len(h) == 3)
full_keys = tuple(sorted(mass, key=str))
lr_key = lambda h: (len(h), mass[h][0] / mass[h][1])
lr_keys = tuple(sorted(set(map(lr_key, mass))))
assert len(full_keys) == 14 and len(lr_keys) == 12
assert all(0 < p and 0 < q for p, q in mass.values())
assert sum(p for _, (p, _) in leaves) == sum(q for _, (_, q) in leaves) == 1
assert lr_key(('A', 1)) == lr_key(('B', 1)) == (2, F(1))
assert lr_key(('A', 1, 1)) == lr_key(('B', 1, 1)) == (3, F(2))
assert z['A', 1] != z['B', 1]

# Terminal P-law and Q-law error Bernoulli rates (strictly between 0 and 1).
def errors(t, h):
    lr = mass[h][0] / mass[h][1]
    return (F(1, 5) + F(t, 20) + F(1+t, 100) / lr,
            F(2, 5) - F(t, 30) + F(t+2, 200) * lr)

assert all(0 < v < 1 for h in mass for t in ([len(h)] if len(h)<3 else [3, 4]) for v in errors(t,h))

def observation(bits, keys, method, check_errors=False):
    flags = dict(zip(keys, bits))
    tp = tq = ep = eq = F(0)
    for (s, yy, zz), (p, q) in leaves:
        paths = ((s,), (s, yy), (s, yy, zz))
        t = 4
        used_path = paths[-1]
        for j, h in enumerate(paths, 1):
            if flags[h if method == 'FULL' else lr_key(h)]:
                t, used_path = j, h
                break
        tp += p*t
        tq += q*t
        if check_errors:
            pe, qe = errors(t, used_path)
            ep += p*pe
            eq += q*qe
    if check_errors:
        assert ep == F(21,100) + tp/F(20) + tq/F(100)
        assert eq == F(41,100) + tp/F(200) - tq/F(30)
    return tp, tq

def polygon(pts):
    pts = sorted(set(pts))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

LR = [observation(tuple((i >> j) & 1 for j in range(len(lr_keys))),
                  lr_keys, 'LR', True) for i in range(1 << len(lr_keys))]
FULL = [observation(bits, full_keys, 'FULL', True)
        for bits in product((0, 1), repeat=len(full_keys))]
Hlr, Hfull = polygon(LR), polygon(FULL)
assert len(Hlr) == len(Hfull) == 13 and set(Hlr) == set(Hfull)
print('FULL deterministic', len(FULL), 'distinct', len(set(FULL)))
print('LR deterministic', len(LR), 'distinct', len(set(LR)))
print('COMMON_POLYGON_VERTICES', len(Hlr))
for v in Hlr:
    print('V', v[0], v[1])

# Each edge's full-support corner graph is connected, which ensures an
# entire continuous boundary loop in the LR hypercube (winding lemma).
edge_sizes = []
for k, u in enumerate(Hlr):
    v = Hlr[(k + 1) % len(Hlr)]
    a, b = u[1]-v[1], v[0]-u[0]
    c = a*u[0] + b*u[1]
    assert all(a*p[0] + b*p[1] >= c for p in FULL)
    corners = {i for i, p in enumerate(LR) if a*p[0] + b*p[1] == c}
    assert any(LR[i] == u for i in corners)
    assert any(LR[i] == v for i in corners)
    connected = {next(iter(corners))}
    stack = list(connected)
    while stack:
        cur = stack.pop()
        for j in range(len(lr_keys)):
            nei = cur ^ (1 << j)
            if nei in corners and nei not in connected:
                connected.add(nei)
                stack.append(nei)
    assert connected == corners
    edge_sizes.append(len(corners))
    print('EDGE', k, 'normal', a, b, 'threshold', c,
          'optimal_corners', len(corners), 'connected', True)
print('EDGE_CORNER_COUNTS', edge_sizes)
print('PASS_EXACT_R5_DOUBLE_COLLISION_WINDING_IMAGE_EQUALITY')
