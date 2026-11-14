#!/usr/bin/env python3
"""Exact rational tests for the R5 one-scalar-gate lift (auxiliary P/Q model)."""
from fractions import Fraction as F
from random import Random

R2 = (F(3, 4), F(5, 4))
R3 = (F(1, 2), F(1), F(3, 2))
R4 = (F(1, 10), F(1), F(19, 10))
Q2 = (F(1, 2), F(1, 2))
Q3 = ((F(13, 20), F(1, 5), F(3, 20)),
      (F(1, 40), F(9, 20), F(21, 40)))
Q4 = {(i, j): ((F(509, 900), F(382, 900), F(9, 900)) if j == 0 else
               (F(9, 900), F(382, 900), F(509, 900)) if j == 2 else
               (F(47, 180), F(43, 90), F(47, 180)) if i == 0 else
               (F(67, 162), F(14, 81), F(67, 162)))
      for i in range(2) for j in range(3)}
R = tuple(sorted(set((F(1),) + R2 + R3 + R4)))
alpha, beta = Q4[0, 1][0], Q4[1, 1][0]
delta = beta - alpha
assert delta == F(247, 1620)
assert len(R) == 7
for i in range(2):
    assert sum(Q3[i]) == 1 and sum(Q3[i][j] * R3[j] for j in range(3)) == R2[i]
    for j in range(3):
        assert min(Q4[i, j]) > 0 and sum(Q4[i, j]) == 1
        assert sum(Q4[i, j][k] * R4[k] for k in range(3)) == R3[j]

def lift(g, u, choices):
    """choices[i][j] are arbitrary FULL_HIST time-3 continuations."""
    b = [[Q2[i] * Q3[i][j] * u[i] for j in range(3)] for i in range(2)]
    x = [[b[i][j] * choices[i][j] for j in range(3)] for i in range(2)]
    V = [sum(b[i][j] for i in range(2)) for j in range(3)]
    X = [sum(x[i][j] for i in range(2)) for j in range(3)]
    A, B = b[0][1], b[1][1]
    J = alpha * x[0][1] + beta * x[1][1]
    M = {r: F(0) for r in R}
    M[F(1)] += 1 - g
    for i in range(2):
        M[R2[i]] += Q2[i] * (g - u[i])
    for j in range(3):
        M[R3[j]] += V[j] - X[j]
    M[R4[0]] += F(509, 900) * X[0] + F(9, 900) * X[2] + J
    M[R4[1]] += F(382, 900) * (X[0] + X[2]) + X[1] - 2 * J
    M[R4[2]] += F(9, 900) * X[0] + F(509, 900) * X[2] + J
    TP = 1 + g + sum(Q2[i] * R2[i] * u[i] for i in range(2)) + sum(R3[j] * X[j] for j in range(3))
    TQ = 1 + g + sum(Q2[i] * u[i] for i in range(2)) + sum(X)
    assert sum(M.values()) == 1 and sum(r * M[r] for r in R) == 1
    assert all(m >= 0 for m in M.values())
    assert 0 <= u[0] <= g <= 1 and 0 <= u[1] <= g
    assert all(0 <= X[j] <= V[j] for j in range(3))
    assert max(alpha * X[1], beta * X[1] - delta * A) <= J
    assert J <= min(beta * X[1], alpha * X[1] + delta * B)
    direct = {r: F(0) for r in R}
    direct[F(1)] += 1 - g
    for i in range(2):
        direct[R2[i]] += Q2[i] * (g - u[i])
        for j in range(3):
            direct[R3[j]] += b[i][j] - x[i][j]
            for k in range(3):
                direct[R4[k]] += x[i][j] * Q4[i, j][k]
    assert direct == M
    defect = (A + B) * J - X[1] * (alpha * A + beta * B)
    assert defect == delta * A * B * (choices[1][1] - choices[0][1])
    return M, TP, TQ, defect, (V, X, J, A, B)

def errors(M, actions):
    eQ = sum(M[r] * actions[r] for r in R)
    eP = sum(r * M[r] * (1 - actions[r]) for r in R)
    for rho in R:
        low = 1 + sum((rho-r)*M[r] for r in R if r > rho)
        high = 1 + sum((rho-r)*M[r] for r in R if r < rho)
        assert low <= eP + rho * eQ <= high
    return eP, eQ

