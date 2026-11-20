"""R762GQ: exact rational second moment/variance of moving-Port absorption.
Python 3 standard library. Does not model an admitted native TRIADIC_CLOSURE_E event.
"""
from collections import deque
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, permutations

E = tuple(combinations(range(4), 2))
S = [tuple(E.index(tuple(sorted((v, u)))) for u in range(4) if u != v)
     for v in range(4)]
I = tuple(range(6))
P = [p for p in permutations(I)
     if sum(p[a] > p[b] for a in I for b in range(a + 1, 6)) % 2 == 0]
PI = {p: i for i, p in enumerate(P)}

def mul(p, q):
    return tuple(p[q[i]] for i in I)

def cycle(star):
    q = list(I)
    a, b, c = star
    q[a], q[b], q[c] = b, c, a
    return tuple(q)

G = [cycle(s) for s in S]
N = [tuple(g.index(i) for i in I) for g in G]
# Every one of the four legal signed source branches retains multiplicity.
arcs = [[PI[mul(p, G[v] if sign == 1 else N[v])]
         for v in E[p[0]] for sign in (-1, +1)] for p in P]
absorbing = {i for i, p in enumerate(P) if p[0] == E.index((2, 3))}
assert len(P) == 360 and len(absorbing) == 60
assert all(all(j in absorbing for j in arcs[i]) for i in absorbing)
initial = PI[I]
reachable = {initial}
queue = deque([initial])
while queue:
    i = queue.popleft()
    for j in arcs[i]:
        if j not in reachable:
            reachable.add(j)
            queue.append(j)
transient = reachable - absorbing
assert len(reachable) == 350 and len(transient) == 290

# Exact eight-event survival bound uniformly over reachable transient states.
h = [int(i in transient) for i in range(360)]
for _ in range(8):
    h = [sum(h[j] for j in arcs[i]) if i in transient else 0
         for i in range(360)]
max_survivors = max(h[i] for i in transient)
assert max_survivors == 39652
q = Fraction(max_survivors, 4 ** 8)  # 9913/16384

# S_m = Pr(tau > m), computed by nonnegative exact BRC source counts.
N_HORIZON = 600
source = [0] * 360
source[initial] = 1
S_prob = []
check = {}
denominator = 1
for m in range(N_HORIZON + 1):
    count = sum(source)
    S_prob.append(Fraction(count, denominator))
    if m in (0, 8, 12, 16, 600):
        check[m] = (count, denominator)
    if m == N_HORIZON:
        break
    nxt = [0] * 360
    for i in transient:
        if source[i]:
            for j in arcs[i]:
                if j in transient:
                    nxt[j] += source[i]
    source = nxt
    denominator *= 4
assert check[12][0] == 6534252
assert check[16][0] == 1118196052

# Survival identities for integer tau >=1:
# E[tau] = sum_{m>=0} S_m, E[tau^2] = sum_{m>=0} (2m+1) S_m.
mean_lo = sum(S_prob[:N_HORIZON])
second_lo = sum((2*m+1)*S_prob[m] for m in range(N_HORIZON))
# S_{N+8j+r} <= S_N*q^j, 0 <= r <= 7, all j >=0.
mean_tail = 8*S_prob[N_HORIZON]/(1-q)
second_tail = S_prob[N_HORIZON]*(
    Fraction(16*N_HORIZON+64, 1)/(1-q)
    + 128*q/(1-q)**2)
mean_hi = mean_lo + mean_tail
second_hi = second_lo + second_tail
var_lo = second_lo - mean_hi**2
var_hi = second_hi - mean_lo**2

def rational_between(lo, hi, lower_decimal, upper_decimal):
    assert Fraction(lower_decimal) < lo <= hi < Fraction(upper_decimal)

rational_between(mean_lo, mean_hi,
                 '12.93946845281426419721', '12.93946845281426419722')
rational_between(second_lo, second_hi,
                 '263.58902488422540237226', '263.58902488422540237227')
rational_between(var_lo, var_hi,
                 '96.15918104284983428470', '96.15918104284983428471')

print('ROTATION_STATES=360 REACHABLE=350 TRANSIENT=290 ABSORBING=60')
print('EIGHT_STEP_MAX=', max_survivors, 'of', 4**8, 'q=', q)
print('SOURCE_COUNTS=', check)
print('MEAN_INTERVAL=(12.93946845281426419721, 12.93946845281426419722)')
print('SECOND_MOMENT_INTERVAL=(263.58902488422540237226, 263.58902488422540237227)')
print('VARIANCE_INTERVAL=(96.15918104284983428470, 96.15918104284983428471)')
with localcontext() as ctx:
    ctx.prec = 35
    def fmt(fr):
        return str(Decimal(fr.numerator)/Decimal(fr.denominator))
    print('MEAN_TAIL_UPPER=', fmt(mean_tail))
    print('SECOND_TAIL_UPPER=', fmt(second_tail))
print('PASS')
