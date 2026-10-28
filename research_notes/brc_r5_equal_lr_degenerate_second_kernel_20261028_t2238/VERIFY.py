#!/usr/bin/env python3
"""Exact finite two-law sequential likelihood-ratio model; Python stdlib only."""
from fractions import Fraction as F
from itertools import product

r = F(3, 2)
a = b = F(1, 4)
initial = {"A": (a, r), "B": (b, r), "O": (F(1, 2), F(1, 2))}
s = (F(1, 2), r, F(5, 2))
q = (F(1, 4), F(1, 2), F(1, 4))
t = (F(1), r, F(2))
z = {"A": (F(1, 4), F(1, 2), F(1, 4)),
     "B": (F(1, 8), F(3, 4), F(1, 8))}
lam = (F(1), F(3, 2), F(0), F(3, 32))


def check_kernel(parent, values, probs):
    values, probs = tuple(values), tuple(probs)
    assert all(x > 0 for x in probs)
    assert sum(probs) == 1
    assert sum(v * x for v, x in zip(values, probs)) == parent
    p = tuple(v * x / parent for v, x in zip(values, probs))
    assert sum(p) == 1 and all(x > 0 for x in p)


def f(u):
    return min(lam[0] * u, lam[1])


def observation(policy, compressed=False):
    # Policy maps (source,1) and (source,2) to boolean continue decisions.
    # A true terminal tie is consistently resolved as "declare P".
    out = [F(0)] * 4
    Ptot = Qtot = F(0)

    def terminal(Qmass, ratio, time):
        nonlocal Ptot, Qtot
        Pmass = Qmass * ratio
        Ptot += Pmass
        Qtot += Qmass
        if lam[0] * ratio < lam[1]:
            out[0] += Pmass  # declare Q, P-error
        else:
            out[1] += Qmass  # declare P, Q-error
        out[2] += Pmass * time
        out[3] += Qmass * time

    terminal(*initial["O"], 1)
    for src in ("A", "B"):
        Qmass, ratio = initial[src]
        if not policy[(src, 1)]:
            terminal(Qmass, ratio, 1)
            continue
        for child, mass in zip(s, q):
            childmass = Qmass * mass
            if child != r or not policy[(src, 2)]:
                terminal(childmass, child, 2)
            else:
                for last, zmass in zip(t, z[src]):
                    terminal(childmass * zmass, last, 3)
    assert Ptot == Qtot == 1
    return tuple(out)


def L(o):
    return sum(x * y for x, y in zip(lam, o))


check_kernel(1, (initial[k][1] for k in initial),
             (initial[k][0] for k in initial))
check_kernel(r, s, q)
for src in ("A", "B"):
    check_kernel(r, t, z[src])
H = sum(qi * f(si) for si, qi in zip(s, q)) - f(r)
J = {k: sum(zi * f(ti) for ti, zi in zip(t, z[k])) - f(r)
     for k in ("A", "B")}
assert H == -F(1, 4)
assert J == {"A": -F(1, 8), "B": -F(1, 16)}
assert lam[3] == -(a * J["A"] + b * J["B"]) / (a + b)
assert a * q[1] * (J["B"] - J["A"]) * b / (a+b) == F(1, 256)

full = []
for acts in product((False, True), repeat=4):
    policy = dict(zip((("A",1),("B",1),("A",2),("B",2)), acts))
    full.append((L(observation(policy)), acts, observation(policy)))
full.sort()
lr = []
for x, y in product((False, True), repeat=2):
    policy = {(k, 1): x for k in ("A", "B")}
    policy.update({(k, 2): y for k in ("A", "B")})
    lr.append((L(observation(policy, compressed=True)), (x,y), observation(policy, compressed=True)))
lr.sort()
assert full[0][0] + F(1, 256) == lr[0][0]
witness_policy = {("A",1): True,("B",1): True,("A",2): True,("B",2): False}
witness = observation(witness_policy)
assert L(witness) == full[0][0]
assert lam[0] + lam[1] + lam[2] + lam[3] == F(83, 32)
assert (lr[0][0] - L(witness)) / sum(map(abs, lam)) == F(1, 664)

print('GLOBAL MODEL two-law normalization: Q=P=1, all kernels strictly positive')
print('H:', H, 'J_A:', J['A'], 'J_B:', J['B'])
print('lambda:', tuple(map(str, lam)))
print('full optimal L:', full[0][0], 'policies:', [x[1] for x in full if x[0]==full[0][0]])
print('LR optimal L:', lr[0][0], 'policies:', [x[1] for x in lr if x[0]==lr[0][0]])
print('strict signed/nonnegative support gap:', lr[0][0]-full[0][0])
print('full witness O*:', tuple(map(str,witness)))
print('global sup-norm distance lower bound:',F(1,664))
# Verify the general Bellman-threshold certificate across rational model families.
# This is finite regression evidence, not the proof of the all-real theorem.
counts = {"jbar_le_h": 0, "jbar_gt_h": 0}
for k, za, zb, aa, bb in product(
    (F(1, 10), F(1, 5), F(1, 4), F(2, 5)),
    (F(1, 4), F(1, 3), F(2, 5)),
    (F(1, 20), F(1, 8), F(1, 6)),
    (F(1, 8), F(1, 5), F(1, 4)),
    (F(1, 8), F(1, 5), F(1, 4))):
    q = (k, 1-2*k, k)
    z = {"A": (za, 1-2*za, za), "B": (zb, 1-2*zb, zb)}
    a, b = aa, bb
    other_Q = 1-a-b
    other_ratio = (1-r*(a+b)) / other_Q
    initial = {"A": (a, r), "B": (b, r), "O": (other_Q, other_ratio)}
    check_kernel(1, (v[1] for v in initial.values()),
                 (v[0] for v in initial.values()))
    check_kernel(r, s, q)
    for src in ("A", "B"):
        check_kernel(r, t, z[src])
    # A has strictly larger future stop-loss gain than B.
    j_A, j_B = za/F(2), zb/F(2)
    h = k  # for s=(1/2,3/2,5/2), f(u)=min(u,3/2)
    jbar = (a*j_A+b*j_B)/(a+b)
    if jbar <= h:
        beta = jbar
        counts["jbar_le_h"] += 1
    else:
        beta = (h+q[1]*jbar)/(1+q[1])
        counts["jbar_gt_h"] += 1
    lam = (F(1), r, F(0), beta)
    vals_full, vals_lr = [], []
    for acts in product((False, True), repeat=4):
        policy = dict(zip((("A",1),("B",1),("A",2),("B",2)), acts))
        vals_full.append(L(observation(policy)))
    for x, y in product((False, True), repeat=2):
        policy = {(source,1): x for source in ("A", "B")}
        policy.update({(source,2): y for source in ("A", "B")})
        vals_lr.append(L(observation(policy)))
    assert min(vals_lr)-min(vals_full) == q[1]*a*b/(a+b)*(j_A-j_B)
assert sum(counts.values()) == 324
assert all(counts.values())
print('exact rational regression models: 324; beta regimes:', counts)
print('PASS_EXACT_R5_EQUAL_LR_DEGENERATE_SECOND_KERNEL')