rnd = Random(113406)
count = 0
max_seen = F(0)
for case in range(600):
    g = [F(0), F(1), F(1, 2)][case] if case < 3 else F(rnd.randrange(21), 20)
    u = [g * F(rnd.randrange(21), 20) for _ in range(2)]
    z = [[F(rnd.randrange(21), 20) for _ in range(3)] for _ in range(2)]
    if case % 11 == 0: z[1][1] = z[0][1]
    M, TP, TQ, defect, (V, X, J, A, B) = lift(g, u, z)
    common = [[X[j] / V[j] if V[j] else F(0) for j in range(3)] for _ in range(2)]
    Mc, TPc, TQc, defect_c, data_c = lift(g, u, common)
    assert (TP, TQ) == (TPc, TQc) and defect_c == 0
    assert defect == 0 if A * B == 0 or z[0][1] == z[1][1] else defect != 0
    assert abs(J - data_c[2]) <= F(247, 23400)
    for r in R:
        if r not in R4: assert M[r] == Mc[r]
    policy = {r:F(rnd.randrange(21), 20) for r in R}
    eP, eQ = errors(M, policy)
    cp, cq = errors(Mc, policy)
    assert abs(eP-cp) <= F(247, 11700) and abs(eQ-cq) <= F(247, 11700)
    max_seen = max(max_seen, abs(eP-cp), abs(eQ-cq))
    count += 1

g = F(1); u = [F(1), F(1)]
z = [[F(0) for _ in range(3)] for _ in range(2)]
z[1][1] = F(1)
M, TP, TQ, defect, (V, X, J, A, B) = lift(g, u, z)
common = [[X[j] / V[j] if V[j] else F(0) for j in range(3)] for _ in range(2)]
Mc, TPc, TQc, defect_c, data_c = lift(g, u, common)
assert J - data_c[2] == F(247, 23400)
sharp_J_err = J - data_c[2]
actions = {r:F(0) for r in R}
actions[R4[0]] = actions[R4[2]] = F(1)
eP, eQ = errors(M, actions)
cp, cq = errors(Mc, actions)
assert eQ-cq == F(247, 11700)

# Reverse the four linear J bounds: every rational feasible lift reconstructs a FULL_HIST policy.
for case in range(360):
    g = F(rnd.randrange(21), 20)
    u = [g * F(rnd.randrange(21), 20) for _ in range(2)]
    b = [[Q2[i] * Q3[i][j] * u[i] for j in range(3)] for i in range(2)]
    V = [sum(b[i][j] for i in range(2)) for j in range(3)]
    X = [v * F(rnd.randrange(21), 20) for v in V]
    A, B = b[0][1], b[1][1]
    jl = max(alpha * X[1], beta * X[1] - delta * A)
    ju = min(beta * X[1], alpha * X[1] + delta * B)
    assert jl <= ju
    J = jl + (ju-jl) * F(rnd.randrange(21), 20)
    x01 = (beta * X[1] - J) / delta
    x11 = X[1] - x01
    assert 0 <= x01 <= A and 0 <= x11 <= B
    choices = [[X[j]/V[j] if V[j] else F(0) for j in range(3)] for _ in range(2)]
    choices[0][1] = x01/A if A else F(0)
    choices[1][1] = x11/B if B else F(0)
    M, TP, TQ, defect, data = lift(g,u,choices)
    assert data[1] == X and data[2] == J
    if V[1]:
        jcommon = X[1]*(alpha*A+beta*B)/V[1]
        assert (defect == 0) == (J == jcommon)
    else: assert defect == 0 and J == 0

print('PASS_EXACT_R5_SCALAR_NONLUMPABILITY_LIFT')
print('forward_cases=', count, 'reverse_lift_cases=', 360, 'ratios=', len(R), 'max_random_coordinate_deviation=', max_seen)
print('alpha=', alpha, 'beta=', beta, 'difference=', delta)
print('sharp_aggregate_J_error=', sharp_J_err, 'sharp_error_coordinate=', eQ-cq)
print('scalar_quadratic_defect_identity_verified; FULL polyhedral lift all 7+7 variables, LR adds one quadratic gate')
