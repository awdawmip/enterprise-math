#!/usr/bin/env python3
"""Independent exact stdlib verifier for R5 curvature-cone no-go.

No Monte Carlo or floating point is used. Exhausts all 2^18 FULL and 2^7
seedless-LR deterministic policies at 7 exact curvature ratios; the
continuum statement is established separately by a Bellman proof.
"""
from fractions import Fraction as F
from itertools import product
from math import lcm

Q = {(0, 0): F(49, 100), (0, 1): F(1, 100),
     (1, 0): F(1, 100), (1, 1): F(49, 100)}
R = (F(1, 2), F(1), F(3, 2))
t = (F(1, 16), F(1, 8))

def kernel(x, u):
    a = t[x]
    return ((F(1, 2)+a, F(1, 2)-2*a, a) if u == 0
            else (a, F(1, 2)-2*a, F(1, 2)+a))

paths = [(x, u, v, Q[x, u]*kernel(x, u)[v]*R[v],
          Q[x, u]*kernel(x, u)[v])
         for x, u, v in product(range(2), range(2), range(3))]
DEN = lcm(*(z.denominator for row in paths for z in row[-2:]))
assert DEN == 3200 and len(paths) == 12
assert all(p > 0 and q > 0 for _, _, _, p, q in paths)
assert sum(row[-2] for row in paths) == sum(row[-1] for row in paths) == 1
paths = [(x, u, v, int(p*DEN), int(q*DEN)) for x, u, v, p, q in paths]

# Return raw integer numerators for (P(STOP2), Q(STOP2),
# P(STOP5), Q(STOP5), E_P[tau], E_Q[tau]); DEN=3200.
def obs(bits, full):
    out = [0]*6
    for x, u, v, p, q in paths:
        continue2 = (bits >> x) & 1
        continue3 = (bits >> (2 + (2*x+u if full else u))) & 1
        continue4 = (bits >> (6+6*x+3*u+v if full else 4+v)) & 1
        tau = (2 if not continue2 else 3 if not continue3 else
               4 if not continue4 else 5)
        out[4] += tau*p
        out[5] += tau*q
        if tau == 2:
            out[0] += p
            out[1] += q
        elif tau == 5:
            out[2] += p
            out[3] += q
    return out

def det4(rows):
    a = [[F(v) for v in row] for row in rows]
    result = F(1)
    for k in range(4):
        i = next(i for i in range(k, 4) if a[i][k])
        if i != k:
            a[k], a[i] = a[i], a[k]
            result = -result
        pivot = a[k][k]
        result *= pivot
        for j in range(k+1, 4):
            factor = a[j][k]/pivot
            for m in range(k, 4):
                a[j][m] -= factor*a[k][m]
    return result

# Five actual seedless-LR deterministic policies always continue at t=2;
# therefore S_2^P=S_2^Q=0, and rank is independent of c.
indices = (3, 7, 11, 23, 39)
base = obs(indices[0], False)
rank_rows = []
for i in indices[1:]:
    o = obs(i, False)
    rank_rows.append([F(o[j]-base[j], DEN) for j in (2, 3, 4, 5)])
rank_det = det4(rank_rows)
assert rank_det == F(67199, 20480000), rank_det

# H = 3 T_P -147/64 T_Q -2 (r S_2^P+S_5^P)
#     +83/64 (r S_2^Q+S_5^Q), with r=c/d.
# Multiply by 64 * denominator(r) * DEN for exact integer maxima.
ratios = (F(-4,357), F(-1,100), F(0), F(1,3), F(1), F(3), F(100))
max_values = {r: {} for r in ratios}
winners = {r: {} for r in ratios}
for full, total in ((False, 1 << 7), (True, 1 << 18)):
    for i in range(total):
        s2p, s2q, s5p, s5q, tp, tq = obs(i, full)
        common = 192*tp - 147*tq -128*s5p +83*s5q
        early = -128*s2p +83*s2q
        for r in ratios:
            score = r.denominator*common+r.numerator*early
            if full not in max_values[r] or score > max_values[r][full]:
                max_values[r][full] = score
                winners[r][full] = i

print('PATHS', len(paths), 'DENOMINATOR', DEN)
print('FULL_BOOLEAN_POLICIES', 1 << 18, 'LR_BOOLEAN_POLICIES', 1 << 7)
print('RANK4_STOP5_BASE_DET', rank_det, 'INDICES', indices)
for r in ratios:
    lr = F(max_values[r][False], 64*r.denominator*DEN)
    full = F(max_values[r][True], 64*r.denominator*DEN)
    assert lr == F(4787,1600), (r,lr)
    assert full == F(19149,6400), (r,full)
    assert full-lr == F(1,6400)
    print('RATIO',r,'FULL',full,'LR',lr,
          'GAP',full-lr,'WINNERS',winners[r])

# Error example: eps2=eps5=5/8, eps3=eps4=1/2 => A=1/2,B=0,c=d=1/8.
eps = (F(5,8), F(1,2), F(1,2), F(5,8))
A, B = eps[1], eps[2]-eps[1]
c = eps[0]-2*eps[1]+eps[2]
d = eps[3]-2*eps[2]+eps[1]
assert all(0 < z < 1 for z in eps) and (c,d)==(F(1,8),F(1,8))
assert [A+B*j+c*(j==2)+d*(j==5) for j in (2,3,4,5)] == list(eps)
print('VALID_ERROR_EXAMPLE',eps,'c',c,'d',d,'LIFTED_DET',rank_det*d*d)
print('PASS_EXACT_R5_STOP_TIME_CURVATURE_CONE_NO_GO')
